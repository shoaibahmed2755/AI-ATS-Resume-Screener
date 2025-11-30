import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
import google.generativeai as genai

from core.parsing import extract_text
from core.jd_processing import analyze_job_description
from core.embeddings import get_resume_embedding, get_jd_embedding
from core.scoring import compute_score
from core.explain import generate_feedback

# ------- Load API -------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ------- Page Setup -------
st.set_page_config(page_title="Resume Screening ATS", layout="wide")

# ------- Custom CSS -------
st.markdown("""
<style>

body {
    background-color: #0f172a;
}

[data-testid="stAppViewContainer"] {
    background-color: #0f172a;
}

h1 {
    font-size: 40px;
    font-weight: 900;
}

.section-box {
    padding: 22px;
    border-radius: 14px;
    background: #1e293b;
    border: 1px solid #334155;
}

.upload-area {
    border: 2px dashed #3b82f6;
    padding: 30px;
    text-align: center;
    border-radius: 15px;
    color: #cbd5e1;
}

.stButton > button {
    width: 100%;
    height: 52px;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
}

.analyze-btn {
    background: #3b82f6 !important;
    color: white !important;
}

.run-btn {
    background: #10b981 !important;
    color: white !important;
}

.stSlider > div {
    padding: 8px 0 !important;
}

.success-box {
    background: #063f2f;
    padding: 15px;
    border-radius: 10px;
    font-weight: bold;
    color: #90EE90;
}

.error-box {
    background: #401010;
    padding: 15px;
    border-radius: 10px;
    color: #ffb3b3;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ------- HEADER -------
col1, col2 = st.columns([7,3])
with col1:
    st.markdown("### <span style='color:white;'>🧠 Resume Screening ATS</span>", unsafe_allow_html=True)
with col2:
    st.markdown("<div style='text-align:right; color:#3b82f6;'>Powered by Gemini 2.5 Flash ⚡</div>", unsafe_allow_html=True)

st.write("")

# ------- SIDEBAR -------
with st.sidebar:
    st.markdown("### 🎛 Score Weights")

    weights = {
        "skills": st.slider("Skills Match", 0.0, 1.0, 0.5),
        "experience": st.slider("Experience", 0.0, 1.0, 0.3),
        "ats": st.slider("ATS Keywords", 0.0, 1.0, 0.1),
        "soft": st.slider("Soft Skills", 0.0, 1.0, 0.1),
    }

    total_weight = sum(weights.values())
    st.progress(total_weight)

    st.markdown(f"**Total Weight: {int(total_weight * 100)}%**")

# ------- MAIN INPUT UI -------
jd_area = st.container()
with jd_area:
    st.markdown("### 📄 Job Description", unsafe_allow_html=True)
    job_description = st.text_area(
        "Paste job description here...",
        placeholder="Include job title, skills, qualifications...",
        height=170
    )

# ------- Resume Upload ------
st.markdown("### 📤 Upload Resumes")
uploaded_files = st.file_uploader(
    "Drag and drop or click to upload (PDF/DOC/DOCX/TXT)",
    accept_multiple_files=True,
)


# ------- Analyze Job Description -------
if st.button("Analyze Job Description", type="primary"):
    if job_description.strip():
        with st.spinner("Analyzing with Gemini..."):
            result = analyze_job_description(job_description)

        if "error" in result:
            st.markdown(f"<div class='error-box'>❌ JSON Parse Error — Showing raw output:<br><br>{result['raw_output']}</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='success-box'>🎯 Job Description Successfully Parsed!</div>", unsafe_allow_html=True)
            st.json(result)
    else:
        st.markdown("<div class='error-box'>⚠ Please enter a job description first.</div>", unsafe_allow_html=True)


# ------- Run Full Screening -------
if st.button("Run Screening 👇", type="primary"):
    if not uploaded_files or not job_description:
        st.markdown("<div class='error-box'>⚠ Upload resumes and enter JD first!</div>", unsafe_allow_html=True)
    else:
        st.info("🔍 Processing resumes...")

        jd_emb = get_jd_embedding(job_description)
        results = []

        for file in uploaded_files:
            text = extract_text(file)
            res_emb = get_resume_embedding(text)

            score, breakdown = compute_score(text, jd_emb, weights, res_emb)
            feedback = generate_feedback(text, job_description, breakdown)

            results.append({"Candidate": file.name, "Score": score})

            with st.expander(f"📌 {file.name} — Score: {score}%"):
                st.write(feedback)
                st.json(breakdown)

        df = pd.DataFrame(results).sort_values("Score", ascending=False)
        st.subheader("🏆 Ranking Results")
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇ Download Results", csv, "ATS-results.csv", "text/csv")

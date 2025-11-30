@echo off
powershell -command ^
"@'
# 🤖 AI Resume Screening ATS
AI-powered Applicant Tracking System that evaluates resumes against job descriptions, calculates ATS compatibility, ranks candidates, and provides improvement feedback.
Built with **Python**, **Streamlit**, **Gemini AI**, and **NLP embeddings**.

# 📊 AI Resume Screening — Smart Hiring Dashboard

![ATS Banner](https://img.freepik.com/free-vector/data-analysis-concept-illustration_114360-8462.jpg)

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)]() [![Streamlit](https://img.shields.io/badge/Streamlit-2.0-red?logo=streamlit)]() [![Gemini AI](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-black?logo=google)]() [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🌐 Live Demo
👉 COMING SOON

---

## 🧠 About the Project
**AI Resume Screening ATS** helps users:

- Upload and analyze **multiple resumes**
- Extract content from **PDF / DOCX / TXT**
- Compare resumes with a given **Job Description**
- Generate **ATS match score**
- Get **personalized improvement feedback**
- Download ranked **CSV reports**

Perfect for:
- Recruiters
- HR Teams
- Job Seekers
- Hiring Platforms

---

## 🚀 Features
- 📂 Multi-resume upload
- 🧠 Gemini-powered JD extraction
- 🎯 ATS similarity scoring
- 📊 Ranking leaderboard table
- 📝 Candidate improvement suggestions
- ⬇ Export final report (.csv)
- 📈 Visualization using Matplotlib

---

## 🖼️ Screenshots

| Dashboard | Resume Analysis | Score Visualization |
|-----------|----------------|---------------------|
| *(coming soon)* | *(coming soon)* | *(coming soon)* |

---

## 🧩 Project Structure
```
AI-ATS/
│
├── app.py
├── requirements.txt
├── .env
│
└── core/
├── parsing.py
├── jd_processing.py
├── embeddings.py
├── scoring.py
└── explain.py
```

---

## ⚙️ Installation
git clone https://github.com/YOUR-USERNAME/AI-ATS.git
cd AI-ATS
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

yaml
Copy code

Open browser:
👉 http://localhost:8501

---

## 🛠️ Built With

- Python 3.10+
- Streamlit
- Google Gemini API
- Pandas
- Matplotlib
- PDF / DOCX parsing

---

## 🤝 Contributing
git fork https://github.com/shoaibahmed2755/AI-ATS.git
git checkout -b feature-name
git commit -m "Add new feature"
git push origin feature-name

yaml
Copy code
Submit a pull request 🚀

---

## 📜 License
MIT License

---

### 🤖 AI Resume Screening ATS — Smarter Hiring Starts Here
> *"Not just matching keywords — understanding candidates."*

---

# Commit and Push
git add README.md
git commit -m "Added full README with details"
git push origin main

vbnet
Copy code
'@ | Set-Content README.md"

echo 📄 README.md successfully created!

from .embeddings import similarity

def compute_score(resume_text, jd_emb, weights, resume_emb):
    sim = similarity(resume_emb, jd_emb)

    skill_score = sim * weights["skills"]
    exp_score = 0.75 * weights["experience"]
    ats_score = 0.60 * weights["ats"]
    soft_score = 0.55 * weights["soft"]

    final_score = (skill_score + exp_score + ats_score + soft_score) * 100

    breakdown = {
        "Skill Match Score": round(skill_score, 2),
        "Experience Score": round(exp_score, 2),
        "ATS Score": round(ats_score, 2),
        "Soft Skills Score": round(soft_score, 2),
        "Similarity Value": round(sim, 3)
    }

    return round(final_score, 2), breakdown

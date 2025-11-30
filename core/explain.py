import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL = "models/gemini-2.5-flash"

def generate_feedback(resume, jd, breakdown):
    prompt = f"""
Compare this resume to the job description and based on the breakdown:

Resume:
{resume}

Job Description:
{jd}

Score Breakdown:
{breakdown}

Write the following sections:

1. Summary (3-4 sentences)
2. Strengths (bullet points)
3. Weaknesses (bullet points)
4. Recommendation: Hire / Consider / Reject
5. Suggested 5 interview questions
"""

    response = genai.GenerativeModel(MODEL).generate_content(prompt)
    return response.text

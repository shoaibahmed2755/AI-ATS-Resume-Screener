import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL = "models/gemini-2.5-flash"

def extract_json(text: str):
    """Extracts clean JSON from model output, even if wrapped in markdown."""
    
    # Remove markdown fences
    text = re.sub(r"```(json)?", "", text, flags=re.IGNORECASE).strip("` \n")

    # Find the first JSON object
    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        return match.group(0)
    
    return None


def analyze_job_description(jd_text):
    prompt = f"""
You MUST respond with ONLY valid JSON. No explanation. No quotes. No markdown. No bullet points.

#### REQUIRED OUTPUT FORMAT ####

{{
  "RoleTitle": "",
  "RequiredSkills": [],
  "OptionalSkills": [],
  "MinExperienceYears": 0,
  "MaxExperienceYears": 0,
  "Responsibilities": [],
  "TopKeywords": []
}}

JOB DESCRIPTION:
{jd_text}
"""

    response = genai.GenerativeModel(MODEL).generate_content(prompt)
    raw = response.text.strip()

    cleaned = extract_json(raw)

    if cleaned:
        try:
            return json.loads(cleaned)
        except Exception:
            return {"error": "JSON parsing failed", "raw_output": raw}

    return {"error": "No JSON found in response", "raw_output": raw}

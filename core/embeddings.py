import google.generativeai as genai
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

EMBED_MODEL = "models/text-embedding-004"

def get_resume_embedding(text):
    res = genai.embed_content(model=EMBED_MODEL, content=text)
    return res['embedding']

def get_jd_embedding(text):
    res = genai.embed_content(model=EMBED_MODEL, content=text)
    return res['embedding']

def similarity(v1, v2):
    v1, v2 = np.array(v1), np.array(v2)
    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

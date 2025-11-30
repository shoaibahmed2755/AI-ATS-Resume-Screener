import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

models = genai.list_models()

print("\n🚀 AVAILABLE MODELS FOR YOUR API KEY:\n")
for m in models:
    print("-", m.name)

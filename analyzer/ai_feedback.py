import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Get the API key from .env file
api_key = os.getenv("GEMINI_API_KEY")

# Create the client only if we have a key, so the app does not crash on startup
if api_key:
    client = genai.Client(api_key=api_key)
else:
    client = None


def generate_ai_feedback(resume_text):
    if client is None:
        return "AI feedback is unavailable right now (no API key configured)."

    prompt = f"""
Look at this resume and give SHORT, SIMPLE feedback. A student should be able
to read the whole thing in under one minute.

Give exactly:
1. Strengths - 3 short points
2. Weaknesses - 3 short points
3. Missing Skills - 3 short points
4. ATS Improvements - 3 short points

Rules:
- Each point must be ONE short sentence.
- Use simple, everyday words. No long or complex sentences.
- Plain text only. Do not use markdown symbols like ** or #.

Resume:
{resume_text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print("Gemini error:", e)
        return "AI feedback is temporarily unavailable. Please try again in a moment."
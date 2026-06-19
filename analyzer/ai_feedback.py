import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_ai_feedback(resume_text):

    prompt = f"""
    Analyze this resume.

    Give:
    1. Strengths
    2. Weaknesses
    3. Missing Skills
    4. ATS Improvements

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)

    return response.text
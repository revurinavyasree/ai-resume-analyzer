from analyzer.gemini_helper import ask_gemini_json

fallback_recommendations = [
    "Add measurable results to your project bullet points (example: improved speed by 20%).",
    "Add a short professional summary near the top of your resume.",
    "Add your GitHub and LinkedIn links near your contact details.",
    "Use strong action words like built, designed, optimized instead of plain wording.",
    "Keep your resume to one page if you are a student or fresher.",
]


def generate_recommendations(resume_text, detected_skills):
    if detected_skills:
        skills_text = ", ".join(detected_skills)
    else:
        skills_text = "no specific skills detected"

    # Only send first 3000 characters so the prompt does not get too long
    if resume_text:
        trimmed_text = resume_text[:3000]
    else:
        trimmed_text = ""

    prompt = f"""Here is my resume text:
{trimmed_text}

My detected skills: {skills_text}

Give me 5 specific tips to improve this resume for both ATS systems and recruiters.
Reply only in JSON like this, nothing else:
{{"recommendations": ["tip 1", "tip 2", "tip 3", "tip 4", "tip 5"]}}"""

    result = ask_gemini_json(prompt)

    if result and "recommendations" in result:
        return result["recommendations"]

    return fallback_recommendations
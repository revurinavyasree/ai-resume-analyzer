from analyzer.gemini_helper import ask_gemini, ask_gemini_json


def generate_ai_summary(detected_skills, ats_score, resume_text):
    if detected_skills:
        skills_text = ", ".join(detected_skills)
    else:
        skills_text = "no specific skills"

    # Trim so the prompt does not get too long
    trimmed_text = (resume_text or "")[:3000]

    prompt = f"""Here is my resume text:
{trimmed_text}

My detected skills: {skills_text}
My ATS score: {ats_score}/100

Write a short 2-3 sentence summary about my profile, based on what is actually
in my resume (my projects, education, and skills), and one tip to improve my resume.
Plain text only, no markdown."""

    result = ask_gemini(prompt)

    if result:
        return result.strip()

    # If Gemini did not work, use a simple fallback message
    return (
        f"You have {len(detected_skills)} skills detected and an ATS score of "
        f"{ats_score}/100. Try adding more achievements with numbers to improve your resume."
    )


def recommend_careers(detected_skills, resume_text):
    if detected_skills:
        skills_text = ", ".join(detected_skills)
    else:
        skills_text = "general technical skills"

    trimmed_text = (resume_text or "")[:3000]

    prompt = f"""Here is my resume text:
{trimmed_text}

My detected skills: {skills_text}

Based on my actual projects, education, and skills above (not just the skill list),
suggest 3 job roles suitable for me.
Reply only in JSON like this, nothing else:
{{"careers": [{{"role": "Role Name", "reason": "short reason based on my actual resume"}}]}}"""

    result = ask_gemini_json(prompt)

    if result and "careers" in result:
        return result["careers"]

    # Fallback list if Gemini did not work
    return [
        {"role": "Software Developer", "reason": "Matches your technical skills"},
        {"role": "QA Engineer", "reason": "Good fit for detail oriented work"},
        {"role": "Technical Analyst", "reason": "Suits an analytical background"},
    ]


def skill_gap_analysis(detected_skills, resume_text):
    if detected_skills:
        skills_text = ", ".join(detected_skills)
    else:
        skills_text = "no specific skills"

    trimmed_text = (resume_text or "")[:3000]

    prompt = f"""Here is my resume text:
{trimmed_text}

My detected skills: {skills_text}

Based on my actual projects and the kind of roles they point toward (not just the
skill list), suggest 4 additional skills I should learn to get a better job.
Reply only in JSON like this, nothing else:
{{"gaps": [{{"skill": "Skill Name", "reason": "short reason based on my actual resume"}}]}}"""

    result = ask_gemini_json(prompt)

    if result and "gaps" in result:
        return result["gaps"]

    # Fallback list if Gemini did not work
    return [
        {"skill": "Git/GitHub", "reason": "Used in almost every coding job"},
        {"skill": "Cloud basics (AWS/GCP)", "reason": "Most companies use cloud now"},
        {"skill": "REST API", "reason": "Needed for backend and full stack roles"},
        {"skill": "Unit Testing", "reason": "Expected in good quality code"},
    ]
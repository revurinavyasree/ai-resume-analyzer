def generate_ai_summary(skills, ats_score):

    top_skills = ", ".join(skills[:6])

    if ats_score >= 80:
        return (
            f"This resume demonstrates a strong technical foundation "
            f"with expertise in {top_skills}. "
            f"The candidate appears suitable for software development, "
            f"backend engineering and AI-related fresher opportunities."
        )

    elif ats_score >= 60:
        return (
            f"The resume showcases skills in {top_skills}. "
            f"The candidate has good placement potential but can improve "
            f"by adding advanced projects and industry-relevant technologies."
        )

    return (
        f"The resume includes skills such as {top_skills}. "
        f"Additional projects, certifications and technical depth "
        f"would improve hiring potential."
    )


def recommend_careers(skills):

    skills = [s.lower().strip() for s in skills]

    careers = []

    if "python" in skills:
        careers.append("Python Developer")

    if "machine learning" in skills:
        careers.append("AI/ML Engineer")

    if "sql" in skills or "mysql" in skills:
        careers.append("Data Analyst")

    if "flask" in skills:
        careers.append("Backend Developer")

    if "html" in skills and "css" in skills:
        careers.append("Frontend Developer")

    if "javascript" in skills:
        careers.append("Full Stack Developer")

    return list(set(careers))


def skill_gap_analysis(skills):

    skills = [s.lower().strip() for s in skills]

    suggestions = []

    if "aws" not in skills:
        suggestions.append("AWS Cloud")

    if "docker" not in skills:
        suggestions.append("Docker")

    if "rest api" not in skills:
        suggestions.append("REST APIs")

    if "mongodb" not in skills:
        suggestions.append("MongoDB")

    if "react" not in skills:
        suggestions.append("React")

    if "linux" not in skills:
        suggestions.append("Linux")

    return suggestions
def predict_role(skills):

    skills = [s.lower().strip() for s in skills]

    if (
        "machine learning" in skills
        or "deep learning" in skills
        or "tensorflow" in skills
        or "pandas" in skills
    ):
        return "AI / ML Engineer"

    if (
        "react" in skills
        and "javascript" in skills
        and "html" in skills
    ):
        return "Frontend Developer"

    if (
        "flask" in skills
        or "django" in skills
    ):
        return "Backend Developer"

    if (
        "aws" in skills
        or "docker" in skills
        or "linux" in skills
    ):
        return "Cloud Engineer"

    if "sql" in skills:
        return "Data Analyst"

    return "Software Engineer"
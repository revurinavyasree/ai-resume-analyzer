def analyze_resume(text, skills):

    strengths = []
    weaknesses = []

    text_lower = text.lower()

    # Technical depth
    if len(skills) >= 10:
        strengths.append(
            "Excellent technical profile with diverse technologies."
        )
    elif len(skills) >= 7:
        strengths.append(
            "Good technical skill coverage for fresher opportunities."
        )

    # Projects
    project_count = text_lower.count("project")

    if project_count >= 3:
        strengths.append(
            "Multiple projects demonstrate practical implementation ability."
        )
    elif project_count >= 1:
        strengths.append(
            "Project experience present."
        )
    else:
        weaknesses.append(
            "No projects found."
        )

    # Internship
    if "internship" in text_lower:
        strengths.append(
            "Internship experience improves employability."
        )
    else:
        weaknesses.append(
            "No internship experience detected."
        )

    # GitHub
    if "github" in text_lower:
        strengths.append(
            "GitHub profile available for recruiter verification."
        )
    else:
        weaknesses.append(
            "GitHub profile missing."
        )

    # LinkedIn
    if "linkedin" in text_lower:
        strengths.append(
            "LinkedIn profile present."
        )
    else:
        weaknesses.append(
            "LinkedIn profile missing."
        )

    # Certifications
    cert_count = (
        text_lower.count("certification")
        + text_lower.count("certified")
    )

    if cert_count >= 2:
        strengths.append(
            "Multiple certifications strengthen the profile."
        )
    elif cert_count == 0:
        weaknesses.append(
            "No certifications detected."
        )

    # Cloud skills
    cloud = [
        "aws",
        "azure",
        "gcp",
        "docker"
    ]

    if any(c in skills for c in cloud):
        strengths.append(
            "Cloud/DevOps skills detected."
        )
    else:
        weaknesses.append(
            "No cloud technologies detected."
        )

    # Action verbs
    verbs = [
        "developed",
        "built",
        "implemented",
        "designed",
        "automated",
        "optimized",
        "deployed"
    ]

    count = sum(
        1 for v in verbs
        if v in text_lower
    )

    if count >= 3:
        strengths.append(
            "Strong action-oriented resume language."
        )
    else:
        weaknesses.append(
            "Use stronger action verbs in project descriptions."
        )

    return strengths, weaknesses
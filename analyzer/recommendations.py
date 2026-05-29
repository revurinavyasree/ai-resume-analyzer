CORE_SKILLS = ["python", "java", "sql", "git", "dsa", "oops"]
CLOUD_SKILLS = ["aws", "azure", "gcp", "docker"]
DATA_SKILLS  = ["machine learning", "data analysis", "power bi", "tableau"]
WEB_SKILLS   = ["html", "css", "javascript", "react"]


def generate_recommendations(text, skills):
    recommendations = []
    text_lower = text.lower()
    skills_lower = [s.lower() for s in skills]

    # --- Profile completeness ---
    if "github" not in text_lower:
        recommendations.append(
            "Add your GitHub profile link — all service-based companies check it during shortlisting."
        )
    if "linkedin" not in text_lower:
        recommendations.append(
            "Add your LinkedIn profile URL — recruiters at TCS, Infosys, and Accenture actively use it."
        )
    if "summary" not in text_lower and "objective" not in text_lower:
        recommendations.append(
            "Add a 2–3 line career objective at the top tailored to IT service roles."
        )

    # --- Experience & projects ---
    if "internship" not in text_lower:
        recommendations.append(
            "No internship found — add any internship or training (even virtual ones from NPTEL, Infosys Springboard, or TCS iON)."
        )
    if "project" not in text_lower:
        recommendations.append(
            "Add at least 2 projects with tech stack, your role, and a GitHub link."
        )
    elif text_lower.count("project") < 2:
        recommendations.append(
            "Try to include at least 2 projects — one individual and one team-based."
        )

    # --- Certifications ---
    if "certification" not in text_lower and "certified" not in text_lower:
        recommendations.append(
            "Add certifications — AWS Cloud Practitioner, Google IT Support, or Infosys Springboard courses are highly valued by service companies."
        )

    # --- Core skill gaps ---
    missing_core = [s for s in CORE_SKILLS if s not in skills_lower]
    if missing_core:
        recommendations.append(
            f"Strengthen these core skills that service companies test: {', '.join(missing_core)}."
        )

    # --- Cloud skills ---
    if not any(s in skills_lower for s in CLOUD_SKILLS):
        recommendations.append(
            "Add at least one cloud skill (AWS, Azure, or GCP) — all major IT companies are cloud-first now."
        )

    # --- Skill count ---
    if len(skills) < 6:
        recommendations.append(
            "Your resume shows fewer than 6 skills — expand your skills section with languages, tools, and frameworks you know."
        )

    # --- Action verbs ---
    verbs = ["developed", "built", "designed", "implemented", "automated",
             "optimized", "deployed", "created", "managed", "tested"]
    used_verbs = [v for v in verbs if v in text_lower]
    if len(used_verbs) < 3:
        recommendations.append(
            "Use strong action verbs in your project descriptions: 'Developed', 'Built', 'Automated', 'Deployed', etc."
        )

    # --- Education section ---
    if "cgpa" not in text_lower and "gpa" not in text_lower and "percentage" not in text_lower:
        recommendations.append(
            "Mention your CGPA or percentage — TCS, Infosys, and Wipro have minimum cutoffs (usually 60% or 6.0 CGPA)."
        )

    # --- Soft skills ---
    if "communication" not in text_lower and "teamwork" not in text_lower:
        recommendations.append(
            "Mention soft skills like communication and teamwork — service companies heavily evaluate these in HR rounds."
        )

    return recommendations
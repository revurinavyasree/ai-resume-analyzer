def calculate_ats_score(text, skills):

    score = 0
    text_lower = text.lower()

    # 1. Skill score (max 30 points)
    skill_points = min(len(skills) * 3, 30)
    score += skill_points

    # 2. Resume sections (5 points each)
    sections = [
        "education",
        "skills",
        "projects",
        "internship",
        "certifications",
        "achievements",
        "objective",
        "summary",
    ]
    for section in sections:
        if section in text_lower:
            score += 5

    # 3. Action verbs (2 points each, max 10)
    action_verbs = [
        "developed", "created", "designed", "implemented",
        "built", "optimized", "automated", "deployed",
        "managed", "collaborated", "achieved", "improved",
        "analysed", "tested", "integrated",
    ]
    verb_points = 0
    for verb in action_verbs:
        if verb in text_lower:
            verb_points += 2
    score += min(verb_points, 10)

    # 4. Fresher essentials (bonus points)
    if "github" in text_lower or "github.com" in text_lower:
        score += 5
    if "linkedin" in text_lower or "linkedin.com" in text_lower:
        score += 3
    if "project" in text_lower:
        score += 5
    if "internship" in text_lower:
        score += 7
    if "certification" in text_lower or "certified" in text_lower:
        score += 5

    return min(score, 100)
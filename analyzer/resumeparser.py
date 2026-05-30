import re


def parse_resume_sections(text):
    """
    Parse raw resume text into structured sections.
    Returns a dict with name, email, phone, linkedin, github,
    objective, education, skills, projects, experience,
    certifications, achievements, areas_of_interest
    """
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    result = {
        "name":              "",
        "email":             "",
        "phone":             "",
        "linkedin":          "",
        "github":            "",
        "objective":         [],
        "education":         [],
        "skills":            [],
        "projects":          [],
        "experience":        [],
        "certifications":    [],
        "achievements":      [],
        "areas_of_interest": [],
    }

    # ── Contact info ──────────────────────────────────────────────
    email_re   = re.compile(r'[\w.+-]+@[\w-]+\.[a-zA-Z]{2,4}')
    phone_re   = re.compile(r'(\+91[\s-]?)?[6-9]\d{9}')
    linkedin_re= re.compile(r'linkedin\.com/in/[\w\-]+', re.I)
    github_re  = re.compile(r'github\.com/[\w\-]+', re.I)

    for line in lines[:15]:   # contact info usually in first 15 lines
        if not result["email"] and email_re.search(line):
            result["email"] = email_re.search(line).group()
        if not result["phone"] and phone_re.search(line):
            result["phone"] = phone_re.search(line).group()
        if not result["linkedin"] and linkedin_re.search(line):
            result["linkedin"] = linkedin_re.search(line).group()
        if not result["github"] and github_re.search(line):
            result["github"] = github_re.search(line).group()

    # First non-contact line is likely the name
    for line in lines[:5]:
        if (not email_re.search(line) and
            not phone_re.search(line) and
            not linkedin_re.search(line) and
            not github_re.search(line) and
            len(line.split()) <= 5 and
            len(line) > 2):
            result["name"] = line
            break

    # ── Section detection ─────────────────────────────────────────
    SECTION_KEYWORDS = {
        "objective":         ["objective", "summary", "about me", "profile"],
        "education":         ["education", "academic", "qualification"],
        "skills":            ["skill", "technical skill", "technologies"],
        "projects":          ["project", "personal project"],
        "experience":        ["experience", "work experience", "internship", "employment"],
        "certifications":    ["certification", "certificate", "course"],
        "achievements":      ["achievement", "award", "accomplishment", "activity"],
        "areas_of_interest": ["area of interest", "interest", "hobbies"],
    }

    def detect_section(line):
        line_lower = line.lower().strip()
        for section, keywords in SECTION_KEYWORDS.items():
            for kw in keywords:
                if kw in line_lower and len(line_lower) < 40:
                    return section
        return None

    current_section = None
    for line in lines:
        section = detect_section(line)
        if section:
            current_section = section
            continue

        if current_section and line not in [result["name"],
                                             result["email"],
                                             result["phone"]]:
            if current_section in result:
                result[current_section].append(line)

    # Clean up — convert lists to strings where needed
    result["objective"] = " ".join(result["objective"][:5])

    return result
def analyze_resume(text, skills):
    strengths  = []
    weaknesses = []
    text_lower = text.lower()

    # --- Strengths ---
    if len(skills) >= 8:
        strengths.append("Strong technical skill set — covers multiple domains.")
    elif len(skills) >= 5:
        strengths.append("Good range of technical skills for a fresher profile.")

    if "internship" in text_lower:
        strengths.append("Has internship experience — a major plus for service-based shortlisting.")

    if "project" in text_lower:
        strengths.append("Projects section present — shows practical application of skills.")

    if "github" in text_lower or "github.com" in text_lower:
        strengths.append("GitHub profile linked — demonstrates coding activity to recruiters.")

    if "certification" in text_lower or "certified" in text_lower:
        strengths.append("Certifications listed — valued by TCS, Infosys, Wipro hiring teams.")

    if "linkedin" in text_lower:
        strengths.append("LinkedIn profile included — improves recruiter discoverability.")

    if any(v in text_lower for v in ["developed", "built", "implemented", "deployed", "automated"]):
        strengths.append("Uses strong action verbs — resume reads as achievement-oriented.")

    if "cgpa" in text_lower or "percentage" in text_lower or "gpa" in text_lower:
        strengths.append("Academic score mentioned — important for service company eligibility cutoffs.")

    if "communication" in text_lower or "teamwork" in text_lower:
        strengths.append("Soft skills highlighted — relevant for HR and managerial rounds.")

    # --- Weaknesses ---
    if "internship" not in text_lower:
        weaknesses.append("No internship experience — consider virtual internships or training programs.")

    if "github" not in text_lower:
        weaknesses.append("GitHub profile missing — most service companies check this during tech screening.")

    if "summary" not in text_lower and "objective" not in text_lower:
        weaknesses.append("No career objective or summary — add 2–3 lines at the top of the resume.")

    if "project" not in text_lower:
        weaknesses.append("No projects found — projects are critical for freshers with no work experience.")

    if "certification" not in text_lower and "certified" not in text_lower:
        weaknesses.append("No certifications — free certs from AWS, Google, or Infosys Springboard add credibility.")

    if len(skills) < 5:
        weaknesses.append("Too few skills detected — expand the skills section with tools and technologies you know.")

    if "cgpa" not in text_lower and "percentage" not in text_lower and "gpa" not in text_lower:
        weaknesses.append("Academic score not mentioned — TCS, Wipro, and Infosys have minimum eligibility criteria.")

    if "linkedin" not in text_lower:
        weaknesses.append("LinkedIn URL missing — add it to improve recruiter reach.")

    return strengths, weaknesses
COMPANIES = {

    # Indian IT giants
    "TCS": {
        "required": ["python", "java", "sql", "git", "oops"],
        "bonus":    ["dbms", "networking", "os", "agile", "communication"],
        "roles":    "Software Engineer / ASE (Associate Software Engineer)",
    },
    "Infosys": {
        "required": ["python", "java", "dbms", "dsa", "sql"],
        "bonus":    ["spring", "rest api", "linux", "agile", "communication"],
        "roles":    "Systems Engineer / Technology Analyst",
    },
    "Wipro": {
        "required": ["java", "oops", "sql", "git", "python"],
        "bonus":    ["c++", "networking", "os", "docker", "communication"],
        "roles":    "Project Engineer / Software Developer",
    },
    "HCL Technologies": {
        "required": ["java", "python", "sql", "git", "oops"],
        "bonus":    ["aws", "linux", "agile", "rest api", "communication"],
        "roles":    "Graduate Engineer Trainee",
    },
    "Tech Mahindra": {
        "required": ["python", "java", "sql", "networking", "git"],
        "bonus":    ["aws", "docker", "agile", "communication", "linux"],
        "roles":    "Software Engineer / Associate",
    },

    # Global service companies
    "Accenture": {
        "required": ["python", "git", "apis", "sql", "agile"],
        "bonus":    ["aws", "docker", "react", "communication", "teamwork"],
        "roles":    "Associate Software Engineer",
    },
    "Cognizant": {
        "required": ["html", "css", "javascript", "sql", "git"],
        "bonus":    ["react", "python", "bootstrap", "communication", "agile"],
        "roles":    "Programmer Analyst Trainee",
    },
    "Capgemini": {
        "required": ["python", "java", "sql", "git", "oops"],
        "bonus":    ["aws", "agile", "communication", "linux", "rest api"],
        "roles":    "Analyst / Software Engineer",
    },

    # Consulting / Big 4 tech arms
    "IBM": {
        "required": ["python", "sql", "git", "linux", "apis"],
        "bonus":    ["aws", "docker", "machine learning", "agile", "communication"],
        "roles":    "Associate / Application Developer",
    },
    "Deloitte": {
        "required": ["python", "sql", "excel", "git", "communication"],
        "bonus":    ["power bi", "tableau", "aws", "agile", "teamwork"],
        "roles":    "Analyst / Technology Consultant",
    },
    "EY (Ernst and Young)": {
        "required": ["python", "sql", "excel", "communication", "git"],
        "bonus":    ["power bi", "tableau", "agile", "teamwork", "problem solving"],
        "roles":    "Technology Consultant / Analyst",
    },
}


def company_match(skills):
    results = {}
    skills_lower = [s.lower() for s in skills]

    for company, data in COMPANIES.items():
        required = data["required"]
        bonus    = data["bonus"]

        required_matched = sum(1 for s in required if s in skills_lower)
        bonus_matched    = sum(1 for s in bonus    if s in skills_lower)

        # Required skills = 70% of score, bonus = 30%
        required_score = (required_matched / len(required)) * 70
        bonus_score    = (bonus_matched    / len(bonus))    * 30

        total = round(required_score + bonus_score)

        results[company] = {
            "score": total,
            "role":  data["roles"],
            "required_matched": required_matched,
            "required_total":   len(required),
        }

    # Sort by score descending
    results = dict(
        sorted(results.items(), key=lambda x: x[1]["score"], reverse=True)
    )
    return results
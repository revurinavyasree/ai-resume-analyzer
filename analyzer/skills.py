SKILLS = [
    # Programming languages
    "python", "java", "c", "c++", "c#", "r", "scala",

    # Web
    "html", "css", "javascript", "typescript", "react", "angular", "vue",
    "bootstrap", "tailwind",

    # Backend / frameworks
    "flask", "django", "spring", "springboot", "nodejs", "express",

    # Database
    "sql", "mysql", "postgresql", "mongodb", "oracle", "sqlite",
    "dbms", "nosql",

    # Cloud & DevOps
    "aws", "azure", "gcp", "docker", "kubernetes", "jenkins",
    "git", "github", "gitlab", "linux", "bash",

    # Data & AI
    "machine learning", "deep learning", "data analysis", "pandas",
    "numpy", "matplotlib", "scikit-learn", "tensorflow", "keras",
    "power bi", "tableau", "excel",

    # Core CS concepts
    "dsa", "oops", "os", "networking", "apis", "rest api",
    "microservices", "agile", "scrum",

    # Soft / certifications keywords
    "communication", "teamwork", "problem solving",
    "aws certified", "azure certified", "google certified",
]


def detect_skills(text):
    detected = []
    text_lower = text.lower()
    for skill in SKILLS:
        if skill in text_lower:
            detected.append(skill)
    return detected
TARGET_ROLES = {

    "Software Engineer": [
        "python",
        "java",
        "sql",
        "git",
        "dsa",
        "oops"
    ],

    "Frontend Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "git"
    ],

    "Backend Developer": [
        "python",
        "flask",
        "sql",
        "git"
    ],

    "Data Scientist": [
        "python",
        "pandas",
        "numpy",
        "machine learning",
        "sql"
    ],

    "Cloud Engineer": [
        "aws",
        "docker",
        "linux",
        "git"
    ]
}


def analyze_skill_gap(
    skills,
    role
):

    skills = [s.lower() for s in skills]

    required = TARGET_ROLES.get(role, [])

    missing = [
        s
        for s in required
        if s not in skills
    ]

    return missing
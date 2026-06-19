def generate_project_questions(projects):

    project_text = " ".join(projects).lower()

    questions = []

    questions.extend([
        "Explain your project architecture.",
        "What challenges did you face during development?",
        "What was your contribution in the project?",
        "How would you improve this project in future?"
    ])

    if "flask" in project_text:
        questions.extend([
            "Why did you choose Flask?",
            "Explain Flask routing.",
            "How did you connect Flask with database?"
        ])

    if "machine learning" in project_text:
        questions.extend([
            "Which machine learning algorithm did you use?",
            "What is overfitting?",
            "How did you evaluate model performance?"
        ])

    if "python" in project_text:
        questions.extend([
            "Why did you choose Python?",
            "Which Python libraries were used?"
        ])

    if "sql" in project_text or "mysql" in project_text:
        questions.extend([
            "Explain your database design.",
            "How did you optimize queries?"
        ])

    return list(dict.fromkeys(questions))
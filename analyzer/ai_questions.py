def generate_ai_questions(skills, projects=[]):

    questions = []

    for skill in skills:

        if skill.lower() == "python":
            questions.append(
                "Explain the difference between list and tuple in Python."
            )

        elif skill.lower() == "sql":
            questions.append(
                "What is the difference between WHERE and HAVING?"
            )

        elif skill.lower() == "machine learning":
            questions.append(
                "What is overfitting in Machine Learning?"
            )

        elif skill.lower() == "flask":
            questions.append(
                "How does Flask routing work?"
            )

    questions.append(
        "Tell me about yourself."
    )

    questions.append(
        "Why should we hire you?"
    )

    return questions[:15]
from analyzer.gemini_helper import ask_gemini_json

fallback_questions = [
    "Can you explain the architecture of this project?",
    "What challenges did you face during development?",
    "What was your contribution to this project?",
    "How would you improve this project in the future?",
    "Why did you choose this technology stack?"
]


def generate_project_questions(projects):

    if not projects:
        return []

    projects_text = "\n".join(projects[:10])

    prompt = f"""
Here are project descriptions from my resume:

{projects_text}

Generate 5  technical interview questions.

Focus on:
- architecture
- implementation
- challenges faced
- scalability
- design decisions

Rules:
- Questions must be suitable for a final year student.
- Ask basic and intermediate questions only.
- Avoid software architecture and system design questions.
- Use simple language.
- Maximum 15 words per question.

Reply ONLY in JSON:

{{
  "questions":[
    "question1",
    "question2",
    "question3",
    "question4",
    "question5"
  ]
}}
"""

    result = ask_gemini_json(prompt)

    if (
        result
        and "questions" in result
        and isinstance(result["questions"], list)
        and len(result["questions"]) > 0
    ):
        return result["questions"][:5]

    return fallback_questions
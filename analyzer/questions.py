import json
from analyzer.gemini_helper import ask_gemini_json

# Used only when no skills were detected
general_fallback_questions = [
    "Tell me about yourself.",
    "Explain your most important project.",
    "What was your role in that project?",
    "What challenges did you face during development?",
    "Why should we hire you for this role?"
]

skill_fallbacks = {
    "python": [
        "What are Python decorators?",
        "What is list comprehension?",
        "What is the difference between a list and a tuple?"
    ],
    "java": [
        "What is OOP?",
        "What is inheritance?",
        "What is the JVM?"
    ],
    "c": [
        "What is a pointer in C?",
        "What is the difference between malloc and calloc?",
        "What is the difference between a local and a global variable?"
    ],
    "r": [
        "What is a data frame in R?",
        "How do you handle missing values in R?",
        "What is vectorization in R?"
    ],
    "html": [
        "What is semantic HTML?",
        "What is the DOM?",
        "What is the difference between id and class?"
    ],
    "css": [
        "What is Flexbox?",
        "What is the CSS box model?",
        "What is the difference between display:none and visibility:hidden?"
    ],
    "javascript": [
        "What is the difference between var, let, and const?",
        "What is a callback function?",
        "What is the difference between == and ===?"
    ],
    "sql": [
        "What is a JOIN?",
        "What is the difference between DELETE and TRUNCATE?",
        "What is normalization?"
    ],
    "machine learning": [
        "What is overfitting?",
        "What is the difference between supervised and unsupervised learning?",
        "How do you evaluate a machine learning model?"
    ],
    "deep learning": [
        "What is a neural network?",
        "What is the purpose of an activation function?",
        "What is the difference between deep learning and machine learning?"
    ],
    "data analysis": [
        "What are the steps in a data analysis project?",
        "How do you handle missing data?",
        "Which tools have you used for data analysis?"
    ],
    "git": [
        "What is the difference between Git and GitHub?",
        "What is a merge conflict and how do you resolve it?",
        "What does git clone do?"
    ]
}


def get_fallback_for_skill(skill):
    key = skill.lower().strip()

    if key in skill_fallbacks:
        return skill_fallbacks[key]

    return [
        f"Explain your experience with {skill}.",
        f"What are the main concepts of {skill}?",
        f"How have you used {skill} in your projects?"
    ]


def generate_questions(detected_skills, company=None):

    if not detected_skills:
        return {"General": general_fallback_questions}

    skills_to_use = detected_skills[:6]
    skills_text = ", ".join(skills_to_use)

    company_text = f" for a job at {company}" if company else ""

    example_shape = {
        skill: [
            "question 1",
            "question 2",
            "question 3"
        ]
        for skill in skills_to_use
    }

    example_json = json.dumps(example_shape)

    prompt = f"""
Generate fresher-level interview questions{company_text}
for these skills:

{skills_text}

Rules:
- Exactly 3 questions per skill
- Questions should be suitable for college students and freshers
- Use simple language
- Include all skills as separate keys

Return ONLY valid JSON.

Example:
{example_json}
"""

    result = ask_gemini_json(prompt)

    print("\n===== GEMINI QUESTIONS =====")
    print(result)
    print("============================\n")

    final_questions = {}

    if result and isinstance(result, dict):

        lower_result = {
            str(k).lower().strip(): v
            for k, v in result.items()
        }

        for skill in skills_to_use:

            key = skill.lower().strip()

            if key in lower_result and isinstance(lower_result[key], list):

                questions = [
                    q for q in lower_result[key]
                    if isinstance(q, str) and q.strip()
                ]

                if len(questions) >= 3:
                    final_questions[skill] = questions[:3]
                else:
                    final_questions[skill] = get_fallback_for_skill(skill)

            else:
                final_questions[skill] = get_fallback_for_skill(skill)

        return final_questions

    # Gemini completely failed
    for skill in skills_to_use:
        final_questions[skill] = get_fallback_for_skill(skill)

    return final_questions

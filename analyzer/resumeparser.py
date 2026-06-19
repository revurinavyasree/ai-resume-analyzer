import re


def calculate_completeness(parsed):

    score = 0

    checks = [

        parsed.get("name"),
        parsed.get("email"),
        parsed.get("phone"),
        parsed.get("linkedin"),
        parsed.get("github"),

        parsed.get("education"),
        parsed.get("skills"),
        parsed.get("projects"),
        parsed.get("experience"),

    ]

    for item in checks:

        if item:
            score += 1

    return round(
        (score / len(checks)) * 100
    )
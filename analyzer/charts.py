import matplotlib.pyplot as plt
import os


def generate_skill_chart(skills, filename):

    if not skills:
        return None

    chart_path = f"static/charts/{filename}.png"

    os.makedirs(
        "static/charts",
        exist_ok=True
    )

    values = [1] * len(skills)

    plt.figure(figsize=(8, 4))

    plt.bar(
        skills,
        values
    )

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(chart_path)

    plt.close()

    return chart_path
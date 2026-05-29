from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(

    filename,
    ats_score,
    skills,
    recommendations
):

    pdf_path = f"reports/{filename}.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "AI Resume Analysis Report",
        styles["Title"]
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    ats = Paragraph(
        f"<b>ATS Score:</b> {ats_score}%",
        styles["BodyText"]
    )

    elements.append(ats)

    elements.append(Spacer(1, 12))

    skill_text = ", ".join(skills)

    skills_para = Paragraph(
        f"<b>Detected Skills:</b> {skill_text}",
        styles["BodyText"]
    )

    elements.append(skills_para)

    elements.append(Spacer(1, 12))

    rec_text = "<br/>".join(recommendations)

    rec_para = Paragraph(
        f"<b>Recommendations:</b><br/>{rec_text}",
        styles["BodyText"]
    )

    elements.append(rec_para)

    doc.build(elements)

    return pdf_path
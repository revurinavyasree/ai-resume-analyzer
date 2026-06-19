from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf_report(
    filename,
    ats_score,
    skills,
    recommendations,
    strengths,
    weaknesses,
    company_scores,
    jd_match_score
):
    """
    Generates a professional PDF report for the Resume Analyzer.
    """

    # Create reports folder if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    # Remove file extension
    base_name = os.path.splitext(filename)[0]

    pdf_filename = f"{base_name}_report.pdf"
    pdf_path = os.path.join("reports", pdf_filename)

    # PDF document
    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()
    elements = []

    ##################################################
    # Title
    ##################################################

    elements.append(
        Paragraph(
            "AI Resume Analysis Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    ##################################################
    # Resume Name
    ##################################################

    elements.append(
        Paragraph(
            f"<b>Resume File:</b> {filename}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 10))

    ##################################################
    # ATS Score
    ##################################################

    elements.append(
        Paragraph(
            f"<b>ATS Score:</b> {ats_score}%",
            styles["BodyText"]
        )
    )

    ##################################################
    # Resume Quality
    ##################################################

    if ats_score >= 90:
        quality = "Excellent Resume"
    elif ats_score >= 75:
        quality = "Good Resume"
    elif ats_score >= 60:
        quality = "Needs Improvement"
    else:
        quality = "Major Improvements Required"

    elements.append(
        Paragraph(
            f"<b>Resume Quality:</b> {quality}",
            styles["BodyText"]
        )
    )

    ##################################################
    # JD Match
    ##################################################

    elements.append(
        Paragraph(
            f"<b>JD Match Score:</b> {jd_match_score}%",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 15))

    ##################################################
    # Skills
    ##################################################

    skill_text = ", ".join(skills) if skills else "No skills detected"

    elements.append(
        Paragraph(
            f"<b>Detected Skills:</b> {skill_text}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 15))

    ##################################################
    # Strengths
    ##################################################

    elements.append(
        Paragraph(
            "Strengths",
            styles["Heading2"]
        )
    )

    if strengths:
        for item in strengths:
            elements.append(
                Paragraph(
                    f"• {item}",
                    styles["BodyText"]
                )
            )
    else:
        elements.append(
            Paragraph(
                "No strengths identified.",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 15))

    ##################################################
    # Weaknesses
    ##################################################

    elements.append(
        Paragraph(
            "Weaknesses",
            styles["Heading2"]
        )
    )

    if weaknesses:
        for item in weaknesses:
            elements.append(
                Paragraph(
                    f"• {item}",
                    styles["BodyText"]
                )
            )
    else:
        elements.append(
            Paragraph(
                "No weaknesses identified.",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 15))

    ##################################################
    # Recommendations
    ##################################################

    elements.append(
        Paragraph(
            "Recommendations",
            styles["Heading2"]
        )
    )

    if recommendations:
        for item in recommendations:
            elements.append(
                Paragraph(
                    f"• {item}",
                    styles["BodyText"]
                )
            )
    else:
        elements.append(
            Paragraph(
                "No recommendations.",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 15))

    ##################################################
    # Company Match Scores
    ##################################################

    elements.append(
        Paragraph(
            "Company Match Scores",
            styles["Heading2"]
        )
    )

    if company_scores:

        sorted_scores = sorted(
            company_scores.items(),
            key=lambda x: x[1]["score"],
            reverse=True
        )

        for company, data in sorted_scores:

            elements.append(
                Paragraph(
                    f"<b>{company}</b> : {data['score']}%",
                    styles["BodyText"]
                )
            )

    else:

        elements.append(
            Paragraph(
                "No company scores available.",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 20))

    ##################################################
    # Overall Recommendation
    ##################################################

    elements.append(
        Paragraph(
            "Overall Recommendation",
            styles["Heading2"]
        )
    )

    if ats_score >= 85:
        overall = (
            "Your resume is well structured and ATS-friendly. "
            "Continue tailoring it for each job description."
        )

    elif ats_score >= 70:
        overall = (
            "Your resume is good but can be improved by adding "
            "more projects, certifications, and stronger keywords."
        )

    else:
        overall = (
            "Your resume needs significant improvements. Focus on "
            "skills, projects, certifications, and ATS optimization "
            "before applying."
        )

    elements.append(
        Paragraph(
            overall,
            styles["BodyText"]
        )
    )

    ##################################################
    # Footer
    ##################################################

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "Generated by AI Resume Analyzer",
            styles["Italic"]
        )
    )

    ##################################################
    # Build PDF
    ##################################################

    doc.build(elements)

    return pdf_filename
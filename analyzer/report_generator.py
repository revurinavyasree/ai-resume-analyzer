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
    missing_skills,
    recommendations,
    strengths,
    weaknesses,
    company_scores,
    jd_match_score,
    interview_questions,
    project_questions=None
):
    """
    Generate a professional AI Resume Analysis PDF Report.
    """

    # Create reports folder if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    # Remove extension from filename
    base_name = os.path.splitext(filename)[0]

    pdf_filename = f"{base_name}_report.pdf"
    pdf_path = os.path.join("reports", pdf_filename)

    # Create PDF document
    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()
    elements = []

    ####################################################
    # TITLE
    ####################################################

    elements.append(
        Paragraph(
            "AI Resume Analysis Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    ####################################################
    # Resume File
    ####################################################

    elements.append(
        Paragraph(
            f"<b>Resume File:</b> {filename}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 10))

    ####################################################
    # ATS SCORE
    ####################################################

    elements.append(
        Paragraph(
            f"<b>ATS Score:</b> {ats_score}%",
            styles["BodyText"]
        )
    )

    ####################################################
    # Resume Quality
    ####################################################

    if ats_score >= 90:
        quality = "★★★★★ Excellent Resume"

    elif ats_score >= 80:
        quality = "★★★★☆ Very Good Resume"

    elif ats_score >= 70:
        quality = "★★★☆☆ Good Resume"

    elif ats_score >= 60:
        quality = "★★☆☆☆ Needs Improvement"

    else:
        quality = "★☆☆☆☆ Major Improvements Required"

    elements.append(
        Paragraph(
            f"<b>Resume Quality:</b> {quality}",
            styles["BodyText"]
        )
    )

    ####################################################
    # JD MATCH SCORE
    ####################################################

    elements.append(
        Paragraph(
            f"<b>Job Description Match:</b> {jd_match_score}%",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 15))

    ####################################################
    # Candidate Summary
    ####################################################

    elements.append(
        Paragraph(
            "Candidate Summary",
            styles["Heading2"]
        )
    )

    summary = (
        f"This resume achieved an ATS score of "
        f"<b>{ats_score}%</b> and a Job Description "
        f"matching score of <b>{jd_match_score}%</b>. "
        f"The analyzer detected "
        f"<b>{len(skills)}</b> technical skills. "
        f"The report below highlights the candidate's "
        f"strengths, weaknesses, missing skills, "
        f"company compatibility, interview preparation, "
        f"and recommendations for improving the resume."
    )

    elements.append(
        Paragraph(
            summary,
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 15))

    ####################################################
    # Detected Skills
    ####################################################

    elements.append(
        Paragraph(
            "Detected Skills",
            styles["Heading2"]
        )
    )

    if skills:

        skill_text = ", ".join(skills)

        elements.append(
            Paragraph(
                skill_text,
                styles["BodyText"]
            )
        )

    else:

        elements.append(
            Paragraph(
                "No technical skills detected.",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 15))
    ####################################################
    # Strengths
    ####################################################
    
    elements.append(
        Paragraph(
            "Strengths",
            styles["Heading2"]
        )
    )

    if strengths:
        for i, item in enumerate(strengths, start=1):
            elements.append(
                Paragraph(
                    f"{i}. {item}",
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


    ####################################################
    # Weaknesses
    ####################################################

    elements.append(
        Paragraph(
            "Weaknesses",
            styles["Heading2"]
        )
    )

    if weaknesses:

        for i, item in enumerate(weaknesses, start=1):

            elements.append(
                Paragraph(
                    f"{i}. {item}",
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


    ####################################################
    # Missing Skills
    ####################################################

    elements.append(
        Paragraph(
            "Missing Skills",
            styles["Heading2"]
        )
    )

    if missing_skills:

        for skill in sorted(missing_skills):

            elements.append(
                Paragraph(
                    f"• {skill}",
                    styles["BodyText"]
                )
            )

    else:

        elements.append(
            Paragraph(
                "No important skills are missing.",
                styles["BodyText"]
            )
        )

   

    elements.append(Spacer(1, 15))


    ####################################################
    # Recommendations
    ####################################################

    elements.append(
        Paragraph(
            "Recommendations",
            styles["Heading2"]
        )
    )

    if recommendations:

        for i, item in enumerate(recommendations, start=1):

            elements.append(
                Paragraph(
                    f"{i}. {item}",
                    styles["BodyText"]
                )
            )

    else:

        elements.append(
            Paragraph(
                "No recommendations available.",
            styles["BodyText"]
            )
        )


    elements.append(Spacer(1, 20))


    ####################################################
    # Company Match Scores
    ####################################################

    elements.append(
        Paragraph(
            "Company Match Scores",
            styles["Heading2"]
        )
    )

    if company_scores:

        sorted_scores = sorted(
            company_scores.items(),
            key=lambda x: x[1].get("score", 0) if isinstance(x[1], dict) else x[1],
            reverse=True
        )

        for company, data in sorted_scores:

            if isinstance(data, dict):
                score = data.get("score", 0)
            else:
                score = data

            if score >= 90:
                level = "★★★★★ Excellent Match"

            elif score >= 80:
                level = "★★★★☆ Very Good Match"

            elif score >= 70:
                level = "★★★☆☆ Good Match"

            elif score >= 60:
                level = "★★☆☆☆ Average Match"

            else:
                level = "★☆☆☆☆ Low Match"

            elements.append(
                Paragraph(
                    f"<b>{company}</b>",
                    styles["BodyText"]
                )
            )
            elements.append(
                Paragraph(
                    f"Score : {score}%",
                    styles["BodyText"]
                )
            )

            elements.append(
                Paragraph(
                    f"Result : {level}",
                    styles["BodyText"]
                )
            )
       

            elements.append(
                Spacer(1, 8)
            )

    else:

        elements.append(
            Paragraph(
                "No company matching data available.",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 20))

    ####################################################
    # Interview Questions
    # interview_questions is a dict like {"python": ["q1", "q2", "q3"], ...}
    # so we loop through each skill, then loop through its question list.
    ####################################################

    elements.append(
        Paragraph(
            "Suggested Interview Questions",
            styles["Heading2"]
        )
    )

    if interview_questions:

        for skill, question_list in interview_questions.items():

            elements.append(
                Paragraph(
                    f"<b>{skill}</b>",
                    styles["BodyText"]
                )
            )

            for i, question in enumerate(question_list, start=1):
                elements.append(
                    Paragraph(
                        f"{i}. {question}",
                        styles["BodyText"]
                    )
                )

            elements.append(Spacer(1, 8))

    else:

        elements.append(
            Paragraph(
                "No interview questions generated.",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 20))

    ####################################################
    # Project-Based Interview Questions
    # project_questions is a flat list of question strings
    ####################################################

    elements.append(
        Paragraph(
            "Project-Based Interview Questions",
            styles["Heading2"]
        )
    )

    if project_questions:

        for i, question in enumerate(project_questions, start=1):

            elements.append(
                Paragraph(
                    f"{i}. {question}",
                    styles["BodyText"]
                )
            )

    else:

        elements.append(
            Paragraph(
                "No project-based questions generated.",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 20))


    ####################################################
    # Overall Evaluation
    ####################################################

    elements.append(
        Paragraph(
            "Overall Evaluation",
            styles["Heading2"]
        )
    )

    if ats_score >= 90 and jd_match_score >= 90:
        overall = (
            "Outstanding resume with excellent ATS optimization "
            "and strong alignment with the job description."
        )

    elif ats_score >= 80 and jd_match_score >= 80:
        overall = (
            "Very good resume. Minor improvements can further "
            "increase interview chances."
        )

    elif ats_score >= 70:
        overall = (
            "Good resume with a solid foundation. Adding more "
            "relevant skills, measurable achievements, and keywords "
            "would improve competitiveness."
        )

    else:
        overall = (
            "Resume requires significant improvements in formatting, "
            "content, and keyword optimization before applying."
        )

    elements.append(
        Paragraph(
            overall,
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))


    ####################################################
    # Final Rating
    ####################################################

    elements.append(
        Paragraph(
            "Final Rating",
            styles["Heading2"]
        )
    )

    final_score = round((ats_score + jd_match_score) / 2)

    if final_score >= 90:
        rating = "★★★★★"

    elif final_score >= 80:
        rating = "★★★★☆"

    elif final_score >= 70:
        rating = "★★★☆☆"

    elif final_score >= 60:
        rating = "★★☆☆☆"

    else:
        rating = "★☆☆☆☆"

    elements.append(
        Paragraph(
            f"<b>Overall Resume Rating:</b> {rating} ({final_score}/100)",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))


    ####################################################
    # Footer
    ####################################################

    elements.append(
        Paragraph(
            "<b>End of Report</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            "This report was automatically generated by the AI Resume Analyzer. "
            "Scores are estimates based on resume content, ATS compatibility, "
            "technical skills, and job description matching.",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 15))

    ####################################################
    # Build PDF
    ####################################################

    doc.build(elements)

    return pdf_path
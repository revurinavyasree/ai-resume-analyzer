def rank_resumes(resumes):

    ranked = sorted(
        resumes,
        key=lambda x: x.get("ats_score", 0),
        reverse=True
    )

    for i, resume in enumerate(ranked):

        resume["rank"] = i + 1

    return ranked
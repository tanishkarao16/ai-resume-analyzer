import re

def compute_match_score(candidate_skills, job_description):
    """
    Calculate match score based on overlapping skills
    """

    if not job_description:
        return 50

    candidate_skills_list = [
        skill.strip().lower() for skill in candidate_skills.split(",")
    ]

    job_text = job_description.lower()

    score = 0

    for skill in candidate_skills_list:
        if skill in job_text:
            score += 20

    return min(score, 100)


def skill_gap_analysis(candidate_skills, job_description):
    """
    Identify missing skills compared to job description
    """

    if not job_description:
        return []

    candidate_skills_list = [
        skill.strip().lower() for skill in candidate_skills.split(",")
    ]

    job_words = re.findall(r"\b[a-zA-Z]+\b", job_description.lower())

    missing_skills = []

    for word in job_words:
        if word not in candidate_skills_list and len(word) > 3:
            missing_skills.append(word)

    return list(set(missing_skills))[:10]
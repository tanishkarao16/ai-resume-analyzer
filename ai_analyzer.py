import re


def analyze_resume(text):

    name = text.split("\n")[0]

    skills_list = [
        "python","sql","excel","java",
        "machine learning","data analysis",
        "react","javascript","flutter",
        "aws","docker","pandas"
    ]

    skills_found = []

    text_lower = text.lower()

    for skill in skills_list:

        if skill in text_lower:
            skills_found.append(skill)

    experience = "Not specified"

    match = re.search(r'(\d+)\s+years', text_lower)

    if match:
        experience = match.group(0)

    return {
        "name": name,
        "skills": ", ".join(skills_found),
        "experience": experience
    }
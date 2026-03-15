import re

def extract_candidate_info(ai_output):

    name = re.search(r"Name:\s*(.*)", ai_output)
    skills = re.search(r"Skills:\s*(.*)", ai_output)
    experience = re.search(r"Experience:\s*(.*)", ai_output)
    score = re.search(r"Score:\s*(.*)", ai_output)

    name = name.group(1) if name else "Unknown"
    skills = skills.group(1) if skills else "Unknown"
    experience = experience.group(1) if experience else "0"
    score = score.group(1) if score else "0"

    return name, skills, experience, float(score)
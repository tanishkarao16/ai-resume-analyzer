import re

def extract_candidate_info(result):

    name = "Unknown"
    skills = "Unknown"
    experience = "Unknown"
    score = "0"

    lines = result.split("\n")

    for line in lines:

        if "Name:" in line:
            name = line.split(":")[1].strip()

        if "Skills:" in line:
            skills = line.split(":")[1].strip()

        if "Experience:" in line:
            experience = line.split(":")[1].strip()

        if "Score:" in line:
            score = line.split(":")[1].strip()

    score = score.split("/")[0]

    return name, skills, experience, float(score)
def analyze_resume(resume_text, job_description):

    prompt = f"""
    Analyze this resume for the following job.

    Job Description:
    {job_description}

    Provide the output in JSON format:

    {{
    "summary": "",
    "skills": [],
    "experience_years": "",
    "match_score": ""
    }}

    Resume:
    {resume_text}
    """
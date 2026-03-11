import requests
import json

def analyze_resume(resume_text):
    
    prompt = f"""
    Analyze the following resume.

    Provide:
    1. Candidate Summary
    2. Skills
    3. Estimated Experience
    4. Job Match Score (0-10)

    Resume:
    {resume_text}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return result["response"]
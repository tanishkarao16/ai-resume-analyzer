import requests

def analyze_resume(resume_text):

    prompt = f"""
    You are an AI recruiter.

    Analyze the resume and return ONLY in this format:

    Name: <candidate name>
    Skills: <comma separated skills>
    Experience: <years>
    Score: <score out of 10>

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
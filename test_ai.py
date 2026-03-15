from resume_parser import extract_text_from_pdf
from ai_analyzer import analyze_resume

file = "resumes/sample_resume.pdf"

text = extract_text_from_pdf(file)

result = analyze_resume(text)

print(result)
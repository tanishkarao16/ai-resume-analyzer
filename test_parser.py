from resume_parser import extract_text_from_pdf

file = "resumes/sample_resume.pdf"

text = extract_text_from_pdf(file)

print(text)
import streamlit as st
from job_matcher import compute_match_score
from resume_parser import extract_text_from_pdf

st.title("Job Description Matching")

job_description = st.text_area("Paste Job Description")

uploaded_files = st.file_uploader(
    "Upload resumes to match",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files and job_description:

    if st.button("Calculate Match Scores"):

        for file in uploaded_files:

            text = extract_text_from_pdf(file)

            score = compute_match_score(job_description, text)

            st.write(f"{file.name} — Match Score: {score}%")
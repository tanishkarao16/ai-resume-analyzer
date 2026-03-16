import streamlit as st
from resume_parser import extract_text_from_pdf
from ai_analyzer import analyze_resume
from database import insert_candidate
from utils import extract_candidate_info

st.title("Upload Resumes")

uploaded_files = st.file_uploader(
    "Upload PDF resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    if st.button("Analyze Resumes"):

        progress = st.progress(0)

        for i, file in enumerate(uploaded_files):

            text = extract_text_from_pdf(file)

            result = analyze_resume(text)

            name, skills, experience, score = extract_candidate_info(result)

            insert_candidate(name, skills, experience, score)

            progress.progress((i + 1) / len(uploaded_files))

        st.success("All resumes processed successfully!")
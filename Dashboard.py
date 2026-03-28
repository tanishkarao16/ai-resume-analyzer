import streamlit as st
from resume_parser import parse_resume
from ai_analyzer import analyze_resume
from job_matcher import compute_match_score
from database import insert_candidate

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer")
st.write("Upload a resume and compare it with a job description.")

st.divider()

job_description = st.text_area(
    "Paste Job Description"
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file and job_description:

    with st.spinner("Analyzing Resume..."):

        resume_text = parse_resume(uploaded_file)

        result = analyze_resume(resume_text)

        name = result["name"]
        skills = result["skills"]
        experience = result["experience"]

        score = compute_match_score(
            skills,
            job_description
        )

        insert_candidate(
            name,
            skills,
            experience,
            score
        )

    st.success("Resume analyzed and saved!")

    st.subheader("Candidate Details")

    st.write("Name:", name)
    st.write("Skills:", skills)
    st.write("Experience:", experience)

    st.metric(
        "Match Score",
        f"{score}%"
    )
import streamlit as st
import pandas as pd

from resume_parser import extract_text_from_pdf
from ai_analyzer import analyze_resume
from database import insert_candidate, get_ranked_candidates
from utils import extract_candidate_info

st.title("AI Resume Analyzer")

st.write("Upload resumes and analyze candidates using AI.")

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    if st.button("Analyze Resumes"):

        progress = st.progress(0)

        for i, uploaded_file in enumerate(uploaded_files):

            text = extract_text_from_pdf(uploaded_file)

            with st.spinner(f"Analyzing {uploaded_file.name}..."):
                result = analyze_resume(text)

            name, skills, experience, score = extract_candidate_info(result)

            insert_candidate(name, skills, experience, score)

            progress.progress((i + 1) / len(uploaded_files))

        st.success("All candidates analyzed and saved!")

# Candidate Rankings
st.subheader("Candidate Rankings")

candidates = get_ranked_candidates()

if candidates:
    df = pd.DataFrame(
        candidates,
        columns=["Name", "Skills", "Experience", "Score"]
    )

    st.table(df)

else:
    st.info("No candidates analyzed yet.")
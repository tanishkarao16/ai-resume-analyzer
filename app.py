import streamlit as st
from resume_parser import extract_text_from_pdf
from ai_analyzer import analyze_resume
from database import insert_candidate, get_ranked_candidates
from utils import extract_candidate_info

st.title("AI Resume Analyzer")

st.write("Upload a resume and analyze the candidate using AI.")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file:

    text = extract_text_from_pdf(uploaded_file)

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing resume with AI..."):
            result = analyze_resume(text)

        st.subheader("AI Analysis Result")
        st.write(result)

        # Extract structured data
        name, skills, experience, score = extract_candidate_info(result)

        # Save candidate
        insert_candidate(name, skills, experience, score)

        st.success("Candidate saved successfully!")

# Candidate Rankings Section
st.subheader("Candidate Rankings")

candidates = get_ranked_candidates()

for c in candidates:
    st.write(f"Name: {c[0]}")
    st.write(f"Skills: {c[1]}")
    st.write(f"Experience: {c[2]}")
    st.write(f"Score: {c[3]}")
    st.write("---")
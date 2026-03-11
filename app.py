import streamlit as st
from resume_parser import extract_text_from_pdf
from ai_analyzer import analyze_resume

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file:

    text = extract_text_from_pdf(uploaded_file)

    if st.button("Analyze Resume"):
        result = analyze_resume(text)
        st.write(result)
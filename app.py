import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("AI Resume Analyzer")

st.markdown("""
### AI Powered Candidate Screening System

This tool allows recruiters to:

• Upload multiple resumes  
• Extract candidate skills automatically  
• Rank candidates using AI  
• Match resumes to job descriptions  
• View candidate analytics
""")

st.info("Use the sidebar to navigate through the application.")
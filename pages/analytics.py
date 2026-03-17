import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import get_ranked_candidates

st.title("Candidate Analytics")

candidates = get_ranked_candidates()

if candidates:

    df = pd.DataFrame(
        candidates,
        columns=["Name", "Skills", "Experience", "Score"]
    )

    st.subheader("Candidate Score Distribution")

    plt.hist(df["Score"], bins=10)
    st.pyplot(plt)

    st.subheader("Experience Distribution")

    df["Experience"] = pd.to_numeric(df["Experience"], errors="coerce")

    plt.figure()
    plt.hist(df["Experience"].dropna(), bins=10)
    st.pyplot(plt)

else:
    st.info("No candidate data available.")
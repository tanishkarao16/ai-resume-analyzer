import streamlit as st
import pandas as pd
from database import get_ranked_candidates

st.title("Candidate Rankings")

candidates = get_ranked_candidates()

if candidates:

    df = pd.DataFrame(
        candidates,
        columns=["Name", "Skills", "Experience", "Score"]
    )

    # Candidate table
    st.subheader("All Candidates")
    st.dataframe(df, use_container_width=True)

    # Top Candidates Leaderboard
    st.subheader("Top Candidates")

    top = df.sort_values("Score", ascending=False).head(5)

    for i, row in top.iterrows():

        st.markdown(
            f"🏆 **{row['Name']}** — Score: {row['Score']} | Skills: {row['Skills']}"
        )

    # Download button
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Candidate List",
        csv,
        "candidates.csv",
        "text/csv"
    )

else:
    st.info("No candidates analyzed yet.")
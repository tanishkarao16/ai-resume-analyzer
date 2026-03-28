import streamlit as st
import pandas as pd
from database import get_ranked_candidates

st.set_page_config(
    page_title="Candidate Rankings",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Candidate Rankings")

candidates = get_ranked_candidates()

if candidates:

    df = pd.DataFrame(
        candidates,
        columns=["ID","Name","Skills","Experience","Score"]
    )

    # Remove ID column
    df = df.drop(columns=["ID"])

    # Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Candidates", len(df))
    col2.metric("Average Score", round(df["Score"].mean(),2))
    col3.metric("Top Score", df["Score"].max())

    st.divider()

    # Top Candidates
    st.subheader("🏆 Top Candidates")

    top = df.sort_values("Score", ascending=False).head(5)

    cols = st.columns(len(top))

    for i, (_, row) in enumerate(top.iterrows()):
        cols[i].metric(
            label=row["Name"],
            value=row["Score"]
        )

    st.divider()

    # All candidates table
    st.subheader("All Candidates")

    st.dataframe(
        df.sort_values("Score", ascending=False),
        use_container_width=True
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
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

    st.dataframe(df)

else:
    st.info("No candidates analyzed yet.")
import streamlit as st

st.title("Firestore Rule Writer")

choice = st.selectbox(
    "What rule would you like to write?",
    ["Allow read", "Allow write",
     "Allow read and write", "Deny all",
     "Allow one of them and deny the other"]
)

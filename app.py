import streamlit as st

st.title("Firestore Rule Writer")

choice = st.selectbox(
    "What rule would you like to write?",
    [
        "Allow read only",
        "Allow write only",
        "Allow read and write",
        "Deny all access",
        "Custom (one allowed, one denied)"
    ]
)

if choice == 'Allow read':
    st.write('Public access - anyone can read')
    st.write('Authenticated access - only logged in users.')
    st.write('Role-based access - logged in and roles can read specific documents.')
    st.write('Owner-based access - only the document creator can read.')
    st.write('Shared list access - only specific allowed users can read.')
    st.write('Time-based access - allowed only before/after a time.')
    st.write('Field-based conditions - depends on data inside the document (e.g. isPublic == true).')

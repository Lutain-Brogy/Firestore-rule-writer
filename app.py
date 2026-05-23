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

if choice == "Allow read only":
    edit_choice = st.selectbox(
        "Select read rule type:",
        [
            "pread ublic access",
            "read authenticated access",
            "rread ole-based access",
            "read owner-based access",
            "read shared list access",
            "read time-based access",
            "read field-based conditions"
        ]
    )
    

 if edit_choice == "read public access":
    st.write("Public access - anyone can read")

    st.code("""
rules_version = '2';

service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read: if true;
    }
  }
}
""")



    elif edit_choice == "Authenticated access":
        st.write("Authenticated access - only logged in users.")

    elif edit_choice == "Role-based access":
        st.write("Role-based access - logged in users with roles can read specific documents.")

    elif edit_choice == "Owner-based access":
        st.write("Owner-based access - only the document creator can read.")

    elif edit_choice == "Shared list access":
        st.write("Shared list access - only specific allowed users can read.")

    elif edit_choice == "Time-based access":
        st.write("Time-based access - allowed only before/after a time.")

    elif edit_choice == "Field-based conditions":
        st.write("Field-based conditions - depends on data inside the document (e.g. isPublic == true).")

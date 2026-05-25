import streamlit as st

st.title("Firestore Rule Writer")

choice = st.selectbox(
    "What rule would you like to write?",
    [
        "Allow read only",
#        "Allow write only",
 #       "Allow read and write",
  #      "Deny all access",
   #     "Custom (one allowed, one denied)"
        
    ]
)

if choice == "Allow read only":
    edit_choice = st.selectbox(
        "Select read rule type:",
        [
            "read public access",
            "read authenticated access",
          #  "read role-based access",
           # "read owner-based access",
            #"read shared list access",
            #"read time-based access",
            #"read field-based conditions"
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

elif edit_choice == "read authenticated access":
    st.write("Authenticated access - only logged in users.")

    
    auth_choice = st.selectbox(
        "Choose authentication type",
        [
            "logged in",
            "admin role",
            "document ownership",
            "custom based",
            "time/date",
            "premium subscription",
            "field change check"
        ]
    )


  if auth_choice == "logged in":
    database = st.text_input("Enter database name", value="(default)")
    document_path = st.text_input("Enter document path", value="/{document=**}")

    st.code(f"""
rules_version = '2';

service cloud.firestore {{
  match /databases/{database}/documents {{

    match {document_path} {{
      allow read: if request.auth != null;
    }}
  }}
}}
""")

# only lets the admin/creator read

elif auth_choice == "admin role":
    st.code("""
rules_version = '2';

service cloud.firestore {
  match /databases/{database}/documents {

    match /{document=**} {
      allow read, write: if request.auth != null
                          && request.auth.token.admin == true;
    }
  }
}
""")

#only alows read to who the document is assigned to

if auth_choice == "document ownership":
    database = st.text_input("Enter database name", value="(default)")
    document_path = st.text_input("Enter document path", value="/users/{userId}")
    user_field = st.text_input("Field storing owner UID", value="ownerId")

    st.code(f"""
rules_version = '2';

service cloud.firestore {{
  match /databases/{database}/documents {{

    match {document_path} {{
      allow read, write: if request.auth != null
                          && resource.data.{user_field} == request.auth.uid;
    }}
  }}
}}
""")


elif auth_choice == "custorm based":
    st.write("make you own custorm term by talking to Lutzet at Whop") 

elif auth_choice == "time/date":
    st.write("Talk with Luzet to make this one")  

elif auth_choice == "premium subscription":
    st.write("Talk with Luzet to make this one")

elif auth_choice == "field change check":
    st.write("Talk with Luzet to make this one active")

#elif edit_choice == "Role-based access":
#    st.write("Role-based access - logged in users with roles can read specific documents.")

#elif edit_choice == "Owner-based access":
 #   st.write("Owner-based access - only the document creator can read.")

#elif edit_choice == "Shared list access":
 #   st.write("Shared list access - only specific allowed users can read.")

#elif edit_choice == "Time-based access":
 #   st.write("Time-based access - allowed only before/after a time.")

#elif edit_choice == "Field-based conditions":
 #   st.write("Field-based conditions - depends on data inside the document (e.g. isPublic == true).")

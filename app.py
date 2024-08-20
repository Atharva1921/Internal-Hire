import streamlit as st


dashboard_page = st.Page(
    page="views/dashboard.py",
    title="Dashboard",
    icon=":material/dashboard:",
)

upload_resume_page = st.Page(
    page="views/upload_resume.py",
    title="Upload Resume",
    icon=":material/upload_file:"
)

search_expertise_page = st.Page(
    page="views/search_expertise.py",
    title="Search Expertise",
    icon=":material/search:"
)

chatbot_page = st.Page(
    page="views/chatbot.py",
    title="Chat",
    icon=":material/chat:",
)



# Navigation menu

pg = st.navigation(pages=[dashboard_page,upload_resume_page,search_expertise_page,chatbot_page])

pg.run()

st.sidebar.text("Made for HR")
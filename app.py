import streamlit as st


dashboard_page = st.Page(
    page="views/1_dashboard.py",
    title="Dashboard",
    icon=":material/dashboard:",
)


chatbot_page = st.Page(
    page="views/2_chatbot.py",
    title="Chat",
    icon=":material/chat:",
)



# Navigation menu

pg = st.navigation(pages=[chatbot_page,dashboard_page])

pg.run()

st.sidebar.text("Made for HR")
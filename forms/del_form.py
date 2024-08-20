import streamlit as st
from Database.Db import delete_entry, load_data


def del_form():

    with st.form("del_form"):
        name = st.text_input("name")
        delete_button = st.form_submit_button("Delete Entry")

        if delete_button:
            with st.spinner("Deleting entry may take sometime. Please wait!!"):
                delete_entry(name=name)
                load_data()
            st.success("Record deleted Successfully")
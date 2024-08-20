import streamlit as st
import pandas as pd
from utils.util_functions import summarize, readPDF, generate_embeddings
import json
from Database.Db import load_data, add_entry



st.title("Upload Resume")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Name")
    department = st.selectbox("Department", options=['Engineering', 'Data Science', 'Product', 'Design', 'Marketing', 'HR','Others']) #Add departments
with col2:
    resume_file = st.file_uploader("Upload Resume (PDF)", type=['pdf'])
    
if st.button("Submit"):
    if name and department and resume_file:
        try:
            with st.spinner("Adding entry may take sometime. Please wait!!"):
                    temp_file = "./temp.pdf"
                    with open(temp_file,"wb") as file:
                        file.write(resume_file.getvalue())
                        file_name = resume_file.name
                        file.close()
                    
                    document = readPDF(temp_file)[0].page_content
                    document_summary = summarize(document)
                    embeddings = generate_embeddings(document_summary)

                    add_entry(name=name,department=department,text=document_summary,embeddings=json.dumps(embeddings))
                    load_data()
                    st.success("Record added Successfully")     
        except Exception as e:
            st.error("Sorry! something went wrong.")  
    else:
        st.error("Please fill in all fields and upload a resume.")
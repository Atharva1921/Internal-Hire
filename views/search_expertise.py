import streamlit as st
from utils.util_functions import generate_embeddings, create_card
from Database.Db import search
import json

st.set_page_config(page_title="HR Dashboard", layout="wide")
st.title("Search Expertise")
    
search_query = st.text_area("Enter skills or job description to search")
    
if st.button("Search"):

    with st.spinner("Loading Data please wait !!"):
        try:
            query_embedding = generate_embeddings(search_query)
            results = search(query_embedding=json.dumps(query_embedding))
        except Exception as e:
            st.error("Sorry! something went wrong.")  
            
        if results:
            st.subheader(f"Search Results:")
            for result in results["result"]:
                create_card(item=result) # display
            
        else:
            st.info("No matching results found.")
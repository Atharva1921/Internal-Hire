from tidb_vector.integrations import TiDBVectorClient
import os

import pandas as pd
import streamlit as st

#database connection
def database_connection():

    vector_store = TiDBVectorClient(
    # The table which will store the vector data.
    table_name='resumes',
    # The connection string to the TiDB cluster.
    connection_string=os.environ.get('TIDB_DATABASE_URL'),
    # The dimension of the vector generated by the embedding model.
    vector_dimension=768,
    # Determine whether to recreate the table if it already exists.
    drop_existing_table=False,
    distance_strategy="cosine",
    )

    return vector_store

#Get data
def load_data():

    vector_store = database_connection()

    result_dictionary = vector_store.execute("SELECT id, name, department, text FROM resumes") #add department
    result_list = result_dictionary['result']

    df = pd.DataFrame(result_list, columns=['ID','NAME','DEPARTMENT','RESUME SUMMARY']) #add department
    st.session_state.df = df

#Delete Entry with name
def delete_entry(name):
    vector_store = database_connection()
    vector_store.execute("DELETE FROM resumes WHERE name= :name",{"name":name})

#Add Entry
def add_entry(name, department, text, embeddings):
    vector_store = database_connection()
    vector_store.execute("INSERT INTO resumes (name, department, text, embedding) VALUES (:name, :department, :text, :embedding)", {"name": name,"department":department, "text": text, "embedding": embeddings})

#Search vectors based on similarity
def search(query_embedding):
    vector_store = database_connection()
    result = vector_store.execute("SELECT id, name, department, text FROM resumes ORDER BY Vec_Cosine_Distance(embedding, :query_embedding) LIMIT 2", {"query_embedding":query_embedding})# modify query   
    return result


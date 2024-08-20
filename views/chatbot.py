import streamlit as st
from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from Database.Db import search
from utils.util_functions import generate_embeddings
import json

#prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a Professional HR Bot. Answer the questions as detailed as possible from the provided context of resumes."),
        ("user","RESUME-CONTEXT: {context} \n QUESTION: {question}")
    ]
)

llm = Ollama(model="llama3.1:8b")
outputParser = StrOutputParser()
chain = prompt | llm | outputParser


#Chat interface
st.title("Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


question = st.chat_input("What is up?")



if question:

    with st.chat_message("user"):
        st.markdown(question)

    st.session_state.messages.append({"role": "user", "content": question})

    with st.spinner("Generating response please wait !!"):
        try:
            query_embedding = generate_embeddings(question)
            result = search(query_embedding=json.dumps(query_embedding))
        except Exception as e:
            st.error("Sorry! something went wrong.") 

    with st.chat_message("assistant"):
        response = chain.invoke({"context": result, "question":question})
        st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})


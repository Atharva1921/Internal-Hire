import streamlit as st
from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a  assistant anme Aura. Please respond to all the question"),
        ("user","Question: {question}")
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
    with st.chat_message(message["ai"]):
        st.markdown(message["content"])


prompt = st.chat_input("What is up?")

if prompt:

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("ai"):
        response = chain.invoke({'question':prompt})
        st.markdown(response)

        st.session_state.messages.append({"role": "ai", "content": response})

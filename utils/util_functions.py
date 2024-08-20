from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import PyPDFLoader
from streamlit_card import card


#PDF to text
def readPDF(file_name):

    loader = PyPDFLoader(file_name)
    pages = loader.load_and_split()
    return pages


def summarize(resume_content):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system","You are a Professional Resume summarizer. I will provide you resume in text format."),
            ("user","Summarize the following resume in less than 500 words, focusing on key qualifications, skills, work experience, and education. Capture the essence of the candidate's professional profile, highlighting their most relevant achievements and expertise. Provide a concise overview that would be useful for HR professionals and talent acquisition specialists in quickly assessing the candidate's fit for potential roles. Avoid using any formatting symbols or new line characters. Present the summary as a continuous paragraph of text. \n RESUME: {resume}")
        ]
    )

    llm = Ollama(model="llama3.1:8b")
    outputParser = StrOutputParser()
    chain = prompt | llm | outputParser

    resume_summary = chain.invoke({"resume": resume_content})
    return resume_summary

def generate_embeddings(text):
    model = SentenceTransformer('all-mpnet-base-v2')
    vector_dim = (model.get_sentence_embedding_dimension())

    embedding = model.encode(text)

    return embedding.tolist()

def create_card(item):
    hasClicked = card(
    title=item[1],
    text=item[3],
)

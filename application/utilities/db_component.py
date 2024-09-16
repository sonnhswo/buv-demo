# from application.const import DATABASES
import os
from dotenv import load_dotenv, find_dotenv
from models.chat import azure_openai
from models.embeddings import text_embedding_3large
from langchain.vectorstores.pgvector import PGVector
import streamlit as st


load_dotenv(find_dotenv('../.env'))

host = os.getenv("DEMO_PG_VECTOR_HOST")
user = os.getenv("DEMO_PG_VECTOR_USER")
password = os.getenv("DEMO_PG_VECTOR_PASSWORD")
collection_name = os.getenv("COLLECTION_NAME")



#----------------------------
DATABASES = {
    "Arts University Bournemouth (AUB)": {
        "Student handbook (pending)": "",
        "AUB-OCT24-FREQUENTLY ASKED QUESTIONS": os.getenv("DEMO_DATABASE_AUB_FREQUENTLYASKEDQUESTION"),
        "PSG Programme Handbook_Oct 2024": os.getenv("DEMO_DATABASE_AUB_PSG"),
    },

    "British University Vietnam (IHM/FE)": {
        "Student handbook (pending)": "",
        "BUV-OCT24-FREQUENTLY ASKED QUESTIONS": os.getenv("DEMO_DATABASE_IHMFE_FREQUENTLYASKEDQUESTION"),
        "PSG Programme Handbook_Oct 2024": os.getenv("DEMO_DATABASE_IHMFE_PSG"),
    },

    "Staffordshire University (SU)": {
        "Student handbook (pending)": "",
        "SU-OCT24-FREQUENTLY ASKED QUESTIONS": os.getenv("DEMO_DATABASE_SU_FREQUENTLYASKEDQUESTION"),
        "PSG Programme Handbook_Oct 2024": os.getenv("DEMO_DATABASE_SU_PSG"),
    },

    "University of London- Undergraduate (UoL)": {
        "Student handbook (pending)": "",
        "UoL-OCT24-FREQUENTLY ASKED QUESTIONS": os.getenv("DEMO_DATABASE_UOL_FREQUENTLYASKEDQUESTION"),
        "PSG Programme Handbook_Oct 2024": os.getenv("DEMO_DATABASE_UOL_PSG"),
    },

    "University of London- International Foundation Programme (IFP)": {
        "Student handbook (pending)": "",
        "IFP-OCT24-FREQUENTLY ASKED QUESTIONS": os.getenv("DEMO_DATABASE_IFP_FREQUENTLYASKEDQUESTION"),
    },

    "University of Stirling (US)": {
        "Student handbook (pending)": "",
        "US-OCT24-FREQUENTLY ASKED QUESTIONS": os.getenv("DEMO_DATABASE_US_FREQUENTLYASKEDQUESTION"),
        "PSG Programme Handbook_Oct 2024":os.getenv("DEMO_DATABASE_US_PSG"),
    },
}




def get_connection_str(uni_name, doc_name):
    db = DATABASES[uni_name][doc_name]
    connection_str = f"postgresql+psycopg2://{user}:{password}@{host}:5432/{db}"
    return connection_str


@st.cache_resource
def get_retriever(uni_name, doc_name):
    vector_store = PGVector(
        embedding_function=text_embedding_3large,
        collection_name=collection_name,
        connection_string=get_connection_str(uni_name=uni_name, doc_name=doc_name),
    )

    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 1,
            "score_threshold": 0.5
        }
    )
    return retriever



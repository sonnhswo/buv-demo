# from application.const import DATABASES
import sys
import os
from dotenv import load_dotenv, find_dotenv

from models.chat import azure_openai
from models.embeddings import text_embedding_3large

from langchain.vectorstores.pgvector import PGVector
from langchain.retrievers import MultiVectorRetriever
from langchain.storage import InMemoryStore, LocalFileStore
from langchain.storage._lc_store import create_kv_docstore

from langchain_community.vectorstores import Chroma

import streamlit as st

__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# print(os.getcwd())
# load_dotenv(find_dotenv('.env'))

host = os.getenv("DEMO_PG_VECTOR_HOST")
user = os.getenv("DEMO_PG_VECTOR_USER")
password = os.getenv("DEMO_PG_VECTOR_PASSWORD")
collection_name = os.getenv("COLLECTION_NAME")
print(f"host: {host}, user: {user}, password: {password}, collection_name: {collection_name}")


#----------------------------
DATABASES = {
    "Arts University Bournemouth": os.getenv("DEMO_AUB"),
    "British University Vietnam": os.getenv("DEMO_IHMFE"),
    "Staffordshire University": os.getenv("DEMO_SU"),
    "University of London- Undergraduate": os.getenv("DEMO_UOL"),
    "University of London- International Foundation Programme": os.getenv("DEMO_IFP"),
    "University of Stirling": os.getenv("DEMO_US"),
}


def get_connection_str(uni_name):
    print(f"uni_name: {uni_name}")
    db = DATABASES[uni_name]
    print(f"db: {db}")
    # connection_str = f"postgresql+psycopg2://{user}:{password}@{host}:5432/{db}"
    connection_str = f"postgresql+psycopg2://{user}:{password}@{host}:5432/{db}"
    return connection_str


@st.cache_resource
def get_retriever(uni_name):
    print("get_retriever for:", uni_name)
    if uni_name == "Arts University Bournemouth":
        vector_store = PGVector(
            embedding_function=text_embedding_3large,
            collection_name=collection_name,
            connection_string=get_connection_str(uni_name=uni_name),
        )

        retriever = vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": 1,
                "score_threshold": 0.5
            }
        )
        return retriever
    elif uni_name == "British University Vietnam":
        vectorstore_chunk_zie_400 = Chroma(
            persist_directory="./processed_data/chroma_db/buv_embedding_400_large_with_source", embedding_function=text_embedding_3large
        )
        # The storage layer for the parent documents
        # store = InMemoryStore()
        fs = LocalFileStore(
            "./processed_data/parent_document_store/buv_embedding_large_with_source")
        store = create_kv_docstore(fs)
        parent_document_retriever = MultiVectorRetriever(
            vectorstore=vectorstore_chunk_zie_400,
            docstore=store,
            search_kwargs={"k": 2},
        )
        return parent_document_retriever
    elif uni_name == "Staffordshire University":
        vectorstore_chunk_zie_400 = Chroma(
            persist_directory="./processed_data/chroma_db/su_embedding_400_large_with_source", embedding_function=text_embedding_3large
        )
        # The storage layer for the parent documents
        # store = InMemoryStore()
        fs = LocalFileStore(
            "./processed_data/parent_document_store/su_embedding_large_with_source")
        store = create_kv_docstore(fs)
        parent_document_retriever = MultiVectorRetriever(
            vectorstore=vectorstore_chunk_zie_400,
            docstore=store,
            search_kwargs={"k": 2},
        )
        return parent_document_retriever
    elif uni_name == "University of London- Undergraduate":
        vector_store = PGVector(
            embedding_function=text_embedding_3large,
            collection_name=collection_name,
            connection_string=get_connection_str(uni_name=uni_name),
        )

        retriever = vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": 1,
                "score_threshold": 0.5
            }
        )
        return retriever
    elif uni_name == "University of London- International Foundation Programme":
        vector_store = PGVector(
            embedding_function=text_embedding_3large,
            collection_name=collection_name,
            connection_string=get_connection_str(uni_name=uni_name),
        )

        retriever = vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": 1,
                "score_threshold": 0.5
            }
        )
        return retriever
    elif uni_name == "University of Stirling":
        vector_store = PGVector(
            embedding_function=text_embedding_3large,
            collection_name=collection_name,
            connection_string=get_connection_str(uni_name=uni_name),
        )

        retriever = vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": 1,
                "score_threshold": 0.5
            }
        )
        return retriever
    #
    # collection_string = get_connection_str(uni_name=uni_name)
    # print("here:", collection_string)
    # vector_store = PGVector(
    #     embedding_function=text_embedding_3large,
    #     # embedding_function=embeddings,
    #     collection_name=collection_name,
    #     connection_string=collection_string,
    # )
    # return


import streamlit as st
from application import const



def get_prompt_ans(question):


    retriever = const.AUB_frequentlyaskedquestion_retriever
    retrieved = retriever.get_relevant_documents(question)
    print(retrieved)
    # return question+"answer", [question + "suggestion 1", question + "suggestion 2", question + "suggestion 3"]
    return retrieved[0].metadata["answer"]
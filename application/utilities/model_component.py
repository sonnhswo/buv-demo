import streamlit as st
from application.utilities import db_component


#------------ retriever
AUB_frequentlyaskedquestion_retriever = db_component.get_retriever(uni_name="Arts University Bournemouth (AUB)", doc_name="AUB-OCT24-FREQUENTLY ASKED QUESTIONS")
US_frequentlyaskedquestion_retriever = db_component.get_retriever(uni_name="Arts University Bournemouth (AUB)", doc_name="AUB-OCT24-FREQUENTLY ASKED QUESTIONS")

#------------ cache mapping uni name and retriever
@st.cache_resource
def get_cached_retriever():
    cached_retriever = {
        "Arts University Bournemouth (AUB)": {
            "Student handbook (pending)": "",
            "AUB-OCT24-FREQUENTLY ASKED QUESTIONS": AUB_frequentlyaskedquestion_retriever,
            "PSG Programme Handbook_Oct 2024": "",
        },

        "British University Vietnam (IHM/FE)": "",
        "Staffordshire University (SU)": "",
        "University of London- Undergraduate (UoL)": "",
        "University of London- International Foundation Programme (IFP)": "",
        "University of Stirling (US)": {
            "Student handbook (pending)": "",
            "US-OCT24-FREQUENTLY ASKED QUESTIONS": US_frequentlyaskedquestion_retriever,
            "PSG Programme Handbook_Oct 2024": "",
        },
    }
    return cached_retriever


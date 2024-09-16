import streamlit as st
from application.utilities import db_component


#------------ retriever
AUB_studenthandbook = "" # db_component.get_retriever(uni_name="Arts University Bournemouth (AUB)", doc_name="Student handbook (pending)")
AUB_frequentlyaskedquestion_retriever = db_component.get_retriever(uni_name="Arts University Bournemouth (AUB)", doc_name="AUB-OCT24-FREQUENTLY ASKED QUESTIONS")
AUB_PSG = db_component.get_retriever(uni_name="Arts University Bournemouth (AUB)", doc_name="PSG Programme Handbook_Oct 2024")

# IHMFE_studenthandbook = ""
# IHMFE_frequentlyaskedquestion_retriever = ""
# IHMFE_PSG = ""

# SU_studenthandbook = ""
# SU_frequentlyaskedquestion_retriever = ""
# SU_PSG = ""

# UoL_studenthandbook = ""
# UoL_frequentlyaskedquestion_retriever = ""
# UoL_PSG = ""

# IFP_studenthandbook = ""
# IFP_frequentlyaskedquestion_retriever = ""

US_studenthandbook = ""
US_frequentlyaskedquestion_retriever = db_component.get_retriever(uni_name="University of Stirling (US)", doc_name="US-OCT24-FREQUENTLY ASKED QUESTIONS")
US_PSG = ""

#------------ cache mapping uni name and retriever
@st.cache_resource
def get_cached_retriever():
    cached_retriever = {
        "Arts University Bournemouth (AUB)": {
            "Student handbook (pending)": "",
            "AUB-OCT24-FREQUENTLY ASKED QUESTIONS": AUB_frequentlyaskedquestion_retriever,
            "PSG Programme Handbook_Oct 2024": AUB_PSG,
        },

        "British University Vietnam (IHM/FE)": {
            "Student handbook (pending)": "",
            "BUV-OCT24-FREQUENTLY ASKED QUESTIONS": "",
            "PSG Programme Handbook_Oct 2024": "",
        },

        "Staffordshire University (SU)": {
            "Student handbook (pending)": "",
            "SU-OCT24-FREQUENTLY ASKED QUESTIONS": "",
            "PSG Programme Handbook_Oct 2024": "",
        },

        "University of London- Undergraduate (UoL)": {
            "Student handbook (pending)": "",
            "UoL-OCT24-FREQUENTLY ASKED QUESTIONS": "",
            "PSG Programme Handbook_Oct 2024": "",
        },
        "University of London- International Foundation Programme (IFP)": {
            "Student handbook (pending)",
            "IFP-OCT24-FREQUENTLY ASKED QUESTIONS",
        },
        "University of Stirling (US)": {
            "Student handbook (pending)": "",
            "US-OCT24-FREQUENTLY ASKED QUESTIONS": US_frequentlyaskedquestion_retriever,
            "PSG Programme Handbook_Oct 2024": "",
        },
    }
    return cached_retriever


import streamlit as st
from application.utilities import db_component


#------------ retriever
AUB_retriever = db_component.get_retriever(uni_name="Arts University Bournemouth")
IHMFE_retriever = db_component.get_retriever(uni_name="British University Vietnam")
SU_retriever = db_component.get_retriever(uni_name="Staffordshire University")
UoL_retriever = db_component.get_retriever(uni_name="University of London- Undergraduate")
IFP_retriever = db_component.get_retriever(uni_name="University of London- International Foundation Programme")
US_retriever = db_component.get_retriever(uni_name="University of Stirling")

#------------ cache mapping uni name and retriever
@st.cache_resource
def get_cached_retriever():
    cached_retriever = {
        "Arts University Bournemouth": AUB_retriever,
        "British University Vietnam": IHMFE_retriever,
        "Staffordshire University": SU_retriever,
        "University of London- Undergraduate": UoL_retriever,
        "University of London- International Foundation Programme": IFP_retriever,
        "University of Stirling": US_retriever,
    }
    return cached_retriever

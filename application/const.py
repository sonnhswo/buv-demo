import streamlit as st
from application.utilities import db_component
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('../.env'))


list_of_uni = [
    "Arts University Bournemouth",
    "British University Vietnam",
    "Staffordshire University",
    "University of London- Undergraduate",
    "University of London- International Foundation Programme",
    "University of Stirling"
]

doc_of_uni = {
    "Arts University Bournemouth (AUB)": [
        "Student handbook (pending)",
        "AUB-OCT24-FREQUENTLY ASKED QUESTIONS",
        "PSG Programme Handbook_Oct 2024",
    ],
    "British University Vietnam (IHM/FE)": [
        "Student handbook (pending)",
        "BUV-OCT24-FREQUENTLY ASKED QUESTIONS",
        "PSG Programme Handbook_Oct 2024",
    ],
    "Staffordshire University (SU)": [
        "Student handbook (pending)",
        "SU-OCT24-FREQUENTLY ASKED QUESTIONS",
        "PSG Programme Handbook_Oct 2024",
    ],
    "University of London- Undergraduate (UoL)": [
        "Student handbook (pending)",
        "UoL-OCT24-FREQUENTLY ASKED QUESTIONS",
        "PSG Programme Handbook_Oct 2024",
    ],
    "University of London- International Foundation Programme (IFP)": [
        "Student handbook (pending)",
        "IFP-OCT24-FREQUENTLY ASKED QUESTIONS",

    ],
    "University of Stirling (US)": [
        "Student handbook (pending)",
        "US-OCT24-FREQUENTLY ASKED QUESTIONS",
        "PSG Programme Handbook_Oct 2024",
    ]
}


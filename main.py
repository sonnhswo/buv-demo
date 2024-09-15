import streamlit as st
from sqlalchemy.sql.functions import random

from application.utilities.home_component import expander_button
from application.const import list_of_uni, doc_of_uni

# initial session state of all variables
if 'item_selected' not in st.session_state:
    st.session_state.item_selected = None

# Sidebar with main buttons
st.sidebar.markdown("### University")

for uni_name in list_of_uni:
    doc_list = doc_of_uni[uni_name]
    expander_button(uni_name, doc_list)

# display main page content

if st.session_state.item_selected:
    st.write(f"you chosen: {st.session_state.item_selected}")
else:
    st.write("Please select an option from sidebar")

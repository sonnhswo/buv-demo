import streamlit as st




def expander_button(uni_name, doc_list):

    with st.sidebar.expander(uni_name, expanded=False):
        for idx,doc in enumerate(doc_list):
            if st.button(doc, key="button" + str(doc) + str(uni_name)):
                st.session_state.item_selected = doc




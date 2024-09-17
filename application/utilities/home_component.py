import streamlit as st
from PIL import Image

# Load the image
image_path = "./data/img/Starleo.png"
image = Image.open(image_path)


def display_homepage():
    col1, col2, col3 = st.columns([0.2, 0.05, 0.75], gap="small")
    col1.image(image_path, width=150)
    col3.markdown("<div style='margin-top:30px;'></div>", unsafe_allow_html=True)
    col3.title("Student Information Hub")

    with st.chat_message("assistant", avatar="./data/img/BUV_assistant_icon.png"):
        st.write("Hi, I’m StarLeo, I’m happy to assist you!")
        st.write("Please select your awarding body for our further support. "
                 "If you are a dual degree student, please select the option "
                 "'British University Vietnam'.",)



def expander_button(uni_name, doc_list):

    with st.sidebar.expander(uni_name, expanded=False):

        for idx,doc in enumerate(doc_list):
            if st.button(doc, key="button" + str(doc) + str(uni_name)):
                st.session_state.item_selected = doc
                st.session_state.uni_name = uni_name




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

    # # Inject custom CSS to make the button smaller
    # st.markdown(
    #     """
    #     <style>
    #     .small-button {
    #         font-size: 20px !important;
    #         padding: 5px 10px !important;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )

    with st.chat_message("assistant", avatar="./data/img/Starleo_himate.png"):
        st.write("Hi, I’m StarLeo, I’m happy to assist you!")
        st.write("Please select your awarding body for our further support. "
                 "If you are a dual degree student, please select the option "
                 "'British University Vietnam'.",)


def show_doc_sidebar(option):
    on = st.sidebar.toggle("Show Documents", value=True)
    # Define constants for URLs and messages
    BUV_FAQ_URL = "https://buvbus.blob.core.windows.net/docs/BUV-JUL24-FAQ.pdf"
    SU_FAQ_URL = "https://buvbus.blob.core.windows.net/docs/SU-JUL24-FAQ.pdf"

    DISCLAIMER_MESSAGE = (
        "Before you begin using our chat services, please note that the information \
        provided by this chatbot is intended for reference purposes only. For more \
        information visit [Chatbot Disclaimer and Guidelines](https://buvbus.blob.core.windows.net/docs/Chatbot_Disclaimer_190824.pdf)."
    )

    SURVEY_MESSAGE = (
        "To help us improve and serve you better, we’d love to hear your thoughts and \
        experiences. Please take a moment to share your feedback by filling out this \
        short survey [User Experience Survey](https://forms.office.com/r/EwP0Cg8exN)"
    )

    # Sidebar content based on selection
    with st.sidebar:
        if on:
            st.empty()
            st.markdown(
                "[Student Handbook 2023-2024](https://buvbus.blob.core.windows.net/docs/Student%20Handbook%202023-2024.pdf)"
            )
            st.markdown(
                "[PSG Programme Handbook](https://buvbus.blob.core.windows.net/docs/PSG%20Programme%20Handbook.pdf)")
            st.markdown(f"[BUV-JUL24-FAQ]({BUV_FAQ_URL})")


    # Add the disclaimer to the bottom of the left sidebar
    st.markdown(DISCLAIMER_MESSAGE)

    # Add the survey to the bottom of the left sidebar
    st.markdown(SURVEY_MESSAGE)


def expander_button(uni_name, doc_list):

    with st.sidebar.expander(uni_name, expanded=False):

        for idx,doc in enumerate(doc_list):
            if st.button(doc, key="button" + str(doc) + str(uni_name)):
                st.session_state.item_selected = doc
                st.session_state.uni_name = uni_name




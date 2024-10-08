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
        # st.write("Please select your awarding body for our further support. "
        #          "If you are a dual degree student, please select the option "
        #          "'British University Vietnam'.",)


def show_doc_sidebar(option):
    on = st.sidebar.toggle("Show Documents", value=True)
    # Define constants for URLs and messages
    AUB_FAQ_URL = "https://buvbus.blob.core.windows.net/docs/AUB_OCT24_FREQUENTLY_ASKED_QUESTIONS.pdf"
    BUV_FAQ_URL = "https://buvbus.blob.core.windows.net/docs/BUV_OCT24_FREQUENTLY_ASKED_QUESTIONS.pdf"
    SU_FAQ_URL = "https://buvbus.blob.core.windows.net/docs/SU_OCT24_FREQUENTLY_ASKED_QUESTIONS.pdf"
    UOL_FAQ_URL = "https://buvbus.blob.core.windows.net/docs/UoL_OCT24_FREQUENTLY_ASKED_QUESTIONS.pdf"
    IFP_FAQ_URL = "https://buvbus.blob.core.windows.net/docs/IFP_OCT24_FREQUENTLY_ASKED_QUESTIONS.pdf"
    STIRLING_FAQ_URL = "https://buvbus.blob.core.windows.net/docs/STIRLING_OCT24_FREQUENTLY_ASKED_QUESTIONS.pdf"

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
            if option == "Home":
                st.markdown(
                    "[Student Handbook 2023-2024](https://buvbus.blob.core.windows.net/docs/Student%20Handbook%202023-2024.pdf)"
                )
                st.markdown(
                    "[PSG Programme Handbook](https://buvbus.blob.core.windows.net/docs/PSG_Programme_Handbook_Oct_2024.pdf)")
                # Add the disclaimer to the bottom of the left sidebar
                st.markdown(DISCLAIMER_MESSAGE)

                # Add the survey to the bottom of the left sidebar
                st.markdown(SURVEY_MESSAGE)
            elif option == "Arts University Bournemouth":
                st.markdown(f"[AUB-FAQ]({AUB_FAQ_URL})")
            elif option == "British University Vietnam":
                st.markdown(f"[BUV-FAQ]({BUV_FAQ_URL})")
            elif option == "Staffordshire University":
                st.markdown(f"[SU-FAQ]({SU_FAQ_URL})")
            elif option == "University of London- Undergraduate":
                st.markdown(f"[UOL-FAQ]({UOL_FAQ_URL})")
            elif option == "University of London- International Foundation Programme":
                st.markdown(f"[IFP-FAQ]({IFP_FAQ_URL})")
            elif option == "University of Stirling":
                st.markdown(f"[STIRLING-FAQ]({STIRLING_FAQ_URL})")




def expander_button(uni_name, doc_list):

    with st.sidebar.expander(uni_name, expanded=False):

        for idx,doc in enumerate(doc_list):
            if st.button(doc, key="button" + str(doc) + str(uni_name)):
                st.session_state.item_selected = doc
                st.session_state.uni_name = uni_name




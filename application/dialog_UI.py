import streamlit as st
import time
# from application.app_AUB import get_prompt_ans

from application.agents import ChatMemoryAgent


def dialog(uni_name):

    #-------------- get the right retriever
    # st.header(str(uni_name))



    chat_history = []

    # Streamed response emulator
    def response_generator(answer):
        for word in str(answer).split():
            yield word + " "
            time.sleep(0.05)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Initialize suggested questions
    if "suggested_questions" not in st.session_state:
        st.session_state.suggested_questions = []

    # Initialize selected questions
    if "selected_questions" not in st.session_state:
        st.session_state.selected_questions = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        if message["role"] == "user":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        if message["role"] == "assistant":
            with st.chat_message(message["role"], avatar="data/img/BUV_assistant_icon.png"):
                st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Hi! How can I help you?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Update session state
        # answer, suggested_questions = app_AUB.get_prompt_ans(prompt)
        answer = ChatMemoryAgent.get_answer(uni_name=uni_name,
                                            question=prompt)
        # answer = "answer 1 "

        # Display assistant response in chat message container
        with st.chat_message("assistant", avatar="data/img/BUV_assistant_icon.png"):
            response = st.write_stream(response_generator(answer))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        # # Update suggested questions
        # st.session_state.suggested_questions = suggested_questions

    # # Display suggested questions
    # st.markdown("### Suggested Questions")
    # for idx,question in enumerate(st.session_state.suggested_questions):
    #     if st.button(question, key="question_"+str(idx)):
    #         # Add the selected question to the list of selected questions
    #         st.session_state.selected_questions.append(question)
    #
    #         # Add user message to chat history
    #         st.session_state.messages.append({"role": "user", "content": question})
    #         # Display user message in chat message container
    #         with st.chat_message("user"):
    #             st.markdown(question)
    #
    #         # Display assistant response in chat message container
    #         with st.chat_message("assistant", avatar="data/img/BUV_assistant_icon.png"):
    #             # get the answer and suggested questions from vectordb
    #             try:
    #                 # answer, suggested_questions = app_AUB.get_prompt_ans(question)
    #                 answer = app_AUB.get_prompt_ans(question)
    #             except:
    #                 answer = "Sorry, I cannot find related information."
    #                 # suggested_questions = []
    #             # display answer
    #             response = st.write_stream(response_generator(answer))
    #         # Add assistant response to chat history
    #         st.session_state.messages.append({"role": "assistant", "content": response})
    #         # # Update suggested questions
    #         # st.session_state.suggested_questions = suggested_questions
    #         st.rerun()

    # # Display selected questions
    # st.markdown("### Selected Questions")
    # for selected_question in st.session_state.selected_questions:
    #     st.markdown(f"- {selected_question}")
    # st.write("Giá trị hiện tại của biến:", st.session_state.state)
import streamlit as st
from streamlit_float import *

import os
import time

# from application.app_AUB import get_prompt_ans
from application.agents import ChatMemoryAgent

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils import retriever as retriever_for_unclear_question
from utils import language_detection_chain, FAQ

from backend import buv_with_direct_prompting_source_and_follow_up, su_with_direct_prompting_source_and_follow_up

from langchain_community.chat_message_histories import (
    StreamlitChatMessageHistory,
)

host = os.getenv("PG_VECTOR_HOST")
user = os.getenv("PG_VECTOR_USER")
password = os.getenv("PG_VECTOR_PASSWORD")
database = os.getenv("PGDATABASE5")
pgport = os.getenv("PGPORT")
# COLLECTION_NAME = "langchain_collection"
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
CONNECTION_STRING = f"postgresql+psycopg2://{user}:{password}@{host}:{pgport}/{database}"



# Using streamlit_float for the chat input bar
float_init(theme=True, include_unstable_primary=False)


def dialog(uni_name):

    #-------------- get the right retriever
    # st.header(str(uni_name))
    
    # Create an engine that connects to the PostgreSQL database
    engine = create_engine(CONNECTION_STRING)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()


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


    def delete_messages_session_state():
        """
        Delete the 'messages' key from the session state if it exists.
        """
        st.session_state.pop("messages", None)
        
    with st.container():
        # Create a 2 column layout
        col4, col5 = st.columns([0.85, 0.15])
        with col5:
            reset_button_b_pos = "-42rem"
            # reset_button_css = float_css_helper(width="12rem", bottom=reset_button_b_pos, right="0rem", transition=0)
            reset_button_css = float_css_helper(width="12rem", bottom=reset_button_b_pos)
            float_parent(css=reset_button_css)
            if st.button("Reset Chat", key="reset_chat", help="Click to reset chat history"):
                delete_messages_session_state()
                st.rerun()
                
        with col4:
            prompt = st.chat_input("Hi! How can I help you?")
            button_b_pos = "-42rem"
            # button_css = float_css_helper(width="2.2rem", bottom=button_b_pos, transition=0)
            button_css = float_css_helper(width="2.2rem", bottom=button_b_pos)
            float_parent(css=button_css)
        
        PATH_BUV_ASSISTANT_ICON = "./data/img/BUV_assistant_icon.png"
        
        # Accept user input
        if prompt:
            if uni_name == "Arts University Bournemouth":
                pass
            elif uni_name == "British University Vietnam":
                
                
                message_history = StreamlitChatMessageHistory(key="buv_follow_up_memory")
                bot_engine = buv_with_direct_prompting_source_and_follow_up.chain_with_follow_up_function(message_history)
                
                
                st.session_state.messages.append({"role": "user", "content": prompt})
                st.chat_message("user").write(prompt)

                with st.spinner("Processing data ..."):
                    with st.chat_message("assistant", avatar=PATH_BUV_ASSISTANT_ICON):
                        st.write("For BUV students:")
                        print("prompt", prompt)
                        language_detection = language_detection_chain.invoke({"input": prompt})
                        print("language_detection", language_detection)
                        if language_detection == "Vietnamese":
                            response = "We're sorry for any inconvenience; however, StarLeo can only answer questions in English. Unfortunately, Vietnamese isn't available at the moment. Thank you for your understanding!"
                            st.write(response)
                        else:
                            # print(
                            #     buv_with_direct_prompting_source_and_follow_up.demo_ephemeral_chat_history.messages)
                            # context_q_chain = buv_with_direct_prompting_source_and_follow_up.contextualize_q_prompt | gpt_4o | StrOutputParser()
                            # q_with_context = context_q_chain.invoke({"input": prompt,
                            #                                          "chat_history": buv_with_direct_prompting_source_and_follow_up.demo_ephemeral_chat_history.messages})
                            # print(
                            #     f"Latest question: {prompt} \nNew query: {q_with_context}")
                            stream_response = bot_engine.stream(
                                {"input": prompt},
                                {"configurable": {"session_id": "unused"}},
                            )
                            print("stream_response", stream_response)
                            response = st.write_stream(stream_response)

                st.session_state.messages.append(
                    {"role": "assistant", "content": "For BUV students:" + "\n\n" + response})
                # Create a new FAQ instance
                new_faq = FAQ(question=prompt, answer=response, bot_type=uni_name)
                # Add the new instance to the session
                session.add(new_faq)
                # Commit the session to insert the data into the table
                session.commit()
                session.close()
            elif uni_name == "Staffordshire University":
                
                message_history = StreamlitChatMessageHistory(key="su_follow_up_memory")
                bot_engine = su_with_direct_prompting_source_and_follow_up.chain_with_follow_up_function(message_history)
                
                retrieved = retriever_for_unclear_question.invoke(prompt)
                if retrieved:
                    handled_prompt, answer = retrieved[0].page_content, retrieved[0].metadata['answer']
                    answer = None if answer == " " else answer
                else:
                    handled_prompt, answer = prompt, None
                
                st.session_state.messages.append({"role": "user", "content": prompt})
                st.chat_message("user").write(prompt)
                
                with st.spinner("Processing data ..."):
                    with st.chat_message("assistant", avatar=PATH_BUV_ASSISTANT_ICON):
                        st.write("For SU students:")
                        language_detection = language_detection_chain.invoke(
                            {"input": prompt})
                        print("language_detection", language_detection)
                        if language_detection == "Vietnamese":
                            response = "We're sorry for any inconvenience; however, StarLeo can only answer questions in English. Unfortunately, Vietnamese isn't available at the moment. Thank you for your understanding!"
                            st.write(response)
                        else:
                            if answer:
                                response = answer
                                st.write(response)
                            else:
                                stream_response = bot_engine.stream(
                                    {"input": handled_prompt},
                                    {"configurable": {"session_id": "unused"}},
                                )
                                print("stream_response", stream_response)
                                response = st.write_stream(stream_response)

                st.session_state.messages.append(
                    {"role": "assistant", "content": "For SU students:" + "\n\n" + response})
                # Create a new FAQ instance
                new_faq = FAQ(question=prompt, answer=response, bot_type=uni_name)
                # Add the new instance to the session
                session.add(new_faq)
                # Commit the session to insert the data into the table
                session.commit()
                session.close()
                
            elif uni_name == "University of London- Undergraduate":
                pass
            elif uni_name == "University of London- International Foundation Programme":
                pass
            elif uni_name == "University of Stirling":
                pass
            
            # ==========NOT USED IT FOR NOW================================
            # # Add user message to chat history
            # st.session_state.messages.append({"role": "user", "content": prompt})
            # # Display user message in chat message container
            # with st.chat_message("user"):
            #     st.markdown(prompt)

            # # Update session state
            # # answer, suggested_questions = app_AUB.get_prompt_ans(prompt)
            # answer = ChatMemoryAgent.get_answer(uni_name=uni_name,
            #                                     question=prompt)
            # # answer = "answer 1 "

            # # Display assistant response in chat message container
            # with st.chat_message("assistant", avatar="data/img/BUV_assistant_icon.png"):
            #     response = st.write_stream(response_generator(answer))
            # # Add assistant response to chat history
            # st.session_state.messages.append({"role": "assistant", "content": response})
            # ==========================================
            
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
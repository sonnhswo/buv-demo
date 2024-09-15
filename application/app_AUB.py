import streamlit as st



def get_prompt_ans(question):
    return question+"answer", [question + "suggestion 1", question + "suggestion 2", question + "suggestion 3"]
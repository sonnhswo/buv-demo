# import sys
# import os
# project_path = os.path.abspath(os.path.join('..'))
# sys.path.append(project_path)

from application.utilities import model_component
from langchain.prompts import PromptTemplate
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from models.chat import azure_openai



cached_retriever = model_component.get_cached_retriever()


def get_answer(uni_name, doc_name, question):
    try:
        # get the right retriever
        retriever = cached_retriever[uni_name][doc_name]
        retrieved = retriever.get_relevant_documents(question)

        combine_doc = ""
        for i in retrieved:
            combine_doc = combine_doc + str(i.metadata["answer"]) + "\n"

        # template
        template = f"""You are a chatbot specialized in answering frequently asked questions from customers about the student shuttle bus service \
        provided by BUV.\n
    
        Use exactly this following information as your answer: {combine_doc}
        
        Current conversation:\n{{history}}\n
        Human: {{input}}\nAI:"""

        # prompt_template = BasePromptTemplate(
        prompt_template = PromptTemplate(
            input_variables=['history', 'input'],
            template=template
        )

        conversation_buf = ConversationChain(
            llm=azure_openai,
            memory=ConversationBufferMemory(),
            prompt=prompt_template,
        )

        # get the answer
        answer = conversation_buf.invoke({
            "input": question
        })

        return answer["response"]
    except Exception as e:
        return "Sorry, I cannot answer your question ..."
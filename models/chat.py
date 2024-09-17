from dotenv import load_dotenv, find_dotenv
from langchain_openai import AzureChatOpenAI
import os

# load_dotenv(find_dotenv("../.env"))


# Azure model
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

# azure_openai = AzureChatOpenAI(
#     # openai_api_version="2023-05-15",
#     openai_api_version="2024-05-01-preview",

#     # azure_deployment="apac-gpt-35-turbo",
#     azure_deployment="demo-gpt-35-turbo-16k",
#     temperature=0
# )

azure_openai = AzureChatOpenAI(
    # openai_api_version="2023-05-15",
    openai_api_version="2024-05-01-preview",
    azure_deployment="Chat_Models",
    temperature=0
)


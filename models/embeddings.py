from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAIEmbeddings, AzureOpenAIEmbeddings
import os

# load_dotenv(find_dotenv("../.env"))

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

# text_embedding_3large = AzureOpenAIEmbeddings(
#     # model="apac-text-embedding-3-large",
#     model="demo-text-embedding-3-large",

#     openai_api_version="2022-12-01",
#     openai_api_key=AZURE_OPENAI_API_KEY,
#     azure_endpoint=AZURE_OPENAI_ENDPOINT,
# )

text_embedding_3large = AzureOpenAIEmbeddings(
    model="Embedding_Models",
    openai_api_version="2022-12-01",
    openai_api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)



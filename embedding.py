from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import os

CHROMA_PATH = 'chroma'
os.environ["OPENAI_API_KEY"] = 'your api key'

def get_embedding_function():
    embedding = OpenAIEmbeddings(
                model="text-embedding-3-large"
                # With the `text-embedding-3` class
                # of models, you can specify the size
                # of the embeddings you want returned.
                # dimensions=1024
            )
    return embedding
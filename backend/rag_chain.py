# Install new provider if not already
# pip install langchain-openai

from langchain_openai import OpenAI  # Correct import for new OpenAI wrapper
from langchain.chains import RetrievalQA  # ✅ Correct
from backend.embeddings import load_vector_store
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable is missing. Please set it in the .env file.")

llm = OpenAI(api_key=openai_api_key, temperature=0)
retriever = load_vector_store().as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

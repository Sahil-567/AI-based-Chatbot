from backend.rag_chain import qa_chain
from langchain_openai import OpenAI
import os
from dotenv import load_dotenv

# Load OpenAI API key from the .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI LLM as fallback
llm_fallback = OpenAI(api_key=openai_api_key, temperature=0.7)

def get_agent_response(query: str):
    # Ensure qa_chain is loaded correctly
    if qa_chain is None:
        raise ValueError("QA chain is not initialized properly.")
    
    # First, try to get the response from the knowledge base (RAG + FAISS)
    print("🔍 Trying to answer with RAG...")
    response = qa_chain.run(query)

    # If the response from the knowledge base is meaningful (not empty or irrelevant), return it
    if response and "I don't know" not in response and response.strip():
        print("✅ Answer found in knowledge base.")
        return f"[From Knowledge Base 📚]: {response}"

    # Otherwise, fallback to OpenAI API for a general response
    print("🤖 Falling back to OpenAI API...")
    return f"[From OpenAI 🤖]: {llm_fallback.invoke(query)}"

# frontend/streamlit_app.py
import streamlit as st
import requests

st.set_page_config(page_title="RAG Chatbot", layout="centered")
st.title("💬 RAG Chatbot (OpenAI + LangChain)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
user_input = st.chat_input("Ask something...")

if user_input:
    # Show user's message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking... 🤖"):
        try:
            response = requests.post(
                "http://localhost:8000/chat",
                json={"message": user_input},
                timeout=15,
            )
            response.raise_for_status()
            bot_reply = response.json().get("response", "🤖 No reply found.")
        except requests.exceptions.RequestException as e:
            bot_reply = f"❌ Error: {e}"

        # Save bot reply
        st.session_state.messages.append({"role": "bot", "content": bot_reply})

# Display conversation history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**🧑‍💻 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 Bot:** {msg['content']}")

import streamlit as st
from groq import Groq

# Initialize Groq client
client = Groq(api_key="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")

st.title("🤖 ChatGPT Clone")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from Groq
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",   # fast + free
    messages=st.session_state.messages
    )

    bot_reply = response.choices[0].message.content

    # Save bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.markdown(bot_reply)
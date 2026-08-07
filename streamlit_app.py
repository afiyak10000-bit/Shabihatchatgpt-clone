import streamlit as st
from groq import Groq

st.set_page_config(page_title="Shabi GPT", page_icon="🤖")
st.title("🤖 Shabi GPT Clone ")

api_key = st.text_input("Paste your Groq API Key here", type="password")
if not api_key:
    st.warning("👆 Please enter your Groq API Key to start")
    st.stop()

client = Groq(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What do you want to ask?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            chat_completion = client.chat.completions.create(
                messages=st.session_state.messages,
                model="llama3-8b-8192",
            )
            response = chat_completion.choices[0].message.content
            st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

import streamlit as st

st.set_page_config(
    page_title="ShabiGPT",
    page_icon="🤖"
)

st.title("🤖 ShabiGPT")
st.write("Welcome to ShabiGPT! Ask me anything.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask ShabiGPT something...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    response = "I'm ShabiGPT! I'm ready to answer your questions soon. 🚀"

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

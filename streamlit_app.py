import streamlit as st
import requests

st.set_page_config(page_title="MCP Assistant", layout="wide")
st.title("Chat Assistant")

# Session history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#Simple Input box
user_input = st.text_input("You:", "")

if st.button("Send") and user_input.strip():
    try:
        res = requests.post("http://localhost:8000/chat", json={"message": user_input})
        reply = res.json().get("response", "Error: No response")
    except Exception as e:
        reply = f"Error: {e}"

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Assistant", reply))

# Displaying conversation
for speaker, msg in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {msg}")

import streamlit as st
import openai
from datetime import datetime
# Page config
with open('index.html', 'r', encoding='utf-8') as f:
   html_template = f.read()

# You can then process this template (e.g., with a templating engine)
# or directly serve it.
print(html_template)
st.set_page_config(page_title="Buddy - An Interactive Chatbot", page_icon="🤖")
# Custom CSS for better UI
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        border-radius: 20px;
        padding: 10px 15px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #4CAF50;
        color: white;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 1rem;
        margin-bottom: 1rem;
        display: inline-block;
        max-width: 80%;
    }
    .user-message {
        background-color: #e3f2fd;
        margin-left: 20%;
    }
    .bot-message {
        background-color: #f1f1f1;
        margin-right: 20%;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi there! I'm Buddy, your personal chatbot. How can I help you today?"}
    ]

# Sidebar for API key and settings
with st.sidebar:
    st.title("LOGIN PAGE")
    openai_api_key = st.text_input("Enter Email ID:", type="password")
    st.markdown("[Forgot your Email?](https://support.google.com/accounts/answer/7682439?hl=en)")
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("Buddy is your personal chatbot assistant. Ask me anything!")
    st.markdown("Built by Students of Presidency University")

# Main chat interface
st.title("🤖 Buddy - An Interactive Chatbot Designed by Us")
  # Add user message to chat history
   # st.session_state.messages.append({"role": "user", "content": prompt})
    
    
    # Add assistant response to chat history
    #st.session_state.messages.append({"role": "assistant", "content": full_response})

















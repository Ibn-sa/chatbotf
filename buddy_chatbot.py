import streamlit as st
import openai
from datetime import datetime

# Page config
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
    st.title("🔑 Settings")
    openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    st.markdown("[Get your OpenAI API key](https://platform.openai.com/account/api-keys)")
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("Buddy is your personal chatbot assistant. Ask me anything!")
    st.markdown("Built by Students of 1PHY19")

# Main chat interface
st.title("🤖 Buddy - An Interactive Chatbot")


    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Initialize OpenAI client
            client = openai.OpenAI(api_key=openai_api_key)
            
            # Get response from OpenAI
            for response in client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                stream=True,
            ):
                if response.choices[0].delta.content is not None:
                    full_response += response.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            full_response = "I'm sorry, I encountered an error. Please check your API key and try again."
            message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})



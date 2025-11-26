import streamlit as st
import openai
from datetime import datetime
# Page config
<script>
(function(){if(!window.chatbase||window.chatbase("getState")!=="initialized"){window.chatbase=(...arguments)=>{if(!window.chatbase.q){window.chatbase.q=[]}window.chatbase.q.push(arguments)};window.chatbase=new Proxy(window.chatbase,{get(target,prop){if(prop==="q"){return target.q}return(...args)=>target(prop,...args)}})}const onLoad=function(){const script=document.createElement("script");script.src="https://www.chatbase.co/embed.min.js";script.id="hWRc78rz6juuOuzaUNB29";script.domain="www.chatbase.co";document.body.appendChild(script)};if(document.readyState==="complete"){onLoad()}else{window.addEventListener("load",onLoad)}})();
</script>
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
   # st.session_state.messages.append({"role": "user", "content": prompt})
    
    
    # Add assistant response to chat history
    #st.session_state.messages.append({"role": "assistant", "content": full_response})











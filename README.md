# 🤖 Buddy - Your Personal Chatbot

A simple and interactive chatbot built with Streamlit and OpenAI's GPT-3.5-turbo model.

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- OpenAI API key (get it from [OpenAI](https://platform.openai.com/account/api-keys))

### Installation

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd buddy-chatbot
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

1. Run the Streamlit app:
   ```bash
   streamlit run buddy_chatbot.py
   ```

2. Open your browser and go to `http://localhost:8501`

3. Enter your OpenAI API key in the sidebar and start chatting with Buddy!

## 🌐 Deploying to Streamlit Cloud

1. Push your code to a GitHub repository

2. Go to [Streamlit Cloud](https://streamlit.io/cloud)

3. Click on "New app" and select your repository

4. Set the following:
   - Branch: `main` (or your default branch)
   - Main file path: `buddy_chatbot.py`

5. Click "Deploy!"

6. Once deployed, go to the app settings and add your OpenAI API key as a secret in the "Secrets" section:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## 🔒 Security Note

Never share your OpenAI API key or commit it to version control. The app will prompt users to enter their own API key when running locally.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

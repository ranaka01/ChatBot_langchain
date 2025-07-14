# LangChain Chatbot with LLAMA3 and Chat History

This project is a simple chatbot web application built using [LangChain](https://python.langchain.com/), [Streamlit](https://streamlit.io/), and the LLAMA3 model (via Ollama). It supports chat history and displays the last four turns of the conversation.

## Features
- Chat with an AI assistant powered by LLAMA3 (gemma3:1b)
- Maintains and displays chat history
- User-friendly web interface using Streamlit
- Environment variable support via `.env`

## Setup Instructions

1. **Clone the repository**

2. **Create and activate a Python virtual environment**
```powershell
python -m venv env
.\env\Scripts\activate
```

3. **Install dependencies**
```powershell
pip install -r requirements.txt
```

4. **Set up environment variables**
- Create a `.env` file in the root directory.
- Add your LangChain API key:
  ```env
  LANGCHAIN_API_KEY=your_api_key_here
  ```

5. **Run the chatbot app**
```powershell
streamlit run chatbot/localama.py
```

## File Structure
```
chatbot/
  localama.py        # Main Streamlit app
requirements.txt     # Python dependencies
.env                 # Environment variables (not included)
```

## How It Works
- The app loads environment variables and sets up LangChain tracing.
- The chat history is stored in Streamlit's session state.
- User input is processed and sent to the LLAMA3 model via LangChain.
- The AI's response and user messages are appended to the chat history.
- The last four turns of the conversation are displayed in the UI.

## Customization
- Change the model by editing the `OllamaLLM(model="gemma3:1b")` line in `localama.py`.
- Adjust the number of displayed chat turns by modifying the slice in the display loop.

## Requirements
- Python 3.11+
- Streamlit
- LangChain
- langchain_openai
- langchain_ollama
- python-dotenv

## License
This project is for educational purposes.

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Initialize Streamlit app
st.set_page_config(page_title="LangChain Chat with History")
st.title('LangChain + LLAMA3 + Chat History')

# Initialize or load session state for history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant. Please respond to the user's queries.")
    ]

# Text input from user
input_text = st.text_input("Ask me anything", key="input")

# Define the LLM
llm = OllamaLLM(model="gemma3:1b")
output_parser = StrOutputParser()

# Define prompt template with dynamic history
prompt = ChatPromptTemplate.from_messages(
    [
        MessagesPlaceholder(variable_name="history"),
        MessagesPlaceholder(variable_name="question")
    ]
)

# Create the chain
chain = prompt | llm | output_parser

# Handle user input
if input_text:
    # Add user message to history
    st.session_state.chat_history.append(HumanMessage(content=input_text))

    # Invoke the chain
    response = chain.invoke({
        "history": st.session_state.chat_history,
        "question": [HumanMessage(content=input_text)]
    })

    # Add AI response to history
    st.session_state.chat_history.append(AIMessage(content=response))

    #Display conversation history (last 4 turns)
    for message in st.session_state.chat_history[-4:]:
        if isinstance(message, HumanMessage):
            st.markdown(f"**You:** {message.content}")
        elif isinstance(message, AIMessage):
            st.markdown(f"**Bot:** {message.content}")

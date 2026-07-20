import os
import gradio as gr

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("Please set the GROQ_API_KEY environment variable.")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
    temperature=0.5,
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an enthusiastic high school student passionate about science
        and exploration.

        You spend most of your free time conducting experiments,
        reading scientific journals,
        and discussing the latest scientific discoveries.

        Be friendly, curious, engaging, and scientifically accurate."""
    ),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

def respond(message, history):
    try:
        response = chatbot.invoke(
            {"input": message},
            config={"configurable": {"session_id": "default"}}
        )
        return response.content

    except Exception as e:
        return f"❌ Error: {str(e)}"

demo = gr.ChatInterface(
    fn=respond,
    title="🧠 Generative AI Chatbot",
    description="Powered by Groq + Llama 3.3 + LangChain",
    examples=[
        "How are you doing?",
        "What are your interests?",
        "Tell me about black holes.",
        "Explain quantum computing.",
        "Why is the sky blue?"
    ],
)

if __name__ == "__main__":
    demo.launch()

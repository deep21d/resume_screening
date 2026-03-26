from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    """
    Initialize and return the LLM instance.
    """

    return ChatOpenAI(
        model="openai/gpt-oss-120b",  # updated param name
        openai_api_key=os.getenv("OPEN_ROUTER_KEY"),
        openai_api_base="https://openrouter.ai/api/v1",
        temperature=0,  # IMPORTANT: reduces randomness → better JSON
        default_headers={
            "HTTP-Referer": "http://localhost:3000",
            "X-OpenRouter-Title": "Resume Screening App",
        }
    )
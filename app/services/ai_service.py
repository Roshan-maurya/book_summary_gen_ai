import requests
import os
from dotenv import load_dotenv

load_dotenv()

def generate_summary(text):
    system_prompt = (
        "You are an expert book summarization assistant. "
        "Generate a concise, neutral, and factual summary in 4–5 sentences. "
        "Do not add opinions or information not present in the text. "
        "If the provided book content is only 2–3 lines or very short, "
        "respond with 'Cannot generate a summary: content too short.'"
    )

    if not text or len(text.replace(' ','')) <= 50:
        return "Cannot generate a summary: content too short. Please provide at least 50 words."

    
    payload = {
        "model": os.getenv('model'),
        "prompt": f"{system_prompt}\n\n{text}",
        "stream": False
    }
    response = requests.post(os.getenv('OLLAMA_URL'), json=payload)
    return response.json().get("response", "")

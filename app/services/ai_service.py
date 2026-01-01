import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_summary(text):
    print(text)
    system_prompt = (
        "You are an expert book summarization assistant. "
        "Generate a concise, neutral, and factual summary in 4–5 sentences. "
        "Do not add opinions or information not present in the text. "
        "If the provided book content is only 2–3 lines or very short, "
        "respond with 'Cannot generate a summary: content too short.'"
    )

    # print(len(text.splitlines()),'kkkkkkkkkkk')

    if not text or len(text.replace(' ','')) <= 50:
        return "Cannot generate a summary: content too short. Please provide at least 50 words."
    

    # payload = {
    #     "model": "llama3.2",
    #     "messages": [
    #         {"role": "system", "content": system_prompt},
    #         {"role": "user", "content": f"Summarize the following book content:\n{text}",}
    #     ],
    #     "stream": False
    # }

    
    payload = {
        "model": "llama3.2",
        # "system_prompt":system_prompt,
        "prompt": f"{system_prompt}\n\n{text}",
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    print(response,'response========')
    return response.json().get("response", "")

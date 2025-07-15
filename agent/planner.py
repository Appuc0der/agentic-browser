import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL", "llama3-70b-8192")

def plan_next_action(context):
    prompt = f"The user wants to: {context['goal']}. What is the first action a browser automation agent should take?"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a smart web agent helping users browse the internet and complete goals."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=body)
    print("✅ Got response from Groq!")
    print(response.json())  # optional, just to see it live

    response.raise_for_status()
    reply = response.json()["choices"][0]["message"]["content"]

    return {
        "type": "navigate",
        "description": reply,
        "url": "https://www.google.com",
        "task": "search"
    }

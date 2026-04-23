import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def call_llm(prompt):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistralai/mistral-7b-instruct",  # ✅ working model
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        data = response.json()
        print("API Response:", data)  # debug

        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        else:
            return "⚠️ AI not available right now."

    except Exception as e:
        return f"Error: {str(e)}"
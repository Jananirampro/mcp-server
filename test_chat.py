import os
import asyncio
import httpx
from dotenv import load_dotenv

# 🔐 Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "mistralai/mistral-7b-instruct:free"  # Choose a valid model from OpenRouter
PROMPT = "What is the capital of France?"

if not API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY not found in .env file")

async def call_openrouter():
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": PROMPT}
        ]
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            message = data["choices"][0]["message"]["content"]
            print("✅ OpenRouter Response:", message)
        except httpx.HTTPStatusError as e:
            print(f"❌ Error {e.response.status_code} - {e.response.text}")
        except Exception as e:
            print("❌ Unexpected Error:", str(e))

if __name__ == "__main__":
    asyncio.run(call_openrouter())

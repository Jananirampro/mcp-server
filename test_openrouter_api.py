import asyncio
from utils.router_client import call_model

# Define test input
test_message = "What is the capital of France?"
test_model = "openrouter/openchat:free"

async def test_call():
    response = await call_model(test_model, test_message)
    print("🧪 Test Prompt:", test_message)
    print("🧠 AI Response:", response)

# Run the async function
if __name__ == "__main__":
    asyncio.run(test_call())

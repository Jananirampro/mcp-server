from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import os
from pydantic import BaseModel
from utils.router_client import call_model
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    filename="mcp_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

app = FastAPI()

class ChatRequest(BaseModel):
    model: str
    message: str

@app.get("/health")
async def health_check():
    return {"status": "✅ MCP server is healthy"}

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    logging.info(f"Request received: {chat_request.model} | {chat_request.message}")
    try:
        print("👉 call_model type:", type(call_model))
        reply =  await call_model(chat_request.model, chat_request.message)
        logging.info(f"Response: {reply}")
        return {"response": reply}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"error": str(e)}

@app.get("/logs", response_class=PlainTextResponse)
async def get_logs():
    log_path = "mcp_logs.txt"
    if not os.path.exists(log_path):
        return "🚫 No logs available."

    try:
        with open(log_path, "r", encoding="utf-8") as log_file:
            content = log_file.read()
            return content if content else "📭 Log file is empty."
    except Exception as e:
        return f"❌ Error reading logs: {str(e)}"

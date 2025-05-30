# main.py
import asyncio
import sys

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

from fastapi import FastAPI
from pydantic import BaseModel
from app import run_memory_chat

app = FastAPI(title="MCP Server - AI Assistant")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"message": "MCP Server is running. Use POST /chat to talk to the assistant."}

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        response = await run_memory_chat(req.message)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}

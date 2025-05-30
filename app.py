import os
import traceback
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# MCP config file
CONFIG_FILE = "browser_mcp.json"

async def run_memory_chat(user_input: str) -> str:
    try:
        print("Initializing MCP Client from config file...")
        client = MCPClient.from_config_file(CONFIG_FILE)
        print("MCPClient initialized successfully.")

        print("Initializing Groq LLM...")
        llm = ChatGroq(model="qwen-qwq-32b")
        print("Groq LLM loaded.")

        print("Creating MCPAgent with memory...")
        agent = MCPAgent(
            llm=llm,
            client=client,
            max_steps=15,
            memory_enabled=True,
        )
        print("Agent created. Running query...")

        response = await agent.run(user_input)
        print("Assistant response received.")
        return response

    except Exception as e:
        print("Exception occurred during chat execution:")
        traceback.print_exc()
        return f"Error: {e}"

    finally:
        try:
            if 'client' in locals() and client.sessions:
                print("Closing MCP sessions...")
                await client.close_all_sessions()
                print(" Sessions closed.")
        except Exception as close_err:
            print(f"Error closing sessions: {close_err}")

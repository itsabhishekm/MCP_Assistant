# MCP based AI Assistant

This is an MCP based AI Assistant built using [Groq](https://groq.com/), [LangChain](https://www.langchain.com/), and [MCP](https://github.com/langchain-ai/mcp), with a Streamlit frontend and FastAPI backend. It enables chat interactions powered by large language models, enhanced with optional tools like search agents and browser automation.

---

## Features

- Groq LLM with LangChain and memory-enabled conversation
- MCP server such as Google Search and Playwright integration
- FastAPI backend to handle chat API requests
- Streamlit frontend for real-time chat
- Utilized Docker for containerized deployment
  
---

## Project Structure
```
MCP_Assistant/
├── app.py 
├── main.py # FastAPI server with chat endpoint
├── streamlit_app.py # streamlit frontend UI
├── browser_mcp.json # MCP servers
├── .env # Environment variables (API keys)
├── requirements.txt # required dependencies
└── README.md # You are here!
```

---

## Setup Instructions

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/itsabhishekm/MCP_Assistant.git
cd MCP_Assistant
python -m venv .venv
.venv\Scripts\activate   
pip install -r requirements.txt
```

### 2. Set Environment Variables
In the .env file in the root past your groq API KEY:
```GROQ_API_KEY=your_groq_api_key```

### 3. Configure MCP Tools (Not Required but optional)
If you want to add any other MCP server customize browser_mcp.json:
```{
  "mcpServers": {
    "google-search": {
      "command": "npx",
      "args": ["-y", "@mcp-server/google-search-mcp@latest"]
    },
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```
Or if you don't want any MCP server, just leave it empty:

``` { "mcpServers": {} } ```

## Running the app
### 1. Start FastAPI Backend

 ``` uvicorn main:app --reload --port 8000 ```

### 2. Launch Streamlit Frontend

```streamlit run streamlit_app.py```
```Visit: http://localhost:8501 ```






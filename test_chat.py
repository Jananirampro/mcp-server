import requests

response = requests.post(
    "http://127.0.0.1:8000/chat",
    json={"model": "openrouter/cypher-alpha:free", "message": "Hello MCP!"}
)

print(response.json())
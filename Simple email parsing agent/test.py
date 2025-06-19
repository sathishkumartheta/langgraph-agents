import requests

# Define the Ollama API endpoint
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

# Prompt and model
MODEL_NAME = "llama3.2:1b"
prompt = "Explain the theory of relativity in simple terms."

# JSON payload
payload = {
    "model": MODEL_NAME,
    "prompt": prompt,
    "stream": False
}

# Bypass proxies for localhost access
session = requests.Session()
session.trust_env = False  # Ignores system proxy settings

# Send the request
response = session.post(OLLAMA_URL, json=payload)

# Output the result
if response.ok:
    print("Model Response:\n", response.json()["response"])
else:
    print("Error:", response.status_code, response.text)

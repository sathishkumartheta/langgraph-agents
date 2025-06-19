import ollama

response = ollama.chat(model='llama3.2:1b', messages=[{'role': 'user', 'content': 'Explain relativity simply.'}])
print(response['message']['content'])

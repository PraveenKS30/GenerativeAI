from llama_index.llms.ollama import Ollama

llm = Ollama(model = "mistral")
response = llm.complete("Tell me a story in 20 words!")
print(response)

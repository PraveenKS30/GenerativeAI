from llama_index.llms.ollama import Ollama

llm = Ollama(model = "llama3")
response = llm.complete("Tell me a story in 20 words!")
print(response)


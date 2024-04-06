import llama_index_base_methods as lm


# Scenario 1 : Your very first llm app using llama index
# packages to install : 
    # pip install llama_index
    # pip install -U llama-index-readers-file

print("Scenario 1 :") 
lm.basic_llamaindex()

# Scenario 2 : You can't digest whole document in one go, parse it into smaller doc
print("Scenario 2 :") 
lm.parse_doc_smaller_chunks()

# Scenario 3 : You want to persist the index and then use it repeatedly without loading index again and again
print("Scenario 3 :") 
lm.store_doc_index_on_local()

# Scenario 4 : You want to use different vector stores like Chroma, MongoDB Atlas etc.. 
# packages to install :
    # pip install chromadb
    # pip install llama-index-vector-stores-chroma

print("Scenario 4 :") 
lm.use_different_vector_store()

# Scenario 5 : You want to retrieve more context while performing queries
print("Scenario 5 :") 
lm.retrieve_more_doc_context()

# Scenario 6 : You don't want to use default gpt-3.5-turbo model 
print("Scenario 6 :") 
lm.change_default_llm_model()

# Scenario 7 : You want to get the streaming response just like ChatGPT
print("Scenario 7 :") 
lm.get_response_in_stream()

# Scenario 8 : You want to use different response mode and not the default one
print("Scenario 8 :") 
lm.get_different_response_mode()

# Scenario 9 : You want a chatbot functionality 
print("Scenario 9 :") 
lm.get_chatbot_for_doc()

# Scenario 10 : You don't want to use default llm model, want to use a different one altogether
# package to install : 
    # pip install llama-index-llms-ollama
    # pip install llama-index-embeddings-huggingface
# run the model before running the python script 
    # ollama run mistral

print("Scenario 10 :") 
lm.use_another_llm_model()
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI
from llama_index.llms.ollama import Ollama
from llama_index.core.embeddings import resolve_embed_model
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore

#scenario 1 : the most basic llmaindex code
def basic_llamaindex():
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()

    response = query_engine.query("What did author do growing up?")

    print(response)

#scenario 2: cant't digest whole documents in one go, parse it into smaller chunks
def parse_doc_smaller_chunks():

    Settings.chunk_size = 512 
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(
        documents, transformations= [
            SentenceSplitter (
                                chunk_size=512, 
                                chunk_overlap=20
                            )
            ])
    query_engine = index.as_query_engine()

    response = query_engine.query("What did author do growing up?")

    print(response)


#scenario 3: don't want to use in-memory index, want to store it on my local and use it for query
def store_doc_index_on_local():
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist()

    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query("What did the author do growing up?")
    print(response)


#scenario 4: I want to use different vector store and not the default one
def use_different_vector_store():
    # create client
    chroma_client = chromadb.PersistentClient()
    # create collection
    chroma_collection = chroma_client.create_collection("quickstart")
    # create vector store
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(
            documents, 
            storage_context=storage_context
    )
    query_engine = index.as_query_engine()
    response = query_engine.query("What did the author do growing up?")
    print(response)
 
#scenario 5: I want to retrieve more context when I query 
def retrieve_more_doc_context():
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine(similarity_top_k=5)

    response = query_engine.query("What did author do growing up?")

    print(response) 
    
#scenario 6 : default model is gpt-3.5-turbo, I want to use different model 
def change_default_llm_model():
    documents = SimpleDirectoryReader("data").load_data()
    llm = OpenAI(temperature=0.1, model="gpt-4")
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine(llm=llm)

    response = query_engine.query("What did author do growing up?")

    print(response) 


#scenario 7 : I want to stream the response back 
def get_response_in_stream():
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine(streaming=True)
    response = query_engine.query("What did the author do growing up?")
    response.print_response_stream()


#scenaio 8: I want to use different response mode 
def get_different_response_mode():
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine(response_mode="tree_summarize")
    response = query_engine.query("What did the author do growing up?")

    print(response)


#scenaio 9 : I want a chatbot insted of Q&A
def get_chatbot_for_doc():
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_chat_engine()
    response = query_engine.chat("What did the author do growing up?")
    print(response)

    response = query_engine.chat("Oh interesting, tell me more.")
    print(response)

    
#scenaio 10: not OpenAI, I want to use different LLM 
def use_another_llm_model():
    Settings.llm = Ollama(model="mistral", request_timeout = 3000.0) 

     # bge embedding model
    Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")
    
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()

    response = query_engine.query("What did author do growing up?")

    print(response) 
    




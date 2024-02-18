import pymongo
import openai
import os
from llama_index import VectorStoreIndex, StorageContext, SimpleDirectoryReader
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from llama_index.storage.storage_context import StorageContext
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# get openai key and mongo connection url
openai.api_key = os.getenv("OPENAI_API_KEY")
mongo_uri = os.getenv("MONGO_URI")


# setup client
mongodb_client = pymongo.MongoClient(mongo_uri)

if mongodb_client :
    print("Connection is successful!")
else:
    print("Connection is not successful!")

# setup store
store = MongoDBAtlasVectorSearch(mongodb_client)
# print(store)

storage_context = StorageContext.from_defaults(
    vector_store=store
)

documents = SimpleDirectoryReader("input/text").load_data()
index = VectorStoreIndex.from_documents(documents, storage_context= storage_context)
#print(index)

# ask query 
query_engine = index.as_query_engine()
response = query_engine.query("What do you feel the author's did right in his career ?")
print(response)

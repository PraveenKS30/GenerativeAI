#pip install llama-index-llms-groq
from llama_index.llms.groq import Groq
#pip install python-dotenv
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core import PromptTemplate, Settings
from llama_index.core.embeddings import resolve_embed_model
import os

load_dotenv()

api_key = os.getenv('GROQ_API_KEY')

def groq_ingest_load(query):

    # only load PDFs files
    required_exts = [".pdf"]

    # load documents 
    loader = SimpleDirectoryReader(
                            "data", 
                            required_exts= required_exts
                        )

    documents = loader.load_data()

    # create embeddings using HuggingFace model
    embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

    # prompt template
    template =  (
        "We have provided context information below. \n"
        "---------------------\n"
        "{context_str}"
        "\n---------------------\n"
        "Given this information, please answer the question: {query_str}\n"
        "If you don't know the answer, please do mention : I don't know !"
    )

    prompt = PromptTemplate(template = template)

    # define llms
    llm = Groq(model="llama3-70b-8192", api_key= api_key)

    # setting up llm and output tokens
    Settings.llm = llm
    Settings.num_output = 250
    Settings.embed_model = embed_model

    # define index
    index = VectorStoreIndex.from_documents(documents)

    # define query engine 
    query_engine = index.as_query_engine()

    # update our custom prompt
    query_engine.update_prompts(prompt)

    # Ask query and get response
    response = query_engine.query(query)

    print(response)


groq_ingest_load("How did shopify scale their database processing?")
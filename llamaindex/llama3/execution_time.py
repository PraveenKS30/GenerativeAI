import time
from ollama_llama3 import ingest_load
from llama3_groq import groq_ingest_load

def get_execution_time():
    # get the start time 
    start_time = time.time()
    ingest_load("How did shopify scale their database processing?")
    end_time = time.time()

    # calculate execution time
    execution_time = end_time - start_time
    print(f"The function llama3 took {execution_time} seconds to execute.")

    # get the start time 
    start_time1 = time.time()
    groq_ingest_load("How did shopify scale their database processing?")
    end_time1 = time.time()

    # calculate execution time
    execution_time1 = end_time1 - start_time1
    print(f"The function groq llama3 took {execution_time1} seconds to execute.")

get_execution_time()


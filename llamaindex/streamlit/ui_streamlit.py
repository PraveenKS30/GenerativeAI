import os, streamlit as st
import openai
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index import LLMPredictor
from langchain.chat_models import ChatOpenAI
import traceback

openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a simple Streamlit app
st.title("Ask LlamaIndex")
query = st.text_input("What would you like to ask?")

# If the 'Submit' button is clicked
if st.button("Submit"):
    if not query.strip():
        st.error(f"Please provide the search query.")
    else:
        try:
                # define custom LLM model
                llm_predictor = LLMPredictor(ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"))

                # Load documents from the 'data' directory
                documents = SimpleDirectoryReader('data').load_data()
                service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

                # build the index
                index = VectorStoreIndex.from_documents(documents, service_context=service_context)

                query_engine= index.as_query_engine()
                response = query_engine.query(query)
                st.success(response)

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.error(traceback.format_exc())




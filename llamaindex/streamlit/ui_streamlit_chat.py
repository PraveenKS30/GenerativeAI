import streamlit as st
import os
import openai
from llama_index import SimpleDirectoryReader, ServiceContext, VectorStoreIndex, LLMPredictor
from langchain.chat_models import ChatOpenAI

st.title("Ask LlamaIndex")

openai.api_key = os.getenv("OPENAI_API_KEY")

def query_response(query):
    # define custom LLM model
    llm_predictor = LLMPredictor(ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", streaming=True))

    # Load documents from the 'data' directory
    documents = SimpleDirectoryReader('data').load_data()
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

    # build the index
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)

    query_engine= index.as_query_engine(streaming=True)
    response = query_engine.query(query)
    #print(response.print_response_stream())
    return response

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # response = f"Echo: {query_response(prompt)}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = query_response(prompt)
        message_placeholder = st.empty()
        full_response = ""
        for chunk in response.response_gen:
            full_response += chunk
            message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)

# Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

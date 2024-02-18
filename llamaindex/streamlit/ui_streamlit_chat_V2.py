import streamlit as st
import os
import openai
from llama_index import SimpleDirectoryReader, ServiceContext, VectorStoreIndex, LLMPredictor
from llama_index.llms import OpenAI

st.title("Ask LlamaIndex")

openai.api_key = os.getenv("OPENAI_API_KEY")

@st.cache_resource(show_spinner=False)
def query_response(prompt):
    # define custom LLM model
    llm = OpenAI()
    #llm_predictor = LLMPredictor(ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"))

    # Load documents from the 'data' directory
    documents = SimpleDirectoryReader('data').load_data()
    service_context = ServiceContext.from_defaults(llm=llm)

    # build the index
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)

    chat_engine= index.as_chat_engine(chat_mode="condense_question", verbose=True)
    response = chat_engine.chat(prompt)
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
        with st.spinner("Thinking!"):
            response = query_response(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message)


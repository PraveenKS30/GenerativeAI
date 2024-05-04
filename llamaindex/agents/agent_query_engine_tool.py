from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata

# define llm 
llm = OpenAI(model= "gpt-4")

# load data
documents = SimpleDirectoryReader("data" , required_exts= [".pdf"]).load_data()

# create index
index = VectorStoreIndex.from_documents(documents)

# query engine
query_engine = index.as_query_engine()

# define QueryEngineTool
query_engine_tools = [
    QueryEngineTool(
        query_engine= query_engine,
        metadata= ToolMetadata(
            name = "data_tool",
            description= "Provides information about the Shopify and OpenAI system's architecture design "
        )
    )
]

agent = ReActAgent.from_tools(query_engine_tools, llm=llm, verbose= True)

response = agent.chat("How did shopify scale their database?")

print(response)
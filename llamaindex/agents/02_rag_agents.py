from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool, QueryEngineTool

# initialize llm 
llm = OpenAI(model = "gpt-4o", temperature=0)

# let's first try with non-agentic approach
# load the pdf file
required_exts = [".pdf"]
documents = SimpleDirectoryReader("data", required_exts= required_exts).load_data()

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("What was the turnout in 2024 indian general elections ?")

print(response)


# let's convert the above to agentic approach 

election_tool = QueryEngineTool.from_defaults(
    query_engine, 
    name = "2024_indian_general_election",
    description= "A RAG engine with details about the 2024 Indian general election"
)

agent = ReActAgent.from_tools([election_tool], verbose=True)

agent_response = agent.chat("How many seats have been won by BJP and Congress in 2024 general elections?")

print(agent_response)

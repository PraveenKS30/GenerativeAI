from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from file_operations_tool import read_file_tool, write_file_tool

# define llm 
llm = OpenAI(model = "gpt-4", temparatue = 0)

# initialize react agents
agent = ReActAgent.from_tools([read_file_tool, write_file_tool], llm=llm, verbose=True)

# chat with agent
result = agent.chat("Could you please crate a python file with GET endpoint using FASTAPI? ")

print(result)
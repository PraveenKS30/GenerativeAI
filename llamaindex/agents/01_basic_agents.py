from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool

# create basic tool on custom functions

# define multiply function
# important : docstring helps LLM to understand what a specific function does
def multiply(a: float, b: float) -> float:
    """multiply two numbers and return a number"""
    return a * b

# define multiply tool 
multiply_tool = FunctionTool.from_defaults(fn=multiply)

# define add function
def add(a: int, b: int) -> int:
    """add two numbers and return a number"""
    return a + b

# define add tool 
add_tool = FunctionTool.from_defaults(fn=add)


# initialize llm 
llm = OpenAI(model = "gpt-3.5-turbo", temprature = 0)

# initialize agent 
agent = ReActAgent.from_tools([multiply_tool, add_tool], verbose= True)

# ask question 
response = agent.chat("What is 20+(2*4)? Use given tool to calculate every step.")

print(response)
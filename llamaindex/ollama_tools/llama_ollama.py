from llama_index.core.tools import FunctionTool
from llama_index.core.agent import ReActAgent
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.llms.groq import Groq
from weather import get_current_weather_C, get_current_weather_F
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("groq_api_key")

# intialize llm 
#Settings.llm = Ollama(model = "llama3.1", request_timeout="300")
Settings.llm = Groq(model="llama-3.1-70b-versatile", api_key= api_key)

# convert method to a tool 
weather_tool_C = FunctionTool.from_defaults(fn = get_current_weather_C)
weather_tool_F = FunctionTool.from_defaults(fn = get_current_weather_F)

# call agent with the given tool 
agent = ReActAgent.from_tools([weather_tool_C, weather_tool_F], verbose=True)

response = agent.query("What's the temparture in Delhi in °F and in °C?")

print(response)



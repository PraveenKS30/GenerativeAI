from openai import OpenAI
from pydantic import BaseModel
import openai
import json
from textwrap import dedent
from util import get_books_by_genre

system_content = '''
    You are a helpful assistant and would utilize given tool 
    to generate book name in the Fantasy, Fiction and Romance genre 
'''
# initialize client
client = OpenAI()

# define pydantic class 
class Book(BaseModel):
    """Provide Book details"""
    title : str
    author: str
    genre : str

# chat completions 
completions = client.beta.chat.completions.parse(
    model= "gpt-4o-mini",
    messages = [
        {
            "role" : "system",
            "content" : dedent(system_content)
        },
        {
            "role" : "user",
            "content" : "Please provide a sample book name, along with author"
        }
    ],
    tools =[
        openai.pydantic_function_tool(Book)
    ]
)

tool_calls = completions.choices[0].message.tool_calls
#print(tool_calls)


for i, tool_call in enumerate(tool_calls):
    args = tool_call.function.arguments
    #print(args)
    genre = json.loads(args).get("genre")
    get_books_by_genre(genre)


from openai import OpenAI
from pydantic import BaseModel
from typing import List
import openai

# initialize client
client = OpenAI()

# pydantic classes 
class Songs(BaseModel):
    name : str


class Album(BaseModel):
    name : str
    songs : List[Songs]

# chat completion
# using tools
completion = client.beta.chat.completions.parse(
     model= "gpt-4o-mini",
     messages=[
         {
             "role" : "user",
             "content" :"please provide random famous album details"
         }
     ], 
     tools =[
         openai.pydantic_function_tool(Album)
     ] 
  
)
# using response_format
completion = client.beta.chat.completions.parse(
     model= "gpt-4o-mini",
     messages=[
         {
             "role" : "user",
             "content" :"please provide random famous album details"
         }
     ], 
     response_format= Album
  
)


# using tools
#print(completion.choices[0].message.tool_calls[0].function.arguments)
#print(completion.choices[0].message.tool_calls[0].function.parsed_arguments)

# using response_format
message = completion.choices[0].message

if message.parsed:
    print(completion.choices[0].message.content)
else :
    print(message.refusal)
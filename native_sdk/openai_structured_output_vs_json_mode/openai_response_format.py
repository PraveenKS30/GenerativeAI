from openai import OpenAI
from pydantic import BaseModel

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
            "role" : "user",
            "content" : "Please provide a sample book name, along with author"
        }
    ],
    response_format= Book
)

print(completions.choices[0].message.content)
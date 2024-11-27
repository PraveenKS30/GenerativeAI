from openai import OpenAI
import json 
from prompts import META_PROMPT, STRUCTURED_OUT_META_SCHEMA, STRUCTURED_OUT_META_PROMPT, FUNCTION_META_SCHEMA, FUNCTION_META_PROMPT
from ollama import chat

# initialize client
client = OpenAI()

# method for auto prompt generation
def generate_prompt(task_or_prompt: str):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": META_PROMPT,
            },
            {
                "role": "user",
                "content": "Task, Goal, or Current Prompt:\n" + task_or_prompt,
            },
        ],
    )
   
    return completion.choices[0].message.content

# method for auto schema generation
def generate_schema(description: str):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_schema", "json_schema": STRUCTURED_OUT_META_SCHEMA},
        messages=[
            {
                "role": "system",
                "content": STRUCTURED_OUT_META_PROMPT,
            },
            {
                "role": "user",
                "content": "Description:\n" + description,
            },
        ],
    )

    return json.loads(completion.choices[0].message.content)

# method for auto function schema generation
def generate_function_schema(description: str):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_schema", "json_schema": FUNCTION_META_SCHEMA},
        messages=[
            {
                "role": "system",
                "content": FUNCTION_META_PROMPT,
            },
            {
                "role": "user",
                "content": "Description:\n" + description,
            },
        ],
    )

    return json.loads(completion.choices[0].message.content)

def ollama_generate_prompt(task_or_prompt: str):
    completion = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": META_PROMPT,
            },
            {
                "role": "user",
                "content": "Task, Goal, or Current Prompt:\n" + task_or_prompt,
            },
        ],
    )
   
    return completion['message']['content']
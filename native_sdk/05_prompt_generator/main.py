from fastapi import FastAPI
from pydantic import BaseModel
import json
from utils import generate_prompt, generate_schema, generate_function_schema, ollama_generate_prompt

# initialize app 
app = FastAPI()
 
class Item(BaseModel): 
    input: str 
    
@app.post("/auto/prompt") 
async def gen_auto_prompt(item: Item): 
    # Generate the prompt 
    output = generate_prompt(item.input) 
    
    print(output)
    return {"response" : output}

@app.post("/auto/prompt/ollama")
async def gen_auto_ollama_prompt(item: Item): 
    # Generate the prompt 
    output = ollama_generate_prompt(item.input) 
    
    print(output)
    return {"response" : output}


@app.post("/auto/prompt/schema")
async def gen_auto_schema(item: Item):
    # Generate schema
    output = generate_schema(item.input)

    return {"response" : output}


@app.post("/auto/promt/func/schema")
async def gen_auto_func_schema(item: Item):
    # Generate function schema
    output =  generate_function_schema(item.input)

    return {"response" : output}

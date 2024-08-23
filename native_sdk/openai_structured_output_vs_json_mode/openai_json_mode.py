from openai import OpenAI


# initialize client
client = OpenAI()

# chat completions 
completions = client.chat.completions.create(
    model= "gpt-4o-mini",
    messages = [
        {
            "role" : "user",
            "content" : "Please provide a sample book name, along with author and genre in the JSON format"
        }
    ],
    response_format= {"type" :"json_object"}

)

print(completions.choices[0].message.content)
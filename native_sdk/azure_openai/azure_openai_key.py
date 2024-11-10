import os 
from openai import AzureOpenAI
from dotenv import load_dotenv

# load environment variables
load_dotenv()

api_key = os.getenv("azure_openai_api_key")
api_version = os.getenv("azure_api_version")
azure_endpoint = os.getenv("azure_endpoint")
azure_deployment = os.getenv("azure_deployment_name")

# create client 
client = AzureOpenAI(
    api_key= api_key, 
    api_version= api_version,
    azure_endpoint= azure_endpoint
)


# generate response 

response = client.chat.completions.create(
    model= azure_deployment, 
    messages= [
        {
            "role" : "user",
            "content" : "Tell me a story in 20 words"
        }
    ]
)

print(response.choices[0].message.content)

import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI
from dotenv import load_dotenv

# load environemnt variables 
load_dotenv()

# get the token 
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
     "https://cognitiveservices.azure.com/.default"
)

print(token_provider)

api_version = os.getenv("azure_api_version")
azure_endpoint = os.getenv("azure_endpoint")
azure_deployment = os.getenv("azure_deployment_name")

# create client 
client = AzureOpenAI(
    azure_ad_token_provider= token_provider,
    api_version= api_version,
    azure_endpoint= azure_endpoint
)

# get response 
response = client.chat.completions.create(
    model = azure_deployment, 
    messages = [
        {
            "role" : "user",
            "content" : "Tell me story in 20 words"
        }
    ]
)

print(response.choices[0].message.content)

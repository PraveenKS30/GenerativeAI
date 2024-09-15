import google.generativeai as genai
from util import get_input_content
from typing_extensions import TypedDict
import os 
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["API_KEY"])

# define response class
class Response(TypedDict):
    text : str
    emotion : str


# initialize model 
model = genai.GenerativeModel("gemini-1.5-flash")

# read the contents of the file
lines = get_input_content()

for line in lines :
    # get the response
    result = model.generate_content(
        ["Detect the emotion in this text", line],
        generation_config= genai.GenerationConfig(
            response_mime_type= "application/json", 
            response_schema= list[Response]
        ),
    )
    print(result.text)
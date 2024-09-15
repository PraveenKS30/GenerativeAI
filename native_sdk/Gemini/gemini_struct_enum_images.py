import google.generativeai as genai
import enum 
from util import get_images
from typing_extensions import TypedDict
import os 
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["API_KEY"])

# define enum as class 
class Emotion(enum.Enum):
    ANGRY = "angry"
    SAD   = "sad"
    HAPPY = "happy"
    WEEPY = "weepy"
    NEUTRAL = "neutral"

class Response(TypedDict):
    image_name : str
    emotion : Emotion


# initialize model 
model = genai.GenerativeModel("gemini-1.5-flash")

# read the contents of the file
images = get_images()
print(images)

for image in images:
    emoji = genai.upload_file(image)
    #print(emoji)
    result = model.generate_content(
        ["Detect the emotion in this image", image],
        generation_config= genai.GenerationConfig(
            response_mime_type= "application/json", 
            response_schema= list[Response]
        ),
    )
    print(result.text)
   
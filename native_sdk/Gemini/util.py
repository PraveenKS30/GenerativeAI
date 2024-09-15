import os
from pathlib import Path

def get_input_content():
    with open("emotions.txt","r" , encoding="utf-8") as f:
        lines = f.readlines()
        return lines

def get_images():
    folder_dir = Path("images")
    image_path = []

    # iterate over all the image files
    for image in os.listdir(folder_dir):
        full_path = folder_dir / image
        image_path.append(str(full_path))

    return image_path
    
    
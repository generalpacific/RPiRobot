import requests
import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

PACIFRAME_DIR = "~/PaciFramePhotos"
API_URL = "https://9xj3ly8j6i.execute-api.us-east-2.amazonaws.com/prod/dailydigest"
response = requests.get(API_URL)

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font_size = 20
font = ImageFont.truetype(font_path, font_size)

image_size = (800, 480)
background_color = (255, 255, 255)
text_color = (0, 0, 0)
padding = 50

def __get_entities(response):
    print("get entities from response")
    digest = response.json()["digest"]
    entities = []
    for entity in digest:
        if "highlight" in entity:
            entities.append(entity["highlight"])
        elif "quote" in entity:
            entities.append(entity["quote"])
    return entities


quotes = __get_entities(response)
PACIFRAME_DIR = os.path.expanduser(PACIFRAME_DIR)
for index, quote in enumerate(quotes):
    print("Creating image for quote no. " + str(index))
    text = quote
    
    # Create a blank image
    img = Image.new('RGB', image_size, color=background_color)
    draw = ImageDraw.Draw(img)
    
    # Wrap text
    wrapped_text = textwrap.fill(text, width=40)
    
    # Calculate text size and position
    text_size = draw.textsize(wrapped_text, font=font)
    text_x = (image_size[0] - text_size[0]) / 2
    text_y = (image_size[1] - text_size[1]) / 2
    
    # Draw the text on the image
    draw.text((text_x, text_y), wrapped_text, fill=text_color, font=font)
    
    # Save the image
    img.save(f"{PACIFRAME_DIR}/quote_{index}.jpeg")

print("Images created successfully.")


#!/usr/bin/env python3

import sys
import os
import time
from PIL import Image
from inky.auto import auto
import random


PACIFRAMEDIR = "~/PaciFramePhotos"
REFRESH_INTERVAL_SEC = 300 

def __get_randomized_filenames(directory):
    """Return all JPG files in the specified directory in random order."""
    expanded_dir = os.path.expanduser(directory)
    print("""Looking for files in {directory}""".format(directory=expanded_dir))
    all_items = os.listdir(os.path.expanduser(directory))
    print("""There are {num} items in {directory}""".format(num=len(all_items), directory=expanded_dir))
    jpg_files = [os.path.join(expanded_dir, file) for file in all_items 
            if os.path.isfile(os.path.join(expanded_dir, file)) 
                and (file.lower().endswith('.jpg') 
                or file.lower().endswith('.jpeg')) and not file.startswith('artoftheday') and not file.startswith('quote')]
    quote_files = [os.path.join(expanded_dir, file) for file in all_items 
            if os.path.isfile(os.path.join(expanded_dir, file)) 
                and (file.lower().endswith('.jpg') 
                or file.lower().endswith('.jpeg')) and file.startswith('quote')]
    random.shuffle(jpg_files)
    random.shuffle(quote_files)
    return (jpg_files, quote_files)


"""
Resizes the image to target_resolution maintaining the aspect ratio of the
original image.
"""
def __resize_and_fill(image, target_resolution):
    original_width, original_height = image.size
    target_width, target_height = target_resolution

    ratio = min(target_width / original_width, target_height / original_height)
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)

    resized_image = image.resize((new_width, new_height), Image.LANCZOS)

    new_image = Image.new('RGB', target_resolution, (0, 0, 0))

    x = (target_width - new_width) // 2
    y = (target_height - new_height) // 2

    new_image.paste(resized_image, (x, y))

    return new_image


def main():
    inky = auto(ask_user=True, verbose=True)
    saturation = 1

    all_files = __get_randomized_filenames(PACIFRAMEDIR)
    jpg_files = all_files[0]
    quote_files = all_files[1]
    print("""There are {num} files""".format(num=len(jpg_files)))


    expanded_dir = os.path.expanduser(PACIFRAMEDIR)
    while True:
        for jpg_file in jpg_files:
            print("Displaying {jpg_file}".format(jpg_file=jpg_file))
            image = Image.open(jpg_file)
            resizedimage = __resize_and_fill(image, inky.resolution) 
            inky.set_image(resizedimage, saturation=saturation)
            inky.show()
            time.sleep(REFRESH_INTERVAL_SEC)
            print("Displaying artofthedays")
            for i in range(3):
                print(f"Displaying artoftheday-{i}.jpeg")
                art_of_the_day = os.path.join(expanded_dir, f"artoftheday-{i}.jpeg")  
                image = Image.open(art_of_the_day)
                resizedimage = __resize_and_fill(image, inky.resolution) 
                inky.set_image(resizedimage, saturation=saturation)
                inky.show()
                time.sleep(REFRESH_INTERVAL_SEC)

            print("Displaying random quote")
            quote_file = random.choice(quote_files)
            print(f"Displaying {quote_file}")
            image = Image.open(quote_file)
            resizedimage = __resize_and_fill(image, inky.resolution) 
            inky.set_image(resizedimage, saturation=saturation)
            inky.show()
            time.sleep(REFRESH_INTERVAL_SEC)


if __name__ == "__main__":
    main()

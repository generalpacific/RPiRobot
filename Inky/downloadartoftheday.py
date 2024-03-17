#!/usr/bin/env python3

import sys
import os
import time
import requests
import base64
import gzip
import io
from datetime import datetime

PACIFRAMEDIR = "~/PaciFramePhotos"
ART_OF_THE_DAY_FILENAME_PREFIX = "artoftheday"

def __download_artoftheday(idx):
    expanded_dir = os.path.expanduser(PACIFRAMEDIR)
    save_path = os.path.join(expanded_dir, f"{ART_OF_THE_DAY_FILENAME_PREFIX}-{idx}.jpeg")

    current_date = datetime.now()
    formatted_date = current_date.strftime('%Y-%m-%d')

    print(f"Getting art of the day for index: {idx}")

    response = requests.get(f"https://6h5c17qwla.execute-api.us-east-2.amazonaws.com/prod/artoftheday?date={formatted_date}&index={idx}")

    response.raise_for_status()

    print(f"Got successful response from artoftheday api: {response}")
    encoded_image_data = response.json()['image']
    compressed_image_bytes = base64.b64decode(encoded_image_data)
    with gzip.open(io.BytesIO(compressed_image_bytes), 'rb') as f:
        decompressed_image_bytes = f.read()
    with open(save_path, 'wb') as image_file:
        image_file.write(decompressed_image_bytes)

    print(f"Image saved to {save_path}")


def main():
    for i in range(2):
        __download_artoftheday(i)



if __name__ == "__main__":
    main()

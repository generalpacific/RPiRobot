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
ART_OF_THE_DAY_FILENAME = "artoftheday.jpeg"

def __download_artoftheday():
    expanded_dir = os.path.expanduser(PACIFRAMEDIR)
    save_path = os.path.join(expanded_dir, ART_OF_THE_DAY_FILENAME)

    current_date = datetime.now()
    formatted_date = current_date.strftime('%Y-%m-%d')

    response = requests.get(f"https://6h5c17qwla.execute-api.us-east-2.amazonaws.com/prod/artoftheday?date={formatted_date}")

    response.raise_for_status()

    print(f"Got sucessful response from artoftheday api: {response}")
    encoded_image_data = response.json()['image']
    compressed_image_bytes = base64.b64decode(encoded_image_data)
    with gzip.open(io.BytesIO(compressed_image_bytes), 'rb') as f:
        decompressed_image_bytes = f.read()
    decompressed_base64_image = base64.b64encode(decompressed_image_bytes)
    with open(save_path, 'wb') as image_file:
        image_file.write(decompressed_base64_image)

    print(f"Image saved to {save_path}")


def main():
    __download_artoftheday()



if __name__ == "__main__":
    main()

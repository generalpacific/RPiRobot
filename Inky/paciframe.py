#!/usr/bin/env python3

import sys
import os
import time
from PIL import Image
from inky.auto import auto


PACIFRAMEDIR = "~/PaciFramePhotos"
REFRESH_INTERVAL_SEC = 10 

def __get_randomized_filenames(directory):
    """Return all JPG files in the specified directory in random order."""
    expanded_dir = os.path.expanduser(directory)
    print("""Looking for files in {directory}""".format(directory=expanded_dir))
    all_items = os.listdir(os.path.expanduser(directory))
    print("""There are {num} items in {directory}""".format(num=len(all_items), directory=expanded_dir))
    jpg_files = [os.path.join(expanded_dir, file) for file in all_items 
            if os.path.isfile(os.path.join(expanded_dir, file)) 
                and (file.lower().endswith('.jpg') 
                or file.lower().endswith('.jpeg'))]
    return jpg_files


def main():
    inky = auto(ask_user=True, verbose=True)
    saturation = 0.5

    jpg_files = __get_randomized_filenames(PACIFRAMEDIR)
    print("""There are {num} files""".format(num=len(jpg_files)))

    for jpg_file in jpg_files:
        print("""
            Displaying {jpg_file}
        """.format(jpg_file=jpg_file))
        image = Image.open(jpg_file)
        resizedimage = image.resize(inky.resolution)
        inky.set_image(resizedimage, saturation=saturation)
        inky.show()
        time.sleep(REFRESH_INTERVAL_SEC)


if __name__ == "__main__":
    main()

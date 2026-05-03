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
    print("Looking for files in {directory}".format(directory=expanded_dir))
    all_items = os.listdir(expanded_dir)
    print("There are {num} items in {directory}".format(
        num=len(all_items), directory=expanded_dir))
    jpg_files = [
        os.path.join(expanded_dir, file) for file in all_items
        if os.path.isfile(os.path.join(expanded_dir, file)) and (
            file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'))
        and not file.startswith('artoftheday') and not file.startswith('quote')
    ]
    quote_files = [
        os.path.join(expanded_dir, file) for file in all_items
        if os.path.isfile(os.path.join(expanded_dir, file)) and (
            file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'))
        and file.startswith('quote')
    ]
    art_files = [
        os.path.join(expanded_dir, file) for file in all_items
        if os.path.isfile(os.path.join(expanded_dir, file)) and (
            file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'))
        and file.startswith('artoftheday')
    ]
    random.shuffle(jpg_files)
    random.shuffle(quote_files)
    random.shuffle(art_files)
    return (jpg_files, quote_files, art_files)


def __resize_and_fill(image, target_resolution):
    """Resizes image to target_resolution maintaining aspect ratio."""
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


def __display_file(inky, path, saturation):
    """Open, resize, and display one image. Returns True on success."""
    try:
        print("Displaying {path}".format(path=path), flush=True)
        image = Image.open(path)
        resized = __resize_and_fill(image, inky.resolution)
        inky.set_image(resized, saturation=saturation)
        inky.show()
        return True
    except Exception as e:
        print("Failed to display {path}: {e}".format(path=path, e=e), flush=True)
        return False


def main():
    inky = auto(ask_user=True, verbose=True)
    saturation = 1

    while True:
        jpg_files, quote_files, art_files = __get_randomized_filenames(PACIFRAMEDIR)
        print("There are {num} photo files, {q} quotes, {a} art".format(
            num=len(jpg_files), q=len(quote_files), a=len(art_files)), flush=True)

        if not jpg_files and not quote_files and not art_files:
            print("No files to display. Sleeping before retry.", flush=True)
            time.sleep(REFRESH_INTERVAL_SEC)
            continue

        for jpg_file in jpg_files:
            __display_file(inky, jpg_file, saturation)
            time.sleep(REFRESH_INTERVAL_SEC)

            if art_files:
                art_file = random.choice(art_files)
                print("Displaying artofthedays", flush=True)
                __display_file(inky, art_file, saturation)
                time.sleep(REFRESH_INTERVAL_SEC)
            else:
                print("No artoftheday files, skipping", flush=True)

            if quote_files:
                quote_file = random.choice(quote_files)
                print("Displaying random quote", flush=True)
                __display_file(inky, quote_file, saturation)
                time.sleep(REFRESH_INTERVAL_SEC)
            else:
                print("No quote files, skipping", flush=True)


if __name__ == "__main__":
    main()

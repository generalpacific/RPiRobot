import os
import shutil
import subprocess
import textwrap
from datetime import date

import requests
from PIL import Image, ImageDraw, ImageFont

# --- Config ---
READWISE_TOKEN = os.environ["READWISE_TOKEN"]
RCLONE_REMOTE = os.environ.get("RCLONE_REMOTE", "gdrive:Inky_Sync")
LOCAL_STAGING = os.environ.get(
    "LOCAL_STAGING", "/home/prashant/readwise-staging"
)

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_SIZE = 20
IMAGE_SIZE = (800, 480)
BG_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

font = ImageFont.truetype(FONT_PATH, FONT_SIZE)


# --- Readwise Daily Review ---
def get_entities():
    """Fetch today's Daily Review from Readwise.
    Returns list of (text, title, author) tuples."""
    r = requests.get(
        "https://readwise.io/api/v2/review/",
        headers={"Authorization": f"Token {READWISE_TOKEN}"},
        timeout=30,
    )
    r.raise_for_status()
    data = r.json()
    return [
        (h["text"], h.get("title") or "", h.get("author") or "")
        for h in data.get("highlights", [])
    ]


# --- Image creation ---
def make_image(text, path):
    img = Image.new("RGB", IMAGE_SIZE, color=BG_COLOR)
    draw = ImageDraw.Draw(img)
    wrapped = textwrap.fill(text, width=40)

    # Pillow 10 removed textsize(); use textbbox instead
    bbox = draw.multiline_textbbox((0, 0), wrapped, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (IMAGE_SIZE[0] - tw) / 2
    y = (IMAGE_SIZE[1] - th) / 2

    draw.multiline_text((x, y), wrapped, fill=TEXT_COLOR, font=font)
    img.save(path, format="JPEG")


# --- rclone helpers ---
def rclone(*args):
    """Run rclone with given args, raising on non-zero exit."""
    cmd = ["rclone", *args]
    print("  $", " ".join(cmd))
    subprocess.run(cmd, check=True)


def delete_old_quotes_from_drive():
    """Delete previous quote_*.jpeg files from the Drive folder.
    Uses --include so we only touch our own quote files, not photos."""
    rclone(
        "delete",
        RCLONE_REMOTE,
        "--include", "quote_*.jpeg",
    )


def upload_staging_to_drive():
    """Copy everything in the local staging folder to Drive."""
    rclone("copy", LOCAL_STAGING, RCLONE_REMOTE)


# --- Main ---
def main():
    quotes = get_entities()
    if not quotes:
        print("No highlights returned from Readwise. Doing nothing.")
        return

    today = date.today().isoformat()

    # Fresh staging dir each run
    if os.path.exists(LOCAL_STAGING):
        shutil.rmtree(LOCAL_STAGING)
    os.makedirs(LOCAL_STAGING)

    # Build all images first. If anything blows up, Drive is untouched.
    for index, (highlight, title, author) in enumerate(quotes):
        print(f"Creating image {index} for: {title}")
        text = f"{highlight} TITLE: {title} AUTHOR: {author}"
        filename = f"quote_{today}_{index}.jpeg"
        make_image(text, os.path.join(LOCAL_STAGING, filename))

    # Now swap: clean up old quotes on Drive, push new ones.
    print("Deleting old quote_*.jpeg from Drive...")
    delete_old_quotes_from_drive()

    print(f"Uploading {len(quotes)} new images to Drive...")
    upload_staging_to_drive()

    print("Done.")


if __name__ == "__main__":
    main()

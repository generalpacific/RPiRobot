#!/bin/bash

export DISPLAY=:0.0

chromium-browser --headless --disable-gpu --no-sandbox --screenshot=screenshot.png --window-size=1280,720 http://www.google.com

python test_display_image.py screenshot.png

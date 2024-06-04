#!/usr/bin/python

import sys
import os.path
from PIL import Image, ImageFont, ImageDraw, ImageSequence

DST_WIDTH=270
BASE_FILE="patrice_base.gif"
DEFAULT_FONT="impact.ttf"
START_FONT_SIZE=50
DST_POS=(31, 430)
TXT_COLOR=(0, 0, 0)
USAGE_MSG=(f"Usage: patric_says.py <text> [OPTIONS]\n"
            f"\t-f, --font FONT_FILE (Default: impact.ttf)\n"
            f"\t-s, --size FONT_SIZE (Default: auto)")

def find_fill_size(font_file: str, base_size: int, text: str):
    size = base_size
    font = ImageFont.truetype(font_file, size)

    while font.getlength(text) >= DST_WIDTH:
        size -= 1
        font = ImageFont.truetype(font_file, size)
    
    while font.getlength(text) < DST_WIDTH:
        font = ImageFont.truetype(font_file, size + 1)
        if font.getlength(text) >= DST_WIDTH:
            return size
        else:
            size += 1

def gen(text: str, font_file:str, font_size: int):
    im = Image.open(BASE_FILE)
    font = ImageFont.truetype(font_file, font_size - 1)
    frames = [f.convert('RGB') for f in ImageSequence.Iterator(im)]

    for image in frames[8:]:
        d = ImageDraw.Draw(image)
        d.text(
               DST_POS,
               text,
               fill=TXT_COLOR,
               font=font,
               stroke_width=1,
               stroke_fill=(
                    255 - TXT_COLOR[0],
                    255 - TXT_COLOR[1],
                    255 - TXT_COLOR[2]
               )
        )
        del d

    file_name = text.replace(' ', '_').lower()
    frames[0].save(f"{file_name}.gif", save_all=True, append_images=frames[1:])

if __name__ == '__main__':
    _, *argv = sys.argv

    if len(argv) == 0:
        print(USAGE_MSG)
        print("ERROR: No text provided")
        exit(1)

    text = argv[0]
    _, *argv = argv
    
    font_file = DEFAULT_FONT
    font_size = None

    i = 0
    while i < len(argv):
        arg = argv[i]

        if arg == "-f" or arg == "--font":
            if i >= len(argv) - 1:
                print(USAGE_MSG)
                print("ERROR: font file specified but not given")
                exit(1)
            font_file = argv[i + 1]
            i += 2

        elif arg == "-s" or arg == "--size":
            if i >= len(argv) - 1:
                print(USAGE_MSG)
                print("ERROR: font_size specified but not given")
                exit(1)
            font_size = argv[i + 1]

            try:
                font_size = int(font_size, 10)
            except ValueError:
                print(f"ERROR: `{font_size}` isn't a valid int representation")
                exit(1)
            i += 2

        else:
            print(USAGE_MSG)
            print(f"ERROR: unknown option `{arg}`")
            exit(1)

    if not os.path.isfile(font_file):
        print(f"ERROR: cannot open file `{font_file}`")
        exit(1)

    if font_size is None or font_size <= 0:
        font_size = find_fill_size(font_file, START_FONT_SIZE, text)

    gen(text, font_file, font_size)

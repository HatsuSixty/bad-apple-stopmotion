#!/bin/env python3

from pathlib import Path
import random
from PIL import Image, ImageEnhance

def lower_brightness(fpath):
    print(f"Lowering brightness of `{fpath}`")
    img = Image.open(fpath)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(0.6)
    img.save(fpath)

def rotate(fpath):
    print(f"Rotating `{fpath}`")
    img = Image.open(fpath).convert("RGBA")
    img = img.rotate(2 if random.randrange(0, 1) == 0 else -2)

    img2 = Image.open("paper.png").convert("RGBA")
    img2.paste(img, (0, 0), img)
    img2.save(fpath)

pathlist = Path(".").glob("./output/*.png")
for path in pathlist:
    path_in_str = str(path)
    try:
        if random.randrange(0, 3) == 1:
            lower_brightness(path_in_str)
        elif random.randrange(0, 3) == 2:
            rotate(path_in_str)
    except:
        pass

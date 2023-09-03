#!/bin/env python3

from PIL import Image
from pathlib import Path
import shutil
import os

pathlist = Path(".").glob("./output/*.png")
for path in pathlist:
    path_in_str = str(path)
    try:
        im = Image.open(path_in_str)
        im.verify()
    except:
        print(f"Image corrupted! Replacing it... ({path_in_str})")
        os.remove(path_in_str)
        shutil.copy(path_in_str.replace("output", "output2"), path_in_str)

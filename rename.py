#!/bin/env python3

from pathlib import Path
from shutil import move

pathlist = Path(".").glob("./output/*.png")
for path in pathlist:
    path_in_str = str(path)
    num = int(path_in_str.replace("output/frame_", "").replace(".png", ""))
    move(path_in_str, "./output/frame_%04d.png" % num)

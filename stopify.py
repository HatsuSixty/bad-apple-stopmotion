#!/bin/env python3

from PIL import Image
import numpy
from math import floor
import sys

if len(sys.argv) < 2:
    print("ERROR: Input frame not specified")
    exit(1)

if len(sys.argv) < 3:
    print("ERROR: Output frame not specified")
    exit(1)

STRETCHNESS = 55
SCALE_FACTOR = 2.8

# https://stackoverflow.com/questions/14177744/how-does-perspective-transformation-work-in-pil
def find_coeffs(pa, pb):
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

    A = numpy.matrix(matrix, dtype=float)
    B = numpy.array(pb).reshape(8)

    res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
    return numpy.array(res).reshape(8)

def is_white(color: (int, int, int)) -> bool:
    return color[0] >= 150 and color[1] >= 150 and color[2] >= 150

print("Starting...")

# prepare frame image
frame = Image.open(sys.argv[1])
frame = frame.convert("RGBA")
frame_pixdata = frame.load()
frame_width, frame_height = frame.size

for y in range(frame_height):
    for x in range(frame_width):
        if is_white(frame_pixdata[x, y]):
            frame_pixdata[x, y] = (255, 255, 255, 0)

coeffs = find_coeffs(
    [(STRETCHNESS, 0), (frame_width - STRETCHNESS, 0), (frame_width, frame_height - 5), (0, frame_height)],
    [(0, 0), (frame_width, 0), (frame_width, frame_height), (0, frame_height)])

frame = frame.transform((frame_width, frame_height),
                        Image.PERSPECTIVE, coeffs, Image.BICUBIC)
frame = frame.resize((floor(frame_width*SCALE_FACTOR), floor(frame_height*SCALE_FACTOR)))

# prepare overlay image
overlay = Image.open("overlay.png")

# prepare light effects image
light = Image.open("light.png")

# make final image with the paper
paper = Image.open("paper.png")
paper.paste(frame, (349, 254), frame)
paper.paste(overlay, (0, 0), overlay)
paper.paste(light, (0, 0), light)

paper.save(sys.argv[2])

print("Done!")

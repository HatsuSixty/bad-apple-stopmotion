#!/bin/bash

value=0
for x in ./frames/*.png; do
    ./stopify.py $x ./output/frame_$value.png
    value=$(($value + 1))
done

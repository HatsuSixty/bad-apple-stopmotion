# Bad Apple Stop Motion

A bunch of python scripts made with the goal of turning [Bad Apple!!](https://www.youtube.com/watch?v=FtutLA63Cp8) into a stop motion style animation.

## How the fuck do I use that shit?

**Before we get into the tutorial, please keep in mind that you will need to have the `pillow` and `numpy` python libraries installed!**

### Step 1

You first need the Bad Apple!! video. Just download it using any YouTube downloader website.
Then, use ffmpeg to reduce the FPS of the video with the following command:
```console
$ ffmpeg -i <input> -filter:v fps=fps=7 badapple7.mp4
```
I recommend using 7 FPS.

### Step 2

Now, you will need to create a `frames` folder, and use ffmpeg to split the video into multiple PNGs using the `frames` folder as the output folder. You can do that by running the following commands:
```command
$ mkdir frames
$ ffmpeg -i badapple7.mp4 ./frames/frame_%04d.png
```

### Step 3

In the next step, you will need to create an `./output` folder, and run `./apply.sh`. This script will run `stopify.py` on each `.png` inside the `./frames` folder, outputing the generated frames into the `./output` folder. You can do that by running the following commands:
```console
$ mkdir output
$ ./apply.sh
```
This will take some time to render, but once you're done, you can go to the next step.

### Step 4

The next step is to backup the `./output` folder into an `./output2` folder, as it will be important later on.
Once you've done that, you will need to run `./worsify.py`. This script will randomly choose frames in the `./output` folder to either dim them or rotate them. You can do that by running the following commands:
```console
$ cp -r output output2
$ ./worsify.py
```

### Step 5

Now, you will need to check for corrupted frames with the `./check.py` script. This script will check for corrupted frames in the `./output` folder, and replace the damaged files with their equivalent in the `./output2` folder. Once again, you can do that by running the following commands:
```console
$ ./check.py
```

### Step 6

You're almost there! Now, run the `./rename.py` script to put the frames in `./output` in the right order. Do that by running:
```console
$ ./rename.py
```
Finally, use ffmpeg to merge the generated frames into a single video. Do that by running:
```console
$ ffmpeg -framerate 7 -pattern_type glob -i './output/*.png' -c:v libx264 -pix_fmt yuv420p out.mp4
```
Later you can add audio, etc. But I'm not going to detail that here.
**That's it!**

## Licensing

Images are Public Domain. For source code licensing details, check [LICENSE](./LICENSE).

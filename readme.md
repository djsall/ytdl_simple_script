# Basic Youtube-dl automation script
This is a script for automating your youtube-dl downloads. 

Just paste your video links into a text file, execute the script and have your files ready.

## How to install?
The first step is to make ffmpeg available to the script.

### Windows:
- If you are running virtualenvwrapper, then you need to put ffmpeg.exe under the scripts folder inside your virtual env. (Default location is %userprofile%/Envs)

- Otherwise, you can install ffmpeg with choco (choco install ffmpeg)

### Linux:
- sudo apt install ffmpeg

### Mac:
- brew install ffmpeg

### After you installed ffmpeg:

After you installed ffmpeg, you can run 'pip install youtube-dl', than you are done with the setup phase.

Now you can create your videos.txt file, which is supposed to contain the video links you want to download.

After you have your list of links, just run the script and wait for all downloads to finish.

The script will spit out 320 mp3 files.

Small disclaimer: they are converted from YouTube's already lossy conversion, which is also a lossy compression of the original audio the video was exported with, which also was most likely exported with lossy compression. 

Also, even the video editor could have used an already lossy file, so sometimes you can get meh quality from youtube rips, but I've only had a few bad experiences.
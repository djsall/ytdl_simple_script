# author: DjSall
# Youtube-dl automator script
# place ffmpeg exe in the virtualenv/scripts directory
# place youtube links into the videos.txr file, which should be in the same directory as the script.
# run the script
from __future__ import unicode_literals

import concurrent
import subprocess
import multiprocessing.dummy

import youtube_dl

ydl_opts = {
  'format': 'bestaudio/best',
  'postprocessors': [{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '320',
  }],
  'outtmpl': '/downloaded/%(title)s.%(etx)s',
}
with open('videos.txt') as f:
  lines = [line.rstrip() for line in f]


def download(link):
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])


p = multiprocessing.dummy.Pool()
p.map(download, lines)

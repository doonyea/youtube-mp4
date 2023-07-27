from pytube import YouTube
from sys import argv

# argv is a list in Python that contains all command-line arguments
link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

vid_mp4 = yt.streams.get_highest_resolution()

vid_mp4.download('/Users/dunyamiletic/Downloads/Youtube_Downloads')



from pytube import YouTube
import moviepy.editor
import os
import re


os.chdir('\Downloads')
url = input("Daj link\n")
ytd = YouTube(url).streams.first().download('/downloads')
print(ytd)

f_name, f_ext = os.path.splitext(ytd)
os.rename(ytd, f_name)
print(f_name)

new_name = re.sub(r'[" "]', '', f_name)
os.rename(f_name, new_name)
print(new_name)

videopath = moviepy.editor.VideoFileClip(new_name)
audio = videopath.audio
audio_format = (new_name + ".mp3")
audio.write_audiofile(audio_format)
videopath.close()
os.remove(new_name)



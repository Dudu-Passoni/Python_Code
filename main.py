from pytube import YouTube
from pathlib import Path
from os import *
from pywebio.input import *
from pyweb.output import *

def video_download():
    while True:
        video_link = input("Informe o link do video; ")
        if video_link.split("//")[0] == "https:":
            put_text("Fazendo download do video....".title()).style('color: red; font-size: 50px')
            video_url = YouTube(video_link)
            video = video_url.streams.get_highest_resolution()
            path_to_download = (r"c:\")
            video.download(path_to_download)
            put_text("Video baixado com sucesso....".title()).style('color: blue; font-size: 50px')
            startfile(r"c:\")

if __name__ == "__main__":
    video_download()

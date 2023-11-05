#!/usr/bin/python3
 
from pytube import YouTube
import argparse
import pathlib as path
import urllib.request
import os

# Variables to download video
VIDEOS_DIR = "./output/videos"
AUDIOS_DIR = "./output/audios"


"""
This function downloads a video from URL

@param url
    Any url
"""
def download_video(url):
    try:
        print("Downloading video...")
        urllib.request.urlretrieve(url, filename=path.title(url))
    except:
        print("\nFailed")
        
def download_video(_url, _filename):
    try:
        print("Downloading video...")
        urllib.request.urlretrieve(url=_url, filename=_filename)
    except:
        print("`\nError has ocurred...")

def download_video():
    try:
        print("Downloading audio...")
    except:
        print("\nFailed!")

"""
Esta función descarga un video de una url 
@param url
    Dirección url del video para descargar
"""
def download_video_from_youtube(url):
    try:
        yt = YouTube(url)
    except:
        print("\nConnection error.")    
    video =  yt.streams.get_highest_resolution()

    try:
        print("Downloading video from YouTube...")
        video.download(output_path=VIDEOS_DIR)
        print("Done.")
    except:
        print("\nFailed!")
    


"""
Esta función descarga el audio de un video de YouTube

@param url
    Dirección URL del video a descargar
"""
def download_audio_from_youtube(url):
    try:
        yt = YouTube(url)
    except:
        print("\nConnection error.")
        
    audio = yt.streams.filter(only_audio = True).first()
    try:
        print("Downloading audio from YouTube...")
        output = audio.download(output_path=AUDIOS_DIR)
        new_filename = os.path.splitext(output)
        os.rename(output, new_filename[0] + ".mp3")
        print("Done.")
    
    except:
        print("\nFailed!")
        
"""
Function to download video from Youtube and rename
file

@param url
    URL to video

@param filename
    Filename to rename the video
"""   
def download_video_from_youtube(url, _filename):
    try:
        yt = YouTube(url)
        
        print("Downloading video from YouTube...")
        video = yt.streams.get_highest_resolution()
        
        video.download(output_path=VIDEOS_DIR, filename=_filename)
        
    except:
        print("Connection error.")
        
        


# Main execution
if __name__ == "__main__":
    
    ap = argparse.ArgumentParser(description="Video downloader from any URL.")
    ap.version = "0.0.1 "
    ap.add_argument("-u", "--url-video", required=True, help="type any video url", type=str)
    ap.add_argument("-a", "--audio", required=False, help="audio only")
    ap.add_argument("-f", "--filename", help="type a name for your new video/audio", action='store')
    ap.add_argument("--youtube", required=False, help="download a video from youtube")
    
    ap.add_argument("-v", "--version", action='version')
    args = ap.parse_args()
    variables = vars(args)
    print(variables)
    if (args["youtube"] and args["url_video"]):
        download_audio_from_youtube(args["url_video"])
    elif (args["youtube"]): 
        download_video_from_youtube(args["url_video"])
        
    elif (args["url_video"]):
        download_video(args["video"])
    elif (args["url_video"] and args["filename"]):
        download_video(args["url_video"], args["filename"])
    else:
        print("Please enter a valid option...")
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
        urllib.request.urlretrieve(url, filename=path.title(url))
    except:
        print("\n[-] Error has ocurred...")



"""
Esta función descarga un video de una url 
@param url
    Dirección url del video para descargar
"""
def download_video_from_youtube(url):
    try:
        yt = YouTube(url)
    except:
        print("\n[!] Connection error")    
    video =  yt.streams.get_highest_resolution()

    try:
        print("Downloading video from " + url)
        video.download(VIDEOS_DIR)
        filename = video.title
    except:
        print("\nAn error has ocurred!")
    
    print("Done.")
    


"""
Esta función descarga el audio de un video de YouTube

@param url
    Dirección URL del video a descargar
"""
def download_audio_from_youtube(url):
    try:
        yt = YouTube(url)
    except:
        print("\nConnection error...")
        
    audio = yt.streams.filter(only_audio = True).first()
    try:
        print("Downloading audio from " + url)
        output = audio.download(AUDIOS_DIR)
        new_filename = os.path.splitext(output)
        os.rename(output, new_filename[0] + ".mp3")
        print("Done.")
    
    except:
        print("\nFailed...")
        


# Main execution
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", required=True, help="youtube video URL")
    ap.add_argument("-a", "--audio", required=False, help="audio only", action=argparse.BooleanOptionalAction)
    ap.add_argument("-f", "--filename", required=False, help="type a name for your new video/audio", action=argparse.BooleanOptionalAction)
    ap.add_argument("--youtube", required=False, help="download a video from youtube", action=argparse.BooleanOptionalAction)
    
    args = vars(ap.parse_args())
    if (args["youtube"] and args["video"]):
        download_audio_from_youtube(args["video"])
    elif (args["youtube"]): 
        download_video_from_youtube(args["video"])
    else:
        print("Please enter a valid option...")
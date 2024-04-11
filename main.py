from pytube import *

runState = True
path = str(input("Enter the path you want to save on: "))
path = path + "/"

def Video():
    link = str(input("Enter the url of the vedio: "))
    video = YouTube(link)
    print("Downloading: " + video.title)
    file = path + video.title

    for i in video.streams.filter(progressive=True):
        print(i)

    itag = int(input("Enter the itag number of the res you want to download: "))
    stream = video.streams.get_by_itag(itag)

    stream.download(output_path=file)
    print("Done!")

def playList():
    link = str(input("Enter the url of the playlist: "))
    playlist = Playlist(link)
    print("Downloading: " + playlist.title)
    file = path + playlist.title

    count = 0

    for video in playlist.videos:
        video.streams.first().download(output_path=file)
        count = count + 1
        print(count)
    
    print("Done!")


while runState == True:
    print("Single video = 1 \nPlaylist = 2\nExit = 0")
    userInput = int(input("What are you going to download using this tool: "))

    if userInput == 1:
        Video()
    elif userInput == 2:
        playList()
    elif userInput == 0:
        runState = False
    else:
        print("Enter a valid input")

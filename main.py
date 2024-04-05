from pytube import *


link = str(input("Enter the url of the vedio: "))
yt = YouTube(link)

print("The title of the viedo is: "+ yt.title + "\n")

for i in yt.streams.filter(progressive=True):
    print(i)

itag = int(input("Enter the itag number of the res you want to download: "))
stream = yt.streams.get_by_itag(itag)

stream.download(output_path="C:/Users/Eric/Downloads/YT")
print("Finished downloading")
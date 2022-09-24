from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

#printing title & views 
print("Title: ", yt.title)
print("View: ", yt.views)

#printing title & views 
print("Length(in sec): ", yt.length)
print("Author: ", yt.author)

#printing description & ratings 
print("Description: ", yt.description)
print("Ratings: ", yt.rating)

#printing  publish date of the video 
print("Publish Date: ", yt.publish_date)


#Fetching the youtube video thumbnail Url
tnail=yt.thumbnail_url
print(tnail)

# for getting only audio list
audio = yt.streams.filter(only_audio=True)
print(audio)#get all reslotions of audio
audio[0].download()#Downloading audio by providing index number

# for getting only video list
video = yt.streams.filter(only_video=True)
print(video)#get all reslotions of video
video[0].download()#Downloading video by providing index number

# for getting whole video with audio with high resolution
yd = yt.streams.get_highest_resolution()
# adding path to download
yd.download(r"C:\Users\lenovo\OneDrive\Desktop")
#Just put r before your normal string it converts normal string to raw string

yd.download(output_path=r"C:\Users\lenovo\OneDrive\Desktop", filename="somg.mp4")#with custom name

#Command to run the file in terminal: python -u "c:\Users\lenovo\OneDrive\Desktop\ytDownload.py" "https://www.youtube.com/watch?v=S9-k5ARrhbo"
#python -u "<file path>" "<video link>"

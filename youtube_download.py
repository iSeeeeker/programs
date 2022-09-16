from tkinter import *
from pytube import YouTube
import os
root = Tk()
root.geometry('600x500')
root.resizable(0,0)
root.title("Youtube Video Downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
#enter link
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 50,textvariable = link).place(x = 32, y = 90)
#function to download video or audio
def Downloadermp4():
    url =YouTube(str(link.get()))
    video = url.streams.filter(progressive=True, file_extension = "mp4").get_highest_resolution()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 230)  
def Downloadermp3():
    url =YouTube(str(link.get()))
    video = url.streams.filter(only_audio=True).first()
    destination = '.'
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + ' .mp3'
    os.rename(out_file, new_file)
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 230)  
Button(root,text = 'DOWNLOAD IN MP3 FORMAT', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloadermp3).place(x=120 ,y = 150)
Button(root,text = 'DOWNLOAD IN MP4 FORMAT', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloadermp4).place(x=120 ,y = 200)
root.mainloop()

#Can download both mp3 and mp4 format. Just past the link and click "mp3" or "mp4"

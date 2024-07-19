import os
import time
from pytubefix import Playlist, YouTube
import tkinter as tk
from tkinter import ttk
def Download_Folder():
    global Default_Path
    Default_Path = os.getcwd()
    #os.chdir('Downloads')
    folder = 'Pytube Downloads'
    if os.path.exists(folder):
        os.chdir('Pytube Downloads')
    elif not os.path.exists(folder):
        os.makedirs(folder)
        os.chdir('Pytube Downloads')
def Download():
    url = Link_Var.get()
    Resolution = Combobox_Var.get()
    Download_Folder()
    if 'playlist' in url:
        Download_Playlist(url,Resolution)
    elif 'youtu.be' in url:
        Download_Video(url,Resolution)
    else:
        Exception_Label = tk.Label(app, text="Invalid Url",bg="#301934",fg="#ffffff",font=("Times New Roman", 12))
        Exception_Label.grid(row=4, column=0, columnspan=2, pady=10)
        app.update()
        time.sleep(5)
        Reset_Exception_Label(Exception_Label)   
def Download_Playlist(url,Resolution):
    Valid_Playlist_Link_Label = tk.Label(app, text="Valid Playlist Link",bg="#301934",fg="#ffffff",font=("Times New Roman", 12))
    Valid_Playlist_Link_Label.grid(row=4, column=0, columnspan=2, pady=10)
    app.update()
    time.sleep(1)
    Playlist_Link = Playlist(url)
    Path = Resolution + " " + Playlist_Link.title 
    if not os.path.exists(Path):
        os.makedirs(Path)
    Number_of_Videos = len(Playlist_Link.video_urls)
    Playlist_Name_Label = tk.Label(app, text=f"Playlist Name - {Playlist_Link.title}",bg="#ffffff",fg="#000000",font=("Times New Roman", 12))
    Playlist_Name_Label.grid(row=5, column=0, columnspan=2, pady=10)
    app.update()
    time.sleep(1)
    Number_of_Videos_Label = tk.Label(app, text=f"Total Number of Videos - {Number_of_Videos}",bg="#ffffff",fg="#000000",font=("Times New Roman", 12))
    Number_of_Videos_Label.grid(row=6, column=0, columnspan=2, pady=10)
    app.update()
    time.sleep(1)
    Initalizing_Download_Label = tk.Label(app, text="Downloading, Kindly Do Not Close The Program",bg="#301934",fg="#ffffff",font=("Times New Roman", 12))
    Initalizing_Download_Label.grid(row=7, column=0, columnspan=2, pady=10)
    app.update()
    time.sleep(1)
    Count = 0
    Progress = ttk.Progressbar(app, orient="horizontal", length=400, mode="determinate", maximum=Number_of_Videos, value=Count)
    Progress.grid(row=8, column=0, columnspan=2, pady=10)
    app.update()
    time.sleep(1)
    for Each_Video in Playlist_Link.videos:
        Count += 1
        try:
            if Resolution == "Highest":
                Each_Video.streams.filter(res="1080p",only_video=True).first().download(Path, filename_prefix=str(Count) + " - ")
                Each_Video.streams.filter(only_audio=True).first().download(Path, mp3=True, filename_prefix=str(Count) + " - ")
            elif Resolution == "720p":
                Each_Video.streams.filter(res="720p",only_video=True).first().download(Path, filename_prefix=str(Count) + " - ")
                Each_Video.streams.filter(only_audio=True).first().download(Path, mp3=True, filename_prefix=str(Count) + " - ")
            elif Resolution == "Lowest":
                Each_Video.streams.get_lowest_resolution().download(Path, filename_prefix=str(Count) + " - ")
            elif Resolution == "Audio Only":
                Each_Video.streams.get_audio_only().download(Path, mp3=True, filename_prefix=str(Count) + " - ")
            time.sleep(1)
        except Exception as Error:
            Exception_Label = tk.Label(app, text=f"Exception : {Error}",bg="#301934",fg="#ffffff",font=("Times New Roman", 12))
            Exception_Label.grid(row=9, column=0, columnspan=2, pady=10)
            app.update()
            time.sleep(5)
            Exception_Label.config(text="",bg="#301934")
            continue
        Progress['value'] = Count
        app.update()
    Download_Completed_Label = tk.Label(app, text="Download Completed, Thank You For Using Our Services",bg="#301934",fg="#ffffff",font=("Times New Roman", 12))
    Download_Completed_Label.grid(row=10, column=0, columnspan=2, pady=10)
    app.update()
    time.sleep(5)
    Reset_Download_Playlist(Valid_Playlist_Link_Label,Playlist_Name_Label,Number_of_Videos_Label,Initalizing_Download_Label,Download_Completed_Label,Progress)
def Download_Video(url,Resolution):
    Valid_Video_Link_Label = tk.Label(app, text="Valid Video Link",bg="#301934",fg="#ffffff",font=("Times New Roman", 12))
    Valid_Video_Link_Label.grid(row=4, column=0, columnspan=2, pady=10)
    app.update()
    time.sleep(1)
    Video_Link = YouTube(url)
    Path = 'Pytube Videos'
    if not os.path.exists(Path):
        os.makedirs(Path)
    try:
        if Resolution == "Highest":
            Size_of_only_Video = Video_Link.streams.filter(res="1080p",only_video=True).first().filesize_mb
            Size_of_only_Audio = Video_Link.streams.filter(only_audio=True).first().filesize_mb
            Size_of_Video = int(Size_of_only_Video + Size_of_only_Audio)
        elif Resolution == "720p":
            Size_of_only_Video = Video_Link.streams.filter(res="720p",only_video=True).first().filesize_mb
            Size_of_only_Audio = Video_Link.streams.filter(only_audio=True).first().filesize_mb
            Size_of_Video = int(Size_of_only_Video + Size_of_only_Audio)
        elif Resolution == "Lowest": 
            Size_of_Video = Video_Link.streams.get_lowest_resolution().filesize_mb
        elif Resolution == "Audio Only":
            Size_of_Video = Video_Link.streams.get_audio_only().filesize_mb
        Video_Name_Label = tk.Label(app, text=f"Video Name - {Video_Link.title}",bg="#ffffff",fg="#000000",font=("Times New Roman", 12))
        Video_Name_Label.grid(row=5, column=0, columnspan=2, pady=10)
        app.update()
        time.sleep(1)
        Size_of_Video_Label = tk.Label(app, text=f"Approximate Size of The Video - {Size_of_Video} MB",bg="#ffffff",fg="#000000",font=("Times New Roman", 12))
        Size_of_Video_Label.grid(row=6, column=0, columnspan=2, pady=10)
        app.update()
        time.sleep(1)
        Initalizing_Download_Label = tk.Label(app, text="Downloading, Kindly Do Not Close The Program",bg="#301934",fg="#ffffff",font=("Times New Roman", 12))
        Initalizing_Download_Label.grid(row=7, column=0, columnspan=2, pady=10)
        app.update()
        time.sleep(1)
        if Resolution == "Highest" :
            Video_Link.streams.filter(res="1080p",only_video=True).first().download(Path)
            Video_Link.streams.filter(only_audio=True).first().download(Path,mp3=True)
        elif Resolution == "720p" :
            Video_Link.streams.filter(res="720p",only_video=True).first().download(Path)
            Video_Link.streams.filter(only_audio=True).first().download(Path,mp3=True)
        elif Resolution == "Lowest":
            Video_Link.streams.get_lowest_resolution().download(Path)
        elif Resolution == "Audio Only":
            Video_Link.streams.get_audio_only().download(Path,mp3=True)
        Download_Completed_Label = tk.Label(app, text="Download Completed, Thank You For Using Our Services",bg="#301934",fg="#ffffff",font=("Times New Roman", 12))
        Download_Completed_Label.grid(row=8, column=0, columnspan=2, pady=10)
        app.update()
        time.sleep(5)
        Reset_Download_Video(Valid_Video_Link_Label,Video_Name_Label,Size_of_Video_Label,Initalizing_Download_Label,Download_Completed_Label)      
    except Exception as Error:
        Exception_Label = tk.Label(app, text=f"Exception : {Error}",bg="#301934",fg="#ffffff",font=("Times New Roman", 12))
        Exception_Label.grid(row=8, column=0, columnspan=2, pady=10)
        app.update()
        time.sleep(5)
        Valid_Video_Link_Label.config(text="",bg="#301934")
        Reset_Exception_Label(Exception_Label)               
def Reset_Download_Playlist(Valid_Playlist_Link_Label,Playlist_Name_Label,Number_of_Videos_Label,Initalizing_Download_Label,Download_Completed_Label,Progress):
    Link_Entry.delete(0,'end')
    Link_Var.set("")
    Combobox_Var.set("")
    Res_Type.current(0)
    Valid_Playlist_Link_Label.config(text="",bg="#301934")
    Playlist_Name_Label.config(text="",bg="#301934")
    Number_of_Videos_Label.config(text="",bg="#301934")
    Initalizing_Download_Label.config(text="",bg="#301934")
    Progress.destroy()
    Download_Completed_Label.config(text="",bg="#301934")
    #Exception_Label.config(text="",bg="#301934")
    os.chdir(Default_Path)
    app.update()
def Reset_Download_Video(Valid_Video_Link_Label,Video_Name_Label,Size_of_Video_Label,Initalizing_Download_Label,Download_Completed_Label):
    Link_Entry.delete(0,'end')
    Link_Var.set("")
    Combobox_Var.set("")
    Res_Type.current(0)
    Valid_Video_Link_Label.config(text="",bg="#301934")
    Video_Name_Label.config(text="",bg="#301934")
    Size_of_Video_Label.config(text="",bg="#301934")
    Initalizing_Download_Label.config(text="",bg="#301934")
    Download_Completed_Label.config(text="",bg="#301934")
    os.chdir(Default_Path)
    app.update()
def Reset_Exception_Label(Exception_Label):
    Link_Entry.delete(0,'end')
    Link_Var.set("")
    Combobox_Var.set("")
    Res_Type.current(0)
    Exception_Label.config(text="",bg="#301934")
    os.chdir(Default_Path)
    app.update()
if __name__ == "__main__":
    app = tk.Tk()
    app.title("Youtube Downloader Manager")
    app.geometry("720x720")
    app.minsize(width=720,height=720)
    app.maxsize(width=720,height=720)
    app.config(background="#301934") 
    Link_Var = tk.StringVar()
    Combobox_Var = tk.StringVar()
    Link_Label = tk.Label(app, text="Enter a Playlist or Video Link ",bg="#301934",fg="#ffffff",font=("Times New Roman", 12))
    Link_Label.grid(row=0, column=0, padx=10, pady=10) 
    Link_Entry = tk.Entry(app, textvariable=Link_Var, width=60,bg="#ffffff",fg="#000000",font=("Times New Roman", 12))
    Link_Entry.grid(row=0, column=1, pady=10)
    Res_Label = tk.Label(app, text="Select The Resolution Type ",bg="#301934",fg="#ffffff",font=("Times New Roman", 12))
    Res_Label.grid(row=1, column=0, padx=10, pady=10) 
    Res_Type = ttk.Combobox(app,textvariable=Combobox_Var,state='readonly',font=("Times New Roman", 12),values=["Highest","720p","Lowest","Audio Only"])
    Res_Type.current(0)
    Res_Type.grid(row=1, column=1, pady=10)
    Download_Button = tk.Button(app, text='Download', command=Download,bg="#ffffff",fg="#000000",font=("Times New Roman", 16))
    Download_Button.grid(row=2, column=0, columnspan=2, pady=10)
    app.update()
    time.sleep(1)
    app.mainloop()
from pytube import YouTube, Playlist

if (input("Youtube Audio HD\nA> Single Video \nB> Playlist Download ")) == "A":
    yt = YouTube(input("Enter Video URL = "))
    dw = yt.streams.get_by_itag(140)
    dw.download("D:/")
    print("TaskCompleted")
elif "B":
    Playlist(input("Enter Playlist URL = ")).download_all("D:/")
else:
    print("Error")

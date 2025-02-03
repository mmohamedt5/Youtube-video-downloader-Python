from pytube import YouTube

import os

def playlist_download():
    try:
        playlist = Playlist(str(input("Enter link: ")))
        print('Number of videos in playlist: %s' % len(playlist.video_urls))

        # Loop through all videos in the playlist and download them
        for video in playlist.videos:
            stream = video.streams.filter(only_audio=True).first()
            print(stream.title)
            print("trying to convert video...")
            destination = "Enter your destination file" ## Enter your destination File
            out_file = stream.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        print("downloads finished")
    except:
        print("Could not complete download")
    

def convert_mp3():
    link = str(input("Enter link\n"))
    try:
        print("getting video...")
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()
        audio = yt.streams.filter(only_audio = True).first()
        print("trying to convert video...")
        destination = "Enter your destination file" ## Enter your destination File
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print("download finsished")
    except:
        print("Could Not Download")

def convert_mp4():
    link = str(input("Enter link\n"))
    try:
        print("getting video...")
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()
        audio = yt.streams.filter(only_audio = True).first()
        print("trying to convert video...")
        destination = "Enter your destination file" ## Enter your destination File
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print("download finsished")
    except:
        print("Could Not Download")

if __name__ == "__main__":

    answer = str(input("Mp3 or Mp4 or playlist (1 or 2 or 3)\n"))
    if (answer == '1'):
        convert_mp3()
    if (int(answer) == 2):
        convert_mp4()
    if (int(answer) == 3):
        playlist_download()
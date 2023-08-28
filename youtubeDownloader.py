from pytube import YouTube, Playlist
from pytube.cli import on_progress

def playlist_download():
    p= Playlist(input("[+] Enter your playlist Link: "))
    print(gap)
    print("")

    print(f'[+] Downloading Playlist : {p.title}')
    print(gap)
    i=1
    for video in p.videos:
        print(f'[{i}]Downloading :{video.title}')
        yt=YouTube(url=video.watch_url,on_progress_callback=on_progress)

        #to change the video resoluation change "720p" to "1080p" or another resolution format.
        yt.streams.get_by_resolution('720p').download() 
        print('')
        print(f'\t\t\t[+][+][+]  Downloaded: {video.title}  [+][+][+]\n')
        i=i+1

    print("\n\n\n[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+]")
    print("###### Successfully downloaded the playlist ######\n\n\n")


def video_download():
    video_link= input("[+] Enter your video Link: ")
    yt=YouTube(url=video_link,on_progress_callback=on_progress)
    print(gap)
    print(f'[+]Downloading : {yt.title}')

    #to change the video resoluation change "720p" to "1080p" or another resolution format.
    yt.streams.get_by_resolution('720p').download()
    print('')
    print(f'\t\t\t[+][+][+]  Successfully Downloaded the video  [+][+][+]\n\n')
    print(gap)



while(True): 
    print("Select option: ")
    print("1. Single video download")
    print("2. Full Playlist download")
    print("[-] Enter anything except 1 & 2 to Exit")
    gap = "#############################################################################"
    select = int(input("Enter your option:\t"))

    if(select==2):
        playlist_download()
    elif(select==1):
        video_download()
    else:
        break



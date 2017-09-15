import pafy
import requests
from bs4 import BeautifulSoup
import subprocess
import glob

playlisturl =  input('Copy and Paste the playlist Link: ')
def download(url):
    video = pafy.new(url)
    audio = video.getbestaudio(preftype="m4a",ftypestrict=True)
    audio.download()
def get_playlist_urls(playlisturl):
    r = requests.get(playlisturl)
    data = r.text
    soup = BeautifulSoup(data,"html5lib")
    a_links=[]
    v_links=[]
    for link in soup.find_all('a'):
        a_links.append(link.get('href'))
    for link in a_links:
        if link[0:5] == "/watc":
            link,garbage=link.split('&', 1)
            garbage,link = link.split('=', 1)
            v_links.append(link)
            print(link)
    return(v_links)


if __name__ == '__main__':
    urls = get_playlist_urls(playlisturl)
    for url in urls:
        url="www.youtube.com/watch?v="+url
        download(url)
        print(url + " DOWNLOADED")
    list_of_m4a_songs = glob.glob('*.m4a')
    for song in list_of_m4a_songs:
        print(song)
        song=song.replace(" ", "\ ")
        song=song.replace("&", "\&")
        song=song.replace("(", "\(")
        song=song.replace(")", "\)")
        song=song.replace("-", "\-")
        command = "ffmpeg -i "+ song +' '+ song[:-3]+"mp3"
        subprocess.call(command, shell=True)
        command = "rm -f "+ song 
        subprocess.call(command, shell=True)

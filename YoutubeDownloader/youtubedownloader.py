import pafy
import requests
from bs4 import BeautifulSoup

playlisturl =  input('Copy and Paste the playlist Link: ')
def download(url):
    video = pafy.new(url)
    audio = video.getbestaudio(preftype="m4a",ftypestrict=True)
    audio.download()
def get_playlist_urls(playlisturl):
    r = requests.get(playlisturl)
    data = r.text
    soup = BeautifulSoup(data)
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
urls = get_playlist_urls(playlisturl)
for url in urls:
    url="www.youtube.com/watch?v="+url
    download(url)
    print(url + " DOWNLOADED")
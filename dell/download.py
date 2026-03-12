import re, sys, os, time, subprocess
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
#print("test")
#runfile('/Users/yuchangnan/Desktop/acodona/dell/download.py', args='https://www.youtube.com/watch?v=wbGPmMDHUag', wdir='/Users/yuchangnan/Desktop/acodona/dell')
main_links = [
"https://www.youtube.com/",
"https://soundcloud.com/",
"https://www.nicovideo.jp/"
]

ero_links = [
"https://www.xvideos.com/"
]

# youtube soundcloud nicovideo
if any(s in sys.argv[1] for s in (main_links)):
    print("test")
    ans = input("type mp3 or mp4: ")
    if "https://www.youtube.com/" in sys.argv[1] and "list=" in sys.argv[1]:
        print("test1")
        th_list = sys.argv[1].split("list=")[1]
    else:
        print("test2")
        th_list = sys.argv[1]
    if ans=="mp3":
        print("test3")
        cmd = 'youtube-dl -o ./%(playlist)s/%(title)s.%(ext)s -ci --extract-audio --audio-format mp3 --add-metadata ' + th_list
    if ans=="mp4":
        print("test4")
        cmd = 'youtube-dl -o ./%(playlist)s/%(title)s.%(ext)s -i -f mp4 --add-metadata ' + th_list
    subprocess.check_call(cmd.split())
    sys.exit()
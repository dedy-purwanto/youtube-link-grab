#!/usr/bin/env python2.7

import requests
import sys
from bs4 import BeautifulSoup

def grab(keyword, author, page=1):
    url = ("http://www.youtube.com/user/%s/videos?sort=da&view=0&page=%s" 
            % (author, page))
    sys.stdout.write("#Processing %s\r\n" % url)
    soup = BeautifulSoup(requests.get(url).content)
    videos_container = soup.find("ol", {"class": "channel-videos-list"})
    videos = videos_container.find_all("li", {"class": "yt-c3-grid-item"})

    if len(videos) > 0:
        for video in videos:
            detail = (video.find("h3", {"class":"yt-c3-grid-item-title"})
                        .find("a"))
            if detail.contents.__str__().find(keyword) >= 0:
                title = detail.contents[0].strip()
                url = detail['href']
                sys.stdout.write("%s#%s\r\n" % (url, title))

    if len(videos_container.contents.__str__()) > 10:
        grab(keyword, author, page+1)

grab("Opera Van Java", "gerandong24")

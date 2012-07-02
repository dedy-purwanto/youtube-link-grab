#!/usr/bin/env python2.7

import requests
import json
import sys

def grab(keyword, limit, author, start=1):
    max_limit = limit if limit <= 50 else 50
    
    url = (
            "http://gdata.youtube.com/feeds/base/videos?max-results=%s&alt=json&q=%s&author=%s&orderby=published&start-index=%s" %
            (max_limit, keyword, author, start)
    )

    output = json.loads(requests.get(url).content)['feed']
    for entry in output['entry']:
        title = entry['title']['$t']
        link = entry['link'][0]['href']
        date = entry['published']['$t']

        sys.stdout.write("%s#%s#%s\r\n" % (link, date, title))

    if limit - 50 > start:
        grab(keyword, limit, author, start+50)


grab("ovj", 100, "gerandong24")

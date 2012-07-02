#!/usr/bin/env python2.7

import requests
import json
import sys

def grab(keyword, limit, author):
    url = (
            "http://gdata.youtube.com/feeds/base/videos?max-results=%s&alt=json&q=%s&author=%s&orderby=published" %
            (limit, keyword, author)
    )

    output = json.loads(requests.get(url).content)['feed']
    for entry in output['entry']:
        title = entry['title']['$t']
        link = entry['link'][0]['href']
        date = entry['published']['$t']

        sys.stdout.write("%s#%s#%s\r\n" % (link, date, title))


grab("ovj", 2, "gerandong24")

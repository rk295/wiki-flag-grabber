#!/usr/bin/env python
from lxml import html
import requests
import re
import urllib

live = True

if live:
    print "Requesting Live copy"
    page = requests.get('https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags')  # noqa
    data = page.content
else:
    print "Using cached copy"
    f = open('wiki-flags.html')
    data = f.read()
    f.close()

tree = html.fromstring(data)

td_list = tree.xpath('//table/tr/td')

count = 0

for td in td_list:
    link_list = td.xpath('a')

    country_name = None
    country_url = None

    for link in link_list:
        a_class = link.attrib.get('class')
        a_title = link.attrib.get('title')
        a_href = link.attrib.get('href')
        a_text = link.text

        if a_class == 'image':
            # Bit of a hack, I'm only interested in the
            # first image in these cells
            thumb_src = link.xpath('img')[0].attrib['src']
            t = thumb_src.replace('/thumb', '')

            regex = '^(.*)\/.*.png$'
            url_matches = re.search(regex, t)
            country_url = url_matches.group(1)

            name_re = '^.*Flag_of_(.*).svg'
            name_matches = re.search(name_re, country_url)
            country_name_encoded = name_matches.group(1)

            country_name = urllib.unquote(country_name_encoded)

            print "Country:%s URL:https:%s" % (country_name, country_url)

            count = count + 1

print "Found %d flags" % count

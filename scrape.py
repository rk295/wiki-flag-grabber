#!/usr/bin/env python
from lxml import html
import requests
import re
import urllib
import json

LIVE = True


def get_page():
    # Grab the page, either from wikipedia, or from
    # the cached local copy. Returns a string of the
    # page contents
    if LIVE:
        page = requests.get('https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags')  # noqa
        data = page.content
    else:
        f = open('wiki-flags.html')
        data = f.read()
        f.close()

    return data


def parse_page(data):
    # Passed a string of the page contents, attempts to build
    # a dictionary of 'contry name' : 'url' where the url is
    # the url to the full SVG of the flag
    tree = html.fromstring(data)

    td_list = tree.xpath('//table/tr/td')

    flag_dict = {}

    for td in td_list:
        link_list = td.xpath('a')

        country_name = None
        country_url = None

        for link in link_list:
            a_class = link.attrib.get('class')

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

                flag_dict[country_name] = country_url

    return flag_dict


def main():
    flags = parse_page(get_page())
    # Just printing this dict as json for now, other uses
    # will be catered for in the future.
    print json.dumps(flags, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == "__main__":
    main()

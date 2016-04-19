#!/usr/bin/env python
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import pystache
from scrape import parse_page, get_page
from pprint import pprint

template_file = "flags.html.mo"

flag_list = parse_page(get_page())
tpl = open(template_file, "r").read()

print pystache.render(tpl, {"flag_list": flag_list})

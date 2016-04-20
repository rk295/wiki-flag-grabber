Wikipedia Flag Grabber
======================

The two scripts in this repo (`scrape.py` and `generate.py`) parses the list of [Sovereign State Flags](https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags) available on wikipedia.

`scrape.py`
------------

 Builds a python list of dictionaries of the name and the URL to the `SVG` for each.

It can run live (i.e. request the page to be parsed from wikipedia), or from a cached local copy. To use a local copy run this command from inside the same directory as `scrape.py`:

```
curl 'https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags' > wiki-flags.html
```
Then change `LIVE` to be `False` on line 8 of the script.

The output is currently a JSON object, as can be seen below.

`generate.py`
-------------

This script imports two functions from `scrape.py` then renders the [Mustache](http://mustache.github.io/) template `flags.html.mo` (using the [PyStache](https://github.com/defunkt/pystache) module) to a web page on `stdout`. This is formatted ok(ish) to print nicely on A3 paper.


Output example
==============
```
[
{
    "name": "The Turkish Republic of Northern Cyprus",
    "url": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Flag_of_the_Turkish_Republic_of_Northern_Cyprus.svg"
},
{
    "name": "The Sahrawi Arab Democratic Republic",
    "url": "https://upload.wikimedia.org/wikipedia/commons/2/26/Flag_of_the_Sahrawi_Arab_Democratic_Republic.svg"
},
{
    "name": "Somaliland",
    "url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Flag_of_Somaliland.svg"
},
]
```

If you want different output then you'll be wanting to edit the print on line 70.

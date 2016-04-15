Wikipedia Flag Grabber
======================

The script `scrape.py` parses the list of [Sovereign State Flags](https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags) available on wikipedia and builds a python dictionary of the name and the URL to the `SVG` for each.

It can run live (i.e. request the page to be parsed from wikipedia), or from a cached local copy. To use a local copy run this command from inside the same directory as `scrape.py`:

```
curl 'https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags' > wiki-flags.html
```
Then change `LIVE` to be `False` on line 8 of the script.

The output is currently a JSON object, as can be seen below.

Output example
==============
```
{
    "Abkhazia": "//upload.wikimedia.org/wikipedia/commons/2/27/Flag_of_Abkhazia.svg",
    "Afghanistan": "//upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Afghanistan.svg",
    "Albania": "//upload.wikimedia.org/wikipedia/commons/3/36/Flag_of_Albania.svg",
    "Algeria": "//upload.wikimedia.org/wikipedia/commons/7/77/Flag_of_Algeria.svg",
    "Andorra": "//upload.wikimedia.org/wikipedia/commons/1/19/Flag_of_Andorra.svg",
    "Angola": "//upload.wikimedia.org/wikipedia/commons/9/9d/Flag_of_Angola.svg"
}
```

If you want different output then you'll be wanting to edit the print on line 70.

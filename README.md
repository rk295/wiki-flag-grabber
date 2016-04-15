Wikipedia Flag Grabber
======================

The script `scrape.py` parses the list of [Sovereign State Flags](https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags) available on wikipedia and outputs the name and the URL to the `SVG` for each.

It can run live (i.e. request the page to be parsed from wikipedia), or from a cached local copy. To use a local copy run this command from inside the same directory as `scrape.py`:

```
curl 'https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags' > wiki-flags.html
```
Then change `live` to be `False` on line 7 of the script.

Output example
==============
```
Country:Yemen URL:https://upload.wikimedia.org/wikipedia/commons/8/89/Flag_of_Yemen.svg
Country:Zambia URL:https://upload.wikimedia.org/wikipedia/commons/0/06/Flag_of_Zambia.svg
Country:Zimbabwe URL:https://upload.wikimedia.org/wikipedia/commons/6/6a/Flag_of_Zimbabwe.svg
Country:Abkhazia URL:https://upload.wikimedia.org/wikipedia/commons/2/27/Flag_of_Abkhazia.svg
Country:the_Cook_Islands URL:https://upload.wikimedia.org/wikipedia/commons/3/35/Flag_of_the_Cook_Islands.svg
Country:Kosovo URL:https://upload.wikimedia.org/wikipedia/commons/1/1f/Flag_of_Kosovo.svg
```

If you want different output then you'll be wanting to edit the print on line 53.

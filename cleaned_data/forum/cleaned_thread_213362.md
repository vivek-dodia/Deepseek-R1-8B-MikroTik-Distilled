# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213362

# Discussion

## Initial Question
Author: [SOLVED]Wed Dec 18, 2024 5:57 pm
``` /interface wifi channel add band=2ghz-ax disabled=no frequency=2412 name=CHAN-1 width=20mhz add band=2ghz-ax disabled=no frequency=2437 name=CHAN-6 width=20mhz add band=2ghz-ax disabled=no frequency=2462 name=CHAN-11 width=20mhz add band=5ghz-ax disabled=no frequency=5500 name=CHAN-100 width=20/40/80mhz ``` It made me smile...Instead of channels, MikroTik uses frequencies. To get an indication of how you can us it:
```
Make sure to check which radio is wifi 2.4GHz and which 5GHz.I often check the information on wikipedia:https://en.wikipedia.org/wiki/List_of_W ... g/n/ax/be)https://en.wikipedia.org/wiki/List_of_W ... /ac/ax/be)


---
```

## Response 1
Author: Wed Dec 18, 2024 6:12 pm
``` /interface wifi channel add band=2ghz-ax disabled=no frequency=2412 name=CHAN-1 width=20mhz add band=2ghz-ax disabled=no frequency=2437 name=CHAN-6 width=20mhz add band=2ghz-ax disabled=no frequency=2462 name=CHAN-11 width=20mhz add band=5ghz-ax disabled=no frequency=5500 name=CHAN-100 width=20/40/80mhz ``` It made me smile...Instead of channels, MikroTik uses frequencies. To get an indication of how you can us it:
```
Make sure to check which radio is wifi 2.4GHz and which 5GHz.I often check the information on wikipedia:https://en.wikipedia.org/wiki/List_of_W ... g/n/ax/be)https://en.wikipedia.org/wiki/List_of_W ... /ac/ax/be)Many many thanks!!!
```
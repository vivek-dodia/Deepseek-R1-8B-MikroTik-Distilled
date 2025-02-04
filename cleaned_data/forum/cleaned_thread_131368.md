# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 131368

# Discussion

## Initial Question
Author: [SOLVED]Wed Feb 28, 2018 9:44 am
``` ~ normis$ curl https://mikrotikdownload.s3.amazonaws.com/routeros/LATEST.6 6.41.2 1517920142 ~ normis$ curl https://mikrotikdownload.s3.amazonaws.com/routeros/LATEST.6rc 6.42rc35 1519641969 ~ normis$ curl https://mikrotikdownload.s3.amazonaws.com/routeros/LATEST.6fix 6.40.6 1519124692 ``` Here you go:
```
---
```

## Response 1
Author: Wed Feb 28, 2018 9:49 am
``` ~ normis$ curl https://mikrotikdownload.s3.amazonaws.com/routeros/LATEST.6 6.41.2 1517920142 ~ normis$ curl https://mikrotikdownload.s3.amazonaws.com/routeros/LATEST.6rc 6.42rc35 1519641969 ~ normis$ curl https://mikrotikdownload.s3.amazonaws.com/routeros/LATEST.6fix 6.40.6 1519124692 ``` Thank you Normis, this is a hidden knowledge one can only know by chance :)Here you go:
```
---
```

## Response 2
Author: Mon Apr 20, 2020 10:06 am
``` # curl https://download.mikrotik.com/routeros/LATEST.6 6.46.5 1586248107 # curl https://download.mikrotik.com/routeros/LATEST.6rc 6.47beta54 1586154743 # curl https://download.mikrotik.com/routeros/LATEST.6fix 6.45.8 1579763985 ``` Sorry for dredging up an old post but I wanted to share the new URL's as the previous URL's mentioned by @normis have stopped being updated. I was about to post a new post but then worked out the new URL's.
```
Hope this helps someone else.


---
```

## Response 3
Author: Wed Jun 19, 2024 11:02 pm
``` curl https://download.mikrotik.com/routeros/NEWESTa7.stable # 7.15.1 1717764551 curl https://download.mikrotik.com/routeros/NEWESTa7.testing # 7.16beta2 1718183008 ``` ``` curl -s https://download.mikrotik.com/routeros/NEWESTa7.testing | awk '{ print $1 }' ``` https://download.mikrotik.com/routeros/ ... 7.<channel>
```
Or to get just the version, awk works:
```
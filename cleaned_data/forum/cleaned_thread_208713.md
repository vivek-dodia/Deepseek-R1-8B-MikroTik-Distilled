# Thread Information
Title: Thread-208713
Section: RouterOS
Thread ID: 208713

# Discussion

## Initial Question
Hi, is there a good way to remove or whitelist entries from the adlist? ---

## Response 1
There is currently no whitelist function. You can delete it manually from a .txt file ---

## Response 2
There is currently no whitelist function. You can delete it manually from a .txt fileGood to know, thanks for your reply.Is there any example script to do this on the router or do I need to make this externally? ---

## Response 3
It's pretty simple, just fetch the file then add it as a file in adlist. in this following example it will be saved as pro.txtThis just means you will need to keep updating though, as from memory the url will try every hour for an update.
```
/tool/fetch url="https://raw.githubusercontent.com/hagezi/dns-blocklists/main/hosts/pro.txt"mode=httpsThat way you can just edit at your leisure.Warning, make sure you have spare space as that file will use 73608 KiB of memory

---
```

## Response 4
Close. I want to whitelist before the import!Here is my solution on Linux that I would to execute on the router.
```
ADLIST="/var/www/www/adlist"curl-s"https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"-o"${ADLIST}.org"if[$?-eq0];thengrep-v"www.googleadservices.com"<"${ADLIST}.org">"${ADLIST}.txt"chown www-data:www-data"${ADLIST}.org""${ADLIST}.txt"fi

---
```

## Response 5
Yeah normis said they was going to add more features but nothing seen as yet!I'm thinking about using the DOH adlist option (as of 7.16_beta2) for queries but that means registering up on a dns provider doesn't it.https://www.youtube.com/watch?v=w4erB0VzyIE ---

## Response 6
@normis Can I ask about the possibility of adding this feature to the stable version of 7.16? It's too bad to disable the entire ad list because of one domain that the author added to it by mistake. ---

## Response 7
Currently whitelist is available on latest 7.17beta2. For now, I just add static DNS for specific domain.For example, if I want to whitelist "googleadservices.com":1. Disable specific list from adlist2. Open terminal > ping googleadservices.com3. Add the ip to static DNS
```
/ip/dns/static/addname=googleadservices.com match-subdomain=yes address=142.250.105.1544. Enable specific list from adlist

---
```

## Response 8
Currently whitelist is available on latest 7.17beta2. For now, I just add static DNS for specific domain.For example, if I want to whitelist "googleadservices.com":1. Disable specific list from adlist2. Open terminal > ping googleadservices.com3. Add the ip to static DNS
```
/ip/dns/static/addname=googleadservices.com match-subdomain=yes address=142.250.105.1544. Enable specific list from adlistAnd how to block everything except the whitelisted domanin?I don't want to manually add everything that is kind impossible, for my use case I just need to open specific domain.

---
```
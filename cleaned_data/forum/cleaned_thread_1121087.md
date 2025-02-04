# Thread Information
Title: Thread-1121087
Section: RouterOS
Thread ID: 1121087

# Discussion

## Initial Question
Hello, are you having problem adding url list of StevenBlack ? When I add it to Adlist it doesn't recognize any results and matches. I think it's because the sheet starts with this:
```
# Title: StevenBlack/hosts## This hosts file is a merged collection of hosts from reputable sources,# with a dash of crowd sourcing via GitHub## Date: 11 July 2024 19:19:26 (UTC)# Number of unique domains: 155,096## Fetch the latest version of this file: https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts# Project home page: https://github.com/StevenBlack/hosts# Project releases: https://github.com/StevenBlack/hosts/releases## ================================================ ==============127.0.0.1localhost127.0.0.1localhost.localdomain127.0.0.1local255.255.255.255broadcasthost::1localhost::1ip6-localhost::1ip6-loopback
fe80::1%lo0 localhost
ff00::0ip6-localnet
ff00::0ip6-mcastprefix
ff02::1ip6-allnodes
ff02::2ip6-allrouters
ff02::3ip6-allhosts0.0.0.00.0.0.0# Custom host records are listed here.# End of custom host records.# Start StevenBlack#=====================================# Title: Hosts contributed by Steven Black# http://stevenblack.com0.0.0.0ck.getcookiestxt.com0.0.0.0eu1.clevertap-prod.com0.0.0.0wizhumpgyros.com0.0.0.0coccyxwickimp.com0.0.0.0webmail-who-int.000webhostapp.com...........................If I make my own file and copy only the useful information from its list things work.
```

```
0.0.0.0XXXXXXXXXXXXBecause in the video tutorial things work out, but I don't know then if the leaf looked like this .https://help.mikrotik.com/docs/display/ROS/DNSHere is my situation:
```

```
url="https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"ssl-verify=nomatch-count=0name-count=0

---
```

## Response 1
Perhaps should ask Steven?? ---

## Response 2
How do I contact him? ---

## Response 3
I think the problem is you are using this on lower end device that's why the list won't populated try this on RB5009 it should work ---

## Response 4
I tried it on my ax2 and it worked.Anyway I use NextDNS. ---

## Response 5
You're right, I tried it on the RB750Gr3, but I also have a HAP AX³ and it worked, got the list without problems. Well, I will use it for DNS. Thank you very much for the help. ---

## Response 6
This works for smaller devices, as allowances are made for the limitations. Also describes how its done.https://itexpertoncall.com/additional_info/moabpre.htmlquote: "MOAB has two tracks, one for MikroTik Routers like the hEX, hAP ax 2, hAP ax 3, the Audience - tracking between 5K and 16K ipset entries - MikroTik Router models like the CHR, RB3011, RB4011, RB5009, RB1100 and all CCR - tracking between 35K and 60K ipset entries. Once we know which MikroTik Router model you have we will decide if your model qualifies and which track to put you on. Both tracks cover over 600 million IP addresses of known perpetrators.For MikroTik Routers like the CHR, RB3011, RB4011, RB5009, RB1100 and all CCR models the maximum download file size is 1 MB or less - 3 times daily.For MikroTik Routers like the hEX, hAP ax 2, hAP ax 3, the Audience - the maximum download file size is 0.5 MB or less - 3 times daily." ---

## Response 7
I have a similar problem and no matches on a hap ax3> ip/dns/adlist/printFlags: X - disabled0 url="https://raw.githubusercontent.com/Steve ... ster/hosts" ssl-verify=no match-count=0 name-count=100908Any idea? ---

## Response 8
Hi.I have the same problem on CCR1009. ---

## Response 9
You have to set your DHCP server or the hosts themselves manually, the DNS server to be the IP address of the Routerboard on which you use Adlist, then you will start to have reporting. The interesting thing is that for me it gives me 154749 on hAP AX3, and on my virtual machine I installed RouterOS with x86 architecture and there it recognizes them as 17266 entries, and for you it gives them 100908. It's different for everyone, I can't explain it.hAP AX3
```
Flags:X-disabled0url="https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"ssl-verify=nomatch-count=2368name-count=154749Virtual RouterOS x86
```

```
Flags:X-disabled0url="https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"ssl-verify=nomatch-count=0name-count=17266

---
```

## Response 10
Lets see:
```
curl-s https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts | grep -v '#' | sed '/^$/d' | wc -l154749It's not correct because it removes the lines with hash tags even if the hash tag come after correct value.Like this lines.
```

```
0.0.0.0iesnare.com# See http://www.codingthewheel.com/archives/online-gambling-privacy-iesnare0.0.0.0www.iesnare.com# See http://www.codingthewheel.com/archives/online-gambling-privacy-iesnareSo these lists have to be massaged a little bit before going into the mikrotik device.

---
```

## Response 11
Lets see:Let me fix it for you:
```
curl-s https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts | sed -e 's/#.*$//' -e '/^$/d' | wc -l155122

---
```

## Response 12
@mkx Thx, I am not the best regex script kiddiesBut if Mikrotik device count is false, it's also removes all the lines with hash tags.But i not getting it with this low value 17266. Maybe it's not getting the hole file. ---

## Response 13
I've never used adlist feature, but I'd expect it to emit some kind of diagnostic messages upon importing the list. At least, say, number of items successfully imported in info channel and any crucial problem in error channel (e.g. if import breaks in the mid of file due to lack of memory or some such). Without it it's impossible to tell why some hosts have lower number of entries than others (and I'd assume that file parser acts the same on all MT platforms so the difference should then be tied to individual device state differences).BTW, I don't expect comments to be the problem, at least config file parser is well able to ignore comments on the code lines. ---

## Response 14
FIRST increase the DNS cache value a lot. Only then enable it. If you see no matches, 99% it's because of that. ---

## Response 15
I would like to give an update about this:I have an Hex S, indeed it does not allow big files (5MB) when using an URL.But, for small files it DOES download and functionally works from a local server using the URL.Same file, on GitHub. DOES NOT work. ---

## Response 16
The problem is poor/stupid programmer or design decision to download adlist files first to device storage instead of memory.... Since the HexS only has 16 MB of storage, and *at best* only a few MB free with ROS 7, you see the problem.I use this script I made, which downloads the target file into*memory*and not the permanent storage:
```
:delay10s# Check cache size and adjust if not large enough:if([ip/dns/getcache-size]!=32768)do={/ip/dns/setcache-size=32768}# Remove all current adlists/ip/dns/adlistremove[find]# Fetch new adlist source file(s)/tool/fetch url=https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts output=file dst-path=sblack-unified-adlist# Short delay to ensure file is created in RAM:delay1s# Create new adlist from file/ip/dns/adlist/addfile=sblack-unified-adlist# Remove temp file from RAM/fileremovesblack-unified-adlistAnd it works just fine.  That list on my HexS shows:
```

```
[admin@RB760iGS]>/ip/dns/printcache-size:32768KiBcache-max-ttl:1waddress-list-extra-time:0svrf:main
                   cache-used:17819KiB[admin@RB760iGS]>/ip/dns/adlist/printFlags:X-disabled0file=sblack-unified-adlist match-count=0name-count=158886Have fun.Edit:  This also gives added bonus of not needlessly wearing out your flash storage by downloading adlist over and over again to it…

---
```

## Response 17
# Create new adlist from file/ip/dns/adlist/add file=sblack-unified-adlistMaybe change it to# Create new adlist from file/ip/dns/adlist/add file=sblack-unified-adlist ssl-verify=noMikrotik says no about ssl herehttps://help.mikrotik.com/docs/display/ROS/DNS ---

## Response 18
@codelogicThank you!Finally I can also use it with hAP AC2, manually updating the host list every time was a nightmare...I created a scheduler with your script and it works perfectly. ---

## Response 19
@BillyVanSince we're loading the adlist from a file in memory we've downloaded, ssl-verify has no bearing or effect.@MassiniaThanks for confirming. I've had it running on my HexS for a couple of weeks without issue as well.Perhaps my post should be marked as real solution here? ---

## Response 20
SOLUTION, I almost sprayed my coffee on the screenTryWORK AROUND.A solution is for Mikrotik to recognize this issue and to make a decision.a. Default adlist to Memory (volatile?)b. Default adlist to storgage device (non-volatile?)Assuming your work-around is viablec. ADD USER SELECTABLE option when executing adlist to choose which is the preferred method.d. Something else, that is way smarter than what I came up with in a nano-second.@Normisresponse ??? ---

## Response 21
The problem is poor/stupid programmer or design decision to download adlist files first to device storage instead of memory.... Since the HexS only has 16 MB of storage, and *at best* only a few MB free with ROS 7, you see the problem.I use this script I made, which downloads the target file into*memory*and not the permanent storage:
```
:delay10s# Check cache size and adjust if not large enough:if([ip/dns/getcache-size]!=32768)do={/ip/dns/setcache-size=32768}# Remove all current adlists/ip/dns/adlistremove[find]# Fetch new adlist source file(s)/tool/fetch url=https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts output=file dst-path=sblack-unified-adlist# Short delay to ensure file is created in RAM:delay1s# Create new adlist from file/ip/dns/adlist/addfile=sblack-unified-adlist# Remove temp file from RAM/fileremovesblack-unified-adlistAnd it works just fine.  That list on my HexS shows:
```

```
[admin@RB760iGS]>/ip/dns/printcache-size:32768KiBcache-max-ttl:1waddress-list-extra-time:0svrf:main
                   cache-used:17819KiB[admin@RB760iGS]>/ip/dns/adlist/printFlags:X-disabled0file=sblack-unified-adlist match-count=0name-count=158886Have fun.Edit:  This also gives added bonus of not needlessly wearing out your flash storage by downloading adlist over and over again to it…My compliments! On my AC2 it works perfectly, just one thing_ to update the file automatically I imagine I have to create a scheduler in ROS to run the script every certain amount of time (2 times a day?)?

---
```

## Response 22
Just confirmed the problem with the support team. They report that the adblock feature will get some attention on this issue in the near future. ---

## Response 23
The problem is poor/stupid programmer or design decision to download adlist files first to device storage instead of memory.... Since the HexS only has 16 MB of storage, and *at best* only a few MB free with ROS 7, you see the problem.I use this script I made, which downloads the target file into*memory*and not the permanent storage:
```
:delay10s# Check cache size and adjust if not large enough:if([ip/dns/getcache-size]!=32768)do={/ip/dns/setcache-size=32768}# Remove all current adlists/ip/dns/adlistremove[find]# Fetch new adlist source file(s)/tool/fetch url=https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts output=file dst-path=sblack-unified-adlist# Short delay to ensure file is created in RAM:delay1s# Create new adlist from file/ip/dns/adlist/addfile=sblack-unified-adlist ssl-verify=no# Remove temp file from RAM/fileremovesblack-unified-adlistAnd it works just fine.  That list on my HexS shows:
```

```
[admin@RB760iGS]>/ip/dns/printcache-size:32768KiBcache-max-ttl:1waddress-list-extra-time:0svrf:main
                   cache-used:17819KiB[admin@RB760iGS]>/ip/dns/adlist/printFlags:X-disabled0file=sblack-unified-adlist match-count=0name-count=158886Have fun.Edit:  This also gives added bonus of not needlessly wearing out your flash storage by downloading adlist over and over again to it…THANKS,it worked on low-end devices

---
```

## Response 24
I agree thatTHISshouldNOTbe marked as the solution:I think the problem is you are using this on lower end device that's why the list won't populated try this on RB5009 it should workThe OP seems to have disappeared, but the reply thatshouldbe marked as the solution is the script by codelogic. Thank you for a very functional workaround. ---

## Response 25
@codelogic Thank you very much ;)My hEX S | RB760iGS got swamped with ERROR messages in Log file:[adlist] no space to store a filecache full, not storing [ignoring repeated messages]Shame that mt.lvmanual pages for the DNSdo not provide solution, but rather ONLY give an advise:"Adlist is stored on device's internal memory. Ensure that there is enough free space to save the desired adlist."Also had to manually enter the commands one by one as it always finished with error on ROS 7.16if I paste the whole things into the bash..........# Check cache size and adjust if not large enough
```
:if([ip/dns/getcache-size]!=32768)do={/ip/dns/setcache-size=32768}# Remove all current adlists
```

```
/ip/dns/adlistremove[find]# Fetch new adlist source file(s)
```

```
/tool/fetch url="https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"output=file dst-path=sblack-unified-adlist# Create new adlist from file
```

```
/ip/dns/adlist/addfile=sblack-unified-adlist# Remove temp file from RAM
```

```
/fileremovesblack-unified-adlist# Check the "DNS" Settings
```

```
/ip/dns/print# Check the "AdList"
```

```
/ip/dns/adlist/print

---
```

## Response 26
tried today this script on hex s 7.16, adlist loading to memory, works perfect! thanks! ---

## Response 27
I believe this has now been fixed with Router OS 7.17 (2025-Jan-16 10:19):"*) adlist - optimized import on system with low disk space;" ---

## Response 28
Hi! Saving lists to USB drive will save space on the router and the resource of the router's storage chip, will allow you to load lists immediately after rebooting the router:
```
:if[/ip/dns/adlist find]do={/ip/dns/adlist reload};If you have a USB in your router and a flash drive, add this script to the scheduler (once a day), you will always have an updated file on the USB drive::
```

```
# MikroTik Adlist USB by UkRainUa (without external functions)# hardcoded: url, usb1-part1# hAP ac2 7.16, 7.17 - test ok:localscriptName"adlist";/log debug"$scriptName started";# update adlist function:localUpdateAdlistdo={:localscriptName"$1->UpdateAdlist->$description";:do{/log debug"$scriptName started";# fetch new adlist source file/tool/fetch mode=https check-certificate=yes url=$url output=file dst-path=$descriptionas-value;# short delay to ensure file is created:delay1s# check adlist:if([/file/get[find name="$description"]value-name=size]>1000000)do={:if[/ip/dns/adlist findwherefile=$description]do={/ip/dns/adlist reload;/log debug"$scriptName adlist reloaded";}else={# Create new adlist from file/ip/dns/adlistaddfile=$description ssl-verify=no;/log debug"$scriptName adlist added";};}else={/ip/dns/adlistremove[findwherefile=$description];/file/remove[find name=$description];/log warning"$scriptName runtime error: file not created or corrupted, adlist removed";};/log debug"$scriptName executed";}on-error={/log warning"$scriptName runtime error";};};# check cache size and adjust if not large enough:if([ip/dns/getcache-size]!=32768)do={/ip/dns/setcache-size=32768};# StevenBlackFGP: Unified hosts + fakenews + gambling + porn:do{# run adlist update function$UpdateAdlist $scriptName url=https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn/hosts description=usb1-part1/StevenBlackFGP;}on-error={/log warning"$scriptName StevenBlackFGP update failed";};# StevenBlack: Unified hosts (adware + malware)# :do {# # run adlist update function# $UpdateAdlist $scriptName url=https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts description=usb1-part1/StevenBlack;# } on-error={# /log warning "$scriptName StevenBlack update failed;# };# HaGeZiLight:do{# run adlist update function$UpdateAdlist $scriptName url=https://raw.githubusercontent.com/hagezi/dns-blocklists/refs/heads/main/hosts/light.txt description=usb1-part1/HaGeZiLight;}on-error={/log warning"$scriptName HaGeZiLight update failed";};/log debug"$scriptName executed";If fetch ends with an error, the script does nothing but report an error, the file will be downloaded and reloaded next time. A script is possible with checking the message in the log about the success of the fetch execution, it will be a little more complicated, it is wise to use a universal external log analysis function for this.

---
```
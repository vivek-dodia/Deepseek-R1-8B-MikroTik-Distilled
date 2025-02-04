# Thread Information
Title: Thread-1122643
Section: RouterOS
Thread ID: 1122643

# Discussion

## Initial Question
Hello, I believe I found a serious (at least for me) bug in RouterOS. We are using couple of10Gb SFP+ DACcopper pigtail cables between mikrotiks and so far, it worked great. Butafter I upgradedour CRS326-24S+2Q+ from ROS 7beta8 to the latest version of RouterOS 7.12 thosecables became "Connector type: unknown". On one side was ROS 6 which saw the cable and on the other side this ROS7 with unknown status.So, after the update the cable become effectively DEAD - no connection between mikrotiks. ROS6 was showing "Rx Lose", ROS7 "Connector type: unknown". This little stunt left me cut off the ROS7 mikrotik. After that Itried to change portson ROS7 without success (every port - unknown), then Itried to Downgradecouple of times, but also unsuccessfully.At the end Ihad to use Netinstalland revert back to 6.49.15 where the cable works as expected.Picture of the cable data in attachment from version 6.49.15. I can also send any additional information, maybe even experiment at night with what RouterOS version will be the last to recognize the cable correctly.Please fix the RouterOS or we will be stuck on this version forever.Thx ---

## Response 1
Apart from showing "unknown", did the cable work? ---

## Response 2
Apart from showing "unknown", did the cable work?If you are asking if the cable is ok, it did work before. After upgrade to ROSv7 the cable was all dead. ROS6 router was showing "Rx Lose" and ROS7 is just "unknown". Not a single bit came through. That's why I was left cut out of the ROS7 mikrotik.Updated the first post. ---

## Response 3
Apparently nobody knows the answer. Should I write to Mikrotik Support so somebody start doing something about it? It looks like they don't read their forum. ---

## Response 4
Yes, you should ooen a ticket with support.I guess nobody here is able to help you also due to the particular setup you're running (e.g. I've no idea what "10Gb copper pigtail cable" might be ... I'm guessing a passive DAC but ...). ---

## Response 5
Yes, you should ooen a ticket with support.I guess nobody here is able to help you also due to the particular setup you're running (e.g. I've no idea what "10Gb copper pigtail cable" might be ... I'm guessing a passive DAC but ...).Its definitely not a "particular setup". This is normal SFP+ Active Copper Cable that is used everywhere. Mikrotik calls them normally DAC "Direct attach cable" (XS+DA0001, XS+DA0003). I have no idea if it was fixed in last 6 months, I'm afraid to upgrade so it doesn't break. Also found more ppl here in forums that had the same problems with different cables and transceivers after upgrading to v7. ---
# Thread Information
Title: Thread-112806
Section: RouterOS
Thread ID: 112806

# Discussion

## Initial Question
Hello, I'm using my RouterBoard to connect to a wireless network. For example SSID: "network"There are multiple SSID's with the same name "network".The connection to the wireless network is working good.My questions is:Is it possible to specify the BSSID the MikroTik should connect to?Goal:I want the MikroTik to connect to a specific AccessPoint.Greetz, BluRay ---

## Response 1
Hello, I'm using my RouterBoard to connect to a wireless network. For example SSID: "network"There are multiple SSID's with the same name "network".The connection to the wireless network is working good.My questions is:Is it possible to specify the BSSID the MikroTik should connect to?Goal:I want the MikroTik to connect to a specific AccessPoint.Greetz, BluRayHi, yes this is possible, In winbox, click on wireless and you will see the tab "connect list", set it up in there. ---

## Response 2
Thanks this worked! ---

## Response 3
Thanks this worked!No problem ---

## Response 4
Hi!How does this work with the newwifi-package instead of the olderwirelesspackage?Is it now/interface/wifi/access-list/? Can someone post a small example? ---

## Response 5
It does not seem that people know the difference between a BSSiD and a SSiD...Not sure if the Wireless method mentioned above locks into aspecificBSSiD.However, moving on -Can someone advise on how to select aspecidicBSSiD using the newer WiFi package? ---

## Response 6
Deja Vu...I just needed to do this again.I googled keywords and ended up on this thread that I previously asked the same question...Is there no way to specify aspecific BSSiDwhen connecting a MikroTik in Station Bridge or Pseudobridge mode? ---

## Response 7
In principle it's possible to force device to connect to specific BSSID using ACL (in wifi/access-list) ... settingstation-roaming=notoconfigurationdoes help afterwards (so that station doesn't even consider roaming to another BSSID). ---
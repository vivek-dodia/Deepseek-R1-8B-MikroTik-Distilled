# Thread Information
Title: Thread-213330
Section: RouterOS
Thread ID: 213330

# Discussion

## Initial Question
Good morning with everyone here, I just saw a problem with some specific onus of the TPLINK brand and I changed the server and some onus appear with empty MTU apparently they are connected but in reality they are not connected I have to throw it out of the mikrotik so that they just come back Enter and connect, this happened to me because I changed servers. I have a virtual mikrotik on a proxmox server. Currently, I have version V7.15.3 on mikrotik. Please if someone can tell me how to solve this problem ---

## Response 1
Have you narrowed the search down to a particular model and software version of the TP-Link ONUs or you just do not have any other ones in your network?Do you have enough disk space on Proxmox so that you could run tcpdump matching on MAC addresses of several ONUs that exhibit this behavior until the issue re-appears, writing all the traffic of these ONUs into a circular file buffer with storage depth of several days?Were the misbehaving ONUs working initially and the next day you found the interfaces in this weird state or they "connected but not really" this way already at the first connection attempt? ---

## Response 2
Last stable version is 7.16.2Try that version if already fix the problem. ---
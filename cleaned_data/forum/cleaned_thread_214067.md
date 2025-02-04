# Thread Information
Title: Thread-214067
Section: RouterOS
Thread ID: 214067

# Discussion

## Initial Question
Hello.I have some issues with routing between different LAN segments. Idea was to have all hardware on one segment and PCs on other. Networks I have are 172.16.10.0/24 for LAN and 172.16.20.0/27 for network hardwares (APs, Switch, Router, etc.). Now I have new NAS which gets IP (from DHCP) 172.16.20.7. I made this IP as static so it stays reserved for it.Primary idea is that NAS isn't visible from internet so all I did is add firewall rule to access from 172.16.10.0/24 to 172.16.20.7 (NAS IP), because all segments are on same router. For start (or for atleast a day) it worked fine. I was able to ping NAS, I could access it trough browser and I saw folders in Network Discovery.Now I can't even ping. I also read all logs if there are any restrictions or if it's dropping trafic for some reason but there is nothing. NAS is working because if I connect to network 172.16.20.0/27 with my PC, I can do everything.I am mostly familiar with Cisco and I used to create "Router on a stick" for those scenarios, but since Mikrotik is capable to see and reach all networks on same router, I didn't configure any NAT or static routes.Please for help if you have any idea. ---

## Response 1
I don`t think we have enough Information to correctly identify the Problem...Can you Provid eus with the Configuration of the Mikrotik-Device/export file=anynameyouwish ( minus router serial number, any public WANIP information, keys etc.) ---

## Response 2
I don`t think we have enough Information to correctly identify the Problem...Can you Provid eus with the Configuration of the Mikrotik-Device/export file=anynameyouwish ( minus router serial number, any public WANIP information, keys etc.)Hello ConnyMercierThank you for respond. After an afternoon sleep I checked again when I wanted to send you details and apparently firewall add rule (or I did typo, don't know) to drop everything to NAS IP. So I removed and worked like a charm.Thank you anyway ---

## Response 3
Sleep often helps :lol: ---
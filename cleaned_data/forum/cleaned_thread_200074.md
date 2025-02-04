# Thread Information
Title: Thread-200074
Section: RouterOS
Thread ID: 200074

# Discussion

## Initial Question
I use PCC/Connection Marking and when fastrack is enabled it still works but seems slow to respond to connection can I reorder the fastrack rules to allow these to be processed first and the fastrack everything else after? ---

## Response 1
Fastrack and mangling do not mix. Suggest turn fastrack off. Do you mangle all your traffic or just some, if just some one thing you can do is ensure you use connection marks on the traffic you are mangling and then on the fasttrack rule itself add the following at the end ...connection-mark=no-mark ---

## Response 2
Thanks that’s useful I only mark a few src IP so I’ll try that ---

## Response 3
Fasttrack works fine with mangle rules, it's the default rule that doesn't because it forces connections to bypass mangle because it's a firewall rule. The fasttrack no-mark/all other traffic in mangle is an efficient way around the issue, but you can also fasttrack any marked connection as well to avoid queues if you desire. ---

## Response 4
Mangle, PCC and fastracking works fine as long you work cleanly.Fastracking in Firewall comes after Mangle, so Mangle has more influence. BTW you can also mark tot fastrack traffic in Mangle.Remember that once marked fasttracked some traffic will go the slow way to allow checks and changes. Secondly fasttracking and using a VPN on the router don't mix. ---

## Response 5
Fastracking in Firewall comes after Mangle, so Mangle has more influence.You're right. It's the queues that are bypassed. ---

## Response 6
Fastrack and mangling do not mix. Suggest turn fastrack off. Do you mangle all your traffic or just some, if just some one thing you can do is ensure you use connection marks on the traffic you are mangling and then on the fasttrack rule itself add the following at the end ...connection-mark=no-markthanks this seems to helped alot ---

## Response 7
Mangle, PCC and fastracking works fine as long you work cleanly.Fastracking in Firewall comes after Mangle, so Mangle has more influence. BTW you can also mark tot fastrack traffic in Mangle.Remember that once marked fasttracked some traffic will go the slow way to allow checks and changes. Secondly fasttracking and using a VPN on the router don't mix.thanks for the info, I am marking some traffic to go a VPN so the above comment of connection-mark=no-mark works well as I don't want to fastrack the VPN connections ---

## Response 8
I set this (connection-mark=no-mark ) in FasttrackI can now activate the 3 WANs and they work fineBut the bandwidth speed of the providers is still halvedWhat can I do?thanks ---

## Response 9
What can I do?By disabling fasttrack, processing gets much more CPU-intensive. Depending on router model used it often means that router is no more capable of routing at high speeds. ---

## Response 10
Fastracking in Firewall comes after Mangle, so Mangle has more influence.You are wrong. FastTrack (1B) processing worksbeforeMangle (1C)."FastTrack packets bypass firewall, connection tracking, simple queues, queue tree with parent=global, ip traffic-flow, IP accounting, IPSec, hotspot universal client, VRF assignment, so it is up to the administrator to make sure FastTrack does not interfere with other configuration!"https://help.mikrotik.com/docs/spaces/R ... -FastTrack"FastTrack can process packets only in the main routing table so it is the system administrator duty to not FastTrack connections that are going through non-main routing table (thus connections that are processed with mangle action=mark-routing rules). Otherwise packets might be misrouted though the main routing table."That's why I recommend disabling FT in multi-WAN cases based on PCC balancing (Mangle rules).Moreover, FastTrack = Fast Path + Connection Tracking. FastPath handler is used if the following conditions are met:...sniffer or torch is not running...That's why some admins have noticed that load-balancing, VPN, and other traffic may change their behavior during the running of these tools. ---

## Response 11
Hellobut FASTTRACK works with a "change MSS" in the ppp profile? ---

## Response 12
but FASTTRACK works with a "change MSS" in the ppp profile?MSS adjustment happens on first/"new" TCP SYN packet & "new" connections not covered by fasttrack established/related rule... ---
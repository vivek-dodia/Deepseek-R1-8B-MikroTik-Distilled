# Thread Information
Title: Thread-213949
Section: RouterOS
Thread ID: 213949

# Discussion

## Initial Question
I am more-less advanced home user, not a network expert, and I have more-less typical home configuration for such users: Mikrotik RB962UiGS as a main home router, WEB server on Synology NAS on internal network, and router is port-forwarding http(s) traffic to WEB server to be able access WEB server from outside. This configuration already works, no problem with this. Now, I would like to turn off my NAS to do some maintenance. I would like outside clients accessing my WEB server get some more informative custom static web page with some text, like "Server is under maintenance, try again 5 minutes later". What is the best way to achieve this? Obvious way - I have to change my port-forwarding rule to point to another, "secondary", web-server with such page. So, my questions splits into two group of questions:1) What is the best way of automatically (?) change port-forwarding rule, if internal server is not available? Are there any example of script, periodically pinging my NAS, and adjust destination IP base on accessible of NAS?2) Can my RB962UiGS router play role of such "secondary" web-server having only single one static web-page? If can - how to set it up to avoid adding extra device with web-server on my home network only for this purpose?Or, may be my logic is not valid at all, and there is another solution for that?Thank you for any help and suggestions... ---

## Response 1
If you want to solve this Issue via the RouterYou can use the Netwatch-Feature in Router OSYou can configure RouterOS to make a HTTP-Request to the NASIf the Server doesn`t repond, aka "DOWN" you can activate a script to redirect the Traffic.and if the Main Web-Server on the NAS is back online, aka. "UP" you can change it back ---

## Response 2
The best way would be HAProxy for this purpose.if not then use netwatch to monitor your web server and if it fails then the netwatch trigers proper Up/Down scripts.In scripts you should search the rule with comment eg. "WWWredirection" and set the dst address to the needed one up/dpwn ones.Edit ... @Conny ... you were faster ---

## Response 3
Ok, got it about scripting, thank you all!Are there any thoughts on capability to use router as "secondary" web-server to redirect traffic to if main server is down?Do not really have separate special device only for such purpose... ---
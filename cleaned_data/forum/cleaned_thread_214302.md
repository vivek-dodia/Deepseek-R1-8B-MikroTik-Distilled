# Thread Information
Title: Thread-214302
Section: RouterOS
Thread ID: 214302

# Discussion

## Initial Question
Hello.I have a mikrotik with L2TP/ipsec which is working perfect. This router is in main office. The organization have a several offices. Each office is whit static public ip address. When more than one peer make a vpn connection to central office the problem appear.Is it possible to continue using L2TP/IPsec and to configure IKEv2 on same router and to configure users which must work from same source address to use IKEv2.other user will continue use L2tPOr must reconfigure all users ? ---

## Response 1
Could you post your config here beforehand because this shouldn't be the caseexport file=anynameyouwish(minus sensitive info)And to answer your question, IKEv2 can work alongside L2TP if configured properly ---

## Response 2
Or must reconfigure all users ?First, you can indeed use L2TP/IPsec and IKEv2 on the same router, as L2TP/IPsec uses IKE (v1) and the contents of the initial IKE (v1) packet and of the initial IKEv2 packet are distinctive enough that the IPsec stack could sort them out properly.Second, you man not need to change any client configuration - I assume the reason why some moderator has subscribed me to this topic is that I have implemented a solution that allows multiple L2TP/IPsec to connect from the same site:viewtopic.php?t=132823. ---
# Thread Information
Title: Thread-214011
Section: RouterOS
Thread ID: 214011

# Discussion

## Initial Question
Hello, I need some help please in how to route VPN traffic (that is separate from regular traffic) FROM a PFSense box, TO my CRS328, from there TO my CRS 109, from there TO a PC, over VLAN 50. See attached diagram.The standard internet connection on the CRS328 gets its IP address via DHCP from the PFsense box, but for VLAN 50, the PFSense box this time is a client to the CRS328 for IP addresses.How can I do this?Thanks, Julian ---

## Response 1
CRS328 -->https://www.youtube.com/watch?v=YLtGQAQ8iS0&t=16s/viewtopic.php?t=143620 ---

## Response 2
Doesn't answer the question sorry. Its a bit more complicated than the guide literally everyone here has read. ---

## Response 3
Not at ALL, conceptually not difficult. assuming you did the opensense properly, you have one trunk port to the 328 and at least one trunk port to the 109. The managment vlan must reach the 109 as all switches get an IP address on that subnet.However not interested in your opinion only on facts and evidence ( for 328)/export file=anynameyouwish (minus device serial number, any public WANIP information, keys etc.) ---
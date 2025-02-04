# Thread Information
Title: Thread-1115985
Section: RouterOS
Thread ID: 1115985

# Discussion

## Initial Question
Hello, I use the "BTest Server" and the "Bandwidth Test" client between a 4G WAP LTE router and a CCR on a fiber link.Most of the time it works well, except on some 4G operator which blocks the TCP 2000 port ...How could I modify the TCP port "BTest Server" and the client "Bandwidth Test" in order to make them work when the TCP port 2000 is blocked?Thanks for your help. ---

## Response 1
Hello Team, i hav the same topic.fortigate in standard config can not forward the port 2000.https://community.fortinet.com/t5/Forti ... a-p/338769please make the port flexible.A variable port can also help me to test the connection in the SD-WAN individually.(we use an AAR that makes it possible to assign different ports or applications to the appropriate path)Best Christmas wishes.Marcus ---
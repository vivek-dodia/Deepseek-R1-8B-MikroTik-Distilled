# Thread Information
Title: Thread-153287
Section: RouterOS
Thread ID: 153287

# Discussion

## Initial Question
Hello, i have a simple question - is it possible to limit speed on ipsec vpn peer?Sorry if this is dumb to ask, but i didnt find any info on that topic and one of my roadwarriors is transmitting a lot of bytes through tunnel. Its not a problem, but i got curious - is it possible to limit him. ---

## Response 1
I'm absolutely no expert, but I believe this shouldn't be difficult to implement assuming the following is true. Are you able to identify the RW by a consistent IP? If not, I think you can achieve that through a combination of /ip ipsec identity and /ip ipsec peer.I found this just now from here:viewtopic.php?t=81797. If you can identify by IP, should be that simple. I'm a bit of a newb though.
```
# Limit Bandwidth of each IP in an entire subnet:/queue typeadd kind=pcq name=pcq-upload-custom pcq-classifier=src-address pcq-rate=2Madd kind=pcq name=pcq-download-custom pcq-classifier=dst-address pcq-rate=2M/queue simpleadd name=Throttle-Each queue=pcq-upload-custom/pcq-download-custom \target=192.168.1.0/24

---
```

## Response 2
I'm absolutely no expert, but I believe this shouldn't be difficult to implement assuming the following is true. Are you able to identify the RW by a consistent IP? If not, I think you can achieve that through a combination of /ip ipsec identity and /ip ipsec peer.I found this just now from here:viewtopic.php?t=81797. If you can identify by IP, should be that simple. I'm a bit of a newb though.
```
# Limit Bandwidth of each IP in an entire subnet:/queue typeadd kind=pcq name=pcq-upload-custom pcq-classifier=src-address pcq-rate=2Madd kind=pcq name=pcq-download-custom pcq-classifier=dst-address pcq-rate=2M/queue simpleadd name=Throttle-Each queue=pcq-upload-custom/pcq-download-custom \target=192.168.1.0/24Yeah i thought that too. like simple queue should work. and yes i can assign a static remote ip to RW (i am using windows NPS as auth method.)But i tested this and if i use simple queue - connection breaks as soon as user starts to do smth(like copy file through vpn) and shaper was not even that little. it was 15M.

---
```

## Response 3
Actually i was testing simple queue when fasttrack was working for ipsec peers. its not disconnecting anymore.but yeah queue works only if remote peer has static ip. not that i give him but his public. kinda meh ---

## Response 4
Could you not use a unique identity verified by a unique cert to assign the client a specific IP each time they connect, like the example here:https://wiki.mikrotik.com/wiki/Manual:I ... figurationI apologize if this is really obvious and already thought of. Just trying to contribute. ---

## Response 5
Could you not use a unique identity verified by a unique cert to assign the client a specific IP each time they connect, like the example here:https://wiki.mikrotik.com/wiki/Manual:I ... figurationI apologize if this is really obvious and already thought of. Just trying to contribute.Sorry for not answering, been busy and forgot.So the thing is - i can assign static ip for any client. its easy with raidus server.But simple queue shaper not working for vpn subnet. it works only for client wan address. i tested it. maybe i miss smth, idk. ---

## Response 6
Old topic but want to share my experience here.Used help topichttps://help.mikrotik.com/docs/display/ ... outerOSv7)and have a running IKEv2+Radius setup for my roadwarrior clinets now.BUT neither the simple qeue nor the UserManager rate limit works for the traffic shaping of the clients... ---

## Response 7
IPsec rate limit can be implemented by using packet marks. Mangle rule to mark IPsec packets (separate rule and marks for UL and DL) and simple queue applied to those marks. ---
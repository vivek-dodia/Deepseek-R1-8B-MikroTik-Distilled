# Thread Information
Title: Thread-1121861
Section: RouterOS
Thread ID: 1121861

# Discussion

## Initial Question
I'm trying to configure CCR2004-1G-12S+2XS as a router for my home lab. I got a symmetric 25G/25G fiber connection.So far I only have a very minimal configuration:
```
/interface bridge
add name=lan port-cost-mode=short

/ip pool
add name=dhcp_pool0 ranges=192.168.1.2-192.168.1.254

/ip dhcp-server
add address-pool=dhcp_pool0 interface=lan name=dhcp1

/interface bridge port
add bridge=lan interface="sfp28-1" internal-path-cost=10 path-cost=10
add bridge=lan interface="sfp-sfpplus1" internal-path-cost=10 path-cost=10
add bridge=lan interface="sfp-sfpplus2" internal-path-cost=10 path-cost=10
add bridge=lan interface="sfp-sfpplus3" internal-path-cost=10 path-cost=10
add bridge=lan interface="sfp-sfpplus4" internal-path-cost=10 path-cost=10
add bridge=lan interface="sfp-sfpplus5" internal-path-cost=10 path-cost=10
add bridge=lan interface="sfp-sfpplus6" internal-path-cost=10 path-cost=10
add bridge=lan interface="sfp-sfpplus7" internal-path-cost=10 path-cost=10
add bridge=lan interface="sfp-sfpplus8" internal-path-cost=10 path-cost=10
add bridge=lan interface="sfp-sfpplus9" internal-path-cost=10 path-cost=10
add bridge=lan interface="sfp-sfpplus10" internal-path-cost=10 path-cost=10
add bridge=lan interface="sfp-sfpplus11" internal-path-cost=10 path-cost=10
add bridge=lan interface="sfp-sfpplus12" internal-path-cost=10 path-cost=10

/ip address
add address=192.168.88.1/24 comment=defconf interface= ether1 network=192.168.88.0
add address=192.168.1.1/24 interface=lan network=192.168.1.0

/ip dhcp-client
add interface=sfp28-2

/ip dhcp-server lease

/ip dhcp-server network
add address=192.168.1.0/24 gateway=192.168.1.1

/ip firewall filter
add action=fasttrack-connection chain=forward hw-offload=yes

/ip firewall nat
add action=masquerade chain=srcnat out-interface=sfp28-2I got my fiber connection plugged into sfp28-2, and sfp28-1 is connected via 25G DAC cable to my server.The issue is that by plugging fiber directly to my server I'm getting 25/25 speeds as expected:https://www.speedtest.net/result/c/56f1 ... 45797a80aaBut when using Mikrotik as a router, even with such a minimal configuration, the upload speed drops dramatically to 20-25% of the expected speed, while download remains more or less the same:https://www.speedtest.net/result/c/538d ... 67c65524eeI did try two completely different DAC cables getting exactly the same result, so I don't believe it is an issue here. I also tried swapping SFP28 ports (accordingly changing Mikrotik configuration) which also didn't affect the results in any way.Is this how it is supposed to work, or am I missing some important bit of the configuration?

---
```

## Response 1
One weird thing I noticed is that when I switch my DAC going to my lab PC on the Mikrotik side from 25G SFP28 port to a 10G SFP+ one, my download speed goes down to 10G (exactly as expected), but my upload speed goes UP to 10G (these results are consistent and reproducible).Unfortunately, I don't know much beyond basics in networking, so can't explain this in the right terms, but I think what happens is when my PC is plugged into 25G port, it allows full 25G to be pushed into the router, but WAN interface is a bit slower, so the same 25G can't leave the router which eventually leads to some buffers in the router overflowing and requiring packet retransmits, which in turn kills the throughput.Did anyone face something similar before? I feel it should be some well known case that is fixed by some configuration change – but I couldn't figure that out myself. ---

## Response 2
I had a similar issue, direct connection to server (fedora) = full speed but via the 2004 low upload speed. Turned out we had to tune the buffers or some other setting on the linux server to fix it. The guy that did it got fired from that company shortly after so I never got a chance to talk to him, but sysctl and sysctl.conf is where you should start. I'll have access to the server this weekend and I bet it is going to cause issues again so gonna pull the conf out and compare with the defaults. If I can find the changes will post them here for you.EDIT: this might help you outhttps://fasterdata.es.net/host-tuning/linux/EDIT2: For fasttrack to work you also need one more rule under the fasttrack onehttps://wiki.mikrotik.com/wiki/Manual:I ... figuration
```
/ip firewall filter add action=accept chain=forward connection-state=established,relatedHW offload does not work on 2004, you need a ccr 2116 or 2216 for that.

---
```

## Response 3
It could also could help to enable flow control on both the server network card and the CCR2004 Ethernet port facing the server. ---

## Response 4
Hi, I have similar problems, I have a 980/110 connection where I actually get 540/110, I can say that I have standard settings for the firewall. A computer connected directly to the connection gets full bandwidth and the router only 540The OS is the latest 7.17 but that didn't help eitherThe settings of the interface itself also didn't bring any solutionsCan I ask for directions on what else I can check ---

## Response 5
I have similar problems, I have a 980/110 connection where I actually get 540/110, ...It doesn't seem similar (to me),. the previous posts were about saturating in upload a 10 Gb links and not reaching 25 Gb, you are having a slow download and a CCR2004 should reach 1 Gb easily both in upload and download even with a sub-optimal configuration.You should start a new thread, describing your setup and posting your current configuration following these instructions:viewtopic.php?t=203686#p1051720 ---
# Thread Information
Title: Thread-213551
Section: RouterOS
Thread ID: 213551

# Discussion

## Initial Question
Hello.I have a question about the setting / default inip/dns/statichere, in addition to the host IP address, there is also the entry "router.lan". Unfortunately, this doesn't work if I enter this name in the browser line and the web console is called up.Now I have more devices that only offer a web console via the IP address, so I thought I could enter a name for these devices there so that I don't always have to enter the IP.How does this work exactly?ThanksFrank ---

## Response 1
1. via dhcp-server you have to send the IP of your router in LAN/ip dhcp-server network set dns-server=192.168.88.1 domain=name.local2. open port for DNS in firewall/ip/firewall/filter add action=accept protocol=udp port=533. allow remote requests/ip dns set allow-remote-requests=yes4. add static entry/ip dns static add address=192.168.88.2 name=switch.local type=A ---

## Response 2
I agree, except for this part:2. open port for DNS in firewall/ip/firewall/filter add action=accept protocol=udp port=53Apart from a missing chain, you don't want to provide access to your DNS server from the internet.And there is a default rule in place that implicitely provides access to the router from LAN:
```
addchain=input action=dropin-interface-list=!LAN comment="defconf: drop all not coming from LAN"

---
```
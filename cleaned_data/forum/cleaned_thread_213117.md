# Thread Information
Title: Thread-213117
Section: RouterOS
Thread ID: 213117

# Discussion

## Initial Question
First of all here my settings* 2024-12-06 17:22:59 by RouterOS 7.16.2
```
# software id = XE51-3KWQ## model = CCR2004-1G-12S+2XS# serial number = xxxxxx/interfaceethernetset[finddefault-name=sfp-sfpplus2]arp=proxy-arp name="LAN "set[finddefault-name=ether1]name=MNGset[finddefault-name=sfp-sfpplus1]name=WAN/interfacewireguardaddlisten-port=17304mtu=1420name=VPN/interfacevlanaddinterface=WAN name="PROVIDER VLAN"vlan-id=XXX/interfacepppoe-clientaddadd-default-route=yes disabled=nointerface="PROVIDER VLAN"name=PROVIDER user=\Xxxxxxx/interfacewireless security-profilesset[finddefault=yes]supplicant-identity=MikroTik/ip pooladdname=dhcp_pool0 ranges=192.168.100.2-192.168.100.254/ip dhcp-serveraddaddress-pool=dhcp_pool0interface="LAN "lease-time=1dname=dhcp1/portset0name=serial0set1name=serial1/ip firewall connection trackingsetudp-timeout=10s/interfacewireguard peersaddallowed-address=172.22.0.2/24interface=VPN name=GETACPublickey="redacted"/ip addressaddaddress=192.168.100.1/24interface="LAN "network=192.168.100.0addaddress=172.22.0.1/24interface=VPN network=172.22.0.0/ip cloudsetddns-enabled=yes ddns-update-interval=1m/ip dhcp-server leaseaddaddress=192.168.100.2client-id=1:50:6b:4b:84:6:70mac-address=\50:6B:4B:84:06:70server=dhcp1addaddress=192.168.100.3client-id=1:50:6b:4b:7c:a6:20mac-address=\50:6B:4B:7C:A6:20server=dhcp1addaddress=192.168.100.9client-id=1:4e:da:85:4b:a0:8fmac-address=\4E:DA:85:4B:A0:8Fserver=dhcp1addaddress=192.168.100.249client-id=1:9c:93:4e:e9:47:be mac-address=\9C:93:4E:E9:47:BE server=dhcp1addaddress=192.168.100.11client-id=1:b4:2e:99:9b:99:b3 mac-address=\
    B4:2E:99:9B:99:B3 server=dhcp1addaddress=192.168.100.12client-id=1:b0:60:88:ad:5c:8cmac-address=\
    B0:60:88:AD:5C:8Cserver=dhcp1/ip dhcp-server networkaddaddress=192.168.100.0/24dns-server=192.168.100.1gateway=192.168.100.1/ip dnssetallow-remote-requests=yes cache-size=40000KiBservers=1.1.1.1/ip dns adlistaddssl-verify=nourl=\
    https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts/ip firewall nataddaction=masquerade chain=srcnat/ip ipsec profileset[finddefault=yes]dpd-interval=2mdpd-maximum-failures=5/ip servicesettelnet disabled=yessetftp disabled=yessetwww disabled=yessetssh address=192.168.100.3/32,172.22.0.2/32port=9442setapi disabled=yessetwinbox address=192.168.100.3/32,172.22.0.2/32setapi-ssl disabled=yes/ip sshsethost-key-size=4096strong-crypto=yes/system clocksettime-zone-name=XXXX/system identitysetname=Datacenter/system notesetshow-at-login=no/system routerboard settingssetenter-setup-on=delete-keyProbably I am missing something stupid but this thing is driving me crazy..This is what I get when I try to do an nslookupThis are the scenarios:First scenario*  DNS IP in DHCP server set to 192.168.100.1*  DNS in windows set to 192.168.100.1*  Running "nslookup google.com 192.168.100.1*  Results in server unknown/timeout*  Running nslookup google.com*  Results in server unknown/timeoutSecond scenario*  DNS IP in DHCP server set to 192.168.100.1*  DNS in windows automatic*  Running "nslookup google.com 192.168.100.1"*  Results in server unknown/timeout*  Running nslookup google.com*  Results in server unknown/timeoutThird scenario*  DNS IP in DHCP server set to 192.168.100.1*  DNS in windows set to 1.1.1.1*  Running "nslookup google.com 192.168.100.1"*  Results in server unkmown/tineout*  Running 'nslookup google.com' insted*  Results in address 1.1.1.1 and a valid querySo I get no internet or no matchesI am probably missing out something stupid but I really cant deal with this anymore..I am going crazyJust to say, I have deleted all of the firewall rules and nat rules because I want to exclude as much as possible

---
```

## Response 1
hello, 
```
/ip firewall nataddaction=masquerade chain=srcnatthat masquerade option needs output interface parameters (ie. wan internet). otherwise any communication won't work correctly.

---
```

## Response 2
Hi, thanks for replying!What do you mean sorry? That rule is what makes me possible to connect to the internet.What do I have to modify? As for now everything work perfectly aside this damned adlist ---

## Response 3
hello, 
```
/ip firewall nataddaction=masquerade chain=srcnatthat masquerade option needs output interface parameters (ie. wan internet). otherwise any communication won't work correctly.Man, I am literally on the verge of crying, thanks.I informed myself more and pointed the nat rule only to my wan interface. Well, now my adlist is working correctly.Thanks <3

---
```
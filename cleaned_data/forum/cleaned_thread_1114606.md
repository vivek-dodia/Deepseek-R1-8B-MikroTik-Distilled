# Thread Information
Title: Thread-1114606
Section: RouterOS
Thread ID: 1114606

# Discussion

## Initial Question
Hello guys, i have this config
```
/interfacebridgeaddname=bridge1/interfacewireguardaddlisten-port=13231mtu=1420name=wireguard1/interfacevlanaddinterface=ether1 name=vlan835 vlan-id=835/interfacebondingaddname=bonding1 slaves=ether2,ether3,ether4/interfacepppoe-clientaddadd-default-route=yes disabled=nointerface=vlan835 name=pppoe-out1 user=xxxxxxx/interfacewifi securityaddauthentication-types=wpa2-psk,wpa3-psk disabled=noname=profile_wifi/interfacewifiset[finddefault-name=wifi1]channel.width=20/40/80mhzconfiguration.country="United States".mode=ap.ssid="Principe Wifi"security=profile_wifiset[finddefault-name=wifi2]channel.width=20/40mhzconfiguration.country="United States".mode=ap.ssid="Principe Wifi"security=profile_wifi/ip hotspot profileset[finddefault=yes]html-directory=hotspot/ip pooladdname=dhcp_pool2 ranges=192.168.2.2-192.168.2.254/ip dhcp-serveraddaddress-pool=dhcp_pool2interface=bonding1 name=dhcp2/interfacebridge portaddbridge=*Binterface=ether5addbridge=*Binterface=wifi1addbridge=*Binterface=wifi2/interfaceovpn-server serveraddmac-address=FE:50:BF:D9:5E:E7 name=ovpn-server1/interfacewireguard peersaddallowed-address=192.168.10.2/32interface=wireguard1 name="Diego - Smartphone"public-key="yI3gQbO3SxuaylV4Y/k2ZHA4vUAziRJiSUcAzFAPF0k="addallowed-address=192.168.10.3/32interface=wireguard1 name="Ricky 5G"public-key="sh41+VdWxPVs44+o2oBXLbfxjRyjOjGd4jgjcEklLVg="addallowed-address=192.168.10.4/32interface=wireguard1 name="Diego - Fire Stick Tv"private-key="mFTNd3KmaVVzasPxCbdSJCF+PCqbXGJTtkfrwHO+A1s="public-key="gNKear5uYEgfCzsPnqEzAE97pdrJ7cQD5e56ggZ3DDw="/ip addressaddaddress=192.168.2.1/24interface=bonding1 network=192.168.2.0addaddress=192.168.10.1/24interface=wireguard1 network=192.168.10.0/ip arpaddaddress=192.168.2.7interface=bonding1 mac-address=04:09:73:DA:24:F0/ip cloudsetddns-enabled=yes ddns-update-interval=1m/ip dhcp-server networkaddaddress=192.168.2.0/24dns-server=8.8.8.8gateway=192.168.2.1/ip dnssetallow-remote-requests=yes servers=8.8.8.8,8.8.4.4,192.168.1.3/ip firewall filteraddaction=fasttrack-connection chain=forward comment="Enable FastTrack"connection-state=established,related hw-offload=yesaddaction=accept chain=input comment="allow Wireguard"dst-port=13231protocol=udpaddaction=accept chain=input dst-port=445in-interface=pppoe-out1 protocol=tcp/ip firewall nataddaction=masquerade chain=srcnatout-interface=pppoe-out1addaction=dst-nat chain=dstnat dst-port=445in-interface=pppoe-out1 protocol=tcp to-addresses=192.168.2.7to-ports=445/ip ipsec profileset[finddefault=yes]dpd-interval=2mdpd-maximum-failures=5/ip servicesettelnet disabled=yessetftp disabled=yessetwww disabled=yessetssh disabled=yessetapi disabled=yessetwinbox disabled=yessetapi-ssl disabled=yes/ip smb sharesset[finddefault=yes]directory=pub/system clocksettime-zone-name=Europe/Rome/system identitysetname=MikroRik/system notesetshow-at-login=no/system ntp clientsetenabled=yes/system ntp client serversaddaddress=it.pool.ntp.org/systempackageupdatesetchannel=testing/system routerboard settingssetcpu-frequency=1800MHzafter i put in a lot of simple queues and after deleting them i went down in speed. i was reaching 2250 mbps without fasttrack now i reach 1650 mbps without fasttrack and 1900 mbps with fast track. symptoms are like something got broken in the config and it's limiting my max speed. I tried to reset with no config and it reaches the full speed but i need al this config and i don't want to redo it. God bless this mf no sense routers <3 please help xDP.S. the command i used to put a lot of simple queues was this:
```

```
:forxfrom2to254do={/queue simple add name="queue-$x" queue=Cake/Caketotal-queue=Cakemax-limit=500M/500Mtarget="192.168.2.$x"}

---
```

## Response 1
you didn't write what hardware you are using?what type queue is cake? (this section is missing in the configuration)creating so many queues you should have a parent for them ---

## Response 2
This bridge has no name:
```
/interfacebridge portaddbridge=*Binterface=ether5addbridge=*Binterface=wifi1addbridge=*Binterface=wifi2Whenever there is an asterisk followed by a (hex) number it means that "something" was there but was removed or deleted and Ros lost track of it, so it placed a reference to it in the form of *<number>.Such cases may or may not be relevant, but they should be fixed anyway.

---
```
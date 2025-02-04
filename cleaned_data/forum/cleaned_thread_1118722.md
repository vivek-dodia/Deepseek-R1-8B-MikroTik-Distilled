# Thread Information
Title: Thread-1118722
Section: RouterOS
Thread ID: 1118722

# Discussion

## Initial Question
I currently have an ubuntu vps acting as a wireguard server. I can connect different devices to the server successfully from inside my home network and with celular data. I currently have tmobile home internet. I connected an rb952 to the tmobile router and configured the wireguard interface and peer. The mikrotik would be acting as a client. ROuter has No default configuration. I can access the internet with devices connected to the mikrotik wifi thats acting as a bridge but wireguard is not doing the handshaking with the server. Any ideas?# 2025-01-09 17:22:09 by RouterOS 7.16.2# software id = U13N-3S1V## model = RB952Ui-5ac2nD# serial number =/interface bridgeadd name=bridge1/interface wirelessset [ find default-name=wlan1 ] ssid=MikroTikset [ find default-name=wlan2 ] ssid=MikroTik/interface wireguardadd listen-port=51820 mtu=1420 name=wg1/interface wireless security-profilesset [ find default=yes ] supplicant-identity=MikroTik/interface bridge portadd bridge=bridge1 interface=all/interface wireguard peersadd allowed-address=0.0.0.0/0 client-address=10.8.0.7/24 client-dns=1.1.1.1 \client-endpoint=XX>XX.XX.XX client-listen-port=51820 endpoint-address=\XX.XX.XX.XX endpoint-port=51820 interface=wg1 name=peer1 preshared-key=\"NiBmzxcmYgVf7KoPcweqhnGvfjMlYUbsxr7ITh9p4NA=" private-key=\"8H/xgcG5EOys0I/BNIO8O8yFWJXzJVQyVFb7t96bOmk=" public-key=\"6B4Rg1yE4arG10Mf1phPwbYE7AZ4HHSkloi7s2Va420="/ip addressadd address=10.8.0.7/24 interface=wg1 network=10.8.0.0/ip dhcp-clientadd interface=bridge1/system noteset show-at-login=no ---

## Response 1
I suspect you may need the MT to act as a router vice switch/bridge? ---

## Response 2
I suspect you may need the MT to act as a router vice switch/bridge?the MT has a bridge configured and all the ports are inside that bridge, the bridge is receiving ip from the Tmobile router, if thats what you mean. But if you mean putting the Tmobile router in bridge mode, not able to do that, tmobile router is restricted ---

## Response 3
I presume that the XX.XX.XX.XX is not on the same network 10.8.0.0/24, right?Can you ping successfully the XX.XX.XX.XX endpoint address from the router?If not, which error do you get? ---

## Response 4
I presume that the XX.XX.XX.XX is not on the same network 10.8.0.0/24, right?Can you ping successfully the XX.XX.XX.XX endpoint address from the router?If not, which error do you get?the endpoint address is 74.208.xx.xxfrom the MT router i can ping google but no the endpoint, timeouton my windows machine i also cant ping the endpoint but that does not prevent me from connecting other devices to the wireguard tunnel ---

## Response 5
It sounds like the Mikrotik router may not have the correct routes or NAT configuration for WireGuard traffic.Debug with `/log print` or `torch` to see if packets are leaving and returning correctly. ---

## Response 6
It sounds like the Mikrotik router may not have the correct routes or NAT configuration for WireGuard traffic.Debug with `/log print` or `torch` to see if packets are leaving and returning correctly. ---

## Response 7
UNfortunately the "timeout" in the ping could be due to anything along the connection, including the remote 74.208.xx.xx prevented from replying to ICMP requests (newish windows as an example have a firewall rule that prevents replying from pings coming from outside the local lan), but it could as well be something in the local router settings.I am still not convinced that the router can reach the endpoint./tool traceroute?And tracert on windows? ---

## Response 8
UNfortunately the "timeout" in the ping could be due to anything along the connection, including the remote 74.208.xx.xx prevented from replying to ICMP requests (newish windows as an example have a firewall rule that prevents replying from pings coming from outside the local lan), but it could as well be something in the local router settings.I am still not convinced that the router can reach the endpoint./tool traceroute?And tracert on windows?[admin@MikroTik] > /tool tracerouteaddress: 66.179.191.147Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV# ADDRESS LOSS SENT LAST AVG BEST WORST STD-DEV1 172.20.10.1 0% 1 4.8ms 4.8 4.8 4.8 02 100% 1 timeout3 100% 1 timeout4 100% 1 timeout5 100% 1 timeout6 100% 1 timeout7 100% 1 timeout8 100% 1 timeout9 0% 1 0msI suspect I am missing something in the configuration in the mikrotik cause if it take the wireguard config and put it in my iPhone or my computer, i can connect to the wireguard server no matter the network i am connected to( home wifi, office wifi, or celullar data), but the mikrotik doesnt, i may be missing some configuration but cant figure it out ---

## Response 9
Well it gets to 172.20.10.1 (and stops there) .What is that address?Your network gateway?I don't really understand how it even gets there without a route (I was suspecting a ping error of "no route to host".).Anyway, post the output of:
```
/ip addressprintand of
```

```
/ip routeprintso that we can check what is created dynamically.

---
```

## Response 10
Well it gets to 172.20.10.1 (and stops there) .What is that address?Your network gateway?I don't really understand how it even gets there without a route (I was suspecting a ping error of "no route to host".).Anyway, post the output of:
```
/ip addressprintand of
```

```
/ip routeprintso that we can check what is created dynamically.wrong output on top[admin@MikroTik] > /tool tracerouteaddress: 74.208.197.52Columns: ADDRESS, LOSS, SENT, LAST, AVG, BEST, WORST, STD-DEV#  ADDRESS       LOSS  SENT  LAST     AVG  BEST  WORST  STD-DEV1  192.168.12.1  0%       1  0.6ms    0.6  0.6   0.6          02  192.0.0.1     0%       1  7.8ms    7.8  7.8   7.8          03                100%     1  timeout4                100%     1  timeout5                100%     1  timeout6                100%     1  timeout7                100%     1  timeout8                100%     1  timeout9                100%     1  timeout10                100%     1  timeout11                100%     1  timeout12                100%     1  timeout13                100%     1  timeout14                100%     1  timeout15                100%     1  timeout16                0%       1  0ms[admin@MikroTik] > /ip address printFlags: D - DYNAMICColumns: ADDRESS, NETWORK, INTERFACE#   ADDRESS            NETWORK       INTERFACE0 D 192.168.12.164/24  192.168.12.0  ether11   10.8.0.2/24        10.8.0.0      wg1[admin@MikroTik] > /ip route printFlags: D - DYNAMIC; A - ACTIVE; c - CONNECT, d - DHCPColumns: DST-ADDRESS, GATEWAY, DISTANCEDST-ADDRESS      GATEWAY       DISTANCEDAd 0.0.0.0/0        192.168.12.1         1DAc 10.8.0.0/24      wg1                  0DAc 192.168.12.0/24  ether1               0The 192.168.12.0/24 is my home network, 10.8.0.0 is wireguard network

---
```

## Response 11
# model = RB952Ui-5ac2nD# serial number =/interface bridgeadd name=bridge1/interface listadd name=WANadd name=LAN/interface list memberadd interface=ether1 list=WANadd interface=wg1 list=WANadd interface=bridge1 list=LAN/ip pooladd name=bridge-pool ranges=192.168.88.2-192.168.88.254/ip dhcp-serveradd address-pool=bridge-pool interface=bridge1 name=bridge-server/interface wireguardadd listen-port=62220 mtu=1420 name=wg1/interface bridge portadd bridge=bridge1 interface=ether2add bridge=bridge1 interface=ether3etc./interface wireguard peersadd allowed-address=0.0.0.0/0 endpoint-address=XX.XX.XX.XX endpoint-port=51820 \interface=wg1 name=peer1 preshared-key="=" private-key="-=" public-key="="/ip addressadd address=10.8.0.7/24 interface=wg1 network=10.8.0.0add address=192.168.88.1/24 interface=bridge1 network=192.168.88.0/ip dnsset allow-remote-requests=yes servers=1.1.1.1/ip dhcp-server networkadd address=192.168.88.0/24 dns-server=192.168.88.1 gateway=192.168.88.1/ip dhcp-clientadd interface=ether1 default route=yes peer-dns=yes/ip neighbor discovery-settingsset discover-interface-list=LAN/ip firewall natadd action=masquerade chain=srcnat out-interface-list=WAN ---

## Response 12
# model = RB952Ui-5ac2nD# serial number =/interface bridgeadd name=bridge1/interface listadd name=WANadd name=LAN/interface list memberadd interface=ether1 list=WANadd interface=wg1 list=WANadd interface=bridge1 list=LAN/ip pooladd name=bridge-pool ranges=192.168.88.2-192.168.88.254/ip dhcp-serveradd address-pool=bridge-pool interface=bridge1 name=bridge-server/interface wireguardadd listen-port=62220 mtu=1420 name=wg1/interface bridge portadd bridge=bridge1 interface=ether2add bridge=bridge1 interface=ether3etc./interface wireguard peersadd allowed-address=0.0.0.0/0 endpoint-address=XX.XX.XX.XX endpoint-port=51820 \interface=wg1 name=peer1 preshared-key="=" private-key="-=" public-key="="/ip addressadd address=10.8.0.7/24 interface=wg1 network=10.8.0.0add address=192.168.88.1/24 interface=bridge1 network=192.168.88.0/ip dnsset allow-remote-requests=yes servers=1.1.1.1/ip dhcp-server networkadd address=192.168.88.0/24 dns-server=192.168.88.1 gateway=192.168.88.1/ip dhcp-clientadd interface=ether1 default route=yes peer-dns=yes/ip neighbor discovery-settingsset discover-interface-list=LAN/ip firewall natadd action=masquerade chain=srcnat out-interface-list=WANI did the config but still the mikrotik is not doing the handshaking. I can use the same wireguard configuration in other devices connected to the same network where the mikrotik gets the ip from and i can connect to the wireguard server successfully. here is the config:# 2025-01-10 18:52:59 by RouterOS 7.16.2# software id = U13N-3S1V## model = RB952Ui-5ac2nD# serial number =/interface bridgeadd name=bridge1/interface wirelessset [ find default-name=wlan1 ] ssid=MikroTikset [ find default-name=wlan2 ] disabled=no mode=ap-bridge ssid=MikroTik/interface wireguardadd listen-port=51820 mtu=1420 name=wg1/interface listadd name=WANadd name=LAN/interface wireless security-profilesset [ find default=yes ] supplicant-identity=MikroTik/ip pooladd name=bridge-pool ranges=192.168.88.2-192.168.88.254/ip dhcp-serveradd address-pool=bridge-pool interface=bridge1 name=bridge-server/interface bridge portadd bridge=bridge1 interface=ether2add bridge=bridge1 interface=ether3add bridge=bridge1 interface=wlan2add bridge=bridge1 interface=wlan1/ip neighbor discovery-settingsset discover-interface-list=LAN/interface list memberadd interface=ether1 list=WANadd interface=bridge1 list=LANadd interface=wg1 list=WAN/interface wireguard peersadd allowed-address=0.0.0.0/0 endpoint-address=66.179.XX.XX endpoint-port=\51820 interface=wg1 name="VPN 66" persistent-keepalive=25s preshared-key=\"+FRlZLci8s37J6Hv2kS3IfeTpAp6AJVX6o//287zc8w=" private-key=\"aPulCKJTSxqdIZltXWROU9xQjPj7uErfbuqKhyTZHXc=" public-key=\"iA1OmT/fKNfLeQyh5OrK04/qyfQBtW0wLpcRvJLi22w="/ip addressadd address=10.8.0.2/24 interface=wg1 network=10.8.0.0add address=192.168.88.1/24 interface=bridge1 network=192.168.88.0/ip dhcp-clientadd interface=ether1/ip dhcp-server networkadd address=192.168.88.0/24 dns-server=192.168.88.1 gateway=192.168.88.1/ip dnsset allow-remote-requests=yes servers=1.1.1.1/ip firewall natadd action=masquerade chain=srcnat out-interface-list=WAN/system clockset time-zone-name=/system noteset show-at-login=no ---

## Response 13
The server info is not showing on the circled part as it should when the handshaking is successful but is still not showing anything ---
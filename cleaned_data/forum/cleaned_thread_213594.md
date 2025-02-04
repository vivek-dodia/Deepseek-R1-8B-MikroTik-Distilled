# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 213594

# Discussion

## Initial Question
Author: [SOLVED]Tue Dec 31, 2024 1:09 pm
``` /certificate import isrgrootx1.pem import r10.pem import r11.pem ``` ``` /ip ipsec profile add name=TheSafety_VPN /ip ipsec proposal add name=TheSafety_VPN pfs-group=none ``` ``` /ip ipsec policy group add name=TheSafety_VPN /ip ipsec policy add dst-address=0.0.0.0/0 group=TheSafety_VPN proposal=TheSafety_VPN src-address=0.0.0.0/0 template=yes ``` ``` /ip ipsec mode-config add name=TheSafety_VPN responder=no ``` ``` /ip ipsec peer add address=lou.msfcsi.com exchange-mode=ike2 name=TheSafety_VPN profile=TheSafety_VPN /ip ipsec identity add auth-method=eap certificate="" eap-methods=eap-mschapv2 generate-policy=port-strict mode-config=TheSafety_VPN peer=TheSafety_VPN policy-template-group=TheSafety_VPN username=myvpn password=myvpn ``` ``` /ip firewall address-list add address=a.b.c.0/24 list=thr_VPN /ip ipsec mode-config set [ find name=TheSafety_VPN ] src-address-list=thr_VPN ``` Ok, for starters you would have to download ISRG ROOT X1 and R10 and R11 as .pem, add them to the router's files ajd import them
```
After that, you would create an IPsec profile and proposal:
```

```
Next, you would configure a policy group and a policy template for the traffic to be sent over the tunnel:
```

```
Following, you add a mode configuration which would be later set to forward the desired traffic through the VPN:
```

```
Further, you would add a peer and an identity - the most important parts; because in peer you add the address/DNS of the server you connect to and in identity the username and password:
```

```
Lastly, after all this is done, you would need to consider traffic from which subnets should be sent over the tunnel by adding them in a firewall address list and adding the list itself in the mode-config settings:
```

```
FYI, the structure of my answer is based on the following article from the MikroTik Docs where there are more detailed explanations but for another VPN vendor:https://help.mikrotik.com/docs/spaces/R ... d+RouterOS


---
```

## Response 1
Author: Wed Jan 01, 2025 12:55 pm
thanks for the answerTheCat12, first I focused on installing Phase 1 and turned on logging, so i saw that i need to enable sha256, for that created a new profile:/ip ipsec profile add enc-algorithm=aes-256, aes-128, 3des hash-algorithm=sha256 name=profile1after that i imported R10 and R11 certificates, and Phase 1 was successfully installed, I think my mistake at this stage was related to the fact that I did not specify eap-methods=eap-mschapv2 and excessive selection of certificatesafter 5-10 seconds Phase 1 is canceled because no policy was created, but then I created the necessary settings and everything workednow everything works, but I see that on the local computer that gets access to the Internet through this tunnel, it takes a very long time to open pages, although I see that ping and nslookip are working fine. perhaps I still need to check the local network settings.yes, that's MTU, added/ip firewall mangle add chain=forward connection-mark=mark1 action=change-mss new-mss=1380 protocol=tcp tcp-flags=syn passthrough=yesand it worked. thanks again for the help!
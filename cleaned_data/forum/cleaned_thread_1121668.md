# Thread Information
Title: Thread-1121668
Section: RouterOS
Thread ID: 1121668

# Discussion

## Initial Question
I have a mikrotik VPN with IPSEC set up.Almost everything works fine, the computers on both networks have communication.However, when pinging from the mikrotik terminal on network 1 to the computers on network 2, the ping does not go out through the tunnel, but rather through the WAN.But I repeat, the computers on network 1 can ping the computers on network 2.Any suggestions on how to force it to go out through the tunnel?It's not L2TP, so there's no interface I could define in ip/routes. ---

## Response 1
you should wait for someone with the magic crystal ball ---

## Response 2
To translate @baragoon's comment - you have not provided enough information for any serious analysis.The following information is necessary:an export of configuration of both devices - whereas an export does not contain any passwords and passphhrases, there is still a lot of information you may not want to publish - like usernames to external services, e-mail addresses, public/global IP addresses, MAC addresses, or serial numbers of the devices. So you need to manually obfuscate this information, but when obfuscating public and global addresses, you have to do that using a text editor where you replace first three bytes of the public addresses and the first three words of the global addresses by some strings likepublic.subnet.1in all the files you are going to post, so that the relationship between individual addresses and gateways would remain visible across all the configurations.the particular ping that takes the wrong path (from what address you ping, to what address you ping). ---

## Response 3
1. You can check in IP/Firewall/Connections what src-addr is used for that ping packets and try to figure out why that particular one is used (lowest/highest/which interface etc) ?2. Try to use /ping x.x.x.x src-address=anyassignedtoyourinterfacesaddress to check which address let you get behind the tunnel and figure out what to do to "persuade" router to use the proper one. ---
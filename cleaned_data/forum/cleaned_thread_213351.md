# Thread Information
Title: Thread-213351
Section: RouterOS
Thread ID: 213351

# Discussion

## Initial Question
hi every onei had a problem in ipsec ikev2 identity, i try to have diffrent identity with diffrent remtoe id, but mikrotik only check the first one.0 peer=ike2 auth-method=pre-shared-key mode-config=ike2-conf remote-id=fqdn:ssecret="4000" generate-policy=port-strictpolicy-template-group=ike2-policies1 peer=ike2 auth-method=pre-shared-key mode-config=ike2-conf remote-id=fqdn:tsecret="4000" generate-policy=port-strictpolicy-template-group=ike2-policies ---

## Response 1
Normally this works, you can use multiple remote peers that only differ in their ID and Mikrotik sorts that out just fine. So what exactly means that "mikrotik only checks the first one" - that the second one (t) never authenticates or that both (s as well as t) end up using the same identity row (s) and thus they interfere with each other?Do both s and t peers use the same operating system and IPsec client or they are different? That may affect what they send as their own ID (initiator ID) and as the ID they expect your Mikrotik to "listen" at (Responder ID); Mikrotik first finds thepeerrow based on local and remote IP address and exchange mode, and then searches through all theidentityrows linked to thatpeerrow, matching on bothmy-idandremote-id. ---

## Response 2
Normally this works, you can use multiple remote peers that only differ in their ID and Mikrotik sorts that out just fine. So what exactly means that "mikrotik only checks the first one" - that the second one (t) never authenticates or that both (s as well as t) end up using the same identity row (s) and thus they interfere with each other?Do both s and t peers use the same operating system and IPsec client or they are different? That may affect what they send as their own ID (initiator ID) and as the ID they expect your Mikrotik to "listen" at (Responder ID); Mikrotik first finds thepeerrow based on local and remote IP address and exchange mode, and then searches through all theidentityrows linked to thatpeerrow, matching on bothmy-idandremote-id.hi dear sindy, tnx for your replay, the "s" authenticates is ok from andriod 14 native vpn using ikev2/ipsec psk , which s is the ipsec identifier.but the "t" with the all same config on same device, is not authenticates and the log say :identity not found for server:x.x.x.x peer: FQDN: t ---

## Response 3
So you take the Android 14 device currently configured as "s", you only change the "s" to a "t" on it, and that is enough to make it fail to authenticate? Or it's actually two distinct (but identical) phones you believe to differ only in the "s" and "t"? ---

## Response 4
YesFirst time i can connect on my Android device with ipsec identifier "s" and then i just change "s" to "t" and it failed.Another test i have done is that for i then just change "s" to "u" on server , and again the connection connect with "u"So i think just the first identifier checked by mikrotik. ---

## Response 5
OK, so if there is no difference between s and k except the name itself on the phone side, there must be some difference between theidentityrows on the Mikrotik side, unless it's (e.g.)s.sfor "s" butttt(no dot inside) for "t" - the matcher used to be quite sensitive to the formal side of things, so if the "fqdn" does not contain at least one dot and/or it contains any other symbols except letters, digits, minuses, and dots, it is considered invalid (not an FQDN) and therefore it is not used for the lookup. ---

## Response 6
No, I'm sure there is no typo.i try the id with number and still as the same.Do you think is there any reason that may the mikrotik not check the second identity?For example in peer configuration? Or in mode config? ---

## Response 7
The search in the identity table is done using the criteria I've listed above, so there is no reason why one row should be ignored.mode-configis an "output parameter" of anidentityrow, not a match one.What does/ip ipsec identity export hide-sensitiveshow? What ROS version are you running? ---

## Response 8
# 2024-12-18 21:09:53 by RouterOS 7.16.2# software id = DJFU-81JT## model = RB951Ui-2HnD# serial number = HCR082NJN3Y/ip ipsec identityadd generate-policy=port-strict mode-config=ike2-conf peer=\ike2 policy-template-group=ike2-policies remote-id=\fqdn:sadd generate-policy=port-strict mode-config=ike2-conf peer=\ike2 policy-template-group=ike2-policies remote-id=\fqdn:t ---

## Response 9
Can you replace the identities bys.siandt.trand try again? I am actually surprised that the first one is found. ---

## Response 10
yes , i try that but still as the same, can you login to my mikrotik and check what is the problem?I can send the login info to your email address? ---

## Response 11
Before eventually taking such extreme measures, enable logging using/system logging add topics=ipsec,!packetif you haven't done that yet, then run/log print follow-only file=working where topics~"ipsec", and let the Android connect with the working settings. Then Ctrl-C the/log print ..., downloadworking.txtfrom the router, delete it there to free the space, run/log print follow-only file=failing where topics~"ipsec", and let the Android try to connect with the wrong settings. After some 5 seconds, Ctrl-C the/log print ..., and download the other file. If reading those files gives you no hint, you can use the information inthis postto send me your contact info if you'd rather send me those files privately than obfuscate them and post them here (the IP addresses are encoded in the hex bytes shown so it is a bit more complicated to obfuscate than when the addresses only appear in the human friendly notation).I have just tested the same setup on the responder side -fqdn:sandfqdn:tdo work as expected if another Mikrotik acting as an initiator identifies itself using these identities. Each row of theidentitylist on the responder side refers to a differentmode-configrow with a differentaddressand everything works as expected, the initiator gets the correct address depending on whatmy-idI set on its onlyidentityrow./ip ipsec identityadd generate-policy=port-strict mode-config=s peer=t-chr-2 remote-id=fqdn:sadd generate-policy=port-strict mode-config=t peer=t-chr-2 remote-id=fqdn:tSo it looks as if the Android was behaving different in some regard - mine is 12 so I have to use an app for IKEv2 that does not support pre-shared key authentication, hence testing on it would not be relevant. It also seems that Mikrotik does not care about the formal correctness of the FQDN IDs any more. ---

## Response 12
hi agian...sorry i was very busyi config a test server and this is a full export of configed server:# 2024-12-21 09:17:47 by RouterOS 7.12.1# software id =#/interface wireless security-profilesset [ find default=yes ] supplicant-identity=MikroTik/ip ipsec policy groupadd name=ike2-policies/ip ipsec profileadd dh-group=modp2048 enc-algorithm=aes-256, 3des hash-algorithm=sha256 name=\ike2/ip ipsec peeradd exchange-mode=ike2 local-address=x.x.x.x name=ike2 passive=yes \profile=ike2/ip ipsec proposaladd auth-algorithms=sha256, sha1 name=ike2 pfs-group=modp2048/ip pooladd name=ike2-pool ranges=192.168.77.2-192.168.77.254/ip ipsec mode-configadd address-pool=ike2-pool address-prefix-length=32 name=ike2-conf/portset 0 name=serial0/ip dhcp-clientadd interface=ether1/ip ipsec identityadd generate-policy=port-override mode-config=ike2-conf peer=ike2 \policy-template-group=ike2-policies remote-id=fqdn:sadd generate-policy=port-override mode-config=ike2-conf peer=ike2 \policy-template-group=ike2-policies remote-id=fqdn:t/ip ipsec policyadd dst-address=192.168.77.0/24 group=ike2-policies proposal=ike2 src-address=\0.0.0.0/0 template=yes/ip serviceset telnet disabled=yesset ftp disabled=yesset www disabled=yesset ssh disabled=yesset api disabled=yesset api-ssl disabled=yes/system noteset show-at-login=noso can you test this config file on your server?and my e-mail address is my id in this forum @ gmailtnx ---
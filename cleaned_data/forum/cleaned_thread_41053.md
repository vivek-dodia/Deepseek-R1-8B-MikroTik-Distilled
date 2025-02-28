# Thread Information
Title: Thread-41053
Section: RouterOS
Thread ID: 41053

# Discussion

## Initial Question
Hallo, I try to replace our linux-based Servers with Mikrotik-Routers in an Docsis-Cable Environment. The provisioning with DHCP/TFTP/TOD is not really a problem and works great.But we use intensively DHCP-Remote-ID (Option-82), to pass the Bundle "CPE-IP and correspondend Cablemodem-MAC" to an external authentication system. The Cisco CMTS works as a DHCP-Relay and passes this information via Option-82 to the Mikrotik-Router, which act as a dhcp-server. My goal is to write a script which parse the entries in "/ip dhcp-server lease print detail" and submit the information in "address and agent-remote-id" via syslog to this authentication system. Here you can see the problem:/ip dhcp-server lease print detailaddress=x.x.x.30 mac-address=00:23:8B:34:66:20 server=cpe-dhcp status=bound expires-after=8m57s last-seen=1m3s active-address=x.x.x.30 active-mac-address=00:23:8B:34:66:20 active-server=cpe-dhcp host-name="emsinb" src-mac-address=00:15:C6:4F:54:00 agent-circuit-id="\00\01\00\03" agent-remote-id="\00\15/\95\B"As you can see is the agent-remote-id field binary and not the mac-address of the cable-modem. This means I cannot take this information in this format for scripting.If I debug the DHCP-Communication I can see this:21:20:30 dhcp, debug, packet dhcp-cmts: cpe-dhcp sending ack with id 2961227336 to x.x.x.121:20:30 dhcp, debug, packet dhcp-cmts: ciaddr = 0.0.0.021:20:30 dhcp, debug, packet dhcp-cmts: yiaddr = x.x.x.3021:20:30 dhcp, debug, packet dhcp-cmts: siaddr = x.x.x.x21:20:30 dhcp, debug, packet dhcp-cmts: giaddr = x.x.x.x21:20:30 dhcp, debug, packet dhcp-cmts: chaddr = 00:23:8B:34:66:2021:20:30 dhcp, debug, packet dhcp-cmts: Msg-Type = ack21:20:30 dhcp, debug, packet dhcp-cmts: Server-Id = x.x.x.x21:20:30 dhcp, debug, packet dhcp-cmts: Address-Time = 60021:20:30 dhcp, debug, packet dhcp-cmts: Subnet-Mask = 255.255.255.021:20:30 dhcp, debug, packet dhcp-cmts: Router = x.x.x.x21:20:30 dhcp, debug, packet dhcp-cmts: Domain-Server = x.x.x.x21:20:30 dhcp, debug, packet dhcp-cmts: Relay-Agent-Info = 01-04-00-01-00-03-02-06-00-15-2F-95-5C-42Here you can see the Relay-Agent-Info. This contains the correct Cablemodem-MAC (last six hex values = 00:15:2F:95:5C:42).It would be great If i could access this Information in "/ip dhcp-server lease print detail" either as a new raw field "Relay-Agent-Info" or correctly separated in circuit-id and remote-id. There it would be easy accessible by the scripting engine.Other solution would be to parse the debug log via scripting and send the correspondend bundle "yiaddr and Relay-Agent-Info" via syslog to our external authentication system. How could this be done? We handle several hundreds simultaneous leases on each Mikrotik. If I run the DHCP on debug this would create large Log-Files on Mikrotik, probably the entries get mixed together? I would pay for a proper script handle this problem.thanksOliver ---

## Response 1
actually, 
```
id="\00\15/\95\B"is 'correct' MAC address00:15:2F:95:5C:42\00\15 are non-printable characters. then \2F, but it's ASCII "/". then \95, and \42 is "B" letterand now - "\5C"! it's ASCII "\", but it should be at least double escaped! it's definitely a BUG! full export should be at least id="\00\15/\95\\B"who will write to support? =)

---
```

## Response 2
last week write 3 messages to support, but still get no answers )) ---

## Response 3
about that problem? =) ---

## Response 4
I did already contact support about this problem. Janis will try to release the changes in v4.8:Janis:We will make it so that our software will detect if the value is in binary ortext format and show them accordingly, atm it is shown as text all the timeand as soon as there are non-printable symbols it is a mess.This is a change we intend to make - is it ok with you?Regards, Janis Megisoliver ---

## Response 5
well, for now it does not mess (maybe a bit), for now the only real problem is with \5c symbol - if you have it, you cannot decode the value correctly. the rest values are parseable ---

## Response 6
actually, 
```
id="\00\15/\95\B"is 'correct' MAC address00:15:2F:95:5C:42\00\15 are non-printable characters. then \2F, but it's ASCII "/". then \95, and \42 is "B" letterand now - "\5C"! it's ASCII "\", but it should be at least double escaped! it's definitely a BUG! full export should be at least id="\00\15/\95\\B"who will write to support? =)But why does get "\95" not replaced with "_" which is a printable character, if I follow the ASCII-Table? From my understanding it takes the binary delivered Sub-Option Remote-ID from Relay-Agent-Info, but treats it as Text-ASCII-Code. If it gets displayed it just converts the valid ASCII-Codes to the correspondend Character. But the valid characters are apparently not all of the printable Characters defined in the ASCII-Table. It would be better if this mix does not even occur. All of this makes it tricky to convert, even without "5c". What do you think?thanksOliver

---
```

## Response 7
\95 is hexadecimal value, decimal is 149, and it's non-printableyes, it would be nice to select between bin and text form for the whole value, not per character. but if there's no '5C', there's nothing tricky even in current output ---

## Response 8
\95 is hexadecimal value, decimal is 149, and it's non-printableyes, it would be nice to select between bin and text form for the whole value, not per character. but if there's no '5C', there's nothing tricky even in current outputA quick and dirty script does the job even with '5c':
```
#!/usr/bin/php<?phpif(!isset($argv[1])){echo"Usage: argv1 = Option-82 in /ip dhcp-server lease print from mikrotik, pass argv1 in ''\n";exit(1);}$remoteid=addslashes($argv[1]);for($i=0;$i<=31;$i++){$hex=strtoupper(dechex($i));if(strlen($hex)<2)$hex="0".$hex;$np[]="\\".$hex;$npr[]=chr($i);}for($i=127;$i<=255;$i++){$hex=strtoupper(dechex($i));$np[]="\\".$hex;$npr[]=chr($i);}$mac=stripslashes(str_replace($np,$npr,$remoteid));for($i=0;$i<strlen($mac);$i++){$sstring=substr($mac,$i,1);$hexstring[]=dechex(ord($sstring));if(strlen($hexstring[$i])<2)$hexstring[$i]="0".$hexstring[$i];}echo implode(":",$hexstring);?>Please no comments about bad coding stylethis was just for testing. I also cannot say that this works with all CM-Macs, but all we tested got correctly converted.Now we discovered a further problem, here is my mail to janis about this:Dear Janis,ok, we tried scripting the Option-82 within Mikrotik. We discovered following additional issue. If I do a "/ip dhcp-server lease print detail" I get following (as already described):address=192.168.51.9 mac-address=00:1D:09:5B:8D:2F server=cpe-dhcp status=bound expires-after=1m3s last-seen=8m57s active-address=192.168.51.9 active-mac-address=00:1D:09:5B:8D:2F active-server=cpe-dhcp host-name="test" src-mac-address=00:15:C6:4F:54:00 agent-circuit-id="\00\01\00\03" agent-remote-id="\00\15/\95\B"If I want to use this value in scripting (to save it in a variable for further processing) I have to get it with following command::local cmMac:set cmMac [/ip dhcp-server lease get [find where address=192.168.51.9] agent-remote-id]it produces following result:[admin@gw-es-01] /system script> :put $cmMac/\B[admin@gw-es-01] /system script>As you see this is not the value from the print output, it just shows the printable characters. No chance to get the mac from this. Is this gonna be fixed as well?thanksOliverIs there any way getting the result from "print" into a variable?thanksOliver

---
```

## Response 9
issue is solved in v4.8. works perfectly for us.thanks to mikrotik for this great support ...oliver ---

## Response 10
Would you tale more about your system with mikrotik?Does the RouterOS handle dhcp requests both clients and modems? Is the leases static for modems or dynamic via radius?ThX ---

## Response 11
Would you tale more about your system with mikrotik?Does the RouterOS handle dhcp requests both clients and modems? Is the leases static for modems or dynamic via radius?ThXRouterOS handles dhcp for cm and cpe in our case. We do run several types of CMTS (Cisco, Arris, Motorola). In Cisco IOS you should make sure that you activate "cable dhcp-giaddr policy" on the cable interface. With this RouterOS is able to choose the right network for cm and cpe, for instance:[admin@xx-xx-xx] > /ip dhcp-server printFlags: X - disabled, I - invalid# NAME INTERFACE RELAY ADDRESS-POOL LEASE-TIME ADD-ARP0 cpe-dhcp ether4 192.168.x.x cpe 10m yes1 cm-dhcp ether4 10.0.x.x cm 1h yesWe authenticate cpes on a different layer. We use a static lease for cm, but it's easy to adopt it to radius. Additionally you can push everything via Mikrotik-API.It's a bit of work, but you can substitute your linux provisioning machines with mikrotik. that was our goal.oliver ---

## Response 12
RouterOS handles dhcp for cm and cpe in our case. We do run several types of CMTS (Cisco, Arris, Motorola). In Cisco IOS you should make sure that you activate "cable dhcp-giaddr policy" on the cable interface. With this RouterOS is able to choose the right network for cm and cpe, for instance:[admin@xx-xx-xx] > /ip dhcp-server printFlags: X - disabled, I - invalid# NAME INTERFACE RELAY ADDRESS-POOL LEASE-TIME ADD-ARP0 cpe-dhcp ether4 192.168.x.x cpe 10m yes1 cm-dhcp ether4 10.0.x.x cm 1h yesWe authenticate cpes on a different layer. We use a static lease for cm, but it's easy to adopt it to radius. Additionally you can push everything via Mikrotik-API.It's a bit of work, but you can substitute your linux provisioning machines with mikrotik. that was our goal.oliverSorry for off-topic.. How can you create two dhcp-server on same interface in RouterOS? If I try, OS says "Couldn't add New DHCP Server - server with such interface and relay is already enabled" ---

## Response 13
RouterOS handles dhcp for cm and cpe in our case. We do run several types of CMTS (Cisco, Arris, Motorola). In Cisco IOS you should make sure that you activate "cable dhcp-giaddr policy" on the cable interface. With this RouterOS is able to choose the right network for cm and cpe, for instance:[admin@xx-xx-xx] > /ip dhcp-server printFlags: X - disabled, I - invalid# NAME INTERFACE RELAY ADDRESS-POOL LEASE-TIME ADD-ARP0 cpe-dhcp ether4 192.168.x.x cpe 10m yes1 cm-dhcp ether4 10.0.x.x cm 1h yesWe authenticate cpes on a different layer. We use a static lease for cm, but it's easy to adopt it to radius. Additionally you can push everything via Mikrotik-API.It's a bit of work, but you can substitute your linux provisioning machines with mikrotik. that was our goal.oliverSorry for off-topic.. How can you create two dhcp-server on same interface in RouterOS? If I try, OS says "Couldn't add New DHCP Server - server with such interface and relay is already enabled"update to newest version and use a different relay as I used in my example. Otherwise RouterOS cannot select from which pool it has to serve the request ...works at least for me without any complain of routeros ...oliver ---

## Response 14
Thanks for info. Would you send me your email or other contact for further questions?kozmai ---

## Response 15
Thanks for info. Would you send me your email or other contact for further questions?kozmaiunfortunately I'm not permitted to write private messages in the forum. Please write an E-Mail to following address:mikrotik.3.emsi@neverbox.com. I'll reply with my correct mail then.thanksoliver ---

## Response 16
by the way, if you add karma, that man receives PM with your comment ---

## Response 17
I did already contact support about this problem. Janis will try to release the changes in v4.8:Janis:We will make it so that our software will detect if the value is in binary ortext format and show them accordingly, atm it is shown as text all the timeand as soon as there are non-printable symbols it is a mess.This is a change we intend to make - is it ok with you?Regards, Janis MegisoliverHi emsi, how do you capture that mac in option 82 on the mikrotik side? I've been trying to do it for a while using option matcher but I can't do it.Thanks ---
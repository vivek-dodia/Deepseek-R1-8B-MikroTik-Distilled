# Thread Information
Title: Thread-1116206
Section: RouterOS
Thread ID: 1116206

# Discussion

## Initial Question
Hello mikrotik fans, I will be bringing up a btest server soon. I have preprared one RB800 and a 1Gbit connection dedicated only for the sake of testing.It is ready, but I want to limit the usage somehow before I post it public. I have created filter rule for input that puts your IP in ban address list for X period of time.I can't figure out how to limit the test sessions per time. You can basically let it run indefinately. Can you tell me how to disconnect every btest connection for example on 5min? ---

## Response 1
Nice work!You can check out the configuration of TomjNorthIdaho posted here:viewtopic.php?f=2&t=104266&p=690150#p690150/ip firewall rawadd action=accept chain=prerouting comment="testers accepted" src-address-list=testeradd action=drop chain=prerouting comment="previous testers drop" src-address-list=previousadd action=add-src-to-address-list address-list=tester address-list-timeout=2m chain=prerouting comment="add to tester" dst-port=2000-2100 protocol=tcpadd action=add-src-to-address-list address-list=tester address-list-timeout=2m chain=prerouting comment="add to tester" dst-port=2000-2100 protocol=udpadd action=add-src-to-address-list address-list=previous address-list-timeout=15m chain=prerouting comment="add to previous" dst-port=2000-2100 log=yes protocol=tcpadd action=add-src-to-address-list address-list=previous address-list-timeout=15m chain=prerouting comment="add to previous" dst-port=2000-2100 log=yes protocol=udpThis will limit tests to 2m every 15m per ip address. ---

## Response 2
It's almost like Mikrotik should run one ---

## Response 3
I did check his config and set it up nicely. Everything works except when the timer runs out for "testing" address list it wouldnt drop the traffic server>client only the other way. This issue appears only when testing UDP. With TCP test there is no problem. I worked on this for about 6 hours last night and I couldnt find a solution. Anyone else experenced this iisue?Should I provide any screenshots? ---

## Response 4
Have you enabled fasttrack? I will probably bypass raw firewall, however doesn't explain why tcp is working.Please do no post screenshots, just export config (/export hide-sensitive) and paste in code blocks.Also.. TomjNorthIdaho mentioned more than a terabyte of traffic per month hosting public bandwidth server.Are you sure your connection can handle such large amount of traffic? ---

## Response 5
I have enabled fasttrack, but it doesn't count packets so I guess i doesn't apply for this.I will post config as soon as I can.The mikrotik will be in a datacenter for the clients to test their bandwith and also for public use. So yes the network behind it will handle alot ---

## Response 6
It's almost like Mikrotik should run onePlease forward the bandwidth test link for Cisco, Juniper, Huawei, Zyxel, TP-Link, .... ---

## Response 7
Hello again.It seems I fixed it and it's now working as expected. RAW rules needed tweaking. I will post before and after output so you can compare:Before:[user@Server] /ip firewall> raw printFlags: X - disabled, I - invalid, D - dynamic0 D ;;; special dummy rule to show fasttrack counterschain=prerouting action=passthrough1 ;;; testers acceptedchain=prerouting action=accept log=no log-prefix="" src-address-list=tester2 ;;; previous testers dropchain=prerouting action=drop log=no log-prefix="" src-address-list=previous3 ;;; add to testerchain=prerouting action=add-src-to-address-list dst-port=2000-3000 log=no log-prefix="" protocol=tcp address-list=tester address-list-timeout=15m4 ;;; add to testerchain=prerouting action=add-src-to-address-list dst-port=2000-3000 log=no log-prefix="" protocol=udp address-list=tester address-list-timeout=15m5 ;;; add to previouschain=prerouting action=add-src-to-address-list dst-port=2000-3000 log=yes log-prefix="" protocol=tcp address-list=previous address-list-timeout=1d6 ;;; add to previouschain=prerouting action=add-src-to-address-list dst-port=2000-3000 log=yes log-prefix="" protocol=udp address-list=previous address-list-timeout=1dAfter:[user@Server] /ip firewall> raw printFlags: X - disabled, I - invalid, D - dynamic0 D ;;; special dummy rule to show fasttrack counterschain=prerouting action=passthrough1 ;;; testers acceptedchain=prerouting action=accept log=no log-prefix="" src-address-list=tester2 ;;; testers acceptedchain=output action=accept log=no log-prefix="" dst-address-list=tester3 ;;; previous testers dropchain=output action=drop log=no log-prefix="" dst-address-list=previous4 ;;; previous testers dropchain=prerouting action=drop log=no log-prefix="" src-address-list=previous5 ;;; add to testerchain=prerouting action=add-src-to-address-list dst-port=2000-3000 log=no log-prefix="" protocol=tcp address-list=tester address-list-timeout=15m6 ;;; add to testerchain=prerouting action=add-src-to-address-list dst-port=2000-3000 log=no log-prefix="" protocol=udp address-list=tester address-list-timeout=15m7 ;;; add to previouschain=prerouting action=add-src-to-address-list dst-port=2000-3000 log=no log-prefix="" protocol=tcp address-list=previous address-list-timeout=1d8 ;;; add to previouschain=prerouting action=add-src-to-address-list dst-port=2000-3000 log=no log-prefix="" protocol=udp address-list=previous address-list-timeout=1d ---

## Response 8
You can test the server at:IP: 87.121.0.45U: neterraP: neterra15min. testing time and 24h ban (this was their request).Please share results when you test. Cheers ---

## Response 9
IP: 87.121.0.45it says "can't connect" for UDP and "test unsupported" for TCP.Are you certain it works fine? ---

## Response 10
Works fine here:RB3011 @ 500Mbps
```
[admin@MikroTik]>/tool bandwidth-test87.121.0.45user=neterra password=neterra direction=both
                status:running
              duration:57stx-current:543.9Mbpstx-10-second-average:543.6Mbpstx-total-average:456.1Mbpsrx-current:543.6Mbpsrx-10-second-average:543.5Mbpsrx-total-average:406.0Mbpslost-packets:4653random-data:nodirection:both
               tx-size:1500rx-size:1500Cannot post 1Gbps result in upcoming 24 hours

---
```

## Response 11
Thanks nescafe2002 for testing. It's interesting how much CPU will be consumed on full bandwidth. Today max was 660mbps and the cpu was around 30%. Tell me from which IP you are testing so I can remove you from ban list for another try ---

## Response 12
Reset to default configuration & got a fresh ipRB4011 @ 1Gbps
```
[admin@MikroTik]>/tool bandwidth-test87.121.0.45user=neterra password=neterra direction=both;;;results can be limitedbycpu,note that traffic generation/termination performance mightnotbe representativeofforwarding performance
                status:running
              duration:59stx-current:696.0Mbpstx-10-second-average:693.7Mbpstx-total-average:685.8Mbpsrx-current:965.2Mbpsrx-10-second-average:972.7Mbpsrx-total-average:963.8Mbpslost-packets:4774random-data:nodirection:both
               tx-size:1500rx-size:1500connection-count:20local-cpu-load:42%remote-cpu-load:100%

---
```

## Response 13
Seems fine for me ---

## Response 14
Nice btest serverI just ran some btest's from my 207.32.194.24 btest server to your new btest server.FYI: UDP is pretty much immune to distance (because it is mostly a fire-and-forget protocol) , and TCP can be sensitive to distance because TCP requires return ACK packets.Here are the results: ---

## Response 15
Nice btest serverI just ran some btest's from my 207.32.194.24 btest server to your new btest server.FYI: UDP is pretty much immune to distance (because it is mostly a fire-and-forget protocol) , and TCP can be sensitive to distance because TCP requires return ACK packets.Here are the results:Great 10x for the testHope it is used a lotDo you think the RB800 will come weak if pushed? I can see it doesn't go higher than 70% cpu when being used for tests with 900mbps. ---

## Response 16
is this server still working?im getting "connecting...."code used:/tool bandwidth-test 87.121.0.45 user=neterra password=neterra direction=both ---

## Response 17
Nice btest serverI just ran some btest's from my 207.32.194.24 btest server to your new btest server.FYI: UDP is pretty much immune to distance (because it is mostly a fire-and-forget protocol) , and TCP can be sensitive to distance because TCP requires return ACK packets.Here are the results:Great 10x for the testHope it is used a lotDo you think the RB800 will come weak if pushed? I can see it doesn't go higher than 70% cpu when being used for tests with 900mbps.RB-800 - don't know --- guess you can just wait and see …North Idaho Tom Jones ---

## Response 18
is this server still working?im getting "connecting...."code used:/tool bandwidth-test 87.121.0.45 user=neterra password=neterra direction=bothNow it is. Try again ---

## Response 19
is the server running on stable or long term ?, lately you can test only if you have the same version of the packages ---

## Response 20
Just tried yor btest and am getting:/tool bandwidth-test 87.121.0.45 user=neterra password=neterra direction=bothstatus: can not connectduration: 0setc.I your btest server also demanding a latest version of ROS?If so it makes it somewhat unusable for me and many I know. ---

## Response 21
Just tried yor btest and am getting:/tool bandwidth-test 87.121.0.45 user=neterra password=neterra direction=bothstatus: can not connectduration: 0setc.I your btest server also demanding a latest version of ROS?If so it makes it somewhat unusable for me and many I know.6.43.8 works for me to this btest server-and-6.43.12 works for me to this btest server-and-6.44 works for me to this btest server ---

## Response 22
6.43.8 works for me to this btest server-and-6.43.12 works for me to this btest server-and-6.44 works for me to this btest serverI am running many routers with pre 6.40 and those I have tried don't connect.The problem is with an arbitrary change of authentication method courtesy of Mikrotik.It would not be a problem if there was no user/pass rquired.Given one has to come here to get the IP, and the user/pass is in clear text, and there is overuse mitigation in place, I can't see the point of requiring a user/pass, especially when it excludes many Mikrotik devices in the field.But that's just me (and many I know). ---

## Response 23
6.43.8 works for me to this btest server-and-6.43.12 works for me to this btest server-and-6.44 works for me to this btest serverI am running many routers with pre 6.40 and those I have tried don't connect.The problem is with an arbitrary change of authentication method courtesy of Mikrotik.It would not be a problem if there was no user/pass rquired.Given one has to come here to get the IP, and the user/pass is in clear text, and there is overuse mitigation in place, I can't see the point of requiring a user/pass, especially when it excludes many Mikrotik devices in the field.But that's just me (and many I know).Re:The problem is with an arbitrary change of authentication method courtesy of Mikrotik.repre 6.40I'm not up to speed with ROS version and authentication changes. What part of authentication does not work properly after an upgrade ? ---

## Response 24
Re:The problem is with an arbitrary change of authentication method courtesy of Mikrotik.repre 6.40I'm not up to speed with ROS version and authentication changes. What part of authentication does not work properly after an upgrade ?Take a look at:viewtopic.php?f=2&t=104266&p=686117&hil ... ty#p686117 ---

## Response 25
Is it still active ? i am getting stuck at 'connecting..'Ping works ---

## Response 26
Is it still active ? i am getting stuck at 'connecting..'Ping worksYes - my 207.32.194.24 public access btest server is on-line and working correctly.- Check the version of your Mikrotik , you may need to upgrade it- The user name is --> btest- The password is --> btest ---

## Response 27
Yes I was able to test with 207.32.194.24. I was asking about 87.121.0.45 ---

## Response 28
Yes, it's working. ---

## Response 29
Thanks a lot!!! ---

## Response 30
For some reason I still get stuck at status: connecting.. Maybe a configuration problem on my side ?Same with 207.32.194.24 and both time out on ping although I havent tried a test in the last 24hThis is my firewall config (newbie alert)/ip firewall filteradd action=accept chain=input comment="defconf: accept established, related, untracked" connection-state=established, related, untrackedadd action=drop chain=input comment="defconf: drop invalid" connection-state=invalidadd action=accept chain=input comment="defconf: accept ICMP" protocol=icmpadd action=drop chain=input comment="defconf: drop all not coming from LAN" in-interface-list=!LANadd action=accept chain=forward comment="defconf: accept in ipsec policy" ipsec-policy=in, ipsecadd action=accept chain=forward comment="defconf: accept out ipsec policy" ipsec-policy=out, ipsecadd action=fasttrack-connection chain=forward comment="defconf: fasttrack" connection-state=established, relatedadd action=accept chain=forward comment="defconf: accept established, related, untracked" connection-state=established, related, untrackedadd action=drop chain=forward comment="defconf: drop invalid" connection-state=invalidadd action=drop chain=forward comment="defconf: drop all from WAN not DSTNATed" connection-nat-state=!dstnat connection-state=new in-interface-list=WANadd action=drop chain=input comment="defconf: drop WAN DNS UDP req" dst-port=53 in-interface=ether1 protocol=udpadd action=drop chain=input comment="defconf: drop WAN DNS TCP req" dst-port=53 in-interface=ether1 protocol=tcp ---

## Response 31
For some reason I still get stuck at status: connecting.. Maybe a configuration problem on my side ?ROS version? ---

## Response 32
it's the latest, 6.44.2, RB750Gr3 ---

## Response 33
it's the latest, 6.44.2, RB750Gr3Then that's not the reason ---

## Response 34
HI, First of all, thanks for your testing server, is great-full having some trusty point to scope when making bandwidth and link stability tests.I am not being able to connect to it, It could be another reason i am not being able to connect to it?Model: RB433ROS: 6.40.8Alexis. ---

## Response 35
Thanks, works very well. RB3011 v644.2 ---

## Response 36
You can test the server at:IP: 87.121.0.45U: neterraP: neterraSpecial thanks to Neterra Telecommunications for sponsoring and providing the hardware and the connectivity for this btest server.15min. testing time and 24h ban (this was their request).Please share results when you test. Cheerstransmitting and receiving 800mbThanks, it worked like a charm. Have a nice day sir ! ---

## Response 37
Seems to not work for me, goes into running state, but then nothing happensNterra Test.JPG ---

## Response 38
just tested, everything works fine
```
> /tool bandwidth-test 87.121.0.45 user=neterra password=neterra direction=both;;; results can be limited by cpu, note that trafficgeneration/termination performance might not berepresentative of forwarding performancestatus: runningduration: 2m57stx-current: 601.2Mbpstx-10-second-average: 605.1Mbpstx-total-average: 603.1Mbpsrx-current: 602.5Mbpsrx-10-second-average: 604.7Mbpsrx-total-average: 607.2Mbpslost-packets: 5416random-data: nodirection: bothtx-size: 1500rx-size: 1500connection-count: 20local-cpu-load: 57%remote-cpu-load: 100%p.s remote CPU load 100% is that ok? you mentioned before that it doesn't get higher than 70%

---
```

## Response 39
Working!!!Got 500-ish out of my 500Mbps cable linkThanks! ---

## Response 40
Authentication failed for me. ---

## Response 41
Hi There, Just wondering if this is still up and running ? I'm interested to see how I can adjust my bandwidth and be able to test what's happening both on my router and behind it.Would be great to be able to test against your server if it's still available.Thanks !! ---

## Response 42
Hi There, Just wondering if this is still up and running ? I'm interested to see how I can adjust my bandwidth and be able to test what's happening both on my router and behind it.Would be great to be able to test against your server if it's still available.Thanks !!The public access btest server I operate is still operational.IPv4 address: 207.32.194.24IPv6 address: 2605:4e40:0:1fe::user: btestpassword: btest ---

## Response 43
Unfortunately i can not make it work..i've entered your given IP address but... my MT is always 'connecting'.korgScreen Shot 2019-12-09 at 12.23.55.png ---

## Response 44
Unfortunately i can not make it work..i've entered your given IP address but... my MT is always 'connecting'.korgScreen Shot 2019-12-09 at 12.23.55.pngTwo questions:1 ) What is your public IP address ? I will check my logs to see if for some reason your IP has been blocked.2 ) Is your Mikrotik a firewall or behind a firewall ? I've seen customer firewall configurations which can prevent return TCP and/or UDP packets from a btest.North Idaho Tom Jones ---

## Response 45
Hi...1. i have dynamic IP address... so i really dont know which IP I had at that time... i will try it and then send you my current IP.. maybe that will help2. Neither nor. its a simple LTE connection and in the fw its just input allow and deny upon the connection status and for the forward as well ---

## Response 46
Hi...1. i have dynamic IP address... so i really dont know which IP I had at that time... i will try it and then send you my current IP.. maybe that will help2. Neither nor. its a simple LTE connection and in the fw its just input allow and deny upon the connection status and for the forward as wellwww.whatismyipaddress.com ---

## Response 47
So, now at 17.11 i have tested my speed through your test server and it worked.txkorg ---

## Response 48
So, now at 17.11 i have tested my speed through your test server and it worked.txkorgYou tested on my server ?If so , then greatNorth Idaho Tom Jones ---

## Response 49
```
/tool bandwidth-test87.121.0.45user=neterra password=neterra direction=both;;;results can be limitedbycpu,note that traffic generation/termination performance mightnotbe 
                        representativeofforwarding performance
                status:running
              duration:1m30stx-current:30.9Mbpstx-10-second-average:31.3Mbpstx-total-average:30.3Mbpsrx-current:273.5Mbpsrx-10-second-average:268.5Mbpsrx-total-average:271.8Mbpslost-packets:3272random-data:nodirection:both
               tx-size:1500rx-size:1500connection-count:20local-cpu-load:100%remote-cpu-load:20%tested with 6.46.1Thanks Martooo!

---
```

## Response 50
I have been trying both 27.121.0.45 u=neterra p=neterra as well as 207.32.194.24 u=btest p=btest but neither work. 207.32.194.24 "can't connect" and 27.121.0.45 is stuck at "connecting" before eventually disconnecting. Any other servers I can test to? ---

## Response 51
I have been trying both 27.121.0.45 u=neterra p=neterra as well as 207.32.194.24 u=btest p=btest but neither work. 207.32.194.24 "can't connect" and 27.121.0.45 is stuck at "connecting" before eventually disconnecting. Any other servers I can test to?Are you behind a firewall ?Is your Mikrotik also a firewall ?A Mikrotik btest needs to be able to make and receive btest connections. If you are using or going through a firewall - or - your Internet provider has you going through a firewall, then a btest might now work.North Idaho Tom Jones ---

## Response 52
I have been trying both 27.121.0.45 u=neterra p=neterra as well as 207.32.194.24 u=btest p=btest but neither work. 207.32.194.24 "can't connect" and 27.121.0.45 is stuck at "connecting" before eventually disconnecting. Any other servers I can test to?Are you behind a firewall ?Is your Mikrotik also a firewall ?A Mikrotik btest needs to be able to make and receive btest connections. If you are using or going through a firewall - or - your Internet provider has you going through a firewall, then a btest might now work.North Idaho Tom JonesHave you tested? ---

## Response 53
hi there i try the 87.121.0.45 with TCP and it starts running and disconects in the same moment, when i try UDP it starts running but with no data at all... the same with the 207.32.194.24 it just says: cant connect both udp and TCP... i tried with the newest stable and with the newest long term ---

## Response 54
hi there i try the 87.121.0.45 with TCP and it starts running and disconects in the same moment, when i try UDP it starts running but with no data at all... the same with the 207.32.194.24 it just says: cant connect both udp and TCP... i tried with the newest stable and with the newest long termHello, It seems that Tom has to temporarily power-off the public access btest server, because the increased bandwidth usage due to Coronavirus issue."I promise to return the btest server back on-line just as soon as my network stabilizes and the bandwidth is once again available", in his own words.Greetings from Spain ---

## Response 55
You can test the server at:IP: 87.121.0.45U: neterraP: neterraSpecial thanks to Neterra Telecommunications for sponsoring and providing the hardware and the connectivity for this btest server.15min. testing time and 24h ban (this was their request).Please share results when you test. Cheerssometimes i can test, but sometimes i cant, what happend? ---

## Response 56
You can test the server at:IP: 87.121.0.45U: neterraP: neterraSpecial thanks to Neterra Telecommunications for sponsoring and providing the hardware and the connectivity for this btest server.15min. testing time and 24h ban (this was their request).Please share results when you test. CheersAwesome! It tested with tx/rx 500/750 Mbps total average on a 1000/1000 line.WHY, won't Mikrotik host servers I wonder? ---

## Response 57
Here is my results (Ukrainian IPto87.121.0.45):
```
/tool bandwidth-test address=87.121.0.45user="neterra"password="neterra"duration=20sstatus: done testingduration: 21srx-current: 91.8Mbpsrx-10-second-average: 94.3Mbpsrx-total-average: 93.9Mbpslost-packets: 858random-data: nodirection: receiverx-size: 1500connection-count: 20local-cpu-load: 54%remote-cpu-load: 9%
```

```
/tool bandwidth-test address=87.121.0.45user="neterra"password="neterra"duration=20srandom-data=yesstatus: done testingduration: 21srx-current: 95.0Mbpsrx-10-second-average: 94.6Mbpsrx-total-average: 94.4Mbpslost-packets: 705random-data: yesdirection: receiverx-size: 1500connection-count: 20local-cpu-load: 58%remote-cpu-load: 25%

---
```

## Response 58
You can test the server at:IP: 87.121.0.45U: neterraP: neterraSpecial thanks to Neterra Telecommunications for sponsoring and providing the hardware and the connectivity for this btest server.15min. testing time and 24h ban (this was their request).Please share results when you test. CheersTx cur: 324.7 Mbps avg: 325.7 Mbps max: 355.4 MbpsRx cur: 414.5 Mbps avg: 410.3 Mbps max: 434.5 Mbps ---

## Response 59
```
>/tool bandwidth-test protocol=tcp \
   direction=receive address=87.121.0.45\
   user="neterra"password="neterra"\
   duration=20sstatus: done testingduration: 21srx-current: 221.2Mbpsrx-10-second-average: 293.5Mbpsrx-total-average: 259.2Mbpsrandom-data: nodirection:receiveconnection-count: 20local-cpu-load: 32%
```

```
>/tool bandwidth-test protocol=tcp \
   direction=transmit address=87.121.0.45\
   user="neterra"password="neterra"\
   duration=20sstatus: done testingduration: 20srx-current: 236.3Mbpsrx-10-second-average: 247.4Mbpsrx-total-average: 210.5Mbpsrandom-data: nodirection:transmitconnection-count: 20local-cpu-load: 31%remote-cpu-load: 31%Direction:bothCapture1.JPG

---
```

## Response 60
Don't know why this one was under the radar for so longISP 500/30 (huge asymmetry, I know)/tool bandwidth-test protocol=tcp \\... direction=receive address=87.121.0.45 \\... user="neterra" password="neterra" \\... duration=20sstatus: done testingduration: 21srx-current: 477.1Mbpsrx-10-second-average: 476.2Mbpsrx-total-average: 465.9Mbpsrandom-data: nodirection: receiveconnection-count: 20local-cpu-load: 30%> /tool bandwidth-test protocol=tcp \\... direction=transmit address=87.121.0.45 \\... user="neterra" password="neterra" \\... duration=20sstatus: done testingduration: 21stx-current: 28.5Mbpstx-10-second-average: 28.5Mbpstx-total-average: 28.5Mbpsrandom-data: nodirection: transmitconnection-count: 20local-cpu-load: 5%remote-cpu-load: 12% ---

## Response 61
bandwidth test_24.12.24.png ---
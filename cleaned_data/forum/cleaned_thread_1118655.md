# Thread Information
Title: Thread-1118655
Section: RouterOS
Thread ID: 1118655

# Discussion

## Initial Question
Hello everyone, I recently purchased a MikroTik CCR2004 and set up my network with the following specifications:ISP Connection: 1 Gbps down / 700 Mbps up (providing IPv4 through IPv6 tunneling with Free FAI in France).Issue Description:I am experiencing very slow download speeds when trying to clone a Git repository or download large files over HTTP. The download speed caps at around 100 KB/s, while the router's CPU usage remains around 0%.Interestingly, while running speedtest from various devices, I consistently receive results over 500 Mbps. But the download of file during this same test is still cap ... (Download from the browser or from wget doesn't change anything still 100 KB/s and from any machine linux or macOS)Additional Observations:Enabling a VPN (such as ProtonVPN) boosts the download speed to over 30 MB/s. Which sound crazy to me.Disabling all firewall rules, including fasttrack, does not change the slow download behavior.When using iperf3, I achieve good results, but using the -R option also caps speeds at about 100 KB/s.Streaming 4K videos on YouTube works seamlessly, with no buffering, even while two 4K Netflix streams are active.Testing Environment:I've tested downloads from multiple devices connected to the network.Within my VLAN setup, iperf tests between VLANs show that traffic saturates the Ethernet link without issues, with low CPU usage on the router.Configuration:I will include my MikroTik configuration in the attachments for reference.Questions:Does anyone have suggestions on what could be causing this issue?Are there specific settings or configurations I should check to resolve the slow download speeds without the VPN?I have concerned maybe about my MTU configuration but this part is a bit obscur to me.Thank you for your help! ---

## Response 1
Most likely this is MTU related, as you mention IPv4-in-IPv6.I have similar setup at home and had to set MTU to 1460, probably you will also need to clamp MSS to MTU.You can check your actual MTU here:http://speedguide.net:8080/Optionally, you can test if this is the case with iperf3 by reducing MSS size using option "-M 1420". ---

## Response 2
Here the result from speedguide
```
«SpeedGuide.net TCPAnalyzerResults»Testedon:2024.11.2113:41IP address:xx.xx.xxx.xxClientOS/browser:MacOS(Firefox132.0)TCP optionsstring:020405b4010303060101080a89a5c79c0000000004020000MSS:1460MTU:1500TCPWindow:131712(notmultipleofMSS)RWINScaling:6bits(2^6=64)UnscaledRWIN:2058RecommendedRWINs:64240,128480,256960,513920,1027840BDP limit(200ms):527Mbps(53Megabytes/s)BDP limit(500ms):211Mbps(21Megabytes/s)MTUDiscovery:OFF 
TTL:54Timestamps:ONSACKs:ON 
IPToS:00000000(0)I tried what you proposed something like that `iperf3 -R -M 1420 -c 185.93.2.193` but it fail with `iperf3: error - unable to set TCP/SCTP MSS: Invalid argument`.In terms of MTU if I'm not wrong in the order- sfp port ACTUAL MTU 1700 L2 MTU 1796- vlan836 ACTUAL MTU 1700 L2 MTU 1792- ipipv6 ACTUAL MTU 1500 L2 MTU 65535- bridge1 ACTUAL MTU 1500 L2 MTU 1596Where do you propose to change the MTU?

---
```

## Response 3
Interesting... according to speedguide you have normal MTU - but this is strange as tunneling IPv4 in IPv6 (without tricks on the way) will definitely make it lower.As to iperf3 - not sure why it fails, did you run it on Linux (or other *ix like) or Windows? It could be also version-dependent.As to changing MTU on an interface - set it to something relatively low (~ 1400) on the interface that has your default gateway for IPv4. If it works, then you could increase it a bit to find the maximum that works.If you are under Linux (which is behind your Mikrotik), you could adjust the MTU for the default route only - like "ip ro re default via <your-default-gw> mtu 1400", instead of changing the interface MTU on the router itself.Another potential issue is that your router or provider blocks ICMP's unreachable messages - under normal circumstances there is no need to fiddle with MTU as it will be auto-discovered, but some providers block such ICMPs, or they are blocked/dropped by your router. ---

## Response 4
just for testing, disable hardware offload in /interface bridge Port for a moment and redo the tests. ---

## Response 5
I disabled all hardware offloading, but unfortunately, it did not resolve the issue.Regarding my testing with iperf, I found that when run on Linux, it performed well, in contrast to my earlier tests on macOS. Without the -R option, I achieved 500 Mbps, but using -R resulted in a drop to just 2 Mbps so it's same as before.Moreover, I conducted further iperf tests using the -P 20 option, which allowed for 20 streams, each conveying 2 Mbps. Does this information assist in troubleshooting?Interestingly, when I connect through a VPN, the slow download issue disappears entirely. I suspect this might be related to my use of WireGuard, which operates over UDP, whereas the issue appears to be isolated to RX TCP traffic. Could this be an indication of a potential MTU issue, if so do you mind explaining why?EDIT: After some reading on MTU I understand know that the issue is indeed at the MTU level since it works over UDP and by extension with WireGuard. Now I don't know where to adjust the MTU properly ---

## Response 6
Small update, I might have wrongly tested the first time but I don't have the issue over IPv6, if you have any other idea I would be happy to hear. ---

## Response 7
If IPv6 is not affected, then it explains why your tests with YouTube and Netflix are doing well, because they would use IPv6. Same with many speedtest.net test servers nowadays. And it looks like the problem only affects IPv4 TCP traffic.When you perform the iperf3 test with -R (the test that produced only 100KB/s), can you check on thesenderside (the remote side) whether aCwndcolumn is available? and which values does that column have? ---

## Response 8
Here the result what are you looking for?
```
Serveroutput:Acceptedconnectionfromxx.xx.xx.xx,port48694[5]local185.93.2.193port5201connected to xx.xx.xx.xx port48704[ID]IntervalTransferBitrateRetrCwnd[5]0.00-1.00sec439KBytes3.59Mbits/sec116127KBytes[5]1.00-2.00sec510KBytes4.17Mbits/sec364147KBytes[5]2.00-3.00sec607KBytes4.97Mbits/sec13655.1KBytes[5]3.00-4.00sec669KBytes5.48Mbits/sec486301KBytes[5]4.00-5.00sec287KBytes2.35Mbits/sec277206KBytes[5]5.00-6.00sec250KBytes2.05Mbits/sec26752.3KBytes[5]6.00-7.00sec486KBytes3.98Mbits/sec33369.3KBytes[5]7.00-8.00sec1.51MBytes12.6Mbits/sec711228KBytes[5]8.00-9.00sec525KBytes4.29Mbits/sec62056.6KBytes[5]9.00-10.00sec356KBytes2.92Mbits/sec2473.5KBytes[5]10.00-11.00sec831KBytes6.81Mbits/sec017.0KBytes[5]11.00-12.00sec831KBytes6.81Mbits/sec017.0KBytes[5]12.00-13.00sec891KBytes7.30Mbits/sec014.1KBytes[5]13.00-14.00sec831KBytes6.81Mbits/sec017.0KBytes[5]14.00-15.00sec1.08MBytes9.09Mbits/sec4691.9KBytes[5]15.00-16.00sec337KBytes2.76Mbits/sec16567.9KBytes[5]16.00-17.00sec653KBytes5.35Mbits/sec017.0KBytes[5]17.00-18.00sec1.16MBytes9.73Mbits/sec017.0KBytes[5]18.00-19.00sec810KBytes6.64Mbits/sec8141.0KBytes[5]19.00-20.00sec387KBytes3.17Mbits/sec31562.2KBytes[5]20.00-21.00sec665KBytes5.44Mbits/sec39390.5KBytes[5]21.00-22.00sec708KBytes5.80Mbits/sec48789.1KBytes[5]22.00-23.00sec3.02MBytes25.4Mbits/sec181463.6KBytes[5]23.00-24.00sec204KBytes1.67Mbits/sec507189KBytes[5]24.00-25.00sec154KBytes1.26Mbits/sec17521.2KBytes[5]25.00-26.00sec245KBytes2.00Mbits/sec23582.0KBytes[5]26.00-27.00sec672KBytes5.50Mbits/sec20533.9KBytes[5]27.00-28.00sec831KBytes6.81Mbits/sec019.8KBytes[5]28.00-29.00sec1.04MBytes8.75Mbits/sec53115KBytes[5]29.00-30.00sec632KBytes5.18Mbits/sec22759.4KBytes[5]30.00-31.00sec577KBytes4.73Mbits/sec10673.5KBytes[5]31.00-32.00sec950KBytes7.78Mbits/sec017.0KBytes[5]32.00-33.00sec1.04MBytes8.76Mbits/sec017.0KBytes[5]33.00-34.00sec1.04MBytes8.76Mbits/sec019.8KBytes[5]34.00-35.00sec1.04MBytes8.76Mbits/sec017.0KBytes[5]35.00-36.00sec1.10MBytes9.24Mbits/sec017.0KBytes[5]36.00-37.00sec1.16MBytes9.73Mbits/sec017.0KBytes[5]37.00-38.00sec1.10MBytes9.24Mbits/sec017.0KBytes[5]38.00-39.00sec1.10MBytes9.25Mbits/sec4645.2KBytes[5]39.00-40.00sec679KBytes5.56Mbits/sec210153KBytes[5]40.00-41.00sec560KBytes4.59Mbits/sec35291.9KBytes[5]41.00-42.00sec298KBytes2.45Mbits/sec2753.7KBytes[5]42.00-43.00sec772KBytes6.32Mbits/sec028.3KBytes[5]43.00-44.00sec2.03MBytes17.0Mbits/sec022.6KBytes[5]44.00-45.00sec1.97MBytes16.5Mbits/sec025.5KBytes[5]45.00-46.00sec1.29MBytes10.8Mbits/sec117167KBytes[5]46.00-47.00sec597KBytes4.89Mbits/sec263113KBytes[5]47.00-48.00sec950KBytes7.78Mbits/sec0110KBytes[5]48.00-49.00sec823KBytes6.74Mbits/sec076.4KBytes[5]49.00-50.00sec847KBytes6.94Mbits/sec17862.2KBytes[5]50.00-51.00sec416KBytes3.41Mbits/sec4987.7KBytes[5]51.00-52.00sec1.22MBytes10.2Mbits/sec025.5KBytes[5]52.00-53.00sec2.09MBytes17.5Mbits/sec039.6KBytes[5]53.00-54.00sec1.05MBytes8.83Mbits/sec221188KBytes[5]54.00-55.00sec247KBytes2.03Mbits/sec2078.48KBytes[5]55.00-56.00sec697KBytes5.72Mbits/sec214277KBytes[5]56.00-57.00sec116KBytes949Kbits/sec20036.8KBytes[5]57.00-58.00sec238KBytes1.95Mbits/sec633.9KBytes[5]58.00-59.00sec297KBytes2.43Mbits/sec017.0KBytes[5]59.00-60.00sec831KBytes6.81Mbits/sec017.0KBytes[5]60.00-60.04sec59.4KBytes12.4Mbits/sec017.0KBytes-------------------------[ID]IntervalTransferBitrateRetr[5]0.00-60.04sec48.3MBytes6.74Mbits/sec10233senderFYI on linux you can get the server output withiperf3 -R --get-server-output -c 185.93.2.193

---
```

## Response 9
Yes, thank you. The congestion window (for the sender side, on your side this is further limited by the receive window) is way too small. And has no chances to increase before encountering a lot of retries (probably due to packet loss). It looks like the round-trip delay from you to the iperf3 server is about 18-20ms. When there are retries the sender side had to reduce the congestion window (cf congestion avoidance algorithms), as you can observe. It looks like retries are needed when the Cwnd is larger than 30KB.If you use a bandwidth delay product calculator, like this onehttps://calculator.academy/bandwidth-de ... alculator/or this onehttps://www.speedguide.net/bdp.php, you'll see that if the congestion window can't get bigger than those numbers, you won't get higher bandwidth. That's also why if you make 20 connections with -P 20, the sum of the bandwidth is larger, because it looks like the Cwnd limit is about the same for the individual connections. For comparison, here is a test from my place to the server of yours. I'm located in a different continent with a much higher ping time (193ms), and the congestion window can steadily increase to 8.74 Mbytes without retries:iperf3-cwnd.pngMy bet is that when you remove the -R option, the sender side (you) can achieve much much larger Cwnd sizes. When you perform iperf3 tests between your VLANs, do you see large or small Cwnd values? Because the delay within your LANs is much smaller (sub ms) you might not notice the effects of a limited congestion window on the final bandwidth. ---

## Response 10
Here the result without `-R`
```
root@docker:~#iperf3--get-server-output-c185.93.2.193-t10Connectingto host185.93.2.193,port5201[5]local192.168.43.251port43242connected to185.93.2.193port5201[ID]IntervalTransferBitrateRetrCwnd[5]0.00-1.00sec58.4MBytes490Mbits/sec95216KBytes[5]1.00-2.00sec71.4MBytes599Mbits/sec19304KBytes[5]2.00-3.00sec73.0MBytes612Mbits/sec22297KBytes[5]3.00-4.00sec78.0MBytes654Mbits/sec4293KBytes[5]4.00-5.00sec73.6MBytes617Mbits/sec12206KBytes[5]5.00-6.00sec64.6MBytes542Mbits/sec46270KBytes[5]6.00-7.00sec76.7MBytes644Mbits/sec3262KBytes[5]7.00-8.00sec75.6MBytes634Mbits/sec12260KBytes[5]8.00-9.00sec64.8MBytes543Mbits/sec6204KBytes[5]9.00-10.00sec72.4MBytes607Mbits/sec1307KBytes-------------------------[ID]IntervalTransferBitrateRetr[5]0.00-10.00sec708MBytes594Mbits/sec220sender[5]0.00-10.04sec707MBytes591Mbits/sec                  receiverThe ping to this server is good.
```

```
root@docker:~#ping185.93.2.193PING185.93.2.193(185.93.2.193)56(84)bytesofdata.64bytesfrom185.93.2.193:icmp_seq=1ttl=58time=3.18ms64bytesfrom185.93.2.193:icmp_seq=2ttl=58time=3.44ms64bytesfrom185.93.2.193:icmp_seq=3ttl=58time=3.07ms64bytesfrom185.93.2.193:icmp_seq=4ttl=58time=2.60ms64bytesfrom185.93.2.193:icmp_seq=5ttl=58time=2.68ms---185.93.2.193ping statistics---5packets transmitted,5received,0%packet loss,time4006msrtt min/avg/max/mdev=2.602/2.993/3.442/0.315msLocally between two desktop not on the same VLAN I have no Retr and Cwnd is bigger and I saturate the GB link
```

```
root@docker:~#iperf3--get-server-output-c192.168.11.3-t10Connectingto host192.168.11.3,port5201[5]local192.168.43.251port40466connected to192.168.11.3port5201[ID]IntervalTransferBitrateRetrCwnd[5]0.00-1.00sec113MBytes950Mbits/sec0362KBytes[5]1.00-2.00sec112MBytes938Mbits/sec0362KBytes[5]2.00-3.00sec112MBytes938Mbits/sec0362KBytes[5]3.00-4.00sec112MBytes938Mbits/sec0362KBytes[5]4.00-5.00sec112MBytes938Mbits/sec0362KBytes[5]5.00-6.00sec112MBytes939Mbits/sec0362KBytes[5]6.00-7.00sec112MBytes939Mbits/sec0362KBytes[5]7.00-8.00sec112MBytes938Mbits/sec0362KBytes[5]8.00-9.00sec112MBytes939Mbits/sec0362KBytes[5]9.00-10.00sec111MBytes933Mbits/sec0362KBytes-------------------------[ID]IntervalTransferBitrateRetr[5]0.00-10.00sec1.09GBytes939Mbits/sec0sender[5]0.00-10.00sec1.09GBytes938Mbits/sec                  receiverand with `-R`
```

```
Acceptedconnectionfrom192.168.43.251,port54910[5]local192.168.11.3port5201connected to192.168.43.251port54926[ID]IntervalTransferBitrateRetrCwnd[5]0.00-1.00sec113MBytes951Mbits/sec0452KBytes[5]1.00-2.00sec111MBytes930Mbits/sec0452KBytes[5]2.00-3.00sec110MBytes926Mbits/sec0519KBytes[5]3.00-4.00sec111MBytes933Mbits/sec0542KBytes[5]4.00-5.00sec112MBytes937Mbits/sec0663KBytes[5]5.00-6.00sec111MBytes933Mbits/sec2619KBytes[5]6.00-7.00sec110MBytes923Mbits/sec3491KBytes[5]7.00-8.00sec111MBytes933Mbits/sec4489KBytes[5]8.00-9.00sec111MBytes933Mbits/sec0509KBytes[5]9.00-10.00sec110MBytes923Mbits/sec0580KBytes-------------------------[ID]IntervalTransferBitrateRetr[5]0.00-10.00sec1.09GBytes932Mbits/sec9sender

---
```

## Response 11
Problem with using public servers (including iperf3 servers) is that there might be bottlenecks other than "last mile". I tried iperf3 server from the screenshots of @CGGXANNX and I got shitty performance in both directions. In both directions I see fair amount of retransmissions ... and for TCP retransmissions are sure way to kill any kind of performance (retransmission both means re-sending data and it shrinks TCP window to portion of what it could be, so throughput in next few seconds is low even without retransmissions). If I tried a few other public iperf3 servers, I was getting various results (but all of them were better and more consistent than the ones I got from server from mentioned screenshot.So when determining performance of router, it's important to be 200% sure that there are no other bottlenecks. ---

## Response 12
I agree with you, Mkx, but I ended up doing this test with iperf because I had very slow internet speed over IPv4, such as when pulling from GitHub. The issue disappeared the moment I used a VPN, even in the same location (city).Also, I tested the same iperf server with the equipment provided by my internet service provider instead of the CCR, and I got good results with no retries. The issue is that I don't want to keep this equipment because it's very old, and I have my own gear. ---

## Response 13
I have the same problem on CCR2216 with L3 HW offloading enabled or disabled. I have even gone so far as to connect the web server directly to the CCR2216 and download of a file is 200Kbps whereas previously it was downloading at my full link speed at home which is 400Mbps.Multi-stream HTTP downloads such as speedtest.net gives full line speed. Streaming absolutely perfect even on 4/8K.I am suspecting that something in the recent OS releases has a bug. Im on 7.16.1 ---

## Response 14
Thanks for sharing I was becoming crazy ... Did you try to downgrade?On my side I did dump the packets between the ONU and my ISP hardware and compared it to the ONU and CCR connection.While using my ISP HW the packets are clearly identify as ipipv6 tunnel where coming from CCR it's only ipv6 packets and I see some TCP RST.I plan to try something that should not impact anything is to put my SFP in a bridge and do the VLAN 836 using VLAN filtering instead of L3 VLAN. I don't have any hope on this part... ---

## Response 15
I just checked I'm on 7.15.1, Upgraded to 7.16.1 and I have the same issue. Still present in 7.17rc2 too ---

## Response 16
Did you only get the issue when you went from 7.15 yo 7.16 ? ---

## Response 17
No I also had the issue in 7.15 and I've just tested the 7.17rc2 still the same. ---

## Response 18
I also have the same issue, only my ipv4 download is very slow 100kb/s maximum ---

## Response 19
Tu as quelle freebox ?configurée en routeur ou pas ?Si routeur, as tu mis en œuvre la délégation des prefix ipv6? ---

## Response 20
Tu as quelle freebox ?configurée en routeur ou pas ?Si routeur, as tu mis en œuvre la délégation des prefix ipv6?J’ai viré la Freebox je suis directement branché sur L’ONU avec le Mikrotik et j’ai bien une connectivité ipv6 le problème est juste présent en download IPv4 ---

## Response 21
I've opened a support ticket. Their answer is that the issue is on the configuration and that they can't help... Any chance on your side Webtelza? ---

## Response 22
Kaxapo any update on your side? ---

## Response 23
Kaxapo any update on your side?Nope, i tried changing dns servers, disabling firewall, change mtu on almost every related interface, turn off tcp timestamps, i just can’t get my IPv4 Speed to go over 4mb/s and my upload is 500mb/s.I dont know anymore where to search :/ ---

## Response 24
Kaxapo any update on your side?Nope, i tried changing dns servers, disabling firewall, change mtu on almost every related interface, turn off tcp timestamps, i just can’t get my IPv4 Speed to go over 4mb/s and my upload is 500mb/s.I dont know anymore where to search :/ ---

## Response 25
The only solution I have is to use wireguard and redirect all the traffic to it. It works because it uses UDP so no more issues. But I would like to have a better solution for the sake of stability... ---

## Response 26
The only solution I have is to use wireguard and redirect all the traffic to it. It works because it uses UDP so no more issues. But I would like to have a better solution for the sake of stability...J’aimerais discuter avec toi par whatsapp pour en savoir plus sur ta config wireguard, je t’avais envoyé mon whatsapp par message privé sur le forum LaFibre.Si tu veut bien m’envoyer un de tes contacts par mail merci:alexis99@live.com.pt ---
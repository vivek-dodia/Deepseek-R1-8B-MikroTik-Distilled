# Thread Information
Title: Thread-1114611
Section: RouterOS
Thread ID: 1114611

# Discussion

## Initial Question
Hello everyone, I see that this solution was never clear for many so I went ahead and outlined a very simple three steps to getting remote packet captures with ROS done quick.This post is meant to be a quick practical guide to help you capture traffic quickly for whatever your reasons may be. It can be a huge help with debugging network issues.Step 1. Configure the packet sniffer tool on ROS to your target machine's IP address. You can change the port, just remember to set it in step 3.mikrotik-wireshark-remote-capture-1.pngStep 2. In Wireshark, you should have an option for "UDP Listener remote capture", click the settings gear to configure the capture optionsIf you don't have this option then your problem is beyond this post and you need to reinstall Wireshark with udpdump.mikrotik-wireshark-remote-capture-2.pngStep 3. Set the port to what you have set in ROS from step 1. If you changed the port from 37008, enter the new port number here.I've set "tzsp" as the payload type so that the output from my capture rules will decode natively and show up as traffic is sent from ROS to Wireshark.You will see traffic based on the rules of your capture in the ROS packet sniffer tool so remember to check your rules twice before starting the capture.mikrotik-wireshark-remote-capture-3.pngFinally, you've got packets! Now, go forth and make debugging network issues easier.If you have any issues or think I've missed something, please feel free to add to this thread.mikrotik-wireshark-remote-capture-4.pngNote: This post is accurate as ofROS 7.1.1, Wireshark Version 3.6.1(v3.6.1-0-ga0a473c7c1ba) andNpcap 1.60 ---

## Response 1
Also available in Mangle:Action - sniff-tzsp - send a packet to a remote TZSP compatible system (such as Wireshark). Set remote target with sniff-target and sniff-target-port parameters (Wireshark recommends port 37008)https://help.mikrotik.com/docs/display/ ... ngle-Stats ---

## Response 2
Also available in Mangle:I didn't even know about this! Thanks! ---

## Response 3
I usethis old experimentof mine, and I'm very satisfied with it. I like that I see only captured packets, there's no unnecessary trace of TZSP. ---

## Response 4
I usethis old experimentof mine, and I'm very satisfied with it. I like that I see only captured packets, there's no unnecessary trace of TZSP.very interesting i will give a try ---

## Response 5
Hi there, I'm playing around with Packet Sniffer and Wireshark but I don't see that much in the received packets.I used default settings so Wireshark simply listen to the LAN port that's it.My MTs and my Wireshark sit in different subnets so is the before mentioned settings are necessary to see the original captured packets? ---
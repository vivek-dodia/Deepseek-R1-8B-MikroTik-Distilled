# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210851

# Discussion

## Initial Question
Author: [SOLVED]Wed Sep 11, 2024 7:16 pm
Hello, I bought a hAP ax2 because i though i could turn it into a WISP router. I am quite disappointed because I don't understand the steps to configure it. Somehow I guess I have to configure my ISP wifi somehere. After searching information it seems that there is a driver issue with ax2 that prevents to configure this with QuickSetup ?See attached my wanted setup.Thanks in advance for any advice.image.png ---

## Response 1
Author: Thu Sep 12, 2024 5:18 pm
Replying to myself after getting support from Mikrotik.Remove wifi1 interface from the bridge (from Bridge / Ports screen)Add wifi1 to WAN interface list (from Interfaces / Interface List screen)Configure wifi1 as station (from Wireless / Wifi Wave 2 screen)Add DHCP client on wifi1 (from IP / DHCP Client screen)Set the ISP modem SSID, Channel band, Auth Type and passphrase (from Wireless / Wifi Wave2 > wifi 1 screen)Plug the PC on eth2 port : access to internet works fine. Yayy !! ---

## Response 2
Author: Thu Sep 12, 2024 5:51 pm
Hi, I'm very glad you solved the problem, but I and the forum would be so much happierif you also mark your case in this forum as solved.See the pictures below.Where you click on the following places on the thread that solved your problem.So the AI can take over and know what the problems are with the respective solution.At board style: CanvasAt board style: prosilver
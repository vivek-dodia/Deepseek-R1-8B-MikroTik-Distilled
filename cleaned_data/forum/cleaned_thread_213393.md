# Thread Information
Title: Thread-213393
Section: RouterOS
Thread ID: 213393

# Discussion

## Initial Question
NTP Synchronization Issue with HMI in a Router-Switch SetupHello everyone, I am facing an issue with NTP synchronization in a setup where an HMI screen is connected to a MikroTik router acting as a switch. Here's a detailed explanation of the problem:Setup:HMI Configuration:The HMI device has only one Ethernet port. It connects directly to the router via one of the LAN ports.The HMI is configured to synchronize its time using an NTP server, but the synchronization fails.Router Functionality:The MikroTik router is configured to act as a switch for the local network, bridging all LAN ports (ETH2-ETH5).The router also serves as the NTP server for the local devices, including the HMI.The WAN port (ETH1) connects to the broader network, providing internet access.Objective:The goal is for the router to act as the NTP server and synchronize the HMI's clock using the router's internal time or by relaying NTP synchronization from an external server.Problem:Despite being properly connected, the HMI is unable to synchronize with the NTP server (router). ---

## Response 1
does the HMI ask for time?add rule/ip fi ma add action=log chain=prerouting dst-port=123 protocol=udpsee logs when packages appear ---

## Response 2
does the HMI ask for time?add rule/ip fi ma add action=log chain=prerouting dst-port=123 protocol=udpsee logs when packages appearThe TP1200 screens (which are the HMI devices I mentioned) were synchronized and working fine for several weeks, but recently they got out of sync. The issue seems to have occurred after the initial period of proper synchronization. I will perform the steps you suggested tomorrow and check the logs to see if there are any NTP requests appearing. I will keep you updated on the findings ---

## Response 3
Verify on Mikrotik that NTP client is properly synchronized. Without that, NTP server won't allow further clients to synchronize to it. ROS NTP server doesn't use own RTC as time source (among other reasons because MT hardware doesn't have RTC). ---

## Response 4
Verify on Mikrotik that NTP client is properly synchronized. Without that, NTP server won't allow further clients to synchronize to it. ROS NTP server doesn't use own RTC as time source (among other reasons because MT hardware doesn't have RTC).I have the same problem, the NTP client comes out as 'started' not as 'synchronized', the client in my case is a PLC if synchronized with the router time but of course the time is out of date every time I turn off and on the router and that's why I said before that the client appears as 'started' instead of synchronized. ---

## Response 5
It could be that your ISP is blocking UDP traffic with dst port 123 towards your router. Have a look at this thread for a work around:viewtopic.php?t=208791 ---

## Response 6
I think you are confused......Either the item is a switch or a router MAKE UP YOUR MIND.If its a switch the only thing the device can do is point to the gateway of the trusted vlan to get NTP itself, the MT device.Getting Time to devices on vlans is the responsibility of the main router.Do you have the settings/config for the main router.Need config of both main router and switch ---
# Document Information
Title: Quick Set
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/328060/Quick+Set,

# Content
# 1.1Summary1.2Modes1.3HomeAP1.3.1Wireless1.3.2Internet1.3.3Local Network1.3.4VPN1.3.5System1.4FAQ
# Summary
Quicksetis a simple configuration wizard page that prepares your router in a few clicks. It is the first screen a user sees, when opening the default IP address 192.168.88.1 in a web browser.
Quickset is available for all devices that have some sort of default configuration from factory. Devices that do not have configuration must be configured by hand. The most popular and recommended mode is the HomeAP (or HomeAP dual, depending on the device). This Quickset mode provides the simplest of terminology and the most common options for the home user.
# Modes
Depending on the router model, different Quickset modes might be available from the Quickset dropdown menu:
# HomeAP
This is the mode you should use if you would like to quickly configure a home access point.
# Wireless
Set up your wireless network in this section:
# Internet
# Local Network
# VPN
If you want to access your local network (and your router) from the internet, use a secure VPN tunnel. This option gives you a domain name where to connect to, and enables PPTP and L2TP/IPsec (the second one is recommended). The username is 'vpn' and you can specify your own password. All you need to do is enable it here, and then provide the address, username and password in your laptop or phone, and when connected to the VPN, you will have a securely encrypted connection to your home network. Also, useful when travelling - you will be able to browse the internet through a secure line, as if connecting from your home. This also helps to avoid geographical restrictions that are set up in some countries.
# System
# FAQ
Q: How is Quickset different from the Webfig tab, where a bunch of new menus appear?
A: QuickSet is for new users who only need their device up and running in no time. It provides the most commonly used options in one place. If you need more options, do not use any Quickset settings at all, click on "Webfig" to open the advanced configuration interface. The full functionality is unlocked.
Q: Can I use Quickset and Webfig together? While settings that are not conflicting can be configured this way, it is not recommended to mix up these menus.
A: If you are going to use Quickset, use only Quickset and vice versa. What is difference between Router and Bridge mode? Bridge mode adds all interfaces to the bridge, allowing to forward Layer2 packets (acts as a hub/switch). In Router mode, packets are forwarded in Layer3 by using IP addresses and IP routes (acts as a router).
Q: In HomeAP mode, should the 2GHz and 5GHz network names be the same, or different?
A: If you prefer that all your client devices, like TV, phones, game consoles, would automatically select the best preferred network, set the names identically. If you would like to force a client device to use the faster 5GHz 802.11ac connection, set the names unique.
Q: Can I create an AP without security settings - no password or connect to such AP while using QuickSet?
A: QuickSet uses WPA2 pre-shared key by default. It means that the minimal password length is 8 symbols and the device can only connect to WPA2 secured AP or serve as AP itself. For configurations with no security settings, you need to configure them manually using WinBox, Webfig, or console.
QuickSet interface:
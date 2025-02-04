# Thread Information
Title: Thread-213465
Section: RouterOS
Thread ID: 213465

# Discussion

## Initial Question
I set up a NordVPN tunnel following the instructions.https://support.nordvpn.com/hc/en-us/ar ... th-NordVPNThe tunnel works. I routed the IP addresses of the TVs through the VPN. The IPTV, which was previously blocked, started working – that’s really cool. This means the tunnel is definitely working. However, I can’t access the app store or open YouTube on the TV. Why is this happening?When I route my computer’s IP address through the VPN, nothing opens – not even Google. But when I install the NordVPN app on my computer, everything works, and all websites open. When NordVPN is installed on the router itself, nothing works except IPTV, but the tunnel clearly works.I’ve looked into different ways to set up NordVPN on MikroTik and tried everything, but it always ends up the way I described. Can this be fixed? ---

## Response 1
Which DNS server is used for resolving? If is ROS router IP and it has ISP DNS IP set as upstream then probably ISP DNS is refusing connections outside its network. TV can be using some public one, like 8.8.8.8 on which can connect and resolve hosts for IPTV. Try withNordVPN DNS serversor some public if is DNS issue. ---

## Response 2
Hi, yes, the TV was configured with the router’s default DNS, 192.168.88.1. I replaced it with the public DNS 8.8.8.8, then tried several other public addresses, but it still doesn’t work. YouTube and LG Content Store still won’t open.Next, I tried adding public DNS addresses in the router settings under IP > DNS. There, I see Dynamic Servers 103.86.96.100. I added a couple of public DNS addresses of my own, but nothing changed. ---

## Response 3
Try adding an exception IPsec policy for local traffic from the router to the LAN devices as describedhere. Without this policy, PMTUD does not work so many TCP connections won't be able to deliver data unless you useaction=change-mssrules in mangle to manually adjust the MSS to match the actual MTU of the IPsec-encrypted packets. ---

## Response 4
Post your config for review/export file=anynameyouwish ( minus router serial number, any public WANIP information, keys etc.) ---
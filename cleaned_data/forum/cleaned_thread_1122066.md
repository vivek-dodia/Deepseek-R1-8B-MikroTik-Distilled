# Thread Information
Title: Thread-1122066
Section: RouterOS
Thread ID: 1122066

# Discussion

## Initial Question
I inherited a RouterBoard RBD53iG-5HacD2HnD configured as a DHCP server with an active hotspot. From what I understand, the captive portal is accessed via a VPN. The issue is that I now need to disable NAT because the RouterBoard will be directly connected to a Huawei L3 switch that handles routing, and NAT must be performed by my firewall. However, when I disable NAT masquerade, the VPN no longer establishes, and I can’t access the captive portal. On the Huawei switch side, the return route is correctly configured. Additionally, the gateway for the 172.29.0.0/16 subnet assigned to the LAN is handled by the RouterBoard, and my switch’s return route points to the WAN IP of the RouterBoard (10.10.3.1).I have networking knowledge, but I’m struggling to understand MikroTik. The system integrator managing the captive portal is unable to find a solution.Thank you for your help. ---

## Response 1
If something doesn't work after disabling NAT, it's a routing problem.You should know the IP address of the portal and check what traffic the VPN carries. To recognize this Use /tool/torch on the vpn interface when it is running... ---

## Response 2
Or better yet, export the config of the router and post it here since I'm expecting to see some firewall/NAT rules added to the hotspot chain system by the integrator that affect the VPN/export file=anynameyouwish(minus sensitive info like public IPs, serial number, passwords, etc.) ---
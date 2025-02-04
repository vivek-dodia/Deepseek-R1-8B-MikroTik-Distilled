# Thread Information
Title: Thread-213868
Section: RouterOS
Thread ID: 213868

# Discussion

## Initial Question
I'm working on a basic configuration that connects an Brocade ICX-6450 switch to a Mikrotik 5009 router.I'd like to have 3 VLANs on the Brocade. The Brocade connects to the Mikrotik via SFP+. The Mikrotik will have internet connected to it and also act as the DHCP server for the VLANs (if possible). The VLANs should have intervlan communication through the switch (to offload the router) and internet access through the Mikrotik.VLAN10: Ports 1-14VLAN20: Port 15VLAN30: Ports 16-24Uplink port: SFP+1To do this, my understanding is I need to do the following on the Brocade in router config:Add VLAN10: Untag ports 1-14. Tag SFP+1Add router-interface ve 10Add IP to router-inferface 10 --> 192.168.10.1/24Add VLAN20: Untag port 15. Tag SFP+1Add router-interface ve 20Add IP to router-inferface 20 --> 192.168.20.1/24Add VLAN30: Untag ports 16-24. Tag SFP+1Add router-interface ve 30Add IP to router-inferface 30 --> 192.168.30.1/24Add VLAN100: Untag SFP+1 <-----This is the transit VLANAdd router-interface ve 100Add IP to router-inferface 100 --> 172.16.1.1/24Setup default route on Brocade: ip default 172.16.1.2i'm confused about what I need to configure on the Mikrotik. Any guidance is much appreciated! ---

## Response 1
Your Brocade config indicates that Brocade will do the routing between VLANs. Are you sure about it? If yes, then you'll have to configure DHCP relay on Brocade. If not, then Brocade needs "router interface" only on management VLAN. ---
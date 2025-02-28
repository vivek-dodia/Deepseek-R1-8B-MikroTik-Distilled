# Thread Information
Title: Thread-1113636
Section: RouterOS
Thread ID: 1113636

# Discussion

## Initial Question
I'm trying to come up with the best way to hand out IP addresses in my WISP network.I've attached a diagram of part of my network, with a Radius server attached.Would something like this work, such that the client routers could obtain an IP address from the Radius server?John ---

## Response 1
If you configure each of these routers 10.1.1.254, 10.2.1.254 etc with some "helper" address (on the customer-facing side) to relay the broadcast-request they see coming in the client-side and deliver it in unicast to your DHCP you'll have no issue to map it to a correct pool I guess.So you are handing out 10.x.y.z IP's right ?? Then you have some centralized NAT taking place to public IP ? ---

## Response 2
Need to clarify a couple of pointsThe radius server simply authenticates it doesn't know or care if the IPs being used are public or private.If you are going to dish out private IP's then you will have a source nat or masquerade from that range to the WAN IP.The ip pool for the hand out can be in a mikrotik pool or in the radius server there are two ways to do it.You can also optionally have the mikrotik pool do the common ones and some fixed static ones be done by the radius.If the radius is setting the IP it will send a FRAMED-IP field in the radius response.So there is flexibility in the ip handout scheme.The radius can also optionally set client queues for speed limit per user it does that via some special response fields.Alternatively you can control customer speeds by other mechanism like tree queues etc.Your start point is setup a radius server and connect it to mikrotik. You can generally organize a vlan on the system to playwithout affecting the current running system. ---

## Response 3
+1 with @ldb @jvanhamWould something like this work, such that the client routers could obtain an IP address from the Radius server?radius (nas server) only handles AAA (users and password, mac addresses etc - as defined in attributes) requested by routers (nas clients) . it needs to work with dhcp server for ip address allocation.mikrotik wiki has a detailed guide for radius. you might want to read. ---

## Response 4
I've got this working - mostly.Here's the configuration that I now have set up:WISP-Network_Rayfield_RADIUS-Test_12-05-2024.pdfThe Client Router gets an IP address from the RADIUS server.But, after a few seconds, I get the following error in the MikroTik log:"Detected conflict by ARP response for 10.1.1.201 from A8:6E:84:16:70:88"ARP is enabled on the Site Router's port to which the Client Router is connected, but Proxy-ARP is not enabled anywhere in the network.Any ideas as to what's causing this?John ---

## Response 5
You could look at the first three bytes of the mac address, to see that mac address is from TP-Link deviceIf that's any clue for you ??https://maclookup.app/macaddress/a86e84 ... ss-detailsMaybe some one have put a TP-Link router into your network, that also answer to your clients dhcp requests. ---

## Response 6
I know what device it is. It's one that I put on the network to test the RADIUS server and DHCP.The problem is in regards to these error messages. I can't figure out why I'm getting them.John ---

## Response 7
Can it be that the dhcp authoritative is not set or set to invalid value.https://help.mikrotik.com/docs/spaces/R ... Properties ---
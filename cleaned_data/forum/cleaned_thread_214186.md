# Thread Information
Title: Thread-214186
Section: RouterOS
Thread ID: 214186

# Discussion

## Initial Question
Hi everybody!I have 1 WAN connection and 2 wireguard connections to mullvad VPN.As the mullvad IP is the same for both connections, I've put the interfaces into their own VRFs.Vlan VLAN1 should use the VPN1 connection, VLAN2 should use the VPN2 connection.I have created a script, which sets everything up:https://gitlab.com/close2/routeros-configuration(router_all.rsc with an example configuration at router-example-configuration.txt)The relevant commands are:
```
/interface/wireguard/addprivate-key=$privateKey1 name=VPN1/interface/wireguard/peers/addallowed-address=0.0.0.0/0,::/0endpoint-address=$endpointAddress1 endpoint-port=$endpointPort1interface=VPN1public-key=$publicKey1 persistent-keepalive=25s/ip/address/addaddress=$address1interface=VPN1/ipv6/address/addaddress=$addressIpv61interface=VPN1/ip/vrf/addinterfaces=VPN1 name=VPN1_VRF# An interface list where I add all vlans, which should use the VPN1/interface/list/addname=USE_VPN1_LIST# Create an additional routing table (not in the VRF!)/routing/table/addfib name=VPN1_RT/ip/route/adddst-address=0.0.0.0/0gateway=VPN1@VPN1_VRF routing-table=VPN1_RT# Not sure if the following line is necessary, but lets add the default route in the VRF as well:/ip/route/adddst-address=0.0.0.0/0gateway=VPN1@VPN1_VRF routing-table=VPN1_VRF# For every VLAN which is added to the USE_VPN1_LIST we will also add routes into the routing tables:/interface/list/member/addinterface=VLAN1  list=USE_VPN1_LIST/ip/route/adddst-address=10.0.1.0/24gateway=%VLAN1 routing-table=VPN1_RT/ip/route/adddst-address=10.0.1.0/24gateway=VLAN1@main routing-table=VPN1_VRF# Make sure that the VLAN1 interface only sees the VPN1 as default route by giving it the VPN1_RT as the routing table:/routing/rule/addinterface=VLAN1 action=lookup-only-in-table table=VPN1_RT# Note that VLAN1 can also access VLAN3.  Add a route for VLAN3 to VPN1_RT (but not VPN1_VRF):/ip/route/adddst-address=10.0.3.0/24gateway=%VLAN3 routing-table=VPN1_RT# Enable NAT on the VPN interface/ip/firewall/nat/addchain=srcnatout-interface=VPN1 ipsec-policy=out,none action=masquerade comment="masquerade vpn"# Add allow route into the firewall:/ip/firewall/filter/addchain=forward action=acceptin-interface-list=USE_VPN1_LISTout-interface=VPN1_VRF comment="accept forwarding vpn-VLANs"######## Same for VPN2Everything seems to work, except for the firewall rule.It doesn't trigger.As shown in router_all.rsc my last firewall rule is:
```

```
/ip/firewall/filter/addchain=forward action=drop comment="drop everything else"If I replace it with:
```

```
/ip/firewall/filter/addchain=forward action=accept comment="accept everything JUST FOR TESTING"devices in my VLAN1 start to use the VPN tunnel.What is the correct firewall rule?I am using 7.17 on a hAP ax².thanksChristian

---
```

## Response 1
I am still trying to get this to work.Is there anything I can provide?Should I open a support ticket?ThanksChristian ---
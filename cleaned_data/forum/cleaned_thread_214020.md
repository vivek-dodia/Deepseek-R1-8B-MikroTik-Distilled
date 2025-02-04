# Thread Information
Title: Thread-214020
Section: RouterOS
Thread ID: 214020

# Discussion

## Initial Question
Using RB1100AHX4 ( ROS V7.16.2 ) with config :
```
192.168.1.1ether1=wan1 ISP1(PublicStaticIP)192.168.2.1ether2=wan2 ISP2(DynamicPrivateIP)192.168.10.2ether3=LAN/ip firewall address-listaddaddress=192.168.10.3list=FOR-WAN1addaddress=192.168.10.0/24list=FOR-WAN2(forthe restofthe clients)/routing tableadddisabled=nofib name=TO-WAN1adddisabled=nofib name=TO-WAN2/ip firewall mangleaddaction=mark-routing chain=prerouting comment="WAN1 TRAFFIC"disabled=nolog=nolog-prefix=""new-routing-mark=TO-WAN1 passthrough=nosrc-address-list=FOR-WAN1addaction=mark-routing chain=prerouting comment="WAN2 TRAFFIC"disabled=nolog=nolog-prefix=""new-routing-mark=TO-WAN2 passthrough=nosrc-address-list=FOR-WAN2/ip firewall nataddaction=masquerade chain=srcnat disabled=nolog=nolog-prefix=""out-interface=ether1 src-address=192.168.10.0/24addaction=masquerade chain=srcnat disabled=nolog=nolog-prefix=""out-interface=ether2 src-address=192.168.10.0/24/ip routeaddcomment="ISP 1"disabled=nodistance=1dst-address=0.0.0.0/0gateway=192.168.1.1pref-src=""routing-table=TO-WAN1 scope=30suppress-hw-offload=notarget-scope=10addcomment="ISP 2"disabled=yes distance=1dst-address=0.0.0.0/0gateway=192.168.2.1routing-table=TO-WAN2 scope=30suppress-hw-offload=notarget-scope=10The problem is all client using only WAN1, my goal is just to have 1 lan lient ( 192.168.10.3 ) using wan1 and the rest of the clients ( 192.168.10.1 192.168.10.2 192.168.10.4 - 255 ) are using wan2.All wan are paralel and with no LB or failoverThanks before

---
```

## Response 1
I don't know if it would make any change but try using src-address directly instead of src-address-list in the mangle rules ---

## Response 2
Maybe you need:add address=192.168.10.3/32list=FOR-WAN1? ---

## Response 3
I don't know if it would make any change but try using src-address directly instead of src-address-list in the mangle rulesThanks for the tip, ip firewall address-list removed and change some routing and also mangle :
```
/ip firewall mangleaddaction=mark-routing chain=prerouting comment="WAN1 TRAFFIC"disabled=nolog=nolog-prefix=""new-routing-mark=TO-WAN1 passthrough=yes src-address=192.168.10.3/ip routeaddcomment="ISP 1"disabled=nodistance=1dst-address=0.0.0.0/0gateway=192.168.1.1pref-src=""routing-table=main scope=30suppress-hw-offload=notarget-scope=10addcomment="ISP 2"disabled=yes distance=1dst-address=0.0.0.0/0gateway=192.168.2.1routing-table=TO-WAN2 scope=30suppress-hw-offload=notarget-scope=10and now its working

---
```
# Thread Information
Title: Thread-1113378
Section: RouterOS
Thread ID: 1113378

# Discussion

## Initial Question
Hello all, I am in the middle of migrating my Cisco 10G Network to a Mikrotik 100 G. Actually I got less than a 3.5G of network traffic, 2 OSPF neigborhs (IPv4 / IPv4) and some SVI on the switch. Routing table has about 436 routes.Yesterday night, I tried to replace the Cisco Layer 3 Switch to CRS510-8XS-2XQ-IN, but immediately the CPU went up to 100%. I check and the networking process was consuming entre 55 and 60% of the CPU.Do you have any clue how to optimized the CPU consumption in my environment.Regards, Alejandro. ---

## Response 1
CRS devices are essentially switches ... as in L2 devices. Yes, running ROS on them does add L3 (routing), but without careful configuration those functions will be done by (slow) CPU.But: there's L3HW offload and it might work for you. Further reading:https://help.mikrotik.com/docs/spaces/R ... Offloading ---

## Response 2
Hello mkx, I tried activating the L3HW using the following commands:Switch Configuration/interface/ethernet/switch set 0 l3-hw-offloading=yesSwitch Port Configuration/interface/ethernet/switch/port set sfp-sfpplus1 l3-hw-offloading=yesBut it didn't have a positive impact on the cpu uitilization. ---

## Response 3
Hello mkx, I tried activating the L3HW using the following commands:Switch Configuration/interface/ethernet/switch set 0 l3-hw-offloading=yesSwitch Port Configuration/interface/ethernet/switch/port set sfp-sfpplus1 l3-hw-offloading=yesBut it didn't have a positive impact on the cpu uitilization.You have to enable it on all ports that are participating in routing.Likewise, if you're using IP addresses on VLAN interfaces, all ports with VLANs need to be a part of the bridge, with all VLANs with IP's tagged to the bridge, along with any ports that need the traffic. ---

## Response 4
Hello sirbryan, Exactly I enabled the L3HW over all active ports ( just only 4 ports). And the SVI and bridge config it's exactly as you describe it.Regards, ---

## Response 5
Are the MTU's on all the interfaces the same.The switch might fragment packets in software.My CRS305 does that... ---

## Response 6
any Firewall rules or VRF configured? ---

## Response 7
Hello rplant.The mtu values as default, do you suggest any other value?Regards, ---

## Response 8
Hello jookraw, No filter rules configured.I thought that the switch would be able to handle my traffic but seems like not. ---

## Response 9
Post your config (sanitized) and one of us can possibly point to what's happening. ---

## Response 10
Perhaps try the following commands to see if L3 offload is not present somewhere.With 400+ routes, you might want to write it to a file, so you can examine it in a text editor or similar./ip routeprint [file=somefilename]
```
Flags:D-DYNAMIC;A-ACTIVE;c-CONNECT,o-OSPF,d-DHCP;H-HW-OFFLOADEDColumns:DST-ADDRESS,GATEWAY,DISTANCE
     DST-ADDRESS       GATEWAY                DISTANCEDAdH0.0.0.0/0192.168.95.11DAcH192.168.40.0/24ether10DAc192.168.41.0/24vlan410DAcH192.168.42.0/24vlan420Doc mentions that larger prefixes (eg /32) are preferred by HW engine, so I assume this might mean that0.0.0.0/0 might be the first to fall out of HW offload if too many routes.(In this case vlan41 has no devices attached)/interface/ethernet/switch/print [file=...]
```

```
Columns:NAME,TYPE,L3-HW-OFFLOADING,QOS-HW-OFFLOADING# NAME     TYPE              L3-HW-OFFLOADING  QOS-HW-OFFLOADING0switch1Marvell-98DX3236yes               yes/interface/ethernet/switch portprint [file=...]
```

```
Columns:NAME,SWITCH,L3-HW-OFFLOADING,STORM-RATE# NAME          SWITCH   L3-HW-OFFLOADING  STORM-RATE0ether1        switch1  yes1001sfp-sfpplus1  switch1  yes1002sfp-sfpplus2  switch1  yes1003sfp-sfpplus3  switch1  yes1004sfp-sfpplus4  switch1  yes1005switch1-cpu   switch1You could put a passthrough firewall rule in the raw table and see if it is counting a lot.

---
```

## Response 11
One other thoughtIf you have an interface that is not part of the bridge, but has an IP address on it, it will route using hw offload.However if you have a vlan on this interface with an IP address on it, the vlan will use the CPU. ---
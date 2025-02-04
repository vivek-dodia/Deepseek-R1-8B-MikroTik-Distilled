# Thread Information
Title: Thread-213095
Section: RouterOS
Thread ID: 213095

# Discussion

## Initial Question
Hey all, Wonder if anyone has come up with a solution to this problem.background is I have 2 ISP connections, both of which hand out IPs using DHCP. Neither connection can be relied upon to provide a stable subnet (i.e. either subnet/gateway/ip will change without warning). I would like to use one connection as primary, and then the second connection as a backup while running my Internet over a Wireguard tunnel to a VPN server. In the event the first connection fails, the wireguard tunnel re-establishes over the secondary connection and there is minimal impact.What I was thinking of doing was tying each ISP-facing interface into its own VRF, and then make a policy rule to lookup the default route in each VRF. I would then use a netwatch script to disable the primary policy route so that lookups would happen over the secondary ISP.VRFs are all setup right, with the default routes being installed as expected, and I can ping out to the Internet with the policy lookups in place, however, the Wireguard tunnel itself doesn't seem to run over the VRF.If I put one of the ISPs in the main table, Wireguard comes up without issue. Is this expected behavior? Anything I can do to force Wireguard to run over the VRF? ---

## Response 1
The question is: do you really need the VRF's?Or you can with simpler different routing tables (fib)?VRF's can be tricky as some services might not work on them (as an example DNS is only partially working), and unless really really needed it is better to avoid them.Post your configuration. ---

## Response 2
Another option is to create a second wireguard interface except this one is live all the time on wan2. Assuming you want a faster migration to a working VPN, then waiting for the router to tell the client hey my WANIP has changed use this one now. ---

## Response 3
VRF's can be tricky as some services might not work on them (as an example DNS is only partially working), and unless really really needed it is better to avoid them.can you describe more, what do you thing by that ---

## Response 4
can you describe more, what do you thing by thatviewtopic.php?t=208899 ---

## Response 5
The question is: do you really need the VRF's?Or you can with simpler different routing tables (fib)?VRF's can be tricky as some services might not work on them (as an example DNS is only partially working), and unless really really needed it is better to avoid them.Post your configuration.Is there a way to accomplish what I want without VRFs? I'm not sure how I would shove a dhcp default route intp an alternate table without them.here is the releveant config snippits
```
/interfaceethernetset[finddefault-name=ether1]comment=TELUSset[finddefault-name=ether2]comment=CABLEset[finddefault-name=ether3]comment=LTE/interfacewireguardaddlisten-port=13237mtu=1420name=wg0/ip vrfaddinterfaces=ether1 name=FIBERaddinterfaces=ether3 name=LTEaddinterfaces=ether2 name=CABLE/interfacewireguard peersaddallowed-address=0.0.0.0/0endpoint-address=x.x.x.x endpoint-port=51820interface=wg0 name=wg-yyz persistent-keepalive=10spublic-key="xxxx"/ip addressaddaddress=100.64.105.3/24interface=wg0 network=100.64.105.0/ip dhcp-clientaddinterface=ether3/routing ruleaddaction=lookup disabled=yes dst-address=10.0.0.0/8table=CABLEaddaction=lookup disabled=yes dst-address=x.x.x.x/32table=CABLE

---
```

## Response 6
Anyone have a suggestion on how to fail a Wrieguard tunnel between multiple dhcp Internet connections without VRFs? ---
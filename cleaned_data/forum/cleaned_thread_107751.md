# Thread Information
Title: Thread-107751
Section: RouterOS
Thread ID: 107751

# Discussion

## Initial Question
I'm activating a new PPPoE server, a CCR1009, and for the first time i saw this message, when pppoe clients where connecting:
```
18:51:16pppoe,infoPPPoEconnection establishedfromEC:08:6B:XX:XX:XX18:51:16pppoe,infoPPPoEconnection establishedfromEC:08:6B:XX:XX:XX18:51:16pppoe,ppp,info,account xxx-yyy loggedin,146.247.ab.cd18:51:16pppoe,ppp,info<pppoe-xxx-yyy>:authenticated18:51:16pppoe,ppp,info<pppoe-xxx-yyy>:connected18:51:17pppoe,ppp,info<pppoe-xxx-yyy>:terminating...-spurios reauthentication18:51:17pppoe,ppp,info,account xxx-yyy loggedout,054723518:51:17pppoe,ppp,info<pppoe-xxx-yyy>:disconnectedThis happen only with two clients, the other 60 reconnected without problemsThe setup is:- the CCR has two interfaces, ether5 and ether6, bonded toghether with LACP;- on bond1 there are 3 VLAN: wan (internet), lan (server), ptp (wireless link to the network);- from the CCR to the RB750, where there are 4 sectors, there are 4 VPLS tunnels, one for each sector;- pppoe connections are encapsulated in VLAN, ID 10, but, for legacy configuration, there is also pppoe servers on "native" interfaces, the VPLSs- VPLS interfaces are unique port for bridges (workaround to avoid mass disconnection from VPLS disconnection)So, a default configuration is something like this
```

```
/interfacevplsaddname=vpls1.../interfacebridgeaddname=vpls1-bridge/interfacebridge portaddbridge=vpls1-bridgeinterface=vpls1/interfacevlanaddname=vlan_pppoe-vpls1interface=vpls1-bridge/interfacepppoe-server serveraddinterface=vlan_pppoe-vpls1addinterface=vpls1-bridgeMy workaround was to disable pppoe server on native interfaces, because I noticed
```

```
18:51:16pppoe,infoPPPoEconnection establishedfromEC:08:6B:XX:XX:XX18:51:16pppoe,infoPPPoEconnection establishedfromEC:08:6B:XX:XX:XXand enabling pppoe debug I saw PADI e PADO packet both from native and VLAN interfaces.Tomorrow I'll downgrade the CCR (but then I'll have to disable bonding interface).Any idea?

---
```

## Response 1
did you ever get a solution to this? I'm seeing the same error message with a pptp-client connectionPPTP server is on CCR1009-7G-1C-1S+ (tile) 6.49.8 ---

## Response 2
Forget about pptp, there are a lot better alternatives.It can be anything, from poor implementation to issues with CGNAT, which didn't existed when pptp was designed. ---
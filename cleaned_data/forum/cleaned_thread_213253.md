# Thread Information
Title: Thread-213253
Section: RouterOS
Thread ID: 213253

# Discussion

## Initial Question
I want to know how to create two different groups that can connect to my two internets that I get from my internet provider on the server.I need the WireGuard service.I have done some work, but I have a few problems with it, I will note them.The internet speed decreases after connecting to WireGuard.When I ping DNS, it times out.Untitledss.png
```
/interfacewireguardaddlisten-port=13231name=wireguard1/ip addressaddaddress=10.10.10.1/24interface=wireguard1addaddress=192.168.150.201/24network=192.168.150.0interface=ether1addaddress=192.168.150.202/24network=192.168.150.0interface=ether2/interface/wireguard/peersaddallowed-address=0.0.0.0/0interface=wireguard1public-key="u7gYAg5tkioJDcm3hyS7pm79eADKPs/ZUGON6/fF3iI="/routing/tableaddfib name=ip1addfib name=ip2/ip firewall mangleaddchain=prerouting src-addresses=10.10.10.11action=mark-routingnew-routing-mark=ip1 passthrough=noaddchain=prerouting src-addresses=10.10.10.12action=mark-routingnew-routing-mark=ip2 passthrough=no/ip firewall nataddchain=srcnat action=masqueradeout-interface=ether1addchain=srcnat action=masqueradeout-interface=ether2/ip/routeadddst-address=0.0.0.0/0gateway=192.168.150.1%ether1 routing-table=ip1adddst-address=0.0.0.0/0gateway=192.168.150.1%ether1 routing-table=ip2

---
```

## Response 1
Full config required, not snippets and its not clear why you need wireguard.From the diagram it looks like you simply want some computers on your LAN to go out WAN1 and some other computers to go out WAN2.Further its not clear if you are connecting to a third party vpn service, a CHR in the cloud or something else, or simply want wireguard to be able to reach the router or subnets when remote. ---
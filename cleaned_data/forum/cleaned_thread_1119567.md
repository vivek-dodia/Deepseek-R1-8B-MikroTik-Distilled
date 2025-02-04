# Thread Information
Title: Thread-1119567
Section: RouterOS
Thread ID: 1119567

# Discussion

## Initial Question
Hi folks, I'm testing the newamnezia-wgprotocol. I built a Docker container and ran it in my Microtic router.I can ping the network's peer IP and other resources from inside the container shell. However, my Microtik ignorance does not let me set up masquerading to be able to access resources from my local network. I would appreciate any help.What I have so far:10.1.0.1 - Amnezia Wireguard peer IP10.1.0.2 - Amnezia Wireguard IP address of the wg0 interface inside Docker containerDocker-related setup
```
/interfacebridgeaddname=containers/interfacevethaddaddress=172.17.0.2/24gateway=172.17.0.1gateway6=""name=veth1/interfacebridge portaddbridge=containersinterface=veth1/ip addressaddaddress=172.17.0.1/24interface=containers network=172.17.0.0/ip firewall nataddaction=masquerade chain=srcnat comment="Outgoing NAT for containers"src-address=172.17.0.0/24/container mountsadddst=/etc/wireguard/name=wg_config src=/wg/ip firewall nataddaction=dst-nat chain=dstnat comment=amnezia-wg dst-port=51820protocol=udp to-addresses=172.17.0.2to-ports=51820/container/addcmd=/sbin/init hostname=amneziainterface=veth1 logging=yes mounts=wg_config file=microtic-awg-arm7.tarTo set up Masquerading I tried the following:1. Create awgtest interface
```

```
/interface/bridge/printFlags:X-disabled,R-running0R name="awgtest"mtu=autoactual-mtu=1500l2mtu=65535arp=enabled arp-timeout=automac-address=32:52:22:4B:31:86protocol-mode=rstp fast-forward=yes igmp-snooping=noauto-mac=yes ageing-time=5mpriority=0x8000max-message-age=20sforward-delay=15stransmit-hold-count=6vlan-filtering=nodhcp-snooping=no2. Add an IP address to it
```

```
/ip/address/printFlags:D-DYNAMICColumns:ADDRESS,NETWORK,INTERFACE#   ADDRESS            NETWORK       INTERFACE;;;AWGMasqueradetest5172.17.1.1/24172.17.1.0awgtest3. Attempted to set up masquerading to 172.17.0.2 address of the Docker container running Amnezia Wireguard from the test 172.17.1.0/24 network
```

```
/ip/firewall/nat/printFlags:X-disabled,I-invalid;D-dynamic4chain=srcnat action=src-nat to-addresses=172.17.0.2src-address=172.17.1.0/24dst-address=10.0.0.0/8log=nolog-prefix=""My goal is to make this ping command work:
```

```
ping10.1.0.1src-address=172.17.1.1From inside the container it seems, it's working fine
```

```
>/container/shell0amnezia:/#ping10.1.0.1PING10.1.0.1(10.1.0.1):56data bytes64bytesfrom10.1.0.1:seq=0ttl=64time=156.498ms---10.1.0.1ping statistics---2packets transmitted,2packets received,0%packet loss
round-trip min/avg/max=156.498/156.651/156.804ms
amnezia:/#wginterface:wg0publickey:wU=privatekey:(hidden)jc:3jmin:100jmax:1000s1:432s2:291h1:1738505818h2:1770286633h3:1757239245h4:1787711703peer:Ig=endpoint:2--0allowed ips:10.1.0.0/16,192.168.0.0/16,151.0.0.0/8latest handshake:14seconds ago
  transfer:62.16MiBreceived,63.18MiBsentThanks in advance!

---
```

## Response 1
My bad. I have duplicate entries in the iptables inside the docker container. Also, I do not need masquerading, just need to set up proper routing, which I figured out already. Thanks. ---

## Response 2
can you share container file please? ---
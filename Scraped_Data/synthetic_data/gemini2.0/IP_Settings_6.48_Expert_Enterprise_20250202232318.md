## IP Settings

### Configuration Scenario and Requirements

This section covers the configuration of IP settings in MikroTik RouterOS for an enterprise-level network:

- IPv4 and IPv6 address assignment
- IP address pools and ranges
- Static and dynamic IP routing
- MAC address management
- Remote monitoring and management

### Step-by-Step Implementation

**1. IPv4/IPv6 Address Assignment**

- Assign an IPv4 address to an interface:
```
/ip address add address=192.168.100.1/24 interface=ether1
```

- Assign an IPv6 address to an interface:
```
/ipv6 address add address=fd00:1:1::1/64 interface=ether1
```

**2. IP Pools**

- Create an IP pool for IPv4 address assignment:
```
/ip pool add name=my-ip-pool range=192.168.100.10-192.168.100.20
```

- Create an IP pool for IPv6 address assignment:
```
/ipv6 pool add name=my-ipv6-pool range=fd00:1:1::10-fd00:1:1::20
```

**3. IP Routing**

- Configure static IPv4 routing:
```
/ip route add gateway=192.168.1.1 dst-address=192.168.100.0/24
```

- Configure dynamic IPv4 routing using OSPF:
```
/routing ospf instance add name=my-ospf
/routing ospf interface add instance=my-ospf interface=ether1
```

**4. MAC Server**

- Add a MAC address to the MAC server:
```
/mac-server add mac-address=00:11:22:33:44:55 interface=ether1
```

- **Note:** Ensure that the MAC server is enabled for the interface.

**5. RoMON**

- Enable RoMON for remote monitoring and management:
```
/tool romon enable
```

- Configure RoMON access:
```
/tool romon server add description="My RoMON Server" address=192.168.1.1 pass="password"
```

**6. WinBox**

- Enable WinBox access:
```
/ip service winbox enable
```

- **Note:** Ensure that the WinBox port (8291) is allowed in the firewall.

**7. Certificates**

- Import a certificate:
```
/certificate import file-name=my-cert.crt
```

- **Note:** Certificates are used for secure communication, such as SSL/TLS.

**8. PPP AAA**

- Create a PPP AAA server for authentication:
```
/ppp aaa server add name=my-ppp-server login=user password=pass
```

- **Note:** PPP AAA is used for authenticating PPP connections.

**9. RADIUS**

- Configure RADIUS authentication:
```
/radius server add address=192.168.1.1 secret=password
```

- **Note:** RADIUS is a centralized authentication server for managing user access.

**10. User/User Groups**

- Create a user account:
```
/user add name=admin password=pass group=admin
```

- Create a user group:
```
/user group add name=admin
```

- **Note:** User management allows for fine-grained access control.

**11. Bridging and Switching**

- Create a bridge:
```
/bridge add name=my-bridge
```

- Add an interface to the bridge:
```
/interface bridge add bridge=my-bridge interface=ether1
```

- **Note:** Bridging allows multiple devices to communicate as if they were on the same network segment.

**12. MACVLAN**

- Create a MACVLAN interface:
```
/interface macvlan add name=my-macvlan parent=ether1 mac-address=00:11:22:33:44:55
```

- **Note:** MACVLAN provides virtual LAN functionality on a single physical interface.

**13. L3 Hardware Offloading**

- Enable L3 hardware offloading:
```
/system l3-hardware-offloading enable
```

- **Note:** L3 hardware offloading improves performance by offloading routing functions to the hardware.

**14. MACsec**

- Configure MACsec encryption:
```
/interface macsec add name=my-macsec interface=ether1 encryption-mode=gcm-aes-256-128
```

- **Note:** MACsec provides encryption and integrity protection for Ethernet traffic.

**15. Quality of Service**

- Create a queue type:
```
/queue type add name=my-queue type=pcq packets-per-second=10000
```

- Assign a queue to an interface:
```
/interface queue add interface=ether1 queue=my-queue
```

- **Note:** QoS allows for prioritizing traffic based on specific criteria.

**16. Switch Chip Features**

- Enable VLAN tagging:
```
/switch chip vlan enable
```

- **Note:** Switch chip features provide advanced functionality on supported devices.

**17. VLAN**

- Create a VLAN:
```
/vlan add name=my-vlan vlan-id=10
```

- Add an interface to the VLAN:
```
/interface vlan add interface=ether1 vlan-id=10
```

- **Note:** VLANs partition a physical network into multiple logical networks.

**18. VXLAN**

- Create a VXLAN tunnel:
```
/interface vxlan add name=my-vxlan local-address=192.168.1.1 remote-address=192.168.100.1 remote-port=4789
```

- **Note:** VXLAN encapsulates traffic over UDP for virtualized network connectivity.

**19. Firewall and Quality of Service**

- Create a firewall rule:
```
/ip firewall filter add chain=forward action=accept src-address=192.168.100.0/24 dst-address=192.168.1.0/24
```

- **Note:** The firewall controls traffic flow through the router.

- Create a connection tracking rule:
```
/ip firewall connection tracking add comment="My Connection Tracking Rule"
```

- **Note:** Connection tracking allows for monitoring and controlling established connections.

- **Additional Firewall and QoS features:**
    - Packet Flow in RouterOS
    - Queues
    - Kid Control
    - UPnP
    - NAT-PMP

**20. IP Services (DHCP, DNS, SOCKS, Proxy)**

- Enable DHCP server:
```
/ip dhcp-server add interface=ether1 range=192.168.100.10-192.168.100.20 lease-time=86400
```

- Configure DNS forwarding:
```
/ip dns add forwarder-servers=8.8.8.8,8.8.4.4
```

- Enable SOCKS proxy:
```
/proxy socks add listen-on-address=192.168.1.1 listen-on-port=1080
```

- Configure HTTP proxy:
```
/proxy http add listen-on-address=192.168.1.1 listen-on-port=8080
```

- **Note:** IP services provide network connectivity and resource sharing.

**21. High Availability Solutions**

- Enable load balancing:
```
/ip load-balancing add balancing-mode=simple
```

- Create a bonding interface:
```
/interface bonding add name=my-bond slaves=ether1,ether2
```

- **Additional High Availability features:**
    - Bonding Examples
    - HA Case Studies
    - Multi-chassis Link Aggregation Group
    - VRRP
    - VRRP Configuration Examples

**22. Mobile Networking**

- Configure GPS tracking:
```
/gps add device-name=my-gps
```

- Enable LTE connectivity:
```
/interface lte add name=my-lte apn=internet.example.com
```

- **Additional Mobile Networking features:**
    - PPP
    - SMS
    - Dual SIM Application

**23. Multi Protocol Label Switching (MPLS)**

- Enable MPLS:
```
/mpls add
```

- Configure MPLS label binding:
```
/mpls forwarding add mpls-label=1000 ip-address=192.168.1.1
```

- **Additional MPLS features:**
    - MPLS Overview
    - MPLS MTU
    - EXP bit and MPLS Queuing
    - LDP
    - VPLS
    - Traffic Eng
    - MPLS Reference

**24.
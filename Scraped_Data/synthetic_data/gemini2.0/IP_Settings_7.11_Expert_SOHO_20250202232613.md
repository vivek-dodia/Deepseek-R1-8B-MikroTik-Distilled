## MikriTik RouterOS 7.11 IP Settings: Expert Configuration for SOHO Networks

### 1. Configuration Scenario and Requirements

- Configure IP addressing for IPv4 and IPv6 networks
- Implement IP pools for dynamic IP assignment
- Establish IP routing for network communication
- Configure advanced IP settings, such as MAC server and RoMON

### 2. Step-by-Step Implementation

**2.1 IP Addressing**

- Create IPv4 and IPv6 addresses on interfaces:
```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=2001:db8::1/64 interface=ether1
```

**2.2 IP Pools**

- Create an IP pool for IPv4 dynamic assignment:
```
/ip pool add name=my-pool ranges=192.168.1.2-192.168.1.100
```

**2.3 IP Routing**

- Configure static routes to specific networks:
```
/ip route add dst-address=10.0.0.0/24 gateway=192.168.1.2
/ip route add dst-address=2001:db8:1::/64 gateway=2001:db8::2
```

**2.4 IP Settings**

- Enable MAC server to track and manage MAC addresses:
```
/ip mac-server set enabled=yes
```

- Configure RoMON to monitor remote devices:
```
/system romon set active=yes
```

### 3. Complete Configuration Commands

The commands used in this configuration are listed below:

- `/ip address add`
- `/ip pool add`
- `/ip route add`
- `/ip mac-server set`
- `/system romon set`

### 4. Common Pitfalls and Solutions

- **Incorrect subnet mask or gateway address:** Ensure that the subnet mask and gateway address match the network configuration.
- **IP conflict:** Avoid duplicate IP addresses on the network. Use the `/ip address print` command to check for conflicts.
- **MAC server not enabled:** Ensure that the MAC server is enabled to track MAC addresses.
- **RoMON not active:** Verify that RoMON is active by using the `/system romon print` command.

### 5. Verification and Testing Steps

- Ping devices within the network to test IP connectivity.
- Use the `/ip pool print` command to verify IP pool configuration.
- Check the `/ip route print` output to ensure that routes are correctly configured.
- Monitor MAC entries using the `/ip mac-server print` command.
- Use the `/system romon print` command to check the status of RoMON.

### 6. Related Features and Considerations

- **DHCP server:** Use a DHCP server to automatically assign IP addresses to devices.
- **DNS server:** Configure a DNS server for name resolution.
- **Firewall:** Implement a firewall to protect the network from unauthorized access.
- **NAT:** Enable NAT to translate private IP addresses to public IP addresses.

### 7. MikroTik REST API Examples

**7.1 Get IP Address List**

**API endpoint:** `/ip/address`

**Request method:** GET

**Example JSON payload:** N/A

**Expected response:**
```json
[
  {
    "interface": "ether1",
    "address": "192.168.1.1/24"
  },
  {
    "interface": "ether2",
    "address": "2001:db8::1/64"
  }
]
```

**7.2 Create IP Pool**

**API endpoint:** `/ip/pool`

**Request method:** POST

**Example JSON payload:**
```json
{
  "name": "my-pool",
  "ranges": [
    "192.168.1.2-192.168.1.100"
  ]
}
```

**Expected response:**
```
{"id": "1"}
```

### 8. Additional Topics and Documentation

- [IP Addressing](https://wiki.mikrotik.com/wiki/Manual:IP/IP_Addressing)
- [IP Pools](https://wiki.mikrotik.com/wiki/Manual:IP/IP_Pool)
- [IP Routing](https://wiki.mikrotik.com/wiki/Manual:IP/IP_Routing)
- [MAC Server](https://wiki.mikrotik.com/wiki/Manual:IP/MAC_Server)
- [RoMON](https://wiki.mikrotik.com/wiki/Manual:System/RoMON)
- [WinBox](https://wiki.mikrotik.com/wiki/Winbox)
- [Certificates](https://wiki.mikrotik.com/wiki/Manual:System/Certificates)
- [PPP AAA](https://wiki.mikrotik.com/wiki/Manual:PPP/PPP_AAA)
- [RADIUS](https://wiki.mikrotik.com/wiki/Manual:PPP/PPP_RADIUS)
- [User / User Groups](https://wiki.mikrotik.com/wiki/Manual:User_Management)
- [Bridging and Switching](https://wiki.mikrotik.com/wiki/Manual:Bridge)
- [MACVLAN](https://wiki.mikrotik.com/wiki/Manual:VLAN/MACVLAN)
- [L3 Hardware Offloading](https://wiki.mikrotik.com/wiki/Manual:CRS/CRS_Hardware_Offloading)
- [MACsec](https://wiki.mikrotik.com/wiki/Manual:CRS/MACsec)
- [Quality of Service](https://wiki.mikrotik.com/wiki/Manual:QoS)
- [Switch Chip Features](https://wiki.mikrotik.com/wiki/Manual:CRS/Switch_Chip_Features)
- [VLAN](https://wiki.mikrotik.com/wiki/Manual:VLAN)
- [VXLAN](https://wiki.mikrotik.com/wiki/Manual:VXLAN)
- [Firewall and Quality of Service](https://wiki.mikrotik.com/wiki/Manual:IP/Firewall)
- [IP Services](https://wiki.mikrotik.com/wiki/Manual:IP)
- [High Availability Solutions](https://wiki.mikrotik.com/wiki/Manual:High_Availability)
- [Mobile Networking](https://wiki.mikrotik.com/wiki/Manual:Mobile_Networking)
- [Multi Protocol Label Switching - MPLS](https://wiki.mikrotik.com/wiki/Manual:MPLS)
- [Network Management](https://wiki.mikrotik.com/wiki/Manual:Management)
- [Routing](https://wiki.mikrotik.com/wiki/Manual:Routing)
- [System Information and Utilities](https://wiki.mikrotik.com/wiki/Manual:System)
- [Virtual Private Networks](https://wiki.mikrotik.com/wiki/Manual:VPNs)
- [Wired Connections](https://wiki.mikrotik.com/wiki/Manual:Ether)
- [Wireless](https://wiki.mikrotik.com/wiki/Manual:Wireless)
- [Internet of Things](https://wiki.mikrotik.com/wiki/Category:Internet_of_Things)
- [Hardware](https://wiki.mikrotik.com/wiki/Category:Hardware)
- [Diagnostics, Monitoring and Troubleshooting](https://wiki.mikrotik.com/wiki/Manual:Diagnostics)
- [Extended Features](https://wiki.mikrotik.com/wiki/Category:Extensions)
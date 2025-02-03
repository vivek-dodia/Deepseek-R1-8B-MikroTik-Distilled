## **IP Settings**

### **Configuration Scenario and Requirements**

- Configure IP addressing for multiple interfaces
- Create and manage IP address pools
- Enable and configure IP routing

### **Step-by-Step Implementation**

**1. IP Addressing**

- Configure IP address for eth1 interface:
```
/ip address add address=192.168.1.1/24 interface=ether1
```
- Configure IPv6 address for eth2 interface:
```
/ipv6 address add address=2001:db8::1/64 interface=ether2
```

**2. IP Pools**

- Create IPv4 address pool:
```
/ip pool add name=my-ipv4-pool range=192.168.1.10-192.168.1.20
```
- Create IPv6 address pool:
```
/ipv6 pool add name=my-ipv6-pool range=2001:db8::20-2001:db8::30
```

**3. IP Routing**

- Enable IP routing:
```
/ip routing enable
```
- Define static route:
```
/ip route add gateway=10.0.0.1 dst-address=192.168.2.0/24
```
- Configure dynamic routing protocol (e.g., OSPF):
```
/routing ospf
set enabled=yes
set area=0.0.0.0 advertise-reachable=yes
set network=192.168.1.0/24 passive=no
```

### **Complete Configuration Commands**

```
/ip address add address=192.168.1.1/24 interface=ether1
/ipv6 address add address=2001:db8::1/64 interface=ether2

/ip pool add name=my-ipv4-pool range=192.168.1.10-192.168.1.20
/ipv6 pool add name=my-ipv6-pool range=2001:db8::20-2001:db8::30

/ip routing enable
/ip route add gateway=10.0.0.1 dst-address=192.168.2.0/24

/routing ospf
set enabled=yes
set area=0.0.0.0 advertise-reachable=yes
set network=192.168.1.0/24 passive=no
```

### **Common Pitfalls and Solutions**

- Duplicate IP addresses: Ensure unique IP addresses are assigned to each interface.
- Incorrect subnet masks: Verify subnet masks match network requirements.
- Overlapping IP pools: Avoid creating overlapping address pools to prevent conflicts.
- Inadequate routing configuration: Ensure appropriate routes are defined to allow traffic flow.

### **Verification and Testing Steps**

- Use ping command to test IP address connectivity:
```
ping 192.168.1.2
ping 2001:db8::2
```
- Check IP routing table:
```
/ip route print
```

### **Related Features and Considerations**

- DHCP: Assign IP addresses automatically using DHCP server.
- DNS: Resolve domain names to IP addresses.
- Firewall: Filter and control IP traffic based on rules.

### **MikroTik REST API Examples**

**Create IPv4 Address Pool**

**Endpoint:** `/api-pools/ip-pool`

**Method:** `POST`

**Request Payload:**

```json
{
  "name": "my-ipv4-pool",
  "ranges": [
    {
      "from": "192.168.1.10",
      "to": "192.168.1.20"
    }
  ]
}
```

**Response:**

```json
{
  "id": "my-ipv4-pool",
  "name": "my-ipv4-pool",
  "ranges": [
    {
      "from": "192.168.1.10",
      "to": "192.168.1.20"
    }
  ]
}
```

**Enable IP Routing**

**Endpoint:** `/api/routing`

**Method:** `PUT`

**Request Payload:**

```json
{
  "enabled": true
}
```
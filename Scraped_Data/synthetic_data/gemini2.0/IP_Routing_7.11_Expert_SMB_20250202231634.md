## IP Routing in MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

Configure IP routing on a MikroTik RouterOS 7.11 router to ensure the efficient flow of packets between different networks. The router should:

- Serve multiple clients with IP addresses from a specific pool
- Forward packets between multiple subnets
- Provide a default route for outgoing traffic

### Step-by-Step Implementation

**1. Define IP Addressing**

- Create an IP pool to assign IP addresses to clients:
```
/ip pool add name=client-pool ranges=192.168.1.2-192.168.1.254
```

- Assign IP addresses from the pool to interfaces:
```
/interface ip address add interface=ether1 address=192.168.1.1/24
/interface ip address add interface=ether2 address=192.168.2.1/24
```

**2. Configure Static Routes**

- Create static routes to forward packets between subnets:
```
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.2
/ip route add dst-address=192.168.1.0/24 gateway=192.168.2.2
```

**3. Set Default Route**

- Configure a default route to handle outgoing traffic:
```
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.254
```

### Complete Configuration Commands

```
/ip pool add name=client-pool ranges=192.168.1.2-192.168.1.254
/interface ip address add interface=ether1 address=192.168.1.1/24
/interface ip address add interface=ether2 address=192.168.2.1/24
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.2
/ip route add dst-address=192.168.1.0/24 gateway=192.168.2.2
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.254
```

### Common Pitfalls and Solutions

- **Incorrect Subnet Masks:** Ensure that the subnet masks specified in IP addresses are valid and match the network configuration.
- **Duplicate IP Addresses:** Avoid assigning the same IP address to multiple devices or interfaces.
- **Missing Gateway:** Verify that the gateway address specified in static routes is correct and reachable.

### Verification and Testing Steps

- Check the IP addresses assigned to interfaces using the command: ```/ip address print```
- Test connectivity between client devices using the command: ```/ping <client-ip-address>```
- Trace the path of packets using the command: ```/ip route trace dst-address=<destination-ip>```

### Related Features and Considerations

- **DHCP Server:** Use the DHCP server to automatically assign IP addresses to clients.
- **Policy Routing:** Create rules to control the flow of traffic based on specific criteria.
- **Virtual Routing and Forwarding (VRF):** Use VRFs to isolate traffic between different network domains.

### MikroTik REST API Examples

**Get IP Routing Configuration**

```
HTTP Method: GET
API Endpoint: /routing/ip/route
```

**Response:**

```json
[
  {
    "active": true,
    "comment": null,
    "distance": 1,
    "disable": false,
    "dst-address": "0.0.0.0/0",
    "gateway": "192.168.1.254",
    "id": "14",
    "interface": null,
    "mask-length": 0,
    "priority": 1,
    "scope": 0,
    "src-address": null,
    "targeted": false,
    "type": 0,
    "virtual-router": null
  },
  {
    "active": true,
    "comment": null,
    "distance": 1,
    "disable": false,
    "dst-address": "192.168.1.0/24",
    "gateway": "192.168.2.2",
    "id": "15",
    "interface": "ether2",
    "mask-length": 24,
    "priority": 1,
    "scope": 0,
    "src-address": null,
    "targeted": false,
    "type": 0,
    "virtual-router": null
  }
]
```
**Topic: IP Settings**

**Configuration Scenario and Requirements**

Configure IP addressing, IP pools, and IP routing on a MikroTik RouterOS 7.11 router for an enterprise network.

**Step-by-Step Implementation**

**1. IP Addressing**

- Assign an IP address to an interface:
```
/ip address add address=192.168.1.1/24 interface=ether1
```

- Remove an IP address from an interface:
```
/ip address remove address=192.168.1.1/24 interface=ether1
```

- Display a list of IP addresses assigned to interfaces:
```
/ip address print
```

**2. IP Pools**

- Create an IP pool:
```
/ip pool add name=my-pool range=192.168.1.10-192.168.1.50
```

- Assign an IP pool to an interface:
```
/interface add dhcp-server dhcp-option=default-lease-time,3600 server=my-pool interface=ether1
```

- Remove an IP pool from an interface:
```
/interface remove dhcp-server interface=ether1
```

**3. IP Routing**

- Add a static route:
```
/ip route add gateway=192.168.1.254 dst-address=192.168.2.0/24
```

- Add a dynamic route:
```
/ip route add distance=1 gateway=192.168.1.254 dst-address=192.168.2.0/24
```

- Display a list of routing entries:
```
/ip route print
```

**Common Pitfalls and Solutions**

- Ensure that the IP address assigned to an interface does not conflict with any other IP address on the network.
- Verify that the IP pool range is not overlapping with any other IP pool ranges.
- Check that the gateway address specified in a static route is reachable.

**Verification and Testing Steps**

- Ping to an IP address assigned to an interface.
- Use the traceroute command to trace the path to a remote host.
- Verify that DHCP clients can obtain IP addresses from the configured IP pool.

**Related Features and Considerations**

- Firewall rules can be used to restrict access to specific IP addresses.
- Quality of Service (QoS) settings can be used to prioritize traffic based on IP addresses.
- Virtual routing and forwarding (VRF) can be used to create separate routing instances for different parts of the network.

**MikroTik REST API Examples**

**Get IP Address Details:**

**API Endpoint**: `/ip/address/getall`
**Request Method**: GET
**Example JSON Payload**: `{}`
**Expected Response**:
```
[
  {
    ".id": "1",
    "address": "192.168.1.1",
    "disabled": false,
    "interface": "ether1"
  },
  {
    ".id": "2",
    "address": "192.168.2.0",
    "broadcast": "192.168.2.255",
    "disabled": false,
    "interface": "ether2"
  }
]
```
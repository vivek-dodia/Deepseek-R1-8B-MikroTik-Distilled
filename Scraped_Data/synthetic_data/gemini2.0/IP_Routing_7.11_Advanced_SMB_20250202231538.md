## IP Routing

**Configuration Scenario and Requirements**

In this scenario, we aim to configure IP routing on a MikroTik RouterOS 7.11 device to enable communication between multiple subnets. The goal is to establish routing rules that determine how network traffic is forwarded based on the destination IP address.

**Step-by-Step Implementation**

**1. Configure IP Addresses**

Assign IP addresses to the interfaces connected to each subnet.

```
/ip address
add address=192.168.1.1/24 interface=ether1
add address=192.168.2.1/24 interface=ether2
```

**2. Configure Routing Table**

Add static routes to the routing table manually or use a routing protocol (e.g., OSPF).

**Static Routing:**

```
/ip route
add dst-address=192.168.2.0/24 gateway=192.168.1.2
```

**Routing Protocol (OSPF):**

```
/routing ospf
set enabled=yes
add network=192.168.1.0/24
add network=192.168.2.0/24
```

**3. Test Connectivity**

Verify connectivity between subnets using ping or traceroute.

```
/ping 192.168.2.10
/traceroute 192.168.2.10
```

**Complete Configuration Commands**

Refer to the Step-by-Step Implementation for specific commands.

**Common Pitfalls and Solutions**

* Ensure that the IP addresses assigned are valid and unique within the assigned range.
* Verify that interfaces are properly connected and have an established link.
* Check that the routing table entries are correct and do not contain conflicting entries.
* Troubleshoot any potential firewall rules that may prevent communication between subnets.

**Verification and Testing Steps**

* Ping devices on different subnets to confirm connectivity.
* Traceroute packets to verify the route taken by traffic.
* Monitor routing table updates and ensure they are as expected.

**Related Features and Considerations**

* **RIP:** A distance-vector routing protocol that can be used for automatic routing within a small network.
* **OSPF:** A link-state routing protocol that can be used to advertise routes over larger networks.
* **Policy Routing:** Allows administrators to define specific policies for routing traffic based on criteria such as source address, destination address, or service type.

**MikroTik REST API Examples**

**Get IP Routing Table:**

```json
GET /routing/ip/route
```

**Example Response:**

```json
[
  {
    ".id": "1",
    "active": true,
    "dst-address": "0.0.0.0/0",
    "gateway": "10.10.10.254",
    "prefix-length": 0
  },
  {
    ".id": "2",
    "active": true,
    "dst-address": "10.0.0.0/8",
    "gateway": "10.10.10.254",
    "prefix-length": 8
  }
]
```

**Add Static Route:**

```json
POST /routing/ip/route
{
  "dst-address": "192.168.2.0/24",
  "gateway": "192.168.1.2"
}
```
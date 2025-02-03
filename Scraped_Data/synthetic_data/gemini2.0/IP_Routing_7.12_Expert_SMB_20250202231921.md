**1. IP Routing**

**Configuration Scenario and Requirements:**

Configure IP routing on a MikroTik RouterOS 7.12 router to enable communication between subnets.

**2. Step-by-Step Implementation:**

1. Configure IP addresses and subnet masks on the router's interfaces.
```bash
/ip address add address=10.0.0.1/24 interface=ether1
/ip address add address=192.168.1.1/24 interface=ether2
```

2. Add static routes to the routing table.
```bash
/ip route add dst-address=192.168.2.0/24 gateway=10.0.0.2
/ip route add dst-address=10.0.0.0/24 gateway=192.168.1.2
```

**3. Complete Configuration Commands:**

| Command | Description |
|---|---|
| `/ip address add` | Adds an IP address to an interface. |
| `/ip address set` | Sets the IP address and subnet mask for an interface. |
| `/ip route add` | Adds a static route to the routing table. |

**4. Common Pitfalls and Solutions:**

* **Incorrect IP addresses or subnet masks:** Ensure that the IP addresses and subnet masks are correct for the network.
* **Duplicate routes:** Check the routing table for duplicate routes that can cause routing loops.

**5. Verification and Testing Steps:**

* Ping devices on different subnets to verify IP connectivity.
* Use the `/ip route print` command to view the routing table.

**6. Related Features and Considerations:**

* **Dynamic Routing Protocols:** Use dynamic routing protocols (e.g., OSPF, RIP) for automatic route discovery and maintenance.
* **Policy Routing:** configure specific routing rules to control traffic flow.
* **Routing Table Management:** Use the `/routing` menu in WinBox to manage routing tables.

**7. MikroTik REST API Examples:**

**Endpoint:** /ip/route/print

**Request Method:** GET

**Example JSON Payload:** None

**Expected Response:** A list of static routes in JSON format.

**Example:**
```json
[
  {
    ".id": ".0",
    "distance": 0,
    "gateway": "10.0.0.2",
    "mask-length": 24,
    "prefix": "192.168.2.0"
  },
  {
    ".id": ".1",
    "distance": 0,
    "gateway": "192.168.1.2",
    "mask-length": 24,
    "prefix": "10.0.0.0"
  }
]
```
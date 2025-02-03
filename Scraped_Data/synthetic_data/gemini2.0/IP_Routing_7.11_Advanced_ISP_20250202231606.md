**IP Routing**

**Configuration Scenario and Requirements**

- Configure a MikroTik RouterOS device as a router for an ISP network.
- The router should be able to route traffic between multiple subnets.
- The router should use static routes for specific destinations.
- The router should use dynamic routing protocols for other destinations.

**Step-by-Step Implementation**

**1. Configure IP Addressing**

- Assign IP addresses to each interface that will be used for routing.
- Create and apply IP addresses and subnet masks to the interfaces using the following commands:

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=192.168.2.1/24 interface=ether2
```

**2. Configure IP Routing**

- Enable IP forwarding on the router.
- Add static routes for specific destinations.
- Configure dynamic routing protocols as needed.

To enable IP forwarding and configure static routes, use the following commands:

```
/ip firewall filter add action=accept chain=forward
/ip route add dst-address=192.168.3.0/24 gateway=192.168.1.2
```

To configure OSPF, a dynamic routing protocol, use the following commands:

```
/routing ospf interface add interface=ether1
/routing ospf router-id 192.168.1.1
```

**3. Configure IP Routing Policies**

- Create IP routing policies to control how certain types of traffic are routed.
- Assign routing policies to specific interfaces or IP addresses.

To create a routing policy, use the following commands:

```
/ip route policy add dst-address=192.168.0.0/16 lookup=lookup2
```

To assign a routing policy to an interface, use the following command:

```
/interface ethernet set ether1 route-policy=lookup2
```

**Complete Configuration Commands**

Below are the complete configuration commands used in this example:

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=192.168.2.1/24 interface=ether2
/ip firewall filter add action=accept chain=forward
/ip route add dst-address=192.168.3.0/24 gateway=192.168.1.2
/routing ospf interface add interface=ether1
/routing ospf router-id 192.168.1.1
/ip route policy add dst-address=192.168.0.0/16 lookup=lookup2
/interface ethernet set ether1 route-policy=lookup2
```

**Common Pitfalls and Solutions**

- **IP forwarding is not enabled:** Ensure that IP forwarding is enabled on the router.
- **Incorrect IP addresses or subnet masks:** Verify that the IP addresses and subnet masks are correct.
- **Incorrect static routes:** Check that the destinations and gateways in the static routes are correct.
- **Incorrect routing protocol configuration:** Ensure that the routing protocol is configured correctly and that the appropriate interfaces are included.
- **Security concerns:** Implement appropriate security measures, such as firewall rules and ACLs, to protect the router from unauthorized access.

**Verification and Testing Steps**

- **Ping:** Test connectivity to different destinations by pinging them from the router.
- **Traceroute:** Trace the path of packets to different destinations to verify the routing path.
- **Routing table:** Check the routing table to ensure that the correct routes are installed.
- **IP route show:** Use the `/ip route show` command to display the current routing table.

**Related Features and Considerations**

- **Policy-based routing:** Allows you to define custom routing policies to control how traffic is routed.
- **Equal-cost multi-path (ECMP):** Enables the router to distribute traffic across multiple equal-cost paths to improve performance.
- **Load balancing:** Distributes traffic across multiple links or paths to balance the load and improve availability.

**MikroTik REST API Examples**

**Get the IP Routing Table**

**Endpoint:** `/routing/route`

**Request Method:** `GET`

**Example JSON Payload:**

```json
{
  "dst-address": "192.168.0.0/16",
  "scope": "global"
}
```

**Expected Response:**

```json
{
  "dst-address": "192.168.0.0/16",
  "gateway": "192.168.1.1",
  "interface": "ether1"
}
```

**Configure a Static IP Route**

**Endpoint:** `/routing/route`

**Request Method:** `POST`

**Example JSON Payload:**

```json
{
  "dst-address": "192.168.3.0/24",
  "gateway": "192.168.1.2"
}
```

**Expected Response:**

```json
{
  "id": 123,
  "dst-address": "192.168.3.0/24",
  "gateway": "192.168.1.2"
}
```
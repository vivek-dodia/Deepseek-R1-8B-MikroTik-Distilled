## IP Addressing (IPv4 and IPv6)

### Prerequisites

* MikroTik RouterOS 6.48 or later
* Basic understanding of IP networking

### IPv4 Addressing

**Step 1: Create an IP Address Pool**

```
/ip pool
add name=my-pool ranges=10.0.0.1-10.0.0.254
```

**Step 2: Enable DHCP Server**

```
/ip dhcp-server
set enabled=yes interface=ether1 pool=my-pool
```

**Step 3: Assign IP Addresses to Clients**

DHCP clients can now obtain IP addresses from the pool.

### IPv6 Addressing

**Step 1: Enable IPv6 on the Interface**

```
/ipv6 address
add address=fe80::1/10 interface=ether1
```

**Step 2: Enable DHCPv6 Server**

```
/ipv6 dhcp-server
set enabled=yes
```

**Step 3: Assign IPv6 Addresses to Clients**

Alternatively, you can use Router Advertisement (RA) to assign IPv6 addresses.

### Common Pitfalls

* **IP Address Conflicts:** Ensure there are no duplicate IP addresses within the network.
* **Incorrect Pool Range:** Verify that the IP pool ranges align with the desired subnet.
* **Invalid Interface:** Specify the correct interface when configuring DHCP or IPv6 settings.

### Verification

* Use `/ip address print` to list assigned IPv4 addresses.
* Use `/ipv6 address print` to list assigned IPv6 addresses.
* Test connectivity using ping or traceroute to ensure proper IP assignment.

### Troubleshooting

* If clients cannot obtain IPs, check if DHCP is enabled and if the correct pool is assigned.
* If IPv6 addressing issues occur, verify that IPv6 is enabled on the interface and that the DHCPv6 server is running.

### Related Features

* **IP Firewall:** Configure firewall rules to restrict access based on IP addresses.
* **IP Routing:** Enable routing to allow traffic flow between different subnets.
* **NAT:** Use Network Address Translation (NAT) to map private IP addresses to public ones.

### REST API Examples

#### GET IPv4 Address

```
GET /ip/address/print
```

#### POST Create IPv6 Address

**Example JSON Payload**:

```json
{
  "address": "fe80::1/10",
  "interface": "ether1"
}
```

```
POST /ipv6/address/add
```

#### Expected Response**:

```json
{
  "ret": "ok",
  "message": "ipv6 address added"
}
```
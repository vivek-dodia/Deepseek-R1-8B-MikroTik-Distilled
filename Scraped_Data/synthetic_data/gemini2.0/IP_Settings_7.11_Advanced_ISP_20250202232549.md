**IP Settings**

**Configuration Scenario and Requirements**

Configure IP settings for an ISP-scale network using RouterOS 7.11 to provide the following functionality:

- IPv4 and IPv6 addressing for multiple interfaces
- IP address pools for dynamic IP allocation
- Static IP routing for optimal network connectivity

**Step-by-Step Implementation**

**1. IP Addressing**

- Assign IPv4 and IPv6 addresses to physical interfaces:
```
/ip address add address=192.168.1.1/24 interface=ether1
/ipv6 address add address=2001:db8::1/64 interface=ether1
```

**2. IP Pools**

- Create IP pools for automatic IP address assignment:
```
/ip pool add name=MAIN addresses=192.168.1.2-192.168.1.255
/ipv6 pool add name=MAIN addresses=2001:db8::2-2001:db8::ffff
```

- Bind IP pools to interfaces for dynamic leasing:
```
/ip address add interface=ether2 dynamic-dhcp-lease-time=3600s ip-pool=MAIN
/ipv6 address add interface=ether2 dynamic-dhcp-lease-time=3600s ipv6-pool=MAIN
```

**3. Static IP Routing**

- Add static routes for IP subnets not directly connected to the router:
```
/ip route add dst-address=10.0.0.0/24 gateway=192.168.1.2
/ipv6 route add dst-address=2001:db8:2::0/64 gateway=2001:db8::2
```

**Complete Configuration Commands**

```
/ip address add address=192.168.1.1/24 interface=ether1
/ipv6 address add address=2001:db8::1/64 interface=ether1
/ip pool add name=MAIN addresses=192.168.1.2-192.168.1.255
/ipv6 pool add name=MAIN addresses=2001:db8::2-2001:db8::ffff
/ip address add interface=ether2 dynamic-dhcp-lease-time=3600s ip-pool=MAIN
/ipv6 address add interface=ether2 dynamic-dhcp-lease-time=3600s ipv6-pool=MAIN
/ip route add dst-address=10.0.0.0/24 gateway=192.168.1.2
/ipv6 route add dst-address=2001:db8:2::0/64 gateway=2001:db8::2
```

**Common Pitfalls and Solutions**

- Incorrect IP address or subnet mask: Verify the IP address and subnet mask are correct and used in the proper format.
- Overlapping IP ranges: Ensure that IP pools do not overlap with statically assigned IP addresses or other subnets.
- Invalid gateway address: Check that the gateway address for static routes is reachable and belongs to the same routing domain.

**Verification and Testing Steps**

- Ping external IP addresses to ensure connectivity:
```
ping 8.8.8.8
ping6 2001:4860:4860::8888
```

- Use `ip address print` and `ipv6 address print` to verify IP addressing and routing table.
- Utilize `ip pool print` and `ipv6 pool print` to inspect IP pools.
- Run `ip route check` and `ipv6 route check` to validate static routes.

**Related Features and Considerations**

- DHCP server configuration
- DNS settings
- Firewall rules for IP traffic filtering

**MikroTik REST API Examples**

**Get IP Address on Interface**

**API Endpoint:** `/ip/address/print`

**Request Method:** GET

**Example JSON Payload:**

```
{
  "interface": "ether1"
}
```

**Expected Response:**

```
[
  {
    "address": "192.168.1.1/24",
    "interface": "ether1"
  }
]
```
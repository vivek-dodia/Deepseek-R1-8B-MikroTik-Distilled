## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

- Configure IPv4 and IPv6 addressing on a MikroTik RouterOS 7.11 router.
- Assign IP addresses to physical and virtual interfaces.
- Enable IPv6 Neighbor Discovery (ND) and Router Advertisement (RA) for automatic IP address assignment.

### Step-by-Step Implementation

**IPv4 Configuration**

1. Assign IPv4 addresses to physical interfaces:
   ```
   /ip address add address=10.10.10.1/24 interface=ether1
   ```

2. Add a default route:
   ```
   /ip route add dst-address=0.0.0.0/0 gateway=10.10.10.254
   ```

**IPv6 Configuration**

1. Enable IPv6 on the router:
   ```
   /ipv6 enable
   ```

2. Assign IPv6 addresses to physical interfaces:
   ```
   /ipv6 address add address=2001:db8:ac10:fe12::1/64 interface=ether1
   ```

3. Enable IPv6 neighbor discovery (ND):
   ```
   /ipv6 nd add interface=ether1
   ```

4. Enable IPv6 router advertisement (RA):
   ```
   /ipv6 nd ra add interface=ether1 prefix=2001:db8:ac10:fe12::/64
   ```

### Complete Configuration Commands

```
# IPv4 Configuration
/ip address add address=10.10.10.1/24 interface=ether1
/ip route add dst-address=0.0.0.0/0 gateway=10.10.10.254

# IPv6 Configuration
/ipv6 enable
/ipv6 address add address=2001:db8:ac10:fe12::1/64 interface=ether1
/ipv6 nd add interface=ether1
/ipv6 nd ra add interface=ether1 prefix=2001:db8:ac10:fe12::/64
```

### Common Pitfalls and Solutions

- **IPv4 and IPv6 addressing conflicts:** Ensure that the assigned IP addresses do not overlap with any other devices on the network.
- **Subnet mask mismatch:** Make sure that the subnet mask specified in the IP address matches the subnet of the connected network.
- **Default gateway unreachable:** Verify that the specified default gateway is reachable and responds to ICMP requests.
- **IPv6 RA not working:** Ensure that the router is enabled for IPv6 and that RA is enabled on the desired interface.

### Verification and Testing Steps

- Ping an IPv4 and IPv6 address to verify connectivity:
   ```
   ping 10.10.10.2
   ping6 2001:db8:ac10:fe12::2
   ```

- Check the IP address and routing table:
   ```
   /ip address print
   /ip route print
   ```

- Use Wireshark or another network analyzer to capture packets and verify IP addressing and routing.

### Related Features and Considerations

- IP Pools: Allow for the dynamic assignment of IP addresses from a pool of available addresses.
- IP Routing: Configure advanced routing protocols (e.g., RIP, OSPF) to determine the best path for packets.
- IP Settings: Modify IPv4 and IPv6 settings, such as DHCP client or server, NAT, and firewall rules.
- MAC server: Manage MAC address tables and provide dynamic MAC address learning.
- RoMON: Enable remote monitoring and management of the router.
- WinBox: Use the graphical user interface (GUI) to configure the router.
- Certificates: Manage certificates for secure connections and authentication.
- PPP AAA: Configure authentication, authorization, and accounting for PPP connections.
- RADIUS: Integrate with a RADIUS server for centralized user authentication and authorization.
- User / User groups: Create and manage user accounts and groups for access control.

## MikroTik REST API Examples

**Get IPv4 addresses assigned to an interface:**

**Endpoint:** `/interface/ip/address/print`

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
    ".id": ".id",
    "address": "10.10.10.1/24",
    "comment": "",
    "disabled": false,
    "interface": "ether1"
  }
]
```

**Add an IPv6 address to an interface:**

**Endpoint:** `/ipv6/address/add`

**Request Method:** POST

**Example JSON Payload:**

```
{
  "address": "2001:db8:ac10:fe12::1/64",
  "interface": "ether1"
}
```

**Expected Response:**

```
{
  ".id": ".id",
  "address": "2001:db8:ac10:fe12::1/64",
  "comment": "",
  "disabled": false,
  "interface": "ether1"
}
```
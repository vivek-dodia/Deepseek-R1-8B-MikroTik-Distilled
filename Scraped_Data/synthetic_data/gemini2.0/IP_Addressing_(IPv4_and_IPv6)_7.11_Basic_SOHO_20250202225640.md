**IP Addressing (IPv4 and IPv6)**

MikroTik RouterOS provides comprehensive support for both IPv4 and IPv6 addressing, allowing for flexible and robust network configurations.

**Configuration Scenario and Requirements:**

- Configure IP addresses for a WAN interface (eth1) and a LAN interface (eth2)
- Enable IPv6 on both interfaces
- Assign IP addresses to hosts on the LAN

**Step-by-Step Implementation:**

**1. Configure WAN Interface (IPv4):**

- Navigate to **IP > Addresses**
- Click the **+** button
- Enter the following parameters:
  - **Interface:** eth1
  - **Address:** 192.168.1.2/24
  - **Gateway:** 192.168.1.1

**2. Enable IPv6 on WAN Interface:**

- Navigate to **IP > IPv6 > Addresses**
- Click the **+** button
- Enter the following parameters:
  - **Interface:** eth1
  - **Address:** 2001:db8::1/64

**3. Configure LAN Interface (IPv4):**

- Navigate to **IP > Addresses**
- Click the **+** button
- Enter the following parameters:
  - **Interface:** eth2
  - **Address:** 192.168.2.1/24
  - **Gateway:** (None)

**4. Enable IPv6 on LAN Interface:**

- Navigate to **IP > IPv6 > Addresses**
- Click the **+** button
- Enter the following parameters:
  - **Interface:** eth2
  - **Address:** 2001:db8::2/64

**5. Assign IP Addresses to Hosts:**

- Navigate to **IP > DHCP Server**
- Click the **+** button
- Enter the following parameters:
  - **Interface:** eth2
  - **Range:** 192.168.2.2-192.168.2.254

**Complete Configuration Commands:**

```
/ip address add interface=eth1 address=192.168.1.2/24
/ip address add interface=eth1 address=2001:db8::1/64
/ip address add interface=eth2 address=192.168.2.1/24
/ip address add interface=eth2 address=2001:db8::2/64
/ip dhcp-server add interface=eth2 range=192.168.2.2-192.168.2.254
```

**Common Pitfalls and Solutions:**

- **IP Address Conflict:** Ensure that the IP addresses are unique within each subnet.
- **Subnet Mask Error:** Verify that the subnet mask is correct and matches the IP address range.
- **Gateway Misconfiguration:** Check that the gateway address is reachable and belongs to the same subnet.
- **IPv6 Prefix Exhaustion:** Use a sufficiently large IPv6 prefix to avoid running out of addresses.

**Verification and Testing Steps:**

- Ping the gateway address from each interface (ping 192.168.1.1 from eth1, ping 192.168.2.1 from eth2)
- Test connectivity to the internet (ping 8.8.8.8)
- Check that hosts on the LAN can access the internet

**Related Features and Considerations:**

- IP Pools
- IP Routing
- IP Settings

**MikroTik REST API Example:**

**API Endpoint:** `/ip/address`

**Request Method:** GET

**Example JSON Payload:**

```json
{
  "interface": "eth1"
}
```

**Expected Response:**

```json
[
  {
    "address": "192.168.1.2/24",
    "interface": "eth1",
    "gateway": "192.168.1.1",
    "disabled": false
  }
]
```
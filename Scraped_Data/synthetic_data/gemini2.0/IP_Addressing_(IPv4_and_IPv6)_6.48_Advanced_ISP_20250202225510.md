**IP Addressing (IPv4 and IPv6)**

**Configuration Scenario and Requirements**

- Configure IPv4 and IPv6 addresses on a MikroTik RouterOS 6.48 router.
- Configure multiple IPv4 addresses on different interfaces.
- Configure IPv6 addresses with prefix delegation.

**Step-by-Step Implementation**

**1. Configure IPv4 Addresses**

- Navigate to IP > Addresses
- Click on the '+' button
- Enter the following parameters:
    - Address: IPv4 address
    - Interface: Interface to assign the address to
    - Network: Network mask
    - Comment: Optional description

**2. Configure Multiple IPv4 Addresses on Different Interfaces**

- Repeat Step 1 for each IPv4 address on different interfaces.

**3. Configure IPv6 Addresses with Prefix Delegation**

- Navigate to IP > Addresses
- Click on the '+' button
- Enter the following parameters:
    - Address: IPv6 address
    - Interface: Interface to assign the address to
    - Mode: Interface
    - Prefix Delegation: Enable
    - Pool Prefix: CIDR range for prefix delegation
    - Lease Time: Lease duration for delegated IPv6 addresses

**4. Save and Apply Configuration**

- Click on the 'Apply' button to save and apply the configuration.

**Complete Configuration Commands**

```
/ip address add address=192.168.1.1/24 interface=ether1 comment="LAN"
/ip address add address=192.168.2.1/24 interface=ether2 comment="WAN"
/ip address add address=2001:db8::1/64 interface=ether1 mode=interface prefix-delegation=yes pool-prefix=2001:db8::/64 lease-time=1h
```

**Common Pitfalls and Solutions**

- **IPv6 address conflicts:** Ensure that the IPv6 address range you assign is unique and does not conflict with other devices on the network.
- **Invalid IPv4 address or subnet mask:** Verify that the IPv4 address and subnet mask are valid and correspond to the network configuration.
- **Prefix delegation not working:** Check if prefix delegation is enabled on the interface and if the pool prefix is correct.

**Verification and Testing Steps**

- Use the following commands to verify the IP address configuration:
    - `/ip address print`
    - `/ip address show`
- Test IP connectivity by pinging other devices on the network.

**Related Features and Considerations**

- DHCP server: DHCP can be used to dynamically assign IP addresses to devices on the network.
- DNS: DNS is used to resolve hostnames to IP addresses.
- Firewall: The firewall can be used to control access to the network based on IP addresses.

**MikroTik REST API Examples**

**Get All IPv4 Addresses**

**API Endpoint:** `/api/ip/address`
**Request Method:** GET
**Response:**

```json
[
  {
    "address": "192.168.1.1",
    "disabled": false,
    "interface": "ether1",
    "network": "192.168.1.0/24"
  },
  {
    "address": "192.168.2.1",
    "disabled": false,
    "interface": "ether2",
    "network": "192.168.2.0/24"
  }
]
```

**Add IPv6 Address with Prefix Delegation**

**API Endpoint:** `/api/ip/address`
**Request Method:** POST
**Request Payload:**

```json
{
  "address": "2001:db8::1",
  "interface": "ether1",
  "mode": "interface",
  "prefix-delegation": true,
  "pool-prefix": "2001:db8::/64",
  "lease-time": "1h"
}
```

**Response:**

```json
{
  "address": "2001:db8::1",
  "disabled": false,
  "interface": "ether1",
  "network": "2001:db8::/64"
}
```
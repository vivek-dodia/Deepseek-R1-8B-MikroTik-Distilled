**IP Addressing (IPv4 and IPv6)**

**Configuration Scenario and Requirements:**

- Configure IPv4 and IPv6 addresses on a MikroTik router for connectivity and routing.

**Step-by-Step Implementation:**

**IPv4 Configuration:**

1. Go to IP -> Addresses
2. Click on the '+' button to add a new address
3. Select the interface (e.g., "ether1")
4. Enter the IPv4 address and subnet mask (e.g., "192.168.1.1/24")

**IPv6 Configuration:**

1. Go to IP -> Addresses
2. Click on the '+' button to add a new address
3. Select the interface (e.g., "ether1")
4. Choose "IPv6" from the Address Family dropdown
5. Enter the IPv6 address and prefix length (e.g., "2001:db8:85a3:8d3:1319:8a2e:370:7334/64")

**Complete Configuration Commands:**

**IPv4:**

```text
/ip address add address=192.168.1.1/24 interface=ether1
```

**IPv6:**

```text
/ip address add address=2001:db8:85a3:8d3:1319:8a2e:370:7334/64 interface=ether1
```

**Common Pitfalls and Solutions:**

- **Incorrect IP address or prefix length:** Ensure that the IP address and prefix length are valid for the connected network.
- **Duplicate IP address:** Multiple devices cannot have the same IP address on the same network.
- **IPv6 address not routable:** Check if the router has a default route for IPv6 traffic.

**Verification and Testing Steps:**

- Ping the IPv4 and IPv6 addresses from another device on the network.
- Use traceroute to verify the routing path.
- Check the IP address and prefix length in the IP -> Addresses section of the RouterOS configuration.

**Related Features and Considerations:**

- **IP Pools:** Create pools of IP addresses for dynamic assignment.
- **IP Routing:** Configure routing protocols to exchange network information and allow traffic flow.
- **IP Settings:** Adjust global IP-related settings, such as TTL and fragment size.
- **MAC Server:** Manage and track MAC addresses associated with IP addresses.

**MikroTik REST API Examples:**

**Endpoint:** `/api/ip/address`

**Request Method:** POST

**JSON Payload (Example):**

```json
{
  "address": "192.168.1.1",
  "prefix_length": 24,
  "interface": "ether1"
}
```

**Expected Response:**

```json
{
  "id": "<address-id>"
}
```
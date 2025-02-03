**IP Addressing (IPv4 and IPv6) in RouterOS 7.12**

**Configuration Level:** Basic

**Network Scale:** ISP

**Configuration Scenario and Requirements:**

Configure IPv4 and IPv6 addressing on a RouterOS 7.12 router to provide connectivity to multiple devices on a network.

**Step-by-Step Implementation:**

**1. IPv4 Addressing**

- Go to **IP > Addresses** in WinBox.
- Click the **+** button to create a new IPv4 address.
- Enter the following parameters:
    - **Interface:** Choose the interface to which you want to assign the address.
    - **Address:** Enter the IP address.
    - **Network:** Enter the network mask.
    - **Gateway:** Enter the default gateway address (optional).
- Click **OK**.

**2. IPv6 Addressing**

- Go to **IPv6 > Addresses** in WinBox.
- Click the **+** button to create a new IPv6 address.
- Enter the following parameters:
    - **Interface:** Choose the interface to which you want to assign the address.
    - **Address:** Enter the IPv6 address.
    - **Prefix Length:** Enter the network mask length (e.g., 64 for a /64 network).
- Click **OK**.

**Complete Configuration Commands:**

```
/ip address add address=10.0.0.1/24 interface=ether1
/ipv6 address add address=fd00::1/64 interface=ether1
```

**Common Pitfalls and Solutions:**

- **Incorrect network mask**: Ensure that you specify the correct network mask for both IPv4 and IPv6 addresses.
- **Gateway not set**: If you do not set a default gateway, devices on the network will not be able to access the internet.
- **IPv6 address conflicts**: Avoid assigning the same IPv6 address to multiple devices on the network.

**Verification and Testing Steps:**

- Use **ip addr** command from the terminal to verify IPv4 addressing.
- Use **ip -6 addr** command from the terminal to verify IPv6 addressing.
- Ping other devices on the network to test connectivity.

**Related Features and Considerations:**

- **IP Pools**: Create IP address pools to automatically assign addresses to devices.
- **IP Routing**: Configure routing protocols to enable network connectivity.
- **IP Settings**: Adjust IP-related settings such as DHCP, DNS, and MTU.

**MikroTik REST API Examples:**

**Create an IPv4 Address:**

**API Endpoint:** `/ip/address/`
**Request Method:** POST
**JSON Payload:**
```json
{
  "interface": "ether1",
  "address": "10.0.0.1/24"
}
```
**Expected Response:**
```json
{
  "id": 1
}
```

**Create an IPv6 Address:**

**API Endpoint:** `/ipv6/address/`
**Request Method:** POST
**JSON Payload:**
```json
{
  "interface": "ether1",
  "address": "fd00::1/64"
}
```
**Expected Response:**
```json
{
  "id": 1
}
```
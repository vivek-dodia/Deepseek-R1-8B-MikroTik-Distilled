**Section: IP Addressing (IPv4 and IPv6)**

**Configuration Scenario and Requirements:**

- Configure IP addresses for IPv4 and IPv6 networks on a MikroTik RouterOS 7.11 device.
- Use static IP addresses for both IPv4 and IPv6.
- Assign IP addresses to specific network interfaces.
- Enable DHCP server for IP address assignment on one network interface.

**Step-by-Step Implementation:**

**1. Set Static IPv4 Address**

- Go to **IP > Addresses** in the RouterOS configuration menu.
- Click the **"+"** button to create a new IP address.
- Select the **Interface** from the dropdown menu.
- Enter the **IPv4 Address** and **Subnet Mask**.
- Click **Apply** to save the configuration.

**2. Set Static IPv6 Address**

- Go to **IP > Addresses** in the RouterOS configuration menu.
- Select the **"IPv6 Tab"**.
- Click the **"+"** button to create a new IPv6 address.
- Select the **Interface** from the dropdown menu.
- Enter the **IPv6 Address** and **Prefix Length**.
- Click **Apply** to save the configuration.

**3. Enable DHCP Server**

- Go to **IP > DHCP Server** in the RouterOS configuration menu.
- Select the **Interface** from the dropdown menu where you want to enable DHCP.
- Click the **Checkbox** next to **"Enable DHCP Server"**.
- Enter the **IP Address Range** and **Subnet Mask** for the DHCP pool.
- Click **Apply** to save the configuration.

**Complete Configuration Commands:**

**IPv4 Static Address:**

```
/ip address add address=192.168.1.1/24 interface=ether1
```

**IPv6 Static Address:**

```
/ipv6 address add address=2001:db8::1/64 interface=ether1
```

**DHCP Server Configuration:**

```
/ip dhcp-server add address-pool=pool1 interface=ether2 range=192.168.2.100-192.168.2.200 subnet-mask=255.255.255.0
```

**Common Pitfalls and Solutions:**

- **Incorrect IP Address Range:** Make sure the IP address range specified for the DHCP server is within the subnet of the network interface.
- **Subnet Mask Mismatch:** Verify that the subnet mask for static IP addresses and the DHCP server pool matches the network segment.
- **Interface Selection:** Select the correct network interface for assigning IP addresses and enabling DHCP.

**Verification and Testing Steps:**

- Use the **"/ip address print"** command to verify the IPv4 address configuration.
- Use the **"/ipv6 address print"** command to verify the IPv6 address configuration.
- Use the **"/ip dhcp-server print"** command to verify the DHCP server configuration.
- Ping the configured IP addresses to test connectivity.

**Related Features and Considerations:**

- Dynamic Host Configuration Protocol (DHCP) allows for automatic assignment of IP addresses.
- Network Address Translation (NAT) can be used to provide public IP addresses to multiple devices behind a private network.
- Firewall rules can be configured to restrict or allow traffic based on IP addresses.

**REST API Examples:**

**Add IPv4 Address:**

**Endpoint:** `/ip/address/add`
**Request Method:** POST
**Example JSON Payload:**

```
{
  "interface": "ether1",
  "address": "192.168.1.1",
  "prefix-length": 24
}
```

**Expected Response:**

```
{
  "id": "1"
}
```

**Add IPv6 Address:**

**Endpoint:** `/ipv6/address/add`
**Request Method:** POST
**Example JSON Payload:**

```
{
  "interface": "ether1",
  "address": "2001:db8::1",
  "prefix-length": 64
}
```

**Expected Response:**

```
{
  "id": "1"
}
```

**Enable DHCP Server:**

**Endpoint:** `/ip/dhcp-server/add`
**Request Method:** POST
**Example JSON Payload:**

```
{
  "interface": "ether2",
  "address-pool": {
    "name": "pool1",
    "ranges": [
      {
        "start": "192.168.2.100",
        "end": "192.168.2.200"
      }
    ],
    "subnet": {
      "address": "192.168.2.0",
      "prefix-length": 255
    }
  }
}
```

**Expected Response:**

```
{
  "id": "1"
}
```
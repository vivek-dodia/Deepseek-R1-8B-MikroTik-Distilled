**IP Settings**

**1. Configuration Scenario and Requirements**

- Configure IP addresses and network settings for multiple interfaces on a MikroTik router running RouterOS 7.11.
- Use both IPv4 and IPv6 addresses, and assign IP addresses from an IP pool.
- Configure a default gateway and DNS servers.

**2. Step-by-Step Implementation**

**A. Configure IP Addresses**

- Navigate to **IP > Addresses**
- Click **+** to add a new IP address
- Select the interface from the **Interface** drop-down
- Enter the IP address in the **Address** field
- Specify the subnet mask in the **Network** field (e.g., /24 for IPv4, /64 for IPv6)
- Optional: Enable or disable NAT by checking/unchecking the **Allow** box
- Click **OK** to save the changes

**B. Configure IP Pool**

- Navigate to **IP > Pool**
- Click **+** to add a new IP pool
- Enter a name for the pool in the **Name** field
- Select the range of IP addresses in the **Range** field
- Optional: Specify a DNS server in the **DNS Server** field
- Optional: Specify a gateway in the **Gateway** field
- Click **OK** to save the changes

**C. Assign IP Addresses from IP Pool**

- Navigate to **IP > Addresses**
- Click **+** to add a new IP address
- Select the interface from the **Interface** drop-down
- Select the IP pool from the **Pool** drop-down
- Click **OK** to save the changes

**D. Configure Default Gateway and DNS Servers**

- Navigate to **IP > Routes**
- Click **+** to add a new route
- Enter the default gateway in the **Gateway** field
- Enter the DNS server(s) in the **DNS Server** field (multiple DNS servers can be separated by commas)
- Click **OK** to save the changes

**3. Complete Configuration Commands**

```
/ip address add address=10.0.0.1/24 interface=ether1
/ip address add address=2001:db8::1/64 interface=ether1
/ip pool add name=pool1 range=10.0.0.10-10.0.0.254
/ip address add address-pool=pool1 interface=ether2
/ip route add gateway=10.0.0.1
/ip route add dns=8.8.8.8
```

**4. Common Pitfalls and Solutions**

- **IP address conflict:** Ensure that the IP addresses assigned to different interfaces do not overlap.
- **No internet access:** Verify that the default gateway and DNS servers are correctly configured.
- **Unable to assign IP address from IP pool:** Check the IP pool configuration and ensure that the pool has available addresses.

**5. Verification and Testing Steps**

- Use the `/ip address print` command to verify the configured IP addresses.
- Use the `/ip route print` command to verify the default gateway and DNS servers.
- Test internet connectivity using the `ping` command.

**6. Related Features and Considerations**

- **DHCP Server:** Configure a DHCP server to automatically assign IP addresses to clients.
- **Firewall:** Configure firewall rules to control inbound and outbound traffic.
- **NAT:** Enable NAT to allow devices on the LAN to access the internet.
- **IPv6 Address Autoconfiguration:** Enable IPv6 address autoconfiguration to automatically assign IPv6 addresses to devices on the network.

**7. MikroTik REST API Examples**

**A. Get IP Addresses**

**Endpoint:** `/ip/address`

**Request Method:** GET

**Expected Response:**

```json
[
  {
    "address": "10.0.0.1/24",
    "interface": "ether1"
  },
  {
    "address": "2001:db8::1/64",
    "interface": "ether1"
  }
]
```

**B. Add IP Address**

**Endpoint:** `/ip/address`

**Request Method:** POST

**JSON Payload:**

```json
{
  "address": "192.168.1.10/24",
  "interface": "ether2"
}
```

**Expected Response:**

```json
{
  "status": "success"
}
```
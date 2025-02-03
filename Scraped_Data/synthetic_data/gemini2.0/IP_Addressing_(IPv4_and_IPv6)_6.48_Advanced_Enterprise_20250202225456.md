## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

The goal of this configuration is to assign IP addresses to the interfaces of a MikroTik RouterOS device, including both IPv4 and IPv6 addresses.

### Step-by-Step Implementation

**IPv4 Address Configuration**

1. Open the RouterOS configuration interface and navigate to the "IP" menu.
2. Select the "Addresses" tab.
3. Click the "Add New" button.
4. Enter the following parameters:
    - **Interface:** Select the network interface to which you want to assign an IPv4 address.
    - **Address:** Enter the desired IPv4 address.
    - **Network:** Enter the IPv4 network mask.
    - **Gateway:** Enter the default gateway for the IPv4 network.
5. Click "Apply" to save the changes.

**IPv6 Address Configuration**

1. Navigate to the "IPv6" section under the "IP" menu.
2. Select the "Addresses" tab.
3. Click the "Add New" button.
4. Enter the following parameters:
    - **Interface:** Select the network interface to which you want to assign an IPv6 address.
    - **Address:** Enter the desired IPv6 address.
    - **Prefix Length:** Enter the IPv6 prefix length (usually 64).
    - **Gateway:** Enter the IPv6 default gateway (if required).
5. Click "Apply" to save the changes.

### Complete Configuration Commands

**IPv4 Address Configuration**

```
/ip address add address=192.168.1.10/24 interface=ether3
```

**IPv6 Address Configuration**

```
/ipv6 address add address=2001:db8::1/64 interface=ether3
```

### Common Pitfalls and Solutions

**IPv4 Configuration**

- Ensure that the IPv4 address and network mask are valid and compatible.
- Check that the default gateway is reachable and online.

**IPv6 Configuration**

- IPv6 addresses are case sensitive. Ensure that the address is entered correctly.
- Verify that the prefix length is valid (usually 64).
- Ensure that the IPv6 gateway is reachable and online.

### Verification and Testing Steps

**IPv4**

- Use the command `/ip address print` to verify the assigned IPv4 address.
- Ping the default gateway to check connectivity.

**IPv6**

- Use the command `/ipv6 address print` to verify the assigned IPv6 address.
- Ping the IPv6 gateway to check connectivity.

### Related Features and Considerations

- **IP Pools:** IP Pools can be used to assign IP addresses dynamically.
- **IP Routing:** Ensure that IP routing is enabled to allow traffic to flow between different networks.
- **IP Settings:** Configure firewall rules and other IP settings to secure the network.
- **Hostname:** Set an appropriate hostname for the device for easy identification.

### REST API Examples

**Get IPv4 Addresses**

**API Endpoint:** `/ip/address/print`

**Request Method:** GET

**Expected Response:**

```json
[
  {
    "address": "192.168.1.10",
    "network": "192.168.1.0/24",
    "gateway": "192.168.1.1",
    "interface": "ether3"
  }
]
```

**Add IPv6 Address**

**API Endpoint:** `/ipv6/address/add`

**Request Method:** POST

**JSON Payload:**

```json
{
  "address": "2001:db8::1",
  "prefix-length": 64,
  "interface": "ether3"
}
```

**Expected Response:**

```
{
  "success": true
}
```
## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

**Scenario:** Configure IP addresses, both IPv4 and IPv6, on interfaces of a MikroTik router.

**Requirements:**

- MikroTik Router with RouterOS 7.12
- Configured interfaces
- IP address ranges and subnet masks

### Step-by-Step Implementation

#### IPv4 Configuration

1. Navigate to **IP** > **Addresses**
2. Click the **plus** (+) icon to create a new address.
3. Select the interface from the **Interface** dropdown.
4. Enter the IP address in the **Address** field.
5. Enter the subnet mask in the **Network** field.
6. Click **Apply** to save the configuration.

**Example:**

```
/ip address
add address=192.168.1.1/24 interface=ether1
```

#### IPv6 Configuration

1. Navigate to **IP** > **Addresses**
2. Click the **plus** (+) icon to create a new address.
3. Select the interface from the **Interface** dropdown.
4. Select **IPv6** from the **Address Family** dropdown.
5. Enter the IPv6 address in the **Address** field.
6. Click **Apply** to save the configuration.

**Example:**

```
/ip address
add address=2001:db8::1/64 interface=ether1
```

### Common Pitfalls and Solutions

- **Incorrect IP address or subnet mask:** Ensure the IP address and subnet mask are valid and match the network requirements.
- **Interface not configured:** Verify that the interface is properly configured and enabled.
- **Address conflict:** Check for IP address conflicts with other devices on the network.

### Verification and Testing Steps

1. Check the IP addresses assigned to the interfaces by running:

```
/ip address
print
```

2. Test connectivity by pinging an external IP address:

```
/ping 8.8.8.8
```

### Related Features and Considerations

- **DHCP Server:** Assign IP addresses automatically using a DHCP server.
- **Firewall:** Configure firewall rules to control traffic based on IP addresses.
- **Routing:** Configure routing protocols to direct traffic between different IP networks.

### REST API Examples

**Create an IPv4 Address:**

**Endpoint:** `/api/ip/address/add`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "address": "192.168.1.1/24",
  "interface": "ether1"
}
```

**Expected Response:**

```json
{
  "id": 1
}
```

**Create an IPv6 Address:**

**Endpoint:** `/api/ip/address/add`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "address": "2001:db8::1/64",
  "interface": "ether1",
  "address-family": "ipv6"
}
```

**Expected Response:**

```json
{
  "id": 1
}
```
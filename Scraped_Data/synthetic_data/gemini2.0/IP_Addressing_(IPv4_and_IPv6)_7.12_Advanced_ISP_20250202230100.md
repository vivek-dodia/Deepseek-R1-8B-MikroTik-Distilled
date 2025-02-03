## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

**Scenario:**
Configure IP addressing (IPv4 and IPv6) on a MikroTik RouterOS router.

**Requirements:**
- MikroTik RouterOS version 7.12 or higher
- Router with at least one Ethernet interface

### Step-by-Step Implementation

**1. Create IPv4 Address:**

- Navigate to **IP > Addresses**
- Click on the **"Add New"** button
- Enter the following parameters:
    - **Interface:** Select the interface to assign the IP address to
    - **Address:** Enter the desired IPv4 address
    - **Network:** Enter the subnet mask of the network
    - **Gateway:** Enter the default gateway address (if necessary)
- Click on the **"Apply"** button

**2. Create IPv6 Address:**

- Navigate to **IP > Addresses**
- Click on the **"Add New"** button
- Enter the following parameters:
    - **Interface:** Select the interface to assign the IPv6 address to
    - **Address:** Enter the desired IPv6 address
    - **Prefix:** Enter the prefix length of the IPv6 address
- Click on the **"Apply"** button

### Complete Configuration Commands

**IPv4 Address:**

```
/ip address add address=192.168.1.1/24 interface=ether1
```

**IPv6 Address:**

```
/ip address add address=2001:db8::1/64 interface=ether1
```

### Common Pitfalls and Solutions

- **Incorrect Interface:** Ensure that the selected interface is the correct one for the IP address to be assigned to.
- **Overlapping Addresses:** Avoid assigning IP addresses that overlap with existing addresses on the network.
- **Incorrect Subnet Mask:** Verify that the subnet mask is correct for the desired network configuration.

### Verification and Testing Steps

- Use the command **"/ip address print"** to verify that the IP addresses have been configured correctly.
- Test the connectivity by pinging other devices on the network.
- Check the status of the interfaces using the command **"/interface print"**.

### Related Features and Considerations

- **DHCP Server:** MikroTik RouterOS supports DHCP server functionality to automatically assign IP addresses to devices on the network.
- **DNS Server:** Configuring DNS settings on the router allows devices to resolve domain names to IP addresses.
- **Static Routes:** Adding static routes can be necessary to route traffic to specific destinations that are not directly connected to the router.

### MikroTik REST API Examples

**GET Request to Retrieve IPv4 Addresses:**

**Endpoint:** `/api/ip/address`

**Request Method:** GET

**Example JSON Payload:**

```json
{}
```

**Expected Response:**

```json
[
  {
    "address": "192.168.1.1",
    "interface": "ether1",
    "network": "192.168.1.0/24"
  }
]
```

**POST Request to Add IPv6 Address:**

**Endpoint:** `/api/ip/address`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "address": "2001:db8::1/64",
  "interface": "ether1"
}
```

**Expected Response:**

```json
{
  "result": "success"
}
```
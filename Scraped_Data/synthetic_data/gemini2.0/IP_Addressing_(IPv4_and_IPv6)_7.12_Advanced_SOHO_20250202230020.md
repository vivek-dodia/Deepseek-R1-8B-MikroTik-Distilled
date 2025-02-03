## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

In this scenario, we will configure IP addresses and related settings for IPv4 and IPv6 networks on a MikroTik RouterOS device. We aim to provide step-by-step instructions for configuring IP addresses, IP subnets, default gateways, and related parameters for both IPv4 and IPv6.

### Step-by-Step Implementation

#### IPv4 Configuration

1. Access the device's RouterOS command line interface (CLI) via SSH or WinBox.
2. Navigate to the IP menu: `/ip address`
3. Click on the '+' button to add a new IP address configuration.
4. Specify the interface on which to configure the IP address.
5. Enter the IPv4 address and subnet mask.
6. Optionally, configure the default gateway for the network.
7. Click on 'OK' to apply the configuration.

#### IPv6 Configuration

1. Navigate to the IPv6 menu: `/ipv6 address`
2. Click on the '+' button to add a new IPv6 address configuration.
3. Specify the interface on which to configure the IPv6 address.
4. Enter the IPv6 address and prefix length.
5. Optionally, configure the default gateway for the network.
6. Click on 'OK' to apply the configuration.

### Complete Configuration Commands

#### IPv4 Configuration
```
/ip address
add address=192.168.1.1/24 interface=ether1
```

#### IPv6 Configuration
```
/ipv6 address
add address=fe80::1/128 interface=ether1
```

### Common Pitfalls and Solutions

- **Incorrect subnet mask:** Ensure that the subnet mask for the IPv4 address is correct for the network topology.
- **Duplicate IP addresses:** Verify that the IP addresses configured on different interfaces do not conflict.
- **Missing default gateway:** For networks requiring access to external networks, a default gateway must be configured.
- **Invalid IPv6 address:** Ensure that the IPv6 address format is correct and falls within the appropriate prefix length.
- **Firewall rules blocking traffic:** Check firewall rules to ensure that they are not blocking traffic to or from the configured IP addresses.

### Verification and Testing Steps

- Use the `/ip address print` and `/ipv6 address print` commands to verify the configured IP addresses.
- Ping the configured IP addresses to ensure connectivity.
- Test access to external networks (if applicable) by browsing the internet or connecting to remote hosts.

### Related Features and Considerations

- **IP Pools:** For dynamic IP address assignment, create IP pools and configure addresses, subnets, and gateways.
- **IP Routing:** Configure routing tables to define forwarding rules for IP traffic.
- **IP Settings:** Adjust global IP-related settings, such as TTL and MTU.
- **MAC server:** Use the MAC server to track MAC addresses and assign IP addresses based on MAC addresses.
- **NAT:** Configure Network Address Translation (NAT) rules to enable private networks to access the public internet.

### MikroTik REST API Examples

#### IPv4
**API Endpoint:** `/ip/address`  
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
#### IPv6
**API Endpoint:** `/ipv6/address`  
**Request Method:** POST
**Example JSON Payload:**
```json
{
  "address": "fe80::1/128",
  "interface": "ether1"
}
```

**Expected Response:**
```json
{
  "id": 1
}
```
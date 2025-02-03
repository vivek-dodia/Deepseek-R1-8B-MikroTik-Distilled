## IP Settings

### 1. Configuration Scenario and Requirements

- Configure an IP address and subnet mask on a MikroTik router.
- Use DHCP to automatically assign IP addresses to clients connected to the router.

### 2. Step-by-Step Implementation

#### Step 1: Configure IP Address on Router's Interface

```
/ip address add address=192.168.1.1/24 interface=ether1
```

- `address`: IP address with subnet mask
- `interface`: Interface on which to configure the IP address

#### Step 2: Configure DHCP Server

```
/ip dhcp-server add interface=ether2 address-pool=pool1 lease-time=24h
```

- `interface`: Interface to enable DHCP on
- `address-pool`: Name of the DHCP pool
- `lease-time`: Lease time for DHCP-assigned IP addresses

### 3. Complete Configuration Commands

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip dhcp-server add interface=ether2 address-pool=pool1 lease-time=24h
```

### 4. Common Pitfalls and Solutions

- Ensure the interface is not blocking DHCP traffic.
- If DHCP clients are unable to obtain an IP address, check the DHCP pool configuration and ensure there are available addresses.

### 5. Verification and Testing Steps

- Verify the IP address configuration on the router:
```
/ip address print
```

- Confirm that DHCP is enabled and working:
```
/ip dhcp-server print
```

- Connect a client to the DHCP-enabled interface and check if it receives an IP address from the router.

### 6. Related Features and Considerations

- **IP Pools:** Specify a range of IP addresses to be assigned by the DHCP server.
- **IP Routing:** Configure routes to other networks for internet access or inter-VLAN communication.
- **MAC Server:** Map MAC addresses to specific IP addresses, ensuring consistent IP assignments.

### 7. MikroTik REST API Examples

**API Endpoint:** `/ip/address`

**Request Method:** `PUT`

**Example JSON Payload:**

```json
{
  "interface": "ether1",
  "address": "192.168.1.1/24"
}
```

**Expected Response:**

```json
{
  "result": "OK"
}
```

**Additional Examples:**

- List all IP addresses on the router: `/ip/address/print`
- Delete an IP address: `/ip/address/delete`

## Other MikroTik Topics

- **IP Addressing (IPv4 and IPv6)**: Configure IPv4 and IPv6 addresses, subnets, and gateway settings.
- **MAC Server**: Map MAC addresses to IP addresses for static IP assignment or DHCP filtering.
- **WinBox**: Use the graphical user interface for easy router configuration.
- **Firewall and QoS**: Implement firewall rules and prioritize network traffic based on criteria.
- **IP Services (DHCP, DNS, SOCKS, Proxy)**: Set up DHCP, DNS, SOCKS, and proxy services for network connectivity.
- **Mobile Networking**: Configure cellular connections, manage SMS, and use GPS for location-based services.
- **Multi Protocol Label Switching - MPLS**: Implement MPLS for advanced traffic engineering and virtual private networks.
- **Routing**: Configure various routing protocols (e.g., OSPF, RIP, BGP) for efficient network communication.
- **System Information and Utilities**: Monitor system resources, manage time zones, and configure logging.
- **Virtual Private Networks**: Configure VPNs (e.g., IPsec, OpenVPN) for secure remote access.
- **Wireless**: Set up wireless networks, manage access points, and implement security measures.
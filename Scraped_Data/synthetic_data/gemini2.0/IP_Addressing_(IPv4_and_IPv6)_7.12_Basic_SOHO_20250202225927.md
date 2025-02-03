## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

- Configure IP addresses for IPv4 and IPv6 networks on a MikroTik router.
- Set up a default gateway and DNS servers for IPv4 and IPv6.
- Assign IP addresses from a pool of addresses to interfaces.

### Step-by-Step Implementation

**IPv4 Configuration**
- Go to **IP → Addresses** tab in WinBox.
- Click on the **+** button to add a new address.
- Select the interface you want to assign an IP address to.
- Enter the IPv4 address and subnet mask.
- (Optional) Enter the default gateway and DNS servers.

**IPv6 Configuration**
- Go to **IP → Addresses** tab in WinBox.
- Click on the **+** button to add a new address.
- Select the desired interface, e.g. "ether1".
- Enable IPv6 by selecting it from the "Address Family" drop-down.
- Click on the **"DHCP Client"** tab.
- Select the interface you want to configure and click on the **"Enable"** checkbox.

**Assigning IP Addresses from a Pool**
- Go to **IP → Pools** tab in WinBox.
- Click on the **+** button to add a new address pool.
- Enter the network address and subnet mask for the pool.
- Set the **"Ranges"** to specify the range of IP addresses available in the pool.
- Go to **IP → Addresses** tab.
- Select the interface you want to assign an IP address from the pool.
- In the **"Pool"** field, select the pool you created.

### Complete Configuration Commands

**IPv4 Configuration**
```
/ip address add address=192.168.1.10/24 interface=ether1
```

**IPv6 Configuration**
```
/ipv6 address add address=2001:db8::1/64 interface=ether1
/ipv6 dhcp-client add interface=ether1
```

**Assigning IP Address from a Pool**
```
/ip address add address=dhcp interface=ether1 pool=dhcp-pool-1
```

### Common Pitfalls and Solutions

- **IP Conflict:** Make sure the IP address assigned is not already in use by another device on the network.
- **Incorrect Subnet Mask:** Ensure the subnet mask entered is correct for the network.
- **Gateway Unreachable:** Verify the default gateway IP address entered is reachable.
- **DNS Server Issues:** Ensure the DNS servers entered are accessible and can resolve domain names.

### Verification and Testing Steps

- Check the **IP → Addresses** tab to confirm the IP addresses have been assigned correctly.
- Ping an external website or a device on the network to test connectivity.
- Use nslookup to check if DNS is working correctly.

### Related Features and Considerations

- **IPv4/IPv6 Address Management:** Use the **IP → Addresses** tab to manage all IP addresses assigned to the router.
- **DHCP Server:** Configure a DHCP server to automatically assign IP addresses to devices on the network.
- **Firewall:** Implement firewall rules to control access to and from the router.
- **NAT:** Enable NAT (Network Address Translation) to allow devices on the private network to access the internet.

### MikroTik REST API Examples

**Create an IPv4 Address**
```
POST /ip/address
{
  "address": "192.168.1.10/24",
  "interface": "ether1"
}
```

**Create an IPv6 Address with DHCP**
```
POST /ipv6/address
{
  "address": "2001:db8::1/64",
  "interface": "ether1",
  "dhcp_client": true
}
```

**Assign an IP Address from a Pool**
```
POST /ip/address
{
  "address": "dhcp",
  "interface": "ether1",
  "pool": "dhcp-pool-1"
}
```
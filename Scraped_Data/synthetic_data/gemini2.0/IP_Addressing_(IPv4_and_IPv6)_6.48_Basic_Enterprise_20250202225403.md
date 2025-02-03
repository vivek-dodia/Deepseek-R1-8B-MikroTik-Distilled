## IP Addressing (IPv4 and IPv6)

### Scenario and Requirements

- Configure IPv4 and IPv6 addresses on multiple interfaces.
- Use IP pools to assign IP addresses dynamically to clients.

### Step-by-Step Implementation

**IPv4 Configuration**

1. Navigate to **IP > Address** in WinBox.
2. Click the **+** button to create a new entry.
3. Select the interface to assign the address to from the **Interface** drop-down menu.
4. Enter the IP address and subnet mask in the respective fields.
5. Click **Apply** to save the changes.

**IPv6 Configuration**

1. Navigate to **IP > IPv6 > Address** in WinBox.
2. Click the **+** button to create a new entry.
3. Select the interface to assign the address to from the **Interface** drop-down menu.
4. Enter the IPv6 address, subnet prefix length, and autoconfiguration type.
5. Click **Apply** to save the changes.

**IP Pool Configuration**

1. Navigate to **IP > Pool** in WinBox.
2. Click the **+** button to create a new pool.
3. Enter a name for the pool in the **Name** field.
4. Select the network type (IPv4 or IPv6) from the **Type** drop-down menu.
5. Enter the starting and ending IP addresses for the pool in the respective fields.
6. Optionally, specify a lease time for the addresses.
7. Click **Apply** to save the changes.

### Complete Configuration Commands

**IPv4 Address**

```
ip address add interface=ether1 address=192.168.1.1/24
```

**IPv6 Address**

```
ipv6 address add interface=ether1 address=2001:db8::1/64
```

**IP Pool**

```
ip pool add name=my-pool type=dhcp-client ranges=192.168.1.100-192.168.1.200 lease-time=3600
```

### Common Pitfalls and Solutions

**Pitfall:** Assigning an incorrect subnet mask or prefix length.
**Solution:** Ensure that the subnet mask or prefix length matches the network topology and address range.

**Pitfall:** Overlapping IP pools.
**Solution:** Ensure that the ranges of IP pools do not overlap to avoid IP address conflicts.

**Pitfall:** Misconfiguration of autoconfiguration type for IPv6 addresses.
**Solution:** Verify that the autoconfiguration type (e.g., SLAAC, DHCPv6) is appropriate for the network environment.

### Verification and Testing Steps

**IPv4 Address Verification:**

- Use the `ip address print` command to display the assigned IPv4 addresses.

**IPv6 Address Verification:**

- Use the `ipv6 address print` command to display the assigned IPv6 addresses.

**IP Pool Verification:**

- Use the `ip pool print` command to display the configured IP pools.
- Assign IP addresses to clients using DHCP or manual configuration and verify that they receive IP addresses from the specified pool.

### Related Features and Considerations

**DHCP Server**

- Use the DHCP server to automatically assign IP addresses and other network configuration parameters to clients.
- Configure DHCP settings in **IP > DHCP Server**.

**DNS Settings**

- Configure DNS settings in **IP > DNS** to resolve hostnames.
- Specify DNS servers or use DNS forwarding to resolve external hostnames.

### REST API Examples

**Add IPv4 Address**

```
POST /ip/address
{
  "interface": "ether1",
  "address": "192.168.1.1/24"
}
```

**Add IPv6 Address**

```
POST /ipv6/address
{
  "interface": "ether1",
  "address": "2001:db8::1/64"
}
```

**Add IP Pool**

```
POST /ip/pool
{
  "name": "my-pool",
  "type": "dhcp-client",
  "ranges": ["192.168.1.100-192.168.1.200"],
  "lease-time": 3600
}
```
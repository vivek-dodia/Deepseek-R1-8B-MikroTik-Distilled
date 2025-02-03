## IP Pools

### Configuration Scenario and Requirements

In an enterprise network, it is necessary to configure and manage IP pools to dynamically assign IP addresses to network devices. This section provides a detailed guide on configuring IP pools in RouterOS 7.11.

### Step-by-Step Implementation

1. **Create an IP Pool:**

   Navigate to **IP > Pool**. Click the "+" button to create a new pool. Enter a name for the pool, select the address range, and choose the network interface to use.

2. **Configure IP Address Options:**

   Under the "Address" tab, specify the IP address range, subnet mask, and default gateway. You can also configure additional IP address options, such as DHCP lease time and DNS servers.

3. **Set DNS and DHCP Options:**

   Under the "DNS" and "DHCP" tabs, configure DNS server settings and DHCP options as per your network requirements.

4. **Save and Apply:**

   Click "Apply" to save the IP pool configuration.

### Complete Configuration Commands

```
/ip pool add name=pool1
/ip pool set pool1 address=192.168.1.0/24 interface=ether1
/ip pool set pool1 dhcp-server=yes
/ip pool set pool1 dns-server=8.8.8.8,8.8.4.4
/ip pool set pool1 lease-time=43200
```

### Common Pitfalls and Solutions

- **IP Address Overlap:** Ensure that the specified IP address range does not overlap with any existing IP addresses in the network.
- **Incorrect Interface:** Verify that the selected network interface is the one to which you want to assign IP addresses.
- **DHCP Server Conflict:** Avoid configuring multiple DHCP servers on the same network to prevent IP address conflicts.

### Verification and Testing Steps

1. **Check IP Pool Status:**

   Navigate to **IP > Pool** and check the status of the created pool under the "Status" column.

2. **Verify DHCP Service:**

   Connect a device to the network and check if it receives an IP address from the DHCP server assigned to the IP pool.

3. **Test DNS Resolution:**

   Check if DNS requests are resolved correctly using the DNS servers configured in the IP pool.

### Related Features and Considerations

- **DHCP Server:** Configure DHCP server settings to automatically assign IP addresses to devices on the network.
- **Firewall Rules:** Implement firewall rules to control access to the IP pool and prevent unauthorized access.
- **Monitoring and Troubleshooting:** Utilize RouterOS tools like "IP > DHCP Snooping" and "Log > Events" to monitor and troubleshoot IP pool issues.

### MikroTik REST API Examples

#### Get IP Pool List

**API Endpoint:** `/router/ip/pool/getall`
**Request Method:** GET
**Example JSON Payload:**
```json
{}
```
**Expected Response:**
```json
[
  {
    ".id": "1",
    "address": "192.168.1.0/24",
    "dhcp-server": "yes",
    "dns-server": "8.8.8.8,8.8.4.4",
    "gateway": "192.168.1.1",
    "interface": "ether1",
    "name": "pool1"
  }
]
```

#### Add IP Pool

**API Endpoint:** `/router/ip/pool/add`
**Request Method:** POST
**Example JSON Payload:**
```json
{
  "name": "pool2",
  "address": "192.168.2.0/24",
  "interface": "ether2"
}
```
**Expected Response:**
```json
{
  ".id": "2"
}
```
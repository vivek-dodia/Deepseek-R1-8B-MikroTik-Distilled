## IP Pools

### Configuration Scenario and Requirements

In this scenario, you need to configure multiple IP pools to assign IP addresses to devices on your network. Each pool will have a specific IP range and subnet mask.

### Step-by-Step Implementation

1. Open the **IP -> IP Pool** section in RouterOS WinBox.
2. Click the **+** button to create a new pool.
3. Configure the following parameters for each pool:

   - **Name:** Give the pool a descriptive name.
   - **Ranges:** Specify the IP range for the pool in CIDR notation (e.g., 192.168.1.0/24).
   - **Gateway:** Enter the gateway IP address for the pool.
   - **DNS Server:** Specify the DNS server IP address for the pool.
   - **Lease Time:** Set the amount of time (in seconds) that IP addresses are leased to devices.

4. Repeat steps 2-3 for each additional pool you need to create.

### Complete Configuration Commands

```
/ip pool add name="MyPool1" ranges=192.168.1.0/24 gateway=192.168.1.1 dns-server=8.8.8.8 lease-time=600
/ip pool add name="MyPool2" ranges=192.168.2.0/24 gateway=192.168.2.1 dns-server=8.8.4.4 lease-time=900
```

### Common Pitfalls and Solutions

- **Ensure that the IP ranges do not overlap.** Overlapping IP ranges can lead to IP address conflicts and network problems.
- **Set appropriate lease times.** Too short lease times can cause devices to lose their IP addresses frequently, while too long lease times can result in wasted IP addresses.
- **Consider using DHCP reservations.** DHCP reservations allow you to assign specific IP addresses to specific devices. This is useful for devices that need a static IP address, such as servers or network printers.

### Verification and Testing Steps

1. Verify that the IP pools are working by assigning IP addresses to devices on your network.
2. Use the **/ip pool print** command to check the status of the pools.
3. Ping the IP addresses assigned to the devices to ensure that they are reachable.

### Related Features and Considerations

- **DHCP Server:** The DHCP server in RouterOS can be used to automatically assign IP addresses from the configured pools.
- **NAT:** Network Address Translation (NAT) can be used to map IP addresses from the pools to external IP addresses.
- **Firewall:** The firewall in RouterOS can be used to restrict access to devices on the network based on the IP pool they are assigned to.

### MikroTik REST API Examples

**API Endpoint:** `/api/ip/pool`

**Request Method:** GET

**Example JSON Payload:**

```json
{
  "ranges": [
    "192.168.1.0/24",
    "192.168.2.0/24"
  ]
}
```

**Expected Response:**

```json
[
  {
    "name": "MyPool1",
    "ranges": [
      "192.168.1.0/24"
    ],
    "gateway": "192.168.1.1",
    "dns-server": "8.8.8.8",
    "lease-time": 600
  },
  {
    "name": "MyPool2",
    "ranges": [
      "192.168.2.0/24"
    ],
    "gateway": "192.168.2.1",
    "dns-server": "8.8.4.4",
    "lease-time": 900
  }
]
```
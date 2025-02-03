## IP Settings

### Configuration Scenario and Requirements

This section describes how to configure basic IP settings on a MikroTik RouterOS device running version 6.48 or later. These settings include IP addressing, IP pools, and IP routing.

### Step-by-Step Implementation

**1. IP Addressing**

- Log into the RouterOS device using WinBox or the CLI.
- Navigate to **IP > Addresses** and click on the "+" button to create a new IP address.
- In the Interface field, select the interface to which you want to assign the IP address.
- In the Address field, enter the IP address you want to assign.
- In the Network field, enter the subnet mask for the IP address.
- Click on the **OK** button to save the changes.

**2. IP Pools**

- Navigate to **IP > Pools** and click on the "+" button to create a new IP pool.
- In the Name field, enter a name for the IP pool.
- In the Ranges field, enter the range of IP addresses that you want to include in the pool.
- Click on the **OK** button to save the changes.

**3. IP Routing**

- Navigate to **IP > Routes** and click on the "+" button to create a new IP route.
- In the Destination field, enter the destination IP address or network that you want to route traffic to.
- In the Gateway field, enter the gateway IP address for the destination network.
- Click on the **OK** button to save the changes.

### Complete Configuration Commands

**IP Addressing:**

```
/ip address add address=192.168.1.1/24 interface=ether1
```

**IP Pools:**

```
/ip pool add name=pool1 ranges=192.168.1.10-192.168.1.254
```

**IP Routing:**

```
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.2
```

### Common Pitfalls and Solutions

- **Incorrect IP address or subnet mask:** Ensure that the IP address and subnet mask are correct for the network you are configuring.
- **IP conflict:** Check for duplicate IP addresses on the network.
- **Gateway not reachable:** Ensure that the gateway IP address is reachable from the device.
- **No route to destination:** Verify that there is a route to the destination network.

### Verification and Testing Steps

- Use the **ping** command to test connectivity to the IP address.
- Use the **ip route print** command to verify that the IP routing table is correct.

### Related Features and Considerations

- **DHCP:** DHCP can be used to automatically assign IP addresses to devices on the network.
- **DNS:** DNS can be used to resolve hostnames to IP addresses.
- **Firewall:** A firewall can be used to control access to the network based on IP addresses.

### MikroTik REST API Examples

**Get all IP addresses:**

```
GET /api/ip/address
```

**Add a new IP address:**

```
POST /api/ip/address
{
  "interface": "ether1",
  "address": "192.168.1.1/24"
}
```

**Get all IP pools:**

```
GET /api/ip/pool
```

**Add a new IP pool:**

```
POST /api/ip/pool
{
  "name": "pool1",
  "ranges": [
    "192.168.1.10-192.168.1.254"
  ]
}
```

**Get all IP routes:**

```
GET /api/ip/route
```

**Add a new IP route:**

```
POST /api/ip/route
{
  "dst-address": "192.168.2.0/24",
  "gateway": "192.168.1.2"
}
```
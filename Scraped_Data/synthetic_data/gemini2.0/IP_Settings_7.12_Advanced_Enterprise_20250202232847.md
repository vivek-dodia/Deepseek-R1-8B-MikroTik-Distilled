## IP Settings

### Configuration Scenario and Requirements

Configure IP settings on a MikroTik RouterOS 7.12 router to provide Internet access to clients and manage network resources efficiently.

**Requirements:**

- MikroTik RouterOS 7.12 router
- Internet connection
- Client devices

### Step-by-Step Implementation

**1. Assign IP Address to WAN Interface:**

- Navigate to **IP > Addresses**
- Click **Add (+)**
- Select **Interface** as WAN interface
- Enter **IP Address** for WAN interface (e.g., from ISP)
- Enter **Network Mask** (e.g., 24)
- Click **Apply**

**2. Set Default Gateway:**

- Navigate to **IP > Routes**
- Click **Add (+)**
- Enter **Destination** network (e.g., 0.0.0.0/0)
- Enter **Gateway** (e.g., ISP router IP address)
- Click **Apply**

**3. Configure DHCP Server:**

- Navigate to **IP > DHCP Server**
- Click **DHCP Setup** tab
- Enable **DHCP Server**
- Select **Interface** to assign IP addresses from
- Enter **Subnet** (e.g., 192.168.1.0/24)
- Click **Apply**

**4. Configure DNS Settings:**

- Navigate to **IP > DNS**
- Click **Settings** tab
- Enter **DNS Servers** (e.g., 8.8.8.8, 8.8.4.4)
- Click **Apply**

**5. Manage MAC Server:**

- Navigate to **IP > MAC Server**
- Click **Add (+)**
- Enter **MAC Address** of device
- Assign **IP Address**
- Enter **Comment** (optional)
- Click **Apply**

**6. Set Firewall Rules:**

- Navigate to **IP > Firewall**
- Click on **Filter Rules** tab
- Click **Add (+)**
- Create rules to allow/deny traffic based on source/destination IP addresses, ports, etc.
- Click **Apply**

### Complete Configuration Commands

```
/ip address add address=10.0.0.1/24 interface=WAN
/ip route add gateway=10.0.0.254/24 destination=0.0.0.0/0
/ip dhcp-server add disabled=no interface=LAN lease-time=12h subnet=192.168.1.0/24
/ip dns set servers=8.8.8.8,8.8.4.4
/ip mac-server add MAC-Address=F8:DE:9F:43:28:64 IP-Address=192.168.1.100
/ip firewall filter add action=drop chain=input dst-address=192.168.1.0/24 protocol=tcp dst-port=25
```

### Common Pitfalls and Solutions

- **Incorrect IP Address**: Ensure the IP address assigned to the WAN interface is valid and matches the ISP configuration.
- **Gateway Not Set**: Verify that the default gateway is correctly configured for the router to access the Internet.
- **DHCP Misconfiguration**: Check the subnet and lease-time settings of the DHCP server to ensure they are appropriate for the network.
- **Firewall Blocks**: Disable or adjust firewall rules if they are preventing connectivity.
- **MAC Address Conflict**: Ensure that each device in the network has a unique MAC address to avoid IP address conflicts.

### Verification and Testing Steps

- Ping the WAN gateway from the router.
- Check Internet connectivity on client devices.
- Verify DHCP-assigned IP addresses on client devices.
- Use a packet sniffer to monitor network traffic and identify any issues.

### Related Features and Considerations

- **IP Addressing**: Understand IP address classes, subnet masks, and network addressing concepts.
- **IP Routing**: Explore different routing protocols (e.g., OSPF, BGP) and their role in network connectivity.
- **IP Settings**: Configure advanced IP settings such as static routes, IPsec tunnels, and QoS policies.
- **MAC Server**: Manage and control MAC addresses for network access.
- **Firewall and QoS**: Implement security and traffic management policies to protect and optimize the network.

### MikroTik REST API Examples

**Get IP Address Information:**

**Endpoint:** `/ip/address/`
**Request Method:** GET
**Response:**

```json
[
  {
    "address": "10.0.0.1",
    "comment": "WAN IP",
    "disabled": false,
    "interface": "WAN",
    "network": "10.0.0.0"
  }
]
```

**Set Firewall Rule:**

**Endpoint:** `/ip/firewall/filter/`
**Request Method:** POST
**Request Body:**

```json
{
  "action": "drop",
  "chain": "input",
  "dst-address": "192.168.1.0/24",
  "protocol": "tcp",
  "dst-port": 25,
  "comment": "Block port 25"
}
```

**Expected Response:**

```json
{
  "id": "99"
}
```
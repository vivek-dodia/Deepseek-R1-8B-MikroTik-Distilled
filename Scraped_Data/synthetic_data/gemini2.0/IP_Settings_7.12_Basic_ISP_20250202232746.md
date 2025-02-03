## IP Settings in MikroTik RouterOS 7.12

### Configuration Scenario and Requirements

This guide covers the basic configuration of IP settings in RouterOS 7.12. The focus is on providing practical examples for IP addressing, IP routes, and IP firewall rules.

**Prerequisites:**

- RouterOS 7.12 installed and accessible
- Basic understanding of IP networking
- Physical network connections (e.g., Ethernet, Wi-Fi)

### Step-by-Step Implementation

#### IP Addressing

**IPv4:**
1. Navigate to **IP > Addresses** in the WinBox GUI.
2. Click **+** to add a new IP address.
3. Configure the **Interface**, **IP Address**, and **Subnet Mask**.
4. Click **OK**.

**IPv6:**
1. Navigate to **IP > Addresses** in the WinBox GUI.
2. Click **+** to add a new IP address.
3. Configure the **Interface**, **IPv6 Address** (e.g., 2001:db8::1/64), and **Prefix Length**.
4. Click **OK**.

**Tip:** Use the "/ip address add" command to add IP addresses via CLI.

#### IP Routes

**Static Route:**
1. Navigate to **IP > Routes** in the WinBox GUI.
2. Click **+** to add a new route.
3. Configure the **Destination Network**, **Gateway**, and **Interface**.
4. Click **OK**.

**Default Gateway:**
1. Navigate to **IP > Routes** in the WinBox GUI.
2. Click the **0.0.0.0/0 Gateway** route.
3. Configure the **Gateway** and **Interface**.
4. Click **OK**.

**Tip:** Use the "/ip route add" command to add routes via CLI.

#### IP Firewall Rules

**Allow Traffic from Specific IP Address:**
1. Navigate to **IP > Firewall** in the WinBox GUI.
2. Click the **+** button under **Filter Rules**.
3. Configure the **Chain** (e.g., forward), **Src.** (source IP address), and **Action** (e.g., accept).
4. Click **OK**.

**Block Traffic from Specific IP Address:**
1. Navigate to **IP > Firewall** in the WinBox GUI.
2. Click the **+** button under **Filter Rules**.
3. Configure the **Chain** (e.g., forward), **Src.** (source IP address), and **Action** (e.g., drop).
4. Click **OK**.

**Tip:** Use the "/ip firewall add" command to add firewall rules via CLI.

### Complete Configuration Commands

**IP Address (IPv4):**
```
/ip address add interface=ether2 address=192.168.1.10/24
```

**IP Address (IPv6):**
```
/ip address add interface=ether2 address=2001:db8::1/64
```

**Static Route:**
```
/ip route add dst-address=10.10.10.0/24 gateway=192.168.1.1
```

**Default Gateway:**
```
/ip route add 0.0.0.0/0 gateway=192.168.1.1
```

**Allow Traffic from Specific IP Address (Firewall):**
```
/ip firewall add chain=forward src-address=10.10.10.10 action=accept
```

**Block Traffic from Specific IP Address (Firewall):**
```
/ip firewall add chain=forward src-address=10.10.10.10 action=drop
```

### Common Pitfalls and Solutions

- **IP Address Conflict:** Ensure there are no duplicate IP addresses on the network.
- **Gateway Not Reachable:** Verify the gateway IP address and interface are correct.
- **No Internet Access:** Check the default gateway route and make sure the router has internet connectivity.
- **Firewall Blocking Legitimate Traffic:** Review firewall rules and ensure they are not blocking expected traffic.

### Verification and Testing Steps

- **IP Address:** Use the "ip address print" command to verify IP addresses.
- **IP Routes:** Use the "ip route print" command to verify routes.
- **Firewall Rules:** Use the "ip firewall print" command to verify firewall rules.
- **Internet Connectivity:** Browse to a website or perform a DNS lookup to test internet access.

### Related Features and Considerations

- **IP Pools:** Assign IP addresses dynamically using IP pools.
- **RoMON:** Remote monitoring and management of RouterOS devices.
- **WinBox:** Graphical user interface for managing RouterOS.

### MikroTik REST API Examples

#### **Get IP Addresses**

**Endpoint:** `/ip/address`
**Method:** GET
**Example JSON Payload:** None
**Expected Response:**
```json
[
  {
    "interface": "ether2",
    "address": "192.168.1.10",
    "network": "192.168.1.0/24",
    "scope": "global"
  }
]
```

#### **Add IP Address**

**Endpoint:** `/ip/address`
**Method:** POST
**Example JSON Payload:**
```json
{
  "interface": "ether2",
  "address": "192.168.1.11/24"
}
```
**Expected Response:** Ok
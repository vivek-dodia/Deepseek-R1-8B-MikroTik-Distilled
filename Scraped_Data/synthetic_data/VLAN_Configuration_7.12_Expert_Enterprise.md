# VLAN Configuration in RouterOS 7.12

**Level:** Expert
**Network Scale:** Enterprise

## Configuration Scenario and Requirements

- Create VLANs for different network segments
- Configure inter-VLAN routing
- Ensure data isolation and security

## Step-by-Step Implementation

### 1. Create VLAN Interfaces

- Navigate to **Interfaces** > **VLAN**
- Click **+** to create a new VLAN interface

| Parameter | Explanation |
|---|---|
| Name | Unique name for the VLAN |
| Bridge | Interface to which VLAN is assigned |
| VLAN ID | VLAN identifier (range: 1-4094) |

**Example:**
```
/interface vlan add name=VLAN1 bridge=ether1 vlan-id=10
/interface vlan add name=VLAN2 bridge=ether2 vlan-id=20
```

### 2. Configure IP Addresses for VLANs

- Navigate to **IP** > **Addresses**
- Click **+** to add a new IP address

| Parameter | Explanation |
|---|---|
| Interface | VLAN interface to assign IP address |
| Address | IP address and subnet mask |
| Gateway | Default gateway (if necessary) |

**Example:**
```
/ip address add address=192.168.10.1/24 interface=VLAN1
/ip address add address=192.168.20.1/24 interface=VLAN2
```

### 3. Configure DHCP Server for VLANs

- Navigate to **IP** > **DHCP Server**
- Click **DHCP Setup** tab
- Check **Enabled** for the desired VLAN interface

**Example:**
```
/ip dhcp-server setup interface=VLAN1 enabled=yes
```

### 4. Configure Inter-VLAN Routing

- Navigate to **IP** > **Routes**
- Click **+** to add a new route

| Parameter | Explanation |
|---|---|
| Gateway | IP address of the router interface on the destination network |
| Destination | Network address and subnet mask |
| Interface | VLAN interface to use for routing |

**Example:**
```
/ip route add gateway=192.168.10.1 dst-address=192.168.20.0/24 interface=VLAN1
/ip route add gateway=192.168.20.1 dst-address=192.168.10.0/24 interface=VLAN2
```

## Complete Configuration Commands

```
/interface vlan add name=VLAN1 bridge=ether1 vlan-id=10
/interface vlan add name=VLAN2 bridge=ether2 vlan-id=20
/ip address add address=192.168.10.1/24 interface=VLAN1
/ip address add address=192.168.20.1/24 interface=VLAN2
/ip dhcp-server setup interface=VLAN1 enabled=yes
/ip route add gateway=192.168.10.1 dst-address=192.168.20.0/24 interface=VLAN1
/ip route add gateway=192.168.20.1 dst-address=192.168.10.0/24 interface=VLAN2
```

## Common Pitfalls and Solutions

- **VLAN ID Conflict:** Ensure VLAN IDs are unique across all interfaces.
- **Bridge Misconfiguration:** Verify that VLANs are assigned to the correct bridge interfaces.
- **IP Address Duplication:** Avoid duplicate IP addresses on different VLANs.
- **Improper Routing:** Check that routing rules are correctly configured to allow inter-VLAN communication.

## Verification and Testing Steps

- **Ping between VLANs:** Test connectivity between devices on different VLANs.
- **Trace Route:** Trace the network path between VLANs to identify any routing issues.
- **Security Audit:** Review access control lists and firewall rules to ensure data isolation.

## Related Features and Considerations

- **VLAN Tagging:** Configure VLAN tagging on switch ports to separate VLAN traffic.
- **Trunking:** Use trunk ports on switches to carry multiple VLANs over a single physical link.
- **Security:** Implement access control lists and firewall rules to restrict traffic between VLANs.
- **Performance Monitoring:** Monitor VLAN traffic load and latency for performance optimization.
## VLAN Configuration in MikroTik RouterOS 7.11 (Advanced)

### Configuration Scenario and Requirements

The goal is to configure VLANs on a MikroTik router to segment a network into multiple isolated logical networks. This guide assumes the use of RouterOS 7.11 and a basic understanding of VLAN concepts.

### Step-by-Step Implementation

**1. Create VLAN Interfaces**

- Navigate to **Interfaces > VLAN**
- Click **"+"** to add a new VLAN interface
- Configure the following parameters:

```
Name: VLAN_Name (e.g., VLAN10)
VLAN ID: 10
Interface: Choose the physical interface to which VLAN will belong
```

**2. Configure Switch Ports**

- Navigate to **Switch**
- Select the switch ports that will belong to the VLAN
- Select **VLAN ID** and choose the appropriate VLAN ID

**3. Configure IP Addresses and Routing**

- Assign IP addresses and configure routing to each VLAN:
- Navigate to **IP > Addresses**
- Click **"+"** to add a new IP address
- Configure the following parameters:

```
Interface: VLAN interface created
Address: IP address for the VLAN
Network: Subnet mask for the VLAN
```

- Navigate to **IP > Routes**
- Add static routes or configure dynamic routing to ensure inter-VLAN routing

### Complete Configuration Commands

```
/interface vlan add name=VLAN10 vlan-id=10 interface=ether1
/interface vlan add name=VLAN20 vlan-id=20 interface=ether2
/interface bridge port add bridge=bridge1 interface=ether1-VLAN10
/interface bridge port add bridge=bridge1 interface=ether2-VLAN20
/ip address add address=192.168.10.1/24 interface=VLAN10
/ip address add address=192.168.20.1/24 interface=VLAN20
/ip route add dst-address=192.168.20.0/24 gateway=192.168.10.1
/ip route add dst-address=192.168.10.0/24 gateway=192.168.20.1
```

### Common Pitfalls and Solutions

- **VLAN ID conflict:** Ensure that VLAN IDs do not overlap between different devices.
- **Trunk port misconfiguration:** Ensure that trunk ports on switches are properly configured to allow VLAN traffic.
- **IP address overlap:** Avoid using overlapping IP address ranges across VLANs.
- **Routing issues:** Verify that appropriate routes are configured for inter-VLAN communication.

### Verification and Testing Steps

- Check the status of VLAN interfaces: `/interface vlan print`
- Test inter-VLAN connectivity: Ping between devices on different VLANs
- Verify routing: `/ip route print`

### Related Features and Considerations

- **VLAN Trunking:** Configure a trunk port on a switch to allow multiple VLANs over a single physical link.
- **STP (Spanning Tree Protocol):** Use STP to prevent network loops when multiple paths exist between VLANs.
- **Security:** Consider implementing firewall rules to restrict access between VLANs.
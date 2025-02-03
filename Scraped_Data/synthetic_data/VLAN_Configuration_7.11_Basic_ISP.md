## VLAN Configuration in RouterOS 7.11 (Basic)

### Configuration Requirements

- MikroTik router with RouterOS 7.11 or higher
- VLAN-capable switches and devices

### Step-by-Step Implementation

**1. Create VLAN Interfaces**

- Navigate to `/interface/vlan` menu in Winbox.
- Click the "+" button to create a new VLAN interface.
- Specify the VLAN ID and the base interface it will use.

```
/interface/vlan add vlan-id=100 interface=ether1
/interface/vlan add vlan-id=200 interface=ether2
```

**2. Assign VLANs to Switch Ports**

- Configure VLAN-capable switches to assign ports to the created VLANs.

**3. Configure IP Addresses**

- Assign IP addresses to the VLAN interfaces.

```
/ip address add address=192.168.100.1/24 interface=vlan100
/ip address add address=192.168.200.1/24 interface=vlan200
```

**4. Enable Routing**

- Enable IP routing between VLANs by setting the `forward` parameter to `enabled` on the `/ip/route` menu.

### Complete Configuration Commands

```
/interface/vlan add vlan-id=100 interface=ether1
/interface/vlan add vlan-id=200 interface=ether2
/ip address add address=192.168.100.1/24 interface=vlan100
/ip address add address=192.168.200.1/24 interface=vlan200
/ip route add dst-address=0.0.0.0/0 gateway=none forward=enabled
```

### Common Pitfalls and Solutions

- **VLANs not communicating:** Ensure that VLANs are correctly configured on both the router and switches.
- **IP addresses not reachable:** Check that IP addresses are assigned to VLAN interfaces and that routing is enabled.
- **Incorrect VLAN tagging:** Verify that switch ports are configured with the correct VLAN tagging standards (e.g., 802.1Q).

### Verification and Testing Steps

- Verify VLAN interfaces are created and assigned to base interfaces.
- Use `ping` to test connectivity between devices on different VLANs.
- Inspect traffic using a packet sniffer to confirm VLAN tagging.

### Related Features and Considerations

- **VLAN Trunking:** Allows multiple VLANs to be transmitted over a single physical link.
- **MAC Address Passthrough:** Preserves MAC addresses across VLANs, simplifying device management.
- **Security:** Segregate network traffic by isolating VLANs, enhancing security.
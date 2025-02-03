## VLAN Configuration in RouterOS 7.12

### Configuration Scenario and Requirements

- Create multiple VLANs to segment the network traffic.
- Assign ports to specific VLANs.
- Configure inter-VLAN routing to allow communication between VLANs.

### Step-by-Step Implementation

#### 1. Create VLANs

```bash
/interface vlan add name=VLAN1 vid=10
/interface vlan add name=VLAN2 vid=20
```

#### 2. Assign Ports to VLANs

```bash
/interface ethernet set ether1 switch-port-vlan-member=VLAN1
/interface ethernet set ether2 switch-port-vlan-member=VLAN2
```

#### 3. Configure Inter-VLAN Routing

Enable IP forwarding:

```bash
/ip firewall filter add action=accept chain=forward
```

Create a virtual interface for inter-VLAN routing:

```bash
/interface bridge add name=vlan-bridge
```

Add VLAN interfaces to the bridge:

```bash
/interface bridge port add interface=VLAN1 bridge=vlan-bridge
/interface bridge port add interface=VLAN2 bridge=vlan-bridge
```

Assign an IP address to the bridge interface:

```bash
/ip address add address=192.168.1.1/24 interface=vlan-bridge
```

#### 4. Enable DHCP Server on VLANs

Optionally, you can enable DHCP servers on the VLANs:

```bash
/ip dhcp-server add lease-address-range=192.168.10.0/24 server=VLAN1
/ip dhcp-server add lease-address-range=192.168.20.0/24 server=VLAN2
```

### Complete Configuration Commands

```bash
/interface vlan add name=VLAN1 vid=10
/interface vlan add name=VLAN2 vid=20
/interface ethernet set ether1 switch-port-vlan-member=VLAN1
/interface ethernet set ether2 switch-port-vlan-member=VLAN2
/ip firewall filter add action=accept chain=forward
/interface bridge add name=vlan-bridge
/interface bridge port add interface=VLAN1 bridge=vlan-bridge
/interface bridge port add interface=VLAN2 bridge=vlan-bridge
/ip address add address=192.168.1.1/24 interface=vlan-bridge
```

### Common Pitfalls and Solutions

- **VLAN ID conflict:** Ensure that each VLAN has a unique VLAN ID (VID).
- **Port mismatch:** Verify that the ports assigned to VLANs are physically connected.
- **Incorrect bridge configuration:** Check that the VLAN interfaces are correctly added to the bridge.
- **Blocked traffic:** Ensure that the firewall allows traffic between VLANs.

### Verification and Testing Steps

- Ping between hosts on different VLANs.
- Use a VLAN-aware switch to verify that traffic is correctly tagged.
- Run sniffer tools (e.g., Wireshark) to analyze traffic flow.

### Related Features and Considerations

- **Security:** Enable VLAN trunking using IEEE 802.1Q standards to prevent unauthorized access between VLANs.
- **Scalability:** RouterOS supports a large number of VLANs, making it suitable for enterprise networks.
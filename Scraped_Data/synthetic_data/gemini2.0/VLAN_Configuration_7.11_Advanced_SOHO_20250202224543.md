## VLAN Configuration in RouterOS 7.11 (Advanced)

### Configuration Scenario and Requirements

In this scenario, we aim to set up VLANs on a MikroTik RouterOS device for network segmentation. We require:

- A RouterOS device with at least two physical interfaces.
- Network devices that support VLAN tagging (e.g., switches, servers).

### Step-by-Step Implementation

**1. Create VLAN Interfaces:**

```
/interface vlan add name=VLAN1 vlan-id=1
/interface vlan add name=VLAN2 vlan-id=2
```

**2. Assign Physical Interfaces to VLANs:**

```
/interface bridge add name=VLAN1-Bridge
/interface bridge port add bridge=VLAN1-Bridge interface=ether1 tagged=yes
/interface bridge add name=VLAN2-Bridge
/interface bridge port add bridge=VLAN2-Bridge interface=ether2 tagged=yes
```

**3. Configure IP Addresses on VLAN Interfaces:**

```
/ip address add address=192.168.1.1/24 interface=VLAN1
/ip address add address=192.168.2.1/24 interface=VLAN2
```

**4. Enable VLAN Tagging on Physical Interfaces:**

```
/interface ethernet switch port set ether1 vlan-mode=tagged vlan-header=yes
/interface ethernet switch port set ether2 vlan-mode=tagged vlan-header=yes
```

**5. Configure Firewall Rules:**

```
/ip firewall filter add chain=forward action=accept src-address=192.168.1.0/24 dst-address=192.168.2.0/24
/ip firewall filter add chain=forward action=accept src-address=192.168.2.0/24 dst-address=192.168.1.0/24
```

### Common Pitfalls and Solutions

- **VLAN ID Collision:** Ensure unique VLAN IDs are assigned to avoid conflicts.
- **Incorrect VLAN Tagging:** Verify that VLAN tagging is configured correctly on both the router and network devices.
- **Firewall Configuration:** Allow traffic between VLANs using appropriate firewall rules.

### Verification and Testing Steps

- Connect devices to the respective VLAN interfaces.
- Check IP connectivity between devices on different VLANs.
- Use tools like Wireshark to verify VLAN tagging.

### Related Features and Considerations

- **VLAN Trunks:** Use VLAN trunks to carry multiple VLANs over a single physical link.
- **DHCP Server:** Configure DHCP servers on VLAN interfaces to provide IP addresses to clients.
- **Security:** Implement VLANs to isolate and protect critical network segments.

### MikroTik REST API Examples

**1. Create VLAN Interface (POST):**

```
curl -X POST -H "Content-Type: application/json" -d "{ \"interface\": \"vlan\", \"name\": \"VLAN1\", \"vlan-id\": 1 }" http://192.168.88.1/rest/interface
```

**2. Assign Physical Interface to VLAN (POST):**

```
curl -X POST -H "Content-Type: application/json" -d "{ \"interface\": \"bridge-port\", \"bridge\": \"VLAN1-Bridge\", \"interface\": \"ether1\", \"tagged\": true }" http://192.168.88.1/rest/interface/bridge-port
```
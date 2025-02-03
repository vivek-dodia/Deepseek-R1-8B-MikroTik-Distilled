## VLAN Configuration in MikroTik RouterOS 6.48

### 1. Configuration Scenario and Requirements

#### Scenario:
Configure VLANs on a MikroTik router to segment a network into separate logical subnets.

#### Requirements:
- RouterOS 6.48 or later
- Enterprise-level network
- VLAN-aware switches

### 2. Step-by-Step Implementation

**Step 1: Create VLAN Interfaces**

```
/interface vlan add interface=eth1 name=VLAN10 vlan-id=10
/interface vlan add interface=eth1 name=VLAN20 vlan-id=20
```

**Step 2: Assign VLAN Interfaces to Ports**

```
/interface vlan add name=VLAN10 vlan-id=10 interface=ether1-port1
/interface vlan add name=VLAN20 vlan-id=20 interface=ether1-port2
```

**Step 3: Configure IP Addresses**

```
/ip address add address=10.0.10.1/24 interface=VLAN10
/ip address add address=10.0.20.1/24 interface=VLAN20
```

**Step 4: Configure Firewall Rules**

```
/ip firewall filter add chain=forward action=accept in-interface=VLAN10 out-interface=VLAN20
/ip firewall filter add chain=forward action=accept in-interface=VLAN20 out-interface=VLAN10
```

### 3. Complete Configuration Commands

- /interface vlan add interface=<physical interface> name=<VLAN name> vlan-id=<VLAN ID>
- /interface vlan add name=<VLAN name> vlan-id=<VLAN ID> interface=<VLAN interface>
- /ip address add address=<IP address/subnet> interface=<VLAN interface>
- /ip firewall filter add chain=forward action=accept in-interface=<Source VLAN> out-interface=<Destination VLAN>

### 4. Common Pitfalls and Solutions

- **VLAN ID Collision**: Ensure unique VLAN IDs on all interfaces.
- **Incorrect Interface Assignment**: Double-check the physical and VLAN interfaces assigned to ports.
- **Firewall Misconfiguration**: Verify that firewall rules allow communication between VLANs as needed.

### 5. Verification and Testing Steps

- **Check VLAN Interface Status**: Run `/interface vlan print` to ensure VLANs are up.
- **Test IP Connectivity**: Ping between devices on different VLANs.
- **Verify Firewall Rules**: Use the `/ip firewall filter print` command to confirm the presence of desired rules.

### 6. Related Features and Considerations

- **VLAN Trunking**: Use VLAN trunking to carry multiple VLANs over a single physical link.
- **MAC Address Learning**: Configure MAC address learning on VLAN interfaces to prevent broadcast traffic flooding.
- **VLAN Security**: Implement appropriate security measures, such as firewall rules and ACLs, to protect VLANs.
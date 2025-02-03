## Bridge Setup in RouterOS 7.12

### Configuration Scenario and Requirements

- Network topology: Multiple physical interfaces need to be combined into a single logical bridge for network segmentation.
- Configuration level: Advanced
- Network scale: Enterprise

### Step-by-Step Implementation

**1. Create the Bridge Interface**

```
/interface bridge add name=my-bridge
```

**2. Add Physical Interfaces to the Bridge**

```
/interface bridge port add bridge=my-bridge interface=ether1
/interface bridge port add bridge=my-bridge interface=ether2
```

**3. Configure Bridge Parameters (Optional)**

- **Spanning Tree Protocol (STP)**: Enable or disable spanning tree for loop prevention.
```
/interface bridge set my-bridge stp=yes
```
- **Port Isolation**: Isolate bridge ports to prevent inter-port communication.
```
/interface bridge port set my-bridge-port-1 isolation=yes
```
- **MAC Aging**: Define the time after which unused MAC addresses are removed from the bridge table.
```
/interface bridge set my-bridge mac-ageing-time=120s
```

**4. Assign IP Address to the Bridge Interface**

```
/ip address add address=192.168.10.1/24 interface=my-bridge
```

### Complete Configuration Commands

```
/interface bridge add name=my-bridge
/interface bridge port add bridge=my-bridge interface=ether1
/interface bridge port add bridge=my-bridge interface=ether2
/interface bridge set my-bridge stp=no
/interface bridge port set my-bridge-port-1 isolation=no
/interface bridge set my-bridge mac-ageing-time=300s
/ip address add address=192.168.10.1/24 interface=my-bridge
```

### Common Pitfalls and Solutions

- **STP loops**: Disable STP or configure proper STP parameters to prevent loops.
- **Port isolation**: Ensure that port isolation is not enabled when inter-port communication is required.
- **MAC address conflicts**: Check for duplicate MAC addresses on connected devices to avoid network inconsistencies.

### Verification and Testing Steps

- Check the bridge interface configuration:
```
/interface bridge print
```
- Test connectivity between devices connected to the bridge:
```
ping 192.168.10.2
```
- Use a network monitoring tool (e.g., Wireshark) to verify traffic flow through the bridge.

### Related Features and Considerations

- **VLANs**: Use VLANs within the bridge to segment traffic further.
- **HW Acceleration**: Enable hardware acceleration for improved performance on supported devices.
- **Security**: Configure firewall rules and other security measures on the bridge interface.
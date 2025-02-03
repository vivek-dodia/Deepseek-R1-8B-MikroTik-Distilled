## Bridge Setup in RouterOS 7.12

### Configuration Scenario and Requirements

- Create a Layer 2 bridge to connect multiple physical ports on a RouterBoard.
- Establish connectivity between devices connected to the bridged ports.
- Ensure traffic does not leak outside the bridge.

### Step-by-Step Implementation

**1. Define the Bridge**

```
/interface bridge add name="Bridge-Name"
```

**2. Add Physical Ports to the Bridge**

```
/interface bridge port add bridge=Bridge-Name interface=ether1
/interface bridge port add bridge=Bridge-Name interface=ether2
```

**3. Disable Spanning Tree Protocol (STP)**

 STP prevents loops in Layer 2 networks. Disable it on the bridge to avoid unnecessary overhead.

```
/interface bridge set Bridge-Name spanning-tree-protocol=no
```

### Complete Configuration Commands

```
/interface bridge add name="Bridge-Name"
/interface bridge port add bridge=Bridge-Name interface=ether1
/interface bridge port add bridge=Bridge-Name interface=ether2
/interface bridge set Bridge-Name spanning-tree-protocol=no
```

### Common Pitfalls and Solutions

- **STP Configuration:** Ensure STP is disabled on the bridge to avoid potential issues with device discovery and connectivity.
- **Port Misconfiguration:** Verify that the physical ports being bridged are actually connected to the devices you intend to connect.
- **Firewall Rules:** Check if any firewall rules are blocking traffic between the bridged ports. Create necessary firewall rules to allow cross-bridge traffic.

### Verification and Testing Steps

- **Ping Test:** Ping devices connected to different bridged ports to verify connectivity.
- **Traffic Sniffing:** Use a tool like Wireshark to capture traffic on the bridge interface. Ensure no traffic is being leaked outside the bridge.
- **Loop Test:** Attempt to create a loop by connecting one of the bridged ports back to the bridge itself. Verify that no traffic is passed through the loop.

### Related Features and Considerations

- **VLAN Bridging:** RouterOS supports bridging of VLANs. Configure VLANs on the physical ports and bridge them for inter-VLAN communication.
- **Security:** Consider applying firewall rules on the bridge interface to restrict access and prevent unauthorized devices from joining the bridge.
- **Port Forwarding:** Port forwarding rules cannot be applied directly to bridged ports. Use IP addresses of specific devices on the bridge for port forwarding.
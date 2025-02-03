## Bridge Setup in RouterOS 6.48 (6.x or 7.x)

### Configuration Scenario and Requirements

**Goal:** Establish a bridge interface to connect multiple physical interfaces and extend the Layer 2 network.

**Requirements:**

- RouterOS device with version 6.48 or higher
- Multiple physical interfaces (e.g., ethernet1, ethernet2)

### Step-by-Step Implementation

**1. Create the Bridge Interface:**

```
/interface bridge add
```

**2. Add Interfaces to the Bridge:**

```
/interface bridge port add bridge=<bridge-name> interface=<interface-name>
```
**Example:**

```
/interface bridge port add bridge=br-lan interface=ethernet1
/interface bridge port add bridge=br-lan interface=ethernet2
```

**3. Configure Bridge Parameters (Optional):**

- **STP (Spanning Tree Protocol):** Controls bridge behavior in network loops.
```
/interface bridge set bridge=<bridge-name> stp=enabled
```
- **Protocol Mode:** Determines the spanning tree mode used.
```
/interface bridge set bridge=<bridge-name> protocol-mode=stp
```

### Complete Configuration Commands

```
/interface bridge add
/interface bridge port add bridge=<bridge-name> interface=ethernet1
/interface bridge port add bridge=<bridge-name> interface=ethernet2
/interface bridge set bridge=<bridge-name> stp=enabled
/interface bridge set bridge=<bridge-name> protocol-mode=stp
```

### Common Pitfalls and Solutions

- **Duplicate Port Assignment:** Ensure each physical interface is added to only one bridge.
- **STP Configuration:** Set STP parameters to prevent bridge loops and ensure network stability.
- **Bridge Name Collision:** Avoid using bridge names that already exist on the network.

### Verification and Testing Steps

- **Ping:** Test communication between devices connected to the bridge.
```
/ip neighbor print
```
- **Bridge Status:** Check the bridge status and port connectivity.
```
/interface bridge print
```

### Related Features and Considerations

**VLAN Support:** Bridges can be used to create VLANs and isolate network traffic.

**MAC Address Learning:** Bridges learn MAC addresses of connected devices and create a MAC forwarding table.

**Network Security:** Bridges do not provide any network security features. Consider implementing firewall rules and VLANs for security.

**STP Best Practices:**

- Enable STP to prevent broadcast storms and network loops.
- Select appropriate STP topology and parameters based on the network requirements.
- Use a network management tool or monitoring software to track STP topology changes.
## Bridge Setup in RouterOS 7.11

**Configuration Level:** Advanced

**Network Scale:** SOHO

### 1. Configuration Scenario and Requirements

**Scenario:**
- Create a bridge interface to connect multiple physical interfaces and allow devices connected to them to communicate with each other.

**Requirements:**
- Two or more physical interfaces (e.g., Ethernet, VLAN)
- Access to RouterOS CLI

### 2. Step-by-Step Implementation

**Steps:**

1. **Create the Bridge Interface:**
```
/interface bridge add
```

2. **Add Physical Interfaces to the Bridge:**
```
/interface bridge port add interface=ether1 bridge=bridge1
/interface bridge port add interface=ether2 bridge=bridge1
```

3. **Enable Bridging:**
```
/interface bridge set bridge1 enabled=yes
```

### 3. Complete Configuration Commands

| Command | Description |
|---|---|
| `/interface bridge add` | Creates a new bridge interface. |
| `/interface bridge port add` | Adds a physical interface to the bridge. |
| `/interface bridge set enabled=yes` | Enables bridging on the bridge interface. |

### 4. Common Pitfalls and Solutions

- **Interface not added to bridge:** Verify that the physical interface is available and correctly configured.
- **Bridge not enabled:** Ensure that the `enabled` parameter is set to `yes` in the `/interface bridge set` command.
- **Devices not communicating:** Check that all devices are properly connected to the bridge interfaces and have valid IP addresses.

### 5. Verification and Testing Steps

- **Verify Bridge Creation:**
```
/interface bridge print
```

- **Test Connectivity:**
Ping devices connected to different physical interfaces within the bridge.

### 6. Related Features and Considerations

- **VLAN Trunking:** Bridges can support VLAN trunking, allowing multiple VLANs to be transmitted over a single physical link.
- **Spanning Tree Protocol (STP):** STP can be enabled to prevent bridge loops and ensure network stability.
- **Security:** Secure the bridge interface with firewall rules to prevent unauthorized access.
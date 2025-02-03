## Bridge Setup in RouterOS 6.x/7.x

### Configuration Scenario and Requirements

- **Goal:** Create a bridge to connect multiple physical interfaces for Layer 2 communication.
- **Network Scale:** ISP
- **Configuration Level:** Basic

### Step-by-Step Implementation

**1. Enable Bridging on Interfaces**

- Navigate to **Interfaces** > **All**.
- Select the interfaces you want to bridge (e.g., ether1, ether2).
- Click **Bridge** > **Create** in the **Bridge** menu.

**2. Configure the Bridge**

- Navigate to **Bridges** > **Bridges**.
- Click **+** to create a new bridge.
- Enter a name for the bridge (e.g., "MyBridge").
- Select the interfaces added to the bridge under **Ports**.

**3. Optional: Disable MAC Learning**

- If necessary, disable MAC learning on the bridge to improve performance.
- Navigate to **Bridges** > **MyBridge** > **Ports**.
- Uncheck **Enable MAC Learning**.

**4. Optional: Configure STP (Spanning Tree Protocol)**

- If necessary, configure Spanning Tree Protocol (STP) to prevent bridging loops.
- Navigate to **Bridges** > **MyBridge** > **STP**.
- Configure STP parameters (e.g., Priority, Hello Time).

**Complete Configuration Commands:**

```text
/interface bridge add name=MyBridge
/interface bridge port add bridge=MyBridge interface=ether1
/interface bridge port add bridge=MyBridge interface=ether2
```

### Common Pitfalls and Solutions

- Ensure that all ports added to the bridge are in the same Layer 2 broadcast domain.
- If experiencing bridging issues, check MAC learning and STP settings.
- Verify that the bridge is enabled and the ports are properly assigned.

### Verification and Testing Steps

- Use the `/bridge print` command to display the bridge configuration.
- Use the `/ip arp print` command to verify MAC address forwarding across the bridge.
- Send Layer 2 traffic between devices connected to the bridged interfaces.

### Related Features and Considerations

- **VLANs:** Bridges can be used to segment Layer 2 networks using VLANs.
- **Security:** Consider applying firewall rules or Layer 2 isolation mechanisms to secure the bridged network.
- **Performance:** Optimize bridge performance by disabling unnecessary features such as MAC learning.
## Bridge Setup in RouterOS 7.12 (Basic)

### Configuration Scenario

Create a bridge to connect multiple physical interfaces and bridge their traffic.

### Step-by-Step Implementation

**1. Create the Bridge**

- Navigate to **Interfaces** > **Bridge** and click **+**.
- Enter a **Name** for the bridge (e.g., "br0").
- Select the **Bridge ports** by dragging and dropping the required interfaces onto the "Bridge Interfaces" list.

**2. Enable the Bridge**

- Click **Apply** to save the changes.
- Select the bridge and click **Enable**.

### Complete Configuration Commands

```
/interface bridge add name=br0
/interface bridge port add bridge=br0 interface=ether1
/interface bridge port add bridge=br0 interface=ether2
/interface bridge enable name=br0
```

### Common Pitfalls and Solutions

- **Loop formation:** Avoid connecting a bridge port to a port that is already part of the bridge.
- **SPAN port inclusion:** Ensure that SPAN ports are not included in the bridge.

### Verification and Testing Steps

- Verify that the bridge is enabled (`/interface bridge print where name=br0`).
- Test connectivity between hosts connected to the bridged interfaces.

### Related Features and Considerations

- **STP (Spanning Tree Protocol):** Enable STP to prevent bridging loops (`/interface bridge set bridge=br0 stp-enabled=yes`).
- **VLANs:** Bridges can be used to isolate VLANs. Assign VLANs to bridge ports using `/interface bridge port vlan add`.
- **Security:** Implement security measures such as firewall rules to protect the bridge.
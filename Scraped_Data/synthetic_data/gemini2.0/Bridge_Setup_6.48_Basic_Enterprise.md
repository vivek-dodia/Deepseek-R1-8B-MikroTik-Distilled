**Bridge Setup in RouterOS 6.48**

**Level:** Basic
**Network Scale:** SMB/Enterprise

## Configuration Scenario and Requirements

To create a bridge, we need multiple physical interfaces connected to the same switch or subnet. Each interface will be added to the bridge, and all traffic passing through it will be bridged.

## Step-by-Step Implementation

1. **Create a Bridge Interface:**
   - Go to **Interfaces** > **Bridge** > **+**
   - Enter a name for the bridge (e.g., "Bridge-1")
2. **Add Interfaces to the Bridge:**
   - Click on the "Add" button under "Ports"
   - Select the interfaces you want to bridge (e.g., ether1, ether2)
3. **Set Bridge Parameters:**
   - **Bridge MAC:** Leave it as default to auto-generate a MAC address for the bridge.
   - **STP**: Disable or enable Spanning Tree Protocol as needed.
4. **Apply Configuration:**
   - Click on the "Apply" button to save the configuration.

## Complete Configuration Commands

```
/interface bridge add name=Bridge-1
/interface bridge port add interface=ether1 bridge=Bridge-1
/interface bridge port add interface=ether2 bridge=Bridge-1
```

## Common Pitfalls and Solutions

- **Interface not Available:** Ensure that the interfaces you want to bridge are physically connected and enabled.
- **STP Loops:** Enable STP if experiencing bridge loops or forwarding issues.
- **MAC Address Conflict:** Avoid using the same MAC address for multiple bridges.

## Verification and Testing Steps

- Check the **Interfaces** > **Bridge** menu to verify that the bridge is created and interfaces are added.
- Ping between devices connected to different interfaces on the bridge to ensure traffic is being forwarded.
- Use **/interface bridge print** to view bridge statistics and status.

## Related Features and Considerations

- **VLANs:** Bridges can be used to create VLANs by isolating traffic from different subnets.
- **Port Isolation:** Configure port isolation on the bridge to prevent devices on different interfaces from communicating directly.
- **Security:** Consider using security filters on the bridge interface to protect the network from unauthorized access.
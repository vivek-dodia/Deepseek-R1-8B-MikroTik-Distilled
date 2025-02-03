## Bridge Setup in RouterOS

### Configuration Scenario and Requirements

- Create a bridge between two physical interfaces to extend the same LAN segment.
- Enable bridging on two Gigabit Ethernet interfaces (ether1 and ether2).
- Configure the bridge with a static MAC address for redundancy.

### Step-by-Step Implementation

1. **Create a bridge interface:**
   ```
   /interface bridge add name=bridge1
   ```

2. **Add physical interfaces to the bridge:**
   ```
   /interface bridge port add bridge=bridge1 interface=ether1
   /interface bridge port add bridge=bridge1 interface=ether2
   ```

3. **Enable bridging:**
   ```
   /interface bridge enable bridge=bridge1
   ```

4. **Configure bridge MAC address:**
   ```
   /interface bridge set bridge=bridge1 mac-address=01:02:03:04:05:06
   ```

### Complete Configuration Commands

```
/interface bridge add name=bridge1
/interface bridge port add bridge=bridge1 interface=ether1
/interface bridge port add bridge=bridge1 interface=ether2
/interface bridge enable bridge=bridge1
/interface bridge set bridge=bridge1 mac-address=01:02:03:04:05:06
```

### Common Pitfalls and Solutions

- **Incorrect interface names:** Double-check the names of the physical interfaces being added to the bridge.
- **Bridge disabled:** Ensure bridging is enabled with `/interface bridge enable bridge=bridge1`.
- **VLAN mismatch:** Verify that all interfaces in the bridge are assigned to the same VLAN, if applicable.

### Verification and Testing Steps

1. **Check bridge status:**
   ```
   /interface bridge print
   ```

2. **Test connectivity:**
   - Connect devices to the bridge and verify communication within the same LAN segment.

### Related Features and Considerations

- **VLAN Tagging:** If using VLANs, bridge ports can be configured with VLAN ID parameters.
- **Spanning Tree Protocol (STP):** Enables loop prevention in bridged networks.
- **Bridge Firewall:** Provides basic firewall functionality for the bridge.
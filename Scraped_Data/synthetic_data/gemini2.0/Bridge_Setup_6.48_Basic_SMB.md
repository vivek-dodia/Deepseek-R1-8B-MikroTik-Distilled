## Bridge Setup in MikroTik RouterOS 6.48 (Basic)

### Configuration Scenario and Requirements

- Create a bridge interface to connect multiple physical interfaces.
- Bridge ports should handle incoming and outgoing traffic between connected devices.

### Step-by-Step Implementation

1. **Create a New Bridge Interface:**

   ```bash
   /interface bridge add name=my-bridge
   ```

2. **Add Ports to the Bridge:**

   - For each interface you want to bridge, run the following command:
   
   ```bash
   /interface bridge port add bridge=my-bridge interface=<interface-name>
   ```
   
   - Replace `<interface-name>` with the name of the physical interface to add to the bridge.

### Complete Configuration Commands

```bash
/interface bridge add name=my-bridge
/interface bridge port add bridge=my-bridge interface=ether1
/interface bridge port add bridge=my-bridge interface=ether2
```

### Common Pitfalls and Solutions

- **Incorrect Interface Names:** Ensure the interface names in the `bridge port` commands match the actual physical interfaces.
- **No IP Address on Bridge:** By default, a bridge interface does not have an IP address. Assign an IP address if necessary using `ip address`.

### Verification and Testing Steps

1. Verify the bridge creation using:
   
   ```bash
   /interface bridge print
   ```

2. Ping between devices connected to the bridged ports (if IP addresses are assigned).

### Related Features and Considerations

- **VLAN Tagging:** VLANs can be used to segment traffic on the bridge using the `/interface bridge port vlan` command.
- **Spanning Tree Protocol (STP):** STP can be enabled to prevent loops in the network topology using `/interface bridge settings set spanning-tree=stp`.
- **Security:** Consider implementing firewall rules to control traffic between bridged interfaces if required.
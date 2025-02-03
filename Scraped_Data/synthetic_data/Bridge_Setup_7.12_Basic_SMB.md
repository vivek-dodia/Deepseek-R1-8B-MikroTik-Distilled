## Bridge Setup in MikroTik RouterOS

### Configuration Scenario and Requirements

- Create a simple bridged network between two or more Ethernet interfaces.
- Connect devices to the bridge and allow them to communicate as if they were on the same physical segment.

### Step-by-Step Implementation

#### Basic Level

1. Create a new bridge:
   ```
   /interface bridge add name=bridge1
   ```

2. Add Ethernet interfaces to the bridge:
   ```
   /interface bridge port add bridge=bridge1 interface=ether1
   /interface bridge port add bridge=bridge1 interface=ether2
   ```

#### Advanced Level

- Modify bridge properties (e.g., spanning tree mode, age time):
   ```
   /interface bridge set bridge1 spanning-tree-protocol=rstp age-time=300
   ```

- Disable/enable bridging for specific ports:
   ```
   /interface bridge port set bridge1-ether1 disabled=yes
   ```

#### Expert Level

- Use VLAN tagging on bridges:
   ```
   /interface bridge vlan add bridge=bridge1 vlan-id=10 name=vlan11
   /interface bridge port set bridge1-ether1 vlan-mode=trunk vlan-ids=10
   ```

- Configure MAC address filtering on bridges:
   ```
   /interface bridge mac-filter add bridge=bridge1 mac-address=00:00:00:00:00:01
   ```

### Complete Configuration Commands

- Create a bridge:
   ```
   /interface bridge add name=<bridge-name>
   ```

- Add an interface to a bridge:
   ```
   /interface bridge port add bridge=<bridge-name> interface=<interface-name>
   ```

- Modify bridge properties:
   ```
   /interface bridge set <bridge-name> <property>=<value>
   ```

- Disable/enable port bridging:
   ```
   /interface bridge port set <bridge-name>-<interface-name> disabled=<yes/no>
   ```

### Common Pitfalls and Solutions

- **Cannot ping devices on the bridged network:**
  - Verify that the bridge is created and the interfaces are added correctly.
  - Check for any firewall rules or security settings that may block traffic.

- **High CPU usage on the bridge:**
  - Disable unnecessary features on the bridge (e.g., spanning tree, MAC filtering).
  - Upgrade to a more powerful router if possible.

### Verification and Testing Steps

- Ping between devices connected to the bridged interfaces.
- Use Wireshark or similar tools to monitor traffic flow across the bridge.

### Related Features and Considerations

- **Port Security:** Configure MAC address filtering on bridge ports to restrict unauthorized device access.
- **VLAN Trunking:** Use VLAN tagging to segment traffic on the bridge and create isolated virtual networks.
- **STP:** Prevent bridging loops using the Spanning Tree Protocol (STP).
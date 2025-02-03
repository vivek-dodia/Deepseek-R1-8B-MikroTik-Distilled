## Bridge Setup in RouterOS 6.48

### Configuration Scenario and Requirements

- Create a bridge interface to connect multiple physical interfaces together.
- Configure the bridge interface with appropriate settings.
- Assign IP addresses to the bridge interface for network connectivity.
- Verify the bridge configuration and troubleshoot any issues.

### Step-by-Step Implementation

1. **Create the Bridge Interface:**
   - Navigate to Interfaces > Bridge
   - Click the "+" button to create a new bridge.
   - Enter a name for the bridge, e.g., "MyBridge."

2. **Add Physical Interfaces to the Bridge:**
   - Select the bridge created in step 1.
   - Click the "Ports" tab.
   - Select the physical interfaces you want to add to the bridge.

3. **Configure Bridge Settings:**
   - Navigate to the "General" tab.
   - Set the "STP" option to "yes" to enable Spanning Tree Protocol.
   - Set the "Ageing Time" to 300 seconds to refresh MAC address entries every 5 minutes.
   - Set the "Learning" option to "yes" to learn MAC addresses from incoming packets.

4. **Assign IP Address to the Bridge:**
   - Navigate to the "Address" tab.
   - Enter the IP address and subnet mask for the bridge.
   - Click the "Apply" button to save the changes.

### Complete Configuration Commands

```
/interface bridge add name=MyBridge
/interface bridge port add bridge=MyBridge interface=ether1
/interface bridge port add bridge=MyBridge interface=ether2
/interface bridge settings set bridge=MyBridge stp=yes ageing-time=300 learning=yes
/ip address add address=192.168.1.1/24 interface=MyBridge
```

### Common Pitfalls and Solutions

- **Bridge Not Working:** Verify that the physical interfaces are properly connected and enabled.
- **No IP Connectivity:** Ensure that the IP address assigned to the bridge is correct and in the correct subnet.
- **STP Loops:** Ensure that the STP settings are correct and that there are no loops in the network topology.

### Verification and Testing Steps

1. **Check Bridge Status:** Navigate to Interfaces > Bridge and verify that the bridge is created and active.
2. **Test Connectivity:** Ping the IP address assigned to the bridge to test network connectivity.

### Related Features and Considerations

- **VLANs:** Bridges can be used to create virtual LANs (VLANs) for traffic segmentation.
- **Hardware Offloading:** Some MikroTik routers support hardware offloading for bridging, which can improve performance.
- **Security:** Consider using firewall rules to restrict access to the bridge interface.

### MikroTik REST API Examples

**Endpoint:** `/interface/bridge`

**Request Method:** GET

**Example JSON Payload:**

```json
{
  "bridge": "MyBridge",
  "interface": "ether1"
}
```

**Expected Response:**

```json
{
  "interface": "ether1",
  "bridge": "MyBridge",
  "path-cost": "100",
  "priority": "128"
}
```
**Request Method:** POST

**Example JSON Payload:**

```json
{
  "name": "MyBridge",
  "st-ageing-time": "300s",
  "st-learning": "yes",
  "st-path-cost": "100",
  "st-priority": "128"
}
```

**Expected Response:**

```json
{
  "name": "MyBridge",
  "st-ageing-time": "300s",
  "st-learning": "yes",
  "st-path-cost": "100",
  "st-priority": "128",
  "st-state": "disabled"
}
```
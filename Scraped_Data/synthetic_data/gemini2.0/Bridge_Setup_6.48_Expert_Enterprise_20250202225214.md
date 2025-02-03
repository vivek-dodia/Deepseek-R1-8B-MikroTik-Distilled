**Bridge Setup in RouterOS 6.48**

**Configuration Level:** Expert

**Network Scale:** Enterprise

## 1. Configuration Scenario and Requirements
- Create a bridge interface with multiple physical ports.
- Assign IP addresses and firewall rules to the bridge.
- Verify connectivity and troubleshoot any issues.

## 2. Step-by-Step Implementation
1. **Create the Bridge**
   ```
   /interface bridge add name=my-bridge
   ```
2. **Add Physical Ports**
   ```
   /interface bridge port add bridge=my-bridge interface=ether1
   /interface bridge port add bridge=my-bridge interface=ether2
   ```
3. **Assign IP Address**
   ```
   /ip address add address=192.168.1.1/24 interface=my-bridge
   ```
4. **Configure Firewall**
   ```
   /ip firewall filter add action=accept chain=input dst-address=192.168.1.0/24
   /ip firewall filter add action=accept chain=output src-address=192.168.1.0/24
   ```

## 3. Complete Configuration Commands
```
/interface bridge add name=my-bridge
/interface bridge port add bridge=my-bridge interface=ether1
/interface bridge port add bridge=my-bridge interface=ether2
/ip address add address=192.168.1.1/24 interface=my-bridge
/ip firewall filter add action=accept chain=input dst-address=192.168.1.0/24
/ip firewall filter add action=accept chain=output src-address=192.168.1.0/24
```

## 4. Common Pitfalls and Solutions
- **Ports not added:** Ensure that the physical ports you wish to bridge are added to the bridge using `/interface bridge port`.
- **IP address conflict:** Verify that the IP address assigned to the bridge does not conflict with any other IP addresses on the network.
- **Firewall rules incorrect:** Ensure that the firewall rules allow traffic to flow correctly across the bridge.

## 5. Verification and Testing Steps
- Verify bridge creation: `/interface bridge print`
- Test connectivity: Ping from a device connected to the bridge to an external IP address.
- Check firewall rules: `/ip firewall filter print`

## 6. Related Features and Considerations
- You can add VLANs to the bridge for network segmentation.
- You can enable Spanning Tree Protocol (STP) on the bridge for redundancy.
- Consider using bridge groups for managing multiple bridges.

## 7. MikroTik REST API Examples
**API Endpoint:** `/interface/bridge`
**Request Method:** GET
**Example JSON Payload:**
```
{}
```
**Expected Response:**
```
[
  {
    "enabled": true,
    "mtu": 1500,
    "name": "my-bridge",
    "ports": [
      {
        "bridge": "my-bridge",
        "enabled": true,
        "interface": "ether1",
        "path-cost": 1
      },
      {
        "bridge": "my-bridge",
        "enabled": true,
        "interface": "ether2",
        "path-cost": 1
      }
    ]
  }
]
```
## Bridge Setup in MikroTik RouterOS 6.48

**Level:** Advanced

**Network Scale:** SMB

### Configuration Scenario and Requirements

- Create a bridge interface to connect multiple Ethernet ports.
- Configure the bridge with IP addressing and DHCP server.
- Allow devices connected to the bridge to communicate with each other.

### Step-by-Step Implementation

**1. Create the Bridge Interface**

```
/interface bridge add name=bridge1
```

**2. Add Ports to the Bridge**

```
/interface bridge port add bridge=bridge1 interface=ether1
/interface bridge port add bridge=bridge1 interface=ether2
```

**3. Configure IP Addressing for the Bridge**

```
/ip address add address=10.0.0.1/24 interface=bridge1
```

**4. Enable DHCP Server on the Bridge**

```
/ip dhcp-server add interface=bridge1 address-pool=pool1
```

### Complete Configuration Commands

```
/interface bridge add name=bridge1
/interface bridge port add bridge=bridge1 interface=ether1
/interface bridge port add bridge=bridge1 interface=ether2
/ip address add address=10.0.0.1/24 interface=bridge1
/ip dhcp-server add interface=bridge1 address-pool=pool1
```

### Common Pitfalls and Solutions

- **Bridge Interface Not Active:** Ensure that the bridge interface is enabled (e.g., `/interface bridge set bridge1 disabled=no`).
- **IP Address Conflict:** Check for conflicting IP addresses on the bridge or connected devices.
- **No Communication Between Devices:** Verify that the bridge is forwarding traffic properly and that firewall rules do not block communication.

### Verification and Testing Steps

- **Ping:** Test communication between devices connected to the bridge.
- **DHCP Assignment:** Connect a client to the bridge and confirm that it receives an IP address from the DHCP server.
- **Web Access:** If applicable, test if devices can access external websites.

### Related Features and Considerations

- **VLANs:** Bridges can be used to create VLANs for isolating traffic on different ports.
- **Security:** Consider applying firewall rules to restrict traffic flow and protect the network.
- **Performance:** Bridge performance can be affected by factors such as the number of ports and traffic load.

### MikroTik REST API Example

**Endpoint:** `/interface/bridge`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "name": "bridge1",
  "interfaces": ["ether1", "ether2"]
}
```

**Expected Response:**

```json
{
  "id": "5",
  "disabled": false,
  "forward-delay": 0,
  "interfaces": [
    "ether1",
    "ether2"
  ],
  "name": "bridge1"
}
```
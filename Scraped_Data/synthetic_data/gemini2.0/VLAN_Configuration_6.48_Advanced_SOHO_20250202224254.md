## VLAN Configuration in RouterOS 6.48

### Configuration Scenario and Requirements

* Create VLANs for different departments or services (e.g., voice, data, management).
* Isolate traffic between VLANs for security and performance purposes.
* Use MikroTik RouterBOARD devices to implement the VLAN configuration.

### Step-by-Step Implementation

1. **Create the VLAN Interfaces:**

   ```
   /interface vlan add name=vlan10 id=10
   /interface vlan add name=vlan20 id=20
   ```

2. **Assign Physical Ports to the VLANs:**

   ```
   /interface bridge port add bridge=bridge1 interface=ether1 pvid=10
   /interface bridge port add bridge=bridge1 interface=ether2 pvid=20
   ```

3. **Enable Inter-VLAN Routing:**

   ```
   /ip routing add dst-address=10.0.10.0/24 gateway=192.168.1.1
   /ip routing add dst-address=10.0.20.0/24 gateway=192.168.2.1
   ```

4. **Configure DHCP Servers for Each VLAN:**

   ```
   /ip dhcp-server add interface=vlan10 address-pool=vlan10-pool
   /ip dhcp-server add interface=vlan20 address-pool=vlan20-pool
   ```

5. **Configure Firewall Rules to Isolate VLANs:**

   ```
   /ip firewall filter add chain=input in-interface=vlan10 action=accept
   /ip firewall filter add chain=input in-interface=vlan20 action=accept
   /ip firewall filter add chain=forward src-address=10.0.10.0/24 dst-address=10.0.20.0/24 action=drop
   ```

### Complete Configuration Commands

```
/interface vlan add name=vlan10 id=10
/interface vlan add name=vlan20 id=20
/interface bridge port add bridge=bridge1 interface=ether1 pvid=10
/interface bridge port add bridge=bridge1 interface=ether2 pvid=20
/ip routing add dst-address=10.0.10.0/24 gateway=192.168.1.1
/ip routing add dst-address=10.0.20.0/24 gateway=192.168.2.1
/ip dhcp-server add interface=vlan10 address-pool=vlan10-pool
/ip dhcp-server add interface=vlan20 address-pool=vlan20-pool
/ip firewall filter add chain=input in-interface=vlan10 action=accept
/ip firewall filter add chain=input in-interface=vlan20 action=accept
/ip firewall filter add chain=forward src-address=10.0.10.0/24 dst-address=10.0.20.0/24 action=drop
```

### Common Pitfalls and Solutions

* **VLAN IDs not unique:** Ensure that VLAN IDs are unique and non-overlapping.
* **Physical ports not assigned:** Verify that physical ports are correctly assigned to the VLANs.
* **Firewall rules not applied:** Check that firewall rules are correctly configured to block inter-VLAN traffic.
* **DHCP servers not active:** Ensure that DHCP servers are active and serving the correct VLANs.

### Verification and Testing Steps

* **Test connectivity within each VLAN:** Ping devices within each VLAN to verify connectivity.
* **Test connectivity between VLANs:** Try to ping across VLANs. If traffic is blocked, check firewall rules.
* **Check DHCP lease distribution:** Monitor DHCP leases to ensure clients are receiving IP addresses from the correct VLANs.

### Related Features and Considerations

* **VLAN Tagging:** Enable VLAN tagging on physical ports to pass VLAN traffic.
* **Trunk Ports:** Use trunk ports to connect multiple VLANs to a single switch port.
* **Security:** Implement VLANs in conjunction with firewall rules to enhance network security.

### MikroTik REST API Examples

**API Endpoint:** `/interface/vlan`

**Request Method:** GET

**Example JSON Payload:**

```json
{ }
```

**Expected Response:**

```json
[
  {
    "interface": "vlan1",
    "name": "Voice VLAN",
    "id": 10,
    "enabled": true
  },
  {
    "interface": "vlan2",
    "name": "Data VLAN",
    "id": 20,
    "enabled": true
  }
]
```
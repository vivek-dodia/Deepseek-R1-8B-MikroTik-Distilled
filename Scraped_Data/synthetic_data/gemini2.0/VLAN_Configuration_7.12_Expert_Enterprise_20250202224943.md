## VLAN Configuration on MikroTik RouterOS

### Configuration Scenario and Requirements

* Configure multiple VLANs on a MikroTik router to isolate and segment different parts of the network.
* The router is running RouterOS 7.12 (6.x or 7.x).
* The VLANs will be used to separate different departments within a large enterprise network.

### Step-by-Step Implementation

#### 1. Create the VLANs

```
/interface vlan add name=VLAN10 id=10
/interface vlan add name=VLAN20 id=20
```

#### 2. Assign VLANs to Interfaces

Assign the VLANs to the interfaces that will connect to the devices in each VLAN.

```
/interface bridge port add bridge=bridge1 interface=ether1 untagged-vlan=VLAN10
/interface bridge port add bridge=bridge2 interface=ether2 untagged-vlan=VLAN20
```

#### 3. Create VLAN Subinterfaces

Create subinterfaces on the VLANs to provide separate IP addresses for the VLANs.

```
/ip address add address=10.10.10.1/24 interface=VLAN10
/ip address add address=10.20.20.1/24 interface=VLAN20
```

#### 4. Enable DHCP on VLAN Subinterfaces

Enable DHCP on the VLAN subinterfaces to automatically assign IP addresses to devices connected to the VLANs.

```
/ip dhcp-server add address-pool=VLAN10-pool interface=VLAN10 range=10.10.10.100-10.10.10.200
/ip dhcp-server add address-pool=VLAN20-pool interface=VLAN20 range=10.20.20.100-10.20.20.200
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN10 id=10
/interface vlan add name=VLAN20 id=20
/interface bridge port add bridge=bridge1 interface=ether1 untagged-vlan=VLAN10
/interface bridge port add bridge=bridge2 interface=ether2 untagged-vlan=VLAN20
/ip address add address=10.10.10.1/24 interface=VLAN10
/ip address add address=10.20.20.1/24 interface=VLAN20
/ip dhcp-server add address-pool=VLAN10-pool interface=VLAN10 range=10.10.10.100-10.10.10.200
/ip dhcp-server add address-pool=VLAN20-pool interface=VLAN20 range=10.20.20.100-10.20.20.200
```

### Common Pitfalls and Solutions

* **VLAN ID Conflict:** Ensure that the VLAN IDs you assign are unique across the network.
* **Incorrect Interface Assignment:** Double-check that the interfaces are assigned to the correct VLANs.
* **VLAN Hopping:** Configure firewall rules to prevent devices from communicating across VLANs without authorization.

### Verification and Testing Steps

* Use the `/interface vlan print` command to verify the VLAN configuration.
* Connect devices to the VLANs and verify that they can communicate with devices within the same VLAN.
* Test the DHCP functionality by connecting a client to the VLAN and checking if it receives an IP address from the DHCP server.

### Related Features and Considerations

* **VLAN Trunking:** Allows for multiple VLANs to be carried over a single physical trunk link.
* **VLAN Routing:** Configure routing between VLANs to enable communication between different departments.
* **Security:** Implement security measures such as access control lists (ACLs) and firewall rules to protect VLANs from unauthorized access.

### MikroTik REST API Examples

#### Create a VLAN

**Endpoint:** `/api/interface/vlan`

**Request Method:** POST

**JSON Payload:**

```json
{
  "name": "VLAN10",
  "id": 10
}
```

**Expected Response:**

```json
{
  "id": 10,
  "name": "VLAN10"
}
```

#### Assign a VLAN to an Interface

**Endpoint:** `/api/interface/bridge/port`

**Request Method:** POST

**JSON Payload:**

```json
{
  "bridge": "bridge1",
  "interface": "ether1",
  "untagged-vlan": "VLAN10"
}
```

**Expected Response:**

```json
{
  "id": 10,
  "bridge": "bridge1",
  "interface": "ether1",
  "untagged-vlan": "VLAN10"
}
```
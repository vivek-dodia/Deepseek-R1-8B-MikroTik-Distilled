### VLAN Configuration in MikroTik RouterOS 6.48

#### Configuration Scenario and Requirements

* **Objective:** Create and configure VLANs on a MikroTik router to segment the network and provide logical isolation.
* **Network Setup:**
    * MikroTik router running RouterOS 6.48
    * Multiple physical interfaces (ethernet or wireless)

#### Step-by-Step Implementation

**1. Create VLAN Interface:**

```
/interface vlan add name=VLAN1 vlan-id=10
/interface vlan add name=VLAN2 vlan-id=20
```

**2. Assign VLANs to Physical Interfaces:**

```
/interface bridge port add bridge=bridge1 interface=ether1 vlan-mode=tagged vlan-ids=10,20
/interface bridge port add bridge=bridge1 interface=ether2 vlan-mode=tagged vlan-ids=10
```

**3. Define VLAN Untagged Interface:**

```
/interface bridge port add bridge=bridge1 interface=ether3 vlan-mode=untagged vlan-id=10
```

**4. Enable VLAN Routing:**

```
/ip routing add dst-address=10.0.10.0/24 gateway=10.1.1.1 interface=VLAN1
/ip routing add dst-address=10.0.20.0/24 gateway=10.1.2.1 interface=VLAN2
```

**5. Add Firewall Rules:**

```
/ip firewall filter add action=accept src-address=10.0.10.0/24 dst-address=10.0.20.0/24
/ip firewall filter add action=accept src-address=10.0.20.0/24 dst-address=10.0.10.0/24
```

**6. Assign IP Addresses to VLAN Interfaces:**

```
/ip address add address=10.1.1.1/24 interface=VLAN1
/ip address add address=10.1.2.1/24 interface=VLAN2
```

#### Common Pitfalls and Solutions

* **VLAN ID Overlap:** Ensure that the VLAN IDs used on different interfaces do not overlap.
* **Untagged Traffic:** Specify the untagged VLAN ID for the interface where untagged traffic is expected.
* **Forgetting Firewall Rules:** Remember to allow traffic between VLANs using firewall rules.
* **Incorrect Interface Assignments:** Double-check that the physical interfaces are assigned to the correct VLANs and bridges.

#### Verification and Testing Steps

* Use the `/interface vlan print` command to verify VLAN creation and configuration.
* Test connectivity between hosts in different VLANs using ping or traceroute.
* Check the firewall logs to ensure traffic is being allowed as expected.

#### Related Features and Considerations

* VLAN Trunking: Configure VLAN trunking between switches to extend VLANs across multiple devices.
* MAC Learning: Enable MAC learning on VLAN interfaces to prevent MAC address flooding.
* DHCP Server: Use the DHCP server in RouterOS to assign IP addresses to hosts in specific VLANs.

#### MikroTik REST API Example

**Endpoint:** `/interface/vlan`
**Request Method:** POST
**Request Payload (JSON):**

```
{
  "name": "VLAN3",
  "vlan-id": 30
}
```

**Expected Response (JSON):**

```
{
  "id": 3
}
```

This API call creates a new VLAN interface named "VLAN3" with a VLAN ID of 30.
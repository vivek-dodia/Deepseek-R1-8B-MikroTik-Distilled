## VLAN Configuration in MikroTik RouterOS 7.12 for ISPs

### Configuration Scenario and Requirements

* VLANs to be configured for Customer Premises Equipment (CPE) and ISP core network.
* VLANs to provide isolation and security between customer traffic.
* VLANs to be tagged on the last mile fiber connection.

### Step-by-Step Implementation

**1. Create VLANs**

- Navigate to `/interface vlan`
- Click the `+` button to create a new VLAN.
- Enter the VLAN ID (e.g., 100, 200)
- Repeat for all required VLANs.

**2. Tag VLANs on Interfaces**

- Navigate to `/interfaces`
- Select the last mile fiber interface (e.g., ethernet1)
- Click on the `VLAN` tab
- Enable the VLAN and select the required VLANs.
- Repeat for other interfaces that require VLAN tagging.

**3. Bridge VLAN Interfaces**

- Navigate to `/interfaces bridge`
- Click on the `+` button to create a new bridge.
- Add the tagged VLAN interfaces to the bridge.
- Define a bridge port for the uplink to the ISP core network (e.g., bridge-local)

**4. Define DHCP Server for VLANs**

- Navigate to `/ip dhcp-server`
- Click on the `+` button to create a new DHCP Server.
- Select the bridge interface created in step 3.
- Configure IP pool, lease time, and other DHCP settings.
- Repeat for each VLAN that requires DHCP services.

**5. Firewall Rules**

- Navigate to `/ip firewall filter`
- Create firewall rules to allow traffic between the VLANs and the ISP core network.

**6. VLAN Configuration Overview**

```
/interface vlan
  add name=vlan100 vlan-id=100
  add name=vlan200 vlan-id=200
  add name=vlan300 vlan-id=300

/interfaces
  configure bridge=bridge-local
    add port=ethernet1 vlan=vlan100 tagged
    add port=ethernet2 vlan=vlan200 tagged
    add port=ethernet3 vlan=vlan300 tagged

/ip dhcp-server
  add interface=bridge-local dhcp-option=router address-pool=dhcp-pool1
  add interface=bridge-local dhcp-option=dns-server address-pool=dhcp-pool2

/ip firewall filter
  add chain=input action=accept src-address=192.168.1.0/24 dst-address=192.168.2.0/24
  add chain=input action=accept src-address=192.168.2.0/24 dst-address=192.168.1.0/24
```

### Common Pitfalls and Solutions

* **VLAN ID Conflict:** Ensure that the VLAN IDs used on different interfaces do not overlap.
* **Untagged Traffic:** Verify that untagged traffic is allowed on the last mile fiber connection.
* **Misconfigured Firewall Rules:** Ensure that firewall rules allow traffic between the VLANs as intended.
* **Spanning Tree Issues:** Consider using Spanning Tree Protocol (STP) to prevent loops on the VLAN-tagged interfaces.

### Verification and Testing Steps

* Verify VLAN functionality by pinging between hosts on different VLANs.
* Check DHCP server operation by requesting an IP address on each VLAN.
* Test firewall rules by sending traffic between the VLANs and the ISP core network.

### Related Features and Considerations

* **VLAN Trunking:** Use VLAN Trunking Protocol (VTP) to propagate VLAN information across multiple MikroTik devices.
* **Static VLAN Assignments:** Assign VLANs to specific ports instead of tagging on interfaces.
* **Security:** Implement appropriate security measures such as access control lists (ACLs) and intrusion detection/prevention systems (IDS/IPS).
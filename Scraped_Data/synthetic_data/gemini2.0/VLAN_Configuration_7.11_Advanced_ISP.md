## VLAN Configuration in RouterOS 7.11

### Configuration Scenario and Requirements

* Create VLANs for different network segments, such as data, voice, and management.
* Allow inter-VLAN routing while isolating traffic between VLANs.
* Configure trunk interfaces to carry tagged traffic from multiple VLANs.
* Implement security measures to prevent unauthorized access to VLANs.

### Step-by-Step Implementation

**1. Create VLANs**

```
/interface vlan add name=data vlan-id=10
/interface vlan add name=voice vlan-id=20
/interface vlan add name=management vlan-id=30
```

**2. Assign VLANs to Interfaces**

```
/interface ethernet set ether1 tagged-vlan=data
/interface ethernet set ether2 tagged-vlan=voice
/interface ethernet set ether3 tagged-vlan=management
```

**3. Create VLAN Interface**

```
/interface vlan add name=trunk
```

**4. Add VLANs to Trunk Interface**

```
/interface vlan-member add parent=trunk member=data
/interface vlan-member add parent=trunk member=voice
/interface vlan-member add parent=trunk member=management
```

**5. Enable VLAN Tagging on Trunk Ports**

```
/interface ethernet set ether1 trunk-port-tag=10,20,30
/interface ethernet set ether2 trunk-port-tag=10,20,30
/interface ethernet set ether3 trunk-port-tag=10,20,30
```

**6. Configure Firewall Rules (Optional)**

```
/ip firewall filter add chain=forward dst-address-list=vlan-data-restricted action=drop
/ip firewall filter add chain=forward src-address-list=vlan-data-restricted action=drop
```

### Complete Configuration Commands

The following commands will create and configure the VLANs, VLAN interface, and trunk ports:

```
/interface vlan add name=data vlan-id=10
/interface vlan add name=voice vlan-id=20
/interface vlan add name=management vlan-id=30
/interface ethernet set ether1 tagged-vlan=data
/interface ethernet set ether2 tagged-vlan=voice
/interface ethernet set ether3 tagged-vlan=management
/interface vlan add name=trunk
/interface vlan-member add parent=trunk member=data
/interface vlan-member add parent=trunk member=voice
/interface vlan-member add parent=trunk member=management
/interface ethernet set ether1 trunk-port-tag=10,20,30
/interface ethernet set ether2 trunk-port-tag=10,20,30
/interface ethernet set ether3 trunk-port-tag=10,20,30
/ip firewall filter add chain=forward dst-address-list=vlan-data-restricted action=drop
/ip firewall filter add chain=forward src-address-list=vlan-data-restricted action=drop
```

### Common Pitfalls and Solutions

* **VLAN ID Conflicts:** Ensure that each VLAN has a unique ID.
* **Tagging Misconfiguration:** Verify that tagging is correctly configured on all affected interfaces.
* **Firewall Oversights:** Enable firewall rules to prevent unauthorized access between VLANs.
* **Trunk Port Configuration Errors:** Use the correct commands and parameters to configure trunk ports.

### Verification and Testing Steps

* Use the `/interface vlan print` command to list VLANs and their configurations.
* Verify that tagged traffic is passing through trunk ports using a packet analyzer.
* Test inter-VLAN routing by pinging devices from different VLANs.
* Check firewall logs to ensure that unauthorized access is blocked.

### Related Features and Considerations

* **VLAN Trunks:** Allows VLAN traffic to be carried on a single physical link.
* **VLAN Snooping:** Provides Layer 2 forwarding of VLAN-tagged frames between switches.
* **VLAN Filtering:** Restricts access to specific VLANs based on device MAC addresses or other parameters.
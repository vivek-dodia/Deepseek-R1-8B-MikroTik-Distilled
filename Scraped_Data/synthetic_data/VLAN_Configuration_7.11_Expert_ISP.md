## VLAN Configuration in MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

* Implement VLANs on a MikroTik router to segment network traffic and isolate devices.
* Assign VLANs to specific physical ports or logical interfaces.
* Allow communication between VLANs as needed.

### Implementation

**Step 1: Create VLANs**

```
/vlan add name=VLAN1 interface=ether1
/vlan add name=VLAN2 interface=ether2
```

**Step 2: Assign Ports to VLANs**

```
/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=1
/interface bridge port add bridge=bridge2 interface=ether2 vlan-id=2
```

**Step 3: Allow Inter-VLAN Communication (Optional)**

```
/ip firewall layer3 add action=accept chain=forward in-interface-list=bridge1 out-interface-list=bridge2
/ip firewall layer3 add action=accept chain=forward in-interface-list=bridge2 out-interface-list=bridge1
```

### Complete Configuration Commands

**VLAN Creation:**

| Parameter | Description |
|---|---|
| `name` | Name of the VLAN |
| `interface` | Physical or logical interface to assign to the VLAN |

**Port Assignment:**

| Parameter | Description |
|---|---|
| `bridge` | Name of the bridge to which the port will be added |
| `interface` | Physical or logical interface to be added |
| `vlan-id` | VLAN ID to be assigned to the port |

**Inter-VLAN Communication:**

| Parameter | Description |
|---|---|
| `action` | Action to take for traffic matching the rule |
| `chain` | Chain in which to add the rule |
| `in-interface-list` | List of input interfaces to which the rule applies |
| `out-interface-list` | List of output interfaces to which the rule applies |

### Pitfalls and Solutions

* **Error: Unable to create VLAN:** Ensure that the specified interface is available and not already assigned to a VLAN.
* **Error: Port cannot be assigned to VLAN:** Check that the port is a member of the correct bridge and that the VLAN ID is valid.
* **Error: No communication between VLANs:** Verify that inter-VLAN communication rules are properly configured and that no other firewall rules are blocking traffic.

### Verification and Testing

* Check the VLAN list using `/vlan print`.
* Use `/interface bridge port print` to confirm port assignments.
* Test communication between VLANs by pinging devices on different VLANs.

### Related Features and Considerations

* **VLAN Tagging:** Ensure that devices connected to VLAN ports are configured with the correct VLAN tags.
* **Security:** Implement access control lists (ACLs) to restrict traffic between VLANs and protect against unauthorized access.
* **Monitoring:** Use tools like SNMP or NetFlow to monitor VLAN traffic and identify performance issues.
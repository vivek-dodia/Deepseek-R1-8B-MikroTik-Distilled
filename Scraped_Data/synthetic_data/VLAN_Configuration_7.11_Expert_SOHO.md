**VLAN Configuration in MikroTik RouterOS 7.11**

**Configuration Scenario and Requirements**

* Configure VLANs to segregate traffic on a MikroTik router.
* Create multiple isolated VLANs for different network segments.
* Assign VLANs to specific physical interfaces and configure inter-VLAN routing.

**Step-by-Step Implementation**

**1. Create VLAN Interfaces**

```
/interface vlan add name=VLAN1 vlan-id=1
/interface vlan add name=VLAN2 vlan-id=2
```

**2. Assign VLAN Interfaces to Physical Ports**

```
/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=1
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=2
```

**3. Enable Inter-VLAN Routing**

```
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1 vlan=VLAN1
/ip route add dst-address=0.0.0.0/0 gateway=192.168.2.1 vlan=VLAN2
```

**4. Configure Firewall Rules (optional)**

```
/ip firewall filter add chain=forward src-address=VLAN1 dst-address=VLAN2 action=accept
/ip firewall filter add chain=forward src-address=VLAN2 dst-address=VLAN1 action=accept
```

**Common Pitfalls and Solutions**

* **Incorrect VLAN ID:** Ensure the VLAN IDs specified in the commands are valid (1-4094).
* **Duplicate VLAN Assignment:** Avoid assigning the same VLAN ID to multiple physical ports.
* **Missing Inter-VLAN Routing:** Verify that appropriate IP routes are configured to allow communication between VLANs.
* **Firewall Blocking:** If firewall rules are enabled, ensure they allow traffic between the configured VLANs.

**Verification and Testing Steps**

* Ping between hosts on different VLANs to verify connectivity.
* Use a VLAN-aware switch to connect devices to the router's VLAN interfaces.
* Check firewall logs to verify that traffic is flowing as expected.

**Related Features and Considerations**

* **VLAN Tagging:** RouterOS supports both tagged and untagged VLAN traffic.
* **MAC Learning:** The router automatically learns MAC addresses on VLAN interfaces.
* **Security:** VLANs provide network isolation, but additional security measures such as firewall rules may be required.

**Complete Configuration Commands**

```
/interface vlan add name=VLAN1 vlan-id=1
/interface vlan add name=VLAN2 vlan-id=2

/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=1
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=2

/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1 vlan=VLAN1
/ip route add dst-address=0.0.0.0/0 gateway=192.168.2.1 vlan=VLAN2

/ip firewall filter add chain=forward src-address=VLAN1 dst-address=VLAN2 action=accept
/ip firewall filter add chain=forward src-address=VLAN2 dst-address=VLAN1 action=accept
```
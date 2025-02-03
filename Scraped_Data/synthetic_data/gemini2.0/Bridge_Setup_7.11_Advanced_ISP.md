## Bridge Setup in MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

* Configuring a bridge interface to connect multiple physical interfaces as a single logical interface.
* Enabling bridging functionalities like MAC learning, filtering, and forwarding between connected interfaces.

### Step-by-Step Implementation

**1. Create a Bridge Interface**

```
/interface bridge add name=myBridge
```

**2. Add Physical Interfaces to the Bridge**

```
/interface bridge set myBridge ports=ether1,ether2
```

### Complete Configuration Commands

```
/interface bridge add name=myBridge
/interface bridge set myBridge ports=ether1,ether2
```

### Common Pitfalls and Solutions

* **Ensure interfaces are in the same Layer 2 network:** The interfaces you add to the bridge must be in the same subnet or VLAN.
* **Avoid loopback configurations:** Do not add the bridge interface back to itself as a port, as this can cause loops and network instability.
* **Consider security implications:** Bridging can expose all connected interfaces to each other, so consider implementing firewall rules to control traffic flow.

### Verification and Testing Steps

* Check the bridge interface status with `/interface bridge print`. It should show as "running".
* Use `/interface bridge port print` to view the interfaces connected to the bridge.
* Test connectivity between devices connected to different bridge ports.

### Related Features and Considerations

* **MAC Address Filtering:** Use `/interface bridge filter` to set up MAC filtering rules for the bridge interface.
* **Spanning Tree Protocol:** Enable STP on the bridge to prevent network loops (`/interface bridge port set ether1 stp=yes`).
* **VLANs on Bridges:** Create VLAN sub-interfaces on the bridge to segment traffic into virtual networks (`/interface vlan add parent=myBridge name=VLAN10`).
* **Bonding:** Use bridging to create bonded interfaces for increased bandwidth and redundancy (`/interface bridge add mode=bond name=myBond ports=ether1,ether2`).
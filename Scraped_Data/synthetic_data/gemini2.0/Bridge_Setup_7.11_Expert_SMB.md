## Bridge Setup in RouterOS 7.11

### Configuration Scenario and Requirements

* Create a bridge to connect multiple physical interfaces and form a single logical interface.
* Configure VLANs on the bridge to isolate traffic.
* Enable Spanning Tree Protocol (STP) to prevent loops and ensure network stability.

### Step-by-Step Implementation

**Step 1: Create a Bridge**

```
/interface bridge add name=MyBridge
```

**Step 2: Add Interfaces to the Bridge**

```
/interface bridge port add bridge=MyBridge interface=ether1
/interface bridge port add bridge=MyBridge interface=ether2
```

**Step 3: Configure VLANs**

```
/interface vlan add name=VLAN10 vlan-id=10 bridge=MyBridge
/interface vlan add name=VLAN20 vlan-id=20 bridge=MyBridge
```

**Step 4: Enable STP**

```
/interface bridge settings set bridge=MyBridge stp-enable=yes stp-type=rstp
```

**Step 5: Assign VLANs to Interfaces**

```
/interface vlan member add interface=ether1 vlan=VLAN10
/interface vlan member add interface=ether2 vlan=VLAN20
```

### Complete Configuration Commands

```
/interface bridge add name=MyBridge
/interface bridge port add bridge=MyBridge interface=ether1
/interface bridge port add bridge=MyBridge interface=ether2
/interface vlan add name=VLAN10 vlan-id=10 bridge=MyBridge
/interface vlan add name=VLAN20 vlan-id=20 bridge=MyBridge
/interface bridge settings set bridge=MyBridge stp-enable=yes stp-type=rstp
/interface vlan member add interface=ether1 vlan=VLAN10
/interface vlan member add interface=ether2 vlan=VLAN20
```

### Common Pitfalls and Solutions

* **STP Loops:** Ensure that interfaces connected to the bridge are in different physical segments to avoid loops.
* **VLAN Misconfiguration:** Verify that VLAN IDs are unique within the bridge and that interfaces are assigned to the correct VLANs.
* **STP Delay:** STP can introduce latency in the network. Adjust the STP parameters if necessary to optimize performance.

### Verification and Testing Steps

* Check the bridge status: `/interface bridge print`
* Test connectivity between VLANs: Send pings from devices connected to different VLANs.
* Examine the STP status: `/interface bridge settings print default`

### Related Features and Considerations

* **Bonding:** Combine multiple physical interfaces into a single logical bond to increase bandwidth and redundancy.
* **Spanning Tree Modes:** Choose the appropriate STP mode based on the size and topology of the network.
* **Security:** Secure the bridge by using firewall rules and access control lists to prevent unauthorized access.
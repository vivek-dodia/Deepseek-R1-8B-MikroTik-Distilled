## Bridge Setup in MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

- Create a bridge interface to connect two or more LAN segments.
- Configure bridge ports to include the connected interfaces.
- Enable spanning tree protocol (STP) to prevent broadcast storms.

### Step-by-Step Implementation

**Step 1: Create a Bridge Interface**

```
/interface bridge add name=my-bridge
```

- `name` parameter: Specifies the name of the bridge interface.

**Step 2: Configure Bridge Ports**

Add the physical interfaces (LAN ports) to the bridge:

```
/interface bridge port add interface=ether1 bridge=my-bridge
/interface bridge port add interface=ether2 bridge=my-bridge
```

- `interface` parameter: Specifies the physical interface to add.
- `bridge` parameter: Specifies the bridge interface to which the port is added.

**Step 3: Enable Spanning Tree Protocol**

```
/bridge setting set stp-enable=yes
/bridge setting set forward-delay=15
/bridge setting set hold-time=1
```

- `stp-enable` parameter: Enables STP.
- `forward-delay` parameter: Configures the time (in seconds) to wait before forwarding traffic after a topology change.
- `hold-time` parameter: Configures the time (in seconds) that the bridge will wait for a bridge hello packet before declaring the bridge as down.

### Complete Configuration Commands

```
/interface bridge add name=my-bridge
/interface bridge port add interface=ether1 bridge=my-bridge
/interface bridge port add interface=ether2 bridge=my-bridge
/bridge setting set stp-enable=yes
/bridge setting set forward-delay=15
/bridge setting set hold-time=1
```

### Common Pitfalls and Solutions

- **STP Loop:** Ensure that there is only one active STP instance in the network. Disable STP on any redundant bridges.
- **Incorrect Bridge Ports:** Verify that all necessary interfaces are added as ports to the bridge interface.
- **STP Configuration Errors:** Choose appropriate STP settings based on the network topology and requirements.

### Verification and Testing Steps

- Check the bridge interface status: `/interface bridge print`
- Verify bridge port membership: `/interface bridge port print`
- Enable STP logging to monitor STP activity: `/logging add topics=stp`
- Test connectivity between devices connected to the bridge: Ping between hosts on different bridge ports.

### Related Features and Considerations

- **Port Isolation:** Enable bridge port isolation to prevent communication between hosts connected to different bridge ports.
- **VLAN Tagging:** Configure VLAN tagging on the bridge and bridge ports to support multiple VLANs over the same physical infrastructure.
- **HW Offloading:** If supported by the hardware, enable HW offloading for the bridge to improve performance.
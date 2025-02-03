## Bridge Setup in RouterOS 6.x/7.x

### Configuration Scenario and Requirements

**Objective:** Create a bridge interface to connect multiple physical interfaces and allow traffic flow between them.

**Requirements:**

- MikroTik router with RouterOS 6.x or 7.x
- Physical interfaces connected to the router
- IP addresses assigned to the bridge interface (optional)

### Step-by-Step Implementation

#### 1. Create the Bridge Interface

```
/interface bridge add name=my-bridge
```

#### 2. Add Physical Interfaces to the Bridge

**Using the CLI:**

```
/interface bridge port add bridge=my-bridge interface=ether1
/interface bridge port add bridge=my-bridge interface=ether2
```

**Using Winbox GUI:**

- Go to **Interfaces** > **Bridge**
- Click **+** and select the bridge interface
- Add physical interfaces by clicking **+** and selecting them

#### 3. Configure IP Address (Optional)

To assign an IP address to the bridge interface:

```
/ip address add address=192.168.1.1/24 interface=my-bridge
```

#### 4. Enable Bridging

By default, bridging is disabled. To enable it:

```
/bridge enable default=yes
```

### Complete Configuration Commands

```
/interface bridge add name=my-bridge
/interface bridge port add bridge=my-bridge interface=ether1
/interface bridge port add bridge=my-bridge interface=ether2
/ip address add address=192.168.1.1/24 interface=my-bridge
/bridge enable default=yes
```

### Common Pitfalls and Solutions

- **Looping:** Ensure that the ports added to the bridge are not connected to each other, as this can create a loop.
- **IP Conflict:** If multiple IP addresses are assigned to the bridge, conflicts may occur. Verify that only one IP address is assigned.
- **Incorrect Interface Names:** Use the correct physical interface names when adding them to the bridge.

### Verification and Testing Steps

- Check the status of the bridge interface using `/interface bridge print`.
- Verify that packets are flowing between the bridged interfaces by using ping or traceroute.
- Confirm that the IP address is assigned correctly if configured.

### Related Features and Considerations

- **VLANs:** Bridges can be used to create VLANs by adding subinterfaces to the bridge.
- **Spanning Tree Protocol (STP):** STP can be configured on bridges to prevent network loops.
- **Security:** Use **/ip firewall** and **/interface firewall** rules to control traffic flow on the bridge.
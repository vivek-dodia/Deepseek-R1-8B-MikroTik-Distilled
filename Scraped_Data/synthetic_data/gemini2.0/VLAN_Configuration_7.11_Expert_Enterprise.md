## VLAN Configuration on MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

Suppose you have an enterprise network with multiple departments and require logical segmentation to isolate specific network sections. This can be achieved by configuring VLANs (Virtual Local Area Networks) on your MikroTik RouterOS router to create virtual, isolated network segments on a single physical network infrastructure.

### Step-by-Step Implementation

#### 1. Create a VLAN Bridge

```
/interface bridge add name=VLAN-Bridge
```

This command creates a virtual bridge called `VLAN-Bridge` that will serve as the backbone for VLANs.

#### 2. Create VLAN Interfaces

For each VLAN you want to configure, create a VLAN interface under the VLAN bridge.

```
/interface vlan add interface=Ethernet1-1 name=VLAN10 vlan-id=10
```

This command creates a VLAN interface named `VLAN10` with VLAN ID `10` on the `Ethernet1-1` physical interface. Replace `Ethernet1-1` with the actual physical interface name.

#### 3. Assign VLAN Interfaces to Ports

Assign specific physical ports to VLANs by adding them to VLAN interface interfaces.

```
/interface vlan-port add interface=VLAN10 ether1 port=ether2
```

This command assigns the `ether2` port to the `VLAN10` interface. Repeat this step for each port you want to assign to a VLAN.

#### 4. Configure IP Addressing for VLAN Interfaces

Configure IP addresses and subnets for each VLAN interface as needed.

```
/ip address add address=192.168.10.1/24 interface=VLAN10
```

This command assigns the IP address `192.168.10.1` with a subnet mask of `/24` to the `VLAN10` interface.

### Complete Configuration Commands

```
/interface bridge add name=VLAN-Bridge
/interface vlan add interface=Ethernet1-1 name=VLAN10 vlan-id=10
/interface vlan-port add interface=VLAN10 ether1 port=ether2
/ip address add address=192.168.10.1/24 interface=VLAN10
```

### Common Pitfalls and Solutions

- **VLAN IDs Conflict:** Ensure that VLAN IDs do not overlap with other VLANs on the same network.
- **Port Membership Error:** Verify that ports assigned to VLANs are physically connected.
- **IP Address Conflict:** Ensure that IP addresses assigned to VLAN interfaces do not conflict with other network devices.

### Verification and Testing Steps

- Check the VLAN bridge and interface configurations:
    - `/interface bridge print`
    - `/interface vlan print`
- Test connectivity between devices in different VLANs:
    - Ping from one VLAN interface to another.
- Verify IP address configurations:
    - `/ip address print detail`

### Related Features and Considerations

- **Port-based VLAN:** Assigning ports to VLANs is a common practice called Port-based VLAN.
- **MAC-based VLAN:** You can configure VLAN membership based on MAC addresses using the command `/interface vlan mac-vlan`.
- **Security:** Implementing VLANs enhances network security by isolating traffic between different network segments.
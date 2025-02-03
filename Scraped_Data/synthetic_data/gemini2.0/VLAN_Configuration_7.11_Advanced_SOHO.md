## VLAN Configuration in RouterOS 7.11 for SOHO Networks

### Configuration Scenario and Requirements

**Objective:** Configure a VLAN on a MikroTik router to logically separate devices within a single physical network.

**Requirements:**
- MikroTik router running RouterOS 7.11 or later
- Physical interfaces to support VLAN traffic (e.g., Ethernet ports)

### Step-by-Step Implementation

**1. Create the VLAN Interface:**

```
/interface vlan add name=VLAN-ID vlan-id=VLAN-ID
```

**Example:**
```
/interface vlan add name=VLAN10 vlan-id=10
```

**2. Assign VLAN Interface to Physical Interface:**

```
/interface bridge port add bridge=bridge-name interface=interface-name pvid=VLAN-ID
```

**Example:**
```
/interface bridge port add bridge=LAN1 interface=ether1 pvid=10
```

**3. Configure IP Address and Gateway on VLAN Interface:**

```
/ip address add address=IP-address/mask-length interface=VLAN-ID
```

**Example:**
```
/ip address add address=192.168.10.1/24 interface=VLAN10
```

### Complete Configuration Commands

- VLAN Interface Creation:
```
/interface vlan add name=VLAN-ID vlan-id=VLAN-ID
```

- VLAN Interface Assignment to Physical Interface:
```
/interface bridge port add bridge=bridge-name interface=interface-name pvid=VLAN-ID
```

- IP Address Configuration on VLAN Interface:
```
/ip address add address=IP-address/mask-length interface=VLAN-ID
```

### Common Pitfalls and Solutions

**Pitfall:** VLAN not working after configuration
**Solution:** Ensure the physical interface is correctly assigned to the bridge and has the correct PVID.

**Pitfall:** Unable to access devices on different VLANs
**Solution:** Verify that the router is routing traffic between the VLANs.

### Verification and Testing Steps

**1. Check VLAN Interface Status:**

```
/interface vlan print
```

**2. Check Physical Interface Bridge Port Membership:**

```
/interface bridge port print
```

**3. Ping Devices on Different VLANs:**

```
/ping destination-ip-address interface=VLAN-ID
```

### Related Features and Considerations

- **VLAN Trunks:** Allow multiple VLANs to be transmitted over a single physical link.
- **VLAN Tagging:** Adds a tag to Ethernet frames to indicate the VLAN membership.
- **Security:** VLANs can enhance network security by isolating different groups of devices.
- **Scalability:** VLANs enable flexible network expansion without the need for physical reconfiguration.
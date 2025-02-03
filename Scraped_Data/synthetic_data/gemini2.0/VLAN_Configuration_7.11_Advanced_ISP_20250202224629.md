## VLAN Configuration in RouterOS 7.11 (Advanced)

**1. Configuration Scenario and Requirements**

- Configure multiple VLANs on a MikroTik router to segment a network.
- Each VLAN will have its own subnet and Layer 2 isolation.
- Use a trunk port to connect the router to a switch that will provide VLAN tagging.

**2. Step-by-Step Implementation**

**a. Create VLANs**

```
/interface vlan add name=VLAN1 interface=ether1-gateway vlan-id=1
/interface vlan add name=VLAN2 interface=ether1-gateway vlan-id=2
```

**b. Assign IP Addresses to VLANs**

```
/ip address add address=192.168.1.1/24 interface=VLAN1
/ip address add address=192.168.2.1/24 interface=VLAN2
```

**c. Configure Trunk Port**

On the switch:
```
configure terminal
interface ether1
switchport mode trunk
switchport trunk allowed vlan 1,2
```

On the MikroTik router:
```
/interface ethernet set ether1-gateway switch-mode trunk
/interface ethernet trunk set ether1-gateway allowed-trunks=1,2
```

**d. Create VLAN Interfaces**

```
/interface vlan add name=vlan1-1 interface=VLAN1 arp=disabled
/interface vlan add name=vlan1-2 interface=VLAN1 arp=disabled
/interface vlan add name=vlan2-1 interface=VLAN2 arp=disabled
/interface vlan add name=vlan2-2 interface=VLAN2 arp=disabled
```

**e. Assign IP Addresses to VLAN Interfaces**

```
/ip address add address=192.168.1.2/24 interface=vlan1-1
/ip address add address=192.168.1.3/24 interface=vlan1-2
/ip address add address=192.168.2.2/24 interface=vlan2-1
/ip address add address=192.168.2.3/24 interface=vlan2-2
```

**3. Complete Configuration Commands**

```
/interface vlan add name=VLAN1 interface=ether1-gateway vlan-id=1
/interface vlan add name=VLAN2 interface=ether1-gateway vlan-id=2

/ip address add address=192.168.1.1/24 interface=VLAN1
/ip address add address=192.168.2.1/24 interface=VLAN2

/interface ethernet set ether1-gateway switch-mode trunk
/interface ethernet trunk set ether1-gateway allowed-trunks=1,2

/interface vlan add name=vlan1-1 interface=VLAN1 arp=disabled
/interface vlan add name=vlan1-2 interface=VLAN1 arp=disabled
/interface vlan add name=vlan2-1 interface=VLAN2 arp=disabled
/interface vlan add name=vlan2-2 interface=VLAN2 arp=disabled

/ip address add address=192.168.1.2/24 interface=vlan1-1
/ip address add address=192.168.1.3/24 interface=vlan1-2
/ip address add address=192.168.2.2/24 interface=vlan2-1
/ip address add address=192.168.2.3/24 interface=vlan2-2
```

**4. Common Pitfalls and Solutions**

- Ensure that the switch port is configured for trunk mode and allowed VLANs.
- **Error: Interface has no VLAN support.**
  - Solution: Check that the interface is properly configured as a VLAN interface (e.g., /interface vlan).
- **Error: Address already in use.**
  - Solution: Check that the assigned IP addresses are unique within the network.

**5. Verification and Testing Steps**

- Check the VLAN configuration using `/interface vlan print`.
- Assign devices to VLANs and check connectivity.
- Use a VLAN tester to verify proper tagging and isolation.

**6. Related Features and Considerations**

- **QoS:** VLANs can be used to prioritize traffic by assigning different QoS profiles.
- **Security:** Segmentation via VLANs provides isolation and reduces the risk of broadcast storms.

**7. MikroTik REST API Examples**

**Endpoint:** `/api/ip/vlan`

**Method:** POST

**JSON Payload:**

```json
{
  "interface": "ether1-gateway",
  "name": "VLAN1",
  "vlan-id": 1
}
```

**Expected Response (Success):**

```json
{
  "id": 1
}
```

**Method:** GET

**Expected Response:**

```json
[
  {
    "id": 1,
    "interface": "ether1-gateway",
    "name": "VLAN1",
    "vlan-id": 1
  }
]
```
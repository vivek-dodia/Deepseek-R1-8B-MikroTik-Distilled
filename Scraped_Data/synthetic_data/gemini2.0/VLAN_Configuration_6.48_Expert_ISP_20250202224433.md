## VLAN Configuration in RouterOS 6.48 for ISPs

### Configuration Scenario and Requirements

* ISP network with multiple customers requiring VLAN segregation
* VLANs for different services (e.g., Internet, VoIP, Management)
* RouterOS as the core router responsible for VLAN tagging and routing

### Step-by-Step Implementation

**1. Create VLANs:**

```
/interface vlan add name=VLAN10 vid=10
/interface vlan add name=VLAN20 vid=20
/interface vlan add name=VLAN30 vid=30
```

**2. Assign VLANs to Physical Interfaces:**

```
/interface ethernet set ether1 tagged-vlan-id=10
/interface ethernet set ether2 tagged-vlan-id=20,30
```

**3. Create VLAN Interfaces:**

```
/interface vlan sub-interface add interface=VLAN10
/interface vlan sub-interface add interface=VLAN20
/interface vlan sub-interface add interface=VLAN30
```

**4. Configure IP Addresses on VLAN Interfaces:**

```
/ip address add interface=VLAN10 address=192.168.10.1/24
/ip address add interface=VLAN20 address=192.168.20.1/24
/ip address add interface=VLAN30 address=192.168.30.1/24
```

**5. Configure Routing between VLANs:**

```
/ip route add dst-address=192.168.20.0/24 gateway=192.168.10.1
/ip route add dst-address=192.168.30.0/24 gateway=192.168.10.1
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN10 vid=10
/interface vlan add name=VLAN20 vid=20
/interface vlan add name=VLAN30 vid=30
/interface ethernet set ether1 tagged-vlan-id=10
/interface ethernet set ether2 tagged-vlan-id=20,30
/interface vlan sub-interface add interface=VLAN10
/interface vlan sub-interface add interface=VLAN20
/interface vlan sub-interface add interface=VLAN30
/ip address add interface=VLAN10 address=192.168.10.1/24
/ip address add interface=VLAN20 address=192.168.20.1/24
/ip address add interface=VLAN30 address=192.168.30.1/24
/ip route add dst-address=192.168.20.0/24 gateway=192.168.10.1
/ip route add dst-address=192.168.30.0/24 gateway=192.168.10.1
```

### Common Pitfalls and Solutions

* **VLAN tagging not configured:** Ensure tagged-vlan-id is set on the appropriate physical interfaces.
* **VLAN interfaces not created:** Create sub-interfaces for each VLAN to enable routing and IP configuration.
* **Incorrect IP addresses:** Verify that IP addresses are configured correctly on VLAN interfaces.
* **Routing not configured:** Add static routes to direct traffic between VLANs.

### Verification and Testing Steps

* Check VLAN interfaces using `/interface vlan print`
* Verify IP addresses on VLAN interfaces using `/ip address print`
* Test connectivity between VLANs with ping or traceroute

### Related Features and Considerations

* **Trunking:** Use EtherTrunks to aggregate multiple physical interfaces into a single logical trunk interface for carrying multiple VLANs.
* **QoS:** Apply QoS rules to prioritize traffic on different VLANs.
* **Access Control Lists (ACLs):** Implement ACLs on VLAN interfaces to restrict access and enhance security.

### MikroTik REST API Examples

**Endpoint:** `/interface/vlan`

**Request Method:** GET

**Example JSON Payload:**

```JSON
{
  "interface": "VLAN10"
}
```

**Expected Response:**

```JSON
[
  {
    "interface": "VLAN10",
    "vid": 10,
    "name": "VLAN10",
    "tagged-vlan-id": "10"
  }
]
```
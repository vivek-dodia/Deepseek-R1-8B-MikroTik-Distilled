## VLAN Configuration in RouterOS 7.12

### Configuration Scenario and Requirements

* Configure multiple VLANs on a single physical interface
* Isolate traffic between VLANs
* Assign IP addresses and DHCP services to VLANs

### Step-by-Step Implementation

**1. Create VLAN Interfaces:**

```bash
/interface vlan add name=vlan10 vlan-id=10 interface=ether1
/interface vlan add name=vlan20 vlan-id=20 interface=ether1
```

**2. Assign IP Addresses and DHCP Services:**

```bash
/ip address add address=10.10.10.1/24 interface=vlan10
/ip dhcp-server add address-pool=dhcp-pool-vlan10 interface=vlan10 range=10.10.10.100-10.10.10.254 lease-time=24h
/ip address add address=10.10.20.1/24 interface=vlan20
/ip dhcp-server add address-pool=dhcp-pool-vlan20 interface=vlan20 range=10.10.20.100-10.10.20.254 lease-time=24h
```

**3. Configure Firewall Rules:**

```bash
/ip firewall filter add chain=input action=accept in-interface=vlan10 dst-address=10.10.20.0/24
/ip firewall filter add chain=input action=accept in-interface=vlan20 dst-address=10.10.10.0/24
```

### Complete Configuration Commands

```bash
/interface vlan add name=vlan10 vlan-id=10 interface=ether1
/interface vlan add name=vlan20 vlan-id=20 interface=ether1
/ip address add address=10.10.10.1/24 interface=vlan10
/ip dhcp-server add address-pool=dhcp-pool-vlan10 interface=vlan10 range=10.10.10.100-10.10.10.254 lease-time=24h
/ip address add address=10.10.20.1/24 interface=vlan20
/ip dhcp-server add address-pool=dhcp-pool-vlan20 interface=vlan20 range=10.10.20.100-10.10.20.254 lease-time=24h
/ip firewall filter add chain=input action=accept in-interface=vlan10 dst-address=10.10.20.0/24
/ip firewall filter add chain=input action=accept in-interface=vlan20 dst-address=10.10.10.0/24
```

### Common Pitfalls and Solutions

* **VLAN ID Collision:** Ensure unique VLAN IDs are assigned to avoid traffic conflicts.
* **Incorrect Firewall Rules:** Double-check firewall rules to ensure traffic is allowed as intended.
* **IP Address Duplication:** Avoid duplicate IP addresses within the same VLAN.

### Verification and Testing Steps

* Ping between hosts within the same VLAN
* Check DHCP lease assignment on client devices
* Inspect firewall logs for successful traffic filtering

### Related Features and Considerations

* **Bridge Filtering:** Enhance security by restricting traffic between VLANs based on MAC addresses.
* **VLAN Trunking:** Configure trunk ports to carry traffic from multiple VLANs over a single physical link.
* **MPLS:** Utilize MPLS for Layer 3 routing of VLAN traffic.

### MikroTik REST API Examples

**Create VLAN:**

* **Endpoint:** `/interface/vlan`
* **Request Method:** POST
* **Request Payload:**

```json
{
  "name": "vlan10",
  "vlan-id": 10,
  "interface": "ether1"
}
```

* **Expected Response:**

```json
{
  "id": "09671093-2329-f7d2-b594-de18639491a1"
}
```

**Assign IP Address:**

* **Endpoint:** `/ip/address`
* **Request Method:** POST
* **Request Payload:**

```json
{
  "address": "10.10.10.1/24",
  "interface": "vlan10"
}
```

* **Expected Response:**

```json
{
  "id": "04b4d1cf-63f6-9e75-88e8-9288c6bb609b"
}
```
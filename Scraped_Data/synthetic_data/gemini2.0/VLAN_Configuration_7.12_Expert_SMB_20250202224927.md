## VLAN Configuration in RouterOS 7.12

### Configuration Scenario and Requirements

Configure multiple VLANs on a MikroTik router to segregate traffic and secure network resources within a small business (SMB) environment. VLANs will be used to separate administration traffic, employee traffic, and guest traffic.

### Step-by-Step Implementation

#### 1. Create VLAN Interfaces

Create VLAN interfaces for each VLAN required:

```
/interface vlan add name=<VLAN_Name> vlan-id=<VLAN_ID>
```

**Example:** Create a VLAN interface named "vlan_admin" with VLAN ID 100:

```
/interface vlan add name=vlan_admin vlan-id=100
```

#### 2. Assign IP Addresses

Assign IP addresses to each VLAN interface for management and connectivity:

```
/ip address add address=<IP_Address> interface=<VLAN_Interface>
```

**Example:** Assign the IP address 192.168.100.1 to the VLAN interface "vlan_admin":

```
/ip address add address=192.168.100.1 interface=vlan_admin
```

#### 3. Configure Firewall Rules

Create firewall rules to restrict traffic between VLANs, allowing only necessary communication:

```
/ip firewall add chain=input action=drop dst-address=<Destination_VLAN_IP> src-address=<Source_VLAN_IP>
```

**Example:** Allow traffic from the "vlan_admin" VLAN to the "vlan_employee" VLAN, but not the other way around:

```
/ip firewall add chain=input action=drop dst-address=192.168.100.0/24 src-address=192.168.200.0/24
/ip firewall add chain=input action=accept dst-address=192.168.200.0/24 src-address=192.168.100.0/24
```

#### 4. Configure DHCP Server

Configure a DHCP server on each VLAN interface to automatically assign IP addresses to devices:

```
/ip dhcp-server add interface=<VLAN_Interface>
```

**Example:** Configure a DHCP server on the "vlan_employee" VLAN:

```
/ip dhcp-server add interface=vlan_employee
```

### Complete Configuration Commands

```
/interface vlan add name=vlan_admin vlan-id=100
/interface vlan add name=vlan_employee vlan-id=200
/interface vlan add name=vlan_guest vlan-id=300

/ip address add address=192.168.100.1 interface=vlan_admin
/ip address add address=192.168.200.1 interface=vlan_employee
/ip address add address=192.168.300.1 interface=vlan_guest

/ip firewall add chain=input action=drop dst-address=192.168.100.0/24 src-address=192.168.200.0/24
/ip firewall add chain=input action=accept dst-address=192.168.200.0/24 src-address=192.168.100.0/24

/ip dhcp-server add interface=vlan_employee
/ip dhcp-server add interface=vlan_guest
```

### Common Pitfalls and Solutions

- **VLAN IDs:** Make sure to use unique VLAN IDs for each VLAN to avoid conflicts.
- **Firewall Rules:** Double-check firewall rules to ensure they are configured correctly and do not allow unauthorized traffic.
- **DHCP Server:** Verify that DHCP servers are enabled on the correct VLAN interfaces to avoid IP address conflicts.

### Verification and Testing Steps

- Access each VLAN interface and verify that IP addresses and firewall rules are working as intended.
- Connect devices to each VLAN and test network connectivity and IP address assignment.
- Use a tool like Wireshark to monitor traffic and ensure VLAN segregation is effective.

### Related Features and Considerations

- **VLAN Trunking:** Use VLAN trunking to connect switches and extend VLANs across multiple devices.
- **IGMP Snooping:** Enable IGMP snooping to optimize multicast traffic within VLANs.
- **RADIUS Authentication:** Integrate RADIUS authentication with VLANs to enhance security and device access control.

### MikroTik REST API Examples

**Endpoint:** `/interface/vlan/add`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "name": "vlan_admin",
  "vlan-id": 100
}
```

**Expected Response:**

```json
{
  "interface": "vlan_admin"
}
```
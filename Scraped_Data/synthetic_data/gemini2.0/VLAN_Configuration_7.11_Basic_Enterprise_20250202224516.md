## VLAN Configuration in MikroTik RouterOS

### Configuration Scenario and Requirements

- Objective: Configure multiple VLANs on a MikroTik router to segregate traffic and enhance network security.
- Router: MikroTik RouterOS 7.11 (or higher)
- VLAN IDs: VLAN 100 (Voice), VLAN 200 (Data), VLAN 300 (Management)
- Switch Ports: Ports 1-8 as VLAN 100, Ports 9-16 as VLAN 200, Port 17 as VLAN 300
- Network Configuration: IP address 192.168.1.254/24 on VLAN 200

### Step-by-Step Implementation

1. **Create VLANs**

   ```
   /interface vlan add name=VLAN100 vlan-id=100
   /interface vlan add name=VLAN200 vlan-id=200
   /interface vlan add name=VLAN300 vlan-id=300
   ```

2. **Assign VLANs to Switch Ports**

   ```
   /interface bridge port set bridge=bridge1 vlan-filtering=yes
   /interface bridge port add bridge=bridge1 interface=ether1 vlan-id=100
   /interface bridge port add bridge=bridge1 interface=ether2 vlan-id=100
   /interface bridge port add bridge=bridge1 interface=ether9 vlan-id=200
   /interface bridge port add bridge=bridge1 interface=ether17 vlan-id=300
   ```

3. **Configure IP Address on VLAN Interface**

   ```
   /ip address add address=192.168.1.254/24 interface=VLAN200
   ```

### Complete Configuration Commands

```
/interface vlan add name=VLAN100 vlan-id=100
/interface vlan add name=VLAN200 vlan-id=200
/interface vlan add name=VLAN300 vlan-id=300

/interface bridge port set bridge=bridge1 vlan-filtering=yes
/interface bridge port add bridge=bridge1 interface=ether1 vlan-id=100
/interface bridge port add bridge=bridge1 interface=ether2 vlan-id=100
/interface bridge port add bridge=bridge1 interface=ether9 vlan-id=200
/interface bridge port add bridge=bridge1 interface=ether17 vlan-id=300

/ip address add address=192.168.1.254/24 interface=VLAN200
```

### Common Pitfalls and Solutions

- **VLAN Flooding:** Ensure that all ports are correctly assigned to VLANs to prevent unintended traffic flooding.
- **Lack of IP Address:** If an IP address is not assigned to a VLAN interface, devices connected to that VLAN will not be able to communicate.
- **VLAN ID Mismatch:** Verify that the VLAN ID specified in the bridge port configuration matches the VLAN ID of the VLAN interface.

### Verification and Testing Steps

- Check if VLANs are created and assigned to switch ports: `/interface vlan print`
- Verify IP address assignment: `/ip address print`
- Test connectivity between devices on different VLANs: Use ping or traceroute to confirm communication.

### Related Features and Considerations

- **VLAN Trunking:** Use trunk ports to carry multiple VLANs over a single physical link.
- **VLAN Isolation:** Enable VLAN isolation to prevent devices on different VLANs from communicating directly.
- **Security:** Utilize VLANs to segment sensitive network segments, such as management or guest networks, to enhance security.

### MikroTik REST API Examples

**Get VLANs:**

| API Endpoint | Request Method | Request Body | Response |
|---|---|---|---|
| `/api/interface/vlan` | `GET` | N/A | `{ "count": 3, "data": [ { "interface": "VLAN100", "vlan-id": 100 }, { "interface": "VLAN200", "vlan-id": 200 }, { "interface": "VLAN300", "vlan-id": 300 } ] }`

**Add VLAN:**

| API Endpoint | Request Method | Request Body | Response |
|---|---|---|---|
| `/api/interface/vlan` | `POST` | `{ "name": "VLAN400", "vlan-id": 400 }` | `{ "interface": "VLAN400", "vlan-id": 400 }`
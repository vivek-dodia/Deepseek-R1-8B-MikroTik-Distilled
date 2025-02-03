## VLAN Configuration in RouterOS 6.48 for SMBs

### Configuration Scenario and Requirements

- Configure VLANs on a MikroTik router to segment the network traffic.
- Create VLAN interfaces for each VLAN.
- Assign IP addresses and default gateways to each VLAN interface.
- Allow communication between VLANs.

### Step-by-Step Implementation

**1. Create VLANs and Interfaces**

```
/interface vlan add name=VLAN10 vlan-id=10
interface vlan add name=VLAN20 vlan-id=20
```

**2. Assign IP Addresses and Gateways**

```
/ip address add address=192.168.10.1/24 interface=VLAN10
/ip address add address=192.168.20.1/24 interface=VLAN20
```

**3. Configure Default Gateway**

```
/ip route add gateway=192.168.0.1 interface=VLAN10
/ip route add gateway=192.168.0.1 interface=VLAN20
```

**4. Enable Inter-VLAN Communication**

```
/interface vlan set VLAN10 mtu=1500
/interface vlan set VLAN20 mtu=1500
/ip firewall filter add chain=forward action=accept in-interface=VLAN10 out-interface=VLAN20
/ip firewall filter add chain=forward action=accept in-interface=VLAN20 out-interface=VLAN10
```

### Complete Configuration Commands

- **Create VLANs:**
  ```
  /interface vlan add name=<VLAN_NAME> vlan-id=<VLAN_ID>
  ```
- **Assign IP Addresses:**
  ```
  /ip address add address=<IP_ADDRESS>/<CIDR> interface=<VLAN_INTERFACE>
  ```
- **Configure Default Gateway:**
  ```
  /ip route add gateway=<GATEWAY_ADDRESS> interface=<VLAN_INTERFACE>
  ```
- **Enable Inter-VLAN Communication:**
  ```
  /interface vlan set <VLAN_INTERFACE> mtu=1500
  /ip firewall filter add chain=forward action=accept in-interface=<VLAN_INTERFACE_1> out-interface=<VLAN_INTERFACE_2>
  /ip firewall filter add chain=forward action=accept in-interface=<VLAN_INTERFACE_2> out-interface=<VLAN_INTERFACE_1>
  ```

### Common Pitfalls and Solutions

- **Incorrect VLAN ID:** Ensure that the VLAN ID specified during creation is valid (1-4094).
- **Duplicate VLANs:** Avoid creating VLANs with the same VLAN ID.
- **VLAN Tagging:** Ensure that the devices connected to the VLAN interfaces support VLAN tagging and are configured to use the correct VLAN ID.
- **Firewall Rules:** Remember to create firewall rules to allow traffic between VLANs if necessary.

### Verification and Testing Steps

- Use `/interface vlan print` to verify the created VLANs.
- Use `/ip address print` to confirm the assigned IP addresses.
- Use `/ip route print` to check the configured default gateways.
- Use `ping` or another network utility to test connectivity between different VLANs.

### Related Features and Considerations

- **VLAN Trunking:** Configure VLAN trunking (802.1Q) to carry multiple VLANs over a single physical interface.
- **VLAN Bonding:** Bond multiple VLAN interfaces for increased bandwidth and redundancy.
- **VLAN Filtering:** Use VLAN filtering to restrict access to specific VLANs based on MAC address or other criteria.
- **VLAN Management:** Utilize the "/vlan" command to manage VLAN settings, including creating, modifying, and removing VLANs.

### MikroTik REST API Examples

- **Get VLANs:**
   - **Endpoint:** `/api/v7/interface/vlan`
   - **Request Method:** GET
   - **Response:**
     ```json
     [
       {
         "disabled": false,
         "interface": "VLAN1",
         "vlan-id": 10
       },
       {
         "disabled": false,
         "interface": "VLAN2",
         "vlan-id": 20
       }
     ]
     ```
- **Create VLAN:**
   - **Endpoint:** `/api/v7/interface/vlan`
   - **Request Method:** POST
   - **Request Payload:**
     ```json
     {
       "interface": "VLAN3",
       "vlan-id": 30
     }
     ```
   - **Response:**
     ```json
     {
       "disabled": false,
       "interface": "VLAN3",
       "vlan-id": 30
     }
     ```
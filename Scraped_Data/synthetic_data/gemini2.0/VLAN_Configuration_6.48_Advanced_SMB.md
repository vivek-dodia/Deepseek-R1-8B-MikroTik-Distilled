## VLAN Configuration in RouterOS 6.48

### Configuration Scenario and Requirements

**Objective:** To configure VLANs on a MikroTik RouterOS router to segment network traffic into isolated domains.

**Requirements:**

- RouterOS v6.48 or later
- Understanding of VLANs and their benefits
- Switches supporting VLAN tagging (e.g., IEEE 802.1Q)
- Network devices compatible with VLANs

### Step-by-Step Implementation

**1. Create VLAN Interfaces**

- Navigate to `Interfaces > VLAN` and click `+`.
- Enter the following parameters:
    - **Name:** Enter a descriptive name for the VLAN.
    - **VLAN ID:** Specify the VLAN ID (1-4094).
    - **Interface:** Select the physical interface to which the VLAN applies.

**2. Configure VLAN Tagging**

- Go to `Interfaces > Bridge` and create a new bridge (e.g., `VLAN-Bridge`).
- Add the VLAN interfaces to the bridge by selecting them in the **Ports** list.
- Enable VLAN tagging by setting `VLAN Tagging` to `Yes`.

**3. Assign IP Addresses**

- Go to `IP > Addresses` and create a new IP address for each VLAN interface.
- Enter the following parameters:
    - **Interface:** Select the corresponding VLAN interface.
    - **Address:** Specify the IP address in the desired subnet.
    - **Network:** Enter the subnet mask.

**4. Configure DHCP Server**

Optionally, you can configure a DHCP server for each VLAN to automatically assign IP addresses to clients.

- Go to `IP > DHCP Server` and create a new DHCP server for each VLAN.
- Select the VLAN interface in the **Interface** field.
- Configure other DHCP settings as needed (e.g., lease time, DNS servers).

### Complete Configuration Commands

```
/interface vlan add name=VLAN1 vlan-id=10 interface=ether1
/interface bridge add name=VLAN-Bridge vlan-tagging=yes
/interface bridge port add bridge=VLAN-Bridge interface=VLAN1
/interface bridge port add bridge=VLAN-Bridge interface=VLAN2
/ip address add address=192.168.10.1/24 interface=VLAN1
/ip address add address=192.168.20.1/24 interface=VLAN2
/ip dhcp-server add interface=VLAN1 address-pool=VLAN1-Pool lease-time=3600s
/ip dhcp-server add interface=VLAN2 address-pool=VLAN2-Pool lease-time=3600s
```

### Common Pitfalls and Solutions

* Ensure switches support VLAN tagging.
* Avoid VLAN ID conflicts by carefully planning.
* Verify that IP subnets for different VLANs do not overlap.
* Troubleshoot connectivity issues by checking VLAN tagging and IP configurations.

### Verification and Testing Steps

* Test connectivity between devices in different VLANs.
* Use a packet sniffer to verify VLAN tagging.
* Check DHCP server logs to ensure IP addresses are assigned correctly.

### Related Features and Considerations

* **Port-Based VLANs:** Assign VLANs based on the physical port.
* **MAC Address-Based VLANs:** Create VLANs based on MAC addresses.
* **Security Considerations:** Isolate sensitive traffic and implement access control lists.
* **Centralized Management:** Manage VLANs across multiple routers using a central controller.
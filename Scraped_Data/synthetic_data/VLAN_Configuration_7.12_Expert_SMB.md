## VLAN Configuration in RouterOS 7.12

### Configuration Scenario and Requirements

* SMB network with multiple devices requiring logical separation
* Create VLANs for different departments or functions
* Assign ports to specific VLANs
* Implement VLAN tagging for inter-VLAN communication

### Step-by-Step Implementation

**1. Create VLANs**

```
/interface vlan add name=VLAN1
/interface vlan add name=VLAN2
```

**2. Assign Ports to VLANs**

```
/interface ethernet set ether1 switch-vlan=VLAN1
/interface ethernet set ether2 switch-vlan=VLAN2
```

**3. Enable VLAN Tagging**

```
/interface vlan set VLAN1 tag=1
/interface vlan set VLAN2 tag=2
```

**4. Configure Inter-VLAN Routing**

```
/ip route add dst-address=192.168.1.0/24 gateway=192.168.1.1
/ip route add dst-address=192.168.2.0/24 gateway=192.168.2.1
```

**5. Verify VLAN Configuration**

```
/interface vlan print
/interface ethernet print
/ip address print
```

### Complete Configuration Commands

```
/interface vlan add name=VLAN1
/interface vlan add name=VLAN2
/interface ethernet set ether1 switch-vlan=VLAN1
/interface ethernet set ether2 switch-vlan=VLAN2
/interface vlan set VLAN1 tag=1
/interface vlan set VLAN2 tag=2
/ip route add dst-address=192.168.1.0/24 gateway=192.168.1.1
/ip route add dst-address=192.168.2.0/24 gateway=192.168.2.1
```

### Common Pitfalls and Solutions

* **Incorrect VLAN Tagging:** Ensure that the VLAN tags assigned to the VLANs and ports are unique and not conflicting.
* **Missing Gateway:** Configure a gateway for each VLAN to allow communication between devices in that VLAN and other networks.
* **VLAN Hopping:** Prevent unauthorized access to devices in other VLANs by limiting which ports can receive tagged traffic.

### Verification and Testing Steps

* **Test Inter-VLAN Communication:** Ping devices in different VLANs to verify that communication is established.
* **Check VLAN Configuration:** Use the commands in the "Verify VLAN Configuration" section to ensure that the VLANs are configured correctly.
* **Monitor Traffic:** Use tools like Wireshark or the built-in packet sniffer in RouterOS to monitor traffic and verify that it is being tagged and routed properly.

### Related Features and Considerations

* **VLAN Trunks:** Configure trunk ports to allow multiple VLANs to pass through a single physical link.
* **Security:** Implement firewall rules to prevent unwanted traffic between VLANs.
* **Quality of Service (QoS):** Apply QoS policies to prioritize traffic on specific VLANs.
* **DHCP Server:** Configure a DHCP server on each VLAN to assign IP addresses to devices.
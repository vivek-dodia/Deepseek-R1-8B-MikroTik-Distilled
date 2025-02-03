**VLAN Configuration in MikroTik RouterOS 7.12**

**Configuration Scenario and Requirements**

* Create multiple virtual LANs (VLANs) on a switch port.
* Assign devices to different VLANs for network segmentation.
* Allow communication between devices on different VLANs through a router.

**Step-by-Step Implementation**

**1. Create VLANs**

On the MikroTik router connected to the switch:

* Navigate to **Interfaces** > **VLAN**
* Click on the **+** button
* Enter a **VLAN ID**
* Assign a **VLAN Name** (optional)
* Click **Apply**

**2. Add VLANs to Switch Port**

On the switch, tag the port with the created VLANs:

* Access the switch management interface
* Enable VLAN tagging on the desired port
* Assign the created VLAN IDs to the port

**3. Configure Inter-VLAN Routing**

On the MikroTik router:

* Navigate to **IP** > **Routing** > **VLAN**
* Click on the **+** button
* Select the **VLAN** from the drop-down menu
* Assign an **IP Address** and **Subnet Mask** within the VLAN
* If necessary, configure firewall rules to allow traffic between VLANs
* Click **Apply**

**Complete Configuration Commands**

**Create VLAN:**
```
/interface vlan add vlan-id=10 name=VLAN10
/interface vlan add vlan-id=20 name=VLAN20
```

**Add VLANs to Switch Port:**
```
[Switch Management Interface]
interface ethernet ether1
switchport mode trunk
switchport trunk allowed vlan 10,20
```

**Configure Inter-VLAN Routing:**
```
/ip routing vlan add vlan=VLAN10 address=10.10.10.1/24
/ip routing vlan add vlan=VLAN20 address=10.10.20.1/24
```

**Firewall Rule (Permit Inter-VLAN Traffic):**
```
/ip firewall filter add chain=forward action=accept in-interface-list=VLAN10 dst-address-list=VLAN20
/ip firewall filter add chain=forward action=accept in-interface-list=VLAN20 dst-address-list=VLAN10
```

**Common Pitfalls and Solutions**

* **VLANs not communicating:** Check if VLAN tagging is enabled on the switch and if the devices are assigned to the correct VLANs.
* **Inter-VLAN routing not working:** Ensure that the VLAN interfaces are created and have valid IP addresses and that the firewall rules allow traffic between the VLANs.
* **Incorrect port configuration:** Verify that the switch port is configured as a trunk port and that the desired VLANs are tagged.

**Verification and Testing Steps**

* Check VLAN configurations on the switch and router using commands like `/interface switch vlan` and `/ip routing vlan`.
* Assign devices to different VLANs and test connectivity using ping or traceroute.
* Monitor firewall logs to ensure inter-VLAN traffic is allowed.

**Related Features and Considerations**

* **QinQ:** Allows for multiple VLANs on a single physical link.
* **VLAN Trunking:** Enables multiple VLANs to be carried over a single trunk link.
* **Security:** Configure firewall rules and access control lists to secure VLAN traffic and prevent unauthorized access.
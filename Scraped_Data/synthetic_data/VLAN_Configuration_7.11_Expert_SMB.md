## VLAN Configuration on MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

* **Objective:** Create multiple VLANs on a MikroTik router to segment and isolate network traffic.
* **Requirements:**
    * MikroTik RouterOS 7.11 or higher
    * Interfaces configured with IP addresses
    * Unmanaged or VLAN-capable switches

### Step-by-Step Implementation

#### 1. Create VLAN Interfaces

* Navigate to **Interfaces > VLAN**.
* Click the **+** button.
* Enter a unique **VLAN ID** (e.g., 10).
* Select the **Interface** to which the VLAN will be added (e.g., ether1).
* Click **OK**.

#### 2. Add IP Address to VLAN Interface

* Navigate to **IP > Addresses**.
* Click the **+** button.
* Select the **VLAN** interface (e.g., vlan10).
* Enter an **IP Address** within the appropriate subnet.
* Click **OK**.

#### 3. Create VLAN Bridge

* Navigate to **Bridge > Bridges**.
* Click the **+** button.
* Enter a **Name** for the bridge (e.g., VLAN-Bridge).
* Add the newly created **VLAN** interface(s) (e.g., vlan10) to the bridge.
* Click **OK**.

#### 4. Configure Port Membership

* Navigate to **Interfaces > VLAN** interfaces (e.g., vlan10).
* In the **Settings** tab, select the appropriate switch **Port** to belong to this VLAN.
* Repeat for all interfaces and ports.

#### 5. Configure Trunk Port

* If using an unmanaged switch, skip this step.
* Configure the switch port trunk to allow untagged traffic for native VLAN and tagged traffic for all other VLANs.
* Example Cisco switch configuration:
```
interface GigabitEthernet 0/1
switchport mode trunk
switchport trunk native vlan 1
switchport trunk allowed vlan 10,20,30
```

### Complete Configuration Commands

```
/interface vlan add name=vlan10 interface=ether1
/ip address add address=10.10.10.1/24 interface=vlan10
/bridge add name=VLAN-Bridge
/interface vlan vlan10 settings set ports=[list=ether1_port1]
```

### Common Pitfalls and Solutions

* **VLAN ID conflict:** Ensure that all VLAN IDs are unique across the network.
* **Incorrect port membership:** Verify that each port is correctly assigned to the intended VLAN.
* **Unconfigured trunk port:** Ensure that the switch port connected to the router is configured for trunking.

### Verification and Testing Steps

* Check the VLAN interfaces' status in **Interfaces > VLAN**.
* Verify IP connectivity within each VLAN.
* Use a packet sniffer to confirm traffic isolation between VLANs.

### Related Features and Considerations

* **Security:** Configure firewall rules to restrict access between VLANs.
* **QoS:** Prioritize traffic by creating VLANs for specific applications or traffic types.
* **Management:** Use RouterOS's **VLAN Manager** to manage and monitor VLAN configurations.
* **Spanning Tree Protocol (STP):** Configure STP to prevent loops in the bridged VLAN network.
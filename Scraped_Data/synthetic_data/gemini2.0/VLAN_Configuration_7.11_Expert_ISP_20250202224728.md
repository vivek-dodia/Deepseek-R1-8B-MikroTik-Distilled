## VLAN Configuration in RouterOS 7.11

### Prerequisites

- MikroTik RouterOS 7.11 (or later)
- Physical or virtual network interfaces

### Configuration Scenario and Requirements

* **Objective:** Configure multiple VLANs on a MikroTik router to segregate traffic on a single physical interface.
* **Requirements:**
    * Define VLAN tags and assign them to physical ports.
    * Enable VLAN awareness on the router.
    * Create VLAN interfaces and configure their IP addresses.
    * Configure firewall rules to enforce VLAN isolation.

### Step-by-Step Implementation

**1. Define VLAN Tags and Assign to Physical Ports**

* Navigate to **Interfaces** -> **VLAN** tab.
* Click on the **+** button to create a new VLAN.
* Set the **VLAN ID** (tag).
* Select the **Interface** (physical port) to which the VLAN tag will be assigned.
* Click **Apply** and then **OK**.

**2. Enable VLAN Awareness**

* Go to **Switch** -> **Settings** tab.
* Check the **VLAN awareness** checkbox.
* Click **Apply** and then **OK**.

**3. Create VLAN Interfaces and Configure IP Addresses**

* Navigate to **Interfaces** -> **VLAN** tab and click on the **+** button.
* Select the **Parent interface** (physical interface with VLAN tag).
* Set the **VLAN ID**.
* Configure the **IP address** and **subnet mask**.
* Click **Apply** and then **OK**.

**4. Configure Firewall Rules**

* Go to **IP** -> **Firewall** -> **Filter Rules** tab.
* Click on the **+** button to create a new rule.
* Set the **Chain** to **forward**.
* Select the **VLAN** interface from the **In. Interface** dropdown.
* Select the **VLAN** interface to which you want to allow traffic from the **Out. Interface** dropdown.
* Click **Apply** and then **OK**.

### Complete Configuration Commands

```
# Define VLAN tag and assign to physical port
/interface vlan add vlan-id=10 interface=ether1

# Enable VLAN awareness
/switch settings set vlan-awareness=yes

# Create VLAN interface and configure IP address
/interface vlan add parent=ether1 vlan-id=10 address=192.168.10.1/24

# Configure firewall rule to allow traffic between VLANs
/ip firewall filter add chain=forward action=accept in-interface=vlan10 out-interface=vlan20
```

### Common Pitfalls and Solutions

- **VLAN ID Conflicts:** Make sure VLAN tags are unique for all interfaces.
- **Incorrect Firewall Rules:** Check that firewall rules are applied correctly to isolate traffic between VLANs.
- **No VLAN Awareness:** Ensure that VLAN awareness is enabled on the switch settings to allow VLAN communication.

### Verification and Testing Steps

- Use the `/vlan print` command to verify VLAN configurations.
- Assign IP addresses to devices connected to each VLAN and test connectivity.
- Monitor firewall logs to ensure that VLANs are isolated as expected.

### Related Features and Considerations

- **VLAN Trunking:** Allows multiple VLANs to be carried over a single physical link using trunking protocols like 802.1Q or ISL.
- **VLAN Tagging:** Specifying VLAN tags on packets allows for VLAN identification and routing.
- **Security:** VLANs provide a layer of security by segmenting networks and isolating traffic between different groups.

### MikroTik REST API Examples

**Endpoint:** `/interface/vlan`

**Request Method:** GET

**Example JSON Payload:**

```json
{
  "resource": [
    {
      ".id": "VLAN_ID"
    }
  ]
}
```

**Expected Response (JSON):**

```json
[
  {
    ".id": "VLAN_ID",
    "name": "VLAN_NAME",
    "interface": "PHYSICAL_INTERFACE",
    "vlan-id": "VLAN_ID",
    "mtu": "MTU",
    "use-ip-firewall": "BOOL"
  }
]
```
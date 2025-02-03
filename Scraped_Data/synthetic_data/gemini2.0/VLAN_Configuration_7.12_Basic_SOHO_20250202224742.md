**VLAN Configuration in RouterOS 7.12**

**Configuration Level:** Basic

**Network Scale:** SOHO

**1. Configuration Scenario and Requirements**

* Create multiple VLANs for network segmentation and traffic isolation.
* Configure VLAN interfaces to access the VLANs.
* Assign IP addresses to the VLAN interfaces.

**2. Step-by-Step Implementation**

1. **Create VLANs:**
   - Navigate to **Interfaces > VLAN**
   - Click **+** to add a new VLAN
   - Enter a **VLAN ID** (e.g., 10)
   - Click **Apply**

2. **Create VLAN Interfaces:**
   - Navigate to **Interfaces**
   - Click **+** to add a new interface
   - Select **VLAN** as the **Type**
   - Select the desired **VLAN ID**
   - Click **Apply**

3. **Assign IP Addresses to VLAN Interfaces:**
   - Navigate to **IP > Addresses**
   - Click **+** to add a new IP address
   - Select the desired **Interface** (VLAN interface)
   - Enter the **IP Address** and **Subnet Mask**
   - Click **Apply**

**3. Complete Configuration Commands**

```
/interface vlan add name=vlan10 vlan-id=10
/interface vlan add name=vlan20 vlan-id=20
/interface vlan add name=vlan30 vlan-id=30

/interface add name=vlan-interface1 type=vlan vlan=vlan10
/interface add name=vlan-interface2 type=vlan vlan=vlan20
/interface add name=vlan-interface3 type=vlan vlan=vlan30

/ip address add address=10.10.10.1/24 interface=vlan-interface1
/ip address add address=10.10.20.1/24 interface=vlan-interface2
/ip address add address=10.10.30.1/24 interface=vlan-interface3
```

**4. Common Pitfalls and Solutions**

* **VLAN ID conflicts:** Ensure that each VLAN has a unique VLAN ID within the network.
* **VLAN interface not created:** Verify that the VLAN interface is successfully created and has the correct VLAN ID.
* **IP address conflict:** Check for any duplicate IP addresses assigned to the VLAN interfaces.

**5. Verification and Testing Steps**

* Ping between devices on different VLANs to verify connectivity.
* Use the command `/interface vlan print` to display the VLAN configuration.
* Use the command `/ip address print` to display the IP addresses assigned to the VLAN interfaces.

**6. Related Features and Considerations**

* **VLAN tagging:** Enable VLAN tagging on the interfaces connected to the VLANs to separate VLAN traffic on the same physical network.
* **QoS:** Configure QoS policies to prioritize traffic on different VLANs.
* **NAT:** Implement NAT rules on the VLAN interfaces to allow communication between VLANs and the Internet.

**7. MikroTik REST API Examples**

**Get VLAN List:**

**API Endpoint:** `/interface/vlan`

**Request Method:** GET

**Expected Response:**

```json
[
  {
    "number": 10,
    "name": "vlan10",
    "mtu": 1500,
    "vlan-id": 10,
    "interface": [],
    "comment": null
  },
  {
    "number": 20,
    "name": "vlan20",
    "mtu": 1500,
    "vlan-id": 20,
    "interface": [],
    "comment": null
  }
]
```

**Create VLAN:**

**API Endpoint:** `/interface/vlan`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "name": "vlan30",
  "vlan-id": 30
}
```

**Expected Response:**

```json
{
  "number": 30,
  "name": "vlan30",
  "mtu": 1500,
  "vlan-id": 30,
  "interface": [],
  "comment": null
}
```
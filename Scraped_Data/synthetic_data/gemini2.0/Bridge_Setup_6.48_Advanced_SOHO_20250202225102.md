## Bridge Setup in MikroTik RouterOS 6.48

### Configuration Scenario and Requirements

* Create a bridge interface to connect multiple physical interfaces into a single logical network segment.
* Assign IP addresses to the bridge interface and set up firewall rules for network access.
* Enable Spanning Tree Protocol (STP) to prevent bridging loops.

### Step-by-Step Implementation

#### 1. Create Bridge Interface

* Navigate to `Interfaces` > `Bridge`
* Click on `+`
* Enter a `Name` for the bridge (e.g., `br0`)
* Click on `Apply`

#### 2. Assign Physical Interfaces to Bridge

* Select the `br0` bridge interface you created
* Go to the `Ports` tab
* Select the physical interfaces you want to add to the bridge (e.g., `ether1` and `ether2`)
* Click on `+` to add them
* Click on `Apply`

#### 3. Configure IP Address and Firewall Rules

* Navigate to `IP` > `Addresses`
* Click on `+`
* Select the `br0` bridge interface
* Enter an IP address and subnet mask (e.g., `192.168.1.1/24`)
* Click on `Apply`

* Navigate to `IP` > `Firewall` > `Filter Rules`
* Click on `+`
* Create two rules:
    * **Allow Inbound Traffic:**
        * `Chain`: `input`
        * `Action`: `accept`
        * `Inbound Interface`: `br0`
    * **Allow Outbound Traffic:**
        * `Chain`: `output`
        * `Action`: `accept`
        * `Outbound Interface`: `br0`

#### 4. Enable STP

* Navigate to `IP` > `Bridge` > `Settings`
* Select the `STP` tab
* Enable `STP` and choose a `STP Bridge Priority` (e.g., `8192`)
* Click on `Apply`

### Complete Configuration Commands

```text
/interface bridge add name=br0
/interface bridge port add bridge=br0 interface=ether1
/interface bridge port add bridge=br0 interface=ether2
/ip address add address=192.168.1.1/24 interface=br0
/ip firewall filter add chain=input action=accept in-interface=br0
/ip firewall filter add chain=output action=accept out-interface=br0
/ip bridge settings set forward-delay=15 hello-time=2 max-age=20 config-bridge=br0
```

### Common Pitfalls and Solutions

* **Bridge Loop:** Ensure that STP is enabled and configured properly to prevent bridging loops.
* **IP Address Conflict:** Check for duplicate IP addresses on the bridge interface and connected devices.
* **Firewall Block:** Make sure the firewall rules allow traffic between the bridge interface and the connected devices.

### Verification and Testing Steps

* **Check Bridge Interface:** Navigate to `Interfaces` > `Bridge` to verify the `br0` bridge is created.
* **Verify IP Address:** Run the command `/ip address print` to check the IP address assigned to the `br0` bridge.
* **Test Connectivity:** Ping from one device connected to the bridge to another device on the same bridge.

### Related Features and Considerations

* [VLANs](https://wiki.mikrotik.com/wiki/VLAN) can be used to create multiple logical networks on the same physical bridge.
* [Bonding](https://wiki.mikrotik.com/wiki/Bonding) can be used to create a logical interface that combines multiple physical interfaces for increased bandwidth and redundancy.
* [Security:** Consider implementing additional security measures, such as disabling unnecessary protocols or setting up intrusion detection/prevention systems.

### MikroTik REST API Examples

**Create Bridge Interface**

**Endpoint:** `/interface/bridge`

**Request Method:** `POST`

**Request Payload:**

```json
{
  "name": "br0"
}
```

**Expected Response:**

```json
{
  "id": 2
}
```

**Assign Physical Interface to Bridge**

**Endpoint:** `/interface/bridge/port`

**Request Method:** `POST`

**Request Payload:**

```json
{
  "bridge": "br0",
  "interface": "ether1"
}
```

**Expected Response:**

```json
{
  "id": 1
}
```
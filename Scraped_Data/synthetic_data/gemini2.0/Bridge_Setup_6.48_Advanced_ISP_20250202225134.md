## Bridge Setup in MikroTik RouterOS 6.48 (ISP)

### 1. Configuration Scenario and Requirements

* Create a bridge to connect multiple physical interfaces and forward traffic between them.
* Configure the bridge with parameters to optimize performance and security.
* Restrict access to the bridge from unauthorized interfaces.

### 2. Step-by-Step Implementation

**Bridge Creation and Configuration**

1. Navigate to **Interfaces** > **Bridges** in RouterOS.
2. Click **+** to create a new bridge.
3. Configure the following parameters:
    - **Name:** Enter a name for the bridge.
    - **Protocol:** Select the bridging protocol (e.g., Spanning Tree Protocol).
    - **Fast Forwarding:** Enable fast forwarding to improve performance.
    - **MAC Learning:** Enable MAC address learning to build a forwarding table.

**Interface Addition**

1. Add physical interfaces to the bridge by selecting them and clicking **Add**.
2. Repeat for all interfaces that需要 to be connected.

**Filter Configuration**

1. To restrict access to the bridge, go to **IP** > **Firewall** > **Filter Rules**.
2. Create a new rule with the following parameters:
    - **Chain:** input
    - **Source:** Select the untrusted interfaces.
    - **Destination:** Address the bridge interface.
    - **Action:** Drop

### 3. Complete Configuration Commands

```
/interface bridge add name=my-bridge protocol=stp fast-forward=yes mac-learning=yes
/interface bridge port add interface=ether1 bridge=my-bridge
/interface bridge port add interface=ether2 bridge=my-bridge
/interface bridge port add interface=ether3 bridge=my-bridge
/ip firewall filter add chain=input action=drop in-interface-list=untrusted-interfaces dst-address=my-bridge
```

### 4. Common Pitfalls and Solutions

* **Interfaces not added to bridge:** Ensure the correct interfaces are selected and clicked in the Add field.
* **Filter rule not applied:** Verify that the filter rule is active and has the correct settings.
* **Fast Forwarding not enabled:** Check if Fast Forwarding is enabled in the bridge configuration.

### 5. Verification and Testing Steps

* **Connectivity test:** Ping between hosts connected to the different interfaces in the bridge.
* **MAC address table:** Display the MAC address table using the command `/interface bridge print forwarding=present` to check if MAC addresses are being learned.
* **Firewall test:** Attempt to access the bridge from an untrusted interface. Traffic should be blocked.

### 6. Related Features and Considerations

* VLANs can be created within bridges for further segmentation.
* Multiple bridging protocols are available, such as STP, RSTP, and MSTP.
* Consider load balancing and failover options to enhance bridge availability.

### 7. MikroTik REST API Examples

**Example 1: Create a bridge**

* **API Endpoint:** `/interface/bridge/add`
* **Request Method:** POST
* **Example JSON Payload:**
```json
{
    "name": "my-bridge"
}
```
* **Expected Response:**
```json
{
    "id": 1
}
```

**Example 2: Add an interface to a bridge**

* **API Endpoint:** `/interface/bridge/port/add`
* **Request Method:** POST
* **Example JSON Payload:**
```json
{
    "bridge": 1,
    "interface": "ether1"
}
```
* **Expected Response:**
```json
{
    "id": 4
}
```
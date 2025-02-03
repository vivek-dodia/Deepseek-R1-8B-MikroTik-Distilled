## Bridge Setup in MikroTik RouterOS 7.11 (Enterprise)

### Configuration Scenario and Requirements

* Create a bridge to connect multiple physical ports
* Use the bridge as a single logical entity for traffic forwarding
* Forward traffic between devices connected to different ports

### Step-by-Step Implementation

#### 1. Create and Configure the Bridge

- Navigate to **Bridge** > **Bridges**
- Click **+** to create a new bridge
- Enter a name (e.g., "LAN-Bridge") in the **Name** field and click **OK**

#### 2. Add Ports to the Bridge

- Select the newly created bridge
- Click **Ports** tab
- Click **+** to add a port
- Select the desired port from the dropdown list
- Click **OK**
- Repeat for other ports you want to add

**Example Configuration:**

```
/interface bridge add bridge=LAN-Bridge ports=ether1,ether2,ether3 name=LAN-Bridge
```

### Common Pitfalls and Solutions

* **Bridge not forwarding traffic:** Ensure that the bridge interface is enabled and all ports are added.
* **Devices on different ports cannot communicate:** Check if the IP addresses of the devices are in the same subnet.
* **Looping:** Avoid connecting the bridge back to itself.

### Verification and Testing Steps

* Check the **Bridge** > **Bridges** page, ensure that the bridge is **Up**
* Ping devices from different ports to verify connectivity
* Use the **Test** button in the **Bridge** > **Bridges** page to test bridge functionality

### Related Features and Considerations

* **Spanning Tree Protocol (STP)**: Can be used to prevent loops in bridged networks. Configure it under **Bridge** > **STP**.
* **Port Isolation**: Enable port isolation to prevent devices on different ports from communicating directly. Configure it under **Bridge** > **Ports**.
* **Security**: Use firewall rules to restrict access to and from the bridge. Configure it under **IP** > **Firewall**.
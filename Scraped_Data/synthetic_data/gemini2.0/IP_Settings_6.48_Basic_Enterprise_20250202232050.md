**IP Settings**

**Configuration Scenario and Requirements**

* Configure static and dynamic IP addresses for interfaces
* Assign IP settings to wireless interfaces
* Set up IP routing for internal and external networks

**Step-by-Step Implementation**

**Static IP Address Configuration**

1. Navigate to **IP** -> **Addresses**
2. Click **+** to add a new address
3. Specify the following parameters:
   - Interface: Select the interface to assign the IP address
   - Address: Enter the desired IP address
   - Network: Enter the network subnet mask
   - Gateway: Optional, enter the default gateway if required
4. Click **OK** to save the settings

**Dynamic IP Address Configuration on Wired Interfaces**

1. Navigate to **IP** -> **DHCP Client**
2. Click **+** to add a new client
3. Specify the interface to enable DHCP on
4. Click **OK** to save the settings

**IP Address Configuration for Wireless Interfaces**

1. Navigate to **Wireless** -> **Interfaces**
2. Select the desired wireless interface
3. In the **DHCP Server** tab:
   - Select **Static Address** or **DHCP**
   - For DHCP, specify the network subnet mask and default gateway if required
4. In the **Address Pool** tab, specify the range of IP addresses to assign to clients

**IP Routing Configuration**

1. Navigate to **IP** -> **Routes**
2. Click **+** to add a new route
3. Specify the following parameters:
   - Destination: Enter the destination network
   - Gateway: Enter the next-hop gateway
   - Distance: 0 for local routes, higher numbers for less preferred routes
4. Click **OK** to save the settings

**Complete Configuration Commands**

**Static IP Address Configuration**

```
/ip address add address=192.168.1.10/24 interface=ether1
```

**Dynamic IP Address Configuration**

```
/ip dhcp-client add interface=ether1
```

**IP Address Configuration for Wireless Interfaces**

```
/interface wireless set [wireless-interface] dhcp-server=yes address-pool=pool1
/ip pool add name=pool1 ranges=192.168.1.100-192.168.1.200
```

**IP Routing Configuration**

```
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.1
```

**Common Pitfalls and Solutions**

* **IP conflict:** Ensure that the assigned IP addresses do not conflict with any other devices on the network.
* **Gateway not reachable:** Ensure that the specified gateway is reachable and has a route to the destination network.
* **DNS issues:** If devices cannot resolve DNS names, configure DNS settings on the router.
* **Incorrect subnet mask:** The subnet mask must accurately reflect the network topology.

**Verification and Testing Steps**

* Use the **ping** command to test connectivity to different IP addresses.
* Check IP settings on the interfaces using the **/ip address print** command.
* Test IP routing by accessing a device on the destination network.

**Related Features and Considerations**

* **Address List:** Used to group IP addresses for filtering or traffic control.
* **Policy Routing:** Allows fine-grained control over IP routing decisions.
* **DHCP Server:** Enables automatic IP address assignment to clients.

**MikroTik REST API Examples**

**Get IP Addresses**

```
GET /ip/address
```

**Add a Static IP Address**

```
POST /ip/address
{
  "address": "192.168.1.10/24",
  "interface": "ether1"
}
```

**Set DHCP Server on Wireless Interface**

```
PUT /interface/wireless/[wireless-interface]
{
  "dhcp-server": "yes"
}
```

**Add IP Pool for Wireless Interface**

```
POST /ip/pool
{
  "name": "pool1",
  "ranges": "192.168.1.100-192.168.1.200"
}
```
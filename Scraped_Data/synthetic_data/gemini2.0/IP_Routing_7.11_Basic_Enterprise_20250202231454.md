## IP Routing

**Configuration Scenario and Requirements:**

* Configure Layer 3 routing on a MikroTik RouterOS device.
* Establish IP connectivity between three subnets: 192.168.1.0/24, 192.168.2.0/24, and 192.168.3.0/24.
* Use the device's two Ethernet interfaces as the gateway for the subnets.

**Step-by-Step Implementation:**

1. **Configure Ethernet Interfaces:**

   ```
   /interface ethernet set ether1 ip-address=192.168.1.1/24
   /interface ethernet set ether2 ip-address=192.168.2.1/24
   ```

2. **Create IP Routes:**

   ```
   /ip route add dst-address=192.168.3.0/24 gateway=192.168.2.2
   /ip route add dst-address=192.168.2.0/24 gateway=192.168.1.2
   ```

3. **Enable IP Forwarding:**

   ```
   /ip firewall set forward=enable
   ```

**Complete Configuration Commands:**

```
/interface ethernet set ether1 ip-address=192.168.1.1/24
/interface ethernet set ether2 ip-address=192.168.2.1/24
/ip route add dst-address=192.168.3.0/24 gateway=192.168.2.2
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.2
/ip firewall set forward=enable
```

**Common Pitfalls and Solutions:**

* Ensure the default gateway on devices in each subnet matches the IP address assigned to the corresponding Ethernet interface.
* Verify that all interfaces are properly connected to the appropriate network segments.
* Check the firewall rules to ensure traffic is allowed to traverse the router.

**Verification and Testing Steps:**

* Ping from a device in one subnet to a device in another subnet.
* Verify that devices can establish remote desktop connections across subnets.
* Run a traceroute to confirm the routing path.

**Related Features and Considerations:**

* **Routing Protocols:** Configure routing protocols (e.g., OSPF, RIP, BGP) for automatic routing updates.
* **DHCP Server:** Set up a DHCP server to automatically assign IP addresses to client devices.
* **Firewall Filtering:** Implement firewall rules to control network traffic and enhance security.

**REST API Examples:**

* **Get Interface IP Address:**

   **Endpoint:** `/interface/ethernet/print`

   **Request Method:** GET

   **Expected Response:**

   ```
   [
     {
       ".id": "ether1",
       "admin-status": "up",
       "address": "192.168.1.1/24",
       "disabled": false,
       "dynamic": false,
       "interface": "ether1",
       "link-up": true,
       "mac-address": "00:00:00:00:00:01",
       "mtu": 1500,
       "name": "ether1",
       "running": true,
       "speed": 1000,
       "type": "ethernet"
     }
   ]
   ```

* **Add IP Route:**

   **Endpoint:** `/ip/route/add`

   **Request Method:** POST

   **Example JSON Payload:**

   ```
   {
     "dst-address": "192.168.3.0/24",
     "gateway": "192.168.2.2"
   }
   ```

   **Expected Response:**

   ```
   {
     ".id": "3"
   }
   ```
**IP Pools**

**Configuration Scenario and Requirements**

* Configure multiple IP address pools for dynamic IP address assignment to clients on an ISP network.
* Pools should be assigned to VLANs for subnet segmentation.

**Step-by-Step Implementation**

**1. Create IP Pools**

* Navigate to **IP** > **Pool** menu in RouterOS configuration.
* Click on the **+** button to create a new pool.
* Configure the **Name**, **Ranges** (IP address range), and **Comment** (optional).
* Repeat this process to create additional pools.

```
/ip pool add name=pool1 ranges=192.168.10.1-192.168.10.254
/ip pool add name=pool2 ranges=192.168.20.1-192.168.20.254
/ip pool add name=pool3 ranges=192.168.30.1-192.168.30.254
```

**2. Assign Pools to VLANs**

* Navigate to **IP** > **DHCP Server** menu.
* Click on the **Interfaces** tab.
* Select the VLAN interface (e.g., ether5).
* In the **DHCP Server** section, select the desired pool from the **Pool** dropdown list.

```
/interface ethernet set ether5 dhcp-server=pool1
/interface ethernet set ether6 dhcp-server=pool2
/interface ethernet set ether7 dhcp-server=pool3
```

**3. Enable DHCP Service**

* Navigate to **IP** > **DHCP Server** menu.
* Click on the **Setup** tab.
* Ensure that the **Enabled** option is checked.

```
/ip dhcp-server set enabled=yes
```

**Common Pitfalls and Solutions**

* **IP address conflict:** Ensure that there are no overlapping IP pools defined.
* **DHCP server not responding:** Verify that the DHCP server is enabled and the correct pool is assigned to the VLAN interface.
* **Incorrect subnet mask:** Ensure that the correct subnet mask is specified for each pool.

**Verification and Testing Steps**

* Connect a client device to a VLAN port.
* Use the `ipconfig` command on Windows or `ifconfig` on Linux to check the IP address assigned to the client.
* Verify that the IP address is within the range of the assigned pool.

**Related Features and Considerations**

* **Lease time:** Configure the lease time for IP addresses assigned from the pool.
* **Static leases:** Reserve specific IP addresses for specific devices by creating static leases.
* **DHCP options:** Assign specific DHCP options to clients, such as DNS servers and gateway addresses.

**MikroTik REST API Examples**

**Endpoint:** `/ip/pool`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "name": "pool1",
  "ranges": ["192.168.10.1-192.168.10.254"]
}
```

**Expected Response:**

```json
{
  "id": 1,
  "name": "pool1",
  "ranges": ["192.168.10.1-192.168.10.254"]
}
```
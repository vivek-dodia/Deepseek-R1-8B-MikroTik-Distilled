**Topic: IP Settings**

**1. Configuration Scenario and Requirements**

* Configure IP settings for multiple interfaces on a MikroTik router.
* Assign IP addresses, subnet masks, and default gateways.
* Enable IPv6 connectivity.

**2. Step-by-Step Implementation**

**IPv4 Configuration**

1. Open WinBox and connect to the router.
2. Navigate to **IP > Addresses**.
3. Click the **+** button.
4. Select the interface to configure.
5. Enter the IP address and subnet mask.
6. Specify the default gateway (optional).
7. Click **OK** to save.

**IPv6 Configuration**

1. In the **IP > Addresses** window, click the **+** button.
2. Select the interface to configure.
3. Choose the **IPv6** tab.
4. Enter the IPv6 address and prefix length.
5. Specify the default gateway (optional).
6. Click **OK** to save.

**3. Complete Configuration Commands**

**IPv4 Configuration**

```
/ip address
add address=192.168.1.1/24 interface=ether1
add default-gateway=192.168.1.254
```

**IPv6 Configuration**

```
/ip address
add address=2001:db8::1/64 interface=ether1
add default-gateway=2001:db8::2
```

**4. Common Pitfalls and Solutions**

* **Incorrect IP address or subnet mask:** Verify that the IP address and subnet mask are correct for the network configuration.
* **IP conflict:** Ensure that the IP address is not already in use by another device on the network.
* **Invalid default gateway:** Check that the default gateway is accessible and has a route to the desired destination.
* **IPv6 prefix mismatch:** Make sure that the IPv6 prefix length matches the number of bits in the subnet mask.

**5. Verification and Testing Steps**

* **IPv4:** Use the following command to verify the IPv4 configuration:

```
/ip address print
```

* **IPv6:** Use the following command to verify the IPv6 configuration:

```
/ip address print detail
```

* **Connectivity:** Test connectivity by pinging an external IP address.

**6. Related Features and Considerations**

* **IP Pool:** Allows dynamic assignment of IP addresses to clients.
* **IP Routing:** Enables the router to forward packets between different networks.
* **RoMON:** Provides remote monitoring and management capabilities.

**7. MikroTik REST API Examples**

**IPv4 Configuration**

**Endpoint:** /api/ip/address

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "address": "192.168.1.1/24",
  "interface": "ether1",
  "default-gateway": "192.168.1.254"
}
```

**Expected Response:**

```json
{
  "id": "1"
}
```

**IPv6 Configuration**

**Endpoint:** /api/ipv6/address

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "address": "2001:db8::1/64",
  "interface": "ether1",
  "default-gateway": "2001:db8::2"
}
```

**Expected Response:**

```json
{
  "id": "1"
}
```
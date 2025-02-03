**IP Settings**

**Configuration Scenario and Requirements**

* Configure IP addresses, subnets, and default gateways for multiple interfaces on a MikroTik RouterOS device running version 7.11.
* Enable and configure IP forwarding.

**Step-by-Step Implementation**

**1. Configuring IP Addresses**

* Navigate to **IP > Addresses** in WinBox.
* Click the **+** button to create a new IP address configuration.
* Select the desired interface from the **Interface** drop-down menu.
* Specify the IP address and subnet mask in the respective fields.
* Enable **Use Gateway** and enter the default gateway IP address.
* Click **Apply**.

**2. Enabling IP Forwarding**

* Navigate to **IP > Routing** in WinBox.
* Click the **General** tab.
* Enable the **Enable IP Forwarding** option.
* Click **Apply**.

**Complete Configuration Commands**

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=192.168.2.1/24 interface=ether2
/ip address add address=192.168.3.1/24 interface=ether3
/ip routing enable
```

**Common Pitfalls and Solutions**

* **Incorrect IP address or subnet mask:** Verify that the specified IP address and subnet mask match the network requirements.
* **Gateway is not reachable:** Ensure that the configured default gateway is accessible from the router.
* **IP forwarding is not enabled:** Make sure that the **Enable IP Forwarding** option is enabled under **IP > Routing > General**.

**Verification and Testing Steps**

* Use the **IP > Addresses > Ping** tool to test connectivity to other hosts on the network.
* Verify that data traffic can be forwarded between interfaces using a packet sniffing tool.

**Related Features and Considerations**

* **DHCP Server:** RouterOS can be configured as a DHCP server to automatically assign IP addresses to clients.
* **Firewall:** Consider implementing a firewall to control inbound and outbound traffic based on IP addresses.
* **NAT:** Network Address Translation (NAT) can be used to translate private IP addresses to public IP addresses.

**REST API Examples**

**Create an IP Address**
**Endpoint:** `/ip/address/add`
**Method:** POST
**Request Payload:**
```json
{
  "address": "192.168.1.1/24",
  "interface": "ether1"
}
```
**Expected Response:**
```json
{
  "id": 1
}
```

**Enable IP Forwarding**
**Endpoint:** `/ip/routing/general/set`
**Method:** PUT
**Request Payload:**
```json
{
  "enable-ip-forwarding": true
}
```
**Expected Response:**
```json
{
  "id": 1
}
```
**IP Settings**

**Configuration Level:** Basic

**Network Scale:** SMB

**1. Configuration Scenario and Requirements**

Configure IP settings for a MikroTik router to provide connectivity to devices on a local area network. The router should have a static IP address, a DHCP server to assign IP addresses to clients, and firewall rules to protect the network.

**2. Step-by-Step Implementation**

**2.1. Static IP Address**

* Open Winbox and connect to the router.
* Navigate to **IP > Addresses** tab.
* Click the **+** button.
* Configure the following parameters:
    - Interface: Select the physical interface to assign the static IP address.
    - Address: Enter the static IP address.
    - Network: Enter the network address.
    - Gateway: Enter the gateway address.
* Click **Apply**.

**2.2. DHCP Server**

* Navigate to **IP > DHCP Server** tab.
* Click the **+** button.
* Configure the following parameters:
    - Name: Enter a name for the DHCP server.
    - Interface: Select the interface to enable DHCP on.
    - Address Pool: Define the range of IP addresses that will be assigned to clients.
    - Lease Time: Set the duration for which IP addresses will be leased to clients.
* Click **Apply**.

**2.3. Firewall Rules**

* Navigate to **IP > Firewall** tab.
* Click the **+** button to create a new firewall rule.
* Configure the following parameters:
    - Action: Select **accept**.
    - Chain: Select **input** to allow incoming connections.
    - In. Interface: Select the interface to allow connections from.
* Click **Apply**.

**3. Complete Configuration Commands**

```text
/ip address add address=192.168.1.1/24 interface=ether1
/ip dhcp-server add address-pool=192.168.1.10-192.168.1.254 interface=ether1 lease-time=4h
/ip firewall filter add action=accept chain=input in-interface=ether1
```

**4. Common Pitfalls and Solutions**

* **IP Address Conflict:** Ensure that the static IP address is not already in use on the network.
* **DHCP Lease Time:** Set the lease time long enough to avoid frequent IP address changes.
* **Firewall Blockage:** Ensure that the firewall rules allow traffic from the intended sources and ports.

**5. Verification and Testing Steps**

* Check the static IP address assignment by running the command ```/ip address print```.
* Test DHCP server functionality by assigning IP addresses to clients.
* Test firewall functionality by attempting to access services from external sources.

**6. Related Features and Considerations**

* **MAC Address Filtering:** Use MAC address filtering to allow or deny connections from specific devices.
* **NAT:** Configure NAT to allow devices on the local network to access the Internet.
* **DNS:** Set up DNS to allow devices to resolve domain names to IP addresses.

**7. MikroTik REST API Examples**

**Endpoint:** `/ip/address`

**Request Method:** GET

**Request:**

```json
{
  "interface": "ether1"
}
```

**Response:**

```json
[
  {
    "address": "192.168.1.1/24",
    "interface": "ether1"
  }
]
```

**Endpoint:** `/ip/dhcp-server`

**Request Method:** POST

**Request:**

```json
{
  "name": "dhcp1",
  "interface": "ether1",
  "address-pool": "192.168.1.10-192.168.1.254",
  "lease-time": "4h"
}
```

**Response:**

```json
{
  "name": "dhcp1",
  "interface": "ether1"
}
```
**IP Settings**

**Configuration Scenario and Requirements**

* Configure IP addresses for network interfaces
* Assign IP addresses dynamically using DHCP

**Step-by-Step Implementation**

**IPv4 Addressing**

1. Access the RouterOS terminal (e.g., via SSH or WinBox)
2. Navigate to the "IP" menu
3. Select "Addresses"
4. Click the "+" button to add a new IP address
5. In the "Interface" field, select the network interface to assign the IP address
6. In the "Address" field, enter the IP address (e.g., 192.168.1.1)
7. Click "OK" to save the configuration

**IPv6 Addressing**

1. Access the RouterOS terminal
2. Navigate to the "IPv6" menu
3. Select "Addresses"
4. Click the "+" button to add a new IPv6 address
5. In the "Interface" field, select the network interface to assign the IPv6 address
6. In the "Address" field, enter the IPv6 address (e.g., fe80::1)
7. Click "OK" to save the configuration

**DHCP Server**

1. Access the RouterOS terminal
2. Navigate to the "IP" menu
3. Select "DHCP Server"
4. Click the "+" button to add a new DHCP server
5. In the "Interface" field, select the network interface to run the DHCP server on
6. In the "Address Pool" field, enter the range of IP addresses to be leased (e.g., 192.168.1.100-192.168.1.200)
7. In the "Lease Time" field, specify the duration of the IP lease (e.g., 1 day)
8. Click "OK" to save the configuration

**Complete Configuration Commands**

```
/ip address add interface=ether1 address=192.168.1.1 (for IPv4)
/ipv6 address add interface=ether1 address=fe80::1 (for IPv6)
/ip dhcp-server add interface=ether1 address-pool=pool1 lease-time=1d (for DHCP server)
```

**Common Pitfalls and Solutions**

* Ensure that the network interface is enabled and has a physical connection.
* Verify that the IP addresses are configured correctly.
* If DHCP is not working, check the server settings and ensure that the IP pool is not exhausted.

**Verification and Testing Steps**

* Use the "ip address print" command to display the configured IP addresses.
* Use the "ip dhcp-server lease print" command to verify DHCP lease information.
* Use a ping command to test connectivity to an external host from the RouterOS device.

**Related Features and Considerations**

* NAT: Network Address Translation can be used to translate the internal IP addresses to a single public IP address.
* Firewall: Configure firewall rules to allow or block specific traffic based on IP addresses.
* DNS: Configure DNS settings to enable name resolution.

**MikroTik REST API Examples**

**Create an IP Address:**

**API Endpoint:** `/api/ip/address`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "interface": "ether1",
  "address": "192.168.1.1/24"
}
```

**Expected Response:**

```json
{
  "id": 1,
  "interface": "ether1",
  "address": "192.168.1.1/24"
}
```

**Get DHCP Server Leases:**

**API Endpoint:** `/api/ip/dhcp-server/lease`

**Request Method:** GET

**Example JSON Response:**

```json
[
  {
    "id": 1,
    "server": "dhcp-server1",
    "interface": "ether1",
    "address": "192.168.1.101",
    "mac-address": "AA:BB:CC:DD:EE:FF",
    "expires": "2023-03-08T15:30:00Z"
  },
  {
    "id": 2,
    "server": "dhcp-server1",
    "interface": "ether1",
    "address": "192.168.1.102",
    "mac-address": "AA:BB:CC:DD:EE:FF",
    "expires": "2023-03-09T15:30:00Z"
  }
]
```
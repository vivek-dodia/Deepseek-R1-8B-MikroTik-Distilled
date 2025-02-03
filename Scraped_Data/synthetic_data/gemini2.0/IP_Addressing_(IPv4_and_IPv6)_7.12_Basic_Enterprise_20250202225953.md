## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

* Configure IPv4 and IPv6 addresses on a RouterOS device
* Set up IPpools to automatically assign IP addresses to clients
* Implement IP routing to enable communication between different networks

### Step-by-Step Implementation

#### IPv4 Address Configuration

1. Go to IP -> Addresses
2. Click the "+" button to create a new address
3. Enter the IP address, subnet mask, and interface
4. Click "Apply" to save the configuration

**Example:**

```
/ip address add address=192.168.1.1/24 interface=ether1
```

#### IPv6 Address Configuration

1. Navigate to IP -> Addresses
2. Click the "+" button
3. Select the "IPv6 Address" tab
4. Enter the IPv6 address, prefix length, and interface
5. Click "Apply" to save the configuration

**Example:**

```
/ip address add address=2001:db8::1/64 interface=ether2
```

#### IP Pool Configuration

1. Go to IP -> Pool
2. Click the "+" button to create a new pool
3. Enter a pool name, network address range, and interface
4. Click "Apply" to save the configuration

**Example:**

```
/ip pool add name=dhcp-pool ranges=192.168.1.10-192.168.1.254 interfaces=ether1
```

#### IP Routing Configuration

1. Navigate to IP -> Routes
2. Click the "+" button to create a new route
3. Enter the destination network, gateway address, and interface
4. Click "Apply" to save the configuration

**Example:**

```
/ip route add dst-address=10.0.0.0/24 gateway=192.168.1.1
```

### Common Pitfalls and Solutions

* **IPv4/IPv6 Address Conflict:** Ensure that the IP addresses assigned to the device do not conflict with existing addresses on the network.
* **Incorrect Subnet Mask or Prefix Length:** Verify that the subnet mask or prefix length is correct for the network topology.
* **No Default Gateway:** Configure a default gateway to enable internet access and communication with other networks.

### Verification and Testing Steps

* Use the "/ip address print" command to display the IP addresses configured on the device.
* Use the "/ip pool print" command to view the IP pools and their assigned addresses.
* Use the "/ip route print" command to check the active routing table.
* Use the "ping" command to test connectivity to different IP addresses.

### Related Features and Considerations

* DHCP Server: Configure a DHCP server to automatically assign IP addresses to clients.
* NAT: Enable Network Address Translation (NAT) to allow internal devices to access the internet.
* VLANs: Use VLANs to segment the network and isolate traffic.
* Firewall: Implement a firewall to control incoming and outgoing traffic.

### MikroTik REST API Examples

**Get IPv4 Address List:**

* Endpoint: `/ip/address/print`
* Request Method: GET
* Response:
```json
[
  {
    "address": "192.168.1.1/24",
    "disabled": false,
    "interface": "ether1"
  }
]
```

**Create IPv6 Address:**

* Endpoint: `/ip/address/add`
* Request Method: POST
* Request Body:
```json
{
  "address": "2001:db8::1/64",
  "interface": "ether2"
}
```

**Get IP Pool List:**

* Endpoint: `/ip/pool/print`
* Request Method: GET
* Response:
```json
[
  {
    "name": "dhcp-pool",
    "ranges": [
      "192.168.1.10-192.168.1.254"
    ],
    "interfaces": [
      "ether1"
    ]
  }
]
```
## IP Addressing (IPv4 and IPv6)

### Configuration Scenario and Requirements

* Configure IP addresses on multiple interfaces.
* Assign static IP addresses to clients.
* Enable DHCP server to automatically assign IP addresses to clients.
* Configure IPv6 addresses and routes.

### Step-by-Step Implementation

#### IPv4 Configuration

1. Open WinBox and connect to your MikroTik router.
2. Navigate to **IP** > **Addresses**.
3. Click the **+** icon to create a new IP address.
4. Enter the following parameters:
    - **Interface:** Select the interface you want to assign the IP address to.
    - **Address:** Enter the IP address in dotted-decimal notation.
    - **Netmask:** Enter the netmask for the IP address.
    - **Gateway:** Enter the default gateway for the interface.
5. Click **Apply** to save the changes.

#### IPv6 Configuration

1. Navigate to **IP** > **Addresses**.
2. Click the **+** icon to create a new IP address.
3. Enter the following parameters:
    - **Interface:** Select the interface you want to assign the IPv6 address to.
    - **Address:** Enter the IPv6 address in colon-hexadecimal notation.
    - **Prefix length:** Enter the prefix length for the IPv6 address.
4. Click **Apply** to save the changes.

#### DHCP Server Configuration

1. Navigate to **IP** > **DHCP Server**.
2. Click the **+** icon to create a new DHCP server.
3. Enter the following parameters:
    - **Interface:** Select the interface you want to enable DHCP on.
    - **Address pool:** Enter the range of IP addresses that the DHCP server will assign to clients.
    - **Netmask:** Enter the netmask for the DHCP server.
    - **Gateway:** Enter the default gateway for the DHCP server.
4. Click **Apply** to save the changes.

### Complete Configuration Commands

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=2001:db8::1/64 interface=ether1
/ip dhcp-server add interface=ether1 address-pool=192.168.1.10-192.168.1.20 netmask=255.255.255.0 gateway=192.168.1.1
```

### Common Pitfalls and Solutions

* **Unable to ping the default gateway:** Verify that the default gateway address is correct and that the gateway is online.
* **DHCP clients not getting IP addresses:** Ensure that the DHCP server is enabled and that the clients are on the correct subnet.
* **IPv6 addresses not working:** Make sure that the IPv6 addresses are properly configured and that the router is advertising IPv6 routes.

### Verification and Testing Steps

* Test IPv4 connectivity by pinging an external host.
* Test IPv6 connectivity by pinging an IPv6 address.
* Verify that DHCP clients are receiving IP addresses by checking the DHCP lease list.

### Related Features and Considerations

* **IP Pools:** Allows you to manage multiple IP address pools for different subnets.
* **IP Routing:** Configure routing protocols to connect different subnets.
* **IP Settings:** Configure global IP settings such as DNS servers and NTP servers.

### MikroTik REST API Examples

#### Add IPv4 Address

**API Endpoint:** `/ip/address/add`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "address": "192.168.1.1/24",
  "interface": "ether1"
}
```

**Expected Response:**

```json
{
  "status": "success"
}
```

#### Add IPv6 Address

**API Endpoint:** `/ip/address/add`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "address": "2001:db8::1/64",
  "interface": "ether1"
}
```

**Expected Response:**

```json
{
  "status": "success"
}
```

#### Add DHCP Server

**API Endpoint:** `/ip/dhcp-server/add`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "interface": "ether1",
  "address-pool": "192.168.1.10-192.168.1.20",
  "netmask": "255.255.255.0",
  "gateway": "192.168.1.1"
}
```

**Expected Response:**

```json
{
  "status": "success"
}
```
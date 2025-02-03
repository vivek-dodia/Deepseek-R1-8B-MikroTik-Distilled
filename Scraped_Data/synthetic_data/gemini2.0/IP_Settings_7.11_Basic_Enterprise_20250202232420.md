## IP Settings

### Configuration Scenario and Requirements

* Configure IP addresses, subnet masks, and default gateways on multiple interfaces.
* Set static IP addresses for hosts on the network.
* Configure IP pools to assign dynamic IP addresses to hosts.
* Enable DHCP server and DNS services.

### Step-by-Step Implementation

**1. Configure IP Addresses**

```bash
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=10.0.0.1/8 interface=ether2
```

**2. Set Static IP Addresses**

```bash
/ip address add address=192.168.1.100/24 interface=ether1 mac-address=00:11:22:33:44:55
/ip dhcp-server add address-pool=pool1 address=192.168.1.101-192.168.1.254 lease-time=24h
```

**3. Enable DHCP Server**

```bash
/ip dhcp-server add interface=ether1 enabled=yes
```

**4. Enable DNS Services**

```bash
/ip dns enable=yes
/ip dns static add name=www.example.com address=8.8.8.8
```

### Complete Configuration Commands

```bash
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=10.0.0.1/8 interface=ether2
/ip address add address=192.168.1.100/24 interface=ether1 mac-address=00:11:22:33:44:55
/ip dhcp-server add address-pool=pool1 address=192.168.1.101-192.168.1.254 lease-time=24h
/ip dhcp-server add interface=ether1 enabled=yes
/ip dns enable=yes
/ip dns static add name=www.example.com address=8.8.8.8
```

### Common Pitfalls and Solutions

* Ensure the configured IP addresses are valid and not already in use.
* Verify that the default gateway is reachable from the interface being configured.
* If DHCP server is enabled, ensure the pool size is sufficient for the number of connected devices.

### Verification and Testing Steps

* Use the `/ip address print` command to view configured IP addresses.
* Use the `/ip dhcp-server print` command to verify DHCP server settings.
* Use the `/ip dns print` command to view DNS settings.
* Use the `ping` tool to test connectivity to configured IP addresses and DNS servers.

### Related Features and Considerations

* IP Firewall and QoS settings
* DHCP relay
* NAT and port forwarding

### MikroTik REST API Examples

**Get IP Address List**

**API Endpoint:** `/ip/address`

**Request Method:** GET

**Example JSON Payload:**

```json
{}
```

**Expected Response:**

```json
[
  {
    "address": "192.168.1.1/24",
    "interface": "ether1",
    "mac-address": "00:11:22:33:44:55"
  },
  {
    "address": "10.0.0.1/8",
    "interface": "ether2"
  }
]
```

**Add Static IP Address**

**API Endpoint:** `/ip/address`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "address": "192.168.1.100/24",
  "interface": "ether1",
  "mac-address": "00:11:22:33:44:55"
}
```

**Expected Response:**

```json
{
  "address": "192.168.1.100/24",
  "interface": "ether1",
  "mac-address": "00:11:22:33:44:55"
}
```
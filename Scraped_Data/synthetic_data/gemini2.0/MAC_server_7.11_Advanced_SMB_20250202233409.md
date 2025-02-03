## MAC Server

**Configuration Scenario and Requirements**

* Manage MAC addresses and assign IP addresses dynamically
* Limit access to the network based on MAC addresses
* Monitor and track MAC addresses on the network

**Step-by-Step Implementation**

1. **Enable MAC Server**

```
/ip mac-server set [interface] enabled=yes
```

2. **Create MAC Pool**

```
/ip mac-server pool add name=[pool-name]
```

3. **Add MAC Addresses to Pool**

```
/ip mac-server pool [pool-name] add mac=[mac-address]
```

4. **Enable DHCP Client**

```
/ip dhcp-client add interface=[interface] pool=[pool-name]
```

5. **Configure Firewall**

```
/ip firewall filter add chain=forward action=accept dst-address=[address-range] mac-address=[mac-address]
```

**Complete Configuration Commands**

```
/ip mac-server set [interface] enabled=yes
/ip mac-server pool add name=[pool-name]
/ip mac-server pool [pool-name] add mac=[mac-address]
/ip dhcp-client add interface=[interface] pool=[pool-name]
/ip firewall filter add chain=forward action=accept dst-address=[address-range] mac-address=[mac-address]
```

**Common Pitfalls and Solutions**

* **MAC addresses not being assigned:** Ensure the DHCP client is enabled on the interface and the MAC pool contains the correct MAC addresses.
* **Network access not being restricted:** Verify that the firewall rules are configured correctly and the MAC addresses of unauthorized devices are not present in the pool.

**Verification and Testing Steps**

* Check the MAC server statistics using `/ip mac-server stats`.
* Connect a device with a known MAC address and verify that it receives an IP address from the assigned pool.
* Attempt to connect a device with an unauthorized MAC address and verify that access is denied.

**Related Features and Considerations**

* **DHCP Leases:** MAC server can be integrated with DHCP leases to manage IP address assignments.
* **Static MAC Addresses:** Static MAC addresses can be assigned to specific devices for manual control.
* **MAC Address Scanning:** Regular MAC address scans can identify unauthorized or rogue devices on the network.

**MikroTik REST API Examples**

**Endpoint:** `/api/ip/mac-server`

**Request Method:** GET

**Example JSON Payload:**

```json
{
  "id": 1,
  "method": "getall",
}
```

**Expected Response:**

```json
[
  {
    "enabled": true,
    "interface": "ether1",
    "name": "default"
  }
]
```
**MAC Server**

**Configuration Scenario and Requirements:**

* Establish a MAC server to provide dynamic IP address assignment based on MAC addresses.

**Step-by-Step Implementation:**

1. **Enable DHCP Server:**
   ```
   /ip dhcp-server add interface=ether1
   ```

2. **Create a MAC Pool:**
   ```
   /ip dhcp-server pool add address-pool=MACPool range=192.168.1.100-192.168.1.200 mac-server=yes
   ```

3. **Configure MAC Address Learning:**
   ```
   /interface ethernet set ether1 mac-address-learning=yes
   ```

4. **Link DHCP Server to MAC Pool:**
   ```
   /ip dhcp-server network add network=192.168.1.0/24 pool=MACPool
   ```

**Complete Configuration Commands:**

```
/ip dhcp-server add interface=ether1
/ip dhcp-server pool add address-pool=MACPool range=192.168.1.100-192.168.1.200 mac-server=yes
/interface ethernet set ether1 mac-address-learning=yes
/ip dhcp-server network add network=192.168.1.0/24 pool=MACPool
```

**Common Pitfalls and Solutions:**

* **Incorrect MAC Pool Range:** Ensure the specified IP range is not overlapping with any existing IP assignments.
* **Disabled MAC Address Learning:** Verify that MAC address learning is enabled on the interface used by the DHCP server.

**Verification and Testing Steps:**

* **Check MAC Address Learning:** Use the `/interface print` command to confirm that MAC addresses are being learned on the interface.
* **Test DHCP Connectivity:** Connect a device to the network and verify that it obtains an IP address from the MAC server.

**Related Features and Considerations:**

* **Static MAC Entries:** Manually add specific MAC addresses to the MAC server using `/ip dhcp-server lease add` commands.
* **MAC Address Filtering:** Use the `/ip firewall filter` to restrict access based on MAC addresses.
* **DHCP Snooping:** Enable DHCP snooping on switch ports to prevent unauthorized IP address assignments.

**MikroTik REST API Examples:**

**API Endpoint:** `/api/ip/dhcp-server/mac-server`

**Request Method:** GET

**JSON Payload:**

```json
{
  "interface": "ether1",
  "address-pool": "MACPool"
}
```

**Expected Response:**

```json
{
  "interface": "ether1",
  "address-pool": "MACPool",
  "mac-server": true
}
```
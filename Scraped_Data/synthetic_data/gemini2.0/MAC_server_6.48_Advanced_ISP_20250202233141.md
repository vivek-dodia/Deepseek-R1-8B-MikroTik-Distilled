**Topic: MAC Server**

**Configuration Scenario and Requirements**

The MAC server feature in MikroTik RouterOS allows for centralized management of MAC addresses on a network. It is commonly used by ISPs to assign and manage public IP addresses dynamically to subscribers based on their MAC addresses.

**Step-by-Step Implementation**

**1. Configure IP Address Pool**

- Create an IP address pool for dynamic IP allocation.
```
/ip pool
add name=dhcp-pool range=192.168.1.10-192.168.1.254
```

**2. Configure MAC Server**

- Enable the MAC server feature and link it to the IP pool.
```
/ip dhcp-server
set mac-server=yes mac-server-pool=dhcp-pool
```

- Define a MAC binding for a specific MAC address and hostname.
```
/ip mac-server
add mac-address=AA:BB:CC:DD:EE:FF host="my-customer"
```

**3. Enable DHCP Server**

- Configure the DHCP server on the same interface as the MAC server.
```
/ip dhcp-server
set interface=ether1
```

**Complete Configuration Commands**

```
/ip pool
add name=dhcp-pool range=192.168.1.10-192.168.1.254
/ip dhcp-server
set mac-server=yes mac-server-pool=dhcp-pool
/ip mac-server
add mac-address=AA:BB:CC:DD:EE:FF host="my-customer"
/ip dhcp-server
set interface=ether1
```

**Common Pitfalls and Solutions**

- **MAC address not assigned:** Verify that the MAC address is correctly entered and that the host is connected to the network.
- **IP address conflict:** Ensure that the IP address pool does not overlap with any existing IP assignments on the network.
- **MAC server not enabled:** Double-check the MAC server settings and make sure it is enabled (`/ip dhcp-server set mac-server=yes`).

**Verification and Testing Steps**

- **MAC Binding Verification:** Check the `/ip mac-server` menu to confirm that the MAC binding is present.
- **IP Lease Verification:** Use the `/ip address` menu to verify that the client has obtained an IP address from the DHCP pool.
- **Connectivity Test:** Ping the client from another device on the network to ensure connectivity.

**Related Features and Considerations**

- **IP Pool Exhaustion:** Monitor the pool size and consider expanding it if necessary.
- **MAC Address Spoofing:** Implement security measures to prevent unauthorized MAC addresses from gaining access to the network.
- **Lease Time:** Adjust the DHCP lease time to suit your network requirements.

**MikroTik REST API Examples**

**Create a MAC Binding:**

```json
POST /api/ip/dhcp-server/mac-server
{
    "mac-address": "AA:BB:CC:DD:EE:FF",
    "host": "my-customer"
}
```

**Expected Response:**

```json
{
    "id": "2"
}
```

**Get MAC Binding:**

```json
GET /api/ip/dhcp-server/mac-server/2
```

**Expected Response:**

```json
{
    "id": "2",
    "mac-address": "AA:BB:CC:DD:EE:FF",
    "host": "my-customer"
}
```
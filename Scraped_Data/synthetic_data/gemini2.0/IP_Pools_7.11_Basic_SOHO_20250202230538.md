**IP Pools**

**Configuration Scenario and Requirements:**

- Create an IP pool for dynamic IP address assignment to DHCP clients.
- The pool should have a range of IP addresses, a netmask, a gateway, and a DNS server.

**Step-by-Step Implementation:**

1. **Create IP Pool:**
   - Navigate to **IP** > **Pool** in the RouterOS web interface.
   - Click **+** to add a new pool.
   - Configure the following parameters:
     - **Name:** Assign a name to the pool for identification.
     - **Ranges:** Specify the range of IP addresses available for assignment.
     - **Network:** Enter the netmask for the pool.
     - **Gateway:** Define the gateway address for the pool.
     - **DNS Servers:** List the DNS server addresses separated by spaces.

2. **Link IP Pool to DHCP Server:**
   - Navigate to **IP** > **DHCP Server**.
   - Select the desired DHCP server interface from the **Interface** dropdown.
   - Click on the **Address Pools** tab.
   - Click **+** to add the newly created IP pool to the DHCP server.
   - Click **Apply** to save the changes.

**Complete Configuration Commands:**

```
/ip pool add name=<pool_name> ranges=<ip_range> network=<netmask> gateway=<gateway> dns-server=<dns_server1>,<dns_server2>,...
/ip dhcp-server add interface=<interface> address-pool=<pool_name>
```

**Common Pitfalls and Solutions:**

- **IP Range Conflict:** Ensure that the IP address range specified for the pool does not overlap with any existing IP address ranges on the network.
- **Gateway Address Error:** Verify that the specified gateway address is accessible from the DHCP clients.
- **DNS Server Connectivity:** Ensure that the DNS servers listed in the pool configuration are reachable and functional.

**Verification and Testing Steps:**

- Connect a DHCP client to the network and verify that it receives an IP address from the pool.
- Test internet connectivity and DNS resolution to confirm proper configuration.

**Related Features and Considerations:**

- **Static IP Address Reservation:** You can reserve specific IP addresses within the pool for fixed devices by creating static leases in the **DHCP Server** configuration.
- **Lease Time:** Set the appropriate lease time for IP addresses assigned from the pool to balance flexibility and network optimization.
- **IP Address Management:** Use the **IP** > **Leases** section to view and manage currently assigned IP addresses and their lease status.

**MikroTik REST API Examples:**

**Create IP Pool:**
**Endpoint:** `/ip/pool/add`
**Request Method:** POST
**JSON Payload:**
```json
{
  "name": "<pool_name>",
  "ranges": [[<start_ip>, <end_ip>]],
  "network": "<netmask>",
  "gateway": "<gateway>",
  "dns-server": ["<dns_server1>", "<dns_server2>", ...]
}
```
**Response:**
```json
{
  "name": "<pool_name>",
  "ranges": [[<start_ip>, <end_ip>]],
  "network": "<netmask>",
  "gateway": "<gateway>",
  "dns-server": ["<dns_server1>", "<dns_server2>", ...]
}
```

**Link IP Pool to DHCP Server:**
**Endpoint:** `/ip/dhcp-server/add`
**Request Method:** POST
**JSON Payload:**
```json
{
  "interface": "<interface>",
  "address-pool": "<pool_name>"
}
```
**Response:**
```json
{
  "interface": "<interface>",
  "address-pool": "<pool_name>"
}
```
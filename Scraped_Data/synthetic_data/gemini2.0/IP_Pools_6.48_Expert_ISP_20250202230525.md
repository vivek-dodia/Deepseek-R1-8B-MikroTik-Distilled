**IP Pools**

**1. Configuration Scenario and Requirements**

- Create an IP pool to assign IP addresses to clients on a specific subnet.
- The IP pool should use the DHCP protocol to automatically allocate IP addresses.
- The IP pool should have a specified range of IP addresses that can be assigned.

**2. Step-by-Step Implementation**

1. In WinBox, navigate to "IP" -> "Pool" and click the "+" button.
2. In the "Name" field, enter a name for the IP pool (e.g., MyIPPool).
3. In the "Ranges" field, specify the range of IP addresses that should be allocated (e.g., 192.168.1.10-192.168.1.20).
4. In the "Interface" field, select the interface that the IP pool should be used on (e.g., ether1).
5. In the "DHCP Server" tab, enable "DHCP Server" and configure the following parameters:
   - Address Pool: Use the previously specified IP address range.
   - DNS Server: Specify the IP address of the DNS server to be used by clients.
   - Gateway: Specify the gateway IP address for the subnet.
6. Click "OK" to save the IP pool configuration.

**3. Complete Configuration Commands**

```
/ip pool add name=MyIPPool ranges=192.168.1.10-192.168.1.20 interface=ether1
/ip dhcp-server add address-pool=MyIPPool dns-server=192.168.1.1 gateway=192.168.1.1
```

**4. Common Pitfalls and Solutions**

- Ensure that the IP address range specified is not already in use on the network.
- If clients are not able to obtain IP addresses, verify that the DHCP server is running and that the interface is configured correctly.
- Check that any firewall rules or Access Control Lists (ACLs) are not blocking the DHCP traffic.

**5. Verification and Testing Steps**

- Use the "ping" command to test whether clients can reach the DHCP server.
- Use the "ip address print" command to verify that clients have been assigned IP addresses from the IP pool.
- Check the DHCP server logs for any errors or warnings.

**6. Related Features and Considerations**

- IP pools can be used in conjunction with NAT to provide internet access to clients.
- IP pools can be used with captive portals to authenticate clients before granting them access to the network.

**7. Mikrotik REST API Examples**

**API Endpoint:** `/ip/pool`

**Request Method:** `GET`

**Example JSON Payload:**

```json
{
  "interface": "ether1",
  "name": "MyIPPool",
  "ranges": [
    "192.168.1.10-192.168.1.20"
  ]
}
```

**Expected Response:**

```json
[
  {
    "interface": "ether1",
    "name": "MyIPPool",
    "ranges": [
      "192.168.1.10-192.168.1.20"
    ],
    "size": 11
  }
]
```
## IP Pools

### Configuration Scenario and Requirements

This section covers configuring IP pools in RouterOS to assign IP addresses dynamically to clients on a network.

### Step-by-Step Implementation

**1. Create a Simple IP Pool**

- Open Winbox and connect to the router.
- Navigate to **IP > Pool.**
- Click on the **"+"** button to create a new pool.
- Enter a name for the pool (e.g., "my_ip_pool").
- Select the interface or bridge that will use this pool.
- Specify the IP address range of the pool (e.g., 192.168.1.10-192.168.1.100).
- Leave other settings as default for now.
- Click on **Apply** to save changes.

**2. Add IP Addresses to the Pool**

- Navigate to **IP > Addresses.**
- Click on the **"+"** button to create a new address.
- Select the IP pool created earlier.
- Enter an IP address from the pool range.
- Optionally, you can specify a MAC address to assign this IP address to a specific client.
- Click on **Apply** to save changes.

**3. Enable DHCP Server on the Interface**

- Navigate to **IP > DHCP Server.**
- Click on the **"+"** button to create a new DHCP server.
- Select the interface or bridge that uses the IP pool.
- Make sure the "Address Pool" field is set to the IP pool created earlier.
- Click on **Apply** to save changes.

### Complete Configuration Commands

```
/ip pool add name=my_ip_pool ranges=192.168.1.10-192.168.1.100 interface=ether1
/ip address add address=192.168.1.10 pool=my_ip_pool
/ip dhcp-server add interface=ether1 address-pool=my_ip_pool
```

### Common Pitfalls and Solutions

- **Ensure that the IP pool range does not overlap with existing static IP addresses on the network.**
- **Verify that the DHCP server is enabled on the correct interface or bridge.**
- **Check that the firewall is not blocking DHCP traffic (ports 67 and 68).**
- **If clients are not receiving IP addresses, try restarting the DHCP server service.**

### Verification and Testing Steps

- Open a command prompt or terminal on a client device.
- Run **ipconfig /all** (Windows) or **ifconfig** (macOS/Linux) to verify the IP address assigned to the client.
- Ensure that the IP address is within the range of the IP pool.
- Test internet connectivity to confirm that the IP address is correctly configured.

### Related Features and Considerations

- **DNS and Gateway Settings:** You can specify DNS servers and gateway IP addresses for the DHCP server to provide to clients.
- **Lease Time:** You can configure the lease time for IP addresses assigned by the DHCP server.
- **Reservations:** You can reserve specific IP addresses from the pool for specific clients by configuring MAC address reservations.

### MikroTik REST API Examples

**Get all IP Pools**

- **API Endpoint:** `/ip/pool/print`
- **Request Method:** GET
- **Example JSON Payload:** N/A
- **Expected Response:**
  - ```json
    [
      {
        ".id": ".id",
        "name": "pool1",
        "ranges": "192.168.1.0/24",
        "interface": "ether1"
      },
      {
        ".id": ".id",
        "name": "pool2",
        "ranges": "192.168.2.0/24",
        "interface": "ether2"
      }
    ]
    ```

**Add a New IP Pool**

- **API Endpoint:** `/ip/pool/add`
- **Request Method:** POST
- **Example JSON Payload:**
  - ```json
    {
      "name": "my_ip_pool",
      "ranges": "192.168.1.10-192.168.1.100",
      "interface": "ether1"
    }
    ```
- **Expected Response:**
  - ```json
    {
      ".id": ".id"
    }
    ```
**IP Pools**

**1. Configuration Scenario and Requirements**

Create an IP pool to assign dynamic IP addresses to clients on a network with the following requirements:

- Network address: 192.168.1.0/24
- Pool range: 192.168.1.10 to 192.168.1.100
- Lease time: 24 hours
- DNS server: 192.168.1.1
- Default gateway: 192.168.1.254

**2. Step-by-Step Implementation**

1. Access the RouterOS command prompt through WinBox or SSH.
2. Create the IP pool using the following command:

   ```
   /ip pool add name=my_pool ranges=192.168.1.10-192.168.1.100 lease-time=24h
   ```

3. Add the DNS server and default gateway to the pool:

   ```
   /ip pool set my_pool dns-servers=192.168.1.1 gateway=192.168.1.254
   ```

**3. Complete Configuration Commands**

```
/ip pool add name=my_pool ranges=192.168.1.10-192.168.1.100 lease-time=24h
/ip pool set my_pool dns-servers=192.168.1.1 gateway=192.168.1.254
```

**4. Common Pitfalls and Solutions**

* **Error:** Overlapping IP ranges.
   * **Solution:** Ensure that the pool range does not overlap with any other existing IP assignments.
* **Error:** Invalid lease time.
   * **Solution:** Use a valid lease time format, such as "24h" or "3d".
* **Error:** No internet access.
   * **Solution:** Verify that the DNS server and default gateway are configured correctly.

**5. Verification and Testing Steps**

* Assign an IP address from the pool to a client:

   ```
   /ip address add interface=ether1 pool=my_pool
   ```

* Verify the assigned IP address:

   ```
   /ip address print
   ```

* Check internet connectivity.

**6. Related Features and Considerations**

* Use static IP addresses for critical devices that require a fixed IP address.
* Consider using VLANs to segregate devices onto different subnets.
* Monitor IP pool usage to ensure efficient address allocation.

**7. MikroTik REST API Examples**

**Endpoint:** `/ip/pool`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "name": "my_pool",
  "ranges": ["192.168.1.10-192.168.1.100"],
  "lease-time": 86400,
  "dns-servers": ["192.168.1.1"],
  "gateway": "192.168.1.254"
}
```

**Expected Response:**

```json
{
  "id": "1",
  "name": "my_pool",
  "ranges": ["192.168.1.10-192.168.1.100"],
  "lease-time": 86400,
  "dns-servers": ["192.168.1.1"],
  "gateway": "192.168.1.254"
}
```
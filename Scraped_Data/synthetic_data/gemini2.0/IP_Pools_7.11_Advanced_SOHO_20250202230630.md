## IP Pools

**Configuration Scenario and Requirements:**

* Create a pool of IP addresses from a specified range
* Assign IP addresses from the pool to DHCP clients on a specific interface

**Step-by-Step Implementation:**

**1. Create the IP Pool:**

```
/ip pool
add name=my-ip-pool
ranges=192.168.10.1-192.168.10.100
```

**2. Assign the Pool to an Interface:**

```
/ip dhcp-server
set interface=ether1 address-pool=my-ip-pool
```

**Complete Configuration Commands:**

```
/ip pool add name=my-ip-pool ranges=192.168.10.1-192.168.10.100
/ip dhcp-server set interface=ether1 address-pool=my-ip-pool
```

**Common Pitfalls and Solutions:**

* **Failed to assign IP addresses from the pool:** Verify that the interface is configured with the correct IP address pool and that DHCP is enabled on the interface.
* **Conflict with existing IP addresses:** Ensure that the IP address range specified in the pool does not overlap with any existing addresses on the network.

**Verification and Testing Steps:**

* Check the IP address pool status with `/ip pool print`
* Connect a DHCP client to the interface and verify that it receives an IP address from the pool using `/ip dhcp-server lease print`

**Related Features and Considerations:**

* **IP Address Management:** Use IP pools to centrally manage and distribute IP addresses to clients.
* **DHCP Client:** Configure DHCP clients to obtain addresses from the specified pool.
* **DHCP Relay:** Forward DHCP requests between different network segments.
* **Firewall Rules:** Create firewall rules to allow traffic from and to the IP pool.

## MikroTik REST API Examples

**Create an IP Pool**

**Endpoint:** `/ip/pool/add`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "name": "my-ip-pool",
  "ranges": ["192.168.10.1-192.168.10.100"]
}
```

**Expected Response:**

```json
{
  "id": "<pool-id>"
}
```

**Assign IP Pool to Interface**

**Endpoint:** `/ip/dhcp-server/set`

**Request Method:** PUT

**Example JSON Payload:**

```json
{
  "interface": "ether1",
  "address-pool": "my-ip-pool"
}
```

**Expected Response:**

```json
{
  "interface": "ether1",
  "address-pool": "my-ip-pool"
}
```
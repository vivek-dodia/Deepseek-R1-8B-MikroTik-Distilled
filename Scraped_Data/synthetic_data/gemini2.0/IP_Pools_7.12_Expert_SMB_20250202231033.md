**Topic: IP Pools**

**1. Configuration Scenario and Requirements**

An IP Pool allocates IP addresses from a specified range to devices on the network. This is useful for managing a large number of devices that require dynamic IP addresses.

**2. Step-by-Step Implementation**

**a. Create an IP Pool**

```
/ip pool add name=pool1 ranges=10.0.0.1-10.0.0.254
```

**b. Assign an IP Pool to an Interface**

```
/interface ip address add address=10.0.0.1/24 interface=ether1 ip-pool=pool1
```

**3. Complete Configuration Commands**

**a. Create an IP Pool**

| Parameter | Explanation |
|---|---|
| name | Name of the IP pool |
| ranges | Range of IP addresses in the pool |

**b. Assign an IP Pool to an Interface**

| Parameter | Explanation |
|---|---|
| address | IP address of the interface |
| interface | Interface to assign the IP pool to |
| ip-pool | Name of the IP pool to use |

**4. Common Pitfalls and Solutions**

* **IP Address Conflict:** Ensure that the IP address range specified in the pool does not overlap with any existing IP addresses on the network.
* **No IP Address Assigned:** Check if the interface is configured to use the correct IP pool and that DHCP is enabled.
* **IP Pool Exhaustion:** Increase the IP address range in the pool to accommodate more devices.

**5. Verification and Testing Steps**

* Use the "/ip pool print" command to view the configured IP pools.
* Assign a device to the interface with the IP pool and verify that it receives an IP address from the pool.

**6. Related Features and Considerations**

* **DHCP Server:** An IP pool can be used with a DHCP server to automatically assign IP addresses to devices.
* **Static IP Addresses:** Devices can be assigned static IP addresses outside of the IP pool range.
* **IP Address Management:** IP pools make it easier to manage a large number of dynamic IP addresses by providing a centralized location for configuration.

**7. MikroTik REST API Examples**

**Endpoint:** `/ip/pool`

**Request Method:** GET

**Example JSON Payload:**

```json
{
  "ranges": "10.0.0.1-10.0.0.254",
  "name": "pool1"
}
```

**Expected Response:**

```json
{
  "status": "success",
  "data": [
    {
      ".id": "pool1",
      "ranges": "10.0.0.1-10.0.0.254",
      "name": "pool1"
    }
  ]
}
```

**8. Practical Examples and Explanations**

**a. DHCP Server with IP Pool**

Create an IP pool and use it with a DHCP server:

```
/ip pool add name=pool1 ranges=10.0.0.1-10.0.0.254
/ip dhcp-server add address-pool=pool1 interface=ether1
```

**b. Static IP Address Outside of IP Pool**

Assign a static IP address to a device outside of the IP pool:

```
/ip address add address=10.0.0.255/24 interface=ether2
```
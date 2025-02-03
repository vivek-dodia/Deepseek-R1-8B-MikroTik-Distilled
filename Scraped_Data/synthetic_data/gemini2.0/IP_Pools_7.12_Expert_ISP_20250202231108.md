**IP Pools**

**Configuration Scenario and Requirements**

* Create a pool of IP addresses to assign to clients on a specific interface.
* Configure a DHCP server to lease IP addresses from the pool.
* Set up a firewall rule to allow traffic from the pool.

**Step-by-Step Implementation**

1. **Create the IP Pool**
```
/ip pool
add name=my-pool ranges=192.168.1.10-192.168.1.20
[/code]
2. **Configure the DHCP Server**
```
/ip dhcp-server
set interface=ether1 address-pool=my-pool
```
3. **Set up the Firewall Rule**
```
/ip firewall filter
add action=accept chain=input dst-address-list=my-pool
```

**Complete Configuration Commands**

```
/ip pool
add name=my-pool ranges=192.168.1.10-192.168.1.20

/ip dhcp-server
set interface=ether1 address-pool=my-pool

/ip firewall filter
add action=accept chain=input dst-address-list=my-pool
[/code]

**Common Pitfalls and Solutions**

* **DHCP Server Not Started:** Ensure that the DHCP server is running by checking `/ip dhcp-server print`.
* **Firewall Rule Not Applied:** Check that the firewall rule is correctly applied by running `/ip firewall filter print`.
* **Address Conflict:** Ensure that the IP pool does not overlap with any other existing IP addresses.

**Verification and Testing Steps**

* Verify that clients can obtain IP addresses from the pool by connecting to the network.
* Use a packet sniffer to check that traffic from the pool is allowed by the firewall.

**Related Features and Considerations**

* **IP Binding:** Bind MAC addresses to specific IP addresses in the pool using `/ip dhcp-server lease`.
* **DHCP Options:** Configure DHCP options such as DNS servers and default gateway using `/ip dhcp-server option`.
* **DHCP Relay:** Forward DHCP requests to a remote DHCP server using `/ip dhcp-relay`.

**MikroTik REST API Examples**

**Endpoint:** `/ip/pool`

**Method:** GET

**Request Payload:** None

**Expected Response:**

```json
[
  {
    "name": "my-pool",
    "ranges": "192.168.1.10-192.168.1.20"
  }
]
```

**Endpoint:** `/ip/dhcp-server`

**Method:** POST

**Example JSON Payload (Add Address Pool):**

```json
{
  "interface": "ether1",
  "add-address-pool": "my-pool"
}
```

**Expected Response:**

```json
{
  "interface": "ether1",
  "address-pools": [
    "my-pool"
  ]
}
```
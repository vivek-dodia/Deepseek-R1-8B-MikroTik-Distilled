**IP Routing**

**1. Configuration Scenario and Requirements**

- Configure IP routing on a MikroTik RouterOS 7.12 (or higher) device in a small office/home office (SOHO) network.
- Define a default gateway and static routes to connect to the internet and other internal networks.

**2. Step-by-Step Implementation**

**2.1. Assign IP Addresses**

- Assign an IP address and netmask to the router's interface connected to the WAN.
  ```
  /ip address add address=192.168.1.1/24 interface=ether1
  ```

- Assign IP addresses and netmasks to the router's interfaces connected to the LAN.
  ```
  /ip address add address=192.168.2.1/24 interface=ether2
  ```

**2.2. Configure Default Gateway**

- Set the default gateway for the LAN interfaces to point to the router's WAN interface.
  ```
  /ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1
  ```

**2.3. Configure Static Routes**

- Add static routes for specific networks that are not directly connected to the router.
  ```
  /ip route add dst-address=10.0.0.0/16 gateway=192.168.3.1
  ```

**3. Complete Configuration Commands**

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=192.168.2.1/24 interface=ether2
/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1
/ip route add dst-address=10.0.0.0/16 gateway=192.168.3.1
```

**4. Common Pitfalls and Solutions**

- **Incorrect IP Addresses:** Verify that the assigned IP addresses and netmasks are correct and do not overlap with other networks.
- **Gateway Not Reachable:** Ensure that the default gateway is reachable from the LAN interfaces.
- **Static Route Not Working:** Check that the destination network and gateway are correct, and that the static route is not overridden by another route.

**5. Verification and Testing Steps**

- Test IP connectivity to the internet by pinging an external IP address.
- Verify connectivity to other internal networks using the static routes.
- Use the `/routing table print` command to check the routing table and ensure that the correct routes are present.

**6. Related Features and Considerations**

- Advanced routing features such as OSPF or BGP can be used for more complex network topologies.
- IP forwarding should be enabled for IP routing to work.
- Security measures such as firewalls and access control lists should be implemented to protect the network.

**7. MikroTik REST API Examples**

**7.1. Add IP Address**

**API Endpoint:**
```
/ip/address/add
```

**Request Method:**
```
POST
```

**Example JSON Payload:**
```
{
  "address": "192.168.1.1/24",
  "interface": "ether1"
}
```

**Expected Response:**
```
{
  "id": "1"
}
```

**7.2. Add Default Gateway**

**API Endpoint:**
```
/ip/route/add
```

**Request Method:**
```
POST
```

**Example JSON Payload:**
```
{
  "dst-address": "0.0.0.0/0",
  "gateway": "192.168.1.1"
}
```

**Expected Response:**
```
{
  "id": "1"
}
```

**7.3. Add Static Route**

**API Endpoint:**
```
/ip/route/add
```

**Request Method:**
```
POST
```

**Example JSON Payload:**
```
{
  "dst-address": "10.0.0.0/16",
  "gateway": "192.168.3.1"
}
```

**Expected Response:**
```
{
  "id": "1"
}
```
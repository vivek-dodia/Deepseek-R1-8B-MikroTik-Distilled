**IP Addressing (IPv4 and IPv6)**

**1. Configuration Scenario and Requirements**

* Assign IP addresses to MikroTik router interfaces
* Enable both IPv4 and IPv6 addressing on the router

**2. Step-by-Step Implementation**

**IPv4 Configuration:**

1. Navigate to IP > Addresses
2. Click the '+' button to add a new address
3. Select the desired interface from the Interface drop-down list
4. Enter the IP address and subnet mask in the Address field (e.g., 192.168.1.1/24)
5. Click Apply

**IPv6 Configuration:**

1. Navigate to IP > Addresses
2. Click the '+' button
3. Select the desired interface from the Interface drop-down list
4. Enable IPv6 by ticking the checkbox next to "Enable IPv6"
5. Select the desired addressing mode from the DHCPv6 Client drop-down list (e.g., DHCPv6 Stateless)
6. Click Apply

**3. Complete Configuration Commands**

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address set interface=ether1 address=192.168.1.1/24
/ip address add interface=ether1 address=2001:db8::1/64
/ip address set interface=ether1 address=2001:db8::1/64 disable-dad=yes
```

**4. Common Pitfalls and Solutions**

* Ensure you enter valid IP addresses and subnet masks.
* Avoid assigning the same IP address to multiple interfaces.
* If IPv6 is enabled but not working, check if the interface supports IPv6.
* Make sure the IPv6 addressing mode is correctly set.

**5. Verification and Testing Steps**

* Use the `/ip address print` command to verify the assigned IP addresses.
* Ping other devices on the network to test connectivity.

**6. Related Features and Considerations**

* DHCP Server: Can be used to assign IP addresses to clients automatically.
* IP Pools: Allow for the management of IP address ranges.
* Static DHCP Leases: Can be used to reserve IP addresses for specific devices.

**7. MikroTik REST API Examples**

**Create an IPv4 Address:**

```
curl -X POST -H "Content-Type: application/json" -d '{
  "address": "192.168.1.1/24",
  "interface": "ether1"
}' http://192.168.1.1/rest/ip/address
```

**Create an IPv6 Address:**

```
curl -X POST -H "Content-Type: application/json" -d '{
  "address": "2001:db8::1/64",
  "interface": "ether1",
  "disable-dad": true
}' http://192.168.1.1/rest/ip/address
```
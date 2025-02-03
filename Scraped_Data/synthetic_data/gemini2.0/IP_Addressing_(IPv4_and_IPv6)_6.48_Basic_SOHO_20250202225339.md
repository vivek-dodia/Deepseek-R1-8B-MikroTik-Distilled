**IP Addressing (IPv4 and IPv6)**

**Configuration scenario and requirements**
- Configure IP addresses for IPv4 and IPv6 network.

**Step-by-step implementation**
- **IPv4 Address:**
1. Go to **IP** > **Addresses**
2. Click on the **+** button to create a new IP address
3. Select the interface from the **Interface** dropdown
4. Enter the IP address in the **Address** field
5. Enter the subnet mask in the **Network** field
6. Optional: Set the gateway address in the **Gateway** field
7. Click **Apply** to save the configuration

- **IPv6 Address:**
1. Go to **IP** > **Addresses**
2. Click on the **+** button to create a new IP address
3. Select the interface from the **Interface** dropdown
4. Select **IPv6 Address** from the **Address Family** dropdown
5. Enter the IPv6 address in the **Address** field
6. Optional: Set the gateway address in the **Gateway** field
7. Click **Apply** to save the configuration

**Complete configuration commands**
**IPv4:**
```
/ip address
add interface=<interface-name> address=<ipv4-address> network=<subnet-mask> gateway=<gateway-address>
```
**Example:**
```
/ip address add interface=ether1 address=192.168.1.10/24 gateway=192.168.1.1
```

**IPv6:**
```
/ip address
add interface=<interface-name> address=<ipv6-address> gateway=<gateway-address>
```
**Example:**
```
/ip address add interface=ether1 address=2001:db8::1 gateway=2001:db8::1
```

**Common pitfalls and solutions**
- **Incorrect IP address or subnet mask:** Verify the IP address and subnet mask are correct and match the network requirements.
- **Gateway not reachable:** Ensure the gateway address is valid and reachable from the device.
- **Interface not configured:** Check if the interface is physically connected and enabled in the RouterOS configuration.

**Verification and testing steps**
- Use the **ping** command to verify connectivity to other devices on the network.
- Use the **ip address** command to display configured IP addresses.

**Related features and considerations**
- **IP Pools** for dynamic IP address assignment
- **IP Routing** for configuring routing rules
- **IP Settings** for advanced IP configuration options
- **MAC server** for MAC address management
- **RoMON** for remote monitoring and management

**MikroTik REST API examples**

**Add IPv4 Address**

**Endpoint:** `/ip/address`
**Request method:** POST
**Example JSON payload:**
```
{
  "interface": "ether1",
  "address": "192.168.1.10/24",
  "gateway": "192.168.1.1"
}
```

**Expected response:**
```
{
  "id": "1",
  "interface": "ether1",
  "address": "192.168.1.10/24",
  "gateway": "192.168.1.1"
}
```

**Add IPv6 Address**

**Endpoint:** `/ip/address`
**Request method:** POST
**Example JSON payload:**
```
{
  "interface": "ether1",
  "address_family": "ipv6",
  "address": "2001:db8::1",
  "gateway": "2001:db8::1"
}
```

**Expected response:**
```
{
  "id": "1",
  "interface": "ether1",
  "address_family": "ipv6",
  "address": "2001:db8::1",
  "gateway": "2001:db8::1"
}
```
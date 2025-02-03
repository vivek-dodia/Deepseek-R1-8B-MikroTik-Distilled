**IP Addressing (IPv4 and IPv6)**

**Configuration Scenario and Requirements**

Configure IPv4 and IPv6 addressing on MikroTik RouterOS 6.48 for a small office/home office (SOHO) network with the following requirements:

- Assign IPv4 address 192.168.1.1/24 to the router's LAN interface
- Assign IPv6 address 2001:db8::1/64 to the router's LAN interface
- Configure static IP addressing for connected devices
- Enable DHCP server on the LAN interface to assign dynamic IP addresses

**Step-by-Step Implementation**

**IPv4 Configuration**

1. Go to **IP > Addresses** in WinBox.
2. Click the **+** button to add a new address.
3. Select the LAN interface from the **Interface** dropdown.
4. Enter the IPv4 address (192.168.1.1) in the **Address** field.
5. Enter the subnet mask (/24) in the **Network** field.
6. Click **Apply** to save the changes.

**IPv6 Configuration**

1. Go to **IP > Addresses** in WinBox.
2. Click the **+** button to add a new address.
3. Select the LAN interface from the **Interface** dropdown.
4. Select **IPv6** from the **Protocol** dropdown.
5. Enter the IPv6 address (2001:db8::1) in the **Address** field.
6. Enter the subnet prefix length (/64) in the **Prefix** field.
7. Click **Apply** to save the changes.

**Static IP Address Assignment**

1. Go to **IP > DHCP Server** in WinBox.
2. Select the LAN interface from the **Interface** dropdown.
3. Click the **Leases** tab.
4. Click the **Add** button to create a new lease.
5. Enter the MAC address of the device you want to assign a static IP address to.
6. Enter the desired IPv4 address in the **Fixed IP Address** field.
7. Click **Apply** to save the changes.

**DHCP Server Configuration**

1. Go to **IP > DHCP Server** in WinBox.
2. Select the LAN interface from the **Interface** dropdown.
3. Click the **Settings** tab.
4. Enter the starting IP address of the DHCP pool in the **Address Pool Start** field.
5. Enter the ending IP address of the DHCP pool in the **Address Pool End** field.
6. Enter the subnet mask in the **Subnet Mask** field.
7. Click **Apply** to save the changes.

**Complete Configuration Commands**

```
/ip address add address=192.168.1.1/24 interface=LAN
/ip address add address=2001:db8::1/64 interface=LAN
/ip dhcp-server lease add mac-address=00:11:22:33:44:55 address=192.168.1.10
/ip dhcp-server set interface=LAN address-pool.ranges=192.168.1.10-192.168.1.100
```

**Common Pitfalls and Solutions**

- **IPv6 Connectivity Issues:** Ensure that IPv6 is enabled on the devices that need to communicate via IPv6.
- **Static IP Conflict:** Avoid assigning the same static IP address to multiple devices.
- **DHCP Server Not Working:** Ensure that the DHCP server is enabled on the correct interface and that the address pool is large enough to accommodate all connected devices.

**Verification and Testing Steps**

- Ping IPv4 and IPv6 addresses to verify connectivity.
- Use the **arp** command to check the MAC address table for statically assigned IP addresses.
- Use the **ip lease** command to view the list of DHCP lease assignments.

**Related Features and Considerations**

- **DHCP Relay:** Forwarded DHCP requests from a client on one network to a DHCP server on another network.
- **DNS Settings:** Configure DNS settings to resolve hostnames to IP addresses.
- **Routing:** Configure routing protocols to establish connectivity between different networks.

**REST API Examples**

**Get IPv4 Address Information**

```
GET /api/v1/ip/address/print
```

**Add IPv4 Address**

```
POST /api/v1/ip/address/add
{
  "address": "192.168.1.1/24",
  "interface": "LAN"
}
```

**Remove IPv4 Address**

```
DELETE /api/v1/ip/address/remove
{
  ".id": "1"
}
```
**IP Addressing (IPv4 and IPv6)**

**IPv4 Addressing**

**Configuration scenario and requirements**

- Assign IPv4 addresses to network interfaces
- Configure default gateways
- Enable DHCP server on specific interfaces

**Step-by-step implementation**

1. Connect to the RouterOS device using WinBox or another management tool.
2. Navigate to **IP > Addresses** tab.
3. Click **+** button to add a new IP address.
4. Select the desired interface from the **Interface** drop-down.
5. Enter the desired IPv4 address in the **Address** field.
6. Enter the netmask in the **Network** field.
7. Enter the default gateway IP address in the **Gateway** field (optional).
8. Enable DHCP server on an interface: Navigate to **IP > DHCP Server** and click **+** to create a new DHCP server. Select the desired interface, enter the IP pool range, and configure other necessary settings.

**Complete configuration commands**

```text
/ip address add address=192.168.1.10/24 interface=ether1
/ip address add address=2001:db8::1/64 interface=ether1
/ip dhcp-server add interface=ether1
```

**Common pitfalls and solutions**

- Incorrect IP address or subnet mask: Verify that the IP address and subnet mask are correct and match the network configuration.
- Duplicate IP addresses: Ensure that no two devices on the same network have the same IP address.
- Incorrect default gateway: Ensure that the default gateway is set correctly and is reachable from the device.

**Verification and testing steps**

- Use the **ping** command to test connectivity to other devices on the network.
- Use the **ip addr** command to verify the assigned IP addresses and default gateway.

**IPv6 Addressing**

**Configuration scenario and requirements**

- Assign IPv6 addresses to network interfaces
- Configure default gateways
- Enable neighbor discovery
- Enable IPv6 forwarding

**Step-by-step implementation**

1. Navigate to **IP > Addresses** tab.
2. Click **+** button to add a new IPv6 address.
3. Select the desired interface from the **Interface** drop-down.
4. Enter the desired IPv6 address in the **Address** field.
5. Enter the netmask in the **Prefix** field.
6. Enable neighbor discovery: Navigate to **IPv6 > ND** and enable **Accept Neighbor Discoveries**.
7. Enable IPv6 forwarding: Navigate to **IP > Settings** and enable **IPv6 Forwarding**.

**Complete configuration commands**

```text
/ip address add address=2001:db8::1/64 interface=ether1
/ipv6 nd set accept-nd=yes
/ip settings set ipv6-forwarding=yes
```

**Common pitfalls and solutions**

- Incorrect IPv6 address or prefix: Verify that the IPv6 address and prefix are correct and match the network configuration.
- Incomplete Neighbor Discovery configuration: Ensure that Neighbor Discovery is enabled and configured correctly.
- IPv6 forwarding is disabled: Ensure that IPv6 forwarding is enabled in the **IP > Settings** tab.

**Verification and testing steps**

- Use the **ping6** command to test connectivity to other IPv6 devices on the network.
- Use the **ip -6 addr** command to verify the assigned IPv6 addresses.

**IP Pools**

**Configuration scenario and requirements**

- Create a pool of IP addresses for dynamic assignment
- Configure DHCP server to use the pool
- Set lease time and other DHCP settings

**Step-by-step implementation**

1. Navigate to **IP > Pool** tab.
2. Click **+** button to add a new IP pool.
3. Enter the desired pool name in the **Name** field.
4. Enter the starting and ending IP addresses in the **Range** field.
5. Configure the lease time and other DHCP settings in the **Ranges** tab.
6. Navigate to **IP > DHCP Server** and select the desired server.
7. Assign the created IP pool to the **Address Pool** field.

**Complete configuration commands**

```text
/ip pool add range=192.168.1.10-192.168.1.200 name=dhcp-pool-1
/ip dhcp-server set address-pool=dhcp-pool-1
```

**Common pitfalls and solutions**

- Overlapping IP pools: Ensure that the IP pools do not overlap with other statically assigned IP addresses.
- Insufficient lease time: Configure an appropriate lease time to avoid frequent DHCP renewals.

**Verification and testing steps**

- Use the **ip dhcp-server lease** command to view assigned DHCP leases.
- Use the **ping** command to test connectivity of devices that have obtained IP addresses from the DHCP server.

**IP Routing**

**Configuration scenario and requirements**

- Configure static routes to specific destinations
- Set up dynamic routing protocols (e.g., OSPF, BGP)

**Step-by-step implementation**

**Static Routing:**

1. Navigate to **IP > Routes** tab.
2. Click **+** button to add a new static route.
3. Enter the destination network in the **Dst. Address** field.
4. Enter the IP address of the next hop router in the **Gateway** field.

**Dynamic Routing (OSPF):**

1. Navigate to **Routing > OSPF** tab.
2. Enable OSPF on the desired interfaces.
3. Configure the area ID, router ID, and other OSPF settings.

**Complete configuration commands**

**Static Routing:**

```text
/ip route add dst-address=172.16.0.0/24 gateway=192.168.1.1
```

**OSPF Routing:**

```text
/routing ospf interface add interface=ether1 cost=10
/routing ospf set router-id=1.1.1.1 area=0
```

**Common pitfalls and solutions**

- Incorrect route configuration: Verify that the destination network and next hop gateway are correct.
- Configuration conflicts: Ensure that there are no conflicting routes for the same destination.
- OSPF configuration errors: Ensure that the area ID, router ID, and interface costs are configured correctly.

**Verification and testing steps**

- Use the **ip route print** command to view the routing table.
- Use the **ping** command to test connectivity to destinations that are reachable through the configured routes.
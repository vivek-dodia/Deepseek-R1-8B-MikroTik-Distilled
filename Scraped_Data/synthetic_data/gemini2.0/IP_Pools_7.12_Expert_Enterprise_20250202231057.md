**IP Pools in MikroTik RouterOS 7.12**

**1. Configuration Scenario and Requirements**

* Enterprise network with multiple subnets and a requirement to assign IP addresses dynamically to devices.
* Use RouterOS 7.12 to create and manage IP pools.

**2. Step-by-Step Implementation**

**2.1 Create an IP Pool**

```
/ip pool add name=pool1 ranges=192.168.1.100-192.168.1.199
```

**2.2 Add an IP Address to a Pool**

```
/ip pool add-address pool=pool1 address=192.168.1.110
```

**2.3 Remove an IP Address from a Pool**

```
/ip pool remove-address pool=pool1 address=192.168.1.110
```

**2.4 Assign a DHCP Server to a Pool**

```
/ip dhcp-server add interface=ether1 pool=pool1 lease-time=3600 address-pool=pool1
```

**3. Complete Configuration Commands**

* **/ip pool add**: Creates a new IP pool.
* **/ip pool add-address**: Adds an IP address to a pool.
* **/ip pool remove-address**: Removes an IP address from a pool.
* **/ip dhcp-server add**: Creates a DHCP server that assigns IP addresses within the specified pool.

**4. Common Pitfalls and Solutions**

* **DHCP server not assigning IP addresses**: Ensure that the DHCP server is enabled for the correct interface and that the pool is assigned to the server.
* **IP address conflicts**: Avoid adding duplicate IP addresses to the pool.
* **IP address exhaustion**: Monitor the IP pool utilization and add more addresses as needed.

**5. Verification and Testing Steps**

* Connect a client device to the subnet.
* Run a DHCP lease acquisition command on the client.
* Verify that the client obtains an IP address from the specified pool.

**6. Related Features and Considerations**

* IP pools can be used with different types of IP addresses (IPv4, IPv6).
* DHCP servers can be configured with additional parameters such as DNS servers, gateway, and lease time.
* MAC server can be used to assign static IP addresses based on MAC addresses.

**7. MikroTik REST API Examples**

* **Get IP pools**:

```
GET /api/ip/pool
```

* **Create an IP pool**:

```
POST /api/ip/pool
{
  "name": "pool1",
  "ranges": ["192.168.1.100-192.168.1.199"]
}
```

**8. Additional Topics**

**IP Addressing**

* **/ip address add**: Assigns an IP address to an interface.
* **/ip address remove**: Removes an IP address from an interface.

**IP Routing**

* **/ip route add**: Adds a static route.
* **/ip route print**: Displays the routing table.

**IP Settings**

* **/ip settings**: Configures global IP settings, such as MTU and DNS servers.

**MAC Server**

* **/mac-server add**: Adds a MAC address-to-IP address mapping.
* **/mac-server remove**: Removes a MAC address mapping.

**RoMON**

* **/romon**: Starts or stops the RoMON monitor.
* **/romon status**: Displays the RoMON status.

**WinBox**

* **/winbox add**: Creates a WinBox user.
* **/winbox remove**: Removes a WinBox user.

**Certificates**

* **/certificate add**: Imports a certificate.
* **/certificate print**: Displays the certificate information.

**PPP AAA**

* **/ppp aaa**: Configures PPP AAA settings.
* **/ppp aaa get-secret**: Displays the PPP AAA secret.

**RADIUS**

* **/radius add**: Adds a RADIUS server.
* **/radius print**: Displays the RADIUS server information.

**User / User Groups**

* **/user add**: Creates a user.
* **/user group add**: Creates a user group.

**Bridging and Switching**

* **/bridge add**: Creates a bridge.
* **/switch add**: Creates a switch interface.

**MACVLAN**

* **/macvlan add**: Creates a MACVLAN interface.
* **/macvlan print**: Displays the MACVLAN interface information.

**L3 Hardware Offloading**

* **/interface bridge set bridge=bridge1 offload=l3**: Enables L3 hardware offloading on a bridge interface.
* **/interface bridge print**: Displays the bridge interface configuration.

**MACsec**

* **/interface macsec add**: Adds a MACsec interface.
* **/interface macsec print**: Displays the MACsec interface information.

**Quality of Service**

* **/queue add**: Adds a queue.
* **/queue print**: Displays the queue information.

**Switch Chip Features**

* **/switch chip enable**: Enables switch chip features.
* **/switch chip monitor**: Monitors the switch chip status.

**VLAN**

* **/vlan add**: Creates a VLAN.
* **/vlan print**: Displays the VLAN information.

**VXLAN**

* **/vxlan interface add**: Creates a VXLAN interface.
* **/vxlan interface print**: Displays the VXLAN interface information.

**Firewall and Quality of Service**

* **/ip firewall add**: Adds a firewall rule.
* **/ip firewall filter**: Displays the firewall rule list.

**IP Services**

* **/dhcp server add**: Creates a DHCP server.
* **/dhcp server print**: Displays the DHCP server configuration.

**High Availability Solutions**

* **/load-balancing add**: Creates a load balancing rule.
* **/load-balancing print**: Displays the load balancing rule list.

**Mobile Networking**

* **/lte add**: Creates an LTE interface.
* **/lte print**: Displays the LTE interface information.

**Multi Protocol Label Switching - MPLS**

* **/mpls add**: Creates an MPLS interface.
* **/mpls print**: Displays the MPLS interface information.

**Network Management**

* **/arp add**: Adds an ARP entry.
* **/arp print**: Displays the ARP table.

**Routing**

* **/routing add**: Adds a routing protocol.
* **/routing print**: Displays the routing protocol configuration.

**System Information and Utilities**

* **/system clock set value=yyyy-mm-dd**: Sets the system clock.
* **/system identity print**: Displays the system identity information.

**Virtual Private Networks**

* **/ipsec tunnel add**: Creates an IPsec tunnel.
* **/ipsec tunnel print**: Displays the IPsec tunnel configuration.

**Wired Connections**

* **/interface ethernet add**: Creates an Ethernet interface.
* **/interface ethernet print**: Displays the Ethernet interface information.

**Wireless**

* **/interface wireless add**: Creates a wireless interface.
* **/interface wireless print**: Displays the wireless interface configuration.

**Internet of Things**

* **/bluetooth add**: Creates a Bluetooth interface.
* **/mqtt broker add**: Creates an MQTT broker.

**Hardware**

* **/system health print**: Displays the system health information.
* **/system leds add**: Creates a new LED.

**Diagnostics, Monitoring, and Troubleshooting**

* **/ping add**: Sends an ICMP ping request.
* **/traceroute add**: Performs a traceroute.

**Extended Features**

* **/container add**: Creates a container.
* **/dlna media-server add**: Creates a DLNA media server.
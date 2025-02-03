**Topic: IP Settings**

**Configuration Level:** Basic

**Network Scale:** SOHO

## IP Addressing (IPv4 and IPv6)

**Configuration Scenario and Requirements:**

* Assign an IPv4 address to an Ethernet interface for device management.
* Assign an IPv6 address to the same interface for future IPv6 support.

**Step-by-Step Implementation:**

1. **Connect to the device and open the terminal.**
2. **Enter the following commands:**
   - `/ip address add address=192.168.1.1/24 interface=ether1`
   - `/ip address add address=2001:db8::1/64 interface=ether1`
3. **Verify the changes:**
   - `/ip address print`

## IP Pools

**Configuration Scenario and Requirements:**

* Create an IP pool to assign dynamic IP addresses to DHCP clients.

**Step-by-Step Implementation:**

1. **Create a new IP pool:**
   - `/ip pool add name=dhcp-pool ranges=192.168.1.10-192.168.1.254`
2. **Assign the pool to an interface:**
   - `/ip dhcp-server add interface=ether1 address-pool=dhcp-pool`
3. **Verify the changes:**
   - `/ip pool print`
   - `/ip dhcp-server print`

## IP Routing

**Configuration Scenario and Requirements:**

* Enable IP forwarding on the device to allow traffic to flow between subnets.

**Step-by-Step Implementation:**

1. **Enable IP forwarding:**
   - `/ip route add dst-address=0.0.0.0/0 gateway=192.168.1.2`
2. **Verify the changes:**
   - `/ip route print`

## MAC Server

**Configuration Scenario and Requirements:**

* Create a MAC server to manage and track MAC addresses of connected devices.

**Step-by-Step Implementation:**

1. **Create a new MAC server:**
   - `/ip mac-server add name=mac-server`
2. **Add a MAC address to the server:**
   - `/ip mac-server add mac-address=00:11:22:33:44:55 server=mac-server`
3. **Verify the changes:**
   - `/ip mac-server print`

#### Common Pitfalls and Solutions

* **Invalid IP address:** Ensure the IP address and subnet mask are correct.
* **IP address conflict:** Check if the IP address is already assigned to another device on the network.
* **DHCP server not responding:** Verify the DHCP server is running and the correct IP pool is assigned to the interface.
* **MAC address not found:** Ensure the MAC address is added to the MAC server.

#### Verification and Testing Steps

* Use the `ping` command to test connectivity between devices.
* Check the DHCP lease list to verify clients are obtaining IP addresses from the DHCP server.
* Use the `ip route` command to verify traffic is routing correctly.
* Use the `mac-server` command to check MAC address information.

#### Related Features and Considerations

* **IPv6:** MikroTik RouterOS supports IPv6 addressing. Refer to the IPv6 documentation for detailed configuration.
* **NAT:** NAT can be used to translate private IP addresses to public IP addresses. See the NAT documentation for more information.
* **Firewall:** The firewall can be used to control traffic flow and protect the network. See the firewall documentation for details.
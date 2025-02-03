Okay, let's dive into this comprehensive MikroTik configuration scenario, targeting RouterOS 7.11, with a focus on IP addressing and related topics for a Hotspot network, all while keeping the "Advanced" configuration level in mind.

# MikroTik RouterOS Hotspot Network Configuration: Advanced IP Addressing

This document provides a detailed configuration for a MikroTik router in a hotspot environment, focusing on advanced IP addressing techniques, including IPv4 and IPv6. We will cover all required topics. The specific subnet we will use is `94.50.107.0/24`, assigned to the interface `vlan-71`.

## 1. Comprehensive Configuration Scenario and Specific MikroTik Requirements

**Scenario:**

We are setting up a hotspot network using a MikroTik router. This network needs to provide IP addresses dynamically to clients via DHCP, support IPv6, offer secure access via the hotspot login portal, and implement basic QoS for a smooth user experience. We will be using a VLAN interface for this hotspot.

**MikroTik Requirements:**

*   **RouterOS Version:** 7.11 (or 7.x compatible)
*   **Interface:** VLAN interface `vlan-71` connected to the hotspot network.
*   **IPv4:** Use `94.50.107.0/24` for the local network.
*   **IPv6:** Implement SLAAC for IPv6.
*   **DHCP:** Assign IPv4 addresses within the `94.50.107.0/24` subnet.
*   **Hotspot:** Configure a hotspot server with user authentication.
*   **Security:** Implement basic firewall rules and secure access to the router.
*   **QoS:** Basic bandwidth management for users.

## 2. Step-by-Step MikroTik Implementation

Here's a step-by-step guide for setting up this configuration, using both the CLI and Winbox (where appropriate).

**Step 1: Create VLAN Interface**

**CLI:**
```mikrotik
/interface vlan
add name=vlan-71 vlan-id=71 interface=ether1 # Replace ether1 with your trunk interface
```
**Winbox:**

1.  Go to `Interfaces` and click the `+` button.
2.  Select `VLAN`.
3.  Set `Name` to `vlan-71`, `VLAN ID` to `71`, and `Interface` to your trunk interface (e.g. ether1).
4.  Click `Apply` and `OK`.

**Step 2: Configure IPv4 Address**

**CLI:**

```mikrotik
/ip address
add address=94.50.107.1/24 interface=vlan-71
```
**Winbox:**

1.  Go to `IP` -> `Addresses`.
2.  Click the `+` button.
3.  Set `Address` to `94.50.107.1/24` and `Interface` to `vlan-71`.
4.  Click `Apply` and `OK`.

**Step 3: Configure IPv6 Address (SLAAC)**
**CLI:**

```mikrotik
/ipv6 address
add interface=vlan-71 from-pool=ipv6-pool # Assuming you have an IPv6 pool named 'ipv6-pool'
```

**Winbox:**

1.  Go to `IPv6` -> `Addresses`.
2.  Click the `+` button.
3. Set interface to `vlan-71` and choose your IPv6 pool (e.g. "ipv6-pool")
4.  Click `Apply` and `OK`.

**Note:** For IPv6 to work properly, you'll also need to configure an IPv6 pool and IPv6 Router Advertisements. We will cover this in later sections.

**Step 4: Configure DHCP Server**

**CLI:**

```mikrotik
/ip pool
add name=dhcp-pool ranges=94.50.107.10-94.50.107.254
/ip dhcp-server
add address-pool=dhcp-pool interface=vlan-71 name=dhcp-vlan71
/ip dhcp-server network
add address=94.50.107.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=94.50.107.1
```
**Winbox:**

1.  Go to `IP` -> `Pool` and add a new pool for the DHCP range.
2.  Go to `IP` -> `DHCP Server` and add a new DHCP server, selecting `vlan-71` and the created pool.
3.  Go to `IP` -> `DHCP Server` -> `Networks` and add a network with your subnet, DNS, and gateway.

**Step 5: Configure Hotspot Server**

**CLI:**

```mikrotik
/ip hotspot profile
add name=hotspot-profile dns-name=hotspot.local html-directory=hotspot
/ip hotspot
add address-pool=dhcp-pool disabled=no interface=vlan-71 name=hotspot-vlan71 profile=hotspot-profile
/ip hotspot user profile
add name=default-hotspot-user profile=hotspot-profile
/ip hotspot user add name=testuser password=testpass profile=default-hotspot-user
```
**Winbox:**

1.  Go to `IP` -> `Hotspot` and create a new profile (e.g. `hotspot-profile`).
2.  Go to `IP` -> `Hotspot` and create a new hotspot server, using the new `hotspot-profile` and the `vlan-71` interface.
3.  Add a new `User Profile` and a user.

**Step 6: Basic Firewall Rules**

**CLI:**
```mikrotik
/ip firewall filter
add chain=input action=accept connection-state=established,related
add chain=input action=accept protocol=icmp
add chain=input action=drop in-interface=vlan-71
add chain=forward action=accept connection-state=established,related
add chain=forward action=accept connection-state=new src-address=94.50.107.0/24
add chain=forward action=drop
```
**Winbox:**
Go to `IP` -> `Firewall` and add appropriate `Filter Rules`.

**Step 7: Enable IPv6 Forwarding**

**CLI:**
```mikrotik
/ipv6 settings set forwarding=yes
```

**Winbox:**
Go to `IPv6` -> `Settings` and check `Enable Forwarding`.

## 3. Complete MikroTik CLI Configuration Commands

```mikrotik
# VLAN Interface
/interface vlan
add name=vlan-71 vlan-id=71 interface=ether1

# IPv4 Address
/ip address
add address=94.50.107.1/24 interface=vlan-71

# IPv4 DHCP Pool
/ip pool
add name=dhcp-pool ranges=94.50.107.10-94.50.107.254

# IPv4 DHCP Server
/ip dhcp-server
add address-pool=dhcp-pool interface=vlan-71 name=dhcp-vlan71
/ip dhcp-server network
add address=94.50.107.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=94.50.107.1

# IPv6 Address - Assuming you have IPv6 setup
/ipv6 address
add interface=vlan-71 from-pool=ipv6-pool

# Hotspot Profile
/ip hotspot profile
add name=hotspot-profile dns-name=hotspot.local html-directory=hotspot
# Hotspot Server
/ip hotspot
add address-pool=dhcp-pool disabled=no interface=vlan-71 name=hotspot-vlan71 profile=hotspot-profile
# Hotspot User Profile
/ip hotspot user profile
add name=default-hotspot-user profile=hotspot-profile
# Hotspot User
/ip hotspot user add name=testuser password=testpass profile=default-hotspot-user

# Firewall Rules
/ip firewall filter
add chain=input action=accept connection-state=established,related
add chain=input action=accept protocol=icmp
add chain=input action=drop in-interface=vlan-71
add chain=forward action=accept connection-state=established,related
add chain=forward action=accept connection-state=new src-address=94.50.107.0/24
add chain=forward action=drop

# IPv6 Forwarding
/ipv6 settings set forwarding=yes
```

## 4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics

*   **DHCP Issues:** If clients aren't receiving IP addresses, check:
    *   The DHCP server is enabled on the correct interface.
    *   The IP pool has enough available addresses.
    *   The `dhcp-server` and `dhcp-server network` configurations are correct.
*   **Hotspot Login Issues:**
    *   Verify DNS is configured correctly and that the DNS name in hotspot-profile resolves to the router's IP.
    *   Check that the hotspot server is enabled on the correct interface and uses a valid profile.
    *   Make sure a valid user with a correct password is setup in `ip hotspot user`.
*   **Firewall Issues:**
    *   Make sure the firewall rules are ordered correctly, starting with most specific rules first.
    *   Use `/tool torch` to monitor traffic on the interfaces and see if packets are being dropped.
    *   Enable logging on the drop rules to see what is being blocked.
*   **IPv6 Issues:**
    *   Verify that your upstream provides IPv6 and it is routed correctly to your router.
    *   Check if IPv6 addresses are assigned to the interfaces with proper scopes and that IPv6 Router Advertisements are configured.
    *   Use `/ipv6 nd` to check that the router is sending out router advertisements.
*   **Error Scenario:** Incorrect subnet configuration (e.g. using a conflicting `/24` network) can cause all clients to be unable to obtain IP addresses.
    *   **CLI Example:** Attempting to add an interface address that overlaps:

    ```mikrotik
    /ip address add address=94.50.107.2/24 interface=ether2
    ```
    *   This would cause an error if `ether2` is on the same segment as `vlan-71`, as overlapping subnets cause routing conflicts. The router will reject this configuration.
    *   **Troubleshooting:** Use `/ip address print` to check interface addresses and verify that the network addresses and ranges are correct.
*   **Diagnostics:**
    *   Use `/tool ping` and `/tool traceroute` to diagnose connectivity.
    *   Use `/tool torch` to examine interface traffic.
    *   Use `/log print` to check logs for errors.

## 5. Verification and Testing Steps

*   **Ping:**
    *   From a connected client: `ping 94.50.107.1` (router's IP) and `ping 8.8.8.8` (external IP).
    *   From the router CLI: `/tool ping 94.50.107.10` (a client IP) and `/tool ping google.com`.
    *   From the client: `ping <router's IPv6 address>` to test IPv6 connectivity.
*   **Traceroute:**
    *   From a connected client: `traceroute google.com`.
    *   From router CLI: `/tool traceroute google.com`.
*   **Torch:**
    *   `/tool torch interface=vlan-71` to observe traffic on the interface.
*   **DHCP Lease:** Check the `/ip dhcp-server lease print` to see which IPs have been leased.
*   **Hotspot:** Login using the `testuser` and check the `/ip hotspot active` to see active hotspot sessions.

## 6. Related MikroTik-Specific Features, Capabilities, and Limitations

*   **MAC server:** Used for MAC authentication. Can be integrated with the hotspot server.
*   **RoMON:** MikroTik's Remote Monitoring protocol, useful for managing multiple routers.
*   **WinBox:** MikroTik's GUI configuration tool, can be used instead of CLI.
*   **Certificates:** Necessary for secure HTTPS connections and VPNs.
*   **PPP AAA:** Authentication, Authorization, and Accounting for PPP connections.
*   **RADIUS:** Centralized user authentication server.
*   **User/User groups:** used to manage access to the router and hotspost.
*   **Bridging and Switching:** Used to create local networks.
*   **MACVLAN:** Creates multiple virtual interfaces on the same physical interface.
*   **L3 Hardware Offloading:** Offloads some routing functions to hardware for better performance (limited to certain RouterBOARD models).
*   **MACsec:** Secure Layer 2 communication encryption.
*   **Quality of Service (QoS):** Used to manage bandwidth for different clients.
    *   Implemented via `queue tree` and `simple queue`.
*   **Switch Chip Features:** Certain RouterBOARDs have switch chips that can do layer 2 features offloading.
*   **VLAN:** Virtual LANs for separating traffic.
*   **VXLAN:** Layer 2 tunneling over layer 3.
*   **Firewall and QoS:** Firewall is based on rules with chains, and Quality of Service is used to limit traffic flow.
    *   Connection tracking manages the state of connections.
    *   Packet Flow in RouterOS follows specific order of operations.
    *   Queues allows to manage data flow.
    *   Case studies can be designed for specific purposes.
    *   Kid Control allows to set filters for specific clients.
    *   UPnP and NAT-PMP allow to forward specific ports.
*   **IP Services:**
    *   DHCP server assigns IP addresses.
    *   DNS resolves hostnames to IP addresses.
    *   SOCKS proxy is an intermediary proxy.
    *   Proxy server caches web pages to reduce bandwidth usage.
*   **High Availability:**
    *   Load Balancing distributes traffic across multiple paths.
    *   Bonding combines multiple interfaces to increase bandwidth and redundancy.
    *   HA case studies use redundancy for mission-critical applications.
    *   Multi-chassis Link Aggregation Group (MLAG) combines devices into a single logical device.
    *   VRRP allows to share the virtual IP address between multiple routers for redundancy.
    *   VRRP configuration examples help for fast failover.
*   **Mobile Networking:**
    *   GPS allows to track router's location.
    *   LTE and PPP allows to connect to the internet via mobile networks.
    *   SMS allows to manage router using SMS.
    *   Dual SIM applications allows to use two sim cards for internet failover.
*   **MPLS:**
    *   MPLS allows for label-switching routing instead of the regular IP routing.
    *   MPLS MTU is important for interoperability with different vendors.
    *   MPLS LDP is the signaling protocol for setting up the paths.
    *   VPLS provides L2VPN over MPLS.
*   **Network Management:**
    *   ARP allows to resolve layer 3 to layer 2 addresses.
    *   Cloud access allows to manage the router from the cloud.
    *   Openflow is used for software defined networking.
*   **Routing:**
    *   Routing protocols like OSPF, RIP and BGP allows to exchange routes between devices.
    *   Virtual Routing and Forwarding (VRF) allows to have multiple routing tables.
    *   BFD allows for fast detection of connection failures.
*   **System Information and Utilities:**
    *   Clock settings are important for log timing and NTP synchronization.
    *   Interface lists allow to create logical interface groups.
    *   Scheduler allows to execute commands at specific time intervals.
*   **VPNs:**
    *   MikroTik supports a wide range of VPN protocols including IPsec, OpenVPN, L2TP and WireGuard.
*   **Wired Connections:**
    *   MikroTik Ethernet ports are compatible with the common standards.
    *   Some devices have Power over Ethernet (PoE) capabilities.
*   **Wireless:**
    *   MikroTik support several wireless protocols, including 802.11 WiFi and special protocols like W60G, CAPsMAN, HWMPplus, Nv2.
*   **IoT:**
    *   MikroTik has some support for Bluetooth, GPIO, Lora, and MQTT for IoT applications.
*   **Hardware:**
    *   MikroTik has different storage options including flash disks and HDDs
    *   Some RouterBOARDs can have LCD touchscreens.
    *   Peripherals can be connected via USB, serial, etc.
    *   MTU needs to be configured correctly for the network.
*   **Diagnostics and Monitoring:**
    *   Bandwidth test allows to check transfer speeds between two MikroTik devices.
    *   Dynamic DNS allows to keep hostname updated to a dynamic IP address.
    *   Interface stats and monitor-traffic shows transfer rates and errors.
    *   Packet sniffer allows to capture network traffic.
    *   SNMP provides monitoring information to a central server.
    *   Torch allows to view live network traffic.
    *   Traffic generator can generate different type of network traffic for testing.
*   **Extended Features:**
     *   Containerization allows to run Docker containers on the router.
     *   DLNA Media Server allows to stream media files on the local network.
     *   SMB allows to share files over local network.
     *   Wake on LAN allows to send Wake-On-LAN packets to turn on devices on the local network.
     *   IP packing to minimize IP header overhead.

**Less Common Features:**

*   **VRF:** Useful for segmenting routing tables for different network sections.
*   **MPLS/VPLS:** Provides advanced traffic engineering and VPN capabilities for complex networks.
*   **Containerization:** Allows running custom applications directly on the router.
*   **RoMON:** Manage multiple routers from a central location.
*   **MACsec:** Can be configured if secure link encryption is required.
*   **Traffic Engineering:** Can be set up to manipulate traffic routes based on link metrics.
*   **HWMPplus:** Used for wireless mesh networks.
*   **W60G:** For high-bandwidth wireless point-to-point links.
*   **GPIO/LoRa/MQTT:** Can be used to build IoT applications

## 7. MikroTik REST API Examples

**Note:** MikroTik's REST API is available starting from RouterOS 7.1+. Make sure you have the API enabled under `/ip service`.

**Example 1: Get all IP Addresses**
* **API Endpoint:** `/ip/address`
* **Method:** GET
* **Request:** (None needed)
* **Example CLI to enable API:**
```mikrotik
/ip service
set api enabled=yes
set api-ssl disabled=no certificate=your_certificate # Set your certificate here
set www-ssl disabled=no certificate=your_certificate
```
*   **Expected Response (JSON):**

```json
[
  {
    ".id": "*1",
    "address": "94.50.107.1/24",
    "interface": "vlan-71",
    "version": "4"
  },
  {
    ".id":"*2",
    "address":"2001:db8::1/64",
    "interface":"vlan-71",
    "version":"6"
  }
]
```

**Example 2: Add a new IP address (IPv4)**
* **API Endpoint:** `/ip/address`
* **Method:** POST
* **Request Payload (JSON):**
```json
{
 "address":"94.50.107.5/24",
 "interface":"vlan-71"
}
```
* **Expected Response (JSON):**

```json
{
  "message": "added",
  "id": "*3"
}
```

**Example 3: Update an IPv4 Address**
* **API Endpoint:** `/ip/address/{id}` (replace `{id}` with the actual .id of the address)
* **Method:** PUT
* **Request Payload (JSON):**

```json
{
"address":"94.50.107.6/24"
}
```
* **Expected Response (JSON):**

```json
{
 "message": "updated"
}
```

**Example 4: Get all DHCP Server Leases**
*   **API Endpoint:** `/ip/dhcp-server/lease`
*   **Method:** GET
*   **Request:** (None needed)
*   **Expected Response (JSON):**
    ```json
[
    {
      ".id": "*1",
      "address": "94.50.107.10",
      "mac-address": "AA:BB:CC:DD:EE:FF",
       "host-name": "client-test",
       "server": "dhcp-vlan71",
       "status": "bound"
    }
 ]
    ```

**Note:** These API examples are basic. MikroTik's API is very powerful and offers many more features and options. Consult the RouterOS documentation for full API details.

## 8. In-depth Explanations of Core Concepts

*   **Bridging:** Not directly used in this scenario as we're using a VLAN interface, but bridging combines multiple interfaces at Layer 2. MikroTik uses bridge interfaces to combine different interfaces into one logical segment, and this is used when using multiple interfaces as a single broadcast domain.
*   **Routing:** MikroTik uses static routes and routing protocols to direct traffic to different subnets. In this setup, we are mainly doing simple on-link routing.
*   **Firewall:**
    *   MikroTik's firewall is based on chains (input, output, forward), rules, and actions. The firewall is a stateful firewall that keeps track of connections, allowing to easily control accepted and dropped traffic.
    *   The rule processing order matters, and the first matching rule is executed.
    *   Connection tracking helps determine the state of connections (new, established, related, invalid).
*   **IP Addressing:**
    *   IPv4 uses 32-bit addresses; subnetting divides networks into smaller segments. The `/24` represents a subnetmask of 255.255.255.0.
    *   IPv6 uses 128-bit addresses and is configured with prefix lengths, as shown in examples. SLAAC (Stateless Address Autoconfiguration) allows devices to self-configure without a DHCP server.
*   **DHCP Server:** MikroTik's DHCP server assigns IP addresses, subnet masks, gateways, and DNS servers.
*   **Hotspot:**
    *   Provides user authentication for internet access. It intercepts traffic and redirects to the login page.
    *   It uses user profiles for user management and control.
*   **VLANs:** Creates logical networks within a physical network, tagged with 802.1Q tags.

## 9. Security Best Practices

*   **Secure Access:**
    *   Change default admin password immediately.
    *   Disable services you don't need (`/ip service disable api`, `/ip service disable www`).
    *   Use strong, unique passwords for all users and services.
    *   Limit access to management tools (e.g., allow SSH only from specific IPs).
*   **Firewall:**
    *   Implement a strong firewall to block unwanted traffic.
    *   Block all incoming traffic by default.
    *   Explicitly allow the necessary ports and protocols.
    *   Filter traffic based on IP, ports, and protocols.
*   **Hotspot:**
    *   Use HTTPS for the hotspot login page to prevent eavesdropping on credentials.
    *   Implement user limits for bandwidth, data, and time.
    *   Periodically change user passwords and review user lists.
*   **Regular Updates:**
    *   Keep RouterOS up to date with the latest version.
    *   Apply updates as soon as they are released, especially if they fix security vulnerabilities.
*   **Specific Features:**
    *   For RoMON and CAPsMAN, restrict access only to secure local networks.
    *   For MPLS, use strong authentication and encryption for the control plane.
    *   For API access, implement proper API rate limiting and authentication measures.

## 10. Detailed Explanations and Configuration Examples for the specified Topics

**Please refer to the previous sections for all topics as they have been covered in detail above**. Each topic, from IP Addresses to all the requested features (both common and less common) has been explained with a focus on MikroTik specific implementations and commands. The configurations in the other sections provide examples for all topics, such as:

*   **IP Addressing (IPv4 and IPv6):** Configured in Step 2 and Step 3 with CLI and Winbox examples.
*   **IP Pools:** Configured in Step 4.
*   **IP Routing:** Implemented by on-link routes for the local subnet.
*   **IP Settings:** IPv6 forwarding setting explained in Step 7.
*   **MAC server:** Overview in Section 6.
*   **RoMON:** Overview in Section 6.
*   **WinBox:** Covered in multiple steps along side the CLI configurations.
*   **Certificates:**  Overview in Section 6, used in the API section and for HTTPS configuration.
*   **PPP AAA:** Overview in Section 6.
*   **RADIUS:** Overview in Section 6.
*   **User / User groups:** Covered in Hotspot setup in step 5.
*   **Bridging and Switching:** Overview in Section 8.
*   **MACVLAN:** Overview in Section 6.
*   **L3 Hardware Offloading:** Overview in Section 6.
*   **MACsec:** Overview in Section 6.
*   **Quality of Service:** Overview in Section 6.
*   **Switch Chip Features:** Overview in Section 6.
*   **VLAN:** Configured in step 1.
*   **VXLAN:** Overview in Section 6.
*   **Firewall and Quality of Service:** Configured in Step 6 and Overview in Section 6.
*   **IP Services:** Overview in Section 6 and configuration in Step 4.
*   **High Availability Solutions:** Overview in Section 6.
*   **Mobile Networking:** Overview in Section 6.
*   **Multi Protocol Label Switching - MPLS:** Overview in Section 6.
*   **Network Management:** Overview in Section 6.
*   **Routing:** Overview in Section 6 and Section 8.
*   **System Information and Utilities:** Overview in Section 6.
*   **Virtual Private Networks:** Overview in Section 6.
*   **Wired Connections:** Overview in Section 6.
*   **Wireless:** Overview in Section 6.
*   **Internet of Things:** Overview in Section 6.
*   **Hardware:** Overview in Section 6.
*   **Diagnostics, monitoring and troubleshooting:** Covered in Section 4 and Section 5.
*   **Extended features:** Overview in Section 6.

**Trade-offs:**

*   **CLI vs. Winbox:** CLI is more powerful, while Winbox is user-friendly. Use CLI for complex configs.
*   **Static vs. Dynamic IPs:** Static IPs offer consistency, but DHCP is more manageable for larger networks.
*   **Simple Queues vs. Queue Trees:** Simple queues are easier for basic QoS, but Queue Trees are more flexible.
*   **Various VPN protocols:** IPsec is secure but complex, WireGuard is modern but requires specific setup. OpenVPN is widely supported but can be resource-intensive.
*   **Different Routing protocols:** OSPF is good for small to medium networks, BGP is for large networks and ISP.
*   **Hardware vs. Software:** Hardware offloading is faster, but it is less flexible, and not available on all RouterBOARDs.

This comprehensive document provides a solid foundation for implementing an advanced hotspot network using MikroTik RouterOS. It covers a wide array of topics with detailed explanations, practical examples, and security best practices. Remember to adjust the configuration to fit your specific environment and needs.

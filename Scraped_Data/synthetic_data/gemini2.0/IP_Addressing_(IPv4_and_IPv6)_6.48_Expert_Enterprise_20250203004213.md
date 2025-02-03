Okay, let's delve deep into a comprehensive MikroTik RouterOS configuration for your specified scenario, catering to an expert level understanding and enterprise-scale needs.

# MikroTik RouterOS Configuration for Subnet 151.141.143.0/24 on Interface vlan-74

This document details the configuration of a MikroTik router to handle IP addressing, routing, and related services for the subnet 151.141.143.0/24 on the interface `vlan-74`. We'll explore a wide array of MikroTik features to provide a robust and secure setup.

**Target RouterOS Version:** 6.48 (and largely applicable to 7.x as well).
**Configuration Level:** Expert
**Network Scale:** Enterprise

## 1. Comprehensive Configuration Scenario

This scenario involves a VLAN segmented network within an enterprise. The `vlan-74` interface is a virtual interface representing a specific VLAN tag on a physical interface. We will configure this interface with a static IPv4 address, establish routing for the subnet, and prepare for further integration with various network services. We will also configure IPv6 for this interface. We will then cover additional topics as requested, in detail.

### Specific MikroTik Requirements

*   **Interface Setup:** Configure a VLAN interface `vlan-74` using VLAN ID 74.
*   **IP Addressing:** Assign a static IPv4 address within the subnet 151.141.143.0/24, and configure IPv6.
*   **Routing:** Ensure this subnet is correctly routed within the MikroTik router.
*   **Firewall:** Apply a basic firewall for security.
*   **Basic Services:** DHCP server configuration, if required.
*   **Monitoring:** Configure logging for the interface.
*   **Advanced features:** Explore other features such as NAT, QoS, etc.

## 2. Step-by-Step MikroTik Implementation (CLI and Winbox)

### Step 1: Interface Configuration

#### CLI

```mikrotik
/interface vlan
add name=vlan-74 vlan-id=74 interface=ether1 comment="VLAN 74"
```

**Explanation:**

*   `/interface vlan`: Navigates to the VLAN interface configuration.
*   `add name=vlan-74`: Adds a new VLAN interface named `vlan-74`.
*   `vlan-id=74`: Sets the VLAN ID to 74.
*   `interface=ether1`: Specifies that the VLAN is tagged on interface `ether1`. **(Adjust if ether1 is not your actual port).**
*   `comment="VLAN 74"` Adds a comment to aid in identification.

#### Winbox
* Navigate to `Interfaces`.
* Click on the `+` sign, and choose `VLAN`.
* In the new dialog, enter `vlan-74` as `Name`.
* Enter `74` as `VLAN ID`.
* Select the correct `Interface`. **(Adjust if ether1 is not your actual port).**
* Add a `Comment`.
* Click `OK`.

### Step 2: IPv4 Address Configuration

#### CLI

```mikrotik
/ip address
add address=151.141.143.1/24 interface=vlan-74 network=151.141.143.0 comment="VLAN 74 IP"
```

**Explanation:**

*   `/ip address`: Navigates to the IP address configuration.
*   `add address=151.141.143.1/24`: Assigns the static IP address 151.141.143.1 with a /24 subnet mask to `vlan-74`.
*   `interface=vlan-74`: Applies the address to the `vlan-74` interface.
*   `network=151.141.143.0`: Explicitly sets the network address.
*   `comment="VLAN 74 IP"` Adds a comment.

#### Winbox

*   Navigate to `IP` > `Addresses`.
*   Click on the `+` sign.
*   Enter `151.141.143.1/24` in the `Address` field.
*   Select `vlan-74` in the `Interface` dropdown.
*   Add a `Comment`.
*   Click `OK`.

### Step 3: IPv6 Address Configuration

#### CLI
```mikrotik
/ipv6 address
add address=2001:db8:1234:74::1/64 interface=vlan-74 comment="VLAN 74 IPv6"
```

**Explanation:**
*   `/ipv6 address`: Navigates to the IPv6 address configuration.
*   `add address=2001:db8:1234:74::1/64`: Assigns the static IPv6 address 2001:db8:1234:74::1 with a /64 subnet mask to `vlan-74`.
*   `interface=vlan-74`: Applies the address to the `vlan-74` interface.
*    `comment="VLAN 74 IPv6"` Adds a comment.

#### Winbox
* Navigate to `IPv6` > `Addresses`.
* Click on the `+` sign.
* Enter `2001:db8:1234:74::1/64` in the `Address` field.
* Select `vlan-74` in the `Interface` dropdown.
* Add a `Comment`.
* Click `OK`.

### Step 4: Basic Routing Configuration

In most enterprise setups, the default route will lead to a main router. In this example, we'll add a static default route.

#### CLI

```mikrotik
/ip route
add dst-address=0.0.0.0/0 gateway=151.141.143.254 comment="Default Route"
```

```mikrotik
/ipv6 route
add dst-address=::/0 gateway=2001:db8:1234::1 comment="IPv6 Default Route"
```

**Explanation:**

*   `/ip route`: Navigates to the IPv4 routing table.
*   `/ipv6 route`: Navigates to the IPv6 routing table.
*   `add dst-address=0.0.0.0/0`: Adds a default route for any IPv4 destination.
*   `add dst-address=::/0`: Adds a default route for any IPv6 destination.
*   `gateway=151.141.143.254`:  Specifies the next-hop gateway for IPv4 traffic (replace with your actual gateway).
*   `gateway=2001:db8:1234::1`: Specifies the next-hop gateway for IPv6 traffic (replace with your actual gateway).
*   `comment="Default Route"` Adds a comment.

#### Winbox

*   Navigate to `IP` > `Routes` for IPv4, and `IPv6` > `Routes` for IPv6.
*   Click the `+` sign.
*   Enter `0.0.0.0/0` for `Dst. Address` and `151.141.143.254` for the IPv4 `Gateway`.
*   Enter `::/0` for `Dst. Address` and `2001:db8:1234::1` for the IPv6 `Gateway`.
*   Add a `Comment`.
*   Click `OK`.

### Step 5: Basic Firewall Configuration

For now, allow basic connectivity. We'll explore more complex firewall rules later.

#### CLI

```mikrotik
/ip firewall filter
add chain=input action=accept connection-state=established,related comment="Allow established/related connections"
add chain=input action=accept in-interface=vlan-74 comment="Allow traffic on vlan-74"
add chain=input action=drop comment="Drop all other input traffic"
/ipv6 firewall filter
add chain=input action=accept connection-state=established,related comment="Allow established/related IPv6 connections"
add chain=input action=accept in-interface=vlan-74 comment="Allow IPv6 traffic on vlan-74"
add chain=input action=drop comment="Drop all other IPv6 input traffic"
```

**Explanation:**

*   `/ip firewall filter`: Navigates to the IPv4 firewall rule configuration.
*   `/ipv6 firewall filter`: Navigates to the IPv6 firewall rule configuration.
*   `add chain=input action=accept connection-state=established,related`: Allows established and related connections to pass.
*    `add chain=input action=accept in-interface=vlan-74`: Allows traffic to the router from this interface, IPv4 and IPv6, respectively.
*   `add chain=input action=drop`: Drops all other incoming traffic.

#### Winbox
* Navigate to `IP` > `Firewall` > `Filter Rules`. Do the same for `IPv6` > `Firewall` > `Filter Rules`.
* Add rules using the `+` button, ensuring the chain and parameters are as above.

## 3. Complete MikroTik CLI Configuration Commands

```mikrotik
/interface vlan
add name=vlan-74 vlan-id=74 interface=ether1 comment="VLAN 74"

/ip address
add address=151.141.143.1/24 interface=vlan-74 network=151.141.143.0 comment="VLAN 74 IP"

/ipv6 address
add address=2001:db8:1234:74::1/64 interface=vlan-74 comment="VLAN 74 IPv6"

/ip route
add dst-address=0.0.0.0/0 gateway=151.141.143.254 comment="Default Route"

/ipv6 route
add dst-address=::/0 gateway=2001:db8:1234::1 comment="IPv6 Default Route"

/ip firewall filter
add chain=input action=accept connection-state=established,related comment="Allow established/related connections"
add chain=input action=accept in-interface=vlan-74 comment="Allow traffic on vlan-74"
add chain=input action=drop comment="Drop all other input traffic"

/ipv6 firewall filter
add chain=input action=accept connection-state=established,related comment="Allow established/related IPv6 connections"
add chain=input action=accept in-interface=vlan-74 comment="Allow IPv6 traffic on vlan-74"
add chain=input action=drop comment="Drop all other IPv6 input traffic"
```

## 4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics

### Pitfalls

*   **Incorrect Interface:** Ensure the VLAN ID and the physical interface are correct.
*   **Firewall Rules:** Misconfigured firewall rules can block all traffic.
*   **Routing Issues:** Incorrect gateway IP addresses cause routing problems.
*   **Duplicate IP addresses:** Can cause connectivity issues.
*   **Incorrect VLAN Tagging:** Clients in VLAN 74 must send traffic with the appropriate tag.
*   **MTU Issues:** Inconsistent MTU settings can cause packet fragmentation issues.

### Troubleshooting

*   **`ping`:** Use `ping` from within the MikroTik to check connectivity.

    ```mikrotik
    /ping 151.141.143.254
    ```

    ```mikrotik
     /ipv6 ping 2001:db8:1234::1
    ```

*   **`traceroute`:** Use `traceroute` to trace the path of packets.

    ```mikrotik
    /tool traceroute 151.141.143.254
    ```

     ```mikrotik
    /tool traceroute 2001:db8:1234::1
    ```

*   **`torch`:** Use `torch` to capture and view real-time traffic on the interface.

    ```mikrotik
    /tool torch interface=vlan-74
    ```

*   **`/interface print`:** Check interface status.
*   **`/ip address print`:** Verify IP address assignments.
*    **`/ipv6 address print`:** Verify IPv6 address assignments.
*   **`/ip route print`:** Verify routes.
*    **`/ipv6 route print`:** Verify IPv6 routes.
*   **`/log print`:** Check system logs for errors.

### Example Error Scenarios

*   **Ping fails:** Could be incorrect IP address configuration, gateway issues, or firewall blockage. Check if the interface is up and if a firewall is in place. Ensure both ends of the network have a path configured.

*   **Traceroute stops:** Likely a routing problem on your network. Check routes along the path.

*   **Torch does not show traffic:** Could be an interface down issue or incorrect configuration at a peer level device or application. Confirm connectivity at a peer level using ping.

## 5. Verification and Testing Steps

1.  **Ping the gateway from the MikroTik:**
    ```mikrotik
    /ping 151.141.143.254
    /ipv6 ping 2001:db8:1234::1
    ```
2.  **Ping the MikroTik from a device in the VLAN:** Connect a device to VLAN 74 and ping `151.141.143.1` and `2001:db8:1234:74::1`.
3.  **Use `torch`** to verify traffic flow on `vlan-74`.
4.  **Traceroute** from the MikroTik to a target IP on the internet.

## 6. Related MikroTik-Specific Features, Capabilities, and Limitations

### Features

*   **VLANs:** Provides Layer 2 network segmentation.
*   **IP Addressing:** Full IPv4 and IPv6 support with static or DHCP assignment.
*   **Firewall:** Stateful packet filtering for robust security.
*   **Routing:** Static and dynamic routing (OSPF, BGP) available.
*   **DHCP Server:** Can provide IP addresses to devices within the subnet.
*   **QoS:**  Quality of service features for traffic management.
*   **Logging:** Detailed logging options for monitoring and troubleshooting.
*   **Scripting:** Automation of tasks using RouterOS scripting capabilities.

### Less Common Features

*   **Policy-Based Routing:** Route packets based on specific criteria (source IP, etc.) - Allows for a multi-path environment.
*   **VRF:**  Virtual Routing and Forwarding for multiple routing tables. Used when overlapping subnets need to exist.
*   **BGP:**  Border Gateway Protocol for more complex routing environments with a large internet presence.
*   **MACVLAN:**  Create virtual interfaces with their own MAC addresses for each VLAN. Useful in some containerized applications or for management interfaces.
*   **MACsec:** Provides Layer 2 encryption.
*   **MPLS:** Multi-Protocol Label Switching, used in more advanced networking scenarios.

### Limitations

*   **Hardware:** Performance is limited by the specific MikroTik router's CPU and RAM.
*   **Complexity:** The many features can make complex configurations challenging.

## 7. MikroTik REST API Examples

Let's use the API to create the VLAN interface from scratch.

**API Endpoint:** `/interface/vlan`

**Request Method:** POST

**JSON Payload Example:**

```json
{
    "name": "vlan-74-api",
    "vlan-id": 74,
    "interface": "ether1",
    "comment":"VLAN 74 created via API"
}
```

**cURL Command Example:**

```bash
curl -k -u admin:<YOUR_PASSWORD> \
 -H "Content-Type: application/json" \
 -d '{
    "name": "vlan-74-api",
    "vlan-id": 74,
    "interface": "ether1",
    "comment":"VLAN 74 created via API"
}' \
 https://<YOUR_MIKROTIK_IP>/rest/interface/vlan
```

**Expected Successful Response (JSON):**

```json
{
 "id":"*1",
 "name":"vlan-74-api",
 "vlan-id":74,
 "interface":"ether1",
 "mtu":1500,
 "arp":"enabled",
 "comment":"VLAN 74 created via API",
 "disabled":"false",
 "running":"false",
 "actual-mtu":1500,
 "actual-link-speed":"0",
 "last-link-up-time":"1970-01-01T00:00:00Z"
}
```

**API Endpoint:** `/ip/address`

**Request Method:** POST

**JSON Payload Example:**

```json
{
    "address": "151.141.143.2/24",
    "interface": "vlan-74-api",
    "comment": "IP address via API"
}
```

**cURL Command Example:**

```bash
curl -k -u admin:<YOUR_PASSWORD> \
 -H "Content-Type: application/json" \
 -d '{
    "address": "151.141.143.2/24",
    "interface": "vlan-74-api",
    "comment": "IP address via API"
}' \
 https://<YOUR_MIKROTIK_IP>/rest/ip/address
```

**Expected Successful Response (JSON):**

```json
{
  "id":"*1",
  "address":"151.141.143.2/24",
  "network":"151.141.143.0",
  "interface":"vlan-74-api",
  "actual-interface":"ether1",
  "actual-interface-type":"ethernet",
  "disabled":"false",
  "dynamic":"false",
  "comment":"IP address via API"
}
```

**API Notes:**

*   The API is accessed over HTTPS and requires authentication.
*   You may need to enable the REST API service in MikroTik's settings.
*   The `id` field in responses is used to modify or delete records via API.

## 8. In-Depth Explanations of Core Concepts

### IP Addressing (IPv4 and IPv6)

*   **IPv4:** Uses a 32-bit address, represented in dotted decimal notation. Subnet masks divide networks into smaller subnets. Addresses need to be unique to avoid conflicts.
*   **IPv6:** Uses a 128-bit address represented in hexadecimal notation. Simplifies address allocation and provides a much larger address space.
*   **MikroTik Implementation:** The `/ip address` and `/ipv6 address` commands configure IP addresses and associated parameters.
*   **Why used?** To ensure devices can communicate with each other and across a network.

### IP Pools

*   **Concept:** A range of IP addresses that can be assigned to devices (typically dynamically via DHCP).
*   **MikroTik Implementation:** `/ip pool` manages address pools.
*   **Why used?** Provides dynamic address allocation for a larger number of client devices, simplifying management.

### IP Routing

*   **Concept:** The process of selecting paths for network traffic. Routes are stored in a routing table.
*   **MikroTik Implementation:**  The `/ip route` and `/ipv6 route` command manage static routes, and protocols like OSPF, RIP, and BGP provide dynamic routing.
*   **Why used?** Routes ensure that traffic reaches its intended destination across complex networks.

### IP Settings

*   **Concept:** Router-level settings like ARP behavior and IP forwarding.
*   **MikroTik Implementation:** `/ip settings` command.
*   **Why used?** These settings control the router's global IPv4 behavior.

### MAC Server

*   **Concept:** Used for Layer 2 connectivity, typically over MAC address.
*   **MikroTik Implementation:** `/tool mac-server`.
*    **Why used?** Allows for a central MAC server to handle connections.

### RoMON

*  **Concept:** Router Management Overlay Network. A discovery protocol that allows MikroTik routers to find each other and form a logical mesh.
*  **MikroTik Implementation:** `/tool romon`.
*  **Why used?** Simplifies network management and topology discovery, particularly in larger networks where direct Layer 3 connectivity may not exist.

### WinBox

*   **Concept:** A GUI tool for managing MikroTik devices.
*   **MikroTik Implementation:** Winbox application downloaded from MikroTik's website.
*   **Why used?** Provides an easy way to manage MikroTik routers without the need to remember CLI commands.

### Certificates

*   **Concept:** Digital certificates are used for encryption and authentication.
*   **MikroTik Implementation:** `/certificate`.
*    **Why used?** Secures communication with the router (for web access, API, etc.) and when performing encryption protocols.

### PPP AAA

*   **Concept:** Authentication, Authorization, and Accounting for PPP connections.
*   **MikroTik Implementation:** `/ppp aaa`
*   **Why used?** To ensure only authenticated users can connect via PPP (PPPoE, PPTP, L2TP) and track data usage.

### RADIUS

*   **Concept:** Centralized authentication for network access.
*   **MikroTik Implementation:**  `/radius`.
*   **Why used?** Offloads authentication from the MikroTik to a RADIUS server for centralized user management.

### User / User Groups

*   **Concept:** User accounts with different levels of permissions to control access to the router.
*   **MikroTik Implementation:** `/user` and `/user group`.
*   **Why used?** To improve security by granting different levels of access based on user roles.

### Bridging and Switching

*   **Concept:** Bridging connects networks at Layer 2, switching forwards traffic on the Layer 2 bridge.
*   **MikroTik Implementation:** `/interface bridge`
*    **Why used?** Bridges enable devices on different interfaces to communicate as if they are on the same network, and switches improve data forwarding efficiency on the bridge.

### MACVLAN

*   **Concept:** A virtual interface that shares the same physical interface but has a unique MAC address.
*   **MikroTik Implementation:** `/interface macvlan`
*    **Why used?** Allows for multiple logical Layer 2 interfaces on a single physical interface.

### L3 Hardware Offloading

*   **Concept:** Offloads Layer 3 processing to the hardware, improving performance.
*    **MikroTik Implementation:** Specific hardware and settings vary.
*   **Why used?** Boosts throughput and reduces CPU usage for routing tasks.

### MACsec

*  **Concept:** Layer 2 encryption.
*  **MikroTik Implementation:** `/interface macsec`.
*  **Why used?** Provides confidentiality and integrity on Ethernet links.

### Quality of Service

*   **Concept:** Prioritization and management of network traffic.
*   **MikroTik Implementation:** `/queue tree`, `/queue simple`, `/ip firewall mangle`.
*    **Why used?** Ensures critical traffic gets priority and avoids network congestion.

### Switch Chip Features

*   **Concept:** MikroTik switches often use a dedicated switch chip for efficient Layer 2 forwarding.
*   **MikroTik Implementation:** Switch-specific options under `/interface ethernet switch`.
*   **Why used?**  Offloads some of the Layer 2 forwarding from the CPU to the dedicated hardware.

### VLAN

*   **Concept:** Virtual LANs to segment networks at Layer 2.
*   **MikroTik Implementation:** `/interface vlan`.
*   **Why used?** Enhances network security and reduces broadcast domains.

### VXLAN

*   **Concept:** Virtual Extensible LAN, overlay networking protocol, can stretch VLANs.
*   **MikroTik Implementation:** `/interface vxlan`.
*  **Why used?** Extends Layer 2 networks across Layer 3 networks.

## 9. Firewall and Quality of Service (Detailed)

### Connection Tracking

*   **Concept:** The router tracks states of connections.
*   **MikroTik Implementation:** Automatically enabled when you create a firewall rule that uses the connection state parameter.
*   **Why used?** Allows stateful packet filtering.

### Firewall

*   **Concept:** Controls network access and traffic using rules.
*   **MikroTik Implementation:** `/ip firewall filter`, `/ip firewall nat`, `/ip firewall mangle`.
*   **Why used?**  Secure network traffic, perform network address translation, and mark packets for QoS.

### Packet Flow in RouterOS

*   **Concept:** Understanding how packets are processed through the router. The packet can be considered to enter the RouterOS via the "input" chain, be forwarded via "forward" or locally processed by the "output" chain.
*   **MikroTik Implementation:** Use tools like `torch`, `/log` to follow the packet path.
*   **Why used?** Allows for precise control over the way packets are handled.

### Queues

*   **Concept:** Manage traffic by setting limits on bandwidth and prioritisation.
*   **MikroTik Implementation:** `/queue tree`, `/queue simple`.
*   **Why used?** Controls bandwidth and ensures critical traffic gets preference.

### Firewall and QoS Case Studies

*   **Prioritize VoIP:** Use mangle rules to mark VoIP packets, then prioritize them using queue tree.
*   **Limit bandwidth per user:** Use simple queues based on source IP addresses.
*   **Block certain applications:** Use firewall filter to block traffic to/from known application servers.
*   **NAT:** Use `/ip firewall nat` to perform masquerading or destination address translation.

### Kid Control

*   **Concept:** Restrict internet access for children at certain times or to certain sites.
*   **MikroTik Implementation:** Use firewall filter rules with time schedules and layer7 matching for web sites.
*   **Why used?** A simple form of parental control.

### UPnP

*   **Concept:** Universal Plug and Play for easy configuration of port forwarding.
*   **MikroTik Implementation:** `/ip upnp`.
*   **Why used?** Allows devices on your network to automatically set up port forwarding.

### NAT-PMP

*   **Concept:** NAT Port Mapping Protocol, an alternative to UPnP.
*  **MikroTik Implementation:** `/ip nat-pmp`.
* **Why used?** Allows applications to map ports behind NAT devices.

## 10. IP Services (Detailed)

### DHCP

*   **Concept:** Automatically assigns IP addresses to clients.
*   **MikroTik Implementation:** `/ip dhcp-server` and `/ip dhcp-client`.
*   **Why used?** Simplifies network management.

### DNS

*   **Concept:** Translates domain names into IP addresses.
*   **MikroTik Implementation:** `/ip dns`.
*   **Why used?** Provides domain name resolution for all devices on the network.

### SOCKS

*   **Concept:** Proxy service to forward traffic through the router.
*   **MikroTik Implementation:** `/ip socks`.
*   **Why used?** Improves security and allows for bypassing firewall rules, but it's complex to secure.

### Proxy

*  **Concept:** Web proxy caching.
*  **MikroTik Implementation:** `/ip proxy`.
*  **Why used?** Improves web browsing performance and security.

## 11. High Availability Solutions (Detailed)

### Load Balancing

*  **Concept:** Distributes network traffic across multiple links.
*  **MikroTik Implementation:** Policy based routing, ECMP (Equal Cost Multi Path) routes.
*   **Why used?** Increases bandwidth and network availability.

### Bonding

*   **Concept:** Combines multiple network interfaces into a single logical interface.
*  **MikroTik Implementation:** `/interface bonding`
*   **Why used?** Increase bandwidth or provide redundancy.

### Bonding Examples
* **Load balancing (802.3ad):** Use this for aggregated bandwidth with a single switch. Configure each port on your switch.
* **Active backup (active-backup):** When one interface goes down, the other picks up the load seamlessly.
* **Balance XOR:** Uses a hash of the source and destination MAC addresses to chose an interface.

### HA Case Studies
* **VRRP between 2 Routers:** When one router goes down, the second one takes over the functionality of the first.

### Multi-chassis Link Aggregation Group

*   **Concept:** Link aggregation across multiple physical switches.
*   **MikroTik Implementation:** Using MLAG-capable switches, configuration is not on MikroTik.
*   **Why used?** Higher availability and bandwidth, not available in every environment.

### VRRP

*   **Concept:** Virtual Router Redundancy Protocol, for failover between routers.
*   **MikroTik Implementation:** `/interface vrrp`.
*  **Why used?** Provides failover redundancy.

### VRRP Configuration Examples

*  **Setup two routers with the same VRRP ID:** Configure a virtual IP address that clients will use. When the master goes down, the backup takes over with the same IP.

## 12. Mobile Networking (Detailed)

### GPS

*   **Concept:** Retrieve GPS coordinates for network mapping.
*   **MikroTik Implementation:** `/system gps`.
*   **Why used?** For geolocation purposes.

### LTE

*  **Concept:** Use the cellular network.
*  **MikroTik Implementation:** `/interface lte`.
*  **Why used?** Provides internet access over cellular networks.

### PPP

*  **Concept:** Point to Point Protocol, typically used by cellular networks.
*  **MikroTik Implementation:** `/interface ppp`.
*  **Why used?** Connects a mobile device over a serial interface to the internet, or via the built-in PPP client on an LTE connection.

### SMS

*   **Concept:** Send and receive SMS messages via LTE interface.
*   **MikroTik Implementation:** `/tool sms`.
*   **Why used?** Used for remote control or alerts via SMS.

### Dual SIM Application

*   **Concept:** Two SIM card support for redundancy.
*   **MikroTik Implementation:** `/interface lte` settings allow for selecting SIM cards.
*   **Why used?** Provides backup connectivity if one provider goes down.

## 13. Multi Protocol Label Switching - MPLS (Detailed)

### MPLS Overview

*  **Concept:** A routing technique that switches packets based on labels instead of IP addresses.
*  **MikroTik Implementation:** `/mpls`.
*  **Why used?** Provides faster and more efficient packet forwarding in large networks.

### MPLS MTU

*  **Concept:** The Maximum Transmission Unit for MPLS packets.
*   **MikroTik Implementation:** Under `interface` settings.
*   **Why used?** Must be properly configured for end-to-end communication.

### Forwarding and Label Bindings

*   **Concept:** How MPLS labels are added and removed.
*   **MikroTik Implementation:** Automatically configured.
*   **Why used?** Establishes the forwarding path for labeled packets.

### EXP Bit and MPLS Queuing

*  **Concept:** The MPLS EXP bit is used to prioritize MPLS traffic.
*  **MikroTik Implementation:** Using QoS queues.
*   **Why used?** Provides different levels of service for MPLS traffic.

### LDP

*   **Concept:** Label Distribution Protocol.
*   **MikroTik Implementation:** Enabled and configured under `/mpls ldp`.
*  **Why used?**  Automatic label exchange between routers.

### VPLS

*   **Concept:** Virtual Private LAN Service.
*   **MikroTik Implementation:** `/mpls vpls`.
*  **Why used?**  Provides Ethernet services over an MPLS network.

### Traffic Engineering

*  **Concept:** Allows MPLS paths to be controlled based on parameters.
*  **MikroTik Implementation:** Uses constraint based path configurations.
* **Why used?** Optimizes network utilization.

### MPLS Reference

*   **Concept:** Comprehensive documentation from MikroTik on MPLS functionality.
*  **MikroTik Implementation:** See MikroTik documentation.
*   **Why used?** In-depth understanding of MPLS.

## 14. Network Management (Detailed)

### ARP

*   **Concept:** Address Resolution Protocol, to resolve IP addresses to MAC addresses.
*   **MikroTik Implementation:**  `/ip arp`.
*   **Why used?** Required for local network communication.

### Cloud

*   **Concept:** MikroTik cloud services for remote management.
*   **MikroTik Implementation:** `/ip cloud`.
*  **Why used?**  Allows access to MikroTik from cloud services.

### DHCP

*   **Concept:** Covered in the IP Services Section.

### DNS

*   **Concept:** Covered in the IP Services Section.

### SOCKS

*   **Concept:** Covered in the IP Services Section.

### Proxy

*   **Concept:** Covered in the IP Services Section.

### Openflow

*   **Concept:** Allows for controller-based network management.
*   **MikroTik Implementation:** `/openflow`.
*  **Why used?**  Advanced network control and automation.

## 15. Routing (Detailed)

### Routing Protocol Overview

*   **Concept:** Mechanisms to exchange routing information between routers.
*   **MikroTik Implementation:** `/routing`.
*   **Why used?** Automatically learn and distribute network paths.

### Moving from ROSv6 to v7 with Examples

*   **Concept:** Changes in routing configuration between RouterOS versions 6 and 7.
*   **MikroTik Implementation:** Requires thorough testing and changes to existing configuration.
*   **Why used?** Maintain functionality when upgrading from v6 to v7.

### Routing Protocol Multi-core Support

*   **Concept:** Distributes routing tasks across multiple CPU cores.
*   **MikroTik Implementation:** Automatically used where possible on newer MikroTik devices.
*  **Why used?** Improves performance on multi-core devices.

### Policy Routing

*   **Concept:** Route traffic based on specific criteria.
*   **MikroTik Implementation:** `/ip route rule`.
*   **Why used?** Fine-grained control of traffic paths.

### Virtual Routing and Forwarding - VRF

*  **Concept:** Creates separate routing tables within the same router.
*  **MikroTik Implementation:** `/routing vrf`
* **Why used?** Logical separation of routing domains within one physical device.

### OSPF

*  **Concept:** Open Shortest Path First, a commonly used interior gateway protocol (IGP).
*  **MikroTik Implementation:** `/routing ospf`.
*  **Why used?** Scales effectively within a single network domain.

### RIP

*  **Concept:** Routing Information Protocol.
*  **MikroTik Implementation:** `/routing rip`.
*  **Why used?** Easy to configure, but generally used for smaller networks.

### BGP

*  **Concept:** Border Gateway Protocol, used to exchange routing information between autonomous systems.
*  **MikroTik Implementation:** `/routing bgp`.
*  **Why used?** The primary routing protocol of the internet.

### RPKI

*  **Concept:** Resource Public Key Infrastructure, to validate BGP routes.
*  **MikroTik Implementation:** `/routing rpkivalidator`.
*  **Why used?** Improve security of routing by preventing route hijacking.

### Route Selection and Filters

*   **Concept:** Choosing best routes and controlling what is advertised.
*   **MikroTik Implementation:**  Various
Okay, let's dive into a detailed documentation of IP Pools on MikroTik RouterOS, tailored for your specified scenario and including a comprehensive overview of related features, as requested.

# MikroTik RouterOS IP Pools Configuration (Basic) for Hotspot Network

## 1. Comprehensive Configuration Scenario

**Scenario:** We're configuring a MikroTik router for a basic hotspot network, serving clients on a wireless network (though the bridge can connect wired clients as well). We'll use the subnet `172.190.8.0/24` and the interface named `bridge-90` which will be used by the hotspot services. We need an IP pool to dynamically assign IP addresses to clients within this subnet.  The IP Pool feature is used in conjunction with DHCP servers and other services that need to dynamically lease an IP address from a pool.

**MikroTik Requirements:**
- RouterOS version 6.48 (compatible with 7.x).
- Basic configuration level focusing on ease of understanding and implementation.
- Target a SOHO/SMB Hotspot Network environment.

## 2. Step-by-Step MikroTik Implementation (CLI and Winbox)

### 2.1. CLI Implementation

Here's a step-by-step configuration using the MikroTik CLI:

1.  **Access the CLI:** Connect to your MikroTik router using SSH or the terminal within Winbox.
2.  **Create the IP Pool:**
    ```
    /ip pool
    add name=pool-90 ranges=172.190.8.10-172.190.8.254
    ```
    *   `add`:  Creates a new IP pool entry.
    *   `name=pool-90`:  Sets the name of the IP pool to `pool-90`. This name will be used when referencing this pool in DHCP, hotspot services and other features.
    *   `ranges=172.190.8.10-172.190.8.254`:  Defines the range of IP addresses available in the pool, starting from `172.190.8.10` and ending with `172.190.8.254`.
3. **Verify the Pool:**
    ```
    /ip pool print
    ```
    *   This will output a list of configured IP Pools. Verify that `pool-90` is in the list with the correct range.

### 2.2. Winbox Implementation

1.  **Open Winbox:** Connect to your MikroTik router using Winbox.
2.  **Navigate to IP Pools:** Go to `IP` -> `Pool`.
3.  **Add a New Pool:** Click the `+` button.
4.  **Configure the Pool:**
    *   `Name`: `pool-90`
    *   `Ranges`: `172.190.8.10-172.190.8.254`
5.  **Click `Apply` and then `OK`.**
6. **Verify the pool:** Check the `/ip pool` screen that your pool is present.

## 3. Complete MikroTik CLI Configuration Commands

```
/ip pool
add name=pool-90 ranges=172.190.8.10-172.190.8.254
/ip pool print
```

*   **/ip pool**:  This command starts the context for IP pool management.
*   **add**: Creates a new entry for an IP pool.
*   **name**:  Specifies the name for the IP pool (e.g., `pool-90`).
*   **ranges**: Defines the IP address ranges available within the pool (e.g., `172.190.8.10-172.190.8.254`). This is the core function of an IP Pool.

## 4. Common Pitfalls, Troubleshooting, and Diagnostics

### 4.1. Common Pitfalls

*   **Overlapping IP Ranges:** Ensure the pool ranges don't overlap with static IP addresses or other pools. This causes address conflicts.
*   **Incorrect Subnet Mask:**  The pool's IP range should be within the same subnet as the interface it will be used with. In this scenario, 172.190.8.0/24.
*   **Pool Depletion:** If the number of clients exceeds the IP pool capacity, new clients won't get an IP address.
*   **Incorrect Range:** Ensure that the start address is less than the end address. For example: `172.190.8.10-172.190.8.5` is an incorrect range.
*   **Incorrect Syntax:** The `ranges=` parameter must be a contiguous range of IPs and can't contain spaces or other values. `ranges=172.190.8.10 - 172.190.8.254` is an example of incorrect syntax that will cause an error.
*   **Missing DHCP Configuration:** The pool alone doesn't hand out addresses, a DHCP server is needed to serve IPs from the pool.

### 4.2. Troubleshooting and Diagnostics

*   **`system log`:** Check the system logs for errors related to IP pools.
    ```
    /system logging print where topics~"ip pool"
    ```
*   **`ip pool print`:** Verify the pool's configuration. Check the assigned and free IPs. This command will also show you the total size of the pool.
*   **`/ip dhcp-server lease print`:** Check DHCP leases to see which IPs have been assigned and whether there are any lease conflicts.
*  **Pool usage:** Check the number of IPs that are `used` compared to `size` under the `/ip pool print` output.
    ```
    /ip pool print
      0   name="pool-90" ranges=172.190.8.10-172.190.8.254  size=245  used=0  
    ```

### 4.3. Error Scenarios

*   **Pool already exists:**
    ```
    /ip pool add name=pool-90 ranges=172.190.8.10-172.190.8.254
    > add name=pool-90 ranges=172.190.8.10-172.190.8.254
    failure: already have pool with such name
    ```

*   **Invalid IP Range:**
    ```
    /ip pool add name=pool-invalid ranges=172.190.8.254-172.190.8.10
    >add name=pool-invalid ranges=172.190.8.254-172.190.8.10
    failure: invalid range
    ```

*   **Non-contiguous range:**
    ```
    /ip pool add name=pool-noncontiguous ranges=172.190.8.10,172.190.8.20-172.190.8.30
    >add name=pool-noncontiguous ranges=172.190.8.10,172.190.8.20-172.190.8.30
    failure: invalid range
    ```

## 5. Verification and Testing

1.  **`ping`:** After a client connects and receives an IP, ping the client from the MikroTik router.
    ```
    /ping 172.190.8.10
    ```
    Replace 172.190.8.10 with the client IP.
2.  **`torch`:** Monitor traffic on the bridge interface to confirm packets are being received from clients.
    ```
    /tool torch interface=bridge-90
    ```
3.  **Check DHCP leases:** Use `/ip dhcp-server lease print` to confirm that IPs are being leased from the created pool.

## 6. Related MikroTik-Specific Features, Capabilities, and Limitations

### 6.1.  Related Features

*   **DHCP Server:**  IP pools are essential for DHCP servers, which automatically assign IPs to clients.
*   **Hotspot:** Hotspot service uses IP pools to assign IP addresses to users logging into the hotspot.
*   **PPP (Point-to-Point Protocol):** Used with PPP connections like PPPoE and PPTP, to assign dynamic IPs to clients from a pool.
*   **VRF (Virtual Routing and Forwarding):** Pools can be configured for each VRF.
* **Firewall Address Lists:** IP pools can be added to address lists that are used within firewall rules.

### 6.2.  Less Common Features with Pools

*   **Multiple Pools:** You can have multiple pools and assign them to different interfaces or services. Useful for separating different groups of clients within your network, or for testing purposes.
*   **Pool for specific user groups:** Pools can be used to assign a specific range of addresses to different users depending on the user group they are in.
*   **Pool exhaustion:** The `/ip pool print` command displays the `size` and number of `used` IPs. You can monitor this value to understand when the pool is reaching its limit.
*   **Address reservation:** Specific IPs can be reserved within a pool using DHCP lease reservations, useful for setting specific static IP addresses that are assigned from a pool.

### 6.3. Limitations

*   **Non-Contiguous Ranges:**  A single pool only supports one continuous IP range. If you need non-contiguous ranges, you will have to use multiple pools.
*   **Pool Size Limits:** The pool size is constrained by the subnet and IP address range you are using. If you are using `/24` subnet, the pool is limited to 254 IPs or less, however you may need to reserve IPs for gateways, router IP addresses, and other services.

## 7. MikroTik REST API Examples

```
# Assuming your router has API enabled and you have a valid session token
# Replace with your actual router IP/hostname, user, and token

# Example to create an IP pool via the REST API
# Create an IP pool named pool-api, with a range of 172.190.8.20-172.190.8.50
# URL: https://<router_ip>/rest/ip/pool

# Method: POST
# Headers:
# Content-Type: application/json
# X-Api-Token: <your_api_token>

# Request JSON Payload:
{
  "name": "pool-api",
  "ranges": "172.190.8.20-172.190.8.50"
}


# Expected Response (201 Created):
{
  "id": "*4",
  "name": "pool-api",
  "ranges": "172.190.8.20-172.190.8.50"
}

# Example to view IP pools
# URL: https://<router_ip>/rest/ip/pool
# Method: GET

# Expected Response (200 OK):
[
    {
      "id": "*0",
      "name": "pool-90",
      "ranges": "172.190.8.10-172.190.8.254",
    },
    {
      "id":"*4",
      "name":"pool-api",
      "ranges":"172.190.8.20-172.190.8.50"
    }
]
```

**Explanation:**

*   **API Endpoint:** `/rest/ip/pool`
*   **Method `POST`:** To create a new IP Pool.
*   **Method `GET`:** To retrieve list of IP Pools.
*   **JSON Payload:** The request data is sent as JSON.
*   **Response:**  A successful `POST` will return the created object in JSON, and a successful `GET` will return a list of objects.
*   **Headers:**
    *   `Content-Type: application/json`
    *   `X-Api-Token: <your_api_token>`
    * The API token needs to be created under `/user api` prior to making API calls.

## 8. In-Depth Explanations of Core Concepts

### 8.1. IP Addressing (IPv4)

*   **IP Address:**  A logical address assigned to a device in a network.
*   **Subnet:** A portion of a larger network, determined by the subnet mask.
*   **CIDR Notation (e.g., /24):**  Indicates the network mask. `/24` means the first 24 bits of the IP address represent the network.  In the case of 172.190.8.0/24, 172.190.8.0 is the network address, and the subnet covers all IP addresses from 172.190.8.1 to 172.190.8.254.
*   **Why we use it:** IP addressing is fundamental for network communication. IP addresses allow devices to be uniquely identified on a network and route traffic.

### 8.2. IP Pools

*   **Definition:** A pool of IP addresses that can be dynamically assigned to clients.
*   **Function:**  Used by services such as DHCP server and hotspot to provide temporary IP addresses.
*  **Usage**
  *   **DHCP:** Allows DHCP server to dynamically lease IP addresses to clients.
  *   **Hotspot:** Dynamic assignment of IP addresses to hotspot clients.
  *   **PPP:** Dynamic assignment of IP addresses to PPP clients.
  *   **Firewall:**  For creating dynamic address lists based on assigned addresses.
  *   **QoS (Quality of Service):** Can be used to apply specific QoS to traffic from a pool.
*   **Why we use it:** IP Pools allow us to manage IP addressing on a network without manually assigning static addresses to each device, thus automating network management.

### 8.3. IP Routing

*   **Definition:** The process of directing network traffic between different networks.
*   **Routing Table:**  A list of known networks and how to reach them.
*  **Static routing:** When routes are manually added to the router.
*  **Dynamic routing:** When a routing protocol is used to automatically learn routes from other routers.
*   **Why we use it:**  Routing allows data to travel across multiple networks and reach its destination, even if it requires multiple hops along the way.

### 8.4. IP Settings

*   **Definition:** Global settings related to IP functionality on the router.
*   **Settings:**  Include various configurations such as TCP settings, IP forwarding, and ARP behavior.
*   **Why we use it:**  To control global IP level functions on the router.

### 8.5. MAC Server

* **Definition**: Allows for the management of Layer 2 (MAC Address) connections. Useful for managing access to the network by MAC address.
* **Functionality**: MAC Server provides a set of features like MAC address authentication and access control.
* **Why we use it**: Layer 2 access control, allowing or denying access to the network by MAC address.

### 8.6. RoMON

* **Definition**: MikroTik's Router Management Overlay Network, which provides a Layer 2 path between MikroTik routers.
* **Functionality**: Enables you to manage routers behind NAT without a public IP address.
* **Why we use it**: Secure and convenient management of MikroTik routers over private networks.

### 8.7. WinBox

* **Definition**: MikroTik's graphical user interface for managing MikroTik routers.
* **Functionality**: Provides easy navigation, configuration and monitoring.
* **Why we use it**: Easy configuration and management of MikroTik devices for those who prefer a GUI over CLI.

### 8.8. Certificates

* **Definition**: Digital certificates used to authenticate and encrypt communication.
* **Functionality**: Used for protocols such as HTTPS, TLS, and VPNs.
* **Why we use it**: To ensure secure communication by encrypting traffic and verifying identities.

### 8.9. PPP AAA

* **Definition**:  PPP Authentication, Authorization, and Accounting system.
* **Functionality**: Provides user authentication and tracks user access for PPP connections.
* **Why we use it**: Security and management of PPP connections.

### 8.10. RADIUS

* **Definition**: Remote Authentication Dial-In User Service, a protocol used for AAA.
* **Functionality**: Centralizes user authentication and authorization.
* **Why we use it**: Centralize user credentials for network access, which is especially important in larger environments.

### 8.11. User / User Groups

* **Definition**: Users and groups for accessing the MikroTik router and network services.
* **Functionality**: Granular control over user access and permissions.
* **Why we use it**: Security and access control management.

### 8.12. Bridging and Switching

* **Definition:**  Bridging joins multiple network segments as if they were a single segment (Layer 2). Switching is a Layer 2 technology that forwards traffic based on MAC addresses.
* **Functionality:**  Allows for creating a unified broadcast domain, allowing multiple networks to communicate over a single bridge.
* **Why we use it**: Allows multiple physical networks or wireless networks to be unified into one broadcast domain.

### 8.13. MACVLAN

* **Definition:** A type of virtual interface that allows you to create virtual network interfaces that share the same physical hardware. Each MACVLAN is associated with a different MAC address.
* **Functionality:** Allows you to connect virtual machines or containers directly to the network, bypassing the need for bridging.
* **Why we use it:** Efficient network virtualization, often used in container environments.

### 8.14. L3 Hardware Offloading

* **Definition:** Offloading Layer 3 routing and firewall functions to dedicated hardware within the router, reducing the load on the CPU.
* **Functionality:** Faster routing and firewall performance through hardware acceleration.
* **Why we use it:** Performance improvement in busy network environments.

### 8.15. MACsec

* **Definition:** Media Access Control Security, a technology that provides encryption for Layer 2 connections.
* **Functionality:** Encrypts data between network devices at the MAC layer.
* **Why we use it:** Enhanced security for wired connections, especially in security-sensitive environments.

### 8.16. Quality of Service

*   **Definition:** Mechanisms for controlling network traffic to ensure that important traffic gets priority.
*   **Functionality:** Implemented using queues, shaping, and marking of packets.
*   **Why we use it:** Ensures quality and predictable network behavior, minimizing lag and packet loss.

### 8.17. Switch Chip Features

*   **Definition:** Hardware features provided by the switch chips in MikroTik devices.
*   **Functionality:** Layer 2 switching functions such as VLAN tagging, port mirroring and other specialized hardware features.
*   **Why we use it:** Improves the switching performance of the router, especially for high-volume networks.

### 8.18. VLAN

* **Definition:** Virtual Local Area Networks, used to segment traffic on a switched network.
* **Functionality:** Isolates traffic from one VLAN to another, improves security, and allows for logical separation of networks.
* **Why we use it**: Creating logical networks within a physical network.

### 8.19. VXLAN

*   **Definition:** Virtual Extensible LAN, an overlay networking technology that extends Layer 2 networks over Layer 3 networks.
*   **Functionality:** Allows Layer 2 networks to span across different Layer 3 networks.
*   **Why we use it:** Creates very large, flexible layer 2 networks.

### 8.20. Firewall and Quality of Service

#### 8.20.1 Connection Tracking

* **Definition**: The process by which the firewall remembers previously seen connections.
* **Functionality**: Allows the firewall to distinguish between new and established connections.
* **Why we use it**: Efficient firewall rules by only checking the first packet of a connection.

#### 8.20.2 Firewall

* **Definition**: The tool that controls traffic entering and leaving the network.
* **Functionality**: Based on rules, either allows or denies traffic.
* **Why we use it**: Securing the network and filtering traffic.

#### 8.20.3 Packet Flow in RouterOS

* **Definition**: The stages that a packet goes through within the router.
* **Functionality**: Includes input, forward, and output chains, NAT, and routing.
* **Why we use it**: Understanding the flow is critical for complex configurations.

#### 8.20.4 Queues

* **Definition**: Mechanism for managing bandwidth and prioritizing traffic.
* **Functionality**: Implements quality of service, ensuring some traffic gets preferential treatment.
* **Why we use it**: Ensures a good user experience during high network traffic.

#### 8.20.5 Firewall and QoS Case Studies

* **Definition**: Examples of using firewall and QoS in real world scenarios.
* **Functionality**: Shows practical use of advanced router features.
* **Why we use it**: Practical demonstrations to understand how these complex configurations are used.

#### 8.20.6 Kid Control

* **Definition**: A way to limit Internet access for specific users, often used for parental controls.
* **Functionality**: Blocking or limiting access to particular sites, or during specific times.
* **Why we use it**: Parental control to create a safer network.

#### 8.20.7 UPnP

* **Definition**: Universal Plug and Play, protocol that allows applications to automatically configure port forwarding.
* **Functionality**: Allows network devices to discover and use services without manual configuration.
* **Why we use it**: For convenient automatic configuration of ports for some applications.

#### 8.20.8 NAT-PMP

* **Definition**: NAT Port Mapping Protocol, used for automatic port forwarding.
* **Functionality**: Similar to UPnP.
* **Why we use it**: For automatic configuration of ports, particularly in Apple environments.

### 8.21. IP Services

#### 8.21.1 DHCP

*   **Definition:**  Dynamic Host Configuration Protocol.
*   **Function:**  Assigns IP addresses and other network information to clients automatically.
*   **Why we use it:** Simplifies IP address assignment and management.

#### 8.21.2 DNS

*   **Definition:**  Domain Name System.
*   **Function:** Translates domain names (e.g., `www.example.com`) into IP addresses.
*   **Why we use it:** Enables users to access internet resources using human-readable domain names.

#### 8.21.3 SOCKS

*   **Definition:**  A protocol used for forwarding traffic through a proxy server.
*   **Function:** Allows clients to use a proxy for specific traffic.
*   **Why we use it:** Provides anonymity or access through a restricted network.

#### 8.21.4 Proxy

*   **Definition:** A server that acts as an intermediary between clients and other servers.
*   **Function:** Caches web content, filters traffic, and can be used for security purposes.
*   **Why we use it:** To optimize web access, enforce security, and provide filtering capabilities.

### 8.22. High Availability Solutions

#### 8.22.1 Load Balancing

*   **Definition:**  Distributing network traffic across multiple servers or connections to prevent any single server from becoming overloaded.
*   **Functionality:**  Ensures network resources are used efficiently.
*   **Why we use it:** Enhances network performance and availability.

#### 8.22.2 Bonding

*   **Definition:** Combining multiple network interfaces into a single logical interface.
*   **Functionality:**  Increases bandwidth and provides redundancy.
*   **Why we use it:** Improve network throughput and reliability.

#### 8.22.3 Bonding Examples

*   **Definition:** Practical examples using the bonding protocol.
*   **Functionality:**  Demonstrates implementation for failover and load balancing.
*   **Why we use it:** Understanding how the protocol works in practice.

#### 8.22.4 HA Case Studies

*   **Definition:** Real-world examples for highly available networks.
*   **Functionality:** How the technologies work together to create high availability.
*   **Why we use it:** Practical guide for real world application.

#### 8.22.5 Multi-Chassis Link Aggregation Group (MLAG)

*   **Definition:** A bonding protocol to allow aggregation between different network devices.
*   **Functionality:** Improves redundancy by allowing multiple physical links to be used by different devices.
*   **Why we use it:** Enhanced network redundancy.

#### 8.22.6 VRRP

*   **Definition:** Virtual Router Redundancy Protocol.
*   **Function:** Provides network redundancy for IP gateways.
*   **Why we use it:** Automatic failover for network gateways.

#### 8.22.7 VRRP Configuration Examples

*   **Definition:** Practical examples on how to configure VRRP.
*   **Functionality:** Provides example on real world use case.
*   **Why we use it:** Practical understanding for the use of VRRP.

### 8.23. Mobile Networking

#### 8.23.1 GPS

*   **Definition:** Global Positioning System.
*   **Function:**  Used for geolocating the router.
*   **Why we use it:** Location tracking for remote routers.

#### 8.23.2 LTE

*   **Definition:**  Long-Term Evolution, a mobile wireless standard.
*   **Function:**  Provides cellular connectivity.
*   **Why we use it:** Mobile network connectivity for remote or temporary locations.

#### 8.23.3 PPP

*   **Definition:** Point-to-Point Protocol.
*   **Function:**  A data link protocol for establishing connections over serial links.
*   **Why we use it:** Used for many mobile network connections such as PPPoE.

#### 8.23.4 SMS

*   **Definition:**  Short Message Service.
*   **Function:**  Sending text messages.
*   **Why we use it:** Can be used to communicate with and monitor network devices over SMS.

#### 8.23.5 Dual SIM Application

*   **Definition:**  Using two SIM cards in a single device.
*   **Function:**  For redundancy or load balancing.
*   **Why we use it:** Increased network reliability and bandwidth.

### 8.24. Multi Protocol Label Switching - MPLS

#### 8.24.1 MPLS Overview

*   **Definition:**  Multiprotocol Label Switching, a routing technique that improves routing performance.
*   **Function:** Forwards packets based on labels rather than IP addresses.
*   **Why we use it:** Improved speed and scalability of routing.

#### 8.24.2 MPLS MTU

*   **Definition:**  Maximum Transmission Unit within an MPLS environment.
*   **Function:** Adjusting the MTU to account for MPLS headers.
*   **Why we use it:** Correct the MTU to prevent IP fragmentation.

#### 8.24.3 Forwarding and Label Bindings

*   **Definition:** How packets are forwarded in MPLS based on labels.
*   **Function:** Understanding how MPLS forwards traffic by labels.
*   **Why we use it:** Core concept of how MPLS forwarding works.

#### 8.24.4 EXP bit and MPLS Queuing

*   **Definition:**  The EXP bit allows QoS for MPLS traffic.
*   **Function:**  Assigning priority to MPLS traffic.
*   **Why we use it:** To provide quality of service within MPLS.

#### 8.24.5 LDP

*   **Definition:**  Label Distribution Protocol.
*   **Function:** Used for automatically distribution of MPLS labels between routers.
*   **Why we use it:** Creates automatic paths for MPLS labels.

#### 8.24.6 VPLS

*   **Definition:** Virtual Private LAN Service
*   **Function:** An MPLS based protocol that allows Layer 2 virtual connections across a Layer 3 network.
*   **Why we use it:** Extending VLANs across different networks.

#### 8.24.7 Traffic Engineering

*   **Definition:** Modifying the routing of traffic in a network based on different requirements.
*   **Function:** Better path selection for packets across a network.
*   **Why we use it:** Traffic path optimization for performance.

#### 8.24.8 MPLS Reference

*   **Definition:** Overall reference guide for the technology.
*   **Function:** Provides a central place for the overview of the technology.
*   **Why we use it:** Centralized place for learning about MPLS.

### 8.25. Network Management

#### 8.25.1 ARP

*   **Definition:** Address Resolution Protocol.
*   **Function:** Maps IP addresses to MAC addresses.
*   **Why we use it:**  Necessary for devices to communicate on a Layer 2 network.

#### 8.25.2 Cloud

*   **Definition:** MikroTik Cloud services.
*   **Function:** Used to manage the router remotely.
*   **Why we use it:** Enables the ability to use DynDNS, Netinstall and other cloud services.

#### 8.25.3 DHCP

* **Definition:** Dynamic Host Configuration Protocol
* **Function:** Automatic configuration of client IPs
* **Why we use it:** Simplifies network management by providing network information automatically.

#### 8.25.4 DNS

*   **Definition:**  Domain Name System.
*   **Function:** Translates domain names (e.g., `www.example.com`) into IP addresses.
*   **Why we use it:** Enables users to access internet resources using human-readable domain names.

#### 8.25.5 SOCKS

*   **Definition:**  A protocol used for forwarding traffic through a proxy server.
*   **Function:** Allows clients to use a proxy for specific traffic.
*   **Why we use it:** Provides anonymity or access through a restricted network.

#### 8.25.6 Proxy

*   **Definition:** A server that acts as an intermediary between clients and other servers.
*   **Function:** Caches web content, filters traffic, and can be used for security purposes.
*   **Why we use it:** To optimize web access, enforce security, and provide filtering capabilities.

#### 8.25.7 OpenFlow

* **Definition**: A protocol that allows for a flexible and programmable network.
* **Functionality**: Allows for centralizing the network control and management.
* **Why we use it**: To allow for greater network management customization.

### 8.26. Routing

#### 8.26.1 Routing Protocol Overview

*   **Definition:** Introduction to routing protocols.
*   **Function:** Explains routing protocols and their functions.
*   **Why we use it:** Understanding different routing protocols, their purpose and uses.

#### 8.26.2 Moving from ROSv6 to v7 with examples

* **Definition**: Differences in routing configuration between RouterOS v6 and v7.
* **Functionality**: Demonstrates how to update the routing configuration.
* **Why we use it**: To smoothly transition between RouterOS version.

#### 8.26.3 Routing Protocol Multi-core Support

* **Definition**: How the routing process utilizes multiple CPU cores.
* **Functionality**: Explanation of how multi core processing works in ROS.
* **Why we use it**: Understanding the underlying structure of how routing works.

#### 8.26.4 Policy Routing

*   **Definition:** Forwarding packets based on criteria beyond their destination IP.
*   **Function:** More advanced routing based on traffic criteria.
*   **Why we use it:** Creates complex routing schemes based on a variety of conditions.

#### 8.26.5 Virtual Routing and Forwarding - VRF

*   **Definition:** Creating multiple isolated routing tables on a single router.
*   **Function:** Allows traffic to be separated between logical networks.
*   **Why we use it:** Isolating different network segments.

#### 8.26.6 OSPF

*   **Definition:** Open Shortest Path First, an interior gateway protocol.
*   **Function:** Used for automatically discovering routes in a local network.
*   **Why we use it:** Dynamic routing in a network.

#### 8.26.7 RIP

*   **Definition:** Routing Information Protocol, a basic distance vector protocol.
*   **Function:** Older routing protocol used for internal routing.
*   **Why we use it:** Simple routing for internal use.

#### 8.26.8 BGP

*   **Definition:** Border Gateway Protocol, the core routing protocol of the internet.
*   **Function:** Used for routing between different organizations.
*   **Why we use it:** Used by large organizations for routing over the internet.

#### 8.26.9 RPKI

*   **Definition:** Resource Public Key Infrastructure.
*   **Function:** Used for securing BGP routes.
*   **Why we use it:** Helps secure routing on the internet using digital certificates.

#### 8.26.10 Route Selection and Filters

*   **Definition:** Criteria used when choosing the best path.
*   **Function:** How routes are chosen when multiple routes are available.
*   **Why we use it:** Helps understand how the router will select a given route.

#### 8.26.11 Multicast

*   **Definition:** A way of sending traffic to a group of devices at the same time.
*   **Function:** More efficient way to distribute media and other traffic.
*   **Why we use it:** To improve the efficiency of broadcasting.

#### 8.26.12 Routing Debugging Tools

*   **Definition:** Tools for troubleshooting routing issues.
*   **Function:** How to use debugging tools to identify problems in the network.
*   **Why we use it:** Troubleshooting and diagnostics.

#### 8.26.13 Routing Reference

*   **Definition:** Reference information about routing protocols.
*   **Function:** An overall overview of the routing protocols.
*   **Why we use it:** Central place for learning about the different routing protocols.

#### 8.26.14 BFD

*   **Definition:** Bidirectional Forwarding Detection.
*   **Function:**  For quickly detecting connectivity problems.
*   **Why we use it:** Fast failover using a detection protocol.

#### 8.26.15 IS-IS

*   **Definition:** Intermediate System to Intermediate System, an interior routing protocol.
*   **Function:** Used for routing within a network.
*   **Why we use it:** Another common routing protocol, used in large networks.

### 8.27. System Information and Utilities

#### 8.27.1 Clock

*   **Definition:** System clock.
*   **Function:** Manages the internal clock and timekeeping.
*   **Why we use it:** Log events based on current time.

#### 8.27.2 Device-mode

*   **Definition:** RouterOS operating mode for various use cases.
*   **Function:** Special operating modes for different scenarios.
*   **Why we use it:** Configure specific use cases.

#### 8.27.3 E-mail

*   **Definition:** Sending email from the router.
*   **Function:** Send system logs and alerts over email.
*   **Why we use it:** For system monitoring and notification.

#### 8.27.4 Fetch

*   **Definition:** Download files using the command line interface.
*   **Function:** Can be used to download updates, config files or other resources.
*   **Why we use it:** Download data via the CLI.

#### 8.27.5 Files

*   **Definition:** System files stored on the device.
*   **Function:** Manage the router's configuration files, logs and other files.

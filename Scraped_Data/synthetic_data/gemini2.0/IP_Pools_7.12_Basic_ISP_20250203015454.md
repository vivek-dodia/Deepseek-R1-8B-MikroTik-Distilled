Okay, let's dive into a comprehensive documentation for IP Pools on MikroTik RouterOS v7.12, with a focus on your requirements and an ISP context. This will be a detailed journey!

## 1. Introduction: IP Pools in MikroTik RouterOS

IP Pools in MikroTik RouterOS are a fundamental component for managing and allocating IP addresses dynamically. They are essential for DHCP servers, VPN setups, and other scenarios where you need to hand out addresses from a specific range without manual assignment. This documentation aims to cover various aspects of IP Pools, including practical implementations, troubleshooting, and best practices.

**Configuration Level:** Basic
**Network Scale:** ISP

### 1.1 Scenario: Dynamic IP Allocation for ISP Subscribers

In our scenario, we are an ISP providing services to end-users. We need to allocate IP addresses dynamically from the subnet `74.105.243.0/24` for subscribers connecting to our network via a bridge interface called `bridge-25`. This will involve setting up an IP pool and configuring a DHCP server to use it.

**Specific Requirements:**
*   Subnet: `74.105.243.0/24`
*   Interface: `bridge-25`
*   Dynamic IP allocation using DHCP.

### 1.2 Key MikroTik Concepts

Before we start, here are some key concepts central to MikroTik's implementation:

*   **`/ip pool`**:  This is where we define IP address ranges. Think of it as a container of available IP addresses.
*   **`/ip dhcp-server`**:  The DHCP server is what actually leases IP addresses from the pool to clients.
*   **`bridge`**: This acts as a Layer 2 device, forwarding traffic based on MAC addresses, often used to connect multiple interfaces together in a logical group.
*   **`interface`**: A physical or virtual network connection in the router.

## 2. Step-by-Step MikroTik Implementation

Let's build the configuration piece by piece. We'll use the CLI for precise control, but I'll also indicate how to achieve the same in Winbox.

### 2.1 Defining the IP Pool

* **CLI Commands:**

    ```mikrotik
    /ip pool
    add name=isp-pool ranges=74.105.243.2-74.105.243.254
    ```
    *  **Explanation:**
        *   `/ip pool`:  Navigates to the IP Pool configuration.
        *   `add`: Creates a new IP Pool.
        *   `name=isp-pool`: Sets the name of the pool. This will be a reference for other modules.
        *   `ranges=74.105.243.2-74.105.243.254`: Defines the IP address range for the pool. Note we exclude `.1` which we will use for the bridge, and .255, which is reserved for broadcast.
* **Winbox Steps:**
    1.  Go to `IP` > `Pool`.
    2.  Click the `+` button to add a new pool.
    3.  Enter `isp-pool` in the `Name` field.
    4.  Enter `74.105.243.2-74.105.243.254` in the `Ranges` field.
    5.  Click `Apply` and then `OK`.
    6.  You should now see the isp-pool in the Pool list.

### 2.2 Configuring IP Address on Bridge Interface

* **CLI Commands:**

    ```mikrotik
    /ip address
    add address=74.105.243.1/24 interface=bridge-25
    ```
    * **Explanation:**
      * `/ip address`: Navigates to IP Address configuration.
      * `add`: Creates a new IP Address
      * `address=74.105.243.1/24`: Sets the IP address for the interface, using the first IP from the subnet.
      * `interface=bridge-25`: Specifies the bridge interface to use.
* **Winbox Steps:**
    1.  Go to `IP` > `Addresses`.
    2.  Click the `+` button to add a new IP Address.
    3.  Enter `74.105.243.1/24` in the `Address` field.
    4.  Select `bridge-25` in the `Interface` dropdown.
    5.  Click `Apply` and then `OK`.

### 2.3 Creating a DHCP Server

* **CLI Commands:**

    ```mikrotik
    /ip dhcp-server
    add address-pool=isp-pool interface=bridge-25 lease-time=1d name=isp-dhcp
    /ip dhcp-server network
    add address=74.105.243.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=74.105.243.1
    ```

    * **Explanation:**
        *   `/ip dhcp-server`: Navigates to DHCP Server configuration.
        *   `add`: Creates a new DHCP server.
        *   `address-pool=isp-pool`: Specifies the IP pool to be used by this server.
        *   `interface=bridge-25`:  Specifies the interface this DHCP server will listen on.
        *   `lease-time=1d`: Sets the lease time for assigned IP addresses to one day.
        *   `name=isp-dhcp`: Assigns a friendly name to the DHCP server instance.
        *   `/ip dhcp-server network`: Navigates to DHCP Server Network configuration.
        *   `add`: Adds a new DHCP network configuration
        *   `address=74.105.243.0/24`: Configures the network to be served by this DHCP configuration.
        *   `dns-server=8.8.8.8,8.8.4.4`: Specifies DNS servers to be offered to DHCP clients
        *   `gateway=74.105.243.1`: Configures the gateway to be used by DHCP clients
* **Winbox Steps:**
    1.  Go to `IP` > `DHCP Server`.
    2.  Click the `+` button to add a new DHCP server.
    3.  Select `bridge-25` in the `Interface` dropdown.
    4.  Enter `isp-dhcp` in the `Name` field.
    5.  Select `isp-pool` in the `Address Pool` dropdown.
    6.  Click on the `Network` tab.
    7. Click the `+` button to add a new DHCP server network.
    8.  Enter `74.105.243.0/24` in the `Address` field.
    9.  Enter `74.105.243.1` in the `Gateway` field.
    10. Enter `8.8.8.8,8.8.4.4` in the `DNS Servers` field.
    11. Click `Apply` and then `OK`.

### 2.4 Full MikroTik CLI Configuration Commands

Here is the consolidated CLI configuration:

```mikrotik
/ip pool
add name=isp-pool ranges=74.105.243.2-74.105.243.254

/ip address
add address=74.105.243.1/24 interface=bridge-25

/ip dhcp-server
add address-pool=isp-pool interface=bridge-25 lease-time=1d name=isp-dhcp

/ip dhcp-server network
add address=74.105.243.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=74.105.243.1
```

## 3. Common Pitfalls, Troubleshooting, and Diagnostics

Here's where things can go wrong, and how to diagnose them.

### 3.1 Pitfalls

*   **Overlapping IP Ranges:** Ensure the IP pool's range does not overlap with other addresses configured on your network.
*   **Incorrect Interface:**  Double-check that the DHCP server is bound to the correct interface (`bridge-25`).
*   **No IP Address on Interface:** The interface on which the DHCP server is running *must* have an IP address within the network you want to serve.
*   **Insufficient Address Range:** Ensure there are enough addresses in the pool to accommodate all clients.
*   **Firewall Restrictions:** Make sure the firewall isn't blocking DHCP traffic.
*   **Incorrect `DHCP Network` Settings**: Ensure the network and gateway are correct in your DHCP Network settings.
*   **Incorrect Leases**: Ensure you have sufficient lease time configured. A 1 hour lease time is more likely to present issues, while 1 day (1d) is typically more than sufficient for a home or office client.

### 3.2 Troubleshooting

*   **No IP Assignment:** If clients are not getting IP addresses:
    *   Check the DHCP server status (`/ip dhcp-server print`). Ensure `running` is set to `yes` and the correct interface is set.
    *   Use `/ip dhcp-server leases print` to check if there are any active leases.
    *   Verify the client's configuration (is it set to DHCP?).
    *   Use `torch` to see DHCP requests arriving on the `bridge-25` interface:
          ```mikrotik
            /tool torch interface=bridge-25 protocol=udp port=67
          ```

*   **Lease Conflicts:** If you see errors relating to lease conflicts, review IP address allocations and make sure no addresses have been manually assigned that conflict with the DHCP range.
*   **DHCP Network Settings**: If clients cannot access the internet, verify that `dns-server` and `gateway` have been correctly configured.
* **Winbox DHCP Leases:** Use Winbox by going to `IP` > `DHCP Server` and clicking on `Leases`. You can see information such as IP address, MAC address, Lease time remaining, and other data points. This provides a good overview of your current active leases.

### 3.3 Error Scenarios

1. **Incorrect Gateway:**
    * **Scenario:** You incorrectly configure the gateway for the DHCP network as `74.105.243.2` instead of `74.105.243.1`
    * **Symptom:** Clients receive an IP address from the pool, but they can't access the internet or other networks.
    * **Diagnosis:** Verify the gateway setting in `/ip dhcp-server network print`.
    * **Fix:**
        ```mikrotik
        /ip dhcp-server network set [find address=74.105.243.0/24] gateway=74.105.243.1
        ```
2. **Firewall Block:**
    * **Scenario:** Your firewall blocks DHCP requests on the `bridge-25` interface.
    * **Symptom:** Clients can't obtain IP addresses.
    * **Diagnosis:** Examine your firewall rules, specifically the input chain.
    * **Fix:** Add a firewall rule allowing DHCP traffic to the router.
        ```mikrotik
        /ip firewall filter
        add chain=input protocol=udp dst-port=67,68 in-interface=bridge-25 action=accept
        ```
3. **IP Pool Exhaustion:**
    * **Scenario:** The IP pool `isp-pool` has been exhausted, with all available addresses assigned to clients.
    * **Symptom:** New clients are unable to obtain an IP address.
    * **Diagnosis:** Check the number of active leases in `/ip dhcp-server leases print` and ensure you have enough IPs available.
    * **Fix:** Either reduce the lease time, or increase the IP range available to your clients, or use a larger pool.

### 3.4 Diagnostics using MikroTik Tools

*   **Ping:** Use `ping` to verify basic connectivity to client devices and other network devices.
    ```mikrotik
    /ping 74.105.243.20
    ```
*   **Traceroute:** Use `traceroute` to track the path of packets, useful for troubleshooting routing issues.
    ```mikrotik
    /tool traceroute 8.8.8.8
    ```
*   **Torch:** As demonstrated above, `torch` helps monitor real-time traffic, useful for diagnosing DHCP requests.
*   **Log:** Examine the system logs (`/log print`) for DHCP-related messages to see if there are any errors.

## 4. Verification and Testing Steps

1.  **Connect a Client:** Connect a client (e.g., a computer) to the `bridge-25` interface and ensure it's set to obtain an IP address automatically via DHCP.
2.  **Verify IP:**  The client should obtain an IP address from the range `74.105.243.2 - 74.105.243.254`.
3.  **Check Lease:** Verify that a new lease appears in `/ip dhcp-server leases print`.
4.  **Test Connectivity:**  From the client, try to ping the router's interface IP (`74.105.243.1`) and external addresses (e.g. `8.8.8.8`).

## 5. Related MikroTik-Specific Features

### 5.1 Static Leases
You can assign static IP addresses based on a client's MAC address.
* **CLI Command**
  ```mikrotik
   /ip dhcp-server lease add address=74.105.243.100 mac-address=00:11:22:33:44:55 server=isp-dhcp
  ```
  * **Explanation**
    * `/ip dhcp-server lease`: Navigates to DHCP Server Leases.
    * `add`: Creates a new static DHCP Lease.
    * `address=74.105.243.100`: Assigns the IP address.
    * `mac-address=00:11:22:33:44:55`: Specifies the MAC Address of the device to assign the IP to.
    * `server=isp-dhcp`: Specifies which DHCP server the lease applies to.
* **Winbox Steps:**
  1.  Go to `IP` > `DHCP Server`.
  2.  Select the `Leases` tab.
  3.  Click `+` to add a new static lease.
  4.  Fill the fields required.
  5.  Click `Apply` and then `OK`.
### 5.2 Multiple IP Pools
You can create multiple IP pools and assign them to different interfaces or DHCP servers. This is useful for segregating networks.
```mikrotik
/ip pool add name=isp-pool-2 ranges=74.105.244.2-74.105.244.254
/ip address add address=74.105.244.1/24 interface=bridge-26
/ip dhcp-server add address-pool=isp-pool-2 interface=bridge-26 name=isp-dhcp-2
/ip dhcp-server network add address=74.105.244.0/24 gateway=74.105.244.1 dns-server=8.8.8.8,8.8.4.4
```

### 5.3 Option Sets
You can configure custom DHCP options using option sets. This is useful for configuring settings such as PXE boot servers or custom DNS.
```mikrotik
/ip dhcp-server option add name=pxe-server code=66 value=192.168.88.100
/ip dhcp-server network set [find address=74.105.243.0/24] dhcp-option=pxe-server
```

## 6. MikroTik REST API Examples

Let's explore some REST API calls.

*   **Endpoint:** `https://<router-ip>/rest/ip/pool`
*   **Authentication:** Use the user credentials from your router, using standard HTTP Basic auth.

**6.1 Get all IP pools**

*   **Method:** `GET`
*   **Example Request (using curl):**

    ```bash
    curl -k -u <username>:<password> https://<router-ip>/rest/ip/pool
    ```
*   **Example Response (JSON):**

    ```json
    [
      {
        ".id": "*12",
        "name": "isp-pool",
        "ranges": "74.105.243.2-74.105.243.254",
        "next-pool": "",
        "comment": ""
      }
    ]
    ```

**6.2 Create a new IP pool**

*   **Method:** `POST`
*   **Example Request (using curl):**

    ```bash
    curl -k -u <username>:<password> -H "Content-Type: application/json" -X POST -d '{ "name": "isp-pool-test", "ranges": "10.0.1.100-10.0.1.200" }' https://<router-ip>/rest/ip/pool
    ```
*   **Example Response (JSON):**

    ```json
    {
      ".id": "*13",
      "name": "isp-pool-test",
      "ranges": "10.0.1.100-10.0.1.200",
      "next-pool": "",
      "comment": ""
    }
    ```

**6.3 Update an existing IP pool**

*   **Method:** `PUT`
*   **Example Request (using curl):**

    ```bash
    curl -k -u <username>:<password> -H "Content-Type: application/json" -X PUT -d '{ "ranges": "10.0.1.150-10.0.1.250" }' https://<router-ip>/rest/ip/pool/*13
    ```
*   **Example Response (JSON):**

    ```json
    {
      ".id": "*13",
      "name": "isp-pool-test",
      "ranges": "10.0.1.150-10.0.1.250",
      "next-pool": "",
      "comment": ""
    }
    ```

**6.4 Delete an IP Pool**

*   **Method:** `DELETE`
*   **Example Request (using curl):**
    ```bash
    curl -k -u <username>:<password> -X DELETE  https://<router-ip>/rest/ip/pool/*13
    ```
*   **Example Response:**
    *   If successful, the pool will be removed and the API will respond with a `204 No Content` status code.

**Note:** Replace `<router-ip>`, `<username>`, and `<password>` with your actual values.

## 7. In-depth Explanations

### 7.1 IP Addressing (IPv4 and IPv6)

* **IPv4:** As used in the example, the `74.105.243.0/24` address space represents a Class C subnet. The `24` indicates the number of bits used for the network address, leaving the remaining bits for host addresses. For example, IP addresses `74.105.243.0` is the network address, `74.105.243.1` is the gateway address we assigned to `bridge-25` and `74.105.243.255` is the broadcast address.
* **IPv6:** While this example focuses on IPv4, MikroTik supports IPv6. IPv6 addresses are 128-bit, typically in hexadecimal. You'd configure IPv6 pools similarly using `::/64` notation for subnetting, using `ip/pool` command with a modified IP address scheme and then use it in DHCPv6 Server configuration.

### 7.2 IP Pools

*   **Concept:**  As mentioned, IP Pools are used to manage address allocation. They are not actual interfaces or routes, but instead act as a source for IPs used by other functions, such as DHCP server.
*   **Implementation:** MikroTik's implementation is robust, allowing you to specify multiple ranges within a pool and to chain pools, though this was not explored in depth.  They can also be allocated via a RADIUS server for PPP users.

### 7.3 IP Routing

*   **Concept:** IP Routing determines how packets are forwarded between networks.
*   **Implementation:** MikroTik supports static and dynamic routing (OSPF, RIP, BGP). While not directly involved with our specific IP pool configuration, the gateway specified within the DHCP config (`gateway=74.105.243.1`) acts as the first hop for the clients. You could add additional routes if you have upstream ISPs to utilize for routing.

### 7.4 IP Settings

*   **Concept:** This refers to global IP settings in RouterOS, such as connection tracking, IP DNS, etc.
*   **Implementation:** Connection tracking is essential for stateful firewall operation. MikroTik handles connection tracking tables efficiently. DNS, Proxy, and other IP services are all configured separately in `/ip`, e.g `/ip dns`, `/ip proxy`, etc.

### 7.5 MAC Server

*   **Concept:** The MAC server is an authentication mechanism that allows you to verify client connections via a MAC address. It's often used in wireless networks.
*   **Implementation:** It's managed under `/interface mac-server` and is a good solution for basic MAC access control.

### 7.6 RoMON

*   **Concept:** Router Management Overlay Network allows you to manage MikroTik devices across different networks using the RoMON protocol.
*   **Implementation:** Configured under `/tool romon` it is useful for managing multiple devices across an infrastructure.

### 7.7 WinBox

*   **Concept:** The primary GUI tool for configuring MikroTik devices on Windows and MacOS.
*   **Implementation:** While the CLI offers more power, WinBox provides an easy-to-use interface for configuration, monitoring, and troubleshooting.  This entire guide could be converted to use Winbox instead of CLI.

### 7.8 Certificates

*   **Concept:**  Used for secure communication in various services, e.g., HTTPS access to the router or VPN protocols like IPSec or WireGuard.
*   **Implementation:** You can generate and import certificates in `/certificate` allowing secure communication protocols.

### 7.9 PPP AAA

*   **Concept:** PPP (Point-to-Point Protocol) AAA is used for authentication, authorization, and accounting of PPP users, typically used in VPN connections.
*   **Implementation:** Managed under `/ppp profile` and uses RADIUS server configuration (covered below).

### 7.10 RADIUS

*   **Concept:**  Remote Authentication Dial-In User Service for centralizing user authentication, used for PPP, wireless, etc.
*   **Implementation:** Configuration under `/radius`. MikroTik supports various attributes for RADIUS, integrating smoothly with most RADIUS servers. In our context, RADIUS is not used in the core example, but is available for use in PPP configuration.

### 7.11 User / User Groups

*   **Concept:** RouterOS uses a user system, similar to Linux, for controlling access and permissions, and grouping user roles.
*   **Implementation:** Configured under `/user`. Group can have permissions assigned for access control.

### 7.12 Bridging and Switching

*   **Concept:** Bridges are Layer 2 devices used to forward packets based on MAC addresses, acting as a logical network segment. Switching refers to Layer 2 operations on specific physical ports.
*   **Implementation:** Our scenario uses `bridge-25`, demonstrating the bridging of multiple ports into a single Layer 2 domain. This configuration can also leverage VLANs.

### 7.13 MACVLAN

*   **Concept:** Allows the creation of virtual interfaces that are directly attached to a physical interface, using different MAC addresses.
*   **Implementation:** Configured under `/interface macvlan`. Often used for running multiple containers or virtual machines sharing one interface.

### 7.14 L3 Hardware Offloading

*   **Concept:** Leveraging the hardware switch chip for fast packet processing, reducing CPU load.
*   **Implementation:** Enabled or disabled on a per-interface basis or globally under `/interface bridge settings`. Only available on some MikroTik models which have switch chips.

### 7.15 MACsec

*   **Concept:** MAC Security protocol for point-to-point security on Ethernet links.
*   **Implementation:** Configured under `/interface macsec` on compatible devices. A more advanced Layer 2 security protocol.

### 7.16 Quality of Service (QoS)

*   **Concept:** Prioritizing or shaping traffic, ensuring important traffic receives the resources needed.
*   **Implementation:** Implemented with queues, queue trees, and firewall mangle rules under `/queue` and `/ip firewall mangle`.

### 7.17 Switch Chip Features

*   **Concept:** Advanced configuration capabilities available on the built-in switch chip, found in some MikroTik models.
*   **Implementation:** Access via `/interface ethernet switch`. These allow you to configure things such as VLANs at the switch level.

### 7.18 VLAN

*   **Concept:** Virtual LANs, used to logically separate networks on the same physical infrastructure, or isolate different traffic types.
*   **Implementation:** Configured on interfaces, bridges and switches using `/interface vlan` and various switch chip controls.

### 7.19 VXLAN

*   **Concept:** Virtual Extensible LAN, allows Layer 2 extension over IP networks.
*   **Implementation:** Configured under `/interface vxlan`. Useful for bridging Layer 2 networks over a Layer 3 infrastructure.

### 7.20 Firewall and Quality of Service

* **Concept:** MikroTik firewall is stateful and can filter, NAT, mangle, and do connection tracking. It's core to MikroTik's security model. QoS is used to control traffic prioritization and ensure optimal throughput.
* **Implementation:** `/ip firewall` and `/queue`. This module covers all facets of the firewall, ranging from basic traffic filtering to complex NAT configurations and shaping traffic using queues. This includes use of connection tracking to determine the state of connections through the router, using mangle for packet marking, and implementing shaping rules to ensure some services receive priority.
    * **Firewall:** Uses `filter` chains, NAT rules for address translation and `mangle` rules for packet modification. Firewall chains cover `input`, `forward` and `output` chains.
    * **Connection tracking:**  The Router will attempt to keep track of connection state. It is used in NAT and firewall rule configuration to determine state, such as `established` or `related`.
    * **Packet Flow:** Packets flow into the router via an interface, are processed by the input chain rules, routed by the router, processed by the forward chain rules, and exit via an interface after being processed by output chain rules.
    * **Queues:** QoS is implemented with queues, parent queue, and queue trees. These ensure certain packets receive prioritization or have a limit imposed.
    * **Case Studies:** QoS examples, such as prioritising VoIP over HTTP or gaming traffic to ensure the quality of service.
    * **Kid Control:** You can implement time based firewall rules for parental controls using the `time` based matchers in the firewall, for example, `time=17:00:00-22:00:00,sat,sun`
    * **UPnP / NAT-PMP:** Universal Plug and Play and NAT Port Mapping Protocol can automatically open ports if a client device requests it. This can be helpful in devices such as game consoles, however it can have a security impact, and it is recommended to carefully consider the risks.

### 7.21 IP Services

* **Concept:** MikroTik offers various network services.
* **Implementation:**
    * **DHCP**: Provides IP addresses and other config to hosts as we described above.
    * **DNS**: DNS is used for resolving domains, and can be configured to use local and remote nameservers. You can also add static mappings in the DNS cache, or specify a local DNS server that uses the router as the server.
    * **SOCKS**: A SOCKS proxy is a proxy server which can be used to route traffic, especially when using a VPN.
    * **Proxy**: A web proxy can be configured on MikroTik, including transparent proxy configurations.

### 7.22 High Availability Solutions

* **Concept:** Mechanisms for ensuring network uptime and fault tolerance.
* **Implementation:**
    * **Load Balancing:** Uses multiple links to handle traffic distribution across links.
    * **Bonding:**  Combines multiple interfaces into one logical interface, providing link aggregation, failover or load balancing.
    * **HA Case Studies:**  Examples on how to combine these solutions to improve availability.
    * **Multi-chassis Link Aggregation Group:** Not commonly used for consumer or small business setups, but useful in datacentres.
    * **VRRP:** Virtual Router Redundancy Protocol is used for setting up a master-backup router setup for failover.

### 7.23 Mobile Networking

* **Concept:** Connecting to mobile networks for internet access.
* **Implementation:**
    * **GPS:** Used for location services with GPS equipped MikroTik devices.
    * **LTE:** Connect to cellular networks via LTE.
    * **PPP:**  Used for dial-up connections, including modems.
    * **SMS:** Send and receive SMS messages via cellular modem.
    * **Dual SIM Application:** Use two SIM cards for redundancy.

### 7.24 Multi Protocol Label Switching (MPLS)

* **Concept:** An advanced routing technology used mainly in larger ISP networks for traffic engineering and routing.
* **Implementation:** MPLS functionality is configured under `/mpls`.
     * **Overview:** Provides an overview of how MPLS works with concepts such as labels and label distribution protocols (LDP).
     * **MTU:** MPLS can affect MTU due to additional headers, which need to be considered.
     * **Forwarding and Bindings:** Describes how to configure Label Forwarding Tables and Bindings.
     * **EXP Bit and Queuing:** Used for prioritising MPLS traffic.
     * **LDP:** Label Distribution Protocol is a key component of MPLS, used to share label information between devices.
     * **VPLS:** Virtual Private LAN service, which can create a virtual LAN across multiple locations.
     * **Traffic Engineering:** Ways to shape and route traffic via MPLS.

### 7.25 Network Management

* **Concept:** Tools for managing the network, ranging from protocols to troubleshooting tools.
* **Implementation:**
    *   **ARP:** Address Resolution Protocol used to map IP addresses to MAC addresses.
    *   **Cloud:** MikroTik cloud functionality for remotely managing devices via a central interface.
    *   **DHCP:** Covered previously.
    *   **DNS:** Covered previously.
    *   **SOCKS:** Covered previously.
    *   **Proxy:** Covered previously.
    *   **Openflow:** Used for software defined networking (SDN).

### 7.26 Routing

* **Concept:** Methods for routing packets throughout the network.
* **Implementation:**
    * **Routing Protocol Overview:** Explains the different types of routing, including static and dynamic routing protocols.
    * **Moving from ROSv6 to v7:** Details the changes required when moving between these major versions.
    * **Routing Protocol Multi-core Support:** Details how newer versions can use multi-core CPUs for improved throughput.
    * **Policy Routing:** How to control routing decisions based on various criteria.
    * **Virtual Routing and Forwarding (VRF):** Used to create isolated routing tables.
    * **OSPF:** Open Shortest Path First dynamic routing protocol.
    * **RIP:** Routing Information Protocol dynamic routing protocol.
    * **BGP:** Border Gateway Protocol dynamic routing protocol used for managing large internet routing.
    * **RPKI:** Resource Public Key Infrastructure is a method for validating routes against routing policies and stopping route hijacking.
    * **Route Selection and Filters:** Methods used to control which routes are used, or how routes are filtered.
    * **Multicast:** Used to send traffic to multiple destinations in a group, using a single transmission.
    * **Debugging Tools:** Command line tools to help diagnose routing issues.
    * **BFD:** Bidirectional Forwarding Detection is used to detect link status changes.
    * **IS-IS:** Intermediate System to Intermediate System dynamic routing protocol.

### 7.27 System Information and Utilities

* **Concept:**  Tools to manage the router itself.
* **Implementation:**
    *   **Clock:**  Sets the system time using an NTP server.
    *   **Device-Mode:** Sets the device-mode to `router` or `switch` mode.
    *   **E-mail:** Allows the sending of emails for logging, alerts, and testing.
    *   **Fetch:** Fetch used to download files from external servers, typically for software updates.
    *   **Files:** Managing system files on the device.
    *   **Identity:** Sets the router's hostname.
    *   **Interface Lists:** Ability to group interfaces together in a logical list.
    *   **Neighbor discovery:** Uses protocols such as CDP or LLDP for neighbour discovery.
    *   **Note:** Add notes to router configs.
    *   **NTP:** Network Time Protocol for syncing time.
    *   **Partitions:** Manage partitions on devices with local storage.
    *   **Precision Time Protocol:** Alternative method for syncing time, often more accurate than NTP.
    *   **Scheduler:** Schedule tasks, using cron-like syntax.
    *   **Services:** Controls which services are enabled, such as the web interface, or SSH.
    *   **TFTP:** Trivial File Transfer Protocol for basic file transfer.

### 7.28 Virtual Private Networks (VPNs)

* **Concept:** Technologies for establishing secure private networks over public networks.
* **Implementation:**
    *   **6to4:** IPv6 tunnelling mechanism over IPv4.
    *   **EoIP:** Ethernet over IP tunnelling protocol used to extend layer 2 networks over layer 3.
    *   **GRE:** Generic Routing Encapsulation, simple tunneling protocol.
    *   **IPIP:** IP in IP tunnelling, tunnelling an IP packet within another IP packet.
    *   **IPsec:**  IP security protocol used for end-to-end encryption.
    *   **L2TP:** Layer 2 Tunneling Protocol, typically used with IPSec.
    *   **OpenVPN:** Open source VPN solution.
    *   **PPPoE:** Point-to-Point Protocol over Ethernet, typically used by ISPs.
    *   **PPTP:** Point-to-Point Tunneling Protocol, an older and less secure VPN.
    *   **SSTP:** Secure Socket Tunneling Protocol, often used on Windows systems.
    *   **WireGuard:** A more modern and efficient VPN solution.
    *   **ZeroTier:** A software defined networking solution that provides similar VPN functionality as a full VPN implementation.

### 7.29 Wired Connections

* **Concept:** Configuration of physical Ethernet ports.
* **Implementation:**
    *   **Ethernet:** Configuration for ethernet ports.
    *   **Compatibility:** Specific compatibilities with different types of wired connections.
    *   **Power Line:** Uses existing power lines for networking.

### 7.30 Wireless

* **Concept:** Configures WiFi connections.
* **Implementation:**
    *   **WiFi:** Standard 802.
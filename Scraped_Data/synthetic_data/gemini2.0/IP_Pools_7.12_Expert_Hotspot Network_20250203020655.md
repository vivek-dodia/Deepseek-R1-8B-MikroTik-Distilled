Okay, let's dive deep into configuring IP Pools on a MikroTik router, specifically within the context of a hotspot network, and then expand to cover all the requested topics. This will be a comprehensive guide.

**1. Comprehensive Configuration Scenario and MikroTik Requirements**

*   **Scenario:** We're setting up a hotspot network in a small business environment (e.g., a cafe or small office).  We need to assign IP addresses to connecting clients dynamically from the 136.176.205.0/24 subnet. This network will primarily use the `ether-97` interface for client connectivity, and will require DHCP service for assigning addresses, DNS, and Gateway information.
*   **MikroTik Requirements:**
    *   RouterOS version: 7.12 (or other 7.x)
    *   Interface: `ether-97` for client connections.
    *   Subnet: 136.176.205.0/24
    *   IP Pool to allocate addresses from this subnet
    *   DHCP Server to automatically provide IP addresses to connecting clients, with the configured address pool
    *   Basic Firewall settings for connectivity, NAT, and security

**2. Step-by-Step MikroTik Implementation**

**2.1. Using CLI (Terminal)**

   *   **Step 1: Create the IP Pool**
        ```mikrotik
        /ip pool add name=hotspot-pool ranges=136.176.205.100-136.176.205.254
        ```
        **Explanation:**
        *   `/ip pool add`: Creates a new IP address pool.
        *   `name=hotspot-pool`: Assigns the name "hotspot-pool" to the pool. This is a logical name to reference in later configurations.
        *   `ranges=136.176.205.100-136.176.205.254`: Specifies the range of IP addresses this pool will manage. We start at .100 and go to .254, reserving some IPs below and above for static or other assignments.
     
    *   **Step 2: Configure the IP address on the interface**
        ```mikrotik
        /ip address add address=136.176.205.1/24 interface=ether-97
        ```
        **Explanation:**
        *   `/ip address add`: Adds a new IP address to an interface.
        *   `address=136.176.205.1/24`: Sets the IP address for the interface to `136.176.205.1` with a subnet mask of `/24`.
        *   `interface=ether-97`: Specifies that this IP address is assigned to the `ether-97` interface.
    *   **Step 3: Create a DHCP Server**
        ```mikrotik
        /ip dhcp-server add address-pool=hotspot-pool interface=ether-97 name=hotspot-dhcp-server
        ```
        **Explanation:**
        *   `/ip dhcp-server add`: Creates a new DHCP Server.
        *   `address-pool=hotspot-pool`: Uses the previously defined IP Pool to provide leases to connected clients
        *   `interface=ether-97`: Specifies that the server should operate on `ether-97`.
        *   `name=hotspot-dhcp-server`: Names the DHCP server for reference later.
   *  **Step 4: Configure the DHCP Network for the Server**
         ```mikrotik
        /ip dhcp-server network add address=136.176.205.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=136.176.205.1
        ```
       **Explanation:**
       * `/ip dhcp-server network add`: Adds a new network configuration to the DHCP server.
       * `address=136.176.205.0/24`: Specifies the network for the leases.
       * `dns-server=8.8.8.8,8.8.4.4`: Sets the DNS server to be passed out to clients.
       * `gateway=136.176.205.1`: Sets the gateway address for clients on the network.

    *   **Step 5:  Basic NAT Masquerade**
         ```mikrotik
        /ip firewall nat add chain=srcnat action=masquerade out-interface=WAN
        ```
       **Explanation:**
       * `/ip firewall nat add`: Adds a new NAT rule.
       * `chain=srcnat`:  Applies to the source network address translation (NAT) chain.
       * `action=masquerade`: Allows clients to use the routers IP address for outbound traffic
       * `out-interface=WAN`: Specifies the interface connected to the internet (replace `WAN` with your actual WAN interface name - e.g. ether-1).

**2.2. Using Winbox**

    *   **Step 1: Create the IP Pool**
        *   Connect to your MikroTik router using Winbox.
        *   Go to `IP` -> `Pool`.
        *   Click the "+" button.
        *   In the `Name` field, enter `hotspot-pool`.
        *   In the `Ranges` field, enter `136.176.205.100-136.176.205.254`.
        *   Click `OK`.
    *   **Step 2: Configure the IP Address**
       * Go to `IP` -> `Addresses`.
       * Click the "+" button.
       * In the `Address` field, enter `136.176.205.1/24`.
       * In the `Interface` dropdown, select `ether-97`.
       * Click `OK`.
    *   **Step 3: Create the DHCP Server**
        *   Go to `IP` -> `DHCP Server`.
        *   Click the "+" button.
        *   In the `Name` field, enter `hotspot-dhcp-server`.
        *   In the `Interface` dropdown, select `ether-97`.
        *   In the `Address Pool` dropdown, select `hotspot-pool`.
        *   Click `OK`.
    *  **Step 4: Create the DHCP Server Network**
       * Go to `IP` -> `DHCP Server`.
       * Click the `Networks` button.
       * Click the "+" button.
       * In the `Address` field, enter `136.176.205.0/24`.
       * In the `Gateway` field, enter `136.176.205.1`.
       * In the `DNS Servers` field, enter `8.8.8.8,8.8.4.4`.
       * Click `OK`.
     *   **Step 5: NAT Masquerade**
         * Go to `IP` -> `Firewall`.
         * Click the `NAT` tab.
         * Click the "+" button.
         * In the `Chain` dropdown, select `srcnat`.
         * Under the `General` tab, click the `Out Interface` dropdown, and select your WAN interface.
         * Under the `Action` tab, select `Masquerade`
         * Click `OK`.

**3. Complete MikroTik CLI Configuration Commands**

```mikrotik
/ip pool
add name=hotspot-pool ranges=136.176.205.100-136.176.205.254
/ip address
add address=136.176.205.1/24 interface=ether-97
/ip dhcp-server
add address-pool=hotspot-pool interface=ether-97 name=hotspot-dhcp-server
/ip dhcp-server network
add address=136.176.205.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=136.176.205.1
/ip firewall nat
add chain=srcnat action=masquerade out-interface=WAN
```
**4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics**

*   **Pitfall:** Incorrect IP Pool Range.
    *   **Error:** Clients can't get an IP address.
    *   **Troubleshooting:** Use `/ip pool print` to verify your pool range is correct and not overlapping with other assigned IPs. Check that it fits within the specified subnet range.
*   **Pitfall:** DHCP Server not enabled or on the wrong interface.
    *   **Error:** Clients receive no IP address.
    *   **Troubleshooting:** Use `/ip dhcp-server print` to verify the server is enabled and bound to the correct interface (`ether-97`). Check that the `disabled` parameter is set to `no`.
*   **Pitfall:** DHCP network has an incorrect gateway address, or missing DNS server.
    *  **Error:** Clients receive an IP, but cannot reach the Internet or DNS services.
    *  **Troubleshooting:** Use `/ip dhcp-server network print` to verify the configured gateway and DNS servers are correct.
*   **Pitfall:** Firewall rules preventing DHCP traffic.
    *   **Error:** Clients cannot get IP or connect to network.
    *   **Troubleshooting:** Temporarily disable firewall rules (using `/ip firewall filter disable numbers=[rule numbers]`) to check if the DHCP issue is related. In particular, check if the forward or input chains are not allowing `udp` port 67 and 68 to pass.
*   **Pitfall:** Client-side network issues.
    *   **Error:**  Client cannot connect, even with correct MikroTik settings.
    *   **Troubleshooting:** Check client wifi/ethernet card and adapter are correctly configured, and any local firewalls are not interfering.

**Diagnostics:**

*   **`ping`:** Use `/ping 136.176.205.1` from the RouterOS terminal to check connectivity to the gateway IP on `ether-97`.
*   **`torch`:** Use `/tool torch interface=ether-97` to monitor DHCP traffic (UDP port 67 and 68) in real time.  This will let you see if clients are sending out requests.
*   **`log`:** Use `/log print` to check for DHCP server or firewall-related errors.  Look for warnings related to address pool exhaustion or DHCP server errors.
*   **`/ip dhcp-server lease print`:** Check the active DHCP leases. This shows you what address is currently leased to connected clients

**5. Verification and Testing Steps**

1.  **Connect a client to `ether-97`:** Connect a device (laptop, phone) to the network connected to the `ether-97` interface.
2.  **Check IP Address:** Verify that the client received an IP address from the range 136.176.205.100 - 136.176.205.254. The client gateway should be 136.176.205.1. You can check from the clients OS configuration screens for network configuration.
3.  **Test Internet Connectivity:** Ensure that the client can access websites and other internet resources.  Verify the client can reach `8.8.8.8` using `ping` or other similar means.
4.  **Monitor RouterOS:** Use the tools mentioned earlier (e.g., `/tool torch`, `/log print`) to ensure proper operation, particularly if issues are encountered.

**6. Related MikroTik-Specific Features, Capabilities, and Limitations**

*   **Multiple IP Pools:** You can create multiple IP pools for different interfaces or purposes (e.g., guest network, employee network).
*   **Static Leases:** You can assign static IP addresses to specific clients based on their MAC address using `/ip dhcp-server lease add` for specific devices. This overrides DHCP assignment based on configured IP pools.
*   **Lease Time:** The DHCP lease time can be configured using `/ip dhcp-server set lease-time=[time]`. This controls how long a client can keep its assigned IP address before needing to request a new one. A long lease-time for static equipment, a short lease time for a high churn network, such as an open guest Wifi network.
*   **DHCP Options:** You can configure additional DHCP options (e.g., custom DNS suffixes, NTP servers) using `/ip dhcp-server network add dhcp-option=[option]`.
*   **Limitations:**
    *   MikroTik's DHCP server is not as feature-rich as some enterprise-grade dedicated DHCP servers.
    *   Large networks might require a different approach, like using a dedicated DHCP server or central management system.
   * **Lease Conflict:**  If the IP assigned statically is within the DHCP assigned ranges, lease conflicts can arise. You will need to ensure that static IP assignment is outside of the specified IP pool ranges.

**7. MikroTik REST API Examples**

*   **Enable the API:** First, enable the MikroTik API. You can do this in Winbox under `IP` -> `Services`. The `api` service should be enabled (and ideally `api-ssl`).  For the commands below, the IP address is `192.168.88.1`, and login details (username, password) are required.

*   **Example 1: Get IP Pool Information**

    *   **API Endpoint:** `https://192.168.88.1/rest/ip/pool` (adjust the IP as necessary).
    *   **Request Method:** `GET`
    *   **Example cURL Command:**
    ```bash
    curl -k -u <username>:<password> https://192.168.88.1/rest/ip/pool
    ```
     * **Expected Response (JSON):**
        ```json
          [
            {
              ".id": "*1",
              "name": "hotspot-pool",
              "ranges": "136.176.205.100-136.176.205.254",
              "next-pool": "none"
            }
        ]
        ```

*  **Example 2: Create IP Pool via API**

    * **API Endpoint:** `https://192.168.88.1/rest/ip/pool`
    * **Request Method:** `POST`
    *   **JSON Payload:**
        ```json
         {
          "name":"api-pool",
          "ranges":"136.176.205.50-136.176.205.60"
         }
        ```
     *   **Example cURL Command:**
        ```bash
           curl -k -u <username>:<password> -H "Content-Type: application/json" -X POST -d '{ "name":"api-pool", "ranges":"136.176.205.50-136.176.205.60" }' https://192.168.88.1/rest/ip/pool
         ```
    *   **Expected Response (JSON):**
          ```json
          {
               "message": "added"
            }
           ```

*  **Example 3: Delete an IP Pool via API**
    * **API Endpoint:** `https://192.168.88.1/rest/ip/pool/<.id>` (Replace `<.id>` with the `id` from the get command).
    * **Request Method:** `DELETE`
    *   **Example cURL Command:**
        ```bash
        curl -k -u <username>:<password> -X DELETE https://192.168.88.1/rest/ip/pool/\*1
         ```
     *   **Expected Response (JSON):**
           ```json
           {
              "message":"removed"
           }
           ```

**8. In-Depth Explanations of Core Concepts**

*   **IP Addressing (IPv4):**
    *   In this configuration, we use IPv4 addressing.  An IPv4 address is a 32-bit number, which we often represent using the dotted decimal notation (e.g., 136.176.205.1).
    *   A `/24` subnet mask means that the first 24 bits are used for the network address, and the last 8 are used for host addresses. This creates 254 usable IPs, with 2 reserved (network and broadcast addresses), all within the same broadcast domain. This is the common Class C network.
*   **IP Pools:**
    *   An IP Pool is simply a defined range of IP addresses.  The router uses this to manage leases to its clients using the DHCP server.  By allocating a range (rather than a static IP), the router can dynamically assign IPs to devices as needed.
*   **IP Routing:**
    *   Our basic configuration is very simple. All hosts exist on a single network, the subnet `136.176.205.0/24`, and thus do not require any special routing settings.  For internet connectivity, the default gateway for all hosts will be the routers IP address (`136.176.205.1`).
    *  MikroTik uses a route table (you can see with `/ip route print`) to track where traffic should be forwarded, based on the destination IP addresses.
*   **IP Settings:**
    *   IP settings control the basic IP configurations of a device or interface, such as IP addresses and interface binding.
*   **DHCP:**
    *   DHCP (Dynamic Host Configuration Protocol) is used by hosts to get their IP addresses, gateway addresses, DNS server addresses, and other network settings. The MikroTik DHCP server provides this service. The client requests an IP, and the server provides a lease from an address pool.
*   **NAT (Network Address Translation):**
    *   NAT, specifically Masquerade here, translates the private IPs of our internal network (136.176.205.0/24) to a single public IP address, and allows us to have many clients reach the Internet using a single routable IP address.
*   **Bridging and Switching:**
    *   A Bridge is a mechanism to treat multiple interfaces as a single network. This is done in MikroTik on the OSI Layer 2 (Data Link Layer). Our configuration is not using bridging, as we want to use `ether-97` as its own network interface.
*   **Firewall:**
    * The firewall in MikroTik uses a stateful firewall, and allows the administrator to control what traffic can traverse the router. The `srcnat` rule in the nat chain provides outbound internet access. We have not set up explicit firewall filter rules (we have only set up NAT rules), so all traffic between hosts in this subnet are allowed.  Without an explicit firewall rule to disallow traffic, inter-network host to host traffic is allowed.

**9. Security Best Practices**

*   **Secure your API access:** Use `api-ssl` to enable encrypted access to the API. Set a strong password for all router users. Only allow access to the API from known IPs in the firewall.
*   **Firewall Rules:** Restrict access to management interfaces (e.g., Winbox, WebFig) from specific IP addresses, and use a strong password.
*   **Keep RouterOS Up-to-Date:**  Install updates to protect against security vulnerabilities.
*   **Disable Unnecessary Services:** Disable any services that are not required (e.g., FTP, Telnet).
*   **Change Default Credentials:** Do not use the default `admin` user. Use a more complex password and user account.
*   **Secure Wireless:** If using a wireless interface (CAPsMAN, etc), use WPA3 for the highest level of security.
*  **Avoid open networks**: Do not use open guest network with no password protection, or basic WEP. Open wireless networks invite abuse.
*   **Regular Backups:** Perform regular backups of your configuration to protect against configuration loss or other issues.

**10. Detailed Explanations and Configuration Examples**

Now let's dive into the full detailed explanations and examples for each of the requested MikroTik topics:

---
### 10.1 IP Addressing (IPv4 and IPv6)
* **IPv4:** As covered, the 32-bit addresses are represented as dotted decimal notation (e.g. 192.168.0.1). Each address consists of a network portion and a host portion, dictated by the subnet mask. We covered this in the main example.
* **IPv6:** Addresses are 128-bit addresses. Typically written in hexadecimal notation, separated by colons (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334), they greatly increase the IP address pool. Here's an example of assigning an IPv6 address:

    ```mikrotik
    /ipv6 address add address=2001:db8::1/64 interface=ether-97
    ```

   * **Dual Stack:** MikroTik supports dual-stack IPv4/IPv6. An interface can have an IPv4 and an IPv6 address assigned. You can configure DHCPv6 to assign addresses to hosts.
* **Configuration:**
    * **CLI:** `/ip address add` (IPv4), `/ipv6 address add` (IPv6)
    * **Winbox:** IP -> Addresses

### 10.2 IP Pools
*   **Concept:** IP pools are ranges of IP addresses to dynamically allocate.
*   **Configuration:**
   *  **CLI:** `/ip pool add` to create, `/ip pool print` to view.
   *  **Winbox:** IP -> Pool
    * **Example with exclusion ranges:**
         ```mikrotik
           /ip pool add name=extended-pool ranges=136.176.205.10-136.176.205.250,136.176.205.150-136.176.205.160
        ```
        This pool uses the range 10-250, excluding 150-160.

### 10.3 IP Routing
* **Concept:** Routing determines the path packets take to reach their destination.
* **Static Routing:** Manually configured routes.
    ```mikrotik
    /ip route add dst-address=10.0.0.0/24 gateway=192.168.10.1
    ```
* **Dynamic Routing Protocols:** OSPF, RIP, and BGP.  See later sections for more detail
* **Policy Routing:** Direct traffic based on source, protocols, or other parameters.

### 10.4 IP Settings
* **Concept:**  Global IP related settings.
* **Configuration:**
    * **CLI:** `/ip settings`
    * **Winbox:** IP -> Settings
    * **Options:**
         * `allow-fast-path`:  (Enabled by default) allows router to perform faster forwarding of packets using hardware.
         * `tcp-syncookies`: Allows the use of SYN cookies to prevent syn flood attacks.
* **Example:**
        ```mikrotik
           /ip settings set allow-fast-path=yes tcp-syncookies=yes
        ```

### 10.5 MAC Server
* **Concept:**  Used to allow communication between devices on the same network even if they do not have an IP Address. Often used with Winbox and other network tools.
* **Configuration:**
    * **CLI:** `/tool mac-server print`, `/tool mac-server set enabled=yes`, `/tool mac-server mac-winbox set allowed-interface=<interface>`
    * **Winbox:** Tools -> MAC Server
    * **Options:**
        * `enabled`: Enables or disables the MAC server globally.
        * `allowed-interface`: Restricts access to certain interfaces for improved security.

### 10.6 RoMON
* **Concept:** MikroTik's proprietary remote management tool that operates at layer 2. It allows discovery of other MikroTik devices in the same broadcast domain, and can be used for configuration.
* **Configuration:**
   *  **CLI:**  `/tool romon`, `/tool romon set enabled=yes`, `/tool romon set id=<romon id>`
    * **Winbox:** Tools -> RoMON
    * **Options:**
        * `enabled`: Turn RoMON on and off
        * `id`: Sets the ID for ROMON discovery. If you have multiple domains, you can separate them with different IDs.
* **Note:** Should be used only in a secured environment. RoMON is an insecure Layer 2 service

### 10.7 WinBox
* **Concept:** MikroTik's graphical configuration tool.
* **Usage:** The main tool for most configuration and monitoring purposes.  All steps have corresponding WinBox examples given in section 2.2.

### 10.8 Certificates
* **Concept:**  Digital certificates for secure connections.
* **Configuration:**
   *  **CLI:** `/certificate`, including importing, exporting, generating certificates
    * **Winbox:** System -> Certificates
    * **Options:**
        * `import`: Imports an existing certificate.
        * `generate-self-signed`: Creates a self-signed certificate.
        * `sign`: Used to sign a certificate request.
* **Use cases:**
    * Used for secure web access, secure API, VPNs, and more.

### 10.9 PPP AAA
* **Concept:** Used to provide authentication, authorization and accounting services for PPP based connections such as PPPoE, L2TP, and PPTP connections.
*   **Configuration:**
    * **CLI:** `/ppp aaa`
    * **Winbox:** PPP -> AAA
    * **Options:**
        *  `use-radius`: Enables the use of RADIUS for authentication.
        *  `accounting`: Enables accounting information for PPP connections.

### 10.10 RADIUS
* **Concept:** Centralized authentication, authorization, and accounting (AAA) server for network access control.
* **Configuration:**
    * **CLI:** `/radius`, `/radius add`, `/radius print`
    * **Winbox:** RADIUS in PPP or User Manager settings.
    * **Options:**
        *  `address`: Specifies the RADIUS server IP.
        *  `secret`: A secret for communication with the RADIUS server.
        *  `port`: The UDP port used by RADIUS server
* **Use cases:**
    * For Hotspots, and other connections requiring external authentication.

### 10.11 User / User groups
* **Concept:** Manage users and groups to provide access to the router or services.
* **Configuration:**
   * **CLI:** `/user`, `/user group`
   * **Winbox:** System -> Users, System -> User Groups
    * **Options:**
        *   `username`, `password`: Used for login credentials.
        *  `group`: Assigns a user to a group which then can be used for setting permissions.
        *  `permissions`: Assigns particular rights to users.
* **Use Cases:**
    * For providing secure and restricted access to the router.

### 10.12 Bridging and Switching
* **Concept:** Bridges combine network interfaces at OSI layer 2. Switching occurs within a bridge.
*   **Configuration:**
    * **CLI:** `/interface bridge`, `/interface bridge port`
    * **Winbox:** Bridge menu under Interface
    * **Options:**
        *   `add`: create a new bridge interface
        * `port`: Add interfaces to a bridge to behave as a single broadcast domain.
* **Use cases:**
    * To connect LAN ports as a single broadcast domain, or transparently pass network traffic.

### 10.13 MACVLAN
* **Concept:** Allows you to create virtual network interfaces on a single physical interface using virtual MAC addresses. Can be used with containers.
*   **Configuration:**
    * **CLI:** `/interface macvlan add`
    * **Winbox:** Not directly through Winbox.
    * **Options:**
       *  `master-interface`: The underlying physical interface to which the MACVLAN interface is tied.
       *  `mac-address`: You can configure a specific MAC address, or the router will generate one for you.
*  **Use Cases:**
    *   Ideal for containers and virtualization.

### 10.14 L3 Hardware Offloading
* **Concept:**  Allows hardware chips to do some of the work of the CPU to increase forwarding performance, and reduce load.
* **Configuration:**
    *  **CLI:** `/interface ethernet set <interface> l3-hw-offload=yes`
    *  **Winbox:** Interface -> Properties -> L3 HW Offload. This is enabled per interface.
*  **Use Cases:**
     *  When working with high bandwidth networks.
*  **Note:** Not all hardware or interfaces support this feature.

### 10.15 MACsec
* **Concept:** Security at the data link layer (layer 2). Provides encryption for each packet.
*   **Configuration:**
    * **CLI:** `/interface macsec`
    * **Winbox:** Requires CLI. No Winbox configuration.
    * **Options:**
       *  `master-interface`: The underlying ethernet interface to be encrypted.
       * `tx-key`, `rx-key`: Keys for the macsec encryption.
*  **Use Cases:**
    * Providing extra security in vulnerable, layer 2 areas.

### 10.16 Quality of Service (QoS)
* **Concept:** Prioritizes specific traffic to improve network performance for important applications.
* **Configuration:**
   *  **CLI:** `/queue tree`, `/queue simple`, `/ip firewall mangle`
   *  **Winbox:** Queues.

*   **Simple Queues:** Limit traffic rate for a specific IP address or interface.

    ```mikrotik
     /queue simple add target=192.168.0.100/32 max-limit=1M/2M
    ```
    This limits the IP 192.168.0.100 to 1M download and 2M upload.
*   **Queue Trees:** More advanced, Hierarchical queuing, with traffic classification.

### 10.17 Switch Chip Features
* **Concept:** Modern MikroTik devices have dedicated switch chips that handle switching functions directly in hardware.
*   **Configuration:**
    * **CLI:** `/interface ethernet switch`
    * **Winbox:** No direct access in Winbox - must be CLI based.
    * **Features:**
        *  VLAN tagging
        *  Port mirroring
        *  Link aggregation
        *  Speed and duplex control.

### 10.18 VLAN
* **Concept:**  Virtual LANs allow you to create multiple isolated logical networks on the same physical network.
*   **Configuration:**
    * **CLI:** `/interface vlan add`
    * **Winbox:** Interfaces -> Add new -> VLAN
    * **Options:**
       * `vlan-id`: Tag IDs for the VLANs (1-4094)
       *  `interface`: Physical interface the VLAN is tied to.
* **Example:**
        ```mikrotik
           /interface vlan add name=vlan10 vlan-id=10 interface=ether-97
        ```
* **Use Cases:**
    *   Separating guest and main network traffic.

### 10.19 VXLAN
* **Concept:**  VXLAN is used to create an extended layer 2 network over an IP network.
*   **Configuration:**
    * **CLI:** `/interface vxlan add`
    * **Winbox:** Not directly accessible in Winbox
    * **Options:**
       * `vni`: The VXLAN network identifier.
       * `interface`: The interface the VXLAN operates on.
       *  `remote-address`: The remote endpoint for the tunnel
*  **Use Cases:**
    *   Extending L2 networks across L3 boundaries

### 10.20 Firewall and Quality of Service
*  **Connection tracking:** MikroTik firewall keeps track of the connection status, and makes sure return traffic to your network is allowed based on existing connections.
*  **Firewall:** As seen with NAT and the `masquerade` action. Can be used to restrict inter-network traffic, and is usually used to stop unsolicited incoming traffic.

    ```mikrotik
       /ip firewall filter add chain=input protocol=tcp dst-port=22 action=drop
    ```
    This disallows ssh access to the router.

* **Packet Flow in RouterOS:** Follows a strict sequence of processing.
    1. Input Chain - Traffic that is destined for the router itself.
    2. Forward Chain - Traffic passing through the router.
    3. Output Chain - Traffic originating from the router.
    4. Pre-routing and post-routing - Special chains for NAT processing.
*  **Queues:** Used for bandwidth control as seen earlier (QoS).
* **Firewall and QoS Case Studies:**
    *  **Prioritizing VoIP Traffic:** Use mangle rules to mark traffic for QoS purposes, then create queues.
*  **Kid Control:** Use the firewall filter rules to block access to websites and services based on time and/or content.
*  **UPnP/NAT-PMP:** Provides applications a method of opening firewall ports. Should be carefully managed, or completely disabled. This feature can provide an attack vector if not handled correctly.

### 10.21 IP Services (DHCP, DNS, SOCKS, Proxy)
* **DHCP:** Covered in the main example.
* **DNS:**
    * **Server:** The MikroTik router can act as a DNS server or forward DNS requests.

      ```mikrotik
      /ip dns set allow-remote-requests=yes servers=8.8.8.8,1.1.1.1
     ```
    *  **Client:** Used to resolve DNS names for the router itself.
* **SOCKS:** SOCKS proxy for outbound access.
* **Proxy:** HTTP proxy for web traffic.

### 10.22 High Availability Solutions
*   **Load Balancing:** Distribute traffic across multiple links or servers.
    *  **ECMP:** Equal Cost Multi-Path.
    *  **NTH:** Distributes traffic based on hashing.
*  **Bonding:** Link multiple physical interfaces to create a single logical high bandwidth interface.
    * **Modes:**
       *  `balance-rr`: Round-robin load balancing
       *  `balance-xor`: Hash based load balancing.
       * `active-backup`: Active interface with backup if it fails.
* **HA Case Studies:**
    * **Redundant Internet Links:** Multiple internet links for backup purposes.
*  **Multi-chassis Link Aggregation Group (MLAG):** A more advanced, hardware based way of linking multiple routers together for high availability.
* **VRRP:** Virtual Router Redundancy Protocol provides a way to have virtual routers that fail over should the primary fail.
    *  Requires two or more routers.
    *  Master Router has a virtual IP address, which is taken over by the backup router in the event of failure.
* **VRRP Configuration Examples:**
        ```mikrotik
            /interface vrrp add interface=ether-97 vrid=1 priority=200 address=136.176.205.2/24 v3=yes
            /interface vrrp add interface=
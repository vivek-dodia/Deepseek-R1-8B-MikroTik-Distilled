Okay, let's dive deep into this comprehensive MikroTik RouterOS configuration scenario, focusing on IP Pools within the context of an ISP-level network and covering all the required aspects.

# MikroTik RouterOS Configuration: IP Pools (ISP-Scale)

This document outlines the configuration of IP Pools on a MikroTik router running RouterOS 7.12 within an ISP-scale network. The focus is on a /24 subnet (22.240.123.0/24) assigned to the interface "ether-90". We'll cover all the requested topics, from basic to advanced, with practical examples.

## 1. Comprehensive Configuration Scenario and Specific MikroTik Requirements

**Scenario:**

An ISP requires an IP pool to be created from the subnet `22.240.123.0/24` for DHCP assignment to customer devices connecting through the interface `ether-90`. We'll configure the IP pool, associated DHCP server, and basic routing necessary for this functionality. We'll also delve into more complex aspects such as firewall rules, quality of service, and advanced features.

**Specific MikroTik Requirements:**

*   RouterOS: 7.12 (or later versions in the 7.x branch)
*   Subnet: `22.240.123.0/24`
*   Interface: `ether-90`
*   Goal: Create an IP pool, a DHCP server, and necessary firewall/routing configurations. This includes advanced considerations like limiting the pool, advanced queue management, firewall rules specific to DHCP services and API calls to inspect DHCP leases.
*   Advanced elements: HA Considerations, IPv6 considerations, MAC Server, RoMON configuration, and a deep dive into diagnostics

## 2. Step-by-Step MikroTik Implementation (CLI and Winbox)

### Step-by-Step Using CLI

1.  **Assign IP Address to the Interface**

    *   Use the following command to assign the IP address `22.240.123.1/24` to `ether-90`:
        ```
        /ip address add address=22.240.123.1/24 interface=ether-90
        ```
2.  **Create an IP Pool**

    *   Create an IP pool named `customer_pool` using the full subnet range, excluding the router's IP (22.240.123.1)
        ```
        /ip pool add name=customer_pool ranges=22.240.123.2-22.240.123.254
        ```

3.  **Create a DHCP Server**

    *   Create a DHCP server listening on `ether-90` using the created pool, with a DNS server and a lease time of 10 minutes.
        ```
        /ip dhcp-server add name=dhcp_server_ether90 address-pool=customer_pool interface=ether-90 lease-time=10m authoritative=yes
        /ip dhcp-server network add address=22.240.123.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=22.240.123.1
        ```
    *    Note, the `authoritative=yes` directive is key to handling DHCP traffic on this network

4.  **Firewall Rules for DHCP**
    * Add rules that ensure DHCP is allowed to both the server and the client
    ```
       /ip firewall filter add chain=input action=accept protocol=udp dst-port=67,68
       /ip firewall filter add chain=forward action=accept protocol=udp dst-port=67,68
    ```

### Step-by-Step Using Winbox

1.  **Assign IP Address to Interface:**
    *   Go to **IP** > **Addresses**.
    *   Click the "+" button.
    *   Enter the address `22.240.123.1/24` and select `ether-90` for the interface.
    *   Click **Apply** and **OK**.

2.  **Create an IP Pool:**
    *   Go to **IP** > **Pool**.
    *   Click the "+" button.
    *   Enter the name `customer_pool` and the range `22.240.123.2-22.240.123.254`.
    *   Click **Apply** and **OK**.

3.  **Create a DHCP Server:**
    *   Go to **IP** > **DHCP Server**.
    *   Click the "+" button.
    *   Enter the name `dhcp_server_ether90`, select `ether-90` for the interface, choose `customer_pool` for the address pool, and set a lease time of `10m`. Ensure authoritative is checked.
    *   Go to the **Networks** tab and click the "+" button.
    *   Enter the address `22.240.123.0/24`, add the DNS servers (e.g., `8.8.8.8,8.8.4.4`), and set `22.240.123.1` as the gateway.
    *   Click **Apply** and **OK** on both windows.

4.  **Firewall Rules for DHCP**
    * Go to **IP** -> **Firewall**
    * In the **Filter Rules** tab, click the "+" button.
    * Set "chain" to `input`, protocol to `udp` and `dst-port` to `67,68`, and action to `accept`.
    * In the **Filter Rules** tab, click the "+" button.
     * Set "chain" to `forward`, protocol to `udp` and `dst-port` to `67,68`, and action to `accept`.
    * Click Apply, and OK.

## 3. Complete MikroTik CLI Configuration Commands

```
# Assign IP address to the interface
/ip address add address=22.240.123.1/24 interface=ether-90

# Create IP pool
/ip pool add name=customer_pool ranges=22.240.123.2-22.240.123.254

# Create DHCP server
/ip dhcp-server add name=dhcp_server_ether90 address-pool=customer_pool interface=ether-90 lease-time=10m authoritative=yes
/ip dhcp-server network add address=22.240.123.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=22.240.123.1

# Firewall rules for DHCP
/ip firewall filter add chain=input action=accept protocol=udp dst-port=67,68
/ip firewall filter add chain=forward action=accept protocol=udp dst-port=67,68
```
## 4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics

*   **DHCP Not Working:** Check the DHCP server configuration, especially the IP pool and network settings. Ensure the interface is correct.
    *   **Error Scenario:** `DHCP server is not enabled` - Verify the DHCP server is enabled and the interface is listening. Check logs using `/system logging print` with `topic=dhcp` and `topic=error`.
    *   **Troubleshooting:**
        *   `/ip dhcp-server print` - Verify DHCP server is enabled.
        *   `/ip dhcp-server network print` - Verify the network range.
        *   Use `/tool sniffer` to capture DHCP packets on the interface.
    *   **Example CLI Error Analysis**
    ```
    /system logging print where topics~"dhcp"
    ```
    This command will give a history of the dhcp server issues on the system.
*   **IP Conflicts:** Check if IPs within the pool are already assigned or statically configured.
    *   **Troubleshooting:** Use `/ip address print` to review IP assignments on other interfaces.
*  **Lease time problems:** DHCP leases may expire quicker than anticipated or not at all.
     *   **Troubleshooting:** Review the DHCP server configuration for `lease-time`
     *   **Error scenario:** Client loses DHCP address, even if it is plugged in.
*   **Firewall Issues:** Ensure necessary firewall rules are in place, especially if `default-forward` is set to `drop`.
    *   **Troubleshooting:** Use `/ip firewall filter print` and `/tool torch interface=ether-90` to observe traffic.
*   **Incorrect Gateway:** Ensure the gateway is correctly set in the DHCP network configuration.
    *   **Troubleshooting:** `/ip dhcp-server network print` to verify gateway address.
*   **Incorrect DNS Server:**  Ensure the DNS servers are correctly set in the DHCP network configuration.
    *   **Troubleshooting:** `/ip dhcp-server network print` to verify DNS server addresses.
*   **Limited IP Pool Range:** If an IP Pool runs out of available addresses, there will be no additional addresses handed out.
    *   **Troubleshooting:** Use `/ip pool print` to verify the current range, as well as `/ip dhcp-server lease print` to view all of the currently handed out IPs.

## 5. Verification and Testing Steps

*   **Ping:** From a client machine connected to `ether-90`, ping `22.240.123.1` to verify basic connectivity to the gateway.
*   **DHCP Lease:** Verify that a client machine receives an IP address from the configured pool. You can view current leases with the following command:
    ```
     /ip dhcp-server lease print
    ```
*   **Traceroute:** From the client, perform a traceroute to a destination outside the subnet (e.g., 8.8.8.8) to verify routing is working.
*   **Torch:** Use MikroTik's `torch` tool on the interface to observe traffic flow. Example:
    ```
    /tool torch interface=ether-90 duration=60
    ```
*   **Packet Sniffer:** Capture and examine traffic using `/tool sniffer`. This will allow for detailed troubleshooting.
  ```
     /tool sniffer quick interface=ether-90 duration=60 file-name=sniffer_output.cap
  ```
*   **IP Scan:** Use `/ip scan interface=ether-90` to see all hosts on the subnet.
*   **Logging:** `/system logging print` to review the logs for any error messages or warnings.

## 6. Related MikroTik-Specific Features, Capabilities, and Limitations

*   **Multiple IP Pools:** MikroTik supports multiple IP pools, which can be used for different VLANs, interfaces or for different address spaces on a given interface.
*   **IP Pool Limitations:** You cannot use IP address outside of a specified CIDR range for a given IP pool.
*   **Address Reservation:** You can specify static DHCP leases using the `mac-address` parameter.  This allows for IP address reservations that can be used to provide servers or special use devices with the same IP on every connection.
    *   **Example CLI:**
        ```
         /ip dhcp-server lease add address=22.240.123.10 mac-address=00:11:22:33:44:55 server=dhcp_server_ether90
       ```

*   **DHCP Options:** You can use the `/ip dhcp-server option` to configure parameters like the NTP server or other network-specific settings.
    *   **Example CLI:**
        ```
         /ip dhcp-server option add name=ntp-server code=42 value="192.168.1.1"
         /ip dhcp-server network set numbers=0 dhcp-option=ntp-server
       ```
*   **VRF Aware DHCP:** DHCP can be tied to VRF, allowing for separation of address assignment based on different VRF contexts, which is important for complex routing setups.
    *  **Example CLI**
    ```
    /routing vrf add name=customer-vrf
    /ip address add address=22.240.123.1/24 interface=ether-90 vrf=customer-vrf
    /ip pool add name=customer-pool vrf=customer-vrf ranges=22.240.123.2-22.240.123.254
    /ip dhcp-server add name=dhcp_server_ether90 address-pool=customer_pool interface=ether-90 vrf=customer-vrf lease-time=10m authoritative=yes
    /ip dhcp-server network add address=22.240.123.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=22.240.123.1 vrf=customer-vrf
    ```

## 7. MikroTik REST API Examples

Here are examples of interacting with the MikroTik DHCP server and address pool settings using the MikroTik REST API.

**Note:** *These examples assume you've configured REST API access on the MikroTik Router (System -> API).*

*   **API Endpoint:** `https://<your_router_ip>/rest/ip/dhcp-server`
*   **Authentication:** Basic Auth with username/password of a router user with API access.

**Example 1: Get DHCP Server List**

*   **Request Method:** `GET`
*   **Example `curl` command:**
    ```bash
    curl -u <your_user>:<your_password> -k -H "Content-Type: application/json" https://<your_router_ip>/rest/ip/dhcp-server
    ```
*   **Expected Response (JSON):**
    ```json
    [
        {
            ".id": "*1",
            "name": "dhcp_server_ether90",
            "interface": "ether-90",
            "address-pool": "customer_pool",
            "lease-time": "10m",
            "authoritative": "yes"
        }
    ]
    ```

**Example 2: Get DHCP leases**

*   **API Endpoint:** `https://<your_router_ip>/rest/ip/dhcp-server/lease`
*   **Request Method:** `GET`
*   **Example `curl` command:**
    ```bash
    curl -u <your_user>:<your_password> -k -H "Content-Type: application/json" https://<your_router_ip>/rest/ip/dhcp-server/lease
    ```
*  **Expected Response (JSON)**

   ```json
  [
     {
       ".id": "*2",
       "address": "22.240.123.2",
       "mac-address": "00:11:22:33:44:55",
       "server": "dhcp_server_ether90",
        "host-name": "Somehost-1",
        "expires-after": "10m"
     }
  ]

   ```

**Example 3: Add a New DHCP Server Lease Reservation**

*   **API Endpoint:** `https://<your_router_ip>/rest/ip/dhcp-server/lease`
*   **Request Method:** `POST`
*   **Example `curl` command:**

    ```bash
    curl -u <your_user>:<your_password> -k -H "Content-Type: application/json" -d '{"address":"22.240.123.10","mac-address":"00:11:22:33:44:55", "server":"dhcp_server_ether90"}' https://<your_router_ip>/rest/ip/dhcp-server/lease
    ```

*   **Expected Response (JSON):**
    ```json
    { "message": "added"}
    ```

**Example 4: Get IP Pool List**

*   **API Endpoint:** `https://<your_router_ip>/rest/ip/pool`
*   **Request Method:** `GET`
*   **Example `curl` command:**
    ```bash
    curl -u <your_user>:<your_password> -k -H "Content-Type: application/json" https://<your_router_ip>/rest/ip/pool
    ```
*   **Expected Response (JSON):**
    ```json
    [
        {
            ".id": "*1",
            "name": "customer_pool",
            "ranges": "22.240.123.2-22.240.123.254"
        }
    ]
    ```

## 8. In-Depth Explanations of Core Concepts

*   **IP Addressing:** In this context, the IP address (`22.240.123.1/24`) is assigned to the router’s interface. This IP address acts as the gateway for the customer devices within the subnet, allowing the clients to communicate with the outside world through NAT or routing. RouterOS uses a CIDR notation (e.g., `/24`) to define the network mask.
*   **IP Pools:** IP Pools are a defined range of addresses that are available for use within RouterOS. The IP addresses in the pool do not need to be in a particular order and can be non-contiguous.
    *  RouterOS dynamically assigns IP addresses from the pool using DHCP protocol.
*   **IP Routing:** The router needs to know how to reach networks outside the local subnet. The gateway configured for the DHCP server points to the router’s IP, which is the next hop in reaching other networks. Static routes or dynamic protocols like OSPF can be configured to define the full routing behavior of the router.
*   **IP Settings:**  RouterOS allows various other IP settings including connection tracking (to keep track of stateful connections), setting an MTU size (Maximum Transmission Unit) on the interface and managing MAC addresses.
*   **Bridging and Switching:** Bridging allows a router to act as a layer 2 switch between ports, extending layer 2 network beyond what single interface can provide.  For this example, we are not using bridging, instead ether-90 will act as the entry point for all clients connecting.
*   **Firewall:** RouterOS firewall is crucial for security, allowing or blocking traffic based on defined rules.  In our example, we added DHCP rules to both the input and forwarding chains, ensuring proper traffic traversal.

## 9. Security Best Practices

*   **Change Default Credentials:** Always change the default admin password.
*   **Disable Unused Services:** Disable any services that are not needed, including API access if it is not required.
*   **Use Strong Passwords:** Implement a strong password policy for all user accounts.
*   **Limit Access:** Use firewall rules to restrict access to the router from specific IP addresses or networks.
*   **Regular Updates:** Keep RouterOS updated to the latest stable version to patch vulnerabilities.
*   **API Access Security:**  Restrict API access using firewall rules, only allow access from trusted sources or management machines.
*   **Implement HTTPS for Winbox and Web:** Use HTTPS with certificates for secure access to the router management interfaces.
*   **Monitor Logs:** Regularly review the logs for any unusual activity.
*   **MAC Address Filtering (if applicable):** If practical in your environment, you can filter DHCP leases based on the MAC address to prevent unknown devices from connecting to your network.

## 10. Detailed Explanations and Configuration Examples for MikroTik Topics

### IP Addressing (IPv4 and IPv6)

*   **IPv4:** Addresses are assigned statically or dynamically using DHCP. As shown above, the subnet is defined with a network address `22.240.123.0/24`.
*   **IPv6:**  RouterOS supports IPv6. An IPv6 address looks like `2001:0db8:0000:0042:0000:8a2e:0370:7334/64`.
    *   **Example CLI:**
        ```
         /ipv6 address add address=2001:0db8::1/64 interface=ether-90
         /ipv6 pool add name=ipv6_pool prefix=2001:db8:1::/48
         /ipv6 dhcp-server add name=ipv6_dhcp_server_ether90 address-pool=ipv6_pool interface=ether-90
         /ipv6 dhcp-server network add address=2001:db8:1::/64 dns-server=2001:4860:4860::8888
         /ipv6 nd add interface=ether-90 advertise-dns=yes
        ```
    * This sets a global scope address on interface ether-90, and assigns the pool to the interface.  The `nd add` command allows a client to auto-configure an address based on the routers configured network.

### MAC server

*   The MAC server allows for telnet/ssh access via MAC address. This is generally only used in very specific cases, and generally not best practice for security purposes.
*    **Example CLI**
    ```
    /tool mac-server set allowed-interface-list=all enabled=yes
    /tool mac-server mac-winbox set allowed-interface-list=all enabled=yes
    /tool mac-server ping set allowed-interface-list=all enabled=yes
    ```

### RoMON

*   RoMON is a MikroTik proprietary tool that allows for a secure layer-2 connection to MikroTik devices. This can be useful for management, especially in cases where devices are far away or disconnected from traditional management interfaces.
*    **Example CLI**
    ```
     /tool romon set enabled=yes id=my_router_id key="my_secure_romon_key"
    ```
* You can then use winbox to connect to other romon enabled devices on the network via IP -> Neighbors and then click connect via Romon.

### WinBox

*   Winbox is the primary GUI management tool for MikroTik routers. All of the commands here can be done via the winbox GUI.

### Certificates

*   Certificates are used for HTTPS, VPN tunnels and other applications that require secure authentication. This is configured under system -> certificates in Winbox or `/certificate print`.
*   **Example CLI:**
    ```
      /certificate generate-self-signed common-name="router.mydomain.com" key-usage=tls-server,digital-signature
    ```
*  This creates a self-signed cert, which can be then enabled for use in Winbox or other services.

### PPP AAA

*   AAA is a term that covers Authentication, Authorization and Accounting of a connection. This is commonly used for PPPoE or other layer 3 VPN tunnels. PPP Secrets contain user information that the PPP service can authenticate against.
*    **Example CLI:**
     ```
    /ppp secret add name=john password=mypassword service=pppoe profile=default
    /ppp profile add name=default dns-server=8.8.8.8,8.8.4.4
     ```
* This creates a basic user/password for a pppoe connection.  The `/ppp profile` defines how the connection works.

### RADIUS

*   RADIUS is a protocol that provides centralized Authentication, Authorization, and Accounting. It is typically used for larger networks. RADIUS servers can be configured with the `/radius print` command.
    *  **Example CLI:**
       ```
        /radius add address=192.168.1.1 secret=radius_secret service=ppp
       ```
 * This adds a basic radius server, with a secret, that can be used for any PPP interface configured.

### User / User groups

*   RouterOS supports multiple users with various permissions, useful for limiting access to the router. User groups help control permissions.
     *   **Example CLI:**
        ```
          /user group add name=limited-access policy=read
          /user add name=readonly_user group=limited-access password=readonly
         ```
* This creates a basic read-only user.

### Bridging and Switching

*  As mentioned above, bridging allows for layer 2 network expansion. Switching refers to the layer 2 capabilities of the router itself.
   *  **Example CLI:**
       ```
         /interface bridge add name=bridge1
         /interface bridge port add bridge=bridge1 interface=ether1
         /interface bridge port add bridge=bridge1 interface=ether2
      ```
*  This creates a bridge, and adds ether1 and ether2 to it. The two ports will now act as a single layer 2 segment.

### MACVLAN

*   MACVLAN allows creation of multiple logical interfaces with different MAC addresses attached to a single physical interface. This is generally not needed for most scenarios.
    *  **Example CLI:**
         ```
          /interface macvlan add master-interface=ether1 mac-address=02:03:04:05:06:07 name=macvlan1
         ```
* This creates a virtual interface on top of ether1, with a different mac address.

### L3 Hardware Offloading

*   L3 Hardware Offloading allows for traffic routing at the hardware level, using the switch chips on the router. This greatly improves throughput.
    * This is automatically enabled on many interfaces. There is not configuration needed in most cases. However if an interface is not offloading, it can be explicitly defined.
     *   **Example CLI:**
          ```
          /interface ethernet set ether1 l3-hw-offload=yes
         ```

### MACsec

*   MACsec (Media Access Control Security) provides security at the data link layer. It’s used to encrypt data transmitted between devices on an Ethernet network.
     *  **Example CLI:**
         ```
         /interface macsec set interface=ether1 eapol-key-type=pre-shared-key eapol-key=mypassword
          ```
* This uses the pre-shared-key protocol to provide MACsec functionality.

### Quality of Service

*   QoS ensures certain types of traffic are prioritized. This is vital for ensuring high priority traffic can flow in a bandwidth limited environment.
    *   **Example CLI:**
        ```
          /queue type add name=low-priority kind=pcq pcq-rate=1M
          /queue tree add name=ether90-out parent=global-out interface=ether-90 queue=low-priority
           /ip firewall mangle add chain=forward action=mark-packet new-packet-mark=low-priority-mark passthrough=no dst-address-list=22.240.123.0/24
           /queue tree add name=low-priority-queue parent=ether90-out packet-mark=low-priority-mark queue=low-priority
        ```
* This defines a type of low priority queue and applies it to outbound traffic on ether90.

### Switch Chip Features

*   RouterOS allows for the configuration of various features on the routers switch chip.  This can include port mirroring, vlan configuration or other similar functionality.
    *   **Example CLI:**
        ```
         /interface ethernet switch vlan add tagged-ports=ether1,ether2 vlan-id=100
          /interface ethernet switch port set ether3 default-vlan-id=100
        ```
* This configures ether1 and ether2 to operate on vlan 100, and sets ether3 to operate in vlan 100 by default.

### VLAN

*   Virtual LANs (VLANs) allow separation of network traffic within the same physical infrastructure.
     *   **Example CLI:**
        ```
         /interface vlan add name=vlan100 vlan-id=100 interface=ether1
          /ip address add address=10.10.10.1/24 interface=vlan100
         ```
* This creates a vlan interface tagged with 100 on top of ether1.

### VXLAN

*   VXLAN allows layer 2 traffic to be tunneled over layer 3 networks. This extends a network using a layer 3 backbone.
    *  **Example CLI:**
        ```
           /interface vxlan add name=vxlan1 vni=1000  interface=ether1
        ```

### Firewall and Quality of Service

*   **Connection Tracking:** RouterOS keeps track of connections, statefully allowing/denying traffic.
*   **Firewall:** As shown, it's crucial for access control.
     *    **Example CLI:**
        ```
          /ip firewall filter add chain=forward action=drop src-address=192.168.1.0/24
        ```
* This drops traffic from the entire 192.168.1.0/24 network.
*   **Packet Flow:** Traffic goes through the input, forward, or output chains of the firewall, and is processed from top to bottom.
*  **Queues:** Queues are used to prioritize and limit traffic. As seen above.
*   **Firewall and QoS Case Studies:** For example, rate-limiting specific IPs or prioritizing VOIP traffic.
*   **Kid Control:** Can be done via scheduler and firewall, limiting access for certain devices.
    *  **Example CLI:**
        ```
          /system scheduler add name=block-kids on-event="/ip firewall filter disable numbers [find where comment=\"kid\"]" start-time=21:00 interval=1d
          /system scheduler add name=enable-kids on-event="/ip firewall filter enable numbers [find where comment=\"kid\"]" start-time=07:00 interval=1d
          /ip firewall filter add comment="kid" chain=forward src-address=192.168.1.2 action=drop
        ```
 * This blocks a specific ip address between 9pm and 7am using the scheduler and the firewall.
*   **UPnP/NAT-PMP:** Can automatically configure port forwards for applications. Can be configured by `/ip upnp print`
    *  **Example CLI:**
    ```
         /ip upnp set enabled=yes allow-disable-external-interface=yes
    ```

### IP Services (DHCP, DNS, SOCKS, Proxy)

*   **DHCP:** Manages IP addresses.
*   **DNS:** RouterOS has a DNS server which can be configured `/ip dns print`
    *  **Example CLI:**
         ```
         /ip dns set servers=8.8.8.8,8.8.4.4 allow-remote-requests=yes
         ```
*   **SOCKS:** A proxy server for traffic forwarding can be configured under `/ip socks print`
    *  **Example CLI:**
         ```
            /ip socks set enabled=yes
           /ip firewall nat add chain=dstnat protocol=tcp dst-port=80 to-addresses=127.0.0.1 to-ports=8080
         ```
* This configures a basic sock server and port forwards all incoming traffic on port 80 to the internal interface and port 8080.
*   **Proxy:** HTTP proxy server used to cache web requests under `/ip proxy print`
     *  **Example CLI:**
           ```
         /ip proxy set enabled=yes
         ```

### High Availability Solutions

*   **Load Balancing:** Can use ECMP routing, NTH connections or other algorithms for load balancing connections across multiple paths.
    * **Example CLI**
    ```
       /ip route add dst-address=0.0.0.0/0 gateway=192.168.1.1 check-gateway=ping
       /ip route add dst-address=0.0.0.0/0 gateway=192.168.2.1 check-gateway=ping
    ```
*   **Bonding:** Combines multiple interfaces into a single logical link for increased throughput and redundancy.
    *  **Example CLI:**
      ```
        /interface bonding add name=bond1 mode=802.3ad slaves=ether1,ether2
     ```
* **HA Case Studies:** Example: VRRP with failover for critical network components.
*   **Multi-chassis Link Aggregation Group (MLAG):** Allows links from multiple switches to be aggregated, increasing uplink capacity for multiple devices.
* **VRRP:** Provides router redundancy, with one acting as master and the other as backup. Configured under `/interface vrrp print`
    *  **Example CLI:**
        ```
          /interface vrrp add name=vrrp1 interface=ether1 vrid=1 priority=100
          /ip address add interface=vrrp1 address=192.168.1.1/24
        ```
*   **VRRP Configuration Examples:** Setting up virtual routers with priority and failover parameters

### Mobile Networking

*   **GPS:** RouterOS can use GPS modules for location tracking under `/system gps print`
*   **LTE:** Built-in LTE functionality for cellular internet access configured under `/interface lte print`
*  **PPP:** As configured above, PPP is used for dial up connections.
*   **SMS:** Supports SMS messaging, generally for remote management, configured using `/tool sms print`
*   **Dual SIM Application:**  RouterOS can be configured for dual SIM failover under `/interface lte`

### Multi Protocol Label Switching - MPLS

*   **MPLS Overview:** MPLS allows for the creation of Layer 2 and 3 connections via labels. This can simplify complex connections.
*   **MPLS MTU:**  MPLS requires a larger MTU due to headers.
*   **Forwarding and Label Bindings:** Labels are assigned to packets for efficient forwarding.
*   **EXP bit and MPLS Queuing:** The EXP bit is used for QoS.
*   **LDP:** Label Distribution Protocol is used for label exchange.
*   **VPLS:**  Virtual Private LAN Service, used to provide multipoint layer 2 connectivity.
*   **Traffic Eng:** Traffic Engineering used for path selection.

### Network Management

*  **ARP:** Address Resolution Protocol, maps MAC to IP addresses. Found under `/ip arp print`
* **Cloud:** MikroTik cloud allows for centralized management of multiple devices. Configured under `/cloud print`
* **DHCP:** As previously covered.
* **DNS:** As previously covered.
* **SOCKS:** As previously covered.
* **Proxy:** As previously covered.
*  **Openflow:** Supports Openflow protocol for SDN type functionality.

### Routing

*   **Routing Protocol Overview:** RouterOS supports static, RIP, OSPF, BGP, and others.
*   **Moving from ROSv6 to v7 with examples:** RouterOS v7 uses a newer architecture of protocols, moving away from the single routing table model.
*   **Routing Protocol Multi-core Support:** Allows for better scaling.
*   **Policy Routing:** Allows you to route packets based on criteria, useful in complex setups.
    *  **Example CLI:**
        ```
        /ip route rule add src-address=192.168.1.0/24 table=special_routing
        /ip route add dst-address=0.0.0.0/0 gateway=10.10.10.1 routing-mark=special_routing
        ```
*  **Virtual Routing and Forwarding - VRF:**  Used for separating routing tables.
    *   **Example CLI:**
         ```
         /routing vrf add name=vrf1
         /ip address add interface=ether1 address=10.0.0.1/24 vrf=vrf1
         ```
*   **OSPF:** Open Shortest Path First,
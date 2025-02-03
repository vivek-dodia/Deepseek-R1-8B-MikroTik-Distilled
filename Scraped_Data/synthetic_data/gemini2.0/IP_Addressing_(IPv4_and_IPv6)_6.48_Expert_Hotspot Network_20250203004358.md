Okay, let's dive deep into this extensive MikroTik documentation. This will be a comprehensive guide, focused on the requested parameters, and geared towards an expert-level understanding of RouterOS.

## MikroTik RouterOS Configuration for a Hotspot Network (Expert Level)

This document provides a comprehensive guide to configuring a MikroTik router for a Hotspot network, specifically focusing on IP addressing and related features. We'll use RouterOS version 6.48 (compatible with 7.x) and the provided parameters: subnet `22.5.209.0/24` on interface `wlan-29`.

**1. Comprehensive Configuration Scenario and Requirements:**

*   **Scenario:** A small to medium-sized hotspot network (e.g., a coffee shop, small hotel) requires reliable and secure internet access for its clients.
*   **Subnet:** We will use the provided `22.5.209.0/24` subnet for the wireless clients.
*   **Interface:** The wireless interface designated for this network is `wlan-29`.
*   **Requirements:**
    *   Dynamic IP address assignment to clients using DHCP.
    *   Basic firewall protection for the hotspot network.
    *   Optional: Limited Quality of Service (QoS) for fairness.
    *   User authentication if desired.

**2. Step-by-Step MikroTik Implementation (CLI & Winbox):**

**Using the CLI:**

*   **Step 1: Access the CLI:** Connect to your MikroTik router via SSH or using the Terminal in Winbox.
*   **Step 2: Configure the Wireless Interface:**
    ```mikrotik
    /interface wireless
    set wlan-29 mode=ap-bridge ssid="Hotspot-Name" band=2ghz-b/g/n channel-width=20/40mhz-Ce country=us frequency=2437 security-profile=default
    enable wlan-29
    ```

     * **Explanation:**
       *   `/interface wireless` accesses the interface wireless config section.
       *   `set wlan-29` sets config parameters for interface wlan-29.
       *   `mode=ap-bridge` configures the interface as an access point bridge
       *   `ssid="Hotspot-Name"` Sets the SSID
       *   `band=2ghz-b/g/n` set band settings.
       *   `channel-width=20/40mhz-Ce` set channel width settings.
       *   `country=us` set country
       *   `frequency=2437` set specific frequency.
       *   `security-profile=default` set the security profile. You'll need to create and configure a security profile later.
       *   `enable wlan-29` activates the wireless interface.

*   **Step 3: Configure the IP Address:**
    ```mikrotik
    /ip address
    add address=22.5.209.1/24 interface=wlan-29
    ```

     * **Explanation:**
       *   `/ip address` accesses the IP Address config section.
       *   `add address=22.5.209.1/24` Sets the IP address of the wlan-29 to 22.5.209.1/24.
       *   `interface=wlan-29` ties the IP to the wlan-29 interface.

*   **Step 4: Configure the DHCP Server:**
    ```mikrotik
    /ip pool
    add name=hotspot-pool ranges=22.5.209.100-22.5.209.254
    /ip dhcp-server
    add address-pool=hotspot-pool disabled=no interface=wlan-29 lease-time=3h name=hotspot-dhcp
    /ip dhcp-server network
    add address=22.5.209.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=22.5.209.1
    ```

     * **Explanation:**
       *   `/ip pool` accesses the IP pool config section.
       *  `add name=hotspot-pool ranges=22.5.209.100-22.5.209.254` Creates an IP address pool named `hotspot-pool`.
       *   `/ip dhcp-server` accesses the DHCP server config section.
       *   `add address-pool=hotspot-pool disabled=no interface=wlan-29 lease-time=3h name=hotspot-dhcp` Creates a DHCP server using the `hotspot-pool`, tying it to interface `wlan-29`, with a 3-hour lease time.
       *   `/ip dhcp-server network` accesses the DHCP network config section.
       *   `add address=22.5.209.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=22.5.209.1` Sets the DNS and gateway information for the DHCP clients.

*   **Step 5: Basic Firewall Configuration:**
    ```mikrotik
    /ip firewall filter
    add chain=input connection-state=established,related action=accept
    add chain=input protocol=icmp action=accept
    add chain=input in-interface=wlan-29 action=drop
    add chain=forward connection-state=established,related action=accept
    add chain=forward in-interface=wlan-29 out-interface=!(wlan-29) action=accept
    add chain=forward in-interface=!(wlan-29) out-interface=wlan-29 action=drop
    /ip firewall nat
    add chain=srcnat out-interface=!(wlan-29) action=masquerade
    ```

     * **Explanation:**
       *   `/ip firewall filter` accesses the firewall filter section.
       *   The first two rules in the input chain allow already established and related connections as well as ICMP (ping) traffic to the router.
       *   The third rule in the input chain drops all other traffic coming into the router via interface `wlan-29`.
       *   The first rule in the forward chain allows already established and related connections
       *   The second rule in the forward chain allows traffic from `wlan-29` to any other interface.
       *   The third rule in the forward chain blocks traffic from other interfaces to `wlan-29`.
       *   `/ip firewall nat` accesses the firewall NAT section.
       *    The rule in the `srcnat` chain configures NAT masquerading for traffic leaving the router through any interface other than `wlan-29`. This rule hides the local network's IP addresses behind the router's public IP address.

*   **Step 6: Configure a Wireless Security Profile**
    ```mikrotik
    /interface wireless security-profiles
    add name=hotspot-security mode=dynamic-keys authentication-types=wpa2-psk,wpa-psk eap-methods=passthrough group-encryption=aes-ccm group-key-update=1h management-protection=allowed unicast-ciphers=aes-ccm wpa-pre-shared-key="YourSecretKey" wpa2-pre-shared-key="YourSecretKey"
    /interface wireless
    set wlan-29 security-profile=hotspot-security
    ```

        * **Explanation:**
          * `/interface wireless security-profiles` accesses the wireless security profiles config section.
          * `add name=hotspot-security` creates a new security profile named hotspot-security
          * `mode=dynamic-keys` enables use of dynamic keys
          * `authentication-types=wpa2-psk,wpa-psk` enables wpa2-psk and wpa-psk authentication
          * `eap-methods=passthrough` disables eap methods
          * `group-encryption=aes-ccm` sets the group encryption
          * `group-key-update=1h` sets group key update rate
          * `management-protection=allowed` enables management protection
          * `unicast-ciphers=aes-ccm` sets the unicast ciphers
          * `wpa-pre-shared-key="YourSecretKey" wpa2-pre-shared-key="YourSecretKey"` sets the wpa and wpa2 pre shared keys.
          * `/interface wireless` accesses the interface wireless section
          * `set wlan-29 security-profile=hotspot-security` sets the wlan-29 interface to use the new security profile

**Using Winbox (GUI):**

1.  **Interface Setup:** Navigate to *Interfaces* -> *Wireless*, and edit `wlan-29`.
    *   Set mode to `ap bridge`, SSID (e.g., "Hotspot-Name"), band, channel, and country.
    *   Enable the interface.
2.  **IP Address Setup:** Navigate to *IP* -> *Addresses*.
    *   Add a new address: `22.5.209.1/24`, Interface: `wlan-29`.
3.  **DHCP Server Setup:** Navigate to *IP* -> *Pool*.
    *   Add a new pool: `name=hotspot-pool`, ranges: `22.5.209.100-22.5.209.254`.
    Navigate to *IP* -> *DHCP Server*.
    *   Add a new DHCP server: `interface=wlan-29`, `address-pool=hotspot-pool`, `lease-time=3h`.
    Navigate to *IP* -> *DHCP Network*.
    *   Add a new network: `address=22.5.209.0/24`, `gateway=22.5.209.1`, `dns-server=8.8.8.8,8.8.4.4`.
4. **Wireless Security Setup:** Navigate to *Wireless* -> *Security Profiles*.
    * Add a new security profile.
        * Set the Name to `hotspot-security`.
        * Set the `mode` to dynamic keys.
        * Set the `authentication-types` to wpa2-psk and wpa-psk.
        * Set the `group-encryption` to aes-ccm
        * Set the `unicast-ciphers` to aes-ccm
        * Set the WPA Pre-Shared Key and the WPA2 Pre-Shared Key to your secret keys.
    *  Navigate back to *Interfaces* -> *Wireless*.
    *  Edit `wlan-29`, change the security profile to the new profile.
5.  **Firewall Setup:** Navigate to *IP* -> *Firewall*.
    *   Add *Filter Rules* for input, forward, and NAT with corresponding settings.
    *   Refer to the CLI commands for filter and NAT rule configuration.

**3. Complete MikroTik CLI Configuration Commands:**

```mikrotik
/interface wireless
set wlan-29 mode=ap-bridge ssid="Hotspot-Name" band=2ghz-b/g/n channel-width=20/40mhz-Ce country=us frequency=2437 security-profile=default
enable wlan-29

/ip address
add address=22.5.209.1/24 interface=wlan-29

/ip pool
add name=hotspot-pool ranges=22.5.209.100-22.5.209.254

/ip dhcp-server
add address-pool=hotspot-pool disabled=no interface=wlan-29 lease-time=3h name=hotspot-dhcp

/ip dhcp-server network
add address=22.5.209.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=22.5.209.1

/ip firewall filter
add chain=input connection-state=established,related action=accept
add chain=input protocol=icmp action=accept
add chain=input in-interface=wlan-29 action=drop
add chain=forward connection-state=established,related action=accept
add chain=forward in-interface=wlan-29 out-interface=!(wlan-29) action=accept
add chain=forward in-interface=!(wlan-29) out-interface=wlan-29 action=drop

/ip firewall nat
add chain=srcnat out-interface=!(wlan-29) action=masquerade

/interface wireless security-profiles
add name=hotspot-security mode=dynamic-keys authentication-types=wpa2-psk,wpa-psk eap-methods=passthrough group-encryption=aes-ccm group-key-update=1h management-protection=allowed unicast-ciphers=aes-ccm wpa-pre-shared-key="YourSecretKey" wpa2-pre-shared-key="YourSecretKey"

/interface wireless
set wlan-29 security-profile=hotspot-security
```

**4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics:**

*   **Wireless Interface not Enabled:**
    *   **Error:** Clients cannot connect to the Wi-Fi.
    *   **Troubleshooting:** Verify the wireless interface is enabled (`/interface wireless print`) and has a valid configuration.
*   **Incorrect IP Address Configuration:**
    *   **Error:** Clients cannot get an IP address via DHCP, or connectivity is limited.
    *   **Troubleshooting:** Double-check that the IP address, interface, and subnet match your desired configuration.
*   **DHCP Server Issues:**
    *   **Error:** Clients do not receive IP addresses.
    *   **Troubleshooting:**
        *   Check if the DHCP server is enabled.
        *   Verify the DHCP Pool ranges are correct.
        *   Ensure the DHCP server is associated with the correct interface.
        *   Use `/ip dhcp-server lease print` to see client leases.
*   **Firewall Issues:**
    *   **Error:** Clients cannot reach the internet, or internal network access is blocked.
    *   **Troubleshooting:**
        *   Review the firewall filter rules to see if anything is blocking communication. Use `/ip firewall filter print`.
        *   Check NAT configuration if clients are failing to reach the internet. Use `/ip firewall nat print`.
*   **DNS Problems:**
    *   **Error:** Clients cannot resolve DNS host names.
    *   **Troubleshooting:** Verify the DNS servers defined in `/ip dhcp-server network`.
* **Security Profile Issues:**
  * **Error:** Clients cannot authenticate to wireless network.
  * **Troubleshooting:** Verify that the correct shared key is being used by the security profile and that the security profile is set for the wlan interface.
*   **Tools:**
    *   `ping`: Test connectivity to and from clients.
    *   `traceroute`: Trace the path of packets.
    *   `torch`: Monitor traffic in real-time. `/tool torch interface=wlan-29`
    *   `/system resource monitor`: Check the system resource usage.
    *   `/log print`: Check RouterOS logs for errors.
    *   `Packet Sniffer`: Capture and analyze network traffic.
* **Error Scenario Example**
  * Error: Clients cannot connect to wireless network even when password is correct
  * `/interface wireless security-profiles print`: Shows that security profiles are correctly configured
  * `/interface wireless print`:  Shows that wlan-29 does not have a security profile set
  * Resolution: `/interface wireless set wlan-29 security-profile=hotspot-security`.
  * Explanation: Wlan-29 didn't have a security profile configured so clients could not authenticate with the router.

**5. Verification and Testing:**

*   **Wi-Fi Connection:** Connect a client device to the "Hotspot-Name" Wi-Fi network.
*   **IP Address:** Verify that the client receives an IP address within the `22.5.209.0/24` subnet.
*   **Ping Test:** Ping the router's interface IP address `22.5.209.1`.
*   **Internet Access:** Browse to a website to confirm internet connectivity.
*   **Traceroute:** Use traceroute to see the path taken to internet destinations.
    * Example `traceroute 8.8.8.8`
*   **Torch:** Use torch to monitor interface usage in real-time.
    * Example `tool torch interface=wlan-29`

**6. Related MikroTik-Specific Features, Capabilities, and Limitations:**

*   **Hotspot Feature:** RouterOS offers a full-fledged Hotspot system with user management, payment gateways, and more. `/ip hotspot`
    *  You can configure login pages, vouchers, radius integration, etc.
*   **VLANs:** Segregate the Hotspot network for added security.
*   **Queue Tree:** Implement advanced Quality of Service (QoS).
*   **User Manager:** Centralized user authentication for multiple hotspots.
*   **MAC address whitelist/blacklist**:  Restrict clients by their mac addresses
*   **IP Bindings**: Issue static IP leases to specific devices based on their MAC address
*   **Limitations:**
    *   RouterOS has a learning curve, and you need to familiarize yourself with the commands and their meanings.
    *   Hardware limitations can affect the number of concurrent users the router can handle.

**7. MikroTik REST API Examples (if applicable):**

*Note: MikroTik's REST API requires enabling the API service and proper authentication. These are just examples, you should use the actual values from your router and enable the api service.*

* **Enabling the API Service**
```mikrotik
/ip service
set api disabled=no
set api-ssl disabled=no
```

* **Example: Retrieving Wireless Interface Information:**

   *   **API Endpoint:** `/rest/interface/wireless`
   *   **Request Method:** GET
   *   **Example using `curl`:**
      ```bash
      curl -k -u "your_api_username:your_api_password" https://your_router_ip/rest/interface/wireless
      ```

    *   **Expected Response (JSON):**
        ```json
        [
         {
            ".id": "*2",
           "name": "wlan-29",
           "mtu": "1500",
           "actual-mtu": "1500",
           "mac-address": "CC:2D:E0:11:22:33",
           "type": "wlan",
           "running": true,
           "disabled": false,
           "arp": "enabled",
           "master-interface": "none",
           "mode": "ap-bridge",
            "band": "2ghz-b/g/n",
            "channel-width": "20/40mhz-Ce",
            "frequency": "2437",
            "ssid": "Hotspot-Name",
            "security-profile": "hotspot-security",
           "wps-mode": "disabled"
          }
        ]
        ```

*  **Example: Adding a new IP address**
  * **API Endpoint:** `/rest/ip/address`
  * **Request Method:** POST
  * **Example using `curl`:**
      ```bash
      curl -k -u "your_api_username:your_api_password" -H "Content-Type: application/json" -X POST  -d '{"address":"22.5.209.2/24", "interface":"wlan-29"}' https://your_router_ip/rest/ip/address
      ```

  *   **Expected Response (JSON):**
        ```json
          {"message":"added"}
        ```
  *  Note: The IP would now be added to the interfaces ip addresses.

*   **Example: Getting IP Addresses:**
    *   **API Endpoint:** `/rest/ip/address`
    *   **Request Method:** GET
    *   **Example using `curl`:**
         ```bash
          curl -k -u "your_api_username:your_api_password" https://your_router_ip/rest/ip/address
        ```
    *   **Expected Response (JSON):**
        ```json
       [
        {
          ".id": "*0",
          "address": "192.168.88.1/24",
          "interface": "ether1",
          "network": "192.168.88.0",
          "actual-interface": "ether1",
           "dynamic": false,
           "invalid": false
       },
       {
          ".id": "*1",
          "address": "22.5.209.1/24",
          "interface": "wlan-29",
          "network": "22.5.209.0",
          "actual-interface": "wlan-29",
          "dynamic": false,
           "invalid": false
        }
      ]
        ```

**8. In-depth Explanations of Core Concepts:**

*   **Bridging:**  A bridge links multiple interfaces so they act as a single network. The default bridge settings on the router are often appropriate for most environments. We did not need to use the bridging configuration for this implementation since we only used a single wlan interface.
*   **Routing:** The process of determining the best path for network traffic. We have only used the default routing settings in this implementation which send all traffic out the default gateway set for the router.
*   **Firewall:** Filters and secures traffic based on predefined rules. The most common firewall rules are in the `/ip firewall filter` section and the `/ip firewall nat` section. Filter rules control what traffic is allowed to pass through the router and NAT rules control how the source ip address of the packets are modified.
*   **DHCP:** Dynamically assigns IP addresses to devices on a network. The server settings are under `/ip dhcp-server` and the related network settings are under `/ip dhcp-server network`.
*   **IP Addressing:** Determines which IP addresses are used on each interface and the associated network mask. The IP address parameters are found under `/ip address`.

**9. Security Best Practices:**

*   **Change Default Passwords:** Always change the default admin password for the RouterOS interface.
*   **Disable Unused Services:** Disable services like Telnet and API if not needed `/ip service`.
*   **Use Strong Passwords:** Use strong, unique passwords for both your device user accounts and your WiFi networks.
*   **Firewall Rules:** Implement proper firewall rules to limit access to the router and your network.
*   **Regular Updates:** Keep your RouterOS version up-to-date to patch security vulnerabilities. `/system package update`.
*   **Management Access:** Limit access to the router's management interface to specific IP addresses `/ip service`.
* **Wireless Security**: Be sure to select a secure wireless authentication and encryption to protect access to your network.

**10. Detailed Explanations and Configuration Examples for additional MikroTik Topics:**

*   **IP Pools:** Used for managing IP address ranges for DHCP.
  *   Example: `/ip pool add name=my-pool ranges=10.0.0.10-10.0.0.200`.
*  **IP Routing**
  * `/ip route print` Displays active IP routes
  * `/ip route add dst-address=192.168.1.0/24 gateway=192.168.88.2` Creates an IP route to the subnet 192.168.1.0/24 via the gateway 192.168.88.2
*   **IP Settings:** Configures basic IP settings like ARP mode.
  * Example: `/ip settings set arp=enabled`.
*   **MAC Server:** Used to manage MAC addresses. Often used with RADIUS for AAA.
  * Example: `/mac-server interface=wlan1`.
*   **RoMON:** MikroTik's Remote Monitoring tool, helps manage multiple routers.
*   **WinBox:** MikroTik's GUI configuration tool (covered in step 2)
*   **Certificates:** Used for secure access to services and VPNs.
*   **PPP AAA:** Authentication, Authorization, and Accounting for PPP connections. Often done via a radius server.
*   **RADIUS:**  Authentication server for wireless, Hotspot, PPP, and other services.
    * Example: `/radius add address=10.10.10.1 secret=mysecret`
*   **User / User groups:** Manage router access via User settings.
  *  Example: `/user add name=testuser password=testpass group=full`
*   **Bridging and Switching:** Connecting interfaces at layer 2.
    * Example: `/interface bridge add name=my-bridge`
* **MACVLAN**: Allows multiple virtual interfaces to be created on a single physical interface.
  * Example: `/interface macvlan add interface=ether1 mac-address=02:44:44:22:22:22 name=macvlan1`
*   **L3 Hardware Offloading:** Offload some L3 processing to the hardware.
*   **MACsec:** MAC-level encryption. Often used on network switches.
*   **Quality of Service (QoS):** Prioritize or limit bandwidth for certain traffic.
    * Example: `/queue tree add name=download parent=global-in max-limit=20M`.
*   **Switch Chip Features:**  Specific switch chip configurations (on specific models).
*   **VLAN:** Virtual LANs to segment your network.
     * Example: `/interface vlan add name=vlan10 interface=ether1 vlan-id=10`
*  **VXLAN:** Virtual eXtensible LANs, allows network extension over L3.
  * Example: `/interface vxlan add name=vxlan1 vni=1000 interface=ether1`
*   **Firewall and Quality of Service:**
     *  **Connection Tracking:**  `/ip firewall connection print`.
     *  **Packet Flow in RouterOS:** Understand how packets go through the router
     *  **Queues:** Limit and prioritize traffic.
     *   **Firewall and QoS Case Studies:** How to use them in specific scenarios.
     *   **Kid Control:** Control internet access for kids.
     *  **UPnP:** Port forwarding. `/ip upnp`
     * **NAT-PMP** Alternate port forwarding tool `/ip nat-pmp`
*  **IP Services:**
    *   **DHCP:** (Covered earlier)
    *   **DNS:** Configures the DNS server on the router. `/ip dns`
    *   **SOCKS:** Simple proxy server. `/ip socks`
    *  **Proxy:** Web proxy configuration `/ip proxy`
* **High Availability Solutions:**
    * **Load Balancing:**
        *  **Per-connection classifier:** Distributes connections between links.
        *  **NTH classifier:** Distributes packets based on their hash.
    *  **Bonding:** Aggregates multiple links for higher bandwidth.
        * Example: `/interface bonding add name=bond1 mode=802.3ad slaves=ether1,ether2`
    * **HA Case Studies:** Best practices for HA.
    *  **Multi-chassis Link Aggregation Group:** Aggregates links from multiple switches
    *  **VRRP:**  Virtual Router Redundancy Protocol. `/interface vrrp`
    *  **VRRP Configuration Examples:** How to setup a vrrp configuration.
*   **Mobile Networking:**
     *   **GPS:** Use gps for location.
     *   **LTE:** 4G connections.
     *   **PPP:** Point-to-Point protocol, used for modems.
     *  **SMS:** Send and receive SMS messages.
     *  **Dual SIM Application:** Use multiple sims on devices that support them.
*   **Multi Protocol Label Switching - MPLS:**
    *   **MPLS Overview:** How MPLS works.
    *   **MPLS MTU:** MTU for MPLS.
    *   **Forwarding and Label Bindings:** How to forward packets based on MPLS labels
    *   **EXP bit and MPLS Queuing:** How to prioritize MPLS traffic using the EXP bit.
    *   **LDP:** Label Distribution Protocol.
    *   **VPLS:** Virtual Private LAN Service.
    *   **Traffic Eng:** MPLS traffic engineering.
    *   **MPLS Reference:** More detailed reference for MPLS.
*   **Network Management:**
    *   **ARP:** Address Resolution Protocol.
    *   **Cloud:** MikroTik's Cloud services.
    *   **DHCP, DNS, SOCKS, Proxy:** (Covered earlier)
    *   **Openflow:** Openflow switch configuration.
*   **Routing:**
    *   **Routing Protocol Overview:**
        *   **Static Routing:**
          * Example:  `/ip route add dst-address=10.0.0.0/24 gateway=192.168.88.2`
        *  **Dynamic Routing:**
    *  **Moving from ROSv6 to v7 with examples:** Configuration differences between RouterOS versions.
    *   **Routing Protocol Multi-core Support:** How to utilize multicore processors for routing.
    *   **Policy Routing:** Routing based on more than the destination IP.
    *   **Virtual Routing and Forwarding - VRF:** Use of VRFs
    *   **OSPF, RIP, BGP, RPKI:** Open Shortest Path First, Routing Information Protocol, Border Gateway Protocol, Resource Public Key Infrastructure
    *   **Route Selection and Filters:** How to determine which route is best.
    *   **Multicast:** Routing of multicast traffic
    *   **Routing Debugging Tools:** Tools to troubleshoot routing.
    *   **Routing Reference:** Detailed routing reference.
    *   **BFD:** Bidirectional Forwarding Detection.
    *   **IS-IS:** Intermediate System to Intermediate System routing.
*  **System Information and Utilities:**
    *  **Clock:** Set the system time.
    *  **Device-mode:** RouterOS device modes (router, switch)
    *  **E-mail:** Send email notifications.
    *  **Fetch:** Download files over http/https.
        * Example: `/tool fetch url=http://test.com/test.txt`
    *  **Files:** Manage files on the router.
    *  **Identity:** Set the Router's identity `/system identity set name="MyRouter"`.
    *  **Interface Lists:** Group interfaces into lists.
    *  **Neighbor discovery:** How devices discover neighbors
    *  **Note:** Add notes to your configuration.
    *  **NTP:** Network Time Protocol
    *  **Partitions:** Manage partitions on disk.
    *  **Precision Time Protocol:** High precision time sync.
    *  **Scheduler:** Schedule scripts to run automatically.
        * Example: `/system scheduler add name=test_script on-event="/system routerboard print" interval=1d`
    *  **Services:**  Enable or disable various services.
    *  **TFTP:** Trivial File Transfer Protocol.
*   **Virtual Private Networks (VPNs):**
    *  **6to4, EoIP, GRE, IPIP, IPsec, L2TP, OpenVPN, PPPoE, PPTP, SSTP, WireGuard, ZeroTier:** Various types of VPNs.

*   **Wired Connections:**
    *   **Ethernet:** Layer 2 wired connections.
    *   **MikroTik wired interface compatibility:** Which interfaces are supported.
    *   **PWR Line:** Powerline communication.
*   **Wireless:**
    *   **WiFi, Wireless Interface:** Configuration of wireless settings (covered earlier).
    *   **W60G:** 60GHz wireless.
    *   **CAPsMAN:** Centralized management of MikroTik wireless access points.
    *   **HWMPplus mesh:** Mesh networking with HWMP.
    *   **Nv2:** MikroTik's proprietary wireless protocol.
    *   **Interworking Profiles:** Configure wireless profiles for certain standards.
    *   **Wireless Case Studies:** How to configure wireless in common environments.
    *  **Spectral scan:** Wireless spectrum scanner. `/interface wireless spectral-history`
*   **Internet of Things (IoT):**
    *   **Bluetooth, GPIO, Lora, MQTT:**  Configuration of IoT interfaces.
*   **Hardware:**
    *   **Disks:** Manage internal or external drives
    *   **Grounding:** Proper grounding for hardware.
    *   **LCD Touchscreen:** Screen usage
    *   **LEDs:** Control LEDs. `/system led`
    *  **MTU in RouterOS:** MTU sizes.
    *  **Peripherals:** Connect peripherals.
    *  **PoE-Out:** Power over Ethernet out on interfaces.
    *  **Ports:**  Interface port information
    *  **Product Naming:** How MikroTik devices are named.
    *  **RouterBOARD:** RouterBOARD hardware info.
    *  **USB Features:** How to use USB devices.
*   **Diagnostics, monitoring and troubleshooting:**
     * **Bandwidth Test:** Test bandwidth between two points `/tool bandwidth-test`.
     * **Detect Internet:** Checks the availability of an internet connection
     * **Dynamic DNS:** Updates a hostname if your IP changes `/ip cloud`.
     * **Graphing:** View interface usage graphs
     * **Health:** Device health checks `/system health`.
     * **Interface stats and monitor-traffic:** How to monitor interfaces.
     * **IP Scan:** Scan for ip addresses in a subnet.
     * **Log:**  RouterOS system log (covered earlier)
     * **Netwatch:** Monitor hosts for availability.
        * Example: `/tool netwatch add host=8.8.8.8 interval=1m up-script="/log info message=\"host 8.8.8.8 is up\"" down-script="/log info message=\"host 8.8.8.8 is down\""`
     *  **Packet Sniffer:** Capture network traffic (covered earlier).
     *  **Ping:** Network connectivity testing tool. (covered earlier)
     *   **Profiler:** View processor usage for processes.
     *   **Resource:** Show resource usage. `/system resource print`
     *   **SNMP:** Simple network management protocol.
     *   **Speed Test:** Router speed testing tool.
     *   **S-RJ10 general guidance:** General S-RJ10 cable info.
     *   **Torch:** Real-time traffic monitoring (covered earlier).
     *   **Traceroute:** Trace network path. (covered earlier)
     *   **Traffic Flow:** Network traffic analysis tool.
     *   **Traffic Generator:** Generate test traffic.
     *   **Watchdog:** Automatically reset the device if something goes wrong. `/system watchdog`
*   **Extended features:**
     *   **Container:** Run containers on the router
     *   **DLNA Media server:** DLNA configuration
     *   **ROSE-storage:** MikroTik's storage service.
     *   **SMB:** Server message block
     *   **UPS:**  Uninterruptible power supply support.
     *   **Wake on LAN:** Send wake on lan packets
     *   **IP packing:** Send custom IP packets.

**Trade-offs Between Configurations:**

*   **Static vs. Dynamic IP:** Static is predictable, dynamic is easier to manage.
*   **Firewall Complexity:** Simple rules are easier to understand, but advanced rules provide
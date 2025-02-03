Okay, let's dive into a comprehensive documentation for MikroTik RouterOS 7.11, focusing on IP addressing and a point-to-point link with the specified parameters. This will be a detailed guide covering numerous aspects, following your specific instructions.

**1. Comprehensive Configuration Scenario**

We are setting up a point-to-point link using a MikroTik router with the following requirements:

*   **Subnet:** 195.190.61.0/24
*   **Interface:** `wlan-21` (assuming a wireless interface for this example, but it can be adapted for an Ethernet interface)
*   **Configuration Level:** Advanced. This means we'll go beyond basic setup and cover additional features.

This setup implies connecting two devices directly over wireless or Ethernet interface, with a private network IP range for communication.

**MikroTik Requirements:**

*   RouterOS 7.11 (or compatible 6.48, 7.x)
*   Access to the RouterOS configuration (Winbox, CLI, WebFig, or API).

**2. Step-by-Step MikroTik Implementation (CLI)**

Here's how to configure this using the MikroTik CLI:

*   **Step 1: Assign IP Address to the Interface**

    ```mikrotik
    /ip address
    add address=195.190.61.1/24 interface=wlan-21 network=195.190.61.0
    ```

    *   `address=195.190.61.1/24`: Assigns IP address `195.190.61.1` with a subnet mask of `/24` (255.255.255.0). This will be our default address on the interface.
    *   `interface=wlan-21`: Specifies the target interface for the IP address.
    *    `network=195.190.61.0`: Explicitly defines the network address. (While RouterOS usually calculates this, it's a good practice).

*   **Step 2: (Optional)  Configure a Second Router on the other end:**

        On the other router connected to wlan-21, configure:

    ```mikrotik
    /ip address
    add address=195.190.61.2/24 interface=wlan-21 network=195.190.61.0
    ```

    This will be the counterpart router’s IP address on the 195.190.61.0 network.

*   **Step 3: Ensure Interface is Enabled:**

    ```mikrotik
    /interface enable wlan-21
    ```

* **Step 4: (Wireless specific) Configure the wireless interface settings:**

   ```mikrotik
   /interface wireless
   set wlan-21 mode=ap-bridge ssid="pointtopoint" band=2ghz-b/g/n frequency=2412  wireless-protocol=802.11
   set wlan-21 country=united-states security-profile=default
   ```
   * `mode=ap-bridge`: Sets the wireless mode, enabling it to operate as an Access Point Bridge
   * `ssid="pointtopoint"`: Sets the name of the wireless network. This value must match on the other device to allow them to connect.
   * `band=2ghz-b/g/n`: Sets the wireless frequency band
   * `frequency=2412`: Sets the specific frequency channel in MHz
   * `wireless-protocol=802.11`: Sets the wireless standard
   * `country=united-states`: Sets the country code
   * `security-profile=default`: applies the security profile `default`. This MUST be secured, so the next steps will add configuration to the security profile.

* **Step 5: (Wireless specific) Configure the security profile:**

   ```mikrotik
   /interface wireless security-profiles
   set default mode=dynamic-keys authentication-types=wpa2-psk  eap-methods=passthrough group-encryption=aes-ccm  unicast-encryption=aes-ccm  wpa2-pre-shared-key="MyPassword123!"
   ```
  * `mode=dynamic-keys`: Set the security profile mode.
  * `authentication-types=wpa2-psk`: Sets the authentication mode.
  * `eap-methods=passthrough`: Sets the EAP methods
  * `group-encryption=aes-ccm`: Sets the encryption method for the broadcast/multicast frames.
  * `unicast-encryption=aes-ccm`: Sets the encryption method for unicast frames.
  * `wpa2-pre-shared-key="MyPassword123!"`: Sets the pre-shared password for the wireless connection. This value must match on the other device.

**3. Complete MikroTik CLI Configuration Commands**
```mikrotik
/ip address
add address=195.190.61.1/24 interface=wlan-21 network=195.190.61.0

/interface enable wlan-21

/interface wireless
set wlan-21 mode=ap-bridge ssid="pointtopoint" band=2ghz-b/g/n frequency=2412  wireless-protocol=802.11
set wlan-21 country=united-states security-profile=default

/interface wireless security-profiles
set default mode=dynamic-keys authentication-types=wpa2-psk  eap-methods=passthrough group-encryption=aes-ccm  unicast-encryption=aes-ccm  wpa2-pre-shared-key="MyPassword123!"

```

**4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics**

*   **IP Address Overlap:** Ensure the IPs don't conflict with existing networks. Overlapping IPs create major routing and connectivity issues.  This example is on the Class C private IP range, but if using other IP addresses you must be aware of conflicts.
*   **Interface Not Enabled:** Double-check that `wlan-21` (or any other interface you're using) is enabled via `/interface enable wlan-21` or from Winbox UI. If it is not, the interface will not pass any traffic.
*   **Firewall Rules:** If you intend to access the router or pass traffic through, make sure that your firewall settings allow it. Otherwise you may find that your traffic is blocked. See section 10 for more detail on firewall.
*   **Wireless Issues (If using Wireless):** Check the wireless frequency, band, SSID, security settings, etc. Ensure that both devices are using the same settings.

**Example Error Scenario:**

*   **IP address conflict**
    *   Error log message might be: `IP address 195.190.61.1/24 already exists on interface bridge1`
        *   **Fix:** Check the current IP configuration using `/ip address print` and make sure the IP is not assigned to any other interface. If it is, remove the IP or move it to the correct interface.
*   **Interface disabled**
    *   You can check this using `interface print`, where the `E` flag indicates the interface is enabled
    *   If the interface is disabled, it will not be passing any traffic
        *   **Fix:** Run `/interface enable <name>` where name is the name of the disabled interface, or enable in WinBox.
*   **Wireless security mismatch:**
    *   The devices will fail to connect if the wireless password or settings don't match. This can be checked in the RouterOS log, but is also apparent if devices cannot associate with the wireless.
    *   **Fix:** Ensure that the wireless security profile, especially the passphrase, match on both devices.

**Diagnostics:**

*   **`ping`:** Use `/ping 195.190.61.2` to test connectivity. If you cannot ping the remote end, you know to check your configuration.
*   **`traceroute`:** Use `/tool traceroute 195.190.61.2` to track the path, which can help identify routing issues if you have more complex networks.
*  **`torch`**: Use `/tool torch interface=wlan-21` to observe traffic on an interface. This tool is invaluable for diagnosing traffic problems, ensuring the right traffic is going over the interface. This is especially important for complex network setups.
*   **Logs:** Check RouterOS logs using `/log print` for errors. These logs usually contain useful messages such as device connection and disconnection or authentication errors.

**5. Verification and Testing Steps**

1.  **Apply the Configuration:** Either use the CLI commands or use Winbox to apply the same settings.
2.  **Verify IP Address:** Use `/ip address print` to confirm the IP is correctly assigned. The output must show the correct IP, network address, and associated interface.
3.  **Ping:** `ping` the remote router (e.g. `195.190.61.2`).  If ping fails, review the firewall settings and wireless security configuration.
4.  **Traffic Check:** Use `torch` on both routers to ensure traffic is present on the interfaces. This confirms basic connectivity is working at a lower layer of the OSI model.

**6. Related MikroTik-Specific Features, Capabilities, and Limitations**

*   **IP Address Management:** MikroTik allows you to set static IPs, DHCP servers, IP pools, and more complex scenarios with VRF and IPv6, all easily configurable using both Winbox and CLI.
*   **Bridging:**  If you want to connect multiple devices on this network as a single broadcast domain, you can add this interface to a bridge by `interface bridge add name=bridge1`, then `interface bridge port add bridge=bridge1 interface=wlan-21`
*   **Routing:** For more complex networks, MikroTik's routing allows you to use static routing, dynamic protocols like OSPF and BGP, and policy-based routing for very specific routing scenarios.
*   **Firewall:** MikroTik has a very complex firewall, allowing granular control over what traffic flows in and out of the router.
*   **Wireless Options**: MikroTik's wireless interface has many configuration options including a variety of wireless standards and security options.

**Less Common Features Scenarios:**

* **VRF:**  You could create a separate VRF for this subnet, isolating it from your other networks. This is useful in multi-tenant setups or to limit access to certain resources.
    * Example CLI configuration:
        ```mikrotik
        /routing vrf add name=pointtopoint
        /ip address add address=195.190.61.1/24 interface=wlan-21 network=195.190.61.0 vrf=pointtopoint
        /interface set wlan-21 vrf=pointtopoint
        ```
    *   With this configuration, all traffic related to the `pointtopoint` VRF will be isolated.
* **Policy Based Routing:** You could implement policy-based routing such that traffic from a specific source IP or destination IP address will be routed out a different interface.  This is useful in advanced network setups to control traffic flow.

**7. MikroTik REST API Examples**

*   **API Endpoint:** `/ip/address`

*   **Request Method:** `POST` to add an IP, `GET` to list, `PUT` to modify, `DELETE` to remove.

*   **Example Add IP Address (POST Request):**

    *   **Endpoint:** `/ip/address`
    *   **Request Method:** `POST`
    *   **JSON Payload:**

        ```json
        {
        "address": "195.190.61.1/24",
        "interface": "wlan-21",
        "network": "195.190.61.0"
        }
        ```

    *   **Expected Response:** (Successful response 200 OK with a payload containing generated ID or success message).
    * Note: This requires having the RouterOS API enabled. This can be configured using `/ip service`

*   **Example Get IP Addresses (GET Request):**

    *   **Endpoint:** `/ip/address`
    *   **Request Method:** `GET`
    *   **Payload:** (None)
    *   **Expected Response:** JSON payload showing all configured IP addresses, including their IDs, address, interfaces, etc.

        ```json
        [
        {
            ".id": "*1",
            "address": "195.190.61.1/24",
            "interface": "wlan-21",
            "network": "195.190.61.0",
             "actual-interface": "wlan-21"
        },
        {
            ".id": "*2",
            "address": "192.168.88.1/24",
            "interface": "ether1",
            "network": "192.168.88.0",
            "actual-interface": "ether1"
        }
         ]
        ```
    *Note: RouterOS API calls will return data in this format. You must parse this JSON response accordingly.*

*   **Example Update IP Address (PUT Request):**
    *   **Endpoint**: `/ip/address/*1`
        * Note:  The ID is *1 from the response above.
    *   **Request Method**: `PUT`
    *   **JSON Payload**:

        ```json
         {
              "address": "195.190.61.20/24"
          }
        ```
    *  **Expected Response**: Successful response (200 OK) with modified response if modified
*  **Example Delete IP Address (DELETE Request):**
     * **Endpoint**: `/ip/address/*1`
         * Note: The ID is *1 from the response above.
     * **Request Method**: `DELETE`
     * **JSON Payload**: None
     * **Expected Response**: Successful response (200 OK) with no payload

**8. In-Depth Explanations of Core Concepts**

*   **IP Addressing:**
    *   **IPv4:**  We are using IPv4 addresses in this example. Each IP address has two parts: a network portion (defined by subnet mask) and a host portion. The `/24` subnet mask means the first 24 bits identify the network (195.190.61), and the remaining 8 bits identify hosts (1 to 254).
    *   **IPv6:**  While not used in this specific configuration, MikroTik also supports IPv6 for more modern addressing. Example IPv6 Configuration:
        ```mikrotik
        /ipv6 address add address=2001:db8::1/64 interface=wlan-21
        ```

*   **Bridging:** Allows you to treat different interfaces as if they are on the same network. This is not required in this point-to-point setup, but useful for connecting multiple Ethernet interfaces together or for creating a single subnet across multiple interfaces. In MikroTik a bridge is a virtual layer-2 device.

*   **Routing:**  The process of directing traffic between networks. In this example, it is simple, but in larger networks, it requires dynamic routing protocols, and the firewall must understand the routing decisions to make proper access control.
*   **Firewall:** This is the gatekeeper for your network. MikroTik firewalls use a chain system, including input, forward, and output chains. Firewalls protect your router and network, and must be properly configured. For example, you may want to drop all traffic by default, then create rules that pass particular traffic.

**9. Security Best Practices**

*   **Strong Passwords:** Use strong, unique passwords for the router, wireless security, and any other user access.
*   **Disable Unnecessary Services:**  Disable services you don't use, like `telnet`, `api`, or `www` (if you don't need them for administration) using `/ip service disable <service name>`.
*   **Firewall Rules:** Configure robust firewall rules and only allow necessary ports and IPs. Do not open ports to the public unless absolutely required. If you do open them, make sure to secure the services behind those ports.
*   **Wireless Security:** Use strong encryption (WPA2/WPA3) for wireless. Avoid WEP or open wireless. Use strong, unique passwords and consider using WPS or other authentication mechanisms.
*   **RouterOS Updates:** Keep your RouterOS version updated to the latest version to patch known vulnerabilities.
*   **Use SSH:** For remote access always use SSH, not Telnet.  SSH is encrypted and thus safer. Use `/ip service enable ssh` to enable SSH and disable Telnet using `/ip service disable telnet`
*   **Address List:** Use address list in firewall rules, to make configuration and maintenance easier.  This is especially important when you have many access control rules based on IP address or range.
*   **HTTPS:** Use HTTPS rather than HTTP when using WebFig or API.  This is secured using a certificate as described in section 10.

**10. Detailed Explanations and Configuration Examples**

   **IP Addressing (IPv4 and IPv6)**: Covered in prior sections.
   **IP Pools**: IP Pools are used for assigning IP addresses via DHCP server. These are not used in this example, which is point to point. However, for a DHCP configuration, you can configure a pool of IPs, for example:
    ```mikrotik
    /ip pool add name=dhcp-pool ranges=195.190.61.100-195.190.61.200
    ```
     This would create a pool of addresses that a DHCP server can use.
   **IP Routing**: The process by which the network is guided to use a particular path. In this scenario, where we are working with a point-to-point, we are implicitly routing to that single connected subnet. In more complex setups, routing will use either static routes or dynamic routing protocols such as OSPF or BGP. The IP routing table can be displayed using `/ip route print`.
   **IP Settings**: Global IP settings such as ARP, ICMP, TCP settings etc. can be viewed using `/ip settings print` and set using `/ip settings set`.
   **MAC Server**: The MAC server allows you to manage clients who access the router, based on MAC address.  This is not used in our example, but the MAC server can be configured using `/tool mac-server`.
   **RoMON**: Router management over network. This can be configured using `/tool romon`. RoMON uses a special protocol, and is configured on a per-interface basis.
   **WinBox**: MikroTik's GUI management tool. WinBox is a Windows-based application that provides a graphical interface to configure RouterOS routers. Most options accessible via CLI are also available in WinBox.
   **Certificates**: Used for HTTPS and VPN servers. Certificates can be created using `/certificate add name=my-certificate common-name=myrouter.local` then importing a certificate file.
   **PPP AAA**: User authentication for PPP protocols such as PPPoE. This uses a system of profiles and secrets. This will not be covered in detail here.
   **RADIUS**: For centralized authentication. Useful for large networks. This can be configured using `/radius`.
   **User / User groups**: Allows the creation of user accounts for router access. You can create a user using `/user add name=mynewuser group=full password="password123!"`.
   **Bridging and Switching**: Covered earlier.
   **MACVLAN**: Used to create multiple logical interfaces on one physical interface. This can be configured using `/interface macvlan add name=macvlan1 interface=ether1 mac-address=<macaddress>`
   **L3 Hardware Offloading**: Allows RouterOS to use the hardware to process L3 routing, resulting in improved performance. This feature is available on compatible hardware.
   **MACsec**: A standard for securing Ethernet frames at the MAC layer. This is not used in our example, but can be configured in the `/interface ethernet macsec` section.
   **Quality of Service**: Allows traffic shaping. Queues can be added using `/queue simple add`.  A queue is used to limit traffic, for example, if a customer is not paying for a particular bandwidth allocation, the router can limit their throughput via queues.
   **Switch Chip Features**: MikroTik routers using switch chips offer hardware-based switching functionalities, such as VLANs and hardware offload. This is not used here.
   **VLAN**: Used to create logically separated networks. Can be configured using `/interface vlan add name=vlan1 vlan-id=10 interface=ether1`.
   **VXLAN**: A tunneling protocol to create logical networks across different layer 2 domains.
   **Firewall and Quality of Service**: A highly flexible firewall allows granular rules based on connections, addresses, ports and many other filters, while QoS allows the control of traffic flow based on rules or priority.
        *   **Connection tracking**: The stateful firewall uses this mechanism to keep track of the connection state. These can be viewed using `/ip firewall connection print`.
        *   **Firewall**: Consists of a number of chains (input, forward, output) where traffic is evaluated.
        *   **Packet Flow in RouterOS**: Incoming traffic is routed based on routing rules, and evaluated based on firewall rules, NAT rules and queues.
        *   **Queues**: Queues allow traffic shaping.
        *   **Firewall and QoS Case Studies**: Traffic shaping examples based on usage and user prioritization.
        *   **Kid Control**: A common use case where traffic to certain internet addresses or ports can be blocked or limited based on a schedule.
        *   **UPnP**: A protocol that allows network devices to discover each other.
        *   **NAT-PMP**: A protocol similar to UPnP which allows network devices to discover each other and request port mappings from a NAT device.
   **IP Services**: These include DHCP, DNS, SOCKS, Proxy.
        *   **DHCP**: To provide dynamic IP addresses. This is configured using `/ip dhcp-server`.
        *   **DNS**: To resolve hostnames to IP addresses.  This is configured using `/ip dns`.
        *   **SOCKS**: A protocol that can be used as a proxy
        *   **Proxy**: To provide caching and filtering for internet traffic. This can be configured using `/ip proxy`
   **High Availability Solutions**: These include load balancing, bonding, VRRP.
       *  **Load Balancing**: Spreading network traffic across different links
       *   **Bonding**: Using multiple links as a single logical link. This can be done using `/interface bonding`.
       *   **Bonding Examples**: Examples of bonding with different configuration parameters.
       *   **HA Case Studies**: Using bonding and VRRP to establish high availability solutions.
       *   **Multi-chassis Link Aggregation Group**: Combining links between multiple chassis.
       *   **VRRP**: Virtual Router Redundancy Protocol. This can be configured using `/interface vrrp`.
       *   **VRRP Configuration Examples**: Example configurations of VRRP for redundancy.
   **Mobile Networking**: This includes GPS, LTE, PPP, SMS, Dual SIM applications. These are configured in `/interface lte` or `/interface ppp`.
   **Multi Protocol Label Switching - MPLS**: A network routing technique. This includes MPLS Overview, MPLS MTU, Forwarding and Label Bindings, EXP bit and MPLS Queuing, LDP, VPLS, Traffic Eng, MPLS Reference. These can be configured in the `/mpls` section.
   **Network Management**: This includes ARP, Cloud, DHCP, DNS, SOCKS, Proxy, Openflow.
   **Routing**: This includes Routing Protocol Overview, Moving from ROSv6 to v7 with examples, Routing Protocol Multi-core Support, Policy Routing, Virtual Routing and Forwarding - VRF, OSPF, RIP, BGP, RPKI, Route Selection and Filters, Multicast, Routing Debugging Tools, Routing Reference, BFD, IS-IS.  These routing protocols can be added using `/routing ospf` or `/routing bgp`.
   **System Information and Utilities**: This includes Clock, Device-mode, E-mail, Fetch, Files, Identity, Interface Lists, Neighbor discovery, Note, NTP, Partitions, Precision Time Protocol, Scheduler, Services, TFTP.
   **Virtual Private Networks**: These include 6to4, EoIP, GRE, IPIP, IPsec, L2TP, OpenVPN, PPPoE, PPTP, SSTP, WireGuard, ZeroTier. These can be configured using `/interface eoip`, `/interface gre` or `/interface ipsec`.
   **Wired Connections**: Ethernet, MikroTik wired interface compatibility, PWR Line. Ethernet can be configured using `/interface ethernet`
   **Wireless**: WiFi, Wireless Interface, W60G, CAPsMAN, HWMPplus mesh, Nv2, Interworking Profiles, Wireless Case Studies, Spectral scan. Wireless can be configured using `/interface wireless`.
   **Internet of Things**: Bluetooth, GPIO, Lora, MQTT.
   **Hardware**: Disks, Grounding, LCD Touchscreen, LEDs, MTU in RouterOS, Peripherals, PoE-Out, Ports, Product Naming, RouterBOARD, USB Features.
   **Diagnostics, monitoring and troubleshooting**: This includes Bandwidth Test, Detect Internet, Dynamic DNS, Graphing, Health, Interface stats and monitor-traffic, IP Scan, Log, Netwatch, Packet Sniffer, Ping, Profiler, Resource, SNMP, Speed Test, S-RJ10 general guidance, Torch, Traceroute, Traffic Flow, Traffic Generator, Watchdog.
   **Extended features**: Container, DLNA Media server, ROSE-storage, SMB, UPS, Wake on LAN, IP packing.

Let me know if you want more details about a specific section. This is a comprehensive explanation, which was requested.

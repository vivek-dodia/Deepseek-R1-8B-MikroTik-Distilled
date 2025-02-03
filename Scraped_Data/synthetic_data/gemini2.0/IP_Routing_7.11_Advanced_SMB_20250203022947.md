Okay, let's dive deep into this comprehensive MikroTik RouterOS documentation. We'll cover a lot of ground, focusing on your specific subnet and interface while exploring a wide array of MikroTik features and concepts.

**1. Comprehensive Configuration Scenario and Specific MikroTik Requirements**

**Scenario:** We are setting up a small business network using a MikroTik router. The business has a wireless network for internal use and needs to route traffic to and from the internet. We'll configure a specific wireless interface (`wlan-49`) to use the subnet `89.24.104.0/24`. The MikroTik router will be responsible for IP routing, DHCP server for the subnet, and basic firewall for security.

**MikroTik Requirements:**

*   **RouterOS Version:** 7.11 (or 6.48, 7.x)
*   **Network Scale:** SMB
*   **Subnet:** 89.24.104.0/24
*   **Interface Name:** wlan-49
*   **IP Addressing:** Assign a static IP address to wlan-49 within the 89.24.104.0/24 subnet.
*   **DHCP Server:** Provide IP addresses to wireless clients.
*   **Firewall:** Implement basic firewall rules to protect the network.
*   **Routing:** Ensure proper routing to the internet.
*   **Wireless:** Configure basic wireless settings for wlan-49
*   **Security:** Implement basic authentication and encryption settings.

**2. Step-by-Step MikroTik Implementation using CLI with Detailed Explanations**

Let's use the CLI (command-line interface) for the initial configuration.

**Step 1: Enable and Name the Interface**
```mikrotik
/interface wireless enable wlan1
/interface wireless set wlan1 name=wlan-49
```
    *   `/interface wireless enable wlan1`: Enables the wireless interface. Note `wlan1` may be different depending on your hardware.  Check your `/interface wireless print` to determine the correct interface name.
    *   `/interface wireless set wlan1 name=wlan-49`: Renames the interface for clarity.

**Step 2: Assign IP Address**
```mikrotik
/ip address add address=89.24.104.1/24 interface=wlan-49
```
    *   `/ip address add address=89.24.104.1/24 interface=wlan-49`:  Assigns IP address `89.24.104.1` and netmask `/24` to `wlan-49`. `89.24.104.1` is the gateway IP on this subnet.

**Step 3: Configure DHCP Server**

   *   **Create IP Pool:**
```mikrotik
/ip pool add name=dhcp_pool_wlan-49 ranges=89.24.104.10-89.24.104.254
```
        *   `/ip pool add name=dhcp_pool_wlan-49 ranges=89.24.104.10-89.24.104.254`: Creates a pool of IP addresses for the DHCP server to assign.
   *   **Setup DHCP Server:**
```mikrotik
/ip dhcp-server add address-pool=dhcp_pool_wlan-49 interface=wlan-49 lease-time=10m name=dhcp_wlan-49
/ip dhcp-server network add address=89.24.104.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=89.24.104.1
```
        *   `/ip dhcp-server add address-pool=dhcp_pool_wlan-49 interface=wlan-49 lease-time=10m name=dhcp_wlan-49`: Configures the DHCP server on `wlan-49` using the address pool and a lease time of 10 minutes.
        *   `/ip dhcp-server network add address=89.24.104.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=89.24.104.1`: Configures the network settings for DHCP clients, including the default gateway and DNS servers.

**Step 4: Configure Basic Wireless Settings**

```mikrotik
/interface wireless set wlan-49 mode=ap-bridge ssid="MyBusinessWiFi" band=2ghz-b/g/n channel-width=20mhz frequency=2437 security-profile=my-secure-profile
```

*   `/interface wireless set wlan-49 mode=ap-bridge ssid="MyBusinessWiFi" band=2ghz-b/g/n channel-width=20mhz frequency=2437`: Sets basic wireless options - AP mode, SSID, frequency, and band. This is a starting point, you may need to adjust these based on the environment.

*   Create security Profile:
```mikrotik
/interface wireless security-profiles add authentication-types=wpa2-psk mode=dynamic-keys name=my-secure-profile supplicant-identity=MikroTik wpa2-pre-shared-key=StrongPassword
```
        * `/interface wireless security-profiles add authentication-types=wpa2-psk mode=dynamic-keys name=my-secure-profile supplicant-identity=MikroTik wpa2-pre-shared-key=StrongPassword`: Creates security profile with a strong password. **Replace "StrongPassword" with a secure password**.

**Step 5:  Set Up Basic Firewall**
   *   **Allow Established Connections:**

```mikrotik
/ip firewall filter add chain=input connection-state=established,related action=accept comment="Allow established connections"
/ip firewall filter add chain=forward connection-state=established,related action=accept comment="Allow forwarding established connections"
```
    *   These rules allow traffic for connections that the router already knows about.

   *   **Drop Invalid Connections:**

```mikrotik
/ip firewall filter add chain=input connection-state=invalid action=drop comment="Drop invalid connections"
/ip firewall filter add chain=forward connection-state=invalid action=drop comment="Drop invalid forward connections"
```

    *   These rules drop packets that are malformed or otherwise invalid.
   *   **Allow Access to Router from Internal Network:**

```mikrotik
/ip firewall filter add chain=input in-interface=wlan-49 action=accept comment="Allow access to Router from wlan-49"
```

    *   This rule allows access to the router from the internal network
   *   **Drop Other Traffic:**
```mikrotik
/ip firewall filter add chain=input action=drop comment="Drop other input traffic"
/ip firewall filter add chain=forward action=drop comment="Drop other forward traffic"
```
    *   This is a basic deny all rule for all other traffic. You must configure forward rule to allow access to the internet.
*     **Allow Forward to the Internet:**
```mikrotik
/ip firewall nat add chain=srcnat out-interface=<internet-interface-name> action=masquerade comment="Masquerade to the Internet"
/ip firewall filter add chain=forward out-interface=<internet-interface-name> action=accept comment="Allow forwarding to the Internet"
```
        * Replace `<internet-interface-name>` with the actual interface connected to the internet (e.g., `ether1`).
    *   This rule allows devices on your wlan-49 network to forward traffic to the internet
**Step 6:  Routing to internet**
*   **Set Default Gateway:**
```mikrotik
/ip route add dst-address=0.0.0.0/0 gateway=<gateway-ip>
```
    * Replace `<gateway-ip>` with the gateway IP provided by your internet service provider (ISP).

**3. Complete MikroTik CLI Configuration Commands with Relevant Parameters**
Here's a summary of all the CLI commands with detailed explanations:
*   **/interface wireless**

    *   `enable <interface>`: Enables a wireless interface.
    *   `disable <interface>`: Disables a wireless interface.
    *   `set <interface> name=<new_name>`: Renames the interface.
    *   `set <interface> mode=<mode>`: Sets the mode (e.g., ap-bridge, station).
    *   `set <interface> ssid=<ssid>`: Sets the SSID.
    *   `set <interface> band=<band>`: Sets the operating band (e.g., 2ghz-b/g/n, 5ghz-a/n/ac).
    *   `set <interface> channel-width=<width>`: Sets the channel width (e.g., 20mhz, 40mhz).
    *   `set <interface> frequency=<frequency>`: Sets the operating frequency.
    *   `set <interface> security-profile=<profile_name>`: Sets the security profile.

*   **/ip address**

    *   `add address=<ip_address>/<cidr> interface=<interface_name>`: Adds an IP address to an interface.
    *   `remove <number>`: Removes an IP address entry (where number is the index from `/ip address print`).
    *   `set <number> address=<new_ip_address>/<cidr>`: Updates the IP address.

*   **/ip pool**

    *   `add name=<pool_name> ranges=<ip_range>`: Creates an IP address pool.
    *   `remove <number>`: Removes the IP address pool.
    *   `set <number> ranges=<new_ip_range>`: Updates the IP address range.

*   **/ip dhcp-server**

    *   `add name=<server_name> interface=<interface_name> address-pool=<pool_name> lease-time=<time>`: Creates a DHCP server.
    *   `remove <number>`: Removes the DHCP server entry.
    *   `set <number> address-pool=<new_pool_name>`: Updates the DHCP address pool.

*   **/ip dhcp-server network**

    *   `add address=<subnet>/<cidr> gateway=<gateway_ip> dns-server=<dns1>,<dns2>`: Creates a DHCP network configuration.
    *   `remove <number>`: Removes the DHCP network configuration.
    *   `set <number> gateway=<new_gateway_ip>`: Updates the default gateway.

*   **/ip firewall filter**

    *   `add chain=<chain_name> action=<action> comment=<comment> <parameters>`: Adds a firewall rule.
    *   `remove <number>`: Removes a firewall rule.
    *   `set <number> action=<new_action>`: Updates the firewall rule action.
        *   `<chain_name>`: `input`, `output`, or `forward`.
        *   `<action>`: `accept`, `drop`, `reject`.
        *   `<parameters>`: e.g., `in-interface`, `out-interface`, `connection-state`.

*   **/ip firewall nat**

    *   `add chain=<chain_name> action=<action> out-interface=<out_interface> comment=<comment> <parameters>`: Adds a NAT rule.
        *   `<chain_name>`: `srcnat`, `dstnat`.
        *   `<action>`: `masquerade`.
        *   `<parameters>`: e.g., `src-address`, `dst-address`.

*   **/ip route**

    *   `add dst-address=<ip_address>/<cidr> gateway=<gateway_ip>`: Adds a routing entry
    *   `add dst-address=0.0.0.0/0 gateway=<gateway_ip>`: Adds a default gateway

*   **/interface wireless security-profiles**
    * `add name=<profile_name> mode=dynamic-keys authentication-types=<auth_types> wpa2-pre-shared-key=<password>`: Creates a security profile for wireless devices.

**4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics**

*   **Pitfalls:**
    *   **Interface Confusion:**  Mixing up interface names (e.g., `wlan1` vs. `wlan-49`). Always double-check with `/interface print`.
    *   **Firewall Rule Order:** Firewall rules are processed top-down. Incorrect order can block traffic unexpectedly.
    *   **DHCP Conflicts:** Two DHCP servers on the same network can cause issues.
    *   **Incorrect NAT:** Masquerading the wrong traffic or forgetting NAT rules.
    *   **Wireless Channel Overlap**: Make sure channels are not overlapping with other devices or neighbouring networks.

*   **Troubleshooting:**
    *   **Ping:** `ping 89.24.104.1` (verify local connectivity); `ping 8.8.8.8` (verify internet connectivity).
    *   **Traceroute:** `traceroute 8.8.8.8` (check the routing path).
    *   **Torch:** `/tool torch interface=wlan-49` (real-time packet capturing).
    *   **Log:** `/log print` (check logs for errors).
    *   **Packet Sniffer:** `/tool sniffer` (capture packets for detailed analysis).
    *   **Interface Status:** `/interface monitor <interface_name>` (check interface statistics).
    *   **IP Address Conflicts:**  Use `/ip address print` to check for duplicate or incorrect IP addresses.

*   **Error Scenarios:**
    *   **No Internet:**
        *   Check NAT configuration (masquerade).
        *   Verify the default gateway is configured correctly.
        *   Ensure the internet-facing interface has an IP address and is up.
        *   Firewall rules are blocking forward traffic.
    *   **DHCP Issues:**
        *   Check IP pool range.
        *   Verify the DHCP server is enabled and the interface is correct.
        *   Ensure no IP address conflicts in the DHCP address pool.
    *   **Wireless Connection Problems:**
        *   Verify the SSID and password.
        *   Check signal strength.
        *   Make sure channel frequency is not interfering with other networks.
        *   Check Security profile settings

**5. Verification and Testing Steps**
*   **Ping Tests:**
    *   From the MikroTik router: `ping 89.24.104.1`, `ping 8.8.8.8`
    *   From a client connected to `wlan-49`: ping the router's IP, ping an internet address like google.com.
*   **Traceroute:**
    *   From the router: `traceroute 8.8.8.8`
    *   From a client on `wlan-49`: traceroute to an external IP.
*   **Connectivity Test from Client Device:**
    *   Connect a device to `MyBusinessWiFi`.
    *   Verify IP address is obtained via DHCP.
    *   Browse to internet websites.
*   **Wireless Signal Test:**
    *   Use a WiFi analyzer app to verify the signal strength and channel on `wlan-49`.
*   **Firewall Testing:**
    *   Attempt connections blocked by firewall rules to verify they are dropped or rejected. Use `torch` on interfaces and connection tracking `/ip firewall connection print` to identify the firewall filter rule that is impacting the traffic

**6. Related MikroTik-Specific Features, Capabilities, and Limitations**

*   **Less Common Features:**
    *   **VRRP (Virtual Router Redundancy Protocol):** For high availability scenarios, allowing a standby router to take over if the primary fails.
    *   **BGP (Border Gateway Protocol):** For advanced routing in larger networks or when peering with other Autonomous Systems.
    *   **MPLS (Multi-Protocol Label Switching):** Used for traffic engineering and VPNs in larger networks.
    *   **Traffic Shaping with PCQ (Per Connection Queue):** Provides advanced bandwidth management.
    *   **Hotspot:** Provides captive portals for guest networks, often used in public places.
*   **Limitations:**
    *   Hardware limitations can restrict throughput. The router's CPU and RAM can impact performance.
    *   The number of supported interfaces can be limited based on the router model.
    *   Certain advanced features require more processing power.

**7. MikroTik REST API Examples**

*   **Enabling the API**
    *  Enable the API in `/ip service`
    ```mikrotik
    /ip service set api-ssl enabled=yes
    /ip service set api enabled=yes
    ```
    *  Ensure you have a user with api rights:
    ```mikrotik
    /user group add name=api-group policy=api,read,write
    /user add name=api-user group=api-group password=securepassword
    ```
    *   You will need to use this username and password in the following REST API calls

* **API Endpoint:** `https://<router-ip>/rest/interface/wireless` (HTTPS for secure communication)
    * Replace `<router-ip>` with your MikroTik's IP address.

*   **Request Method:** `GET` (to retrieve information)

*   **Example Request (Get Wireless Interfaces):**

```bash
curl -k -u api-user:securepassword -H "Content-Type: application/json"  https://<router-ip>/rest/interface/wireless
```
    *  `-k`: Ignore SSL certificate verification (for testing purposes). In a production environment, configure proper SSL certificates.
    *   `-u api-user:securepassword`: Provide authentication credentials.
    *   `-H "Content-Type: application/json"`:  Specify JSON as the content type.
*   **Expected Response (Example JSON):**
```json
[
    {
        ".id": "*1",
        "name": "wlan-49",
        "mtu": "1500",
        "actual-mtu": "1500",
        "mac-address": "C8:DF:0F:98:74:12",
        "type": "wlan",
        "enabled": true,
        "mode": "ap-bridge",
        "ssid": "MyBusinessWiFi",
        "band": "2ghz-b/g/n",
        "frequency": 2437,
        "channel-width": "20mhz",
        "security-profile": "my-secure-profile"
      },
    {
         ".id": "*2",
         "name": "wlan2",
         "mtu": "1500",
         "actual-mtu": "1500",
         "mac-address": "C8:DF:0F:98:74:13",
         "type": "wlan",
         "enabled": false,
         "mode": "station",
        ...
    }
  ]
```

*   **Request Method:** `PUT` (to modify)

*   **Example Request (Set Wireless SSID):**
```bash
curl -k -u api-user:securepassword -H "Content-Type: application/json" -X PUT -d '{"ssid":"NewSSID"}' https://<router-ip>/rest/interface/wireless/*1
```
   *  `-X PUT`: specify PUT method to modify
   * `-d '{"ssid":"NewSSID"}'`: provide a json payload to update

*   **Expected Response (JSON):**
```json
{
    "message": "updated",
    "id": "*1",
    "name": "wlan-49"
}
```

**8. In-Depth Explanations of Core Concepts**

*   **IP Addressing (IPv4):** Each device on a network requires a unique IP address for communication. IPv4 addresses are 32-bit numbers, typically represented in dotted decimal notation (e.g., 89.24.104.1).  Subnet masks are used to divide IP addresses into network and host portions. In our case `89.24.104.0/24` indicates that the first 24 bits are the network, and the last 8 are for hosts.
*   **IP Pools:** Ranges of IP addresses that DHCP servers use to dynamically assign to devices. They ensure that each device gets a unique address within the specified range.
*   **IP Routing:** The process of forwarding packets between networks based on destination IP addresses. MikroTik uses a routing table that contains destination networks and their corresponding routes.
*   **IP Settings:** Include settings like interface IP addresses, DNS settings, and gateways. They control how the device connects to and communicates with networks.
*   **Bridging:** Joins network segments at the data link layer. MikroTik bridges allow network devices to behave as if they are on the same broadcast domain.
*   **Firewall:** Protects networks from unauthorized access by inspecting network traffic based on configured rules. It can block or allow packets based on source/destination IP, ports, connection states, etc.
*   **Connection Tracking:**  Keeps records of active network connections, facilitating stateful firewall filtering (remembering state of connection and allowing responses automatically).  This is crucial to understanding how traffic flows.
*   **NAT (Network Address Translation):** Modifies IP addresses in network traffic, typically used to allow private networks to access the internet using a single public IP address. Masquerading is a form of NAT commonly used in MikroTik.
* **Why are Specific Commands Used:**
    *   `add address=89.24.104.1/24`: This sets up a specific address and subnet on our `wlan-49` interface for our internal network.
    *   `add address-pool=dhcp_pool_wlan-49`: The pool provides a dynamic address range for assigning to the connected clients.
    *   `chain=input`: Applies a rule to traffic destined *for* the router itself.
    *   `chain=forward`: Applies a rule to traffic *passing through* the router.
    *   `action=masquerade`:  Conceals private network IPs behind the router's public IP, allowing outbound internet access.
    *   `dst-address=0.0.0.0/0`: This is the default route, telling the router to send any traffic not specifically defined to the default gateway.

**9. Security Best Practices Specific to MikroTik Routers**

*   **Strong Passwords:** Always use strong and unique passwords for all users.
*   **Disable Unused Services:** Disable unused services such as `telnet`, `ftp`.
*   **Change Default Ports:** Change default ports for services like `ssh` and `winbox`.
*   **Firewall Rules:** Implement a strong firewall configuration with deny-all policy for the `input` and `forward` chain, then allow traffic that is required.
*   **Enable HTTPS:** Use HTTPS for Winbox and the API for secure communication.
*   **Regular Updates:** Keep RouterOS updated to the latest stable version for security patches.
*   **User Access Control:** Use user groups and permissions to restrict access based on user roles.
*   **Wireless Security:** Always use WPA2/WPA3 encryption and strong pre-shared keys for wireless connections. Consider MAC Address filtering if appropriate.
*   **Remote Access Restrictions:** Restrict remote access to specific IP addresses to prevent unauthorized access from public networks
*   **Disable Default User**: Remove the default `admin` user.

* **Less common security settings:**
   * **RoMON**: Use RoMON with appropriate security settings to monitor/manage your devices
   * **Certificates:** Use TLS Certificates for secure connections to the API and services.
   * **MAC server**: Ensure the MAC Server does not provide services from outside your network

**10. Detailed Explanations and Configuration Examples for MikroTik Topics**
(See the comprehensive lists in the outline above for all the topics)

We'll go into further detail for some specific points here, focusing on how to configure the commands and explaining the trade-offs.
*   **IP Addressing (IPv4 and IPv6)**
    *   **IPv4** (`/ip address`) is the basic IP addressing used in the configuration already discussed. To add IPv6 addresses, you would use the same command structure using IPv6 addresses:

```mikrotik
/ipv6 address add address=2001:db8:1234::1/64 interface=wlan-49
```
         *   Addresses must be in valid IPv6 format
    *   **IPv6** Configuration is very similar to IPv4. IPv6 addresses are 128-bit. RouterOS fully supports IPv6.

*   **IP Pools**
    *   IP Pools are used to define ranges of IP addresses to be used, mainly by DHCP servers, Hotspots, and PPP.
    *   Example of IPv6 Pool:
```mikrotik
/ipv6 pool add name=ipv6_pool_wlan-49 prefix=2001:db8:1234::/64 prefix-length=64
```
          *  The prefix is the IPv6 network prefix, and `prefix-length` is the length of that prefix
*   **IP Routing**
    *   Routing is based on the destination IP of traffic and the routing table in the MikroTik device.
    *   Static routes are manually defined (like we did with the default route):
```mikrotik
/ip route add dst-address=192.168.200.0/24 gateway=192.168.100.2
```
         *   This would send traffic destinted to `192.168.200.0/24` through the device at `192.168.100.2`.
    *   Dynamic routing protocols (e.g., OSPF, BGP) automate route discovery and management.
    *   **Policy Routing** enables traffic to be routed based on parameters other than just the destination IP address. For example, based on the source IP:
```mikrotik
/ip route rule add src-address=10.10.10.0/24 action=lookup-via-gateway table=my_custom_routing_table
/ip route add dst-address=0.0.0.0/0 gateway=192.168.100.1 routing-mark=my_custom_routing_table
```
         *  Traffic from `10.10.10.0/24` will use the routing table `my_custom_routing_table`, which has its own default gateway.
    *   **VRF (Virtual Routing and Forwarding)** allows multiple instances of routing table on the router.  This is useful for segregating traffic.

*   **IP Settings**
    *   Global settings under `/ip settings` control global router behavior.
    *   Examples: TCP timeout settings, whether or not to accept ICMP redirects, or enabling fast path.
    *   These settings are typically left at the default unless you have very specific reasons to change them.

*   **MAC server**
    *   The MAC server allows you to manage devices via their MAC addresses.
    *   It can be accessed via the API or `winbox`
    *   Ensure you disable the MAC server on any interfaces open to the internet for security.
```mikrotik
    /mac-server interface set ether1 disabled=yes
```
*   **RoMON**
     *   RoMON allows secure access to your router from another MikroTik router.
     *   Enabling RoMON will open access to the management plane of the router via the defined interfaces
    ```mikrotik
    /tool romon set enabled=yes
    /tool romon interface add interface=ether1
    ```

*   **WinBox**
    *   Winbox is the graphical tool used for most configuration by users.
    *   To connect, you will need the routers IP and user credentials.
    *   You will be presented with the full range of router configurations options.

*   **Certificates**
    *   Certificates are used for secure communication over TLS, particularly for `https`, and `vpn` tunnels.
    *   You can create, import, and manage certificates under the `/certificate` menu.
    *   Self-signed certificates can be created for testing, but production use should employ certs signed by a Certificate Authority (CA)

*   **PPP AAA**
    *   PPP (Point-to-Point Protocol) AAA (Authentication, Authorization, Accounting) is used for authentication of dial-in connections such as PPPoE, PPTP, L2TP and SSTP
    *   Radius (explained below) is typically used to authenticate those connections.
    *   Basic configuration of PPP server:
```mikrotik
/ppp server add name=pppoe-server service-name=pppoe interface=ether1 max-mru=1492
/ppp secret add name=ppp-user password=strong-ppp-password service=pppoe
/ppp profile add name=pppoe-profile local-address=192.168.1.1 remote-address=pppoe-pool use-encryption=yes dns-server=8.8.8.8,8.8.4.4
/ip pool add name=pppoe-pool ranges=192.168.2.10-192.168.2.200
/ppp server set pppoe-server profile=pppoe-profile
```
       * These commands would set up a very basic pppoe server for incoming connections on `ether1`.

*   **RADIUS**
    *   RADIUS (Remote Authentication Dial-In User Service) is used for centralized authentication, often used in conjunction with AAA.
    *   Configured under `/radius`, RADIUS can provide authentication for users on multiple services like PPP, Hotspot, etc.
```mikrotik
/radius add address=192.168.100.10 secret=radiussecret service=ppp timeout=3
```
         *  This radius server can be referenced later in the PPP config
```mikrotik
/ppp profile set pppoe-profile use-radius=yes
```

*   **User / User groups**
     *   User management is located in `/user` and `/user group`
     *   You can create roles (like API user, full admin) with policies, and assign users to those groups.
     *  This allows for least privilege access

*   **Bridging and Switching**
    *   Bridging `/interface bridge` combines multiple interfaces so they act as a single ethernet segment.
    *   Switching `/interface ethernet switch` controls how traffic is managed at the switch chip level of a physical router. This provides low-level performance
    *   Configuring a basic bridge
```mikrotik
/interface bridge add name=br-lan
/interface bridge port add interface=ether2 bridge=br-lan
/interface bridge port add interface=ether3 bridge=br-lan
```
         *   This bridge will combine `ether2` and `ether3` into a single bridge `br-lan`

*   **MACVLAN**
    *   MACVLAN is a special kind of virtual interface that allows multiple MAC addresses on a single physical interface.  Each MAC VLAN will appear as it's own unique physical connection.
    *   Configuration:
```mikrotik
/interface macvlan add interface=ether2 mac-address=C8:DF:0F:98:74:14 name=macvlan1
```
         * This creates `macvlan1` on `ether2` with a new MAC address.

*   **L3 Hardware Offloading**
    *   Some MikroTik devices support Layer 3 hardware offloading, where routing and NAT processes are handled by dedicated hardware. This significantly increases performance.
    *   Enabling L3 hardware offloading is typically under `/interface ethernet set <interface> hw=yes`

*   **MACsec**
    *   MACsec provides link layer encryption at the ethernet level, increasing security between switches or routers.  This has to be supported on both sides of the connection.
    *   Configuring `MACsec` is a complex process requiring preshared keys or certificates.
```mikrotik
/interface macsec add name=macsec-eth2 parent-interface=ether2 secret=strongmacsecsecret
/interface set macsec-eth2 macsec-on=yes
```

*   **Quality of Service**
    *   QoS ensures that certain traffic gets priority over other traffic, essential for VoIP, video streaming, etc.
    *   MikroTik uses Queues `/queue` and Firewall (to mark traffic).
    *   Basic Queue Configuration
```mikrotik
/queue type add name=my_priority_queue kind=pcq pcq-rate=10M pcq-classifier=dst-address
/queue simple add name=priority_traffic target=192.168.1.0/24 max-limit=20M queue=my_priority_queue
```
         *  This simple queue will prioritize traffic destined for `192.168.1.0/24` to 20Mbps using the `my_priority_queue` which provides fair queuing.
    *   **Packet Flow in RouterOS:** Understanding the chain of events: Incoming Interface -> Input Chain -> Routing Decision -> Forward chain -> NAT -> Output Chain -> Outgoing Interface.

*   **Switch Chip Features**
    *   Many MikroTik devices use a switch chip to handle forwarding and VLAN tagging.
    *   Access under `/interface ethernet switch`
    *   Allows for high performance switching at layer 2.
    *   Specific switch features are dependent on the chip in your MikroTik device.

*   **VLAN**
    *   VLANs (Virtual LANs) allow multiple logical networks to share the same physical infrastructure, allowing for better security and network management.
    *   Configuring a VLAN:
```mikrotik
/interface vlan add name=vlan10 id=10 interface=ether2
/ip address add interface=vlan10 address=192.168.10.1/24
```
    * This will create a VLAN interface on ether2 with the ID of 10 and an IP address on the `192.168.10.0/24` network

*   **VXLAN**
    *   VXLAN is a tunneling protocol that allows to extend Layer 2 network over a layer 3 network.
    *   You have to configure the remote VNI (VXLAN Network Identifier).
```mikrotik
/interface vxlan add name=vxlan-remote vni=1000 interface=ether1 remote-address=192.168.100.10
```

*   **Firewall and Quality of Service (Case Studies, etc.)**
    *   **Firewall Case Study**: Restrict access to the Router web interface from a specific subnet
        *   Create an address list for the allowed subnet:
```mikrotik
/ip firewall address-list add list=allowed_web address=192.168.100.0/24
```
        * Add firewall rule only to allow access from the `allowed_web` address list
```mikrotik
/ip firewall filter add chain=input dst-port=80,443 protocol=tcp in-interface=ether1 src-address-list=!allowed_web action=drop comment="Drop web traffic to router"
```
    *   **Kid Control**: Using time-based firewall rules to restrict access for specific clients.
    *   **UPnP / NAT-PMP**: Provides automatic port forwarding for clients that need to communicate through the router.  It is often disabled for
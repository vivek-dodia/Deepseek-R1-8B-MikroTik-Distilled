Okay, let's dive into a comprehensive MikroTik configuration guide, focusing on the scenario you've provided and expanding to cover a broad range of RouterOS functionalities. This documentation is geared towards an advanced user and covers a lot of ground, from basic IP configurations to complex features like MPLS and advanced routing.

**1. Comprehensive Configuration Scenario and Specific MikroTik Requirements**

**Scenario:**
We are configuring a MikroTik router for a Small Office/Home Office (SOHO) environment. The router will be the gateway for the local network. We need to:

*   Configure a static IPv4 address on the `ether-51` interface within the subnet `84.146.173.0/24`.
*   Explore IPv6 addressing.
*   Set up DHCP server to lease addresses in this subnet to local devices.
*   Implement basic firewall rules for security.
*   Implement QoS.
*   Set up DNS.
*   Explore other advanced features.

**Specific MikroTik Requirements:**

*   RouterOS version: 7.11 (though most settings should also work on 6.48 and later 7.x versions)
*   Hardware: Any MikroTik router capable of running RouterOS 7.11 with at least one interface called `ether-51`.
*   Configuration level: Advanced.
*   Target: SOHO Network.

**2. Step-by-Step MikroTik Implementation (CLI and Winbox)**

**Step 1: Access the Router**

*   **CLI:** Connect to the MikroTik router via SSH or the serial console.
*   **Winbox:** Download and install Winbox, and connect to your router via MAC address or IP address (if already configured).

**Step 2: Configure the IP Address on `ether-51`**

*   **CLI:**
    ```mikrotik
    /ip address
    add address=84.146.173.1/24 interface=ether-51 comment="Static IP for ether-51"
    ```
*   **Winbox:**
    1.  Go to *IP > Addresses*.
    2.  Click the "+" button.
    3.  Enter `84.146.173.1/24` in the "Address" field.
    4.  Select "ether-51" from the "Interface" dropdown.
    5.  Add an appropriate comment in the "Comment" field.
    6.  Click "Apply" and "OK".

    **Explanation:** We assign the IP `84.146.173.1` with a `/24` subnet mask to the interface `ether-51`. This means that valid IP range for the network is `84.146.173.1-84.146.173.254`. `84.146.173.0` is the network address and `84.146.173.255` is the broadcast address.

**Step 3: Configure an IP Pool**

*   **CLI:**
    ```mikrotik
    /ip pool
    add name=dhcp_pool ranges=84.146.173.10-84.146.173.200
    ```
*   **Winbox:**
    1.  Go to *IP > Pool*.
    2.  Click the "+" button.
    3.  Enter `dhcp_pool` in the "Name" field.
    4.  Enter `84.146.173.10-84.146.173.200` in the "Ranges" field.
    5.  Click "Apply" and "OK".

    **Explanation:** We create a pool of IP addresses to be used by the DHCP server, for the range `84.146.173.10` to `84.146.173.200`.

**Step 4: Set up DHCP Server**

*   **CLI:**
    ```mikrotik
    /ip dhcp-server
    add address-pool=dhcp_pool disabled=no interface=ether-51 name=dhcp_server
    /ip dhcp-server network
    add address=84.146.173.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=84.146.173.1
    ```
*   **Winbox:**
    1.  Go to *IP > DHCP Server*.
    2.  Click the "+" button in the "DHCP Server" tab.
    3.  Choose `ether-51` from the "Interface" dropdown.
    4.  Enter `dhcp_server` in the "Name" field.
    5.  Select `dhcp_pool` from the "Address Pool" dropdown.
    6.  Click "Apply"
    7.  Go to "Networks" tab, click "+".
    8.  Enter `84.146.173.0/24` in the "Address" field.
    9.  Enter `84.146.173.1` in the "Gateway" field.
    10. Enter `8.8.8.8,8.8.4.4` in "DNS Server" field.
    11. Click "Apply" and "OK".

    **Explanation:** We create a DHCP server on the `ether-51` interface that uses the `dhcp_pool` for IP addresses, it provides the default gateway (`84.146.173.1`) and DNS servers.

**Step 5: Basic Firewall Configuration**

*   **CLI:**
    ```mikrotik
    /ip firewall filter
    add chain=input connection-state=established,related action=accept comment="Accept established and related connections"
    add chain=input protocol=icmp action=accept comment="Allow ICMP"
    add chain=input in-interface=ether-51 action=drop comment="Drop other input from ether-51"
    add chain=forward connection-state=established,related action=accept comment="Accept established and related forwarding"
    add chain=forward action=drop comment="Drop other forward traffic"
    /ip firewall nat
    add chain=srcnat out-interface=ether-51 action=masquerade comment="NAT outbound traffic"
    ```
*   **Winbox:**
    1.  Go to *IP > Firewall*.
    2.  Go to "Filter Rules" tab:
    3.  Add rules for input chain (accept established, ICMP, and drop other).
    4.  Add rules for forward chain (accept established, drop other).
    5.  Go to "NAT" tab, add NAT rule for masquerading.

    **Explanation:** This setup is the minimum. The input chain accepts already established connections and ICMP, and drops other incoming connections. The forward chain accepts only established and related forward traffic, dropping everything else. We also create a NAT rule that will masquerade internal IP addresses behind the public IP address of the ether-51 interface for outbound communication.

**Step 6:  Test the network**

1. Connect a client device to the network (connected on any of the LAN interfaces).
2. Verify that it receives a valid IP from our pool.
3. Verify that the device can access the internet, this verifies the NAT configuration.
4. Ping devices on the internet using `ping 8.8.8.8` from a client device on the local network.
5. Test using `traceroute 8.8.8.8` from a client device on the local network.
6. From the MikroTik terminal try to ping `ping 8.8.8.8` to verify internet connectivity.

**3. Complete MikroTik CLI Configuration Commands**

Here's the consolidated CLI configuration:

```mikrotik
/ip address
add address=84.146.173.1/24 interface=ether-51 comment="Static IP for ether-51"
/ip pool
add name=dhcp_pool ranges=84.146.173.10-84.146.173.200
/ip dhcp-server
add address-pool=dhcp_pool disabled=no interface=ether-51 name=dhcp_server
/ip dhcp-server network
add address=84.146.173.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=84.146.173.1
/ip firewall filter
add chain=input connection-state=established,related action=accept comment="Accept established and related connections"
add chain=input protocol=icmp action=accept comment="Allow ICMP"
add chain=input in-interface=ether-51 action=drop comment="Drop other input from ether-51"
add chain=forward connection-state=established,related action=accept comment="Accept established and related forwarding"
add chain=forward action=drop comment="Drop other forward traffic"
/ip firewall nat
add chain=srcnat out-interface=ether-51 action=masquerade comment="NAT outbound traffic"
/ip dns
set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
```

**4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics**

**Pitfalls:**

*   **Incorrect Interface Names:** Double-check interface names, especially if you have a complex setup.
*   **Conflicting IP Addresses:** Ensure no address conflicts with existing routers or devices.
*   **Firewall Issues:** Overly restrictive rules can block needed traffic, or the lack of rules can expose your network to vulnerabilities.
*   **DHCP Conflicts:** Make sure DHCP server is not enabled on another router in your network.
*   **Incorrect NAT configuration:** Incorrect nat rules can block internet access.

**Troubleshooting:**

*   **`ping`:** Use `ping` in the MikroTik terminal to check basic connectivity, for example `ping 8.8.8.8`.
*   **`traceroute`:** Use `traceroute` for diagnosing routing issues, for example `traceroute 8.8.8.8`.
*   **`torch`:** A powerful tool to monitor traffic on interfaces, for example `/tool torch interface=ether-51`.
*   **`/system resource print`:** Check system resources (CPU, memory).
*   **`/log print`:** Examine system logs for errors or warnings.
*   **`/interface ethernet monitor ether-51 once`:** Monitor interface statistics.
*   **Winbox Tools:** Winbox provides monitoring tools (Traffic, Resources, etc.).

**Error Scenarios:**

*   **No IP address assigned:**
    *   **Problem:** The DHCP server is misconfigured or has run out of leases.
    *   **Solution:** Check DHCP server settings, and increase the IP address range if necessary, check log files on the router using `/log print`.
*   **Cannot access the internet:**
    *   **Problem:**  NAT rules are incorrect or missing, check firewall settings using `/ip firewall filter print` or `/ip firewall nat print`.
    *   **Solution:** Verify that the srcnat rule is active and is using the correct interface. Check routing using `/ip route print`.
*   **No DNS resolution:**
    *   **Problem:** DNS settings are incorrect, check `/ip dns print`.
    *   **Solution:** Check the DNS server addresses and if remote requests are allowed.

**5. Verification and Testing Steps**

*   **Ping Test:** From the MikroTik terminal, `ping 8.8.8.8`.
*   **Traceroute Test:** From the MikroTik terminal, `traceroute 8.8.8.8`.
*   **DHCP Client Test:** Connect a device to the network and verify it gets an IP from `84.146.173.10` through `84.146.173.200`.
*   **Web Access Test:** From a client connected to the local network, verify access to websites.
*   **Traffic Monitor:** Use Winbox's *Tools > Traffic Monitor* or CLI's `/tool torch interface=ether-51` to see real-time traffic.

**6. Related MikroTik-Specific Features, Capabilities, and Limitations**

**Less Common Features Examples:**

*   **MAC server:** MAC Server allows connecting to the router via MAC address, even if IP is not configured on the interface.
    ```mikrotik
    /tool mac-server
    print
    /tool mac-server set allowed-interface=ether-51
    ```
*   **RoMON:**  MikroTik Router Management Overlay Network (RoMON) is used for centralized management of multiple routers.
    ```mikrotik
     /tool romon
     set enabled=yes
     /tool romon print
    ```
*   **Certificates:**  For secure HTTPS access or VPNs.
    ```mikrotik
    /certificate print
    ```
*   **L3 Hardware Offloading:** Hardware acceleration of routing can be enabled.
    ```mikrotik
    /interface ethernet print detail
    /interface ethernet set l3-hw-offload=yes [find name="ether-51"]
    ```
    **Note:**  Not all hardware supports L3 offload.
*   **MACsec:** For data security over ethernet links (advanced).
    ```mikrotik
    /interface ethernet macsec print
    ```
*   **VXLAN:** Virtual Extensible LAN, for creating overlays.
    ```mikrotik
    /interface vxlan print
    ```

**7. MikroTik REST API Examples**

**Enable the API (if not enabled):**
```mikrotik
/ip service enable api
/ip service enable api-ssl
```
**NOTE:** By default API access is only available from 127.0.0.1. To allow API access from an IP address you must change the `/ip service` rules. See the MikroTik API documentation for details.

**API Endpoint:** `https://<router-ip>/rest/ip/address` (using HTTPS for secure access)
**Authentication:** Authentication is done by using a valid session ID or via basic authentication. For this example we'll use basic auth.

**Example: Get IP Addresses (GET)**

**Request (using curl):**
```bash
curl -k -u <admin_user>:<admin_password> https://<router-ip>/rest/ip/address
```

**Expected Response (JSON):**
```json
[
  {
    "id": "*1",
    "address": "84.146.173.1/24",
    "interface": "ether-51",
    "network": "84.146.173.0",
    "actual-interface": "ether-51",
    "invalid": "false",
    "dynamic": "false"
   }
]
```

**Example: Add an IP Address (POST)**

**Request (using curl):**
```bash
curl -k -u <admin_user>:<admin_password> -H "Content-Type: application/json" -X POST -d '{ "address": "84.146.173.2/24", "interface": "ether-51"}' https://<router-ip>/rest/ip/address
```
**Expected Response (JSON) upon success:**
```json
{"message": "added"}
```

**Example: Delete an IP Address (DELETE)**
First we need the id of the address to remove:
```bash
curl -k -u <admin_user>:<admin_password>  https://<router-ip>/rest/ip/address
```
The response will include an `id`. For example `"*1"`. Then we use that id in a `DELETE` request.
```bash
curl -k -u <admin_user>:<admin_password> -X DELETE https://<router-ip>/rest/ip/address/*1
```
**Expected Response (JSON) upon success:**
```json
{"message": "removed"}
```

**NOTE:** Replace `<admin_user>`, `<admin_password>`, and `<router-ip>` with your router's credentials and IP address.

**8. In-Depth Explanations of Core Concepts**

*   **Bridging:** Combines interfaces at Layer 2 (Ethernet), creating a single broadcast domain.
    *   *Why:* For switching, VLANs. Not used in this example directly, but fundamental for many MikroTik configurations.
    ```mikrotik
    /interface bridge
    add name=bridge1
    /interface bridge port
    add bridge=bridge1 interface=ether1
    add bridge=bridge1 interface=ether2
    ```

*   **Routing:** Forwarding packets based on Layer 3 (IP) addresses.
    *   *Why:* Directing traffic between subnets and to the internet.
    *   Routing Table: `/ip route print`.
    *   Static Routes: `/ip route add dst-address=0.0.0.0/0 gateway=84.146.173.x`.
    *   Dynamic Routing: OSPF, BGP, etc.

*   **Firewall:** Controls network traffic based on rules.
    *   *Why:* Securing the network, access control.
    *   Chains: Input, Forward, Output.
    *   Connection Tracking: Remember connection states.
    *   NAT: Network Address Translation.

*   **IP Pools:** Groups of IP addresses for specific purposes.
    *   *Why:* Dynamic address allocation via DHCP.

*   **DHCP:** Dynamic Host Configuration Protocol.
    *   *Why:* Automates IP address assignment.

**9. Security Best Practices Specific to MikroTik Routers**

*   **Change Default Credentials:** Always change the default admin password.
*   **Disable Unused Services:** Disable API, telnet, or other services you don't need.
    ```mikrotik
    /ip service disable telnet
    /ip service disable api
    ```
*   **Use Strong Passwords:** Employ strong, unique passwords for all user accounts.
*   **Secure Winbox Access:** Limit access to Winbox via IP or MAC address rules in the firewall.
*   **Update RouterOS:** Keep your router up to date with the latest RouterOS version for security patches.
*   **Firewall Rules:** Properly configure your firewall, consider using address lists to group IPs, drop all unneeded traffic.
    ```mikrotik
    /ip firewall address-list
    add list=allowed_admin_ips address=192.168.88.0/24
    /ip firewall filter
    add chain=input in-interface=ether-51 src-address-list=!allowed_admin_ips action=drop comment="Drop non-authorized IP addresses"
    ```
*   **Avoid Default Ports:** Use custom ports for remote access (e.g. use a different port than 22 for SSH, and change Winbox port).
*   **Use HTTPS/TLS for API Access:** Always use the HTTPS protocol for API access and never use the plain HTTP protocol. Also if you need remote access use VPN.
*   **Limit remote access:** Do not expose any sensitive service to the internet.

**10. Detailed Explanations and Configuration Examples**

This section will go over each of the topics you've asked, using the current setup as our base.

**IP Addressing (IPv4 and IPv6)**

* **IPv4:** We've already configured this with the `84.146.173.1/24` address. You can add multiple addresses to an interface, for example `/ip address add address=84.146.173.2/24 interface=ether-51`.
* **IPv6:**
    * Obtain an IPv6 address if your provider provides one. This can be done using DHCPv6 or static addressing.
    * Enable IPv6:
    ```mikrotik
    /ipv6 settings set disable-ipv6=no
    ```
    * Enable DHCPv6 client on your external interface:
    ```mikrotik
    /ipv6 dhcp-client
    add interface=ether-51 request=address,prefix pool-name=ipv6_pool
    ```
    * Use IPv6 address from your provider or configure a static IPv6 address.
    ```mikrotik
    /ipv6 address
    add address=2001:db8::1/64 interface=ether-51
    ```
    * You can also configure a `::/64` IPv6 range using prefix delegation and assign it to your LAN interface:
    ```mikrotik
    /ipv6 pool
    add name=ipv6_pool prefix=2001:db8::/64
    /ipv6 address
    add address=2001:db8::1/64 interface=ether-52 from-pool=ipv6_pool
    /ipv6 nd
    set  [find interface="ether-52"] advertise-dns=yes advertise-other-config=no
    ```
    This assumes `ether-52` is an internal interface.
    * Configure firewall for IPv6.
      * Allow established and related input/forward:
      ```mikrotik
      /ipv6 firewall filter
      add chain=input connection-state=established,related action=accept
      add chain=forward connection-state=established,related action=accept
      ```
     * Allow ICMPv6:
      ```mikrotik
      /ipv6 firewall filter
      add chain=input protocol=icmpv6 action=accept
      ```
     * Block all other forward traffic:
      ```mikrotik
      /ipv6 firewall filter
      add chain=forward action=drop
      ```
     * Block all other input traffic on `ether-51`:
      ```mikrotik
      /ipv6 firewall filter
      add chain=input in-interface=ether-51 action=drop
      ```
    * Remember to enable IPv6 forward:
    ```mikrotik
    /ipv6 settings set forwarding=yes
    ```

**IP Pools**

* Already covered, but you can create multiple pools with different ranges. For example, a separate pool for a guest network, `/ip pool add name=guest_pool ranges=192.168.100.10-192.168.100.200`.
* DHCP servers use pools to lease IP addresses.

**IP Routing**

*   **Static Routes:**
    ```mikrotik
    /ip route
    add dst-address=0.0.0.0/0 gateway=84.146.173.x comment="Default Route to internet"
    ```
    Replace `84.146.173.x` with the gateway IP address.
*   **Dynamic Routing (OSPF):**
    ```mikrotik
    /routing ospf instance
    add name=ospf1 router-id=1.1.1.1
    /routing ospf area
    add instance=ospf1 area-id=0.0.0.0
    /routing ospf interface
    add instance=ospf1 interface=ether-52
    ```

*   **Dynamic Routing (BGP):**

```mikrotik
/routing bgp instance
add as=65000 name=bgp1 router-id=1.1.1.1
/routing bgp peer
add instance=bgp1 remote-address=192.168.100.2 remote-as=65001
```
*   **Policy-Based Routing:** Used for routing based on specific criteria.
    ```mikrotik
    /ip route rule
    add dst-address=192.168.10.0/24 action=lookup-only-in-table table=vpn
    /ip route
    add dst-address=0.0.0.0/0 gateway=192.168.1.1 routing-mark=vpn table=vpn
    ```
*   **Virtual Routing and Forwarding (VRF):** Used to create separate routing tables.
    ```mikrotik
    /ip vrf
    add name=vpn route-distinguisher=100:1
    /ip route
    add dst-address=0.0.0.0/0 gateway=192.168.1.1 routing-mark=vpn vrf=vpn
    ```

**IP Settings**

*   Global IP settings: `/ip settings print`.
*   Change TCP/UDP settings, etc., use `/ip settings set`

**MAC Server**

*   Covered before. Enables Winbox connection via MAC address. This is done via `/tool mac-server`.

**RoMON**

*   Covered before. Use it to manage multiple routers. This is done via `/tool romon`.

**WinBox**

*   GUI tool, used to connect to and configure MikroTik routers. Use `/ip service print` to change Winbox port and allowed addresses.

**Certificates**

*   For HTTPS access and secure VPNs. Use `/certificate print` to verify the installed certificates and to create new certificates using `/certificate add`.

**PPP AAA**

*   For authentication in PPP based interfaces (PPPoE, L2TP).
   ```mikrotik
    /ppp profile
    add name=myprofile local-address=192.168.200.1 remote-address=192.168.200.2
    /ppp secret
    add name=user1 password=password1 profile=myprofile
   ```

**RADIUS**

*   For centralized authentication. Use `/radius print` and `/radius add` to configure RADIUS servers and parameters.

**User / User Groups**

*   Managing user accounts in MikroTik.
    ```mikrotik
    /user
    add name=new_user password=new_password group=full
    /user group
    add name=limited policy=read,test
    ```

**Bridging and Switching**

*   Already covered but it includes VLANs, and STP. For example:
    ```mikrotik
    /interface bridge vlan
    add bridge=bridge1 tagged=ether-51 vlan-id=10
    /interface bridge vlan
    add bridge=bridge1 tagged=ether-52 vlan-id=20
    ```

**MACVLAN**

*   Virtual interfaces on the same physical interface. Can be used to create multiple networks on a single interface with different MAC addresses.
    ```mikrotik
    /interface macvlan
    add interface=ether-51 mac-address=02:00:00:00:00:01 name=macvlan1
    ```
**L3 Hardware Offloading**
*   Already covered, but can reduce CPU usage. See `/interface ethernet print detail` and `/interface ethernet set l3-hw-offload`

**MACsec**
*   Security for ethernet links. Use `/interface ethernet macsec print` and `/interface ethernet macsec add` to see and configure settings.

**Quality of Service**

*   **Simple Queues:** Use `/queue simple print` and `/queue simple add` to see and configure bandwidth control on a per-ip/interface basis.
    ```mikrotik
    /queue simple
    add max-limit=10M/10M name=limit-to-10M target=192.168.88.0/24
    ```
*   **Queue Trees:** Provides more control and is configured via `/queue tree print` and `/queue tree add`.
    ```mikrotik
    /queue tree add name=upload parent=global-out max-limit=10M
    /queue tree add name=download parent=global-in max-limit=10M
    ```
*   **HTB:** Hierarchical Token Bucket. More complex for granular control. Configured via `/queue tree`.
*   **QoS and Traffic Shaping:** The key is to use simple queues for simple tasks and queue trees for advanced configuration.
    * **Priority:** Can be set using the `priority` parameter in queues.
    * **Bursts:** Allow for short periods of higher bandwidth.
*   **PCQ:** Per Connection Queuing, based on source/destination address or port for fair bandwidth sharing between connections.

**Switch Chip Features**

*   Some MikroTik devices contain hardware switches that can do VLAN and wire-speed switching.
   * Configuration is usually done in `/interface ethernet switch`.

**VLAN**

*   Virtual LANs. Use `/interface vlan print` and `/interface vlan add` for configuration.
    ```mikrotik
    /interface vlan
    add name=vlan10 vlan-id=10 interface=ether-52
    ```

**VXLAN**
*   Virtual Extensible LAN, used to create layer-2 overlays on layer-3 networks.
    ```mikrotik
    /interface vxlan
    add name=vxlan1 vni=1000 interface=ether-51 remote-address=10.1.1.20
    ```

**Firewall and Quality of Service**

*   **Connection Tracking:** Key to firewall rule efficiency, done automatically by the router.
*   **Firewall:**
    * Filter Rules: Input, Forward, Output, see `/ip firewall filter`.
    * NAT: For network address translation, see `/ip firewall nat`.
    * Mangle: For packet marking for QoS, see `/ip firewall mangle`.
    * Address lists: For easy grouping of IP addresses, see `/ip firewall address-list`.
    * Layer7 filters: To filter specific protocols or application, see `/ip firewall layer7-protocol`.
*   **Packet Flow in RouterOS:** Input, Output, Forward chains with different logic. See MikroTik documentation for detailed flow.
*   **Queues:** For bandwidth management (simple queues, queue tree) as covered above.
*   **Case Studies:** Prioritize certain traffic like VoIP, limit bandwidth for downloads, etc.
*   **Kid Control:** Can use firewall rules based on IP address and time schedule to filter or disable access.
*   **UPnP:** Universal Plug and Play. Can be enabled for some devices to open ports automatically. Consider security implications. Use `/ip upnp print` and `/ip upnp set`.
*   **NAT-PMP:** NAT Port Mapping Protocol, use `/ip nat-pmp print` and `/ip nat-pmp set`.

**IP Services (DHCP, DNS, SOCKS, Proxy)**

*   **DHCP:** Covered previously, but check `/ip dhcp-server` and `/ip dhcp-server network`.
*   **DNS:** See `/ip dns`, configure servers and enable cache.
    * Example:
    ```mikrotik
    /ip dns set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
    ```
    * **DNS Cache:** MikroTik uses a built-in DNS cache to speed up queries.
*   **SOCKS:** Create a SOCKS proxy using `/ip socks print` and `/ip socks set`.
    * SOCKS proxy is generally used for accessing networks behind firewalls.
    ```mikrotik
    /ip socks set enabled=yes
    ```
*   **Proxy:** Configure a HTTP/HTTPS proxy using `/ip proxy print` and `/ip proxy set`.
    * You can also configure a transparent proxy, to intercept traffic without explicit proxy settings on the clients.
    ```mikrotik
    /ip proxy set enabled=yes
    ```

**High Availability Solutions**

*   **Load Balancing:** Use multiple WAN interfaces and balance traffic based on load. Use the `/routing` section and policies to implement this.
    * You can configure it using static routes, ECMP, or with dynamic routing protocols.
*   **Bonding:** Aggregate multiple Ethernet interfaces into a single logical interface for redundancy or higher speed. See `/interface bonding`.
    ```mikrotik
    /interface bonding
    add mode=802.3ad name=bond1 slaves=ether1,ether2
    /ip address
    add address=192.168.10.1/24 interface=bond1
    ```
*   **Bonding Examples:** Active-backup (failover), balance-alb (adaptive load balancing).
*   **HA Case Studies:** Router failover, redundant links.
*   **Multi-chassis Link Aggregation Group (MLAG):** More complex and used on larger networks.
*   **VRRP:** Virtual Router Redundancy Protocol for failover.
    ```mikrotik
    /interface vrrp
    add interface=ether-51 priority=100 vrid=1 virtual-address=192.168.10.10/24
    /interface vrrp
    add interface=ether-51 priority=90 vrid=1 virtual-address=192.168.10.10/24
    ```
*   **VRRP Configuration Examples:** Master/backup setup.

**Mobile Networking**

*   **GPS:** Track the router's location, use `/system gps print`.
*   **LTE:** Use built-in or USB LTE modems, check `/interface lte print`.
    ```mikrotik
    /interface lte apn
    add apn=your_apn_name interface=lte1
    ```
*   **PPP:** Point-to-Point Protocol, use `/interface ppp print` and `/interface ppp add` for PPPoE or PPP.
*   **SMS:** Sending/receiving SMS via an LTE modem, see `/tool sms`.
    ```mikrotik
    /tool sms send lte1 message="Test SMS" phone-number="+11231231234"
    ```
*   **Dual SIM Application:** Automatic or manual failover on dual-SIM LTE devices, use `/interface lte print` for status.

**Multi Protocol Label Switching - MPLS**

*   **MPLS Overview:** Data forwarding using labels rather than IP addresses.
*   **MPLS MTU:** Maximum Transmission Unit, configure if needed in `/interface print detail`.
*   **Forwarding and Label Bindings:** Use `/mpls label print`, and `/mpls interface print` to see how labels are assigned.
*   **EXP bit and MPLS Queuing:** For traffic prioritization using MPLS.
*   **LDP:** Label Distribution Protocol, used to assign and negotiate labels using `/mpls ldp print` and `/mpls ldp add`.
    ```mikrotik
    /mpls ldp
    add interface=ether-51 transport=tcp
    /mpls ldp print
    ```
*   **VPLS:** Virtual Private LAN Service for point-to-multipoint Layer 2 tunnels. `/mpls vpls print` and `/mpls vpls add`.
     ```mikrotik
     /mpls vpls
     add name=vpls1 interface=ether-51 remote-peer=10.1.1.20 vpls-id=100:1
     ```
*   **Traffic Engineering:** Using MPLS TE to manage traffic flow on a network, use `/mpls traffic-eng print` and `/mpls traffic-eng add`.
*   **MPLS Reference:** MikroTik documentation for deep dive into MPLS.

**Network Management**

*   **ARP:** Address Resolution Protocol, see `/ip arp print`.
*   **Cloud:** Use MikroTik Cloud for management and dynamic DNS using `/ip cloud print` and `/ip cloud set`.
*   **DHCP:** Covered, see `/ip dhcp-server`.
*   **DNS:** Covered, see `/ip dns`.
*   **SOCKS:** Covered, see `/ip socks`.
*   **Proxy:** Covered, see `/ip
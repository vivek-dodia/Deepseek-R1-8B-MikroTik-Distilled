Okay, let's dive into a comprehensive exploration of IP addressing and related concepts on MikroTik RouterOS, tailored for an expert audience and focused on the specified scenario.

## Comprehensive IP Addressing & Networking on MikroTik RouterOS (v7.12)

**Configuration Level:** Expert
**Network Scale:** ISP
**Subnet:** 102.55.83.0/24
**Interface:** `bridge-56`

### 1. Configuration Scenario and MikroTik Requirements

**Scenario:** We are configuring a MikroTik router within an ISP environment. Our primary goal is to provide network access using the `102.55.83.0/24` subnet on the `bridge-56` interface. We'll also cover essential aspects like IP pools for DHCP, static IPs, IPv6, and related network management tasks.

**MikroTik Requirements:**

-   RouterOS version 7.12 or higher. (Also covers 6.48, and other 7.x versions where the commands are compatible.)
-   A pre-existing bridge interface named `bridge-56`.
-   Knowledge of basic network concepts (IP addressing, subnets, routing).
-   Access to the router via CLI (SSH or console) or Winbox.

### 2. Step-by-Step MikroTik Implementation

**Step 1: Accessing the MikroTik Router:**

   - Connect to the MikroTik router via SSH, console, or Winbox.
   - Log in using your admin credentials.

**Step 2: Configuring IPv4 Address on `bridge-56`:**

   - Using the CLI:

   ```mikrotik
   /ip address
   add address=102.55.83.1/24 interface=bridge-56 comment="Main IPv4 Address on bridge-56"
   ```
   - **Explanation**: This command adds the IPv4 address `102.55.83.1/24` to the `bridge-56` interface. The `/24` defines the subnet mask (255.255.255.0).

   - Using Winbox:
     - Navigate to *IP -> Addresses*.
     - Click the "+" button.
     - In the *Address* field, enter `102.55.83.1/24`.
     - In the *Interface* drop-down, select `bridge-56`.
     - Optionally, add a *Comment*.
     - Click *Apply* and *OK*.

**Step 3: Creating an IP Pool for DHCP:**

   - Using the CLI:
   ```mikrotik
   /ip pool
   add name=dhcp_pool_56 ranges=102.55.83.100-102.55.83.200 comment="DHCP pool for bridge-56"
   ```
    - **Explanation**: This command creates an IP pool named `dhcp_pool_56` with the IP address range of `102.55.83.100-102.55.83.200`. These IP addresses will be assigned to devices through DHCP.

   - Using Winbox:
       - Navigate to *IP -> Pool*.
       - Click the "+" button.
       - Enter `dhcp_pool_56` for *Name*.
       - In the *Ranges* field, enter `102.55.83.100-102.55.83.200`.
       - Add a comment if required.
       - Click *Apply* and *OK*.

**Step 4: Setting up a DHCP Server:**

   - Using the CLI:
   ```mikrotik
   /ip dhcp-server
   add name=dhcp_server_56 interface=bridge-56 address-pool=dhcp_pool_56 authoritative=yes lease-time=1d disabled=no comment="DHCP server for bridge-56"
   ```
   - **Explanation**: This command creates a DHCP server named `dhcp_server_56` associated with the `bridge-56` interface. It uses the previously created `dhcp_pool_56`, is set to `authoritative` ( meaning it will provide DHCP responses), has a lease time of 1 day, and is enabled.

   - Using Winbox:
       - Navigate to *IP -> DHCP Server*.
       - Click the "+" button.
       - Choose a *Name* e.g. `dhcp_server_56`.
       - In the *Interface* drop-down, select `bridge-56`.
       - In the *Address Pool* drop-down, select `dhcp_pool_56`.
       - Select the authoritative checkbox to enable it.
       - Set lease-time to e.g. 1d
       - Make sure that enabled checkbox is selected.
       - Add a comment if required.
       - Click *Apply* and *OK*.

**Step 5: Configuring DHCP Network settings:**

   - Using the CLI:
   ```mikrotik
    /ip dhcp-server network
   add address=102.55.83.0/24 gateway=102.55.83.1 dns-server=8.8.8.8,8.8.4.4 comment="DHCP Network settings for bridge-56"
   ```
   - **Explanation**: This command adds network settings for the DHCP server.  Specifically, it provides clients with the network address `102.55.83.0/24`, a default gateway at `102.55.83.1`, and DNS servers at `8.8.8.8` and `8.8.4.4`.

   - Using Winbox:
      - Navigate to *IP -> DHCP Server -> Networks tab*.
      - Click the "+" button.
      - In the *Address* field, enter `102.55.83.0/24`.
      - In the *Gateway* field, enter `102.55.83.1`.
      - In the *DNS Server* field, enter `8.8.8.8,8.8.4.4`.
      - Add a comment if required.
      - Click *Apply* and *OK*.

**Step 6: (Optional) Configuring Static IP Address Mapping**

    - If some devices need static IP, we can do that as well.
    - Using the CLI:
        ```mikrotik
        /ip dhcp-server lease
        add mac-address=AA:BB:CC:DD:EE:FF address=102.55.83.50 server=dhcp_server_56 comment="Static IP for device with MAC address AA:BB:CC:DD:EE:FF"
        ```
        - **Explanation:** This command sets up a static IP address (`102.55.83.50`) for the device with a MAC address of `AA:BB:CC:DD:EE:FF` from within the DHCP server `dhcp_server_56`.

    - Using Winbox:
        - Navigate to *IP -> DHCP Server -> Leases tab*.
        - Click the "+" button.
        - Enter the *MAC address* of the device in the MAC Address field e.g. `AA:BB:CC:DD:EE:FF`.
        - Enter the static IP address you need in *Address* field e.g. `102.55.83.50`.
        - Select server `dhcp_server_56` from the drop down.
        - Add a comment if required.
        - Click *Apply* and *OK*.

**Step 7: Basic IPv6 Addressing (Optional)**

- To add IPv6 addressing.
   - Using the CLI:
       ```mikrotik
       /ipv6 address
       add address=2001:db8::1/64 interface=bridge-56 comment="IPv6 Address on bridge-56"
       ```
    - **Explanation:** This adds an IPv6 address to the bridge interface `bridge-56`. Note: You would need an upstream IPv6 connection for this to be fully functional.

   - Using Winbox:
       - Navigate to *IPv6 -> Addresses*.
       - Click the "+" button.
       - In the *Address* field, enter `2001:db8::1/64`.
       - In the *Interface* drop-down, select `bridge-56`.
       - Optionally, add a *Comment*.
       - Click *Apply* and *OK*.

### 3. Complete MikroTik CLI Configuration Commands

```mikrotik
/ip address
add address=102.55.83.1/24 interface=bridge-56 comment="Main IPv4 Address on bridge-56"
/ip pool
add name=dhcp_pool_56 ranges=102.55.83.100-102.55.83.200 comment="DHCP pool for bridge-56"
/ip dhcp-server
add name=dhcp_server_56 interface=bridge-56 address-pool=dhcp_pool_56 authoritative=yes lease-time=1d disabled=no comment="DHCP server for bridge-56"
/ip dhcp-server network
add address=102.55.83.0/24 gateway=102.55.83.1 dns-server=8.8.8.8,8.8.4.4 comment="DHCP Network settings for bridge-56"
/ip dhcp-server lease
add mac-address=AA:BB:CC:DD:EE:FF address=102.55.83.50 server=dhcp_server_56 comment="Static IP for device with MAC address AA:BB:CC:DD:EE:FF"
/ipv6 address
add address=2001:db8::1/64 interface=bridge-56 comment="IPv6 Address on bridge-56"
```

### 4. Common MikroTik-Specific Pitfalls, Troubleshooting, and Diagnostics

- **Pitfalls:**
    - **Incorrect Interface:** Ensure you are configuring the correct bridge interface (`bridge-56` in our case).
    - **Address Overlap:** Avoid IP address conflicts with other devices or subnets.
    - **Incorrect Subnet Mask:** Using a different subnet mask than intended can cause network connectivity issues.
    - **DHCP Authoritative Settings:** When you have multiple DHCP servers on the network, you might end up having conflicting servers. Set the authorative flag for the correct server and also make sure that the other servers are not providing DHCP services.
    - **Firewall Interference:** Incorrect firewall rules can block DHCP traffic.
    - **Lease time:** Lease time should be set based on your requirement.
- **Troubleshooting:**
    - **`ping`:** Check connectivity to the router's IP address (e.g., `ping 102.55.83.1`).
    - **`torch`:** Use `torch` to examine traffic on `bridge-56`. E.g., `/tool torch interface=bridge-56`
    - **`/ip dhcp-server lease print`:**  Verify that clients are getting IP addresses.
    - **`/log print`:** Check the MikroTik logs for any errors.
    - **`/ip firewall filter print`:** Examine your firewall rules, looking for any rules that might block your traffic or DHCP requests/replies.

    - **Error Scenario 1: DHCP Failure**
      -  **Cause:** Misconfigured DHCP server or firewall rules blocking DHCP traffic.
      - **Steps:**
        - Use `/tool torch` to check DHCP traffic.
        - Check DHCP server configuration using `/ip dhcp-server print`.
        - Check firewall using `/ip firewall filter print`.
        - Ensure that interface is correct and associated with the server.
      - **Solution:** Adjust the DHCP configuration to be correct and make sure that your firewall is not blocking your DHCP related packets.

    - **Error Scenario 2: No IPv6 connectivity**
      - **Cause:** No upstream IPv6 connectivity.
      - **Steps:**
        - Check IPv6 address on upstream interface.
        - Check whether any other IPv6 settings need to be set.
        - Use `ping6` to check IPv6 connectivity.
      - **Solution:** Ensure you have an IPv6 internet connection and proper settings on your MikroTik device.

### 5. Verification and Testing

- **Ping Test:** From a client on the `102.55.83.0/24` network, use the `ping` command to verify network connectivity:
   - `ping 102.55.83.1` (pinging the router's interface IP).
   - `ping 8.8.8.8` (pinging an external address if the router has internet access).

- **DHCP Test:** Check the `/ip dhcp-server lease print` command on the MikroTik router. You should see IP addresses assigned to clients on your network.
- **Traceroute Test:**
  - From a client device, use `traceroute` (or `tracert` on Windows) to check the path your packets are taking.
  - E.g. `traceroute 8.8.8.8`.
- **Torch Test:**
  - Use `/tool torch interface=bridge-56` to monitor packets going through the `bridge-56` interface.
  - Using torch you will be able to see the DHCP related packets.

### 6. Related MikroTik-Specific Features, Capabilities, and Limitations

-   **IP Address Lists:** Create address lists for groups of IPs to use in firewall rules.
    -   Example CLI command:
        ```mikrotik
        /ip firewall address-list
        add list=my_local_network address=102.55.83.0/24
        ```
-   **VRF (Virtual Routing and Forwarding):**  Use VRF for network segmentation in complex environments.
-   **MAC Binding:** Configure static IP addresses based on the MAC address of devices.
-   **Layer 7 Filtering:** Apply complex filtering based on application layer data.

**Less Common Features Scenario - Address Lists and Layer 7 Filtering:**

Let's assume we need to create a rule to allow HTTP traffic but block HTTP traffic from some specific IP addresses.
-   **Address list:**
    ```mikrotik
    /ip firewall address-list
    add list=blocked_ips address=102.55.83.101 comment="IP to block"
    add list=blocked_ips address=102.55.83.105 comment="IP to block"
    ```

-   **Layer 7 rule:**
    ```mikrotik
    /ip firewall layer7-protocol
    add name=http regexp="^.+(GET|POST).+Host: .+(\\r\\n)\$"
    ```
-   **Firewall rule:**
     ```mikrotik
        /ip firewall filter
        add chain=forward action=accept layer7-protocol=http src-address-list=!blocked_ips  comment="Allow HTTP from local lan except blocked IPs"
        add chain=forward action=drop layer7-protocol=http comment="Drop HTTP from all the other addresses"
     ```

### 7. MikroTik REST API Examples

- **API Endpoint:** `http://<router_ip>/rest/ip/address`
- **Request Method:** `GET` (to read), `POST` (to create), `PUT` (to update), `DELETE` (to delete)
- **Example 1: Get all IP Addresses**

    -   **Request:**
        -   Method: `GET`
        -   URL: `http://<router_ip>/rest/ip/address`

    -   **Expected Response:**
         ```json
        [
           {
             ".id": "*2",
             "address": "102.55.83.1/24",
             "interface": "bridge-56",
             "actual-interface": "bridge-56",
             "network": "102.55.83.0",
             "broadcast": "102.55.83.255",
             "comment": "Main IPv4 Address on bridge-56",
             "disabled": false,
             "dynamic": false
           }
        ]
         ```

- **Example 2: Create an IP Address**

    -   **Request:**
        -   Method: `POST`
        -   URL: `http://<router_ip>/rest/ip/address`
        -   JSON Payload:
             ```json
             {
              "address": "102.55.83.2/24",
              "interface": "bridge-56",
              "comment": "Additional IP Address"
            }
             ```

    -   **Expected Response:**
         ```json
        {
             ".id": "*3",
              "address": "102.55.83.2/24",
              "interface": "bridge-56",
              "actual-interface": "bridge-56",
              "network": "102.55.83.0",
              "broadcast": "102.55.83.255",
              "comment": "Additional IP Address",
              "disabled": false,
              "dynamic": false
        }
         ```

- **Example 3: Update an IP Address**
   - **Request**
     - Method: PUT
     - URL:  `http://<router_ip>/rest/ip/address/*2`
     - JSON Payload:
       ```json
         {
           "comment": "Main IPv4 Address on bridge-56 updated"
         }
        ```
   - **Expected Response:**

        ```json
          {
             ".id": "*2",
             "address": "102.55.83.1/24",
             "interface": "bridge-56",
             "actual-interface": "bridge-56",
             "network": "102.55.83.0",
             "broadcast": "102.55.83.255",
             "comment": "Main IPv4 Address on bridge-56 updated",
             "disabled": false,
             "dynamic": false
           }
         ```

- **Example 4: Delete an IP Address**
    - **Request**
      - Method: DELETE
      - URL:  `http://<router_ip>/rest/ip/address/*3`
   - **Expected Response:**
        - An empty response or a success code 204

**Note:**
- Replace `<router_ip>` with the IP address of your MikroTik Router.
- Ensure the REST API is enabled under `IP -> Services` and your user has API read/write privileges.

### 8. In-depth Explanations of Core Concepts

- **Bridging:** Bridging in MikroTik combines multiple physical network interfaces into a single logical interface. This allows devices connected to different interfaces to be part of the same broadcast domain.
  -   In our case, we add IP address to `bridge-56` instead of adding IP address to the physical interfaces that are part of the bridge.
  -   Bridge handles layer2 switching as well.
- **Routing:**  MicroTik uses a powerful routing engine. When an IP address is assigned to an interface the router will automatically create the relevant routes for that specific network.
- **Firewall:** MikroTik's firewall is stateful, tracking connections to allow return traffic, and it supports complex filtering rules using different parameters.
- **Connection Tracking:** Used by firewall for stateful inspection.
-   **DHCP:** DHCP dynamically assigns IP addresses to the clients connected to your network.
- **IP Pools**: Provide ranges of IP addresses for DHCP and other services.

### 9. Security Best Practices

-   **Secure Router Access:** Change default username/password, use strong passwords, disable unnecessary services, and restrict access using firewall rules.
-   **Disable Unnecessary Services:**  Disable services like Telnet and FTP. Use SSH.
-   **Firewall Rules:** Implement a strong firewall policy, allowing only essential traffic.
-   **Regular Updates:** Keep RouterOS updated to the latest stable version.
- **MAC address whitelisting:** When configuring static IP addresses in DHCP, it would be useful to create a whitelist for MAC address so that no unknown devices are given IP address.

**Security scenario - API Access**

1. **Create a dedicated user for API:** Create a new user with the specific permissions needed to access the REST API
    ```mikrotik
    /user add name=apiuser password=securepass group=read,write
    ```
2. **Enable API Access:** In *IP->Services*, ensure that the `api-ssl` service is enabled for secure access.
3. **Firewall restrictions:**
    ```mikrotik
     /ip firewall filter
        add chain=input protocol=tcp dst-port=8729 action=drop comment="drop rest-api requests from outside your local network"
        add chain=input protocol=tcp dst-port=8729 src-address-list=my_local_network action=accept comment="Allow rest-api from your local network"
    ```
-   **Explanation:** These commands create a user specifically for API access, enable secure API access and also make sure that API access from outside local network is dropped. It is also important to have strong password in the user.

### 10. Detailed Explanations and Configuration Examples for Specified MikroTik Topics

**Note:** Covering all of these topics in this document would make it excessively large. Below, I will provide a brief overview of each with examples, focusing on key RouterOS concepts.

**1. IP Addressing (IPv4 and IPv6):**

- We have covered IPv4 and IPv6 addressing earlier with the main example.
-   **Key Concept:** Addresses are associated with interfaces. Each interface on the router can have multiple IPv4 and IPv6 addresses.

**2. IP Pools:**

- We covered IP pools above as well.
-   **Key Concept:** Logical collections of IP addresses used by DHCP, Hotspot, and other services.

**3. IP Routing:**

-   **Key Concept:** RouterOS uses a routing table that automatically gets updated based on the IP addresses.
-   **Example - Static Route:** Add a static route to the destination network:
    ```mikrotik
    /ip route
    add dst-address=172.16.0.0/16 gateway=192.168.10.1 comment="Static Route"
    ```

**4. IP Settings:**

-   **Key Concept:** Configuration settings like ARP, ICMP behavior, etc.
-   **Example:** Disable ICMP redirect messages:
    ```mikrotik
    /ip settings set send-redirects=no
    ```

**5. MAC Server:**

-   **Key Concept:** Can manage MAC address to IP binding and is used by other services.
-   **Example:** You can see the static MAC to IP binding from the DHCP server leases tab.

**6. RoMON:**

-   **Key Concept:** MikroTik’s proprietary remote monitoring protocol that allows easy connection to the other routers.
-   **Example:**  Enable RoMON:
    ```mikrotik
    /tool romon set enabled=yes
    ```

**7. WinBox:**

-   **Key Concept:** A graphical user interface for managing MikroTik routers.
-   **Example:** All examples so far have mentioned WinBox configuration.

**8. Certificates:**

-   **Key Concept:** Used for secure connections to RouterOS services like webfig, api, ssh etc.
- **Example**: Creating self signed certificate
   ```mikrotik
    /certificate
    add name=self-signed common-name="myrouter" key-usage=digital-signature,key-encipherment,tls-server
    sign self-signed ca=yes
   ```
-   This command will create a self signed certificate that can be used for secure services.

**9. PPP AAA (Authentication, Authorization, and Accounting):**

-   **Key Concept:** Manages authentication for PPP connections.
-   **Example:** Configure user for PPP connection:
    ```mikrotik
    /ppp secret
    add name=myuser password=mypassword service=pppoe
    ```

**10. RADIUS:**

-   **Key Concept:** Centralized authentication and accounting.
-   **Example:** Configure RADIUS server
    ```mikrotik
    /radius add address=192.168.10.1 secret=mysecret timeout=30
    ```

**11. User / User groups:**

-   **Key Concept:** Managing users and their permissions.
-   **Example:** We have seen above on creating a specific user for API access.

**12. Bridging and Switching:**

-   **Key Concept:** We have already described this above.
-   **Example:** Add interface to bridge:
    ```mikrotik
     /interface bridge port
     add bridge=bridge-56 interface=ether2
    ```

**13. MACVLAN:**

-   **Key Concept:** A virtual interface associated with MAC address on top of other physical interface.
-  **Example:** Add a macvlan interface
      ```mikrotik
      /interface macvlan
      add mac-address=02:11:22:33:44:55 interface=ether1 comment="macvlan on top of ether1"
      ```

**14. L3 Hardware Offloading:**

-   **Key Concept:** Offloading routing to the switch chip for improved performance.
-   **Note:** Only available on specific MikroTik devices with compatible hardware.

**15. MACsec:**

-   **Key Concept:** Provides layer2 security using encryption between peers.
-   **Note:** Advanced feature. Not available in all devices.

**16. Quality of Service (QoS):**

-   **Key Concept:** Prioritize network traffic.
-   **Example:** Setting up a simple queue:
    ```mikrotik
    /queue simple
    add name=download_queue target=102.55.83.0/24 max-limit=10M comment="limit download to 10M for local network"
    ```

**17. Switch Chip Features:**

-   **Key Concept:**  Advanced features available on MikroTik devices that have switch chip.

**18. VLAN:**

-   **Key Concept:**  Segmentation of network using VLAN IDs.
-   **Example:** Add a VLAN on a bridge:
    ```mikrotik
     /interface vlan
     add name=vlan100 interface=bridge-56 vlan-id=100 comment="Vlan on top of bridge 56"
     /interface bridge port
      add bridge=bridge-56 interface=vlan100
    ```

**19. VXLAN:**

-   **Key Concept:** Layer2 tunnel over IP.
-  **Example:** Add a VXLAN interface
     ```mikrotik
     /interface vxlan
     add name=vxlan1 remote-address=192.168.10.1 vni=100 interface=bridge-56
     ```

**20. Firewall and Quality of Service:**

-   **Key Concept:** We have mentioned firewall above. For QoS you can configure queues to prioritize certain type of traffic.
-   **(Detailed topics):**  Connection tracking, Firewall, Packet Flow in RouterOS, Queues, Firewall and QoS Case Studies, Kid Control, UPnP, NAT-PMP.
- **Example**:
  - See QoS and Firewall examples above.
  - For NAT-PMP, use command: `/ip upnp set enabled=yes allow-nat-pmp=yes`.

**21. IP Services (DHCP, DNS, SOCKS, Proxy):**

-  **(Detailed Topics):** DHCP we have covered in detail. For others, you can use:
     ```mikrotik
     /ip dns set servers=8.8.8.8,8.8.4.4 allow-remote-requests=yes
     /ip socks set enabled=yes
     /ip proxy set enabled=yes
     ```

**22. High Availability Solutions (Including: Load Balancing, Bonding, Bonding Examples, HA Case Studies, Multi-chassis Link Aggregation Group, VRRP, VRRP Configuration Examples):**

-   **Key Concept:** These are features to ensure that there is no single point of failure.
-   **Example - VRRP:**
    ```mikrotik
    /interface vrrp add name=vrrp1 interface=bridge-56 vrid=10 priority=200 address=102.55.83.254/24
    ```
-   **Example - Bonding:**
    ```mikrotik
    /interface bonding
    add name=bond1 mode=802.3ad slaves=ether1,ether2
    ```

**23. Mobile Networking (Including: GPS, LTE, PPP, SMS, Dual SIM Application):**

-   **Key Concept:** Features to connect using mobile networks.
-   **Example - LTE:**  (Commands will vary based on the modem):
    ```mikrotik
   /interface lte apn add name=myapn apn=myapn user=myuser password=mypassword
   /interface lte set lte1 apn-profile=myapn
    ```

**24. Multi Protocol Label Switching - MPLS (Including: MPLS Overview, MPLS MTU, Forwarding and Label Bindings, EXP bit and MPLS Queuing, LDP, VPLS, Traffic Eng, MPLS Reference):**

-   **Key Concept:** Layer 2.5 protocol to handle packet routing.
-   **Note:** Advanced feature for specific network requirement.

**25. Network Management (Including: ARP, Cloud, DHCP, DNS, SOCKS, Proxy, Openflow):**

-   **Key Concept:** Network management features available in MikroTik devices. We have already seen DHCP, DNS, Socks and Proxy above.
-  **Example - Cloud**
    ```mikrotik
    /ip cloud set ddns-enabled=yes update-time=60s
    ```

**26. Routing (Including: Routing Protocol Overview, Moving from ROSv6 to v7 with examples, Routing Protocol Multi-core Support, Policy Routing, Virtual Routing and Forwarding - VRF, OSPF, RIP, BGP, RPKI, Route Selection and Filters, Multicast, Routing Debugging Tools, Routing Reference, BFD, IS-IS):**

-   **Key Concept:** Dynamic routing protocols like OSPF, RIP and BGP.
- **Example - OSPF**
    ```mikrotik
     /routing ospf instance add name=ospf1 router-id=1.1.1.1
     /routing ospf area add instance=ospf1 area-id=0.0.0.0
     /routing ospf network add instance=ospf1 area=0.0.0.0 network=102.55.83.0/24
    ```

**27. System Information and Utilities (Including: Clock, Device-mode, E-mail, Fetch, Files, Identity, Interface Lists, Neighbor discovery, Note, NTP, Partitions, Precision Time Protocol, Scheduler, Services, TFTP):**

-   **Key Concept:** System level information and management utilities.
-   **Example:** Set the device identity:
    ```mikrotik
    /system identity set name=myrouter
    ```
 - **Example:** NTP configuration
     ```mikrotik
      /system ntp client set enabled=yes primary-ntp=0.pool.ntp.org secondary-ntp=1.pool.ntp.org
     ```
**28. Virtual Private Networks (Including: 6to4, EoIP, GRE, IPIP, IPsec, L2TP, OpenVPN, PPPoE, PPTP, SSTP, WireGuard, ZeroTier):**

-   **Key Concept:** Different types of VPN technologies that can be configured in the MikroTik devices.
-   **Example - WireGuard:**
     ```mikrotik
        /interface wireguard
        add name=wg1 listen-port=13231 private-key="<PRIVATE_KEY>"
        /interface wireguard peers
        add interface=wg1 allowed-address=192.168.11.0/24 endpoint-address=192.168.10.2 endpoint-port=13231 public-key="<PUBLIC_KEY>" persistent-keepalive=25s
        /ip address add address=192.168.11.1/24 interface=wg1
        ```

**29. Wired Connections (Including: Ethernet, MikroTik wired interface compatibility, PWR Line):**

-   **Key Concept:** Physical interfaces.
-   **Note:** Different models of MikroTik will have different interfaces.

**30. Wireless (Including: WiFi, Wireless Interface, W60G, CAPsMAN, HWMPplus mesh, Nv2, Interworking Profiles, Wireless Case Studies, Spectral scan):**

-   **Key Concept:** MikroTik also has devices with wireless support.
-   **Example - Wireless configuration:**
    ```mikrotik
    /interface wireless set wlan1 mode=ap-bridge ssid=myssid band=2ghz-b/g/n security-profile=default
   ```

**31. Internet of Things (Including: Bluetooth, GPIO, Lora, MQTT):**

-   **Key Concept:**  MikroTik also supports IoT related connectivity.
-   **Note:**  Available in devices which have required hardware.

**32. Hardware (Including: Disks, Grounding, LCD Touchscreen, LEDs, MTU in RouterOS, Peripherals, PoE-Out, Ports, Product Naming, RouterBOARD, USB Features):**

-   **Key Concept:** Specific hardware related settings.
- **Note**: Different devices have different configuration.
-  **Example - set MTU:**
     ```mikrotik
     /interface set ether1 mtu=1500 l2mtu=1596
    ```

**33. Diagnostics, monitoring and troubleshooting (Including: Bandwidth Test, Detect Internet, Dynamic DNS, Graphing, Health, Interface stats and monitor-traffic, IP Scan, Log, Netwatch, Packet Sniffer, Ping, Profiler, Resource, SNMP, Speed Test, S-RJ10 general guidance, Torch, Traceroute, Traffic Flow, Traffic Generator, Watchdog):**

-  We have already used some of these like `ping`, `torch` and others.
-  **Example - Netwatch**
    ```mikrotik
     /tool netwatch add host=8.8.8.8 interval=10s timeout=100ms up-script="/log warning message=\"8.8.8.8 is up\"" down-script="/log error message=\"8.8.8.8 is down\""
    ```

**34. Extended features (Including: Container, DLNA Media server, ROSE-storage, SMB, UPS, Wake on LAN, IP packing):**

-   **Key Concept:** Some extended feature that can be used on specific MikroTik devices
-   **Example - Enable SMB server:**
    ```mikrotik
    /smb set enabled=yes
    ```

### Trade-offs Between Configurations

- **Static vs. Dynamic IP:**
  - **Static:**  Predictable IP addresses for devices.  Good for servers and devices that need to be reachable. But it is difficult to manage in a large network.
  - **Dynamic (DHCP):** Easier for client management.  Dynamic IP addresses assigned by DHCP server.  Can be limiting if some devices need to be reachable at the same IP address always.
- **Bridging vs.
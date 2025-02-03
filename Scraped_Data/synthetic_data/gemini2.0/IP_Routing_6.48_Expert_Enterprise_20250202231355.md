**IP Routing**

**Configuration scenario and requirements:**

* Configure IP routing for a network with multiple subnets and internet access.
* Implement static and dynamic routing protocols to optimize traffic flow.
* Ensure high availability with advanced features like load balancing and bonding.

**Step-by-step implementation:**

1. **Configure IP Addresses:**
   - Assign IP addresses to all interfaces connected to different subnets.
   - Use `/interface` menu to set IP addresses, subnet masks, and default gateways.

2. **Enable IP Forwarding:**
   - Navigate to `/ip settings` and check `Allow forwarding for all addresses` option.

3. **Add Static Routes:**
   - Use `/ip route add` command to add static routes.
   - Specify destination network, netmask, gateway, and distance (metric).

4. **Configure OSPF Dynamic Routing:**
   - Navigate to `/routing ospf` and enable OSPF.
   - Create areas, assign interfaces, and set timers.

5. **Implement Load Balancing:**
   - Navigate to `/ip firewall mangle add` and create a rule to manipulate routing.
   - Use `forward jump` target to distribute traffic across multiple routes or gateways.

6. **Set Up Bonding for High Availability:**
   - Configure bonding interfaces in `/interface bonding add` menu.
   - Specify bonding mode, load balancing algorithm, and failover settings.

**Complete configuration commands:**

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=10.10.10.1/24 interface=ether2
/ip settings set allow-forwarding-for-all-addresses=yes
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.254
/routing ospf enable
/routing ospf network add area=0 interface=ether1
/ip firewall mangle add action=forward-jump jump-target=lb-dist jump-next-firewall=lb-routing
/interface bonding add name=bond0 mode=balance-rr ports=ether1,ether2
```

**Common pitfalls and solutions:**

* **Route flapping:** Verify routing tables for incorrect routes or routing loops. Use `/routing monitor` to track route changes.
* **Packet loss:** Ensure proper firewall rules allow traffic and check interface status. Use `ping`, `traceroute`, and `packet sniffer` to isolate issues.
* **Poor performance:** Analyze traffic flow with `/ip traffic flow` and optimize routing with load balancing and bonding.

**Verification and testing steps:**

* Use `ping` and `traceroute` to test connectivity between subnets and internet gateway.
* Check routing tables (`/ip route print`) for correct routes and distances.
* Simulate network failures to verify high availability with bonding.

**Related features and considerations:**

* **Policy Routing:** Configure multiple routing tables and policies to handle specific traffic types differently.
* **Virtual Routing and Forwarding (VRF):** Isolate routing domains for improved security and traffic management.
* **QoS (Quality of Service):** Prioritize traffic and manage bandwidth allocation to ensure optimal performance.

**MikroTik REST API examples:**

**List IP Addresses:**

* API Endpoint: `https://<ip-address>/rest/ip/address`
* Request Method: GET
* Example JSON Payload: N/A
* Expected Response:
    ```json
    [
        {
            "address": "192.168.1.1",
            "interface": "ether1"
        },
        {
            "address": "10.10.10.1",
            "interface": "ether2"
        }
    ]
    ```

**Add Static Route:**

* API Endpoint: `https://<ip-address>/rest/ip/route`
* Request Method: POST
* Example JSON Payload:
    ```json
    {
        "dst-address": "192.168.2.0/24",
        "gateway": "192.168.1.254"
    }
    ```
* Expected Response:
    ```json
    {
        "address": "192.168.2.0/24",
        "gateway": "192.168.1.254"
    }
    ```
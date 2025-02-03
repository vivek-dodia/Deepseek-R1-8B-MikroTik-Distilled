Okay, let's dive into creating comprehensive documentation for IP routing on a MikroTik RouterOS device, specifically for a point-to-point link using the 201.94.190.0/24 subnet on the wlan-56 interface. We'll aim for RouterOS 7.12 compatibility, with notes for 6.48 and 7.x as needed.

## Scenario Description:

We're setting up a point-to-point wireless link using MikroTik devices, with each device having an interface (named `wlan-56` in our case) connected to the wireless network. We'll configure basic IP routing so that devices on the 201.94.190.0/24 subnet can communicate through this link. Our focus is on IP address assignment and basic routing. For now, we assume that the underlying layer 2 (wireless link) is working and the stations can see each other. We will focus entirely on the IP layer.

## Implementation Steps:

Here's a step-by-step guide, focusing on both the CLI and Winbox for maximum usability:

1. **Step 1: Assign an IP Address to the `wlan-56` Interface**

   *   **Purpose:** To give the interface an IP address within the designated subnet, allowing it to participate in IP communication.
   *   **CLI Command Before**:
       ```
       /ip address print
       ```
        *Example Output:*
        ```
        Flags: X - disabled, I - invalid, D - dynamic
        #   ADDRESS            NETWORK         INTERFACE
        0   192.168.88.1/24    192.168.88.0     ether1
        ```
   *   **CLI Command:**
       ```
       /ip address add address=201.94.190.1/24 interface=wlan-56
       ```
   *   **Winbox GUI:** Go to `IP > Addresses`, click the `+` button. Enter `201.94.190.1/24` in the `Address` field, select `wlan-56` in the `Interface` dropdown, and click `OK`.
   *   **CLI Command After:**
        ```
        /ip address print
        ```
        *Example Output:*
        ```
        Flags: X - disabled, I - invalid, D - dynamic
        #   ADDRESS            NETWORK         INTERFACE
        0   192.168.88.1/24    192.168.88.0     ether1
        1   201.94.190.1/24    201.94.190.0    wlan-56
        ```
   *   **Effect:** The `wlan-56` interface now has an IP address (`201.94.190.1`) from the 201.94.190.0/24 subnet. We also will set up the other side of this link on a different router.

2.  **Step 2: Assign an IP Address to the other side of the `wlan-56` Interface**

    *  **Purpose:** To give the other router's interface an IP address within the designated subnet, allowing it to participate in IP communication.
    *  **CLI Command Before**:
        ```
        /ip address print
        ```
        *Example Output:*
        ```
        Flags: X - disabled, I - invalid, D - dynamic
        #   ADDRESS            NETWORK         INTERFACE
        0   192.168.88.1/24    192.168.88.0     ether1
        ```
    *  **CLI Command:**
        ```
        /ip address add address=201.94.190.2/24 interface=wlan-56
        ```
    *  **Winbox GUI:** Go to `IP > Addresses`, click the `+` button. Enter `201.94.190.2/24` in the `Address` field, select `wlan-56` in the `Interface` dropdown, and click `OK`.
    *  **CLI Command After:**
        ```
        /ip address print
        ```
        *Example Output:*
        ```
        Flags: X - disabled, I - invalid, D - dynamic
        #   ADDRESS            NETWORK         INTERFACE
        0   192.168.88.1/24    192.168.88.0     ether1
        1   201.94.190.2/24    201.94.190.0    wlan-56
        ```
    *   **Effect:** The `wlan-56` interface on the other router now has an IP address (`201.94.190.2`) from the 201.94.190.0/24 subnet.

3.  **Step 3: Add a Static Route (Optional for Point-to-Point)**

    *   **Purpose:** While not strictly required for a simple point-to-point link within the same subnet,  we'll add a route for demonstration and completeness. This is especially necessary if the endpoints are not directly connected or if you have complex routing needs. In this particular scenario, the IP of the other side router will be visible from each side through the same `wlan-56` interface.
    *   **CLI Command Before:**
        ```
        /ip route print
        ```
        *Example Output:*
        ```
        Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme, B - blackhole, U - unreachable
        #     DST-ADDRESS        PREF-SRC        GATEWAY            DISTANCE
        0  ADC 192.168.88.0/24                  ether1             0
        ```
    *   **CLI Command on Router #1:**
        ```
        /ip route add dst-address=201.94.190.0/24 gateway=201.94.190.2
        ```
    * **CLI Command on Router #2:**
        ```
        /ip route add dst-address=201.94.190.0/24 gateway=201.94.190.1
        ```
    *   **Winbox GUI:** Go to `IP > Routes`, click the `+` button. Enter `201.94.190.0/24` in `Dst. Address` field, and `201.94.190.2` in the `Gateway` (for Router #1) or `201.94.190.1` in the `Gateway` field (for Router #2) field, click `OK`.
    *   **CLI Command After (Router #1):**
        ```
        /ip route print
        ```
        *Example Output (Router #1):*
        ```
        Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme, B - blackhole, U - unreachable
        #     DST-ADDRESS        PREF-SRC        GATEWAY            DISTANCE
        0  ADC 192.168.88.0/24                  ether1             0
        1  AS 201.94.190.0/24                  201.94.190.2         1
        ```
        *Example Output (Router #2):*
        ```
        Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme, B - blackhole, U - unreachable
        #     DST-ADDRESS        PREF-SRC        GATEWAY            DISTANCE
        0  ADC 192.168.88.0/24                  ether1             0
        1  AS 201.94.190.0/24                  201.94.190.1         1
        ```
    *   **Effect:**  Packets destined for the 201.94.190.0/24 network will be routed via the other end's IP address. In reality, if both interfaces are on the same physical link, this configuration may be redundant. However, in larger networks with multiple hops this is crucial.

## Complete Configuration Commands:

Here's the combined set of commands to replicate this configuration on both routers:

**Router #1:**
```
/ip address
add address=201.94.190.1/24 interface=wlan-56
/ip route
add dst-address=201.94.190.0/24 gateway=201.94.190.2
```
**Router #2:**
```
/ip address
add address=201.94.190.2/24 interface=wlan-56
/ip route
add dst-address=201.94.190.0/24 gateway=201.94.190.1
```
**Explanation of Parameters:**

| Command Parameter       | Value       | Description                                                                                                                |
| :--------------------- | :---------- | :------------------------------------------------------------------------------------------------------------------------- |
| `/ip address add`     |             | Begins the command to add an IP address                                                                                 |
| `address`             | `201.94.190.1/24` (Router #1) / `201.94.190.2/24` (Router #2)          | The IP address and subnet mask for the interface.                                             |
| `interface`           | `wlan-56`    | The name of the interface to assign the IP to.                                                                             |
| `/ip route add`       |             | Begins the command to add a static route.                                                                               |
| `dst-address`          | `201.94.190.0/24`     | The destination network address and mask.                                                                          |
| `gateway`             |`201.94.190.2` (Router #1) / `201.94.190.1` (Router #2) | The IP address of the next-hop router.  |

## Common Pitfalls and Solutions:

*   **Incorrect IP Addresses:**
    *   **Problem:** Using overlapping IP addresses or incorrect subnet masks will cause communication issues.
    *   **Solution:** Double-check IP addresses, subnet masks, and interface assignments. Use `ip address print` to verify your settings.
*   **Firewall Blocking:**
    *   **Problem:** The MikroTik firewall can block traffic even when basic IP routing is correct.
    *   **Solution:** Verify firewall rules (`/ip firewall filter print`). Ensure there are rules to allow communication on the desired interface or disable the firewall for basic testing (`/ip firewall filter set disabled=yes`). **Important:**  This should only be done for testing, and should not be left disabled in any real world scenario.
*   **Layer 2 Issues:**
    *   **Problem:** The point-to-point link is not working on the lower layers (wireless, cable).
    *   **Solution:** Check the link status (e.g., signal strength, associated devices). Use `interface wireless monitor wlan-56` to examine the link. Also verify proper bridge settings, if necessary.
*   **Misconfigured Routes:**
    *   **Problem:**  Typing a wrong gateway address in the route configuration, or misinterpreting route precedence.
    *   **Solution:** Always double check that the gateway you are inputting is reachable and is the IP address of the next-hop router.
*   **Missing Routes:**
    *   **Problem:** For more complex topologies, routes can be missing for different subnets.
    *   **Solution:**  Run the `/ip route print` command to see all routes, and add any missing routes as needed.
*  **Resource Issues**
  *  **Problem:** Although this simple configuration won't cause resource issues, more complex routing configurations with large numbers of routes, large firewall rules, or multiple interfaces might cause high CPU usage.
  * **Solution:** Check the router resources using `/system resource print` if you suspect resource issues.

## Verification and Testing Steps:

1.  **Ping Test:**
    *   **Command (on Router #1):**
        ```
        /ping 201.94.190.2
        ```
    *   **Command (on Router #2):**
        ```
        /ping 201.94.190.1
        ```
    *   **Expected Result:** A successful ping should show packets transmitted and received with low or no packet loss.

2.  **Traceroute:**
    *   **Command (on Router #1):**
        ```
        /tool traceroute 201.94.190.2
        ```
     *   **Command (on Router #2):**
        ```
        /tool traceroute 201.94.190.1
        ```
    *   **Expected Result:** A traceroute should show only one hop, indicating direct connectivity over the point-to-point link.

3.  **IP Address Table Check:**
    *   **Command (on both Routers):**
        ```
        /ip address print
        ```
    *   **Expected Result:** The interface should have the correct IP address.

4.  **Route Table Check:**
    *   **Command (on both Routers):**
        ```
        /ip route print
        ```
    *   **Expected Result:** The static route for the 201.94.190.0/24 subnet should be present with the correct gateway.

5. **Torch Tool:**
    * **Command:** (on both routers)
        ```
        /tool torch interface=wlan-56
        ```
    * **Expected Result:** Using the torch tool, you should see IP traffic between both IP addresses.

## Related Features and Considerations:

*   **Dynamic Routing Protocols (OSPF, BGP, RIP):** For larger networks, use dynamic routing protocols to automatically update routes. OSPF, or Open Shortest Path First, is a common choice for interior routing in larger networks because it scales better than RIP. BGP or Border Gateway Protocol is used to route traffic between different networks. It is rarely used internally, but usually used to connect your network to another, like your internet provider. RIP or Routing Information Protocol is a more basic routing protocol.
*   **Firewall Rules:**  Always configure a restrictive firewall for security. Be careful about having allow-all rules, and make sure to have rules that only allow necessary traffic between endpoints.
*   **QoS (Quality of Service):** Implement QoS rules to prioritize certain traffic types (e.g., VoIP) on the wireless link.
*   **VLANs:**  If you have multiple services, VLANs might be needed to segment the network.
*   **Bridge:**  If the wireless link is part of a larger network, you may need to incorporate a bridge.

## MikroTik REST API Examples (if applicable):

Here are examples for adding an IP address via the REST API. This uses the MikroTik specific API.

**1. Getting an API token:**
    *  **API Endpoint:** `/login`
    * **Request Method:** `POST`
    *  **Example JSON Payload:**
        ```json
        {
            "username": "your_username",
            "password": "your_password"
        }
        ```
    * **Expected Response:**
        ```json
        {
            "token": "your_api_token"
        }
        ```
    * **Error Handling:**
        * Invalid credentials: The API will return an appropriate error message, usually an HTTP 401 error code.
        * Ensure your device has API enabled under `/tool/api/` in RouterOS.

**2. Adding an IP address:**
   * **API Endpoint:** `/ip/address`
   * **Request Method:** `POST`
   * **Example JSON Payload (Router #1):**
      ```json
      {
        "address": "201.94.190.1/24",
        "interface": "wlan-56"
      }
      ```
   * **Example JSON Payload (Router #2):**
      ```json
      {
         "address": "201.94.190.2/24",
         "interface": "wlan-56"
      }
      ```
    * **Expected Response:**
      ```json
      {
           "message": "add done",
            "id": "*1"
      }
      ```
   *   **Error Handling:**
       *  Invalid parameters:  The API will return an error if parameters such as "address" or "interface" are not present, or if their values are invalid.

**3. Adding a Static Route:**
   *  **API Endpoint:** `/ip/route`
   * **Request Method:** `POST`
   *  **Example JSON Payload (Router #1):**
        ```json
       {
           "dst-address": "201.94.190.0/24",
            "gateway": "201.94.190.2"
        }
        ```
    * **Example JSON Payload (Router #2):**
        ```json
       {
           "dst-address": "201.94.190.0/24",
            "gateway": "201.94.190.1"
        }
       ```
   *   **Expected Response:**
        ```json
      {
           "message": "add done",
            "id": "*2"
      }
      ```
   * **Error Handling:**
       * Invalid parameters:  The API will return an error if parameters such as "dst-address" or "gateway" are not present, or if their values are invalid.

**Note:**  Replace `"your_username"` and `"your_password"` with your actual MikroTik username and password, and ensure your router has the API enabled. Always use HTTPS to send your credentials over the internet.

## Security Best Practices

*   **Secure API Access:** Always use secure communication when accessing the RouterOS API. Use SSL/TLS (HTTPS) connections.
*   **Restrict Access:** Limit API access to specific IP addresses or networks via the `/tool/api/settings` menu.
*   **Strong Passwords:** Use strong, unique passwords for all MikroTik accounts.
*   **Disable Unused Services:** Disable services you are not using for security reasons, such as telnet.
*   **Keep RouterOS Updated:**  Regularly update RouterOS to patch security vulnerabilities.
*  **Firewall rules** The most critical part of a Mikrotik firewall is the input chain, which defines what happens to the traffic destined for the router. Never use accept-all rules in the input chain. A good rule is to have a `drop` rule by default, and add `accept` rules for only the ports that are necessary. Never disable the firewall for any longer period of time than the necessary to do basic testing, as leaving it disabled can lead to security vulnerabilities.
*  **Physical Security:** Don't forget to have physical security, so that no unwanted users can directly connect to the router.

## Self Critique and Improvements

*   **More Advanced Routing:**  This setup is a very basic IP routing. We could improve this with dynamic routing protocols, which are more scalable. We could also improve this configuration by adding more advanced features like OSPF, BGP and RIP, and doing load balancing and failover between redundant links.
*   **Firewall Rules:** For production use, the firewall should be configured to only allow necessary traffic. Specific rules can be configured for different services.
*   **Monitoring:** SNMP or other monitoring mechanisms could be added to provide observability into the devices. The device could also be configured to send log information to a central server to ease troubleshooting.
*   **Error Handling:** The API calls here are basic, but more advanced error handling could be done, including more verbose logging.
*   **Automation:** These steps can be automated through scripting, using tools such as Ansible, or through the use of MikroTik's API.

## Detailed Explanations of Topic

*   **IP Routing:** IP Routing is the process of forwarding packets based on destination IP addresses. The goal is to move the data from one place to another, in an efficient manner. IP routing is used at the network layer, layer 3 of the OSI model. Each IP address is formed by the IP and the network address, which is indicated by the CIDR notation. For instance, in the IP address `192.168.1.1/24`, `192.168.1.1` is the IP address, and `/24` indicates the network address is `192.168.1.0`. Each hop on the network layer makes a routing decision, which means that each router needs to have the IP of each of its interfaces, and know what is the best path to each destination network address.
*   **Static vs. Dynamic Routing:**
    *   **Static Routing:** Routes are manually configured and do not change unless manually adjusted. These are good for simple networks, like this point-to-point link.
    *   **Dynamic Routing:** Routes are learned and updated automatically using routing protocols. This is better for larger, more complex networks where manual route management becomes unfeasible.
*   **Gateway:** A gateway is an IP address that is the next hop for a packet. It can be an interface of another router, or it can be the same interface if the network is directly attached.
*  **MikroTik specific behavior**: MikroTik routers can have several network interfaces, of several different types, and they can be configured with specific roles to ease the setup of a network. In general, IP addresses are assigned to an interface, and the IP stack will then route the packets based on the destination IP. Several tools, such as `torch`, and `traceroute` are important tools to ease troubleshooting.

## Detailed Explanation of Trade-offs

*   **Static Routes vs. Dynamic Routing:**
    *   **Static Routes:** Simpler to set up, but do not automatically adapt to network changes, requiring more administrative overhead in larger or dynamic environments. They are also less robust in case of failures.
    *   **Dynamic Routing:** More complex to configure, but offer automatic route updates and better redundancy. This choice depends heavily on the scale and complexity of the network. For very small point-to-point links, a static route may be sufficient.
*   **OSPF vs BGP vs RIP:**
    *   **OSPF (Open Shortest Path First):** A link state routing protocol that scales well for internal networks and offers fast convergence. It is more complex to set up.
    *   **BGP (Border Gateway Protocol):**  A path vector routing protocol that works well for interconnecting different networks (autonomous systems). It is the most complex to set up, and typically used in internet service providers.
    *   **RIP (Routing Information Protocol):**  A distance vector protocol that is easier to set up than OSPF and BGP, but it's not very scalable or efficient.
*   **Direct Connection vs Gateway:**
    *   **Direct Connection:** If two devices are on the same L2 network and have addresses within the same subnet, they can communicate directly.
    *   **Gateway:** A gateway is needed if communication needs to happen across different subnets. Even though both addresses can communicate directly, it is important to set up a gateway if more hops are to be added later on.
*   **Firewall Rules:**
    *   **Allow-All:** This simplifies initial testing but opens up significant security vulnerabilities.
    *  **Restrictive Rules:**  More secure, but require a more detailed understanding of the network traffic. This is the preferred method for real world usage.

## Configuration for Specific RouterOS Versions:

This configuration targets RouterOS 7.12 but will be compatible with 6.48 and other versions 7.x:

*   **RouterOS 6.x:** Most of the commands are similar to 7.x.  The primary difference you'll encounter is the syntax and feature set in the API, which may not be the same as the 7.x API. In ROS 6, some of the API endpoints for certain features might differ slightly from ROS 7. Refer to the official MikroTik documentation for 6.x specifics.
*   **RouterOS 7.x:** The configurations above are designed for the 7.x API.
*   **REST API:** Pay special attention to the API endpoints in 7.x, as they may have been modified.

Let me know if you'd like me to elaborate on any particular aspect or have other scenarios you want me to cover!

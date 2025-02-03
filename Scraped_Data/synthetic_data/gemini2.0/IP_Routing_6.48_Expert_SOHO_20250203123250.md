Okay, let's dive into a detailed documentation for IP Routing on MikroTik RouterOS 6.48 (and applicable to 7.x), focusing on a SOHO network with a subnet of 10.55.217.0/24 connected to interface ether-59. This is an Expert configuration, so we'll go deep into the details.

## Scenario Description:

This scenario involves configuring a basic IP network on a MikroTik router. We aim to establish a subnet at 10.55.217.0/24 and assign an IP address to the interface `ether-59`. We'll then explore adding a default route to allow traffic outside of the subnet, which makes a useful starting point for more complex scenarios. This is a foundational setup often used in SOHO and other similar network environments.

## Implementation Steps:

Here’s a step-by-step guide for configuring IP routing with this setup. We’ll include CLI and Winbox equivalent instructions as well as expected outcomes at each step.

### 1. Step 1: Assign IP Address to Interface

*   **Goal:** Assign an IP address from the subnet 10.55.217.0/24 to the `ether-59` interface.
*   **Why:** To enable IP communication on this interface within the specified subnet.

    **Before:**
    *   No IP address assigned to `ether-59`.
    *   Ping to 10.55.217.x will not work on the interface
    **CLI:**
    ```mikrotik
    /ip address
    print
    ```
    (This would display the existing ip address list)

    **Winbox:**
    *   Navigate to IP > Addresses.
    *   The address list will likely be empty if it is a new installation or does not have any IPs
    *   There will be no IP for `ether-59`


    **Configuration:**

    *   **CLI:**

        ```mikrotik
        /ip address
        add address=10.55.217.1/24 interface=ether-59
        ```

        *   **`add`**: Adds a new IP address entry.
        *   **`address=10.55.217.1/24`**: Specifies the IP address and subnet mask. `10.55.217.1` is assigned to the interface and /24 means a subnet mask of `255.255.255.0`
        *   **`interface=ether-59`**: Specifies the interface to which the IP is assigned.

    *   **Winbox:**
        1.  Go to IP > Addresses.
        2.  Click on the "+" button to add a new address.
        3.  Enter:
            *   **Address:** `10.55.217.1/24`
            *   **Interface:** `ether-59`
        4.  Click "Apply" and then "OK."
    **After:**
    *   `ether-59` has the IP address 10.55.217.1/24 assigned.
    *   Ping from the router to `10.55.217.1` is successful.
    **CLI:**
    ```mikrotik
    /ip address
    print
    ```
    (This would show that the ip address was added)
    **Winbox:**
    *  The IP address `10.55.217.1/24` should be listed under IP > Addresses and be assigned to `ether-59`

### 2. Step 2: Add a Default Route

*   **Goal:** Add a default route to send traffic destined for networks outside of 10.55.217.0/24 to a gateway address.
*   **Why:** To enable internet access or communication with other networks outside of the local subnet. This assumes there is a gateway device connected to the router's other interfaces.
*   **Note:** For this example we will assume there is a gateway router at `10.55.217.254`

    **Before:**
    *   There is no default route setup. Any request to an ip outside the local subnet will be unroutable
    **CLI:**
    ```mikrotik
    /ip route
    print
    ```
    (This would display the existing ip route list)
    **Winbox:**
    *   Navigate to IP > Routes.
    *   The route list will show that only connected routes exists

    **Configuration:**
    *   **CLI:**

        ```mikrotik
        /ip route
        add dst-address=0.0.0.0/0 gateway=10.55.217.254
        ```
        *   **`add`**: Adds a new route entry.
        *   **`dst-address=0.0.0.0/0`**:  Specifies the destination network. 0.0.0.0/0 is the default route representing all other possible ip networks.
        *   **`gateway=10.55.217.254`**: Specifies the gateway IP address for this default route. (replace with your actual gateway address). This is usually an address on your ISP router.

    *   **Winbox:**
        1. Go to IP > Routes.
        2. Click on the "+" button to add a new route.
        3.  Enter:
            *   **Dst. Address:** `0.0.0.0/0`
            *   **Gateway:** `10.55.217.254`
        4.  Click "Apply" and then "OK."

    **After:**
    *   A default route is added, with a gateway at `10.55.217.254`.
    *   The router can reach outside the `10.55.217.0/24` network.
    **CLI:**
    ```mikrotik
    /ip route
    print
    ```
    (This would show that the default route was added)
    **Winbox:**
    *  The route `0.0.0.0/0` should be listed under IP > Routes and should have a gateway of `10.55.217.254`

## Complete Configuration Commands:

Here is the complete set of commands to implement the setup using MikroTik CLI:

```mikrotik
/ip address
add address=10.55.217.1/24 interface=ether-59
/ip route
add dst-address=0.0.0.0/0 gateway=10.55.217.254
```

*   **`/ip address add address=10.55.217.1/24 interface=ether-59`**
    *   **`/ip address`**: Accesses the IP address management section.
    *   **`add`**: Adds a new IP address.
    *   **`address=10.55.217.1/24`**: The IP address (10.55.217.1) with a /24 subnet mask.
    *   **`interface=ether-59`**: Assigns the IP to the interface named `ether-59`.
*   **`/ip route add dst-address=0.0.0.0/0 gateway=10.55.217.254`**
    *   **`/ip route`**: Accesses the IP route management section.
    *   **`add`**: Adds a new route.
    *   **`dst-address=0.0.0.0/0`**: The destination address for this route which in this case represents all other networks, i.e. the default route
    *   **`gateway=10.55.217.254`**: The gateway IP address to use for this default route. You must set this to your router's gateway IP address for proper functionality.

## Common Pitfalls and Solutions:

*   **Incorrect Interface Name:** If the interface name is wrong (typo), the IP address will not be assigned to the correct interface.
    *   **Solution:** Double-check the interface name using `/interface print` or via Winbox interface list.
*   **Incorrect Subnet Mask:** Using the wrong subnet mask (e.g., /23 instead of /24) will lead to IP address conflicts and issues.
    *   **Solution:** Verify the correct subnet mask using `/ip address print` and adjust as needed, especially when calculating subnet needs.
*   **Missing Gateway IP:** The gateway IP could be incorrect or the device could be offline. If the gateway is incorrect the router will not route packets.
    *   **Solution:** Verify the gateway address, ensure the gateway is active and check firewall rules if the router has one.
*   **Firewall Issues:**  The MikroTik firewall could be blocking connectivity.
    *   **Solution:** Ensure there are allow firewall rules in place for the traffic you expect. Verify there are not any drop rules that might block traffic to and from `ether-59`

*   **High CPU/Memory Usage:** This configuration is very basic and will not cause CPU/memory issues, however, complex routing setups can lead to resource exhaustion on low powered routers.
    *   **Solution**: Monitor system resources using `/system resource print` or via Winbox. Optimize routing rules, or potentially upgrade the router if the load is too high for the device capabilities.
*   **DHCP Server:** In some cases, you may want to run a DHCP server on `ether-59` to assign IPs to client devices. If there is no DHCP server on the local network this can lead to connectivity problems.
    *   **Solution:** Add a DHCP server configuration, or use static ip assignment.

## Verification and Testing Steps:

1.  **Ping from the Router:**
    *   **CLI:** `ping 10.55.217.1` (to verify the address is up on the router)
    *   **CLI:** `ping 10.55.217.254` (to verify gateway reachability)
    *   **CLI:** `ping 8.8.8.8` (to verify outside access, requires default route.)
    *   **Winbox:** Tools > Ping

2.  **Traceroute:**
    *   **CLI:** `traceroute 8.8.8.8` (to check the route to an outside IP, or to the gateway if the external IP is not accessible).
    *  **Winbox:** Tools > Traceroute

3.  **Interface Status:**
    *   **CLI:** `/interface print` (Check `ether-59` status)
    *   **Winbox:** Interfaces (See if `ether-59` is enabled and showing activity)

4.  **IP Address Check:**
    *   **CLI:** `/ip address print` (Verify `10.55.217.1/24` is on `ether-59`)
    *   **Winbox:** IP > Addresses

5.  **Route Check:**
    *   **CLI:** `/ip route print` (Verify the default route exists)
    *   **Winbox:** IP > Routes

## Related Features and Considerations:

*   **Static Routes:** You can add more static routes for specific subnets if needed, using the same `/ip route add` command format.
*   **Dynamic Routing:** For larger networks, consider using dynamic routing protocols like OSPF or BGP for more efficient routing.
*   **VLANs:** You can create VLAN interfaces on `ether-59` using `/interface vlan add`, for creating isolated subnets, and then add ip addresses to them.
*   **Firewall Rules:** Implement firewall rules using `/ip firewall filter` to secure your network and limit access to/from the 10.55.217.0/24 subnet.
*   **DHCP Server:**  Setup a DHCP server on `ether-59` using `/ip dhcp-server` to dynamically assign IPs in the 10.55.217.0/24 range.
*   **NAT:** If you require external internet access you may need NAT, set this up with `/ip firewall nat`.

## MikroTik REST API Examples:

Here's how to use the MikroTik REST API to configure the IP address and default route (requires RouterOS 6.44+ and API service enabled):

*   **Endpoint:** `/ip/address` and `/ip/route`
*   **Method:** POST (for add)
*   **Authentication:**  Requires a session ID or a token. (assumes session id)

**1. Add IP Address:**

*   **Request URL**: `https://<router_ip>/rest/ip/address`
*   **Method:** POST
*   **Request JSON Payload:**
    ```json
    {
        "address": "10.55.217.1/24",
        "interface": "ether-59"
    }
    ```
    *   **`address`**: IP address with subnet mask
    *   **`interface`**: Router interface to assign the address to.

*   **Example Request:**

    ```bash
    curl -k -u <username>:<password> -H "Content-Type: application/json" -H "X-Csrf-Token: <csrf_token>" -d '{ "address": "10.55.217.1/24", "interface": "ether-59" }' https://<router_ip>/rest/ip/address

    ```

    * The `<csrf_token>` can be obtained from the `/tool/fetch url="https://<router_ip>/rest/system/csrf-token"` command.

*   **Expected Successful Response (201 Created):**

    ```json
    {
        ".id":"*5",
        "address":"10.55.217.1/24",
        "interface":"ether-59",
        "actual-interface":"ether-59",
        "dynamic":"false",
        "invalid":"false"
    }
    ```
* Error response, such as attempting to assign an IP that already exists:

     ```json
    {
        "message": "already have such address",
        "error": true
    }
    ```
**2. Add Default Route:**

*   **Request URL**: `https://<router_ip>/rest/ip/route`
*   **Method:** POST
*   **Request JSON Payload:**

    ```json
    {
        "dst-address": "0.0.0.0/0",
        "gateway": "10.55.217.254"
    }
    ```
    *   **`dst-address`**: Destination network, `0.0.0.0/0` being the default route.
    *   **`gateway`**: The gateway IP address for this route.

*   **Example Request:**

    ```bash
    curl -k -u <username>:<password> -H "Content-Type: application/json" -H "X-Csrf-Token: <csrf_token>" -d '{ "dst-address": "0.0.0.0/0", "gateway": "10.55.217.254" }' https://<router_ip>/rest/ip/route
    ```

*   **Expected Successful Response (201 Created):**

     ```json
     {
      "dst-address": "0.0.0.0/0",
      "gateway": "10.55.217.254",
      "gateway-state": "reachable",
      "pref-src": "",
      "distance": "1",
      "scope": "30",
      "target-scope": "10",
      "vrf": "main",
      "disabled": "false",
       ".id": "*14"
      }
     ```
* Error response, such as attempting to set a gateway that is unreachable:

   ```json
   {
    "message": "gateway is unreachable",
    "error": true
    }
    ```
*   **Error Handling:** The API returns JSON formatted errors if any are present. It is important to handle these error codes in your application. For example, if the IP address already exists you would need to update the address, rather than attempt to create it.

## Security Best Practices:

*   **Strong Passwords:** Always use strong, unique passwords for the router's user accounts.
*   **Limit API Access:** Only allow access to the REST API from trusted IP addresses or specific networks.
*   **Firewall:** Implement robust firewall rules. Only allow traffic necessary to the router and its subnet
*   **Disable Unused Services:** Disable all unused services on the router to reduce the attack surface.

## Self Critique and Improvements:

*   **Simplicity:** This configuration provides a barebones setup that could be modified for a range of scenarios.
*   **More Advanced Routing:** For more complex scenarios consider adding dynamic routing protocols to the configuration.
*   **DHCP Integration**: Adding a DHCP server configuration could automate IP assignment on the 10.55.217.0/24 network.
*   **QOS:** Consider QOS (Quality Of Service) configuration for prioritizing traffic.
*   **NAT**: Consider including NAT (Network Address Translation) configuration for routing traffic from the local subnet to an external network.
*  **Dynamic IP:** The current setup assumes static IP assignments. A DHCP client could be enabled to retrieve a dynamic IP address.

## Detailed Explanations of Topic:

IP Routing is the process of forwarding IP packets across networks. It involves:

*   **IP Addresses:** Each device on a network has an IP address, which identifies it.
*   **Subnets:** IP networks are divided into subnets, which are logical groupings of IP addresses.
*   **Routing Tables:** The router maintains a routing table, which maps destination IP addresses to the next hop (gateway) the packet should be forwarded to.
*   **Default Route:** The default route tells the router where to send packets for destinations not explicitly specified in the routing table.
*   **Static Routes:** Manually defined routes to specific networks.
*   **Dynamic Routing Protocols:**  Protocols such as OSPF or BGP that dynamically learn routes from other routers.

## Detailed Explanation of Trade-offs:

*   **Static vs Dynamic Routing:** Static routes are simple to configure for small networks but are difficult to manage in large networks. Dynamic routing protocols, on the other hand, provide greater scalability and flexibility by dynamically adapting to network changes, but require more configuration and resources.
*   **Subnet Mask:** A larger subnet mask (e.g., /24) creates smaller subnets with fewer available addresses, while a smaller subnet mask (e.g., /16) creates larger subnets with more addresses. The choice of mask depends on the number of devices on your network.
*   **Resource Usage:** Complex configurations with a large number of routes, firewalls, or dynamic routing protocols can be resource intensive. Optimizing the configuration, using the correct mask, and limiting the number of addresses will reduce resource use.
*   **Security vs Access:** Firewalls are essential for network security, but can also block legitimate traffic. The correct balance between security and usability must be determined for each use case.

## Configuration for Specific RouterOS Versions:

*   **RouterOS 6.48 and 7.x:** The provided commands are applicable for both versions. There are some notable differences in the rest API, particularly token usage. Please refer to the MikroTik documentation for specific differences in commands.

This detailed documentation and configuration should give you a solid foundation for setting up and managing basic IP routing on your MikroTik router. Remember to always double-check your configurations, especially in a production environment.

Okay, let's dive into a detailed technical document for setting up a MAC server on MikroTik RouterOS 6.48 (compatible with 7.x) within a Hotspot network, specifically using the bridge interface `bridge-72` and the subnet `115.125.170.0/24`. This will be an advanced configuration focusing on practical implementation and in-depth explanations.

## Scenario Description:

This scenario describes the need for a centralized MAC address authentication service, operating as a "MAC Server," within a Hotspot network. Instead of directly authorizing individual devices with usernames and passwords, the Hotspot will authenticate clients based solely on their MAC addresses. This configuration is useful in situations where users are known in advance and their devices are pre-approved, such as in a company's internal network or in some controlled Hotspot scenarios. The `bridge-72` interface will be the designated interface for all these clients connected to the network and should be working as a layer 2 segment and connecting all devices to the same network. The network uses the subnet `115.125.170.0/24`.

## Implementation Steps:

Here's a step-by-step guide for implementing the MAC server configuration.

**1. Step 1: Define the Address List**

*   **Explanation:** We need to create an address list that will hold authorized MAC addresses. This list will be used by the Hotspot server to determine which clients are allowed to access the network. We will name this address list "mac-auth".

*   **Before Configuration:** There is no address list named "mac-auth".

*   **CLI Command:**
    ```mikrotik
    /ip firewall address-list
    add list=mac-auth comment="Authorized MAC Addresses for MAC Server"
    ```

*   **Winbox GUI:**
    *   Navigate to `IP` -> `Firewall`
    *   Go to the `Address Lists` tab.
    *   Click the `+` button.
    *   Enter the name `mac-auth` in the `Name` field.
    *   Add a comment to explain it's purpose.
    *   Click `Apply` then `OK`.

*   **After Configuration:** The "mac-auth" address list will exist, and can be populated with IP addresses.

**2. Step 2: Configure the Bridge Interface**

*   **Explanation:** The interface `bridge-72` must be configured as a bridge interface. This is where the clients will connect and where the hotspot feature will be active.

*   **Before Configuration:** You may have `bridge-72` already created, but might have different settings, such as IP configurations. We need to make sure that this is a plain layer 2 bridge.

*   **CLI Command:**
    ```mikrotik
    /interface bridge
    add name=bridge-72
    ```

*   **Winbox GUI:**
    *   Navigate to `Bridge` under `Interfaces` menu.
    *   Click on the `+` button to add a new bridge.
    *   Set the `Name` to `bridge-72`
    *   Click `Apply` then `OK`.

*   **After Configuration:** The bridge `bridge-72` should exist as a L2 interface.

**3. Step 3: Add Ports to the Bridge**

*   **Explanation:** We now need to add the interfaces that will participate on the created bridge to work correctly. These may be wireless interfaces such as `wlan1`, ethernet interfaces such as `ether1`, or VLANs.

*   **Before Configuration:** The bridge `bridge-72` exists but does not have interfaces associated with it.

*   **CLI Command (Example):**
    ```mikrotik
    /interface bridge port
    add bridge=bridge-72 interface=ether1
    add bridge=bridge-72 interface=wlan1
    ```

*   **Winbox GUI:**
    *   In the `Bridge` interface, go to the `Ports` tab
    *   Click the `+` button to add a new port.
    *   Choose the desired interface to include in the bridge (e.g. `ether1`).
    *   Click `Apply` then `OK`.
    *   Repeat these steps to add more interfaces.

*   **After Configuration:** The `bridge-72` interface will now have the selected interfaces included as part of the L2 segment.

**4. Step 4: Configure the IP Pool**

*   **Explanation:** We need to create an IP pool that the hotspot will use to assign to clients connecting to the hotspot.

*  **Before Configuration:** There is no IP pool defined.

*   **CLI Command:**
    ```mikrotik
    /ip pool
    add name=hotspot-pool ranges=115.125.170.10-115.125.170.250
    ```

*   **Winbox GUI:**
    *   Go to `IP` -> `Pool`.
    *   Click on the `+` button.
    *   Set `Name` to `hotspot-pool`
    *   Set the range to `115.125.170.10-115.125.170.250`.
    *   Click `Apply` then `OK`.

*   **After Configuration:** The `hotspot-pool` will be created with the defined IP ranges.

**5. Step 5: Configure DHCP Server**

*   **Explanation:** We now need to create a DHCP server for our subnet. This DHCP server will use the IP pool defined in the previous step. The interface associated with this server will be the bridge itself.

*   **Before Configuration:** There is no DHCP server configured for the `bridge-72`.

*   **CLI Command:**
    ```mikrotik
    /ip dhcp-server
    add address-pool=hotspot-pool interface=bridge-72 lease-time=1d name=hotspot-dhcp
    /ip dhcp-server network
    add address=115.125.170.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=115.125.170.1
    ```

*   **Winbox GUI:**
    *   Go to `IP` -> `DHCP Server`.
    *   Click on the `+` button on `DHCP Servers` tab
    *   Set `Name` to `hotspot-dhcp`.
    *   Set `Interface` to `bridge-72`.
    *   Set `Address Pool` to `hotspot-pool`.
    *   Set `Lease Time` to `1d`
    *   Click `Apply` then `OK`.
    *   Go to the `Networks` tab.
    *   Click the `+` button
    *   Set `Address` to `115.125.170.0/24`.
    *   Set `Gateway` to `115.125.170.1`.
    *   Set `DNS Servers` to `8.8.8.8,8.8.4.4`.
    *   Click `Apply` then `OK`.

*   **After Configuration:** The DHCP server will be configured for bridge `bridge-72` and the DHCP Network will be configured to allow clients to connect to the network.

**6. Step 6: Create the Hotspot Server**

*   **Explanation:** Now, we need to create the Hotspot server itself, defining how clients authenticate. We will not use regular user/password authentication here. We will rely solely on MAC address authorization. We will associate the created address list to this hotspot.

*   **Before Configuration:** There are no Hotspot servers configured.

*   **CLI Command:**
    ```mikrotik
     /ip hotspot profile
    add name=mac-hotspot-profile address-pool=hotspot-pool dns-name="" html-directory=hotspot mac-cookie-timeout=3d transparent-proxy=no use-radius=no
    /ip hotspot
    add name=mac-hotspot interface=bridge-72 profile=mac-hotspot-profile address-per-mac=yes
    /ip hotspot user profile
    add name="mac-auth" shared-users=unlimited mac-address-list=mac-auth
    ```

*   **Winbox GUI:**
    *   Go to `IP` -> `Hotspot`.
    *   Go to the `Hotspot Profiles` tab.
    *   Click the `+` button.
    *   Set `Name` to `mac-hotspot-profile`
    *   Set `Address Pool` to `hotspot-pool`.
    *   Set `DNS Name` to `""`.
    *   Set `HTML Directory` to `hotspot`.
    *   Set `MAC Cookie Timeout` to `3d`
    *   Set `Transparent Proxy` to `no`
    *   Set `Use Radius` to `no`.
    *   Click `Apply` then `OK`.
    *   Go to the `Hotspot Servers` tab.
    *   Click the `+` button
    *   Set `Name` to `mac-hotspot`
    *   Set `Interface` to `bridge-72`
    *   Set `Profile` to `mac-hotspot-profile`
    *   Set `Address per MAC` to `yes`.
    *   Click `Apply` then `OK`.
    *   Go to the `User Profiles` tab.
    *   Click the `+` button
    *   Set `Name` to `mac-auth`
    *   Set `Shared Users` to `unlimited`
    *   Set `MAC Address List` to `mac-auth`
    *   Click `Apply` then `OK`.

*   **After Configuration:** The Hotspot server is active and uses the MAC address list for authentication.

**7. Step 7: Add Authorized MAC Addresses**

*   **Explanation:** Now, add the authorized MAC addresses to the `mac-auth` address list.  For testing, use a MAC Address of your choice, or from a machine you have at hand. In a real-world scenario, you would be adding MAC Addresses of clients you wish to authorize on the network.

*   **Before Configuration:** The `mac-auth` address list is empty.

*   **CLI Command (Example):**
    ```mikrotik
    /ip firewall address-list
    add list=mac-auth address=11:22:33:44:55:66
    ```

*   **Winbox GUI:**
    *   Go to `IP` -> `Firewall`.
    *   Go to the `Address Lists` tab.
    *   Select the `mac-auth` list.
    *   Click the `+` button.
    *   Enter the desired MAC address in the `Address` field.
    *   Click `Apply` then `OK`.
    * Repeat this to add more addresses to the list.

*   **After Configuration:** The `mac-auth` list will include the provided MAC addresses.

## Complete Configuration Commands:

```mikrotik
/ip firewall address-list
add list=mac-auth comment="Authorized MAC Addresses for MAC Server"
/interface bridge
add name=bridge-72
/interface bridge port
add bridge=bridge-72 interface=ether1
add bridge=bridge-72 interface=wlan1
/ip pool
add name=hotspot-pool ranges=115.125.170.10-115.125.170.250
/ip dhcp-server
add address-pool=hotspot-pool interface=bridge-72 lease-time=1d name=hotspot-dhcp
/ip dhcp-server network
add address=115.125.170.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=115.125.170.1
/ip hotspot profile
add name=mac-hotspot-profile address-pool=hotspot-pool dns-name="" html-directory=hotspot mac-cookie-timeout=3d transparent-proxy=no use-radius=no
/ip hotspot
add name=mac-hotspot interface=bridge-72 profile=mac-hotspot-profile address-per-mac=yes
/ip hotspot user profile
add name="mac-auth" shared-users=unlimited mac-address-list=mac-auth
/ip firewall address-list
add list=mac-auth address=11:22:33:44:55:66
```

## Common Pitfalls and Solutions:

*   **Issue:** Clients cannot access the network after connecting.
    *   **Solution:** Verify the MAC address added to the `mac-auth` list is correct. Double check the bridge interfaces and correct associated interfaces are connected to `bridge-72`.
    *   **Troubleshooting:** Use `Tools` -> `Torch` in Winbox to monitor traffic on `bridge-72`. Use `/ip dhcp-server lease print` to see if an IP address was offered to the client.
*   **Issue:** Client is connecting, but cannot access the Internet.
    *   **Solution:** Check the DHCP server configuration and the gateway configuration. Ensure the Mikrotik has a route to the internet, and a correctly configured NAT rule. Make sure that the DHCP server has a valid DNS configuration.
    *   **Troubleshooting:** Ping the gateway address from the Mikrotik (`/ping 115.125.170.1`). Use `/ip route print` to see the current active routes on the router.
*   **Issue:** High CPU Usage
    *   **Solution:** Check if any other processes are utilizing high cpu. The Hotspot and bridge features may cause high utilization if there are many connected clients. Consider upgrading to a more powerful router if needed.
    *   **Troubleshooting:** Use `/system resource print` and `/system profile` to see the current status and resource usage of the router.
*   **Issue:**  Router is not correctly forwarding connections.
    *   **Solution:** Check for other firewall rules that may be interfering, such as a blocking rule that might be in place. Make sure that NAT is enabled and that all client traffic is being correctly masked with the public IP address.
    *   **Troubleshooting:**  Use `/ip firewall filter print` and `/ip firewall nat print` to see the current rules applied on the firewall.

## Verification and Testing Steps:

1.  **Connect a client:** Connect a device with a known MAC address (e.g., `11:22:33:44:55:66`) to the network through an interface connected to `bridge-72`.
2.  **IP Address Verification:** Verify that the client receives an IP address from the `115.125.170.0/24` subnet. Check this via client-side commands (e.g., `ipconfig` on Windows, `ifconfig` on Linux/macOS) or through the Mikrotik command `/ip dhcp-server lease print`.
3.  **Internet Connectivity:** Ensure the client can access the internet. If the client gets an IP address but cannot reach the internet, try to ping the gateway IP (`115.125.170.1`) on the client side. If the ping is unsuccessful, then check if the MikroTik has a correct internet connection configured.
4.  **Try with different client**: Connect a second client with an unauthorized MAC address and see if it receives an IP. If this unauthorized client does not receive an IP, then the configuration is working as expected.

## Related Features and Considerations:

*   **Hotspot Customization:** You can customize the Hotspot login page and user profiles using HTML and CSS in the `html-directory`. Although not directly used for MAC authentication in this scenario, it can be used to display custom messages.
*   **MAC Address Filtering:** The MikroTik firewall allows even more advanced filtering based on MAC addresses. It is possible to define specific rules for specific source MAC addresses. For example, you could have a limited bandwidth rule for all devices except for those with a given MAC address.
*   **Address Lists:** Address lists can be used in a variety of places in MikroTik configuration. This feature is useful to group many different types of addresses, such as IP or MAC addresses.
*   **RADIUS Authentication:** For more complex scenarios, you can combine this MAC-based authentication with RADIUS for more granular control and centralized user management.
*   **Bridge Spanning Tree Protocol:** In more complex scenarios, where multiple switches are used to increase the number of clients connected, it is important to understand how the spanning tree protocol works. This feature helps to avoid loops in network infrastructures.

## MikroTik REST API Examples (if applicable):

While the Hotspot and bridge configurations can't be fully controlled via the REST API, you can manage the address list. Here are some examples:

**1. Add a MAC Address to the Address List:**

*   **Endpoint:** `/ip/firewall/address-list`
*   **Method:** `POST`
*   **JSON Payload:**
    ```json
    {
        "list": "mac-auth",
        "address": "AA:BB:CC:DD:EE:FF"
    }
    ```
*   **Expected Response (Success - HTTP 200 OK):**
    ```json
    {
       "message": "added",
       "id": "*2"
    }
    ```
*   **Error Handling:** If the list does not exist or if the input is incorrect, the API will return a 400 (Bad Request) error.

**2. Get a specific MAC Address from the Address List:**

*   **Endpoint:** `/ip/firewall/address-list`
*   **Method:** `GET`
*   **JSON Payload (Optional):** None
*   **URL Params:** `?.proplist=.id,.list,.address&list=mac-auth&address=AA:BB:CC:DD:EE:FF`
*   **Expected Response (Success - HTTP 200 OK):**
    ```json
    [
      {
        ".id": "*2",
        "list": "mac-auth",
        "address": "aa:bb:cc:dd:ee:ff"
      }
    ]
    ```
*   **Error Handling:** If the address does not exist in the list, the API will return an empty array `[]`

**3. Remove a MAC Address from the Address List:**

*   **Endpoint:** `/ip/firewall/address-list`
*   **Method:** `DELETE`
*   **URL Params:** `*1` (Where `*1` is an identifier of the record, this must be acquired from a previous GET call)
*   **JSON Payload (Optional):** None
*   **Expected Response (Success - HTTP 200 OK):**
    ```json
    {
      "message":"removed"
    }
    ```
*   **Error Handling:** If the address identifier is not correct, the API will return a 404 (Not Found) error.

**Note:** In these examples, the MikroTik REST API is assumed to be configured and accessible. You will need to enable and authenticate with the API before sending calls.

## Security Best Practices:

*   **MAC Address Spoofing:** Be aware that MAC addresses can be spoofed. This method should not be used as your sole security measure.
*   **Physical Access:** Secure physical access to the router. If an attacker gains physical access, they can bypass most security features and gain full control of the router.
*   **RouterOS Updates:** Keep RouterOS updated to the latest stable version to patch any security vulnerabilities. The current version (6.48) is dated, it is important to consider upgrading to version 7.x.
*   **API Security:** Disable the API if not needed, and restrict access to only needed IP addresses.
*   **Disable Unused Services:** Always disable any unused services, since these may be used by attackers to get access to the router.
*   **Strong Passwords:** Use strong passwords for all MikroTik user accounts.
*   **Firewall Rules:** Set up strong firewall rules to protect the router itself. Block any port that is not explicitly needed.

## Self Critique and Improvements:

*   **Simplicity:** This implementation relies entirely on MAC address authorization, which is less secure than combining MAC with RADIUS or other forms of authentication.
*   **Scalability:**  Managing a large number of MAC addresses manually can become cumbersome. For large networks, a RADIUS solution would be preferable.
*   **Limited Security:** While it provides a basic access control mechanism, it is not as robust as other methods. MAC addresses can be spoofed.
*   **Monitoring:** It would be advisable to add monitoring rules to quickly detect issues related to client connections.
*   **Error Handling:** While some troubleshooting and error handling were discussed, these could be expanded in a real-world environment. The current setup does not include logging features for troubleshooting.
*   **Improvement:** Implement RADIUS to handle user accounts centrally, also combined with the MAC address list to provide extra security.

## Detailed Explanations of Topic:

The MAC Server implementation uses the MikroTik Hotspot feature combined with an Address List that is configured as the `mac-address-list` on a specific Hotspot user profile.

*   **Hotspot:** The Hotspot service intercepts all HTTP requests on the selected interface, redirecting them to a login page. With this configuration, the Hotspot service authenticates clients based on their MAC address. In this implementation, no user login page is necessary, since the authentication is done directly using the address list.
*   **Address List:** The address list feature of RouterOS is extremely useful for creating groups of addresses that can be referenced in other parts of the configuration. These address lists can contain IP addresses, IP Ranges, or MAC Addresses.
*   **Bridge:** A bridge interface works by joining two or more interfaces into a single L2 segment. This means that traffic is transparently forwarded from one interface to another, as if they were connected by a switch.
*   **DHCP Server:** The DHCP server is responsible for automatically assigning IP addresses to clients connected to the network.

## Detailed Explanation of Trade-offs:

*   **MAC Address Authentication vs. RADIUS:** MAC authentication is simple to implement but provides limited security. It should not be used as the sole security method. RADIUS, while more complex, offers centralized authentication and stronger security with the possibility of using more authentication methods.
*   **Hotspot vs. Static IP:** The Hotspot provides a layer of control for the client's access to the network, but requires more configuration compared to static IP assignment. Static IPs are simpler, but they are also easier to abuse or spoof, and offer no central management.
*   **Bridge vs. Router:** A bridge provides layer 2 connectivity, meaning devices are on the same network. Routers provide layer 3 (IP) connectivity and can provide NAT, firewall, and advanced routing capabilities. A bridge will be more appropriate for local connections, while a Router will be more appropriate to manage connections to different networks or to the internet.
*   **Lease Time:** A DHCP lease time indicates how long an IP address is allocated to a specific client. A small lease time will reduce the chances of IP conflicts, while a bigger lease time will reduce the load on the router, and the number of DHCP requests it receives.

## Configuration for Specific RouterOS Versions:

The commands provided are compatible with both RouterOS 6.48 and later 7.x versions. There are no version specific commands being used in this setup. If a feature is not available or works differently on each version, the user should check the MikroTik documentation regarding that feature.

This document should provide a solid foundation for deploying a MAC-based authentication service within a Hotspot network using a MikroTik router. It's important to adjust and customize the configurations for the needs of your specific environment.

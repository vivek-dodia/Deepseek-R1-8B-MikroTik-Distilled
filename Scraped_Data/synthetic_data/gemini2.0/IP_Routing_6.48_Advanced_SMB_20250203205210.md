Okay, let's get into a detailed guide for IP routing on MikroTik RouterOS, targeting version 6.48 with a focus on a /24 subnet on a bridge interface.

## Scenario Description:

We will configure basic IP routing for a single subnet, `205.99.158.0/24`, on a bridge interface named `bridge-89`. This scenario represents a common setup in a small to medium business (SMB) network where a LAN segment is attached to a bridge, and that bridge interface needs to be assigned an IP address so devices on that segment can communicate and route traffic through the MikroTik. This setup is crucial for providing IP connectivity within the defined subnet.

## Implementation Steps:

**1. Step 1: Pre-Configuration State Check and Interface Verification**

* **Action:** Before we begin, verify that our target bridge interface (`bridge-89`) exists and has no prior IP configuration. We will use the CLI for the check.
* **Command (CLI):**
    ```mikrotik
    /interface bridge print
    /ip address print
    ```
* **Expected Output (Before):**
    - Output of `/interface bridge print` should show that `bridge-89` exists and is enabled.
    - Output of `/ip address print` should show that there is no IP address configured on `bridge-89` (unless there was a previous configuration that we are overriding).
* **Rationale:** We must ensure that the target interface exists, is enabled, and does not have any conflicting previous configurations to avoid issues.
* **Winbox GUI:**
    - Go to `Bridge` > `Interfaces` to view bridge interfaces and check the `Enabled` column.
    - Go to `IP` > `Addresses` to check existing IP addresses.

**2. Step 2: Assign an IP Address to the Bridge Interface**

* **Action:** Assign an IP address from our subnet, `205.99.158.0/24`, to the `bridge-89` interface. We will use `205.99.158.1/24`.
* **Command (CLI):**
    ```mikrotik
    /ip address add address=205.99.158.1/24 interface=bridge-89
    ```
* **Explanation of Parameters:**
    * `address=205.99.158.1/24`:  Specifies the IP address and subnet mask.
    * `interface=bridge-89`:  Specifies the target interface.
* **Expected Output (After):**
    - Output of `/ip address print` should now include an entry showing `205.99.158.1/24` assigned to `bridge-89`.
* **Rationale:** This assigns the router an IP on the specified subnet, allowing the router to participate in communications within the subnet.
* **Winbox GUI:**
    - Go to `IP` > `Addresses`, Click the `+` button to add new address.
    - Set the `Address` field to `205.99.158.1/24`.
    - Select `bridge-89` for the `Interface`.

**3. Step 3: Verify IP Address Assignment**

* **Action:** After applying the address, check if the configuration was successful.
* **Command (CLI):**
    ```mikrotik
    /ip address print
    ```
* **Expected Output:**
    - The output will list all the interface addresses, and must contain the new entry with address `205.99.158.1/24` assigned to interface `bridge-89`.
* **Rationale:** It is always important to verify the work that has been performed.
* **Winbox GUI:**
    - Go to `IP` > `Addresses` and check that the new address has been added to the list.

**4. Step 4: Enabling IP Forwarding**
   
* **Action:** While this isn't strictly needed if no routing is involved for non-local traffic (like routing to/from a WAN interface), enable IP forwarding by default, so that we do not forget about this step.
* **Command (CLI):**
    ```mikrotik
    /ip settings set ip-forward=yes
    ```
* **Explanation of Parameters:**
    * `ip-forward=yes`: Enables forwarding, which will allow this router to pass packets that are not destined for it, but are being routed through it.
* **Expected Output:**
    - We can verify by using `/ip settings print` and seeing that `ip-forwarding=yes`.
* **Rationale:** Even if not immediately required, enabling IP forwarding is usually needed for more advanced setups.
* **Winbox GUI:**
    - Go to `IP` > `Settings` and make sure the `IP Forwarding` checkbox is checked.

**5. Step 5: Test with `ping`**

* **Action:** We will test using a ping command from the router itself to verify that communication on the local subnet works. We will need to have a device connected to `bridge-89` with an IP address within the same subnet (for example `205.99.158.2/24`).
* **Command (CLI):**
    ```mikrotik
    /ping 205.99.158.2
    ```
* **Expected Output:**
    - If successful, the command will show ping replies from 205.99.158.2 and will show the time in milliseconds the reply took to arrive. If there is a firewall rule blocking the communication or if the device is not available, there will be no replies, and a message stating 'No reply from ....' will be present.
* **Rationale:** This test confirms the IP address was assigned correctly, and that the router is able to communicate on the specified subnet.
* **Winbox GUI:**
    - Go to `Tools` > `Ping`.
    - Enter the target IP address and click `Start`.

## Complete Configuration Commands:

```mikrotik
/interface bridge print
/ip address print
/ip address add address=205.99.158.1/24 interface=bridge-89
/ip address print
/ip settings set ip-forward=yes
/ip settings print
/ping 205.99.158.2
```

## Common Pitfalls and Solutions:

* **Problem:** Incorrect subnet mask specified on the IP address configuration.
   * **Solution:** Double check the subnet mask using `/ip address print` and correct it using the `/ip address set` command (specify the address and the interface).
* **Problem:**  Conflicting IP address on the same subnet.
   * **Solution:** Ensure that no other device has the same IP address as the router (`205.99.158.1`). Use `/ip arp print` or tools to identify other devices with that IP address.
* **Problem:** `bridge-89` does not exist or is not enabled.
   * **Solution:** Ensure that the bridge has been created in `/interface bridge` and enabled using the `enable` command within the bridge interface.
* **Problem:** Firewall rules are blocking the pings.
   * **Solution:** Check `/ip firewall filter print` to ensure there are no rules blocking ICMP packets destined for the router itself (input chain) or being generated by the router (output chain). Add rules to allow ICMP if necessary.
* **Problem:** IP forwarding is not enabled when it is expected.
   * **Solution:** Use `/ip settings set ip-forward=yes` and check with `/ip settings print`
* **Problem:** DNS configurations not in place in the router if the devices connected to this network are supposed to use it.
   * **Solution:** Set the correct DNS server on the router using `/ip dns set servers=8.8.8.8,1.1.1.1`, and then use `/ip dhcp-server network set dns-server=8.8.8.8,1.1.1.1` to pass the DNS information to devices connected to the subnet.

## Verification and Testing Steps:

1.  **Check IP Address:** Run `/ip address print` and confirm the address `205.99.158.1/24` is assigned to `bridge-89`.
2.  **Ping Local Device:** Ping a known device in the `205.99.158.0/24` network (e.g., `205.99.158.2`) from the RouterOS CLI using `/ping 205.99.158.2`. Expect successful replies.
3.  **Ping Router from Local Device:** Ping the router's IP address (205.99.158.1) from a device on the `205.99.158.0/24` network. Expect successful replies.
4.  **Use `torch`**: Use `/tool torch interface=bridge-89 duration=10` to observe traffic on the interface to confirm that the IP stack is working and that traffic is coming in.
5.  **Traceroute**: Use the traceroute utility from a device on the `205.99.158.0/24` network to another machine on a different network and verify that the MikroTik is the next hop in the route.

## Related Features and Considerations:

*   **DHCP Server:** To automatically assign IP addresses to devices on this subnet, configure a DHCP server on `bridge-89` using `/ip dhcp-server`.
*   **Firewall Rules:** Implement firewall rules to control traffic flow and enhance security on the subnet.
*   **Static Routes:**  If routing to other networks is required, add static routes using `/ip route add`.
*   **VLANs:** If you want to further segment your network, you can configure VLANs on the bridge interface and create more subnets accordingly.
*   **DNS:** Configure DNS settings within the DHCP server or manually on devices within the subnet.

## MikroTik REST API Examples (if applicable):

Let's show some practical REST API examples using MikroTik's API. To use these, you will need to have the RouterOS API enabled in the router settings, and be able to send HTTP requests to its port (usually 8728 for secure or 80 for unsecure).

**Example 1: Get IP Addresses**
```json
# API Endpoint: /ip/address
# Method: GET
# Authentication is usually done with the headers.
# In this case the request will be performed through command line for brevity.
# This command assumes you are logged in.
curl -s -k -H 'Content-Type: application/json'  https://192.168.88.1/rest/ip/address
```
*   **Expected Response (JSON):** This returns a JSON array of IP address objects, which includes our configured address on `bridge-89`.
    ```json
    [
        {
            ".id": "*0",
            "address": "205.99.158.1/24",
            "interface": "bridge-89",
            "network": "205.99.158.0",
            "version": "4"
        }
    ]
    ```
* **Explanation:** This GET request fetches all of the configured IP addresses on the router. The response is a JSON object with a key per configured IP address, each one containing details about the ip address, mask, interface and version.

**Example 2: Add IP Address**
```json
# API Endpoint: /ip/address
# Method: POST
# Authentication is usually done with the headers.
# In this case the request will be performed through command line for brevity.
# This command assumes you are logged in.

curl -k -s -H "Content-Type: application/json" -X POST -d '{
    "address": "205.99.158.5/24",
    "interface": "bridge-89"
}' https://192.168.88.1/rest/ip/address
```
*   **Request (JSON):** The JSON payload contains the `address` (including subnet mask) and the `interface` where the IP address is to be set.
    ```json
    {
      "address": "205.99.158.5/24",
      "interface": "bridge-89"
    }
    ```
*   **Expected Response (JSON):**  A successful response will return the new object created:
    ```json
    {
        ".id": "*1",
        "address": "205.99.158.5/24",
        "interface": "bridge-89",
        "network": "205.99.158.0",
         "version": "4"
    }
    ```
* **Explanation:** This POST request will add a new IP address to the router. The request body contains a JSON object with the parameters of the IP address configuration. The `address` parameter is a string in CIDR notation.

**Example 3: Deleting an IP Address**
```json
# API Endpoint: /ip/address
# Method: DELETE
# Authentication is usually done with the headers.
# In this case the request will be performed through command line for brevity.
# This command assumes you are logged in.

curl -k -s -X DELETE https://192.168.88.1/rest/ip/address/*1
```
*  **Expected Response:** A successful response is a status code of 204. In the command line no output will be generated.
* **Explanation:** This DELETE request will delete the IP address configuration identified by `*1` (which is the `.id` of the configuration we added in example 2)

## Security Best Practices:

*   **Firewall:** Implement firewall rules that allow the minimum traffic required to protect the network and the router itself.
*   **RouterOS Version:** Keep RouterOS updated to the latest version with security patches.
*   **Strong Passwords:**  Use a strong password for the admin user, or, if possible, create specific users and avoid the default `admin`.
*   **API Security:** Disable the API if not used, or only allow access to it through specific addresses or networks. Consider using HTTPS for secure access.
*   **Disable Unused Services:** Disable unused services on the router.
*   **Avoid Default Ports:** Consider using a different port for accessing the API, Winbox or SSH service.
*   **Access control:** Ensure that access to the router is controlled using IP filtering or source address restriction.
*   **Audit Log:** Check the audit logs frequently to detect any changes or suspicious behaviour.

## Self Critique and Improvements:

This configuration covers the basic IP routing functionality for a single subnet on a MikroTik router. Here are some improvements that could be made:
*   **DHCP Server Configuration:**  Add a DHCP server configuration, which is common on this kind of setup.
*   **More Complex Routes:** This example only has one subnet, and no gateway is configured. This could be expanded to create more realistic setups with multiple networks and external gateways.
*   **Firewall Rules:** Specific firewall rules were not configured in this example. This is a critical aspect of security and a working configuration should have a basic set of rules to avoid accidental misconfiguration or unwanted behaviour.
*   **Logging:** Add some logging for diagnostic purposes.
*   **Rate limiting:** Add rate limits for specific protocols or interfaces.
*   **QoS:** Configure QoS if necessary for optimal traffic prioritization.

## Detailed Explanations of Topic:

IP routing is the process of forwarding IP packets from one network to another. In MikroTik, the routing table is used to make routing decisions. It contains information about destination networks and the next hop to reach those networks.

Key Concepts in MikroTik IP Routing:
*   **IP Addresses and Subnets:** An IP address is a logical address assigned to a device on a network. A subnet mask defines which portion of the IP address represents the network and which represents the host.
*   **Interfaces:**  Network interfaces are physical or logical connection points on the router.
*   **Routing Table:** A table containing the routes the router knows about.  These can be manually added (static) or learned through routing protocols (dynamic).
*   **Next Hop:** The next IP address in the route towards the final destination network.
*   **Default Route:** The route used when no other matching route is found. It is often pointed to the gateway.
*   **IP Forwarding:** Enables or disables the router's ability to forward packets between interfaces.
*   **Static Routes:** Routes manually configured by the administrator.
*   **Dynamic Routes:** Routes learned automatically through routing protocols (OSPF, BGP, etc).

## Detailed Explanation of Trade-offs:

*   **Static vs Dynamic Routing:**
    *   **Static:** Simple for small, unchanging networks. Requires manual configuration but provides very direct control over the routing. Can be less flexible when the network grows or changes.
    *   **Dynamic:**  Scales well for large, complex networks. Automatically learns and adapts to changes in network topology. More complex to configure and requires a solid understanding of the routing protocols used. Can have additional overhead on the router itself.
*   **Bridge Interface vs Separate Interfaces:**
    *   **Bridge:** Useful for simplifying network management when multiple devices share the same broadcast domain (e.g., a LAN segment), or the devices require broadcast communication with other devices in the same network. There is a single layer 2 interface.
    *   **Separate Interfaces:** Useful for greater segmentation and management of different network segments, requiring routing between each one. Each interface will be a different broadcast domain.
*   **Firewall Rules:**
    *   **Too permissive:** Can open up the router to security risks and leave the network unprotected.
    *   **Too restrictive:** Can block legitimate traffic and break the intended functionality.
    *   **Optimal:** Requires careful planning and must allow only the necessary traffic.
*   **DHCP Server:**
    *   **Using DHCP:** Simplifies IP address assignment on the subnet. Requires an active server configuration.
    *   **Static:** Manual IP assignment can be more complex, but provides the most control over the address assignment.
*  **IP Forwarding:**
    *  **Enabled:** Allows the router to forward packets between interfaces. If not enabled, the router will not perform any routing. It also consumes more CPU cycles.
    *  **Disabled:** Blocks the router from forwarding packets. Useful in scenarios where there is only one network connected, or in cases where the router should never forward packets. Consumes less CPU.

## Configuration for Specific RouterOS Versions:

All the commands used in this example are valid for RouterOS version 6.48. If the instructions are to be used for RouterOS version 7.x there are two small differences:

1. The `ip-forward` setting, which can be found at `/ip settings` in 6.x has been moved to the top level of the `/ip` settings in 7.x. This means that in version 7 the correct command is `/ip set forwarding=yes` instead of `/ip settings set ip-forward=yes`. Also, this setting can be found at the top level in Winbox at `IP>Settings` instead of under `IP>Settings`.
2. Some of the fields in the output of the commands may have different names or output format, but the behaviour of the commands will remain the same.

This complete guide covers a basic IP routing scenario on MikroTik RouterOS with detailed explanations, practical examples, API calls and considerations. Remember to always test any configuration in a lab environment before applying it to a production network.

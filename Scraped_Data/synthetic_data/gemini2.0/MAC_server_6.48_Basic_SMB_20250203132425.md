Okay, let's dive into a detailed documentation for setting up a MAC server on a MikroTik router running RouterOS 6.48, focusing on a basic SMB scenario with a specific subnet and interface.

## Scenario Description:

We will configure the MikroTik router to act as a MAC server, listening for MAC address requests on a specific interface (`ether-96`). This is often used in network environments where you might want to implement MAC-based access control, DHCP reservation by MAC address, or other MAC-specific services. We'll use the subnet `74.74.67.0/24` as context but this configuration focuses on the MAC server itself, not IP address assignment. The MAC server feature allows you to create a list of MAC addresses that will respond with an IP address when a MAC address request is sent.

## Implementation Steps:

Here's a step-by-step guide to configure the MAC server on your MikroTik router using CLI commands and also, where relevant, through Winbox:

1. **Step 1: Enable the MAC Server Feature and Add a MAC Address Entry**

   *   **Explanation:** We need to enable the MAC server globally and add a specific MAC address we want to listen for and respond to. By default, the MAC server is disabled, so we start by enabling it. We then add a sample entry. This entry pairs a MAC address with an IP address. It is important to note that the MAC server does not assign the IP address to the client automatically.
   *   **CLI Before:**

        ```mikrotik
        /interface ethernet print
        # Typically no MAC server configuration exists by default.
        /ip mac-server print
        ```

    * **Winbox Before:**
         *   Navigate to `/IP/MAC Server` on the sidebar, and observe that no configuration is in place yet.
         * Navigate to `/Interface` and observe the current interfaces
   *   **CLI Configuration Command:**

        ```mikrotik
        /ip mac-server set enabled=yes
        /ip mac-server add interface=ether-96 mac-address=00:11:22:33:44:55 address=74.74.67.100
        ```

   *   **CLI After:**

        ```mikrotik
        /ip mac-server print
        # Should show:
        # enabled: yes
        #
        /ip mac-server print
        # Should show the added entry similar to
        # Columns: address, interface, mac-address, disabled
        #
        #  0 address=74.74.67.100 interface=ether-96 mac-address=00:11:22:33:44:55 disabled=no
        ```

    *  **Winbox After:**
         *   Navigate to `/IP/MAC Server` on the sidebar. You should see the MAC server enabled, and an entry with your configured `mac-address` and `address`.

2. **Step 2: Configure the Interface to Use MAC Server**

   *   **Explanation:** While the MAC server is enabled, it won't do anything until an interface is assigned to make use of it. Here we are setting the interface to listen for MAC address requests, enabling the specified `interface` (ether-96) to listen for MAC address requests.
   *   **CLI Before:**

        ```mikrotik
        /interface ethernet print
        # Check configuration of ether-96 (no MAC server specifics)
        ```

    * **Winbox Before:**
        *Navigate to `/Interface/Ethernet` and click `ether-96` and view the config. Note there is no MAC server specific config.

   *   **CLI Configuration Command:**

        ```mikrotik
        /interface ethernet set ether-96 mac-server=yes
        ```

   *   **CLI After:**

        ```mikrotik
        /interface ethernet print
        # Check configuration of ether-96. `mac-server=yes` should be present
         /interface ethernet get ether-96
        # Should show, among other information, "mac-server: yes"
        ```
    *  **Winbox After:**
        *Navigate to `/Interface/Ethernet`, and click `ether-96`. On the `General` tab, you'll see the `MAC Server` option is now checked.

## Complete Configuration Commands:

```mikrotik
# Enable the MAC server globally
/ip mac-server set enabled=yes

# Add a MAC address entry for interface ether-96
/ip mac-server add interface=ether-96 mac-address=00:11:22:33:44:55 address=74.74.67.100

# Set interface ether-96 to use the MAC server
/interface ethernet set ether-96 mac-server=yes
```
| Parameter              | Explanation                                                                                                                                  | Example Value       |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| `/ip mac-server set enabled` | Enables or disables the MAC server globally                                                                                                       | `yes` or `no`     |
| `/ip mac-server add interface`   |  Specifies the interface to use                                                                                                          | `ether-96`     |
| `/ip mac-server add mac-address`| The MAC address to match                                                                                                                  | `00:11:22:33:44:55` |
| `/ip mac-server add address`  | The IP address that is associated with the MAC address. *Note that the client is not automatically assigned this address.*                         | `74.74.67.100`     |
| `/interface ethernet set <interface> mac-server` | Enables or disables the MAC server for a specific interface                                                                | `yes` or `no`     |

## Common Pitfalls and Solutions:

*   **Problem:** MAC server is enabled but doesn't respond.
    *   **Solution:** Ensure the correct interface is configured to use the MAC server (`mac-server=yes`). Double-check the MAC address is entered correctly. Use the `/interface ethernet print` command or Winbox's Interface screen to confirm.
*   **Problem:** The MAC server entry doesn't work for the given interface
    *   **Solution:** Verify that the `interface` setting in the `/ip mac-server add` matches the interface where the MAC requests are sent. Check if any firewall rules are blocking the request from coming from or leaving the interface, and ensure the destination address is in your specified subnet.
*   **Problem:** Misconfigured MAC addresses.
    *   **Solution:** Double check the MAC addresses, and ensure they are all properly formatted (using colons as separators). MAC addresses are case-insensitive.

*   **Problem:** High CPU usage with many MAC server requests.
    *   **Solution:** If you have many devices making MAC server requests, or a large number of entries in your MAC server configuration, it can potentially cause an increase in CPU usage. Evaluate if a MAC server is needed for all clients and only enable it for those that do.

## Verification and Testing Steps:

1.  **Use `torch` to capture MAC server requests:** On the MikroTik Router, use the torch tool to capture traffic on the `ether-96` interface. You should see the MAC requests coming from your network.

    ```mikrotik
    /tool torch interface=ether-96 mac-address=00:11:22:33:44:55 duration=60
    ```
    If you send a request from a device with the MAC address `00:11:22:33:44:55` you should see it in the output. Note that MAC requests are broadcast at the layer 2 level, so even a simple `ping` command will show up in torch.

2.  **Check the MAC Server entry:** Make sure the correct entry is present
    ```mikrotik
    /ip mac-server print
    ```
    and ensure the `address`, `interface` and `mac-address` are correct.
3.  **Use a network tool on a client machine:**
    * Run an Arp request on the client on a command line for your specific IP address, this will cause a MAC request for the IP address, and that should show up in the torch output.
    * Example: `ping 74.74.67.100`

## Related Features and Considerations:

*   **DHCP Server:** The MAC server can be used in conjunction with a DHCP server for static leases. You can define a lease for a specific MAC address. If a client has a static lease, the lease will take priority over the MAC server configuration.
*   **Firewall:** Firewall rules can affect the MAC server. If you are not seeing requests being matched, verify that your firewall isn't blocking your Layer 2 requests.
*   **MAC-based VLAN:** You can use the MAC server with VLANs to isolate traffic by MAC address.

## MikroTik REST API Examples:

Since the MAC Server operates at layer 2, there is no direct REST API to fetch layer-2 information. The most relevant API endpoint for this context is `/ip/mac-server`.

1. **Fetching MAC Server Entries:**

   *   **API Endpoint:** `/ip/mac-server`
   *   **Request Method:** `GET`
   *   **Example cURL Command:**

        ```bash
        curl -k -u 'admin:password'  https://<your-router-ip>/rest/ip/mac-server
        ```

   *   **Example Response:**
        ```json
        [
            {
                ".id": "*1",
                "address": "74.74.67.100",
                "interface": "ether-96",
                "mac-address": "00:11:22:33:44:55",
                "disabled": false
            }
        ]
        ```

2. **Adding a MAC Server Entry:**

   *   **API Endpoint:** `/ip/mac-server`
   *   **Request Method:** `POST`
   *   **Example JSON Payload:**

        ```json
        {
            "interface": "ether-96",
            "mac-address": "00:AA:BB:CC:DD:EE",
            "address": "74.74.67.101"
        }
        ```
    * **Example cURL Command:**
         ```bash
            curl -k -u 'admin:password' -H "Content-Type: application/json" -d '{ "interface": "ether-96", "mac-address": "00:AA:BB:CC:DD:EE", "address": "74.74.67.101" }'  https://<your-router-ip>/rest/ip/mac-server
        ```

    *   **Example Response:**
        ```json
        {
            "message": "added"
        }
        ```

3.  **Error Handling:** If the API request fails, the response will contain an error message. For example, if you try to create a MAC server entry with an existing `mac-address` and `interface`, the response will be:
     ```json
      {
          "message": "already have such entry"
        }
     ```
     You should use this output to diagnose the specific error, and perform a new request based on the returned error message.

## Security Best Practices:

*   **Secure Access:**  Use strong passwords for the MikroTik router and disable access methods that you do not need.
*   **Firewall Rules:** Ensure that only authorized networks can connect to the MikroTik and the MAC Server.
*   **MAC Spoofing:** Be aware that MAC addresses can be spoofed, so don't rely on the MAC server as the only form of security. Use it in combination with other measures.
*   **Limit Access:** Control who has access to modify the MAC server configuration.

## Self Critique and Improvements:

This configuration provides a basic setup for a MAC server. Here are a few ways it could be improved:

*   **More Entries:** For larger networks, you'd need to add more MAC address entries. The API could be useful here to automate the process.
*   **Dynamic Updates:** A script could be written to dynamically add or remove MAC entries based on other data sources (like a device database).
*   **Integration with DHCP Server:**  Integrating the MAC server information with the DHCP server to automate static lease assignment would be a valuable enhancement.
*  **Logging:** Implement logging for when MAC addresses are requested, for better network auditing and security analysis.

## Detailed Explanation of Topic:

The MikroTik MAC server is a feature that enables the router to respond to layer 2 requests based on configured MAC addresses. When the router receives a MAC address request, it checks its MAC server table. If it finds a matching MAC address on the specified interface, it responds with the associated IP address. This is useful for various scenarios, such as:

*   **Network Discovery:** Discovering clients by their MAC address, and identifying their IP address.
*   **MAC-Based Authentication/Authorisation:** In combination with other features, this can create a more secure network access control method.
*   **Static Address Assignment:** You can use this feature to assign IP addresses based on MAC address. This can be further integrated with the DHCP server.

## Detailed Explanation of Trade-offs:

*   **Manual Configuration:** Manually entering MAC addresses is tedious and error-prone. Consider using the API for bulk uploads and a database to maintain addresses.
*   **Security:** Relying solely on MAC address filtering is not secure. MAC addresses are easily spoofed. Implement additional security measures like 802.1x or VPNs.
*   **Scalability:** With a large number of entries, management becomes cumbersome. This can be mitigated by using scripts and automation.
*   **Resource Usage:**  If you create a large number of entries, the router has to search through that data on every request.

## Configuration for Specific RouterOS Versions:

This configuration is valid for MikroTik RouterOS version 6.48. The commands used are consistent and available across the RouterOS 6.x versions. For versions 7.x, the commands and their behavior are still present, so there should be no incompatibilities. It is advisable to check the release notes for specific router OS releases. For this specific example there are no significant differences.

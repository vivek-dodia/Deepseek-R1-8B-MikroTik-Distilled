Okay, let's craft some detailed documentation for setting up a MAC server on a MikroTik router, specifically targeting RouterOS 7.12 (and providing notes for 6.48/7.x compatibility) within an Enterprise network scale scenario. This will use a subnet of `142.169.73.0/24` and the interface `wlan-6`.

## Scenario Description:

This document describes configuring a MAC server on a MikroTik router, listening for MAC addresses on a specific interface, to then use it for other services (e.g., DHCP, Hotspot). In our scenario, we aim to configure a MAC server to operate on the `wlan-6` interface and monitor devices connected to this interface, possibly for user registration and access control. The MAC server itself does not do anything, but rather acts as a lookup table, allowing other services to do things based on MAC addresses.

## Implementation Steps:

Here's a detailed step-by-step guide to implementing the MAC server:

**Detailed Explanation of Topic: MAC Server**
The MAC server on MikroTik, is not an actual service that *does* something. Instead, it creates an active list of mac addresses and their associated interfaces, that other RouterOS services can use to implement rules. For instance, you can use the MAC server as an identification source to:
- Block MAC addresses
- Allow MAC addresses
- Implement a DHCP server, that only serves a specific range of IP's to known MAC addresses.
- Implement a Hotspot server, that only allows specific MAC addresses.
- Create simple access lists.

1.  **Step 1: Verify Interface Existence**
    Before configuring the MAC server, we need to ensure that the interface `wlan-6` exists and is properly configured.

    *   **CLI Command (Before):**

        ```mikrotik
        /interface print
        ```

        This command lists all interfaces. Check if `wlan-6` is present, and note down its current status (enabled, disabled, etc).

    *   **Winbox GUI (Before):** Go to *Interfaces* and verify if interface `wlan-6` exists.
    *   **Action:** Verify the interface `wlan-6` exists. If not, it must be created and configured.
    *   **CLI Command (After, if creating the interface):**
        ```mikrotik
        /interface wireless add name=wlan-6 mode=ap-bridge ssid="YourWiFiSSID" band=2ghz-b/g/n frequency=auto security-profile=default
        /interface enable wlan-6
        ```
        **NOTE:** Customize the WiFi parameters (SSID, frequency, etc.)
        *   **Explanation:** The above commands will create a wireless interface named wlan-6 and enable it.
    *   **Winbox GUI (After, if creating the interface):** Go to *Wireless* and create a new interface by pressing the "+" button. Set the parameters, and enable it.
    *   **Effect:** The `wlan-6` interface exists and is active.

2.  **Step 2: Create a MAC Server Configuration**
    Now, we create the MAC server instance, we must create one that will use the `wlan-6` interface.

    *   **CLI Command (Before):**

        ```mikrotik
        /mac-server print
        ```

        This command will print any existing MAC server instances. We expect that there isn't any on a fresh configuration.

    *   **Winbox GUI (Before):** Navigate to *MAC Server*. There should be nothing there in a fresh configuration.
    *   **Action:** Create the MAC Server Instance.
    *   **CLI Command (After):**

        ```mikrotik
        /mac-server add interface=wlan-6
        ```

        *   **Explanation:** This command adds a new MAC server instance that will listen on the `wlan-6` interface.
    *   **Winbox GUI (After):** Navigate to *MAC Server* and click the "+" to add a new instance. Select wlan-6 as the interface, and leave the rest as is, then press "Apply" and "OK".
    *   **Effect:** The MAC server is now enabled on interface `wlan-6`

3.  **Step 3:  Verify MAC Addresses are Being Registered**
    The mac server by itself does not do anything. But other services can utilize the registered MAC addresses. Check that you can see mac addresses appearing.

    *   **CLI Command:**

        ```mikrotik
        /mac-server print detail
        ```

        *   **Explanation:** This command displays the MAC addresses that have connected to the interface.

    *   **Winbox GUI:** Navigate to *MAC Server*. You should be able to see a list of the registered MAC addresses on the bottom.
    *   **Effect:** The MAC server is now listing all of the connected MAC addresses. You can use these in other services, such as DHCP server, hotspot, etc.

## Complete Configuration Commands:

```mikrotik
# Ensure interface exists, enable it if needed
/interface wireless add name=wlan-6 mode=ap-bridge ssid="YourWiFiSSID" band=2ghz-b/g/n frequency=auto security-profile=default
/interface enable wlan-6
# Add MAC server instance for wlan-6
/mac-server add interface=wlan-6
# Print detail of MAC addresses
/mac-server print detail
```

## Parameter Explanation

| Command/Parameter | Description                                                                                                                                 |
| :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| `/interface wireless add` | Creates a new wireless interface                                                                                             |
| `name`            | Name of the interface, e.g., `wlan-6`.                                                                                                   |
| `mode` | Wireless mode (ap-bridge, station, etc), in this case we want an access point                              |
| `ssid`            | SSID of the wireless network.                                                                                                          |
| `band`            | Wireless band frequency.                                                                                                        |
| `frequency`       | Specific frequency or `auto`.                                                                                                          |
| `security-profile` | Profile to be used for authentication, usually the default is sufficient.                               |
| `/interface enable` | Enable the interface created |
| `/mac-server add`    | Creates a new mac server                                                                                |
| `interface`       | Specifies the interface where the MAC server will listen, in our case, `wlan-6`.                                                          |
| `/mac-server print` | Display the mac server configurations. Adding the parameter `detail` will show the individual mac addresses                                   |

## Common Pitfalls and Solutions:

1.  **Interface Not Enabled:**
    *   **Problem:** The `wlan-6` interface is disabled or incorrectly configured, hence the MAC server will not detect devices.
    *   **Solution:** Use `/interface enable wlan-6` to enable it and make sure the wireless parameters are correct (SSID, security, etc). Check the `/interface wireless monitor` to see if the interface is working correctly.

2.  **Wrong Interface Selected:**
    *   **Problem:** The MAC server instance is not set to the intended interface.
    *   **Solution:** Verify the interface parameter in the `/mac-server print` output. If it’s wrong, use `/mac-server remove [ID]` to remove and `/mac-server add interface=wlan-6` to fix. Replace `[ID]` with the actual id, that you will find with the command `/mac-server print`.

3.  **No Devices Connecting:**
    *   **Problem:** No devices are connecting to `wlan-6`.
    *   **Solution:** Check the wireless settings, ensure the SSID is visible, and that client devices have the correct password. Check the wireless settings (such as frequencies and channels) to be sure that your target devices can connect to that frequency band. Also check the wireless logging by using `/system logging print` and then `/system logging add topics=wireless action=memory`.

4.  **Resource Issues:**
    *   **Problem:** If the number of devices on the wireless network is very high, this might cause the device to have issues.
    *   **Solution:** Monitor CPU and memory usage using `/system resource print`. If resources are very high, consider reducing the device count per AP, or move to a more powerful MikroTik device.

## Verification and Testing Steps:

1.  **Check MAC Server Status:**
    *   **CLI:** Use `/mac-server print` to check the MAC server instance.
    *   **Winbox:** Navigate to *MAC Server*. Verify that the instance is correctly configured and enabled.
2.  **Check Registered MAC Addresses:**
    *   **CLI:** Use `/mac-server print detail` to list all connected MAC addresses.
    *   **Winbox:** Navigate to *MAC Server*. See the registered mac addresses at the bottom.
3.  **Monitor Device Connection:** Connect a test device to the `wlan-6` network and check if its MAC address is registered using the command in step 2.
4.  **Use Torch Tool:**
    *   **CLI:** Use `/tool torch interface=wlan-6` to check network traffic. This will confirm that traffic is passing over the interface, ensuring that the interface is properly configured.

## Related Features and Considerations:

*   **DHCP Server:** Use registered MAC addresses in conjunction with a DHCP server to assign fixed IPs to specific devices based on MAC address in `/ip dhcp-server lease`.
*   **Hotspot:** Restrict access to the Hotspot based on the MAC server by using MAC address based registration rules in `/ip hotspot user`.
*   **Access Lists:** Implement simple MAC address based allow/block lists using the `mac-address-list` in `/interface bridge port`.
*   **Advanced Hotspot Features:** Implement MAC-address registration and user management in the Hotspot environment, using the MAC server as an identity source.

## MikroTik REST API Examples (if applicable):

The RouterOS REST API is not the best option for directly managing MAC addresses, as there isn't any explicit API call to get a list of the connected mac addresses, however the API can be used to configure a mac server. However, you can configure a MAC server instance. Here's how:

1.  **Create a MAC Server instance via API**
    *   **Endpoint:** `/mac-server`
    *   **Method:** `POST`
    *   **JSON Payload:**

        ```json
        {
          "interface": "wlan-6"
        }
        ```

    *   **Expected Response (Success - 201 Created):**

        ```json
        {
            "message": "added",
            ".id":"*3"
        }
        ```
    *   **Error Handling:** If an error occurs (e.g. the interface does not exist), you'll get a 400 code with the `message` field giving the error description.

2.  **Read MAC server via API**
    *   **Endpoint:** `/mac-server`
    *   **Method:** `GET`
    *   **JSON Payload:** None

    *   **Expected Response (Success - 200 OK):**

        ```json
        [
          {
            "interface": "wlan-6",
            ".id": "*3",
            "disabled":"false"
          }
        ]
        ```
    *   **Error Handling:** If an error occurs, you'll get a 400 code with the `message` field giving the error description.

3.  **Delete MAC server via API**
   *   **Endpoint:** `/mac-server/*3`
   *   **Method:** `DELETE`
   *   **JSON Payload:** None

    *   **Expected Response (Success - 200 OK):**
    ```json
    {
        "message":"removed"
    }
    ```
    *   **Error Handling:** If an error occurs, you'll get a 400 code with the `message` field giving the error description.

**Notes on using the API**

*   RouterOS API uses the `.id` to identify specific instances. In the examples, the id `*3` is used, but in your setup, it may be different. You must fetch the mac-servers via `GET` and find the correct id to delete or modify existing mac servers.
*   Always include a content-type header in the API requests for the body parameters with the value: `Content-Type: application/json`.
*   Always authenticate using an API token.

## Security Best Practices

*   **Interface Security:** Ensure the `wlan-6` interface has adequate security in terms of authentication. Make sure you are using WPA2 or WPA3 to avoid any easy brute force attacks against your wifi network.
*   **API Security:** Protect the API with strong passwords and a strong firewall. Never expose the API to the internet without a VPN or similar. Make sure you create a specific user for the API access, and limit the permissions of the API user to only what is needed.
*   **MAC Address Spoofing:** While the MAC server registers MAC addresses, consider that these can be spoofed and can be used to bypass some restrictions. If using a system that is based on mac-addresses, make sure the level of security is appropriate.

## Self Critique and Improvements

*   **MAC Address Whitelist/Blacklist:** This implementation only registers the MAC addresses but doesn't automatically add them to an allow/block list. An improvement could be to create scripts or dynamic lists based on the server's data, for example using a script to constantly update a static list based on the detected MAC addresses.
*   **Error Handling:** The error handling is basic. It could be improved with logging and more descriptive error messages to specific log files.
*   **API Usage:** As noted, the API doesn't have direct access to the registered MAC address. One way to get around it, would be to run a script on the router, that periodically uploads the mac addresses list to an external server, that can then be accessed via the API, or you can use RouterOS built-in features to send the info to a remote log server, that can be accessed using the appropriate methods.

## Detailed Explanation of Trade-offs:

*   **Manual vs. Dynamic Lists:** Manually managed lists of MAC addresses are easier to implement, but dynamic lists are more scalable. For larger networks, manually maintaining lists becomes impractical.
*   **MAC vs. Other Identification:** MAC addresses can be easily spoofed. For security-sensitive applications, consider using more robust authentication methods (like WPA2/WPA3, Radius based authentication, certificates, etc.).
*   **Centralized vs. Decentralized Management:** For large networks, a centralized MAC address management system is better to simplify the management of rules, allowing you to configure each router individually, using a central database.

## Configuration for Specific RouterOS Versions:

*   **RouterOS 7.12:** The provided commands are fully compatible with version 7.12.
*   **RouterOS 7.x (Earlier versions):** The commands will work on any RouterOS 7.x version, as no specific version features are used in the configuration.
*   **RouterOS 6.48:** All commands related to the mac server and basic interface configurations are compatible. Wireless parameters are very similar and may require slight adjustments to the parameters based on the interface and device.

This complete document provides the essential information to configure a MAC server on a MikroTik router, covering a detailed explanation, implementation, troubleshooting, security practices, and future improvements. Remember to always check the official MikroTik documentation for the most up-to-date information.

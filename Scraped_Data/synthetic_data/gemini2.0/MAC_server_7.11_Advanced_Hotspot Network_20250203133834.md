Okay, let's dive deep into configuring a MAC server on a MikroTik RouterOS 7.11 device within the context of a Hotspot network, specifically using `ether-6` on the subnet `104.67.132.0/24`.

## Scenario Description:

We will configure a MAC server on our MikroTik router that listens on interface `ether-6`. The MAC server allows authorized clients to connect to the network based solely on their MAC address. This is useful in scenarios like:

- **Simplified Hotspot Access**: Where users can connect with their devices without explicit login procedures if their MAC address is pre-approved.
- **Limited Access Networks**: Granting access only to specific devices, ignoring IP based authentication.
- **Temporary Device Access**: Allowing temporary access for specific devices that require no user interaction.

We'll specifically use subnet `104.67.132.0/24` and the interface `ether-6` as the foundation of the network. This configuration will not provide network access on any other interface.

## Implementation Steps:

Here's a step-by-step guide to configuring the MAC server, including CLI and Winbox instructions.

**1. Step 1: Configure the IP Address on the Interface**

*   **Description:** Assign an IP address to the `ether-6` interface. This is the basis of communication on the network segment.
*   **Before Configuration:** The `ether-6` interface likely has no IP address.
*   **CLI Instructions:**

    ```mikrotik
    /ip address
    add address=104.67.132.1/24 interface=ether-6 network=104.67.132.0
    ```

*   **Winbox GUI:**
    *   Navigate to `IP` -> `Addresses`.
    *   Click the `+` button to add a new address.
    *   Enter the `Address`: `104.67.132.1/24`.
    *   Select the `Interface`: `ether-6`.
    *   Click `Apply` and then `OK`.
*   **After Configuration:** The interface `ether-6` is configured with the IP address `104.67.132.1/24`.
*   **Effect:** This step enables the router to communicate on the specified subnet via `ether-6`.

**2. Step 2: Enable the MAC Server**

*   **Description:** Activate the MAC server functionality on the `ether-6` interface.
*   **Before Configuration:** The MAC server is disabled by default.
*   **CLI Instructions:**

    ```mikrotik
    /interface mac-server
    add interface=ether-6 disabled=no
    ```

*   **Winbox GUI:**
    *   Navigate to `Interface` -> `MAC Server`.
    *   Click the `+` button to add a new MAC server instance.
    *   Select the `Interface`: `ether-6`.
    *   Uncheck the `Disabled` box.
    *   Click `Apply` and then `OK`.
*   **After Configuration:** The MAC server is enabled on `ether-6`.
*   **Effect:** The router will now listen for client MAC addresses connecting to `ether-6` and process them based on its configured rules.

**3. Step 3: Add Allowed MAC Addresses**

*   **Description:** Define the specific MAC addresses that are allowed to connect via the MAC server.
*   **Before Configuration:** No MAC addresses are allowed by default.
*   **CLI Instructions:**

    ```mikrotik
    /interface mac-server mac-address
    add address=AA:BB:CC:DD:EE:FF comment="Device 1" server=ether-6
    add address=00:11:22:33:44:55 comment="Device 2" server=ether-6
    ```
    **Note**: Replace `AA:BB:CC:DD:EE:FF` and `00:11:22:33:44:55` with the actual MAC addresses you want to allow.
*   **Winbox GUI:**
    *   Navigate to `Interface` -> `MAC Server` -> `MAC Addresses` tab.
    *   Click the `+` button to add a new allowed MAC address.
    *   Enter the `Address` (e.g., `AA:BB:CC:DD:EE:FF`) and an optional `Comment` (e.g., `Device 1`).
    *   Select the `Server`: `ether-6`.
    *   Click `Apply` and then `OK`.
    *   Repeat for other allowed MAC addresses.
*   **After Configuration:** The listed MAC addresses are permitted to connect through the MAC server.
*   **Effect:** Only devices with a MAC address configured on the MAC server will be allowed to connect through the interface.

**4. Step 4: (Optional)  Enable Logging (for diagnostic)**

*   **Description:** Configure logging to see if clients are connecting or denied.
*   **Before Configuration:** Logging is not enabled.
*   **CLI Instructions:**
```mikrotik
    /system logging action
    add name=mac-server-log target=memory
    /system logging
    add topics=mac-server action=mac-server-log
```
*   **Winbox GUI:**
    *   Navigate to `/System/Logging/Actions` and click on the `+` to add `mac-server-log`, select `memory` as target.
    *   Navigate to `/System/Logging` and click on the `+` to add `mac-server` as `topic`, select the recently created `mac-server-log` as action.
*   **After Configuration:** Any MAC server related traffic will be logged to memory.
*   **Effect:** Easier to debug MAC server activity.

## Complete Configuration Commands:

```mikrotik
/ip address
add address=104.67.132.1/24 interface=ether-6 network=104.67.132.0

/interface mac-server
add interface=ether-6 disabled=no

/interface mac-server mac-address
add address=AA:BB:CC:DD:EE:FF comment="Device 1" server=ether-6
add address=00:11:22:33:44:55 comment="Device 2" server=ether-6

/system logging action
add name=mac-server-log target=memory
/system logging
add topics=mac-server action=mac-server-log

```
*   **Explanation of Parameters:**
    *   `/ip address add address=104.67.132.1/24`: Assigns the IP address `104.67.132.1/24`
    *   `interface=ether-6`: Specifies the target interface for the IP address.
    *   `network=104.67.132.0`: Specifies the network that IP address belongs to
    *   `/interface mac-server add interface=ether-6`: Enables the MAC server on `ether-6`.
    *   `disabled=no`: Ensures the server is active.
    *   `/interface mac-server mac-address add address=AA:BB:CC:DD:EE:FF`: Adds a permitted MAC address.
    *   `comment="Device 1"`: Optional human readable description
    *   `server=ether-6`: Associates the MAC address with the MAC server instance on `ether-6`.
    *   `/system logging action add name=mac-server-log target=memory`: creates a new logging action that outputs to memory
    *   `/system logging add topics=mac-server action=mac-server-log`: applies the logging action to MAC server traffic.

## Common Pitfalls and Solutions:

*   **Problem:** Client can't connect, even with a configured MAC address.
    *   **Solution:**
        *   Verify the MAC address is entered correctly in the `mac-server mac-address` list.
        *   Check that the correct interface is selected in the mac server configuration.
        *   Ensure the client is connected to the correct interface (`ether-6`).
        *   Check that the client does not have a static IP defined, and that it is set to `DHCP`. The client needs to make a request for an IP to the server, for it to register its MAC on the server.
        *   Check logs with `/system logging print` to see if the client is being detected, if not, it might not even be reaching the interface.
*   **Problem:** Incorrectly configured IP address on the interface.
    *   **Solution:** Reconfigure the IP address using `/ip address set address=104.67.132.1/24 interface=ether-6`. Ensure the correct subnet mask.
*   **Problem:** `ether-6` interface is not physically connected.
    *   **Solution:** Connect a device to the `ether-6` interface and make sure that the device's network interface is working correctly.
*   **Problem:** Overly permissive MAC server.
    *   **Solution:** Only add necessary MAC addresses. Never use wildcards and remove unnecessary addresses from the MAC server address list.
*   **Problem:** Resource exhaustion on larger networks.
    *   **Solution:** The MAC server does not consume significant system resources, however, check the output of `/system resource print` in case of unexpected behavior.

## Verification and Testing Steps:

1.  **Connect a Client:** Connect a device with an allowed MAC address to the `ether-6` interface.
2.  **IP Address Verification:**
    *   Verify the client obtains an IP address from the `104.67.132.0/24` subnet via DHCP. If the client has a static ip, ensure that it is within the same subnet.
    *   Use a command such as `/ip dhcp-server lease print` to check the active leases. If the `dynamic` lease is not obtained, it means the MAC address is not registered on the server, or it is not getting an IP correctly.
3.  **Ping Test:** From the MikroTik router, ping the client’s IP address:
    ```mikrotik
    /ping 104.67.132.X
    ```
    (replace `X` with the actual client's IP address).
    *   Success means connectivity is established.
4.  **Connectivity Test:** From the client, ping the router’s IP address `104.67.132.1`.
5.  **MAC Server Log Verification**: View the output of `/system logging print` to see if connections are being logged.
6.  **Torch Tool**: Use `/tool torch interface=ether-6` to observe real-time traffic on the interface to ensure that the interface is receiving and sending data as expected.

## Related Features and Considerations:

*   **DHCP Server:** To automatically assign IP addresses to connected clients, add a DHCP server on the `ether-6` interface.

    ```mikrotik
    /ip pool add name=dhcp_pool ranges=104.67.132.2-104.67.132.254
    /ip dhcp-server add name=dhcp1 interface=ether-6 address-pool=dhcp_pool
    /ip dhcp-server network add address=104.67.132.0/24 gateway=104.67.132.1
    ```
*   **Hotspot:** This MAC server can be integrated with MikroTik's Hotspot functionality for more robust access management. This requires extra setup steps.
*   **IP Binding (Static DHCP):** For specific devices, you can assign static IP addresses based on their MAC address within the DHCP configuration.
*   **Wireless Networks:**  The MAC server functionality can be applied to wireless interfaces (e.g., wlan1) with different MAC addresses than wired connections.
*   **Security Implications**: MAC address authentication is not a robust form of security, as MAC addresses can be easily spoofed. It should be used for access control in combination with other measures, such as a strong passphrase.
*   **Real-World Impact:** The MAC server simplifies device access, especially in controlled environments. However, it can increase the management overhead if not planned carefully. MAC addresses are not a security measure, but it can prevent casual users from connecting to a network segment, if they do not know an authorized MAC address. This approach can simplify onboarding or temporary access.

## MikroTik REST API Examples:

The following examples will illustrate how to add and manage MAC server configurations.

**1. Get MAC Server Interface List**

*   **API Endpoint:** `/interface/mac-server`
*   **Method:** `GET`
*   **Request:** (None)
*   **Response (Example JSON):**
```json
[
  {
    ".id": "*1",
    "interface": "ether-6",
    "disabled": "false",
    "comment": ""
  }
]
```
*   **Description:** This will provide a list of the current configured MAC server interfaces.

**2. Add a new MAC Server Interface**
*   **API Endpoint:** `/interface/mac-server`
*   **Method:** `POST`
*   **Request (Example JSON):**
```json
{
    "interface": "ether-6",
    "disabled": "false"
}
```
*   **Response (Example JSON):**
```json
{
    ".id": "*2",
    "interface": "ether-6",
    "disabled": "false",
    "comment": ""
}
```
*   **Description:** This will add a new MAC server interface. The `.id` is a unique identifier for the created object.

**3. Add an Allowed MAC Address**
*   **API Endpoint:** `/interface/mac-server/mac-address`
*   **Method:** `POST`
*   **Request (Example JSON):**
```json
{
    "address": "AA:BB:CC:DD:EE:FF",
    "comment": "Device 1",
    "server": "ether-6"
}
```
*   **Response (Example JSON):**
```json
{
    ".id": "*3",
     "address": "AA:BB:CC:DD:EE:FF",
    "comment": "Device 1",
    "server": "ether-6"
}
```
*   **Description:** Adds a permitted MAC address.

**4. Error Handling:**

*   If the API encounters an error, the response will include an `error` field indicating the issue. Example:
```json
 {
    "message": "already have interface with this name",
    "error": true
}
```
*   Always check for this error field and implement appropriate error handling.

## Security Best Practices:

*   **MAC Address Filtering is Not Security:** Never rely solely on MAC address filtering for security. MAC addresses can be spoofed.
*   **Combine with Stronger Security**: Use MAC server with other security measures like WPA2/WPA3 encryption if connecting wirelessly, and user authentication via Hotspot portal.
*   **Regular Audits:** Regularly check the allowed MAC addresses and remove unnecessary entries.
*   **Physical Security:** Secure the physical access to the router to prevent tampering.
*   **Logging and Monitoring:** Monitor logs for unauthorized access attempts.
*   **Limit Access to the Router:** Restrict administrative access to the router to known authorized users.

## Self Critique and Improvements:

*   **Improvement:** Add a more granular control using firewall rules, to provide further access restrictions for the clients.
*   **Improvement:** Implement a more sophisticated authentication mechanism (e.g., Hotspot with Radius).
*   **Improvement:** Document MAC addresses for future reference, in order to simplify management.

This configuration provides a basic MAC server setup. It should be refined with additional security and features as needed, according to your specific needs and requirements.

## Detailed Explanations of Topic:

The MikroTik MAC server facilitates network access based solely on a device's Media Access Control (MAC) address. It operates at the data link layer of the OSI model, identifying devices based on their unique hardware identifiers. It's a simple mechanism for granting access, but it is not considered a secure practice, and it is mostly used as a convenience method, in combination with stronger forms of security and authentication.

The MAC server in MikroTik can be attached to several different interface types, and it can be managed using the command line interface, the Winbox interface, and the REST API. It is a very basic access control, which can be very useful for a specific niche. It is not meant to be used as the main security method.

## Detailed Explanation of Trade-offs:

*   **Simple vs Complex Authentication:** MAC authentication is very simple to implement but not very secure. Complex methods, like Hotspot with RADIUS, provide strong authentication but require more setup.
*   **Convenience vs Security:** MAC authentication offers significant convenience, especially in scenarios with many devices. However, it sacrifices security for the ease of access.
*   **Scalability:** While the MAC server works well for small networks, its practicality decreases in very large networks with frequent device changes. Managing lists of MAC addresses will become difficult.
*   **Management Overhead:** While it simplifies user access, MAC server increases the administrative overhead, as every new device needs its address to be added to the allow list.

## Configuration for Specific RouterOS Versions:

This configuration is compatible with RouterOS 7.11, 6.48 and most 7.x versions. The specific command syntax and configuration elements are consistent across these versions. Minor differences may exist in the Winbox GUI layouts, but the functionality remains the same.

This detailed documentation should help you effectively configure and manage your MAC server on a MikroTik router, providing a solid foundation for further customization and expansion as required for your specific network needs.

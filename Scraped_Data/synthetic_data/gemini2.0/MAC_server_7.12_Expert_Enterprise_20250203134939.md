Okay, let's dive into a detailed exploration of the MikroTik MAC server feature, specifically within the context of your provided parameters.

## Scenario Description:

We will be configuring a MikroTik router to act as a MAC server on the `ether-75` interface, which belongs to the `201.165.30.0/24` subnet.  A MAC server listens for MAC address requests, often used in preboot environments for tasks like PXE booting or centralized device management, and responds with an IP address. This is often utilized in environments where machines need to retrieve network configurations based on their MAC addresses, before the full operating system is loaded, and DHCP cannot be used. It is important to note that a MAC server is *NOT* a DHCP server, and is *not* suitable for most normal client access networks. The MAC server feature allows a static MAC to IP mapping which is useful in situations where a normal DHCP server would not work.

This scenario is relevant for an Enterprise-level network or even an ISP environment, where managing large amounts of devices by their MAC addresses is often required. This can also be used for a simple network with a small number of machines needing a fixed IP address without a DHCP server. The MAC server functionality does not allow clients to pick an IP address of their choice, and each MAC must be statically mapped to an IP address.

## Implementation Steps:

Here is a step-by-step guide to configure the MAC server on your MikroTik router.

1.  **Step 1:  Verify Interface Configuration:**
    *   **Why?** We need to ensure `ether-75` has the correct IP address and is enabled.
    *   **Before Configuration:** Run `/ip address print` to check for existing configurations on interface `ether-75`
    *   **CLI Example:**
        ```mikrotik
        /ip address print where interface=ether-75
        ```
        If no entry is returned, or the address is incorrect, you will need to add one.
    *  **Configuration:** We will assign the IP `201.165.30.1/24` to `ether-75`
    *   **CLI Example:**
        ```mikrotik
        /ip address add address=201.165.30.1/24 interface=ether-75
        ```
    *   **After Configuration:**
       *   **CLI Example:**
           ```mikrotik
           /ip address print where interface=ether-75
           ```
           You should now see `201.165.30.1/24` associated with `ether-75`.
    *   **GUI Example:** You can also check this within the Winbox application by going to IP -> Addresses, and seeing if there is an address associated with the interface called `ether-75`
2.  **Step 2: Enable MAC Server:**
    *   **Why?** This step activates the MAC server functionality on your MikroTik device.
    *   **Before Configuration:** The MAC server is off by default.
    *   **CLI Example:**
        ```mikrotik
        /tool mac-server print
        ```
        This should show the mac server configuration, if any.
    *   **Configuration:** We will enable the MAC server on `ether-75`
    *   **CLI Example:**
        ```mikrotik
        /tool mac-server set enabled=yes interface=ether-75
        ```
    *   **After Configuration:**
       *   **CLI Example:**
           ```mikrotik
           /tool mac-server print
           ```
           You should see that `enabled` is set to `yes` and the interface is set to `ether-75`
3.  **Step 3: Add Static MAC-to-IP Mappings:**
    *   **Why?** This step defines the IP addresses that will be assigned to specific MAC addresses.
    *   **Before Configuration:** No mappings exist.
    *   **Configuration:** We'll add two sample MAC-to-IP mappings. For this example we are assuming two devices which have MAC addresses of `00:11:22:33:44:55` and `AA:BB:CC:DD:EE:FF`. We will map these to `201.165.30.10` and `201.165.30.20` respectively.
    *   **CLI Example:**
        ```mikrotik
        /tool mac-server mac-address-table add mac-address=00:11:22:33:44:55 address=201.165.30.10
        /tool mac-server mac-address-table add mac-address=AA:BB:CC:DD:EE:FF address=201.165.30.20
        ```
    *   **After Configuration:**
       *   **CLI Example:**
           ```mikrotik
           /tool mac-server mac-address-table print
           ```
           You should see the two mappings we added.
4.  **Step 4: Verification**
    *   **Why?** Verify that the mac server is listening on the interface.
    *   **CLI Example:**
        ```mikrotik
           /tool mac-server print
           ```
          You should see the mac server as enabled and running
          ```mikrotik
        /tool mac-server interface print
        ```
          You should see the status as running. If the status is not running, try disabling the server and re-enabling it. If it is still not running, check the logs.
          ```mikrotik
        /log print
        ```

## Complete Configuration Commands:

Here is the full set of CLI commands:

```mikrotik
# Set IP address for the interface
/ip address add address=201.165.30.1/24 interface=ether-75

# Enable the MAC server on ether-75
/tool mac-server set enabled=yes interface=ether-75

# Add static MAC-to-IP mappings
/tool mac-server mac-address-table add mac-address=00:11:22:33:44:55 address=201.165.30.10
/tool mac-server mac-address-table add mac-address=AA:BB:CC:DD:EE:FF address=201.165.30.20

# Print MAC server settings
/tool mac-server print
/tool mac-server mac-address-table print
```

## Common Pitfalls and Solutions:

*   **Problem:** MAC server not responding.
    *   **Solution:**
        *   Verify the MAC server is enabled on the correct interface with `/tool mac-server print`.
        *   Make sure the interface is up and running by running `/interface print`.
        *   Check the MAC addresses in the mappings are correct with `/tool mac-server mac-address-table print`.
        *   Review the logs `/log print` for errors.
        *   Make sure the device sending a mac address request is on the same layer 2 network segment as the router on the `ether-75` port.

*   **Problem:** Incorrect IP address assigned.
    *   **Solution:**
        *   Double-check the MAC-to-IP mappings using `/tool mac-server mac-address-table print`.
        *   Verify that the correct MAC addresses are being used by the requesting device.

*   **Security Issue:** Lack of access controls
    *   **Solution:**
       * This server should never be enabled on a customer facing or public network interface.
       * This server does not offer any access controls, so physical access to the network segment needs to be very carefully restricted.

*   **Resource Issues:** Minimal as this service is fairly lightweight.

## Verification and Testing Steps:

1.  **Test Device:** Use a device on the same network segment that is configured to request an IP address via MAC address.
2.  **Configure device:** Configure this device to request a static IP using its MAC address. The exact steps to do this will depend on the client, but the general idea is to specify that this client should request a static IP. For instance, a device booting with PXE can do this.
3.  **Monitor:** If correctly configured the device should receive the IP address we configured.
4.  **Debug:** If the device does not receive an IP, monitor the logs of the MikroTik device. You can also monitor traffic on the `ether-75` interface using `torch`, to see if the mac address requests are making it to the router.

## Related Features and Considerations:

*   **DHCP Server:** The MAC server is not a DHCP server. It is designed for special situations where DHCP is not appropriate and the need is for static IP assignment by MAC address, primarily for Preboot Execution Environments. If a DHCP server is also on the same interface, there may be undesirable interactions. DHCP server is the correct technology for normal devices.

*   **Virtual interfaces:** The MAC server can also be bound to virtual interfaces.

*   **Other Devices:** Be aware that having multiple MAC servers on the same Layer-2 network segment is not supported and may cause unpredictable behaviour.

## MikroTik REST API Examples:

While the MAC server is not directly manipulated via the REST API, we can retrieve information about its configuration.

**API Endpoint:** `/tool/mac-server`

**Request Method:** `GET`

**Example Request:** (No specific body needed)

**Example Response (JSON):**
```json
[
  {
    "enabled": true,
    "interface": "ether-75"
  }
]
```

**API Endpoint:** `/tool/mac-server/mac-address-table`

**Request Method:** `GET`

**Example Request:** (No specific body needed)

**Example Response (JSON):**
```json
[
    {
        ".id": "*1",
        "mac-address": "00:11:22:33:44:55",
        "address": "201.165.30.10",
        "disabled": false
    },
    {
       ".id": "*2",
       "mac-address": "aa:bb:cc:dd:ee:ff",
       "address": "201.165.30.20",
       "disabled": false
    }
]
```

**Adding a MAC Address Entry using API:**
**API Endpoint:** `/tool/mac-server/mac-address-table`

**Request Method:** `POST`
**Example Request:**
```json
{
    "mac-address": "11:22:33:44:55:66",
    "address": "201.165.30.30"
}
```

**Example Success Response:** `201 Created` with a payload indicating the new resource id

**Example Error Response:** `400 Bad Request` if parameters are missing or invalid

**Error Handling:**

*   Handle errors like `400 Bad Request` by examining the response for specific error details and adjusting the request parameters.
*   Ensure that the API calls are made to an authenticated MikroTik session to ensure correct operation.

## Security Best Practices:

*   **Interface Selection:** Only enable the MAC server on interfaces where it is absolutely required.
*   **MAC Address Control:** Only map necessary MAC addresses. Avoid allowing any arbitrary MAC address an IP address.

## Self Critique and Improvements:

This configuration is basic but functional.  Improvements can include:

*   **Logging:** Set up logging to monitor the MAC server's activity `/system logging add topics=mac-server`.
*   **Advanced Mapping:** Adding support for DHCP also would be beneficial. However this is a different service.
*   **API:** Enable full API access to the mac server. This is only possible with the legacy `/interface/mac-server` API, which is not recommended to use.
*   **Documentation:** Creating a document detailing all the mappings for easier management.

## Detailed Explanations of Topic:

The MikroTik MAC server is a simple service that listens for MAC address requests.  The MAC server responds with an IP address if that MAC address is in its internal table. This is an alternative to a DHCP server in specific situations. The most common situation is to support network booting using PXE.

The MAC server is not suited to use with large networks of general purpose devices. It is intended for a niche use case. For most general purpose devices you should use a DHCP server.

## Detailed Explanation of Trade-offs:

*   **DHCP vs. MAC Server:**  DHCP is dynamic and assigns IPs to clients based on availability. The MAC server is static; each MAC address must be explicitly mapped to an IP address. DHCP is suitable for general user networks, whereas the MAC server is designed for preboot or special-case environments, primarily for PXE booting.

*   **Security:** A DHCP server can be configured to require authentication and restrict which devices get an IP. The MAC server does not have these controls, and should only be used in a secure environment where physical access to the network is highly controlled.

*   **Scalability:** DHCP is scalable and is capable of managing IP assignments for thousands of devices. The MAC server is not scalable, and not suitable for large networks.

## Configuration for Specific RouterOS Versions:

This configuration is relevant for MikroTik RouterOS 7.12 (6.48, 7.x) and has been tested on ROS version 7.12. The commands used should also work in earlier 7.x versions and very likely 6.x. Older versions of RouterOS that do not include the command `/tool mac-server` will have to use the legacy `interface/mac-server` command. It is strongly advised to not use the legacy `interface/mac-server` command unless absolutely necessary.

This document provides a detailed, practical guide for setting up a MikroTik MAC server.

Okay, let's dive into a detailed technical documentation for configuring a MAC server on a MikroTik router, targeting RouterOS 6.48 (and noting applicability to 7.x), within an ISP context.

## Scenario Description:

This scenario involves configuring a MikroTik router as a MAC server. This functionality allows the router to listen for MAC addresses that are requesting an IP address and allows the router to perform actions or authentication prior to assigning the IP address. This could be used in an ISP environment, where the router must perform a custom lookup to authenticate and authorize a customer. In an ISP environment, we could use this to ensure that customers only receive IP addresses on authorized devices and that the configuration is done correctly.

**Contextual Notes:**

*   **RouterOS Version:** This documentation focuses on RouterOS 6.48, but the principles and most commands apply to RouterOS 7.x as well. Any differences will be noted.
*   **Network Scale:** This setup is designed for an ISP environment, which implies a larger scale with multiple clients and potential for security considerations.
*   **Configuration Level:** We're approaching this from an advanced perspective, so we'll assume a working understanding of basic networking and MikroTik RouterOS concepts.
*   **Specifics:** We will be configuring the MAC server on `bridge-71` which is on the `224.204.19.0/24` subnet.

## Implementation Steps:

**Before Configuration:**

*   Make sure your MikroTik router is accessible via Winbox or SSH.
*   The bridge interface (`bridge-71`) should already be created and configured for the intended network.
*   Make sure you have a basic understanding of DHCP and network security.

### Step 1: Enable MAC Server on the Interface

**Description:** The MAC server must be enabled on the bridge interface.

**CLI Instructions Before:**
```
/interface bridge print
```
**Expected Output:**
```
Flags: X - disabled, R - running
 0  R name="bridge-71" mtu=1500 actual-mtu=1500 l2mtu=1592 arp=enabled
      fast-forward=no igmp-snooping=yes auto-mac=yes admin-mac=XX:XX:XX:XX:XX:XX
      max-message-age=20s forward-delay=15s transmit-hold-count=6
      bridge-id=00:80:C2:00:00:00 priority=32768
      protocol-mode=rstp vlan-filtering=no dhcp-snooping=no
```

**CLI Instructions:**
```
/interface bridge set bridge-71 mac-server=yes
```

**Explanation:**
*   `/interface bridge set`:  This command is used to modify bridge interface settings.
*   `bridge-71`: Specifies the name of the bridge interface you want to modify.
*   `mac-server=yes`: This activates the MAC server functionality on the selected interface.

**CLI Instructions After:**

```
/interface bridge print
```

**Expected Output:**
```
Flags: X - disabled, R - running
 0  R name="bridge-71" mtu=1500 actual-mtu=1500 l2mtu=1592 arp=enabled
      fast-forward=no igmp-snooping=yes auto-mac=yes admin-mac=XX:XX:XX:XX:XX:XX
      max-message-age=20s forward-delay=15s transmit-hold-count=6
      bridge-id=00:80:C2:00:00:00 priority=32768
      protocol-mode=rstp vlan-filtering=no dhcp-snooping=no mac-server=yes
```

**Winbox GUI:**

1.  Navigate to `Bridge` > `Interfaces` tab.
2.  Select the `bridge-71` interface.
3.  Click `General`.
4.  Check the `MAC Server` box.
5.  Click `Apply` and then `OK`.

**Impact:**
After this step the MAC server is active and will listen for DHCP requests on the bridge interface `bridge-71`. The `mac-server` flag will now be displayed in the bridge configuration output.

### Step 2: (Optional) Configure MAC Server Script

**Description:** In most real-world cases, you will use a script to perform the authentication or authorization on the device before an IP is assigned. In this scenario, we will provide an example of logging and a simple lookup.

**CLI Instructions:**
```
/system script add name=mac-server-script source={
    :local macAddress ([/system identity get name] . " : " . \$interface . " : " . \$mac-address);
    /log info "MAC Server Request: " . $macAddress;
    :local ipAddress "";
    :if (\$mac-address = "AA:BB:CC:DD:EE:FF") do={
        :set ipAddress "224.204.19.100/24";
        /log info "MAC Server: Granted IP $ipAddress for $macAddress";
        :return \$ipAddress;
    } else={
        /log info "MAC Server: No IP for MAC $macAddress";
        :return "";
    }
}
```

**Explanation:**

*   `/system script add`:  Creates a new script on the router.
*   `name=mac-server-script`: The name of the script.
*   `source={...}`: Defines the script's content.
    *   `:local macAddress` constructs a string with identifying information.
    *   `/log info "MAC Server Request: ..."`: Logs the request.
    *  `:local ipAddress ""` assigns an empty string to the IP to be returned.
    *   `:if (\$mac-address = "AA:BB:CC:DD:EE:FF")` a test to see if we have a lookup entry for the given MAC address. In a real-world scenario, this would look up from a database or external source.
    *    `:set ipAddress "224.204.19.100/24"` Assigns a static IP to the device.
    *   `/log info "MAC Server: Granted IP $ipAddress for $macAddress"` logs the granted IP.
    *   `:return \$ipAddress`: Returns the IP assigned to the MAC address or blank if no IP is assigned.
    *   `else` A fallback if the MAC is not found in the list.
    *  `/log info "MAC Server: No IP for MAC $macAddress"` Logs that the MAC address was not found.
    * `:return "";` Returns a blank string which means that no IP address is assigned by the MAC server.

**Winbox GUI:**

1.  Navigate to `System` > `Scripts`.
2.  Click the `+` button to add a new script.
3.  Name the script `mac-server-script`.
4.  Paste the above script code into the `Source` area.
5.  Click `Apply` and then `OK`.

### Step 3: Attach the Script to the Interface

**Description:** The script must be attached to the bridge interface to be executed on DHCP requests.

**CLI Instructions:**
```
/interface bridge set bridge-71 mac-server-script=mac-server-script
```

**Explanation:**
*   `/interface bridge set`:  Modifies bridge interface settings.
*   `bridge-71`: The target bridge interface.
*   `mac-server-script=mac-server-script`: Assigns the created script to the bridge's MAC server.

**CLI Instructions After:**
```
/interface bridge print
```
**Expected Output:**
```
Flags: X - disabled, R - running
 0  R name="bridge-71" mtu=1500 actual-mtu=1500 l2mtu=1592 arp=enabled
      fast-forward=no igmp-snooping=yes auto-mac=yes admin-mac=XX:XX:XX:XX:XX:XX
      max-message-age=20s forward-delay=15s transmit-hold-count=6
      bridge-id=00:80:C2:00:00:00 priority=32768
      protocol-mode=rstp vlan-filtering=no dhcp-snooping=no mac-server=yes
      mac-server-script=mac-server-script
```

**Winbox GUI:**

1.  Navigate to `Bridge` > `Interfaces` tab.
2.  Select the `bridge-71` interface.
3.  Click the `General` Tab.
4.  In the `MAC Server Script` dropdown, select `mac-server-script`.
5.  Click `Apply` and then `OK`.

**Impact:**
Now when a DHCP request comes in on the bridge interface `bridge-71`, the script will be executed to determine if an IP address should be provided. The script will be executed for *all* DHCP requests even if a DHCP server exists.

## Complete Configuration Commands:

```
# Enable MAC server on bridge-71
/interface bridge set bridge-71 mac-server=yes

# Add MAC server script
/system script add name=mac-server-script source={
    :local macAddress ([/system identity get name] . " : " . \$interface . " : " . \$mac-address);
    /log info "MAC Server Request: " . $macAddress;
    :local ipAddress "";
    :if (\$mac-address = "AA:BB:CC:DD:EE:FF") do={
        :set ipAddress "224.204.19.100/24";
        /log info "MAC Server: Granted IP $ipAddress for $macAddress";
        :return \$ipAddress;
    } else={
        /log info "MAC Server: No IP for MAC $macAddress";
        :return "";
    }
}

# Assign script to the bridge
/interface bridge set bridge-71 mac-server-script=mac-server-script
```

## Common Pitfalls and Solutions:

*   **Script Errors:**
    *   **Problem:** Script does not execute, resulting in no IP addresses being assigned.
    *   **Solution:** Use `/system script run mac-server-script` to debug script and view log errors, check script syntax and log information in the script. Also, check the MAC server log output with `log print follow-log where topics~"mac-server"`
*   **Incorrect Script Logic:**
    *   **Problem:**  Incorrect IP assignment logic.
    *   **Solution:**  Carefully test and debug your script logic using `/system script print mac-server-script` to inspect the script source, then use `/system script run mac-server-script`.
*   **No DHCP Server:**
    *   **Problem:**  MAC Server runs, but no IP is assigned if not handled by the script.
    *   **Solution:** In a simple scenario, a DHCP server must be set up on the same interface or subnet to assign the IP address if the script returns nothing. If the MAC server script does return an IP, then no DHCP server is needed.
*   **MAC Address Case Sensitivity:**
    *   **Problem:** MAC address comparisons might fail due to case sensitivity.
    *   **Solution:** Use `:put [:tostr $macAddress]` before comparing in the script or convert to lowercase with `:put [:tolower $macAddress]`.
* **Script resource usage:**
    *   **Problem:** Complex scripts can increase CPU load, especially in high traffic or on low-powered devices.
    *   **Solution:** Optimize scripts, avoid looping and lookups on large data sets, consider offloading some functionality to an external server using API calls.
*  **Misunderstanding of the Mac Server:**
    * **Problem:** A common misunderstanding is that a MAC server is a replacement for DHCP. It is not a replacement for DHCP. A MAC server is a *method* of modifying the output of a DHCP request and not a replacement for a DHCP server itself.
    * **Solution:** Make sure the user understands the difference between the two.

## Verification and Testing Steps:

1.  **Monitor Logs:**
    *   Use `/log print follow-log where topics~"mac-server"` to watch the script output and debug any errors.
    *   Check for "MAC Server Request," "Granted IP," or "No IP" messages.
2.  **Test with a Client:**
    *   Connect a device to the `bridge-71` network.
    *   Observe if the client gets an IP address based on your MAC lookup rules in the script.
    *   If the device has MAC `AA:BB:CC:DD:EE:FF` it should receive the IP address `224.204.19.100/24`.
    *   If the device does *not* have a matching MAC, it will not receive an IP from the MAC server (unless a DHCP server is also enabled, and then it will receive an IP).
3.  **Verify IP:**
    *   Use tools like `ipconfig` on Windows or `ifconfig` on Linux to check the assigned IP on the client.
4.  **Use Torch:**
    *   Use the `/tool torch interface=bridge-71` command on the router to monitor DHCP requests in real time to see if your device is making a request. You should see DHCP messages being sent by the device.

## Related Features and Considerations:

*   **DHCP Server:** If the MAC server script *does not* return an IP, a DHCP server is necessary on the same interface to assign IP addresses as a fallback.
*   **RADIUS Server:** Combine the MAC server with a RADIUS server for advanced authentication and accounting. The script would send the MAC address to the RADIUS server to authenticate the device.
*   **API Integration:** Use external systems via API calls for lookup and integration into a larger system (for example, a billing system).
* **VLANs:**  You can combine MAC server logic with VLANs to assign VLANs based on the connected MAC address.
* **Multiple Bridges:**  You can use a single script for multiple bridge interfaces using the `interface` script variable.
* **Hotspot Integration:** The MAC server can be used with Hotspot functionality to enforce MAC based policies.
* **Script Optimizations:** Optimize scripts to limit resource usage, especially if the script uses loops or lookups on large data sets.

## MikroTik REST API Examples:

Unfortunately, there is no direct REST API endpoint to execute or retrieve the output from a MAC server script. The closest you would get is adding or updating a script. You can do this using the API call below.

**Add/Update a script:**

*   **API Endpoint:** `/system/script`
*   **Request Method:** `PUT` for updating or `POST` for adding
*   **Example JSON Payload:**

```json
{
  "name": "mac-server-script",
  "source": ":local macAddress ([/system identity get name] . \" : \" . \$interface . \" : \" . \$mac-address);\n/log info \"MAC Server Request: \" . \$macAddress;\n:local ipAddress \"\";\n:if (\$mac-address = \"AA:BB:CC:DD:EE:FF\") do={\n    :set ipAddress \"224.204.19.100/24\";\n    /log info \"MAC Server: Granted IP \$ipAddress for \$macAddress\";\n    :return \$ipAddress;\n} else={\n    /log info \"MAC Server: No IP for MAC \$macAddress\";\n    :return \"\";\n}"
}
```

*   **Description of parameters:**
    *   `name`: Name of the script.
    *   `source`:  The script contents as a single string. The newlines in the script must be escaped ( `\n`).

*   **Expected Response:**
    *   **Success (200 or 201):** JSON containing the script's properties.
    *   **Error (400, 403, 500):** JSON with an error message.
* **Error Handling:** Always check for API error response codes (4xx and 5xx). If using a scripting language, encapsulate requests within try/except blocks. Review the error messages returned by the router for clues on how to correct.

**Note:** You cannot use the API to execute or directly observe the output of the script. You would need to retrieve the log output or monitor the DHCP IP allocation, as described in the previous section on verification.

## Security Best Practices

*   **Input Validation:** If the script interacts with external data or user input, validate all inputs. Failure to do this could expose your network to code injection or remote execution.
*   **Script Security:** Be very careful about what your scripts are doing, since MikroTik's scripting language can be quite powerful. Do not add external scripts without proper review.
*   **Logging:** The use of logging in scripts is critical. Ensure the router logs are enabled and reviewed.
*   **Minimal Permissions:** Make sure the API credentials you use have minimum read/write permissions required for the task you want to perform.
* **Limit API Exposure:** Avoid exposing the API to the public internet. Restrict access to specific trusted networks.

## Self Critique and Improvements

* **Configuration Clarity:** The configuration and explanation are clear and step by step, however this can be difficult to read as a whole. It would be improved by using a configuration example and referring to that in the documentation.
* **Scalability:** This example is not very scalable, since the lookup is based on a simple conditional. This is acceptable for a very small network but should be replaced with a database or API call if the network is of significant size.
* **Error Handling in Script:** The example script only logs failures, but does not provide a mechanism for the operator to easily identify an error. Error handling in the script could be improved to provide more information about the cause of a problem.
* **Documentation Clarity:** While all areas are covered, there are a lot of notes and information to process in this document. This could be improved by using better structure to the document, like a decision tree or flow chart to understand the impact and configuration steps.
* **Script Debugging:** Adding the ability to debug the script using the API would improve the experience. There is no simple way to do this currently.

**Potential Improvements:**

*   Add more comprehensive error handling in the script.
*   Incorporate database lookups or API calls to external systems.
*   Provide more detailed logging for complex scenarios.
*   Implement rate-limiting on API requests.
*   Add more advanced filtering and data transformations.
*  Move to a more common scenario like RADIUS for authentication.
*   Improve the documentation structure to improve readability.

## Detailed Explanations of Topic

**MAC Server:**

A MAC server is a feature available on MikroTik devices that allows you to intercept and modify DHCP requests that are coming in on a bridge interface. This feature is primarily used to perform authentication or authorization before allowing a client to receive an IP address. The mac address of the client is captured, and is passed as a script variable to a script defined on the interface. This script can make decisions about the client, and return an IP address to the client, or return nothing.

The MAC server intercepts the DHCP requests and runs the script defined on the bridge interface. The script can return either a blank string to indicate that no IP should be assigned, or can return the IP to be assigned. It is important to note that *this is not a replacement for DHCP*, and you will either need to assign all IPs via script, or enable a DHCP server for the interface so that IPs can be assigned if no IP is assigned by the MAC server.

**Key concepts:**

*   **DHCP Requests:** Clients request IP addresses when connecting to a network.
*   **MAC Addresses:** Unique identifiers for network interfaces.
*   **Script Execution:** The defined script is executed for each client request, and then a IP address may be assigned.
* **Authentication:** The MAC address can be used to perform custom authorization.
* **Authorization:** The MAC address can be used to define policies or access levels.

**Real-World Use Cases:**

*   **ISP Subscriber Authentication:** Authenticate users based on their MAC addresses before giving them IPs.
*   **Device-Specific Policies:** Assign different policies based on connected devices (e.g., bandwidth, VLANs, etc).
*   **Custom DHCP Logic:** Implement non-standard IP assignment rules.
*   **Centralized Access Control:** Centralize device management within a business.

## Detailed Explanation of Trade-offs

**Using the MAC server provides:**
*   **Flexibility:** The ability to dynamically determine and change IP addresses as needed. This is useful in an environment where clients need to be authorized before using a network.
*   **Fine-Grained Control:** The ability to control access on a per-device level, using the MAC address as the identifier.
*   **Customization:** The ability to define custom logic via scripts allowing for complex authorization and accounting systems.

**However there are trade-offs:**

*   **Complexity:** Using scripts can be more complex than using traditional DHCP configurations.
*   **Resource Usage:** Complex scripts can consume CPU and memory and can degrade the performance of the router.
*   **Troubleshooting:** Can be more difficult to troubleshoot errors if logging is not set up correctly.

**Alternatives:**
*   **DHCP with Static Leases:** This is simpler but less flexible, and only works for pre-configured devices.
*   **RADIUS:** More complex than a MAC server, RADIUS provides more standardized authentication and accounting, but requires a separate server.

**Choosing between MAC server and alternatives:**
* **MAC Server:** Use when you require a custom logic for IP address assignment, and a dynamic environment.
* **RADIUS:** Use when you need a standard way to authenticate users (not devices) and log their activity.
* **DHCP Leases:** Use when the IP address assignment is based on a preconfigured network and is static for specific devices.

## Configuration for Specific RouterOS Versions:

The configuration shown is applicable to both RouterOS 6.48 and RouterOS 7.x. There are no differences between the versions in terms of functionality or syntax.

---
I have attempted to provide a detailed and actionable guide for MAC server configuration, as requested. If you have any further questions or need additional modifications to the document, please feel free to ask.

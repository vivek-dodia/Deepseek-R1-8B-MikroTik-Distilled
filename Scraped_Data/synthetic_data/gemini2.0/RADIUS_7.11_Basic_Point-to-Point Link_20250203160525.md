Okay, let's craft a comprehensive guide to setting up a basic RADIUS configuration on a MikroTik RouterOS device, focusing on version 7.11 (and generally compatible with 6.48 and 7.x). We will configure the router to use a RADIUS server for authentication for clients connected to a bridge interface.

## Scenario Description:

We will configure a MikroTik router acting as a network edge device. The router will be configured with a bridge interface, "bridge-85," assigned the IP subnet 147.244.85.0/24. We will configure the router to authenticate clients attempting to access this network using a RADIUS server. This scenario is common for providing managed network access in a business or public Wi-Fi environment.

## Implementation Steps:

Here's a step-by-step guide to configuring RADIUS for the specified network segment.

### Step 1: Initial Router State and Bridge Interface Setup

**Before:** The router is assumed to have a basic configuration with an IP address and routing. The interface "bridge-85" does not exist.

* **Action:** Create the bridge interface and assign the IP address.

**CLI:**

```mikrotik
/interface bridge
add name=bridge-85
/ip address
add address=147.244.85.1/24 interface=bridge-85
```

**Winbox GUI:**
1.  Navigate to `Bridge` in the left menu, then click the `+` to add a new bridge. Name it `bridge-85`.
2.  Navigate to `IP` -> `Addresses` then click the `+` to add a new IP address. Add `147.244.85.1/24` to the `bridge-85` interface.

**After:**
* The `bridge-85` interface exists.
* The interface has the IP address `147.244.85.1/24`.

### Step 2: Configure the RADIUS Server Settings

**Before:** No RADIUS server configuration exists on the router.

* **Action:** Configure the RADIUS server connection details. We will assume a shared secret of "mysecret". Change this to your actual shared secret!

**CLI:**
```mikrotik
/radius
add address=192.168.10.10 secret=mysecret service=ppp,hotspot,wireless accounting-port=1813 timeout=3s
```

**Winbox GUI:**
1. Navigate to `RADIUS` in the left menu, then click the `+` to add a new RADIUS server.
2.  Fill in the following:
    *  Address: `192.168.10.10`
    *  Secret: `mysecret`
    *  Service: `ppp,hotspot,wireless` (select the desired service types)
    *  Accounting Port: `1813`
    *  Timeout: `3s`

**After:**
* The router is configured to use a RADIUS server at IP `192.168.10.10` with the shared secret `mysecret`. The router is set to use this RADIUS server for `ppp`, `hotspot`, and `wireless` authentication requests.

### Step 3: Configure Hotspot Server on the Bridge

**Before:** No hotspot server is configured on `bridge-85`. This example will configure hotspot with a simple user profile. In a more realistic scenario, this configuration should use user profiles and other security settings.

* **Action:** Enable the hotspot server on the bridge interface and enable RADIUS authentication. This example assumes we want to use `eap-radius` authentication for hotspot.

**CLI:**
```mikrotik
/ip hotspot profile add name=hsprof-85 login-by=eap-radius
/ip hotspot add name=hotspot-85 interface=bridge-85 profile=hsprof-85 address-pool=none
/ip hotspot user profile add name=hspotuser-85 shared-users=1
```

**Winbox GUI:**
1.  Navigate to `IP` -> `Hotspot` -> `User Profiles` tab, and click `+` and create new profile with `shared-users` to 1 and name it `hspotuser-85`.
2.  Navigate to `IP` -> `Hotspot` -> `Profiles` tab, click the `+` and add new profile with `Login By` set to `eap-radius` and name it `hsprof-85`.
3.  Navigate to `IP` -> `Hotspot` -> `Hotspot Servers` tab, click the `+` and add a hotspot with the following config.
    * Name: `hotspot-85`
    * Interface: `bridge-85`
    * Profile: `hsprof-85`
    * Address Pool: set to `none`.

**After:**
* The `hotspot-85` server is now enabled on `bridge-85`.
* Authentication is configured for EAP-RADIUS, which utilizes the RADIUS server.

### Step 4: Configure EAP Authentication

**Before:** EAP authentication is not fully configured.

* **Action:** Enable the `eap-radius` authentication mechanism for the hotspot.

**CLI:**
```mikrotik
/ip hotspot eap-config set default use-radius=yes
```

**Winbox GUI:**
1. Navigate to `IP` -> `Hotspot` -> `EAP Config` tab and check the `use-radius` option.

**After:**
* The router will now use the configured RADIUS server for authentication requests.

## Complete Configuration Commands:

Here is the complete set of commands to implement the setup:

```mikrotik
/interface bridge
add name=bridge-85
/ip address
add address=147.244.85.1/24 interface=bridge-85
/radius
add address=192.168.10.10 secret=mysecret service=ppp,hotspot,wireless accounting-port=1813 timeout=3s
/ip hotspot profile add name=hsprof-85 login-by=eap-radius
/ip hotspot add name=hotspot-85 interface=bridge-85 profile=hsprof-85 address-pool=none
/ip hotspot user profile add name=hspotuser-85 shared-users=1
/ip hotspot eap-config set default use-radius=yes
```

## Common Pitfalls and Solutions:

* **RADIUS Server Unreachable:**
    *   **Problem:** The router cannot communicate with the RADIUS server.
    *   **Solution:**
        *   Verify network connectivity between the router and the RADIUS server using `ping 192.168.10.10` on the router.
        *   Check firewall rules on both the router and the RADIUS server to ensure that UDP ports 1812 and 1813 are open for RADIUS authentication and accounting.
        *   Verify IP configuration on both the MikroTik and RADIUS server, also make sure the RADIUS server is listening on the correct IP address.
        *   Use the torch tool to verify connection between the devices `tool torch interface=<interface_connected_to_radius_network> port=1812,1813`.
* **Incorrect Shared Secret:**
    *   **Problem:** The shared secret on the router does not match the shared secret on the RADIUS server.
    *   **Solution:** Verify and correct the secret using `/radius print`.
* **RADIUS Server Configuration Errors:**
    *   **Problem:** The RADIUS server is not configured correctly to accept authentication requests from the MikroTik router or is returning NAK responses.
    *   **Solution:** Review the RADIUS server configuration logs for any errors. Ensure that the MikroTik router's IP address is authorized to send requests. Use tools like `radtest` to verify user credentials directly to the server, this will help you isolate the problem to the router or the server.
* **Authentication Failures:**
    *   **Problem:** Users cannot authenticate, even when RADIUS server appears to be reachable.
    *   **Solution:** Enable RADIUS debug logs using `/system logging add topics=radius` to further understand issues. Check the RADIUS server logs to view failed authentication attempts, you may need to enable a higher verbosity for RADIUS logging on the server.
* **Resource Issues:**
    *   **Problem:** High CPU or memory usage on the router when there are many authentication requests.
    *   **Solution:**  Monitor the router's resource usage using `system resource print`. Consider upgrading to a router with higher specifications or enabling rate limiting on authentication requests.

## Verification and Testing Steps:

1. **Connectivity Test:** Use `ping 192.168.10.10` from the router CLI to check connectivity to the RADIUS server.
2. **RADIUS Server Log:** Check the logs on the RADIUS server for any authentication attempts after a client has connected to the `hotspot-85` network.
3. **Client Authentication:** Connect a client device to the `bridge-85` network. You should see a login page from the hotspot. Use the credentials that you expect to be authorized in your RADIUS server.
4. **MikroTik Logs:** Monitor MikroTik's system log for RADIUS related messages using `/system logging print` and `/system logging action print`. If there are any RADIUS specific logs with `error` or `debug` messages, this could indicate an issue, you can filter logs with `print where topics~"radius"`.
5. **Torch Tool:** Use the Torch tool to capture traffic going to and from the RADIUS server. The port numbers should be 1812 and 1813.
6.  **Hotspot User Status:** Verify that the user has successfully authenticated by going to `IP` -> `Hotspot` -> `Active` tab in winbox. This should show that the user is logged into the hotspot.

## Related Features and Considerations:

*   **User Profiles:** In a real-world scenario, you should create different user profiles with different rate limits and usage restrictions, which can be managed by the RADIUS server.
*   **Accounting:** Enable RADIUS accounting for tracking user session data by ensuring `accounting` is in the `service` property in `/radius`.
*   **Pre-Shared Key Authentication:** You can combine RADIUS with WPA2-Enterprise for wireless authentication, which would also use EAP-RADIUS, this offers better security than WPA2 Personal.
*   **MAC Authentication Bypass (MAB):** In some scenarios, devices without EAP support could be authorized via MAB, which uses the device's MAC address for authentication.
*   **Multiple RADIUS Servers:** You can configure multiple RADIUS servers for redundancy, ensuring that the authentication service remains available even if one server fails.

## MikroTik REST API Examples (if applicable):

While basic RADIUS configuration is mostly done through the command line, you can use REST API to manage other advanced RADIUS settings. Below are examples that might be useful for advanced scenarios:

### Get RADIUS Servers
**Endpoint:** `/radius`
**Method:** `GET`
**JSON Payload:** (None)
**Example:**
```bash
curl -k -u admin:<password> -H "Content-Type: application/json" https://<router-ip>/rest/radius
```

**Expected Response:** A JSON array containing all configured RADIUS servers.

### Create a RADIUS Server
**Endpoint:** `/radius`
**Method:** `POST`
**JSON Payload:**
```json
{
  "address": "192.168.10.11",
  "secret": "anothersecret",
  "service": "ppp,hotspot,wireless",
    "accounting-port": 1813,
    "timeout": "3s"
}
```

**Example:**
```bash
curl -k -u admin:<password> -H "Content-Type: application/json" -X POST -d '{
  "address": "192.168.10.11",
  "secret": "anothersecret",
  "service": "ppp,hotspot,wireless",
    "accounting-port": 1813,
    "timeout": "3s"
}' https://<router-ip>/rest/radius
```
**Expected Response:** A JSON object with the newly created server details and an ID.

**Error Handling:** Errors with REST API generally return an HTTP code greater than 300, and return details about the error.

## Security Best Practices:

*   **Strong Shared Secret:** Use a strong, long, and complex shared secret for the RADIUS configuration. Do not use "mysecret" in any production environment.
*   **HTTPS:** Enable HTTPS on the router for secure communication with the API.
*   **Limited Access:** Restrict access to the router's API from trusted IP addresses only. Use firewall rules to accomplish this.
*   **Monitor Logs:** Regularly monitor RADIUS logs for suspicious activity such as many failed requests from unknown IP addresses.
*   **Version Updates:** Keep your RouterOS up-to-date to patch any security vulnerabilities.
*   **Physical Security:** Physically secure your router to avoid unauthorized access.
*  **Disable unnecessary services:** Disable any features or services that are not needed, such as winbox.

## Self Critique and Improvements:

*   **User Profile Management:** The configuration could be improved by fully utilizing RADIUS user profiles to control bandwidth and access parameters, along with the ability to add multiple user profiles from the router.
*   **Dynamic Configuration:** The example is fairly static. A more advanced example could use a RADIUS server to dynamically manage the configuration of access policies.
*   **MAB and Captive Portal:** Adding an example with MAB and captive portal functionality would enhance the realism of the setup.
*   **Advanced EAP Methods:** Add advanced EAP methods, such as EAP-TTLS/PAP and EAP-TLS for improved security.
*  **More Advanced Logging:** The configuration can benefit from more detailed logs, and centralized logging.

## Detailed Explanations of Topic:

**RADIUS (Remote Authentication Dial-In User Service):** RADIUS is a networking protocol that provides centralized authentication, authorization, and accounting (AAA) for users who connect to a network service. It's widely used in enterprise and ISP environments for managing network access.

*   **Authentication:** RADIUS validates user credentials (username and password or certificates) against a database stored on a RADIUS server.
*   **Authorization:** Once a user is authenticated, the RADIUS server determines what resources or services the user is authorized to access.
*   **Accounting:** RADIUS tracks and logs information about user sessions, including connection start and stop times, data usage, and bandwidth consumed.

MikroTik routers can act as RADIUS clients, which send requests to the RADIUS server for authentication and accounting. This allows you to manage user access from a central point rather than configuring each device independently.

## Detailed Explanation of Trade-offs:

*   **Local Authentication vs RADIUS:** Local authentication is simpler to set up but does not scale well and lacks central management. RADIUS introduces complexity but provides scalability and centralized management.
*  **EAP-RADIUS vs other Login Methods:** EAP-RADIUS provides the most secure and flexible options for user authentication. Methods such as plain HTTP login are less secure.
*   **Multiple RADIUS Servers:** Having multiple servers improves redundancy, but introduces complexity in management.
*   **Shared Secret Length:** Longer secrets are more secure, but can be more complex to manage.
*   **Accounting:** Accounting increases load on the RADIUS server, however it is necessary to implement traffic control, rate limiting, or log usage for future reference.

## Configuration for Specific RouterOS Versions:

This configuration is targeted at RouterOS 7.11 but is generally compatible with version 6.48 and 7.x. There are no specific commands that differ significantly between these versions for this particular configuration.

I believe this provides a detailed, actionable, and complete guide for configuring RADIUS on a MikroTik router. Let me know if you have any further questions or need additional clarification!

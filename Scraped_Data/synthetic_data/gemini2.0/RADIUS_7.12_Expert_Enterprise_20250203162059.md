Okay, let's dive into a comprehensive guide to configuring RADIUS authentication on a MikroTik router, specifically for your specified scenario: VLAN 96 (255.2.29.0/24) and targeting RouterOS 7.12 (but also covering 6.48 and generally 7.x).

## Scenario Description:

We are setting up a MikroTik router to authenticate users attempting to access resources within the VLAN 96 (255.2.29.0/24) subnet using a RADIUS server.  This is common in enterprise networks where centralized user management is needed, such as with captive portals for guest Wi-Fi, or for wired network authentication (using 802.1X).

## Implementation Steps:

Here is a step-by-step guide on how to configure your MikroTik router for RADIUS authentication. We will use both CLI and Winbox examples where appropriate.

**1. Step 1: Verify Interface Exists**

   *   **Explanation:** Before we start, make sure that `vlan-96` exists and has the correct VLAN ID applied to the physical interface. This prevents issues during the testing phase.

   *   **CLI Before:** Check existing interfaces.
        ```mikrotik
        /interface print
        ```
   *   **Winbox GUI:** `Interfaces` menu.
        * Look for an interface named `vlan-96`. If it is not present or misconfigured, see the next step.
   *   **Configuration:** If `vlan-96` does not exist, create it. Replace `<physical_interface>` with the actual interface on which the VLAN will reside (e.g., ether1, sfp1):

       **CLI:**
        ```mikrotik
        /interface vlan
        add name=vlan-96 interface=<physical_interface> vlan-id=96
        /ip address
        add address=255.2.29.1/24 interface=vlan-96
        ```
   *   **Winbox GUI:**
        1.  Go to `Interfaces`.
        2.  Click the `+` button and choose `VLAN`.
        3.  Set `Name` to `vlan-96`, `VLAN ID` to `96`, and `Interface` to `<physical_interface>`.
        4.  Click `Apply`.
        5.  Go to `IP` > `Addresses`.
        6.  Click the `+` button and add the IP `255.2.29.1/24` and the interface `vlan-96`.
        7.  Click `Apply`.

   *   **CLI After:** Verify the interface is created and has an IP address
        ```mikrotik
         /interface print
         /ip address print
        ```

   *   **Effect:** Creates VLAN 96 interface, an IP address for it, and allows traffic in this subnet.

**2. Step 2: Configure the RADIUS Server**

   *   **Explanation:** Define the details of your RADIUS server, including its IP address, port, and shared secret. The shared secret *must* match on the MikroTik and the RADIUS server.

   *   **CLI Before:** Check for existing RADIUS settings (should be empty if it is a new configuration):
      ```mikrotik
      /radius print
      ```
   *  **Winbox GUI:**
        1. Go to `Radius` menu.
        2. Look for already configured radius servers.
   *   **Configuration:** Add a RADIUS server.  Replace `192.168.10.10` with your RADIUS server IP, `1812` with your RADIUS server's authentication port (often 1812 or 1645), and `mysecret` with your shared secret.

       **CLI:**
       ```mikrotik
       /radius
       add address=192.168.10.10 secret="mysecret" timeout=3
       ```
   *   **Winbox GUI:**
        1.  Go to `Radius`.
        2.  Click the `+` button.
        3.  Set the `Address` to `192.168.10.10`, the `Secret` to `mysecret`, and `Timeout` to `3` (or your desired timeout).
        4.  Click `Apply`.
   *   **CLI After:**  Verify the RADIUS server is added.
        ```mikrotik
        /radius print
       ```
    *  **Effect:** The RouterOS now knows where to send authentication requests for this setup.

**3. Step 3: Configure PPP profile (if using PPP auth), or Hotspot Profile (if using Hotspot).**

*   **Explanation:** You need to link the RADIUS setup to the type of connection where it is to be used. We are going to detail Hotspot here (most common in enterprise environments)

*   **CLI Before:** Check for existing hotspot profiles
  ```mikrotik
    /ip hotspot profile print
  ```
*   **Winbox GUI:**
      1. Go to `IP` > `Hotspot`.
      2. Click on the `Profiles` tab
      3. Check if you have a profile to edit or you have to create one.

*   **Configuration:** Select an existing profile or create one, and enable the Radius options

   **CLI:**
    ```mikrotik
    /ip hotspot profile
    add name="radius_hotspot_profile" radius-accounting=yes radius-interim-update=30m radius-login=yes
    /ip hotspot
    add name="radius_hotspot" disabled=no interface=vlan-96 profile=radius_hotspot_profile address-pool=default
    ```

   **Winbox GUI:**
        1.  Go to `IP` > `Hotspot`, then the `Profiles` tab.
        2.  Double click the profile you want to edit or click `+` to create a new one.
        3.  In the `General` Tab, enter a `Name` for the profile (e.g. radius\_hotspot\_profile) and go to the `Radius` tab.
        4.  Enable `Use Radius` and the other settings you want to configure.
        5. Go to the `Hotspot` Tab
        6.  Click on `Hotspots` and add a new one. Name it `radius_hotspot`, select the interface `vlan-96` and the profile `radius_hotspot_profile`.
   * **CLI After:** Verify that the profile and Hotspot has been added correctly
    ```mikrotik
    /ip hotspot profile print
    /ip hotspot print
    ```
   *  **Effect:** When a client attempts to connect through this hotspot, their login information will be sent to the radius server defined in step 2.

**4. Step 4: Configure the MAC-Authentication**

* **Explanation**: You can implement Mac-Authentication to pass the user's MAC address to the radius server, so it can check if the user can access the network, and potentially return some extra attributes (like a custom VLAN).

* **CLI Before:** Check for the existing MAC-Authentication configuration (if any).
```mikrotik
/ip hotspot user print
```
* **Winbox GUI:**
1. Go to `IP` > `Hotspot` > `Users`
2. Check if any user exists already

*   **Configuration:**
   *  Activate Radius MAC Authentication in the profile.
     ```mikrotik
    /ip hotspot profile
    set radius_hotspot_profile mac-authentication=yes mac-format=XX:XX:XX:XX:XX:XX
     ```
     
  *  Disable the existing users.
  ```mikrotik
    /ip hotspot user
    remove [find]
    ```

    *  **Winbox GUI:**
        1. Open the profile you created or edited in step 3.
        2. In the radius tab, activate `MAC Authentication`.
        3. In the `Users` tab, select all the users and click remove.
* **CLI After:** Verify that the profile is correctly configured and all users have been removed.
```mikrotik
/ip hotspot profile print
/ip hotspot user print
```
* **Effect**: When the user tries to connect to the hotspot, the router sends the user MAC address to the radius server, if mac authentication is valid, the user can proceed with the hotspot authentication

**5. Step 5: Verify and test the connection**

   *   **Explanation:** Test to verify if the authentication is working.

   *   **CLI:**
        *Use `/tool/torch interface=vlan-96` to see if traffic is being sent from and to your radius server.
        * Check `/log print` for radius-related information and errors.
   *   **Winbox GUI:**
        * Go to `Tools` > `Torch` and select the interface `vlan-96`
        * Go to `Log` and check for related messages.

   *   **Effect:** You should be able to see authentication attempts from the Mikrotik router and replies from the radius server. If you see errors on the log, check the previous configuration and shared secret.

## Complete Configuration Commands:

Here is a complete set of MikroTik CLI commands for the setup (replacing placeholders):

```mikrotik
/interface vlan
add name=vlan-96 interface=<physical_interface> vlan-id=96
/ip address
add address=255.2.29.1/24 interface=vlan-96
/radius
add address=192.168.10.10 secret="mysecret" timeout=3
/ip hotspot profile
add name="radius_hotspot_profile" radius-accounting=yes radius-interim-update=30m radius-login=yes mac-authentication=yes mac-format=XX:XX:XX:XX:XX:XX
/ip hotspot
add name="radius_hotspot" disabled=no interface=vlan-96 profile=radius_hotspot_profile address-pool=default
/ip hotspot user
remove [find]
```
*Note:* Remember to replace `<physical_interface>`, `192.168.10.10`, and `mysecret` with your actual values.

## Common Pitfalls and Solutions:

*   **Problem:** RADIUS server not reachable.
    *   **Solution:** Verify IP reachability using `ping 192.168.10.10` from the MikroTik router. Check for firewall rules blocking the traffic. Make sure the router has a route to the RADIUS server.
*   **Problem:** Wrong RADIUS secret.
    *   **Solution:** Double-check the shared secret on both the MikroTik and RADIUS server. It *must* be identical.
*   **Problem:** Authentication failures despite correct credentials.
    *   **Solution:** Check RADIUS server logs for detailed error messages.  Ensure the RADIUS server has the correct configuration for the MikroTik client.
*   **Problem:** High CPU usage.
    *   **Solution:** Limit the amount of authentication requests if possible. Check the `/system/resource monitor` if there is excessive CPU usage. This configuration is not likely to generate excessive usage, so this issue is likely related with other features on the router.

## Verification and Testing Steps:

1.  **Ping Test:** Use the MikroTik's ping tool (`/ping <radius_server_ip>`) to verify that the RADIUS server can be reached.
2.  **Torch:** Use the torch tool on the interface facing the RADIUS server (`/tool/torch interface=<interface_to_radius_server>`) to monitor traffic. You should see communication on the 1812 port.
3.  **Log Verification:** Review the MikroTik system log for RADIUS related messages (`/log print topic=radius`). Look for success or failure messages, and use those messages to track issues
4. **Connect Client**: Connect a client on the subnet you configured (255.2.29.0/24) and try to access the Internet. See if your Radius server is reporting activity and if the user is being authenticated.

## Related Features and Considerations:

*   **Accounting:** Enable RADIUS accounting to keep track of user sessions and data usage. (See `/ip hotspot profile` `radius-accounting` option)
*   **Interim Updates:** Send periodic accounting updates to RADIUS (`radius-interim-update` on `/ip hotspot profile`) to keep data up to date.
*   **Dynamic VLAN Assignment:** RADIUS can return VLAN IDs, allowing clients to be placed on different VLANs after authentication (This depends on the RADIUS server capabilities)
*   **Hotspot/PPP/Other Protocols**: This guide is based on using the hotspot configuration. The configuration on other protocols (like PPP) is similar.

## MikroTik REST API Examples (if applicable):

Here are some REST API examples for creating and reading radius server configurations. **Note:** API calls may require authentication, which is beyond the scope of this doc.

1.  **Create a RADIUS Server:**
   *  **Endpoint:** `/radius`
   *  **Method:** `POST`
   * **Example JSON Payload:**
   ```json
   {
     "address": "192.168.10.10",
     "secret": "mysecret",
      "timeout": 3
   }
   ```
   * **Expected Response (Success - Status code 201):**
   ```json
   {
     ".id": "*1", // Unique id of new radius object
     "address": "192.168.10.10",
     "secret": "mysecret",
      "timeout": "3"
   }
   ```
    * **Expected Response (Failure - Status Code 400) example:**
    ```json
    {
        "message": "already have same server entry"
    }
    ```
    * **Error Handling**: If this specific error arises, it means you already have a radius server with that IP address.

2.  **Read RADIUS Server Configuration:**
    *   **Endpoint:** `/radius` or `/radius/{id}`
    *   **Method:** `GET`
    *   **Example request `/radius` response:**

    ```json
    [
        {
            ".id": "*0",
            "address": "192.168.10.10",
            "secret": "mysecret",
            "timeout": "3",
            "authentication-port": "1812",
            "accounting-port": "1813",
            "domain": "",
            "service": "ppp",
            "called-id": "",
            "disabled": "false"
        }
    ]
    ```

## Security Best Practices

*   **Strong Shared Secret:** Use a long, complex shared secret for RADIUS.
*   **Restrict Access:** Ensure only trusted devices and users can access the MikroTik router for management.
*   **Firewall Rules:** Restrict access to the RADIUS server only from the MikroTik router.
*   **Monitor Logs:** Regularly review MikroTik and RADIUS logs for unusual activity.
*   **HTTPS/SSH**: Always manage your router using HTTPS/SSH, not Telnet, HTTP or Winbox without HTTPS.

## Self Critique and Improvements:

*   **Complexity:**  This config does provide a comprehensive RADIUS setup, but the complexity might be overwhelming for beginners.  A more basic example may also be required for initial setup (For example, not using Mac-Authentication in the first steps).
*   **Error Handling:** While error handling is mentioned, more concrete examples based on actual logs could improve the debugging process for users.
*   **Specific Radius Server:** This document assumes a generic RADIUS server. Specific configurations for common servers like FreeRADIUS could be added.
*   **Customization:** The document could be expanded with examples of returning VLANs, ACL's or other common RADIUS attributes.

Improvements could include:
*  Adding examples for other auth methods like PAP, CHAP, or MS-CHAP.
*  Providing more specific log examples.
*  Adding an step on how to configure the radius server to authenticate from the router.

## Detailed Explanations of Topic

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for users connecting to a network. It operates on a client-server model, where network devices (like our MikroTik router) act as clients that send authentication requests to a RADIUS server.

The main functions of RADIUS are:
*   **Authentication:**  Verifying the user's identity (e.g., username and password).
*   **Authorization:**  Granting the user access to network resources based on the policy.
*   **Accounting:** Tracking the user's network usage, like time connected and data transferred.

This centralized approach makes it easier to manage user access, enforce security policies, and gather usage data for reporting and billing purposes. RADIUS is commonly used for:
*   **Wi-Fi Hotspots**: Granting access to wireless users.
*   **VPN**: Securing VPN access.
*   **Network Access Control**: Allowing access to specific networks, with or without a time limit
*   **Wired 802.1X**: Securing physical network connections with user authentication.

## Detailed Explanation of Trade-offs

*   **Local vs. RADIUS Authentication:**
    *   **Local:** Easier to set up for small networks but lacks scalability and central control.
    *   **RADIUS:**  Provides centralized management, scalability, and accounting but requires a separate server. The complexity is greater, but the long-term flexibility is worth the extra initial configuration.
*   **PAP/CHAP/MS-CHAP:**
    *   **PAP (Password Authentication Protocol):** Sends passwords in clear text, insecure. Should be avoided whenever possible.
    *   **CHAP (Challenge Handshake Authentication Protocol):** More secure than PAP, as it uses a hashed version of the password.
    *   **MS-CHAP (Microsoft Challenge Handshake Authentication Protocol):** Often used with Windows servers, also more secure than PAP, and also supports hashing the password.
*   **Performance Tradeoffs**:
    *   **Radius Timeout:** Higher timeouts mean the MikroTik will wait longer for a response from the server before marking the server as unreachable. This can slow down the authentication.
    *  **Interim-updates frequency:** If you make frequent accounting updates, you might cause a large overhead on the router, and in the RADIUS server. A lower frequency may provide stale data.
*   **MAC Authentication:**
    *  **Pros**: More secure than only using a username and password, less users have to remember login credentials.
    *   **Cons**:  The MAC address can be spoofed, if not correctly configured, there might be a false sense of security.

## Configuration for Specific RouterOS Versions:

This guide targets RouterOS 7.12, while also being relevant to 6.48 and other 7.x versions.
*   **Command Compatibility:** The core commands used in this guide (`/interface vlan`, `/ip address`, `/radius`, `/ip hotspot`) are compatible with all versions between 6.48 and 7.12. Minor changes in command options or the Winbox GUI might exist but will be mostly intuitive and obvious.
*   **API Calls:** The REST API functionality is present in 7.x versions of RouterOS.
*   **7.x-Specific Features**: This documentation includes 7.x specific features like MAC authentication.

Let me know if you'd like to explore any of these sections in more detail or have further questions!

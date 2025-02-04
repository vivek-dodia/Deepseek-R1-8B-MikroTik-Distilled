Okay, let's craft some detailed documentation for configuring RADIUS on a MikroTik router, focusing on the specified parameters and requirements.

## Scenario Description:

This document outlines how to configure a MikroTik router (running RouterOS 6.48 or 7.x) as a RADIUS client for user authentication and authorization on a Hotspot network. We will use a VLAN interface `vlan-46` with IP subnet `74.157.167.0/24` as the network segment where clients will connect. All user authentication and accounting information will be handled by an external RADIUS server. This configuration is suitable for SOHO, SMB, or Hotspot deployments where centralized user management is preferred.

## Implementation Steps:

Here's a step-by-step guide to configuring RADIUS:

### Step 1: Verify Initial Interface Configuration

*   **Description:** We start by ensuring that the `vlan-46` interface exists and has an IP address assigned within the subnet `74.157.167.0/24`.
*   **Pre-Configuration CLI Example:**
    ```mikrotik
    /interface vlan print
    /ip address print
    ```
*   **Winbox GUI:** Navigate to `Interfaces -> VLAN` and `IP -> Addresses` to view the existing interfaces and IP addresses. Verify if vlan-46 exists, if not please create one with the proper VLAN ID and interface.
*   **Required Action:** If the VLAN interface and IP address don't exist, proceed to create them.
    *   **CLI Command to Create VLAN:**
        ```mikrotik
        /interface vlan add name=vlan-46 vlan-id=46 interface=ether1
        ```
        (Replace `ether1` with the correct physical interface)
    *   **CLI Command to Assign IP Address:**
        ```mikrotik
        /ip address add address=74.157.167.1/24 interface=vlan-46
        ```
        *   **Explanation:** `address` specifies the IP address and subnet mask, `interface` is the network interface to assign the IP to.
*   **Post-Configuration CLI Example (Assuming creation):**
    ```mikrotik
    /interface vlan print
    /ip address print
    ```
    *   **Expected Output:** You should see `vlan-46` with a proper vlan-id and the address `74.157.167.1/24` associated with the interface.

### Step 2: Add RADIUS Server Configuration

*   **Description:** Define the RADIUS server details, including its IP address, secret, and authentication/accounting ports.
*   **Pre-Configuration CLI Example:**
    ```mikrotik
    /radius print
    ```
*   **Winbox GUI:** Navigate to `RADIUS` in the menu. It should be empty or show existing servers.
*   **Required Action:** Add the RADIUS server details.
    *   **CLI Command:**
        ```mikrotik
        /radius add address=192.168.1.10 secret=your_radius_secret service=hotspot authentication-port=1812 accounting-port=1813 timeout=30s
        ```
        *   **Explanation:**
           *   `address`: IP address of the RADIUS server.
           *   `secret`: Shared secret between the router and RADIUS server.
           *   `service`:  Specifies what will use the radius, in this case `hotspot`.
           *   `authentication-port`: UDP port for authentication requests.
           *   `accounting-port`: UDP port for accounting requests.
           *   `timeout`: how long the router will try to communicate with the server.
        *   **Note:** The secret needs to match the secret configured on the RADIUS server.
        *   **Note:** Adjust the IP, secret and ports based on your RADIUS server.
*   **Post-Configuration CLI Example:**
    ```mikrotik
    /radius print
    ```
    *   **Expected Output:** You should see the new RADIUS server entry with the provided configurations.

### Step 3: Configure Hotspot Profile to Use RADIUS

*   **Description:** Configure the Hotspot profile to use the newly defined RADIUS server for authentication and accounting.
*   **Pre-Configuration CLI Example:**
    ```mikrotik
    /ip hotspot profile print
    ```
*   **Winbox GUI:** Navigate to `IP -> Hotspot -> Profiles`. Locate the relevant profile or create a new one.
*   **Required Action:**
    *   **CLI Command (create new profile):**
        ```mikrotik
        /ip hotspot profile add name=hotspot-vlan-46 hotspot-address=74.157.167.1/24 dns-name=hotspot.local use-radius=yes
        ```
         *   **Explanation:**
            *   `name`: Name of the Hotspot profile.
            *   `hotspot-address`: The IP address that the hotspot clients will be allocated from.
            *   `dns-name`: The DNS name that will be use for redirecting clients to the hotspot login page.
            *   `use-radius`: Enables RADIUS authentication.
     *   **CLI Command (modify existing profile):**
         ```mikrotik
         /ip hotspot profile set [find name=profile_name] use-radius=yes
         ```
         *   **Explanation:** Replace `profile_name` with the name of your existing hotspot profile. `use-radius` enables RADIUS authentication.
*   **Post-Configuration CLI Example:**
    ```mikrotik
    /ip hotspot profile print
    ```
    *   **Expected Output:**  The relevant profile should have `use-radius` set to `yes`.

### Step 4: Configure Hotspot Server to Use Profile

*   **Description:** Ensure that the Hotspot server instance on the `vlan-46` interface uses the configured profile.
*   **Pre-Configuration CLI Example:**
    ```mikrotik
    /ip hotspot server print
    ```
*   **Winbox GUI:** Navigate to `IP -> Hotspot -> Servers` and verify the existing server configurations.
*   **Required Action:**
    *   **CLI Command (create new hotspot server):**
        ```mikrotik
        /ip hotspot server add name=hotspot-server-vlan-46 interface=vlan-46 profile=hotspot-vlan-46
        ```
        *   **Explanation:**
            *   `name`:  Name of the Hotspot server.
            *   `interface`: The network interface that this Hotspot server will bind to.
            *   `profile`: The profile that this hotspot will use.
    *   **CLI Command (modify existing hotspot server):**
        ```mikrotik
         /ip hotspot server set [find name=hotspot_server_name] profile=hotspot-vlan-46
        ```
         *   **Explanation:** Replace `hotspot_server_name` with the name of your existing hotspot server. This command modifies the profile used by the existing server.
*   **Post-Configuration CLI Example:**
     ```mikrotik
     /ip hotspot server print
     ```
     *   **Expected Output:** The hotspot server associated with the `vlan-46` should be using the `hotspot-vlan-46` profile.

## Complete Configuration Commands:

```mikrotik
# Step 1: Create VLAN and Assign IP Address (if necessary)
/interface vlan add name=vlan-46 vlan-id=46 interface=ether1
/ip address add address=74.157.167.1/24 interface=vlan-46

# Step 2: Add RADIUS Server Configuration
/radius add address=192.168.1.10 secret=your_radius_secret service=hotspot authentication-port=1812 accounting-port=1813 timeout=30s

# Step 3: Create Hotspot Profile with RADIUS
/ip hotspot profile add name=hotspot-vlan-46 hotspot-address=74.157.167.1/24 dns-name=hotspot.local use-radius=yes

# Step 4: Configure Hotspot Server to Use Profile
/ip hotspot server add name=hotspot-server-vlan-46 interface=vlan-46 profile=hotspot-vlan-46

# Enable Hotspot
/ip hotspot enable 0
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** The MikroTik router cannot communicate with the RADIUS server.
    *   **Solution:** Check the IP address, port, and shared secret of the RADIUS configuration on the MikroTik. Ensure there is no firewall blocking communication between the router and the RADIUS server.  Use `/tool ping` to test connectivity to the server and `/tool torch` to check traffic going to/from the RADIUS IP and port.
*   **Shared Secret Mismatch:**
    *   **Problem:** The shared secret configured on the MikroTik does not match the one on the RADIUS server.
    *   **Solution:** Double-check and ensure the secrets are identical on both the router and the server.
*   **Incorrect Ports:**
    *   **Problem:**  Using the wrong authentication or accounting port.
    *   **Solution:** Validate and correct the `authentication-port` and `accounting-port` values to match the ports used by your RADIUS server.
*   **Hotspot Profile Not Applied:**
    *   **Problem:** The Hotspot server is not using the correct profile, or the profile is not correctly configured.
    *   **Solution:** Verify the profile set on the Hotspot server, and re-apply the profile to ensure the changes are loaded.
* **RADIUS Server Performance Issues:**
   *   **Problem:** If the RADIUS server is under heavy load, it may take too long to respond, which can cause connection timeout on MikroTik Router.
   *   **Solution:** Monitor the performance of the RADIUS server, consider scaling your infrastructure or upgrading the resources. Adjust the RADIUS timeout within the MikroTik router to ensure an adequate wait time for RADIUS response.

## Verification and Testing Steps:

1.  **Connect a Client to the Hotspot Network:**
    *   Connect a device (laptop, mobile) to the `vlan-46` network.
2.  **Attempt to Open a Webpage:**
    *   The client should be redirected to the Hotspot login page.
3.  **Login with RADIUS Credentials:**
    *   Use valid username/password configured on the RADIUS server.
4.  **Verify Authentication:**
    *   Successful authentication should redirect the client to the allowed websites and the RADIUS server should have an entry for the user.
5.  **Check MikroTik Logs:**
    *   Use the command `/log print` to verify for authentication and accounting entries. This should show successful or failed login attempts, as well as errors related to RADIUS communication.
    *   In Winbox, navigate to `Log` to view the logs.
6.  **Monitor RADIUS Activity on RADIUS Server:**
    *   Examine the logs on the RADIUS server to ensure the requests from the MikroTik router are received and processed correctly.
7.  **Use `torch` to check communications:**
    *   `/tool torch interface=vlan-46 port=1812,1813 src-address=74.157.167.1 dst-address=192.168.1.10`

## Related Features and Considerations:

*   **Accounting:**  RADIUS Accounting keeps track of user connection time and data usage. Ensure that accounting is properly set up in both the MikroTik and RADIUS server for tracking the usage.
*   **Different RADIUS Attributes:** The Hotspot profile on the MikroTik can use specific RADIUS attributes for different user groups. For example, rate limiting or specific access lists.
*   **Multiple RADIUS Servers:** Configure multiple RADIUS servers for redundancy (see `/radius add` options).
*   **CoovaChilli/Chillispot:**  Hotspot can use other protocols like CoovaChilli or Chillispot, which offer more advanced features but can be harder to configure.
*   **Custom Login Page:** The Hotspot login page can be customized for branding and user experience purposes.

## MikroTik REST API Examples (if applicable):

While specific RADIUS configurations are not directly accessible by the MikroTik REST API, the following example demonstrate the creation of Hotspot Server via the API. This would allow you to automate the provisioning of the hotspot configuration.

* **Endpoint:** `/ip/hotspot/server`

* **Method:** `POST`

*   **Request JSON Payload:**
    ```json
    {
    	"name": "hotspot-server-api",
        "interface":"vlan-46",
        "profile": "hotspot-vlan-46",
        "disabled": false
    }
    ```
    *   **Explanation:**
        *  `name`: Sets the name of the hotspot server.
        * `interface`: Sets the interface to be used by the server.
        *  `profile`: Sets the hotspot profile to be used.
        *  `disabled`: `false` value enables the server.
*   **Expected Successful Response (200 OK):**

    ```json
        [
         {
            ".id": "*12",
            "name": "hotspot-server-api",
            "interface": "vlan-46",
            "profile": "hotspot-vlan-46",
            "disabled": false
         }
        ]
    ```
* **Error Handling:**

   If the request cannot be performed a `400 Bad Request` error may be returned. If an already existing `name` is used a `500 Internal Server Error` will be returned with a message indicating that the element already exist.

## Security Best Practices:

*   **Strong RADIUS Secret:** Use a strong, complex, and unique shared secret for RADIUS communication.
*   **Restrict Access:** Limit network access to the RADIUS server, if possible, only allow the IP of the Mikrotik to send queries to this server.
*   **HTTPS for Login Page:** Use HTTPS for the Hotspot login page to protect user credentials.
*   **Regular Audits:** Regularly review and update the configuration, RADIUS secret, and user credentials.
*   **Hotspot User Separation:** Employ VLANs and access control lists to isolate Hotspot traffic from other parts of the network.

## Self Critique and Improvements:

This configuration is a solid foundation for a basic RADIUS setup on a MikroTik router. Potential improvements could include:

*   **More granular control:** Implement more specific RADIUS attributes for user group control, such as bandwidth management or per-user ACLs.
*   **Automation:** Automate user provisioning and configuration via a centralized system, preferably using the API.
*  **Error handling:** add retry mechanisms and error handling to the Radius connection.
* **More sophisticated logging:** Enable specific accounting and debug level logs on both the MikroTik and RADIUS servers.

## Detailed Explanations of Topic:

RADIUS (Remote Authentication Dial-In User Service) is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users connecting to a network.  In a hotspot network, RADIUS allows a centralized server to handle user authentication, instead of storing credentials directly on the MikroTik router. The RADIUS server makes decisions to allow or deny network access based on the credentials that are send to it.
MikroTik routers act as RADIUS clients, sending authentication and accounting requests to the RADIUS server and acting upon the responses. This approach offers several advantages, including:

*   **Centralized User Management:** Manage all user accounts and permissions from a single location.
*   **Improved Security:** Prevents the storage of sensitive user credentials on multiple devices.
*   **Enhanced Flexibility:** Easier to implement complex authentication schemes and policies.
*   **Scalability:** Can handle many concurrent users without impacting the performance of the MikroTik router.
*   **Reporting:**  RADIUS Accounting allows detailed tracking of user usage.

## Detailed Explanation of Trade-offs:

*   **Using RADIUS vs. Local Authentication:**
    *   **Local Authentication:** Simple to setup but not scalable, it stores users on the device and is hard to maintain.
    *   **RADIUS:** More complex but scalable and secure.  Requires a separate RADIUS server but offers a better level of control, security and scalability.
*   **RADIUS Timeout:**
    *   **Short Timeout:**  Causes issues when the RADIUS server is busy or has poor performance.
    *   **Long Timeout:** May affect user experience with longer delays for login attempts.
*   **Accounting:**
    *   **Without Accounting:** Easier to setup and monitor, but has no detail on users' usage.
    *   **With Accounting:** Provides usage logs, but consumes resources on both the MikroTik router and the RADIUS server.

## Configuration for Specific RouterOS Versions:

The commands and configurations shown in this document are applicable to both RouterOS 6.48 and 7.x. However, while there are no major differences for the commands used here, be sure to always check the RouterOS documentation to make sure you are using the proper commands.

This comprehensive documentation should equip you to configure RADIUS on your MikroTik router effectively. If you have further questions or need more specific scenarios addressed, feel free to ask.

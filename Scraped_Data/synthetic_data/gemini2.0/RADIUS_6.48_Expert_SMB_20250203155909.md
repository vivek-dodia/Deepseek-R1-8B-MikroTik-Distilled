Okay, let's craft a detailed technical documentation for configuring RADIUS authentication on a MikroTik RouterOS device, focusing on version 6.48, within the provided context.

## Scenario Description:

This document outlines the configuration steps for enabling RADIUS authentication on a MikroTik router, specifically for clients connected to a network on the `bridge-48` interface, residing in the 176.112.195.0/24 subnet. The RADIUS server will be used to authenticate user credentials for gaining network access. This configuration is typical for an SMB environment needing centralized authentication for wireless or wired users.

## Implementation Steps:

Here's a step-by-step guide to configure RADIUS on your MikroTik router.

### 1. Step 1: Configure the Bridge Interface and IP Address
Before setting up RADIUS, we need to ensure the bridge interface `bridge-48` is configured with the appropriate IP address and subnet.

**Before:**
- Initially the interface may or may not exist. The interface has no assigned IP address.

**Command (CLI):**

```mikrotik
/interface bridge
add name=bridge-48
/interface bridge port
add bridge=bridge-48 interface=ether1 # Assuming ether1 is to be part of the bridge, adjust to your setup
/ip address
add address=176.112.195.1/24 interface=bridge-48
```

**Explanation:**

*   `/interface bridge add name=bridge-48`: Creates a new bridge interface named `bridge-48`.
*   `/interface bridge port add bridge=bridge-48 interface=ether1`: Adds the `ether1` interface (or any relevant interface) to the `bridge-48` bridge.  Replace `ether1` with the appropriate interface.
*   `/ip address add address=176.112.195.1/24 interface=bridge-48`: Assigns the IP address 176.112.195.1/24 to the bridge interface `bridge-48`, acting as the gateway for the subnet.

**After:**
- Interface `bridge-48` should be created.
- Interface `ether1` should be added to `bridge-48`.
- Interface `bridge-48` should have the IP address 176.112.195.1/24.

**Winbox GUI:**

1.  Go to `Bridge > +` and create `bridge-48`.
2.  Go to `Bridge > Ports > +`, select your interface (e.g., `ether1`), and set the `Bridge` to `bridge-48`.
3.  Go to `IP > Addresses > +`, and enter the address `176.112.195.1/24` and choose the interface `bridge-48`.

### 2. Step 2: Add a RADIUS Server Configuration
Now we configure the MikroTik to communicate with the RADIUS server.

**Before:**
- There is no RADIUS server configuration on the MikroTik.

**Command (CLI):**

```mikrotik
/radius
add address=192.168.88.100 secret=mysecret service=ppp timeout=3
```

**Explanation:**

*   `/radius add`: Creates a new RADIUS server configuration.
*   `address=192.168.88.100`: Specifies the IP address of the RADIUS server. Replace with your actual server's IP.
*   `secret=mysecret`: Sets the shared secret key that the MikroTik will use to authenticate with the RADIUS server. Replace `mysecret` with your actual shared secret key. This must match the one configured on the RADIUS server.
*   `service=ppp`: Specifies the type of service for the RADIUS configuration. For our bridge configuration we are using ppp, and will use the configuration to authenticate user accounts.
*   `timeout=3`: Set timeout for connection with radius server.

**After:**
- A RADIUS server configuration has been created and will be used to authenticate users.

**Winbox GUI:**

1.  Go to `Radius` and click `+`.
2.  Enter the `Address` (e.g., `192.168.88.100`), the `Secret` (`mysecret`), the `Service` (set to `ppp`) and `Timeout` to 3 seconds.

### 3. Step 3: Configure PPP Profile to use RADIUS
Here, we configure a PPP Profile to use the RADIUS configuration.

**Before:**
- There is no RADIUS authentication being performed for user logins.

**Command (CLI):**

```mikrotik
/ppp profile
add name=radius-ppp-profile use-radius=yes local-address=176.112.195.20 remote-address=176.112.195.21
```

**Explanation:**

* `/ppp profile add name=radius-ppp-profile`: Creates a new PPP profile named `radius-ppp-profile`.
* `use-radius=yes`: Enables RADIUS authentication for this profile.
* `local-address=176.112.195.20`: Assigns a local IP address within the subnet for users connecting via this profile.
* `remote-address=176.112.195.21`: Defines the IP address that will be assigned to users logging in with this profile.

**After:**
- The `radius-ppp-profile` will force the MikroTik to query the RADIUS server for any connection that makes use of this profile.

**Winbox GUI:**

1. Go to `PPP > Profiles`, and click `+`.
2. Set the `Name` to `radius-ppp-profile`, check the `Use Radius` box, and fill in the `Local Address` (e.g., `176.112.195.20`) and `Remote Address` (e.g., `176.112.195.21`) fields.

### 4. Step 4: Add a user to use this configuration
Add a user to use the configuration setup in the previous steps.

**Before:**
- There are no user accounts configured to use `radius-ppp-profile`.

**Command (CLI):**

```mikrotik
/ppp secret add name=testuser password=testpass profile=radius-ppp-profile
```

**Explanation:**

*   `/ppp secret add name=testuser`: Creates a new user named `testuser`.
*   `password=testpass`: Sets the password for the user.
*   `profile=radius-ppp-profile`: Assigns the user the previously created `radius-ppp-profile`, which will make the router query the RADIUS server for login credentials.

**After:**
- A new user is created which will authenticate via the RADIUS server.

**Winbox GUI:**

1. Go to `PPP > Secrets`, and click `+`.
2. Set the `Name` to `testuser`, the `Password` to `testpass`, and the `Profile` to `radius-ppp-profile`.

## Complete Configuration Commands:

```mikrotik
/interface bridge
add name=bridge-48
/interface bridge port
add bridge=bridge-48 interface=ether1
/ip address
add address=176.112.195.1/24 interface=bridge-48
/radius
add address=192.168.88.100 secret=mysecret service=ppp timeout=3
/ppp profile
add name=radius-ppp-profile use-radius=yes local-address=176.112.195.20 remote-address=176.112.195.21
/ppp secret add name=testuser password=testpass profile=radius-ppp-profile
```

## Common Pitfalls and Solutions:

*   **RADIUS Server Unreachable:**
    *   **Problem:** The MikroTik cannot communicate with the RADIUS server.
    *   **Solution:** Verify the RADIUS server IP address, shared secret, and network connectivity. Use `ping` to test connectivity, and check the RADIUS server logs for connection attempts.
*   **Shared Secret Mismatch:**
    *   **Problem:** The secret on the MikroTik doesn't match the one on the RADIUS server.
    *   **Solution:** Ensure the secret is identical on both devices. Double check your spelling.
*   **RADIUS Service Incorrect:**
    *   **Problem:** The radius service is not set to the expected value.
    *  **Solution:** Ensure the radius service is set to `ppp` for ppp user authentication.
*   **User Not Authorized:**
    *   **Problem:** The user's credentials are not configured on the RADIUS server, or they have incorrect settings.
    *   **Solution:** Verify user configuration on the RADIUS server. Check that the usernames match. Check the MikroTik logs for denied authentication attempts (`/system logging print`).
*   **Timeout Issues:**
    *   **Problem:** RADIUS requests are timing out, leading to failed authentication.
    *   **Solution:** Increase the `timeout` parameter within the radius configuration or verify the RADIUS server is running correctly. Also ensure that the network connection between the MikroTik and RADIUS server is functioning.

## Verification and Testing Steps:

1.  **Ping RADIUS Server:** Use `ping 192.168.88.100` from the MikroTik terminal to verify network reachability to the RADIUS server.
2.  **Check MikroTik Logs:** Use `/system logging print` to see any relevant RADIUS authentication attempts, successes, or failures. Look for radius-related entries.
3.  **Test Authentication:** Attempt to connect as a user defined on the Mikrotik using the defined profile. Monitor the logs to check whether an authentication attempt is taking place with the RADIUS server.
4.  **Monitor RADIUS Server Logs:** Verify that the RADIUS server is receiving authentication requests and responding correctly.

## Related Features and Considerations:

*   **Accounting:** Configure RADIUS accounting to log user activity, which could be useful for monitoring and billing purposes.
*   **Multiple RADIUS Servers:** Configure redundant RADIUS servers for failover. If the primary server is unavailable, the router can try the secondary one.
*   **RADIUS Proxy:** If you have an extensive infrastructure, you could consider using a RADIUS proxy to centralize your RADIUS services.
*   **DHCP:** Combine with DHCP to issue IP addresses to users.
*   **Firewall:** Configure firewall rules to restrict access based on user groups.

## MikroTik REST API Examples:

While the RADIUS configuration is available via the API, direct user management using `/ppp secret` requires using the `/ppp/secret` resource with authentication parameters. The following example shows creation of a RADIUS config and a user.
Note that in general the API endpoints directly reflect the CLI structure in RouterOS.

**Create RADIUS config:**

*   **Endpoint:** `/radius`
*   **Method:** POST
*   **Payload (JSON):**

```json
{
  "address": "192.168.88.100",
  "secret": "mysecret",
  "service": "ppp",
  "timeout": 3
}
```

*   **Response (Success):**

```json
{
  ".id": "*1",
  "address": "192.168.88.100",
  "secret": "mysecret",
  "service": "ppp",
  "timeout": "3",
  "authentication": "yes",
  "accounting": "no"
}
```
*   **Response (Error):**
    ```json
    { "message": "invalid value for argument 'address' - expected IP address" }
   ```

**Create PPP User:**

*   **Endpoint:** `/ppp/secret`
*   **Method:** POST
*   **Payload (JSON):**

```json
{
 "name": "testuser",
 "password": "testpass",
 "profile": "radius-ppp-profile"
}
```

*   **Response (Success):**

```json
{
        ".id": "*2",
        "name": "testuser",
        "service": "any",
        "caller-id": "",
        "password": "testpass",
        "profile": "radius-ppp-profile",
        "disabled": "false"
}
```

*   **Response (Error):**

```json
{
  "message": "already have a user with this name"
}
```

Note: Make sure to handle JSON exceptions and provide proper validation on the returned data. Make sure to have proper authentication set up when using the MikroTik API.

## Security Best Practices

*   **Strong Shared Secret:** Use a strong and complex shared secret for RADIUS authentication. Do not use weak or easily guessable secrets.
*   **Secure Communication:**  Consider using RADIUS over IPsec for enhanced security and confidentiality between your MikroTik router and the RADIUS server. This requires an additional configuration of IPsec.
*   **Access Control:** Restrict access to the MikroTik router and the RADIUS server to authorized personnel only. Utilize user based access controls (Role Based Access Control) for administrators.
*   **Regular Audits:** Audit your configuration and logs regularly for any security breaches.
*   **Firmware Updates:** Keep your RouterOS and RADIUS server software up to date with the latest security patches.
*   **Disable Unused Services:** Disable any unused services on your RouterOS device to minimize the attack surface.
*   **Firewall Rules:** Utilize firewall rules to restrict access to the radius service to specific addresses.

## Self Critique and Improvements

This configuration provides a basic yet solid starting point for using RADIUS on a MikroTik router.  Here's some room for improvement:

*   **User Grouping:** A more sophisticated configuration could include assigning users to different user groups (e.g., via RADIUS attributes) and applying different profiles and access policies. This would require using a more complex configuration on the radius server.
*   **Dynamic Authorization:** Implementation of dynamic authorization (CoA – Change of Authorization) is possible with RADIUS. This allows for real-time changes to user settings.
*   **Detailed Accounting:** Currently the example only enables authentication. A more detailed configuration can be created to enable accounting and monitor the activity of connected users.
*   **IPSec:** RADIUS configuration with IPsec would provide additional security.
*  **Rate Limiting:** Implement per user rate limiting.
*  **Centralized logging:** Offload all system logs to a dedicated server for easier monitoring and inspection.

## Detailed Explanations of Topic

**RADIUS (Remote Authentication Dial-In User Service)** is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) for users trying to access network services. A RADIUS client (like your MikroTik router) sends authentication requests to the RADIUS server. The RADIUS server verifies the credentials against a database (or other authentication method), and responds with whether the user is allowed or denied access. A successful authentication allows for a subsequent accounting process which monitors user activity, such as time spent connected.

## Detailed Explanation of Trade-offs

*   **Local User Database vs. RADIUS:**
    *   **Local Database:** Simple to set up and manage for smaller networks, but difficult to maintain in larger scale environments.
    *   **RADIUS:** Provides centralized management for many users, making it easier to administer large networks. A disadvantage is that it can become a single point of failure unless implemented with redundancy.
*   **Service Selection:** The specific RADIUS service that is selected should correspond to the type of connection being used. Using an incorrect service can result in authentication failures.
*   **Shared Secret Length:** A long shared secret will offer more security, however, will be more difficult to remember and manually configure across many devices. It may require storing it in a password vault.
*   **Timeout Length:** The timeout value specifies the time before a request is considered failed. Setting a too short of a timeout could result in connection problems if there is any latency on the connection with the server. Setting too long of a timeout could make the connection slow and not responsive.

## Configuration for Specific RouterOS Versions:

The provided commands and configuration steps are generally compatible with RouterOS versions 6.48 and 7.x. However, it's always best practice to consult the official MikroTik documentation for any specific syntax changes or updates for the version you are using.

This completes the detailed technical documentation for RADIUS authentication on a MikroTik RouterOS device. Let me know if you need further adjustments or have any other requests!

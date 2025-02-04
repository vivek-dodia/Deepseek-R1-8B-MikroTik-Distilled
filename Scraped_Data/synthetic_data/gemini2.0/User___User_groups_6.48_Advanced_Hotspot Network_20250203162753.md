Okay, let's dive deep into user and user group management on a MikroTik RouterOS 6.48 device, focusing on a Hotspot network scenario. This will be an advanced configuration and tailored to the given subnet and interface.

## Scenario Description:

We are configuring a MikroTik router for a hotspot network using the `wlan-71` interface connected to a wireless access point.  We will define multiple user groups with varying upload/download speeds and user profiles associated with each. This configuration will be applicable to a small to medium business hotspot network. The IP subnet for this network is `46.138.222.0/24`.

## Implementation Steps:

### Step 1: Initial Router State & Interface Verification
* **Goal:** Verify the initial state of the `wlan-71` interface. This will confirm if the interface is properly configured before the addition of users.
* **CLI Command (Before):**
  ```mikrotik
  /interface print where name=wlan-71
  ```
* **Expected Output:** (Will vary depending on your setup).
  ```
  Flags: D - dynamic, X - disabled, R - running, S - slave
  #    NAME                                TYPE       MTU  MAC-ADDRESS       ARP       MASTER-PORT
  0  R wlan-71                             wlan       1500 xx:xx:xx:xx:xx:xx  enabled   none
  ```
* **GUI Instruction:** In Winbox, navigate to *Interfaces*. Verify that the `wlan-71` interface exists and is enabled.
* **Explanation:** We are checking for the existence of our interface and that is up and running. If the interface is not enabled, we will need to enable it first. The `R` flag indicates that the interface is running.
* **CLI Command (After):** No change to the interface at this time.

### Step 2: Creating User Profiles
* **Goal:**  Define user profiles with different data rates using the `/ppp profile` command.
* **CLI Commands:**
  ```mikrotik
  /ppp profile add name=basic-user local-address=46.138.222.100 remote-address=46.138.222.200 rate-limit=512k/2M
  /ppp profile add name=premium-user local-address=46.138.222.101 remote-address=46.138.222.201 rate-limit=2M/10M
  /ppp profile add name=admin-user local-address=46.138.222.102 remote-address=46.138.222.202 rate-limit=50M/50M
  ```
* **GUI Instruction:**  Navigate to *PPP* then *Profiles* and add a new profile for each user group with the corresponding rate limits.
* **Explanation:**  We are creating three different user profiles: `basic-user`, `premium-user`, and `admin-user`, with different upload/download speeds using the `rate-limit` parameter. `local-address` and `remote-address` specify the IP address range.
* **CLI Command (After):**
   ```mikrotik
  /ppp profile print
  ```
* **Expected Output:**
  ```
  Flags: * - default
   0    name="default" use-encryption=yes only-one=no change-tcp-mss=yes 
        address-list="" dns-server=""  rate-limit="0/0" 
        incoming-filter=""  outgoing-filter=""  
   1    name="basic-user" use-encryption=no only-one=no change-tcp-mss=yes 
        local-address=46.138.222.100 remote-address=46.138.222.200  
        rate-limit="512k/2M" address-list="" dns-server="" 
        incoming-filter="" outgoing-filter="" 
   2    name="premium-user" use-encryption=no only-one=no change-tcp-mss=yes 
        local-address=46.138.222.101 remote-address=46.138.222.201  
        rate-limit="2M/10M" address-list="" dns-server="" 
        incoming-filter="" outgoing-filter="" 
   3    name="admin-user" use-encryption=no only-one=no change-tcp-mss=yes 
        local-address=46.138.222.102 remote-address=46.138.222.202 
        rate-limit="50M/50M" address-list="" dns-server="" 
        incoming-filter="" outgoing-filter=""
  ```

### Step 3: Creating User Accounts
* **Goal:** Add user accounts to the router with the correct user profiles using the `/ppp secret` command.
* **CLI Commands:**
  ```mikrotik
  /ppp secret add name=basic1 password=basic1 service=hotspot profile=basic-user
  /ppp secret add name=premium1 password=premium1 service=hotspot profile=premium-user
  /ppp secret add name=admin1 password=admin1 service=hotspot profile=admin-user
  ```
* **GUI Instruction:**  Navigate to *PPP* then *Secrets* and add a new secret for each user with the corresponding profiles and password. Ensure service is set to `hotspot`.
* **Explanation:**  We are creating three users, `basic1`, `premium1` and `admin1`, each associated with a specific profile. The service needs to be set to `hotspot`.
* **CLI Command (After):**
    ```mikrotik
  /ppp secret print
    ```
* **Expected Output:**
  ```
  Flags: X - disabled, D - dynamic 
   0  name="basic1"    password="basic1"   service=hotspot profile=basic-user  
        caller-id=""    comment=""          encoding=default 
   1  name="premium1"  password="premium1" service=hotspot profile=premium-user 
        caller-id=""    comment=""          encoding=default 
   2  name="admin1"    password="admin1"   service=hotspot profile=admin-user  
        caller-id=""    comment=""          encoding=default
  ```

### Step 4: Setting up Hotspot Server
* **Goal:** Create the Hotspot server interface on `wlan-71`.
* **CLI Commands:**
  ```mikrotik
  /ip hotspot add name=hotspot1 interface=wlan-71 address-pool=hotspot-pool profile=default
  /ip hotspot ip-binding add mac-address=00:00:00:00:00:00 type=bypassed comment=Allow-Direct-Access
  /ip pool add name=hotspot-pool ranges=46.138.222.10-46.138.222.254
  /ip hotspot profile set default use-radius=no
  /ip hotspot profile add name=hsprofile1 login-by=cookie,http-pap,mac-cookie dns-name=hotspot.example.com html-directory=hotspot
  /ip hotspot set hotspot1 profile=hsprofile1
  ```
* **GUI Instruction:** Navigate to *IP* then *Hotspot* and create a hotspot server on `wlan-71`. Then add a profile, and assign to the new hotspot. Add a new IP pool for this hotspot network.
* **Explanation:**
  *  `/ip hotspot add`: This creates a hotspot instance named `hotspot1` bound to the `wlan-71` interface. The `address-pool` parameter specifies which address pool should be used.
  * `/ip hotspot ip-binding add`: This adds an exception for MAC address `00:00:00:00:00:00` which allows direct access without login. It is best practice to have this and assign to the routers MAC.
  * `/ip pool add`: This defines a pool of IP addresses for the hotspot network.
  * `/ip hotspot profile set default`: This disables the default radius service to make things simple.
  * `/ip hotspot profile add name=hsprofile1`: This creates a hotspot profile with specific login options and DNS name (for custom login pages).
  * `/ip hotspot set hotspot1 profile=hsprofile1`: This assigns the `hsprofile1` to the hotspot service.
* **CLI Command (After):**
    ```mikrotik
  /ip hotspot print
  /ip hotspot profile print
  /ip pool print
    ```
* **Expected Output:**
  ```
  Flags: X - disabled, I - invalid
   0   name="hotspot1"  interface=wlan-71  profile="hsprofile1" address-pool="hotspot-pool" 
        idle-timeout=5m keepalive-timeout=10m status-autorefresh=1m 
        
  Flags: * - default
   0  *  name="default"  use-radius=no login-by=cookie,http-pap  
           dns-name="" html-directory=""  
   1      name="hsprofile1"  use-radius=no login-by=cookie,http-pap,mac-cookie  
          dns-name="hotspot.example.com" html-directory="hotspot" 
   
  Flags: D - dynamic
  #   NAME      RANGES            
  0   hotspot-pool 46.138.222.10-46.138.222.254
  ```

### Step 5: Optional - Custom Hotspot Pages
* **Goal:** If you want to customize the hotspot login page, upload custom HTML, CSS, JS files to the router's `hotspot` directory by FTP.
* **GUI Instruction:** Connect to the router through FTP (e.g. Filezilla) and upload to `/hotspot` folder. Ensure your user and pass have the permission.

### Step 6: (Optional) Add a walled-garden for specific domains
* **Goal:** Allow users to reach specific sites (e.g. your company website) without needing to log in first.
* **CLI Command:**
   ```mikrotik
  /ip hotspot walled-garden ip add dst-address=172.217.160.142 comment="google.com IP"
  /ip hotspot walled-garden domain add domain=google.com comment="google.com"
    ```
* **GUI Instruction:** Navigate to `IP` and then `Hotspot`, then to `Walled Garden`.
* **Explanation:** This allows the website on the IP `172.217.160.142` and on the `google.com` domain name to be accessible before authentication.

## Complete Configuration Commands:
```mikrotik
/interface print where name=wlan-71

/ppp profile add name=basic-user local-address=46.138.222.100 remote-address=46.138.222.200 rate-limit=512k/2M
/ppp profile add name=premium-user local-address=46.138.222.101 remote-address=46.138.222.201 rate-limit=2M/10M
/ppp profile add name=admin-user local-address=46.138.222.102 remote-address=46.138.222.202 rate-limit=50M/50M

/ppp secret add name=basic1 password=basic1 service=hotspot profile=basic-user
/ppp secret add name=premium1 password=premium1 service=hotspot profile=premium-user
/ppp secret add name=admin1 password=admin1 service=hotspot profile=admin-user

/ip pool add name=hotspot-pool ranges=46.138.222.10-46.138.222.254
/ip hotspot add name=hotspot1 interface=wlan-71 address-pool=hotspot-pool profile=default
/ip hotspot ip-binding add mac-address=00:00:00:00:00:00 type=bypassed comment=Allow-Direct-Access
/ip hotspot profile set default use-radius=no
/ip hotspot profile add name=hsprofile1 login-by=cookie,http-pap,mac-cookie dns-name=hotspot.example.com html-directory=hotspot
/ip hotspot set hotspot1 profile=hsprofile1

/ip hotspot walled-garden ip add dst-address=172.217.160.142 comment="google.com IP"
/ip hotspot walled-garden domain add domain=google.com comment="google.com"
```

## Common Pitfalls and Solutions:

* **Login Problems:**
  * **Problem:** Users cannot log in using the provided credentials.
    * **Solution:** Verify username/password are correct. Check if the service for the user secret is `hotspot`.
    * **Diagnostic:** `/ppp secret print` to check secrets and `/log print` for login errors.
  * **Problem:** User is redirected back to the login page after entering credentials.
    * **Solution:** The hot spot is not working correctly, or the user's browser might not be accepting cookies. Check `/ip hotspot active print` to make sure the user is logged in correctly.
* **Speed Issues:**
  * **Problem:** Users are not receiving the correct speed profiles.
    * **Solution:** Check the rate-limits on the PPP profiles with `/ppp profile print`.
    * **Diagnostic:** Use torch or other tools to check current speed.
* **IP Address Conflicts:**
   * **Problem:** If you have configured static IP addresses, this may cause conflicts.
    * **Solution:** Ensure IP address range in the pool is correct and does not overlap with any static IP ranges.
    * **Diagnostic:** Check the IP Pool `ip pool print`.
* **High CPU Usage:**
   * **Problem:** Large number of concurrent connections in the hotspot might lead to increased CPU usage.
    * **Solution:** Ensure router's hardware is adequate, limit concurrent user sessions and apply more restrictive limits to the profiles.
    * **Diagnostic:** Use `/system resource print` to check CPU/memory usage, and tools such as the `/tool profile` to find bottleneck.

## Verification and Testing Steps:

1. **Connect to the Hotspot:** Connect a device to the `wlan-71` network.
2. **Open a Web Browser:** Attempt to access a website. You should be redirected to the hotspot login page.
3. **Login with Basic User:**  Login using the `basic1` username and password.
4. **Verify Bandwidth:** Test the internet speed with `speedtest.net`. You should get around `512k/2M`.
5. **Logout or timeout:** Disconnect and reconnect and use the `premium1` user and password.
6. **Verify Bandwidth:** Test the internet speed with `speedtest.net`. You should get around `2M/10M`.
7. **Logout or timeout:** Disconnect and reconnect and use the `admin1` user and password.
8. **Verify Bandwidth:** Test the internet speed with `speedtest.net`. You should get around `50M/50M`.
9. **Verify Login:** Use the command `/ip hotspot active print` to confirm if your users are online and are logged in.
10. **Walled Garden:** Attempt to access `google.com` before and after logging in. If the walled garden is correctly configured, it should work before login.
11. **Testing:** From the router CLI use `ping google.com` to test that the DNS configuration is working.
12. **Testing:** From a client machine on your wireless network, try pinging the router at the IP you configured.

## Related Features and Considerations:

*   **RADIUS Server:** For larger networks, consider using a RADIUS server for authentication and accounting. This is especially important in larger networks, where you will be using more complex user management strategies.
*   **Custom Login Pages:** Upload custom HTML files to the `/hotspot` directory to brand the login page.
*   **User Quota:** Set quotas on user accounts to control data usage.
*   **Firewall Rules:** Implement firewall rules to limit access to internal network segments from the hotspot network.
*   **QoS:** Prioritize traffic for critical services using Queue Trees, for example.

## MikroTik REST API Examples (if applicable):
The `/ppp` and `/ip hotspot` sections can be managed by the API. Here's an example for creating a new user with API.

```
# POST /ppp/secret
# Header:
Content-Type: application/json
X-Mikrotik-API: {YOUR_TOKEN}

# JSON Payload
{
  "name": "api_user",
  "password": "api_password",
  "service": "hotspot",
  "profile": "basic-user"
}

# Expected response (200 OK)
{
    "message": "added"
}
```

```
#GET /ppp/secret

# Expected response
{
    ".id":"*2",
    "name":"basic1",
    "password":"basic1",
    "service":"hotspot",
    "profile":"basic-user",
    "caller-id":"",
    "comment":"",
    "encoding":"default"
}
```
**Explanation:**

*   **Endpoint:** `/ppp/secret`
*   **Method:** `POST` for creating a secret, `GET` for reading.
*   **JSON Payload:** Contains the user details (name, password, service, profile).
*   **Expected Response:**  A JSON object confirming the addition (`{"message": "added"}`). You should always check for potential errors, as sometimes adding a user can fail (e.g. if a user exists with that name already).

## Security Best Practices

*   **Strong Passwords:** Enforce strong passwords for user accounts.
*   **Limit Access:** Use firewall rules to restrict access to management interfaces, only to secure addresses or networks.
*   **Regular Updates:** Keep the RouterOS firmware and packages up-to-date.
*   **Disable Default Accounts:**  Change or disable any default user accounts.
*   **Hotspot Isolation:**  Isolate the hotspot network from the internal network.
*   **HTTPS:** If you allow access to the RouterOS via Web, enable HTTPS and use secure certificates.
*   **API Security:** Limit API access to specific IP addresses and use secure tokens.

## Self Critique and Improvements
This configuration provides a solid foundation for a basic hotspot network, however some improvements could be:
*   **More granular control:** User group rate-limits could be controlled with queue trees in combination with the hotspot profiles.
*   **RADIUS for user management:** Using RADIUS server for larger scale user managements is a must.
*   **More complex login options:** This setup does not leverage the flexibility of the hotspot.
*   **More advanced firewall rules:** This setup does not include advanced firewall rules to protect the router, or client networks.
*   **Failover strategies:** A method of failover to protect the network from one route failure is not present.

## Detailed Explanations of Topic
* **Users:** On RouterOS users are managed in the `/ppp` section. The user's passwords, and profile information are specified here.
* **User Groups:** In RouterOS, user groups are called *Profiles* and are also defined in the `/ppp` section. Each profile has a name, local IP and remote IP ranges, and most importantly, rate-limits for bandwidth management. These profiles can be assigned to users.
* **Hotspot:** The hotspot service is what authenticates users on your network. It provides a login page, enforces user policies and rate-limits based on user profiles. It allows for walled-garden configuration, which allows you to offer a limited service before login.

## Detailed Explanation of Trade-offs
*   **Hotspot vs User Manager (UserMan):** The built-in hotspot server is good for smaller deployments. User Manager (a separate RouterOS package), is better suited to larger networks and more complex user management tasks with features such as Voucher codes and complex billing.
*   **Internal DHCP vs Hotspot DHCP:** You can use DHCP on the interfaces, or use the Hotspot to provide DHCP. The benefit of the Hotspot service doing DHCP is that it automatically registers clients.
*   **Static IP vs Dynamic IPs:** Using dynamic IP pools in the hotspot reduces configuration complexity. However, static IP assignments can be necessary for some use cases.

## Configuration for Specific RouterOS Versions:
This document is specifically designed for RouterOS 6.48. Be aware that command syntax or feature availability may differ in other versions of RouterOS. Always verify your RouterOS version and consult the MikroTik documentation for version-specific details.

This should give you a solid start to managing users and user groups on your MikroTik router. Let me know if you have any other questions!

Okay, let's craft a comprehensive guide on certificates within the context of a MikroTik hotspot network. This will be geared towards RouterOS 6.48, but will also include notes on RouterOS 7 where applicable.

## Scenario Description:

This scenario focuses on implementing and managing certificates for a MikroTik hotspot network operating on the 31.246.237.0/24 subnet, using the 'vlan-64' interface. We will demonstrate how to generate a self-signed certificate, use it for HTTPS access to the hotspot login page, and discuss the implications of using self-signed certificates versus those from a certificate authority (CA). This will enhance security by ensuring encrypted communication between the users and the hotspot.

**Configuration Level:** Basic
**Network Scale:** Hotspot Network (SOHO, SMB)
**Subnet:** 31.246.237.0/24
**Interface Name:** vlan-64

## Implementation Steps:

Here’s a step-by-step guide on how to generate and use a self-signed certificate for your MikroTik hotspot.

### 1. Step 1: Verify Interface and IP Address

Before setting up the certificate, ensure your interface and IP address are configured correctly.

**Before:**
```
/interface vlan print
/ip address print
```

**Expected Output (Example):**
```
/interface vlan print
Flags: X - disabled, R - running
 #    NAME                                MTU   MAC-ADDRESS        VLAN-ID  INTERFACE
 0  R vlan-64                              1500  XX:XX:XX:XX:XX:XX  64       ether1

/ip address print
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE         
 0   192.168.88.1/24    192.168.88.0    ether2            
 1   31.246.237.1/24   31.246.237.0   vlan-64
```

**Action:**
- If the interface `vlan-64` and IP address `31.246.237.1/24` on vlan-64 are not configured, configure it before proceeding using these commands.

```
/interface vlan add name=vlan-64 vlan-id=64 interface=ether1
/ip address add address=31.246.237.1/24 interface=vlan-64
```
* `interface vlan add`: Creates a new VLAN interface with a specified name, VLAN ID, and physical interface to bind to.
    * `name`: Sets the name of the new interface.
    * `vlan-id`: Sets the VLAN ID.
    * `interface`: Specifies the physical interface on which the VLAN will be configured.
* `ip address add`: Adds a new IP address to an interface.
    * `address`: Sets the IP address and subnet mask in CIDR notation.
    * `interface`: Specifies the interface to assign the address.
- After running the commands, double-check using `/interface vlan print` and `/ip address print` to make sure the interface is configured properly and the IP address is assigned.

**After:**
```
/interface vlan print
/ip address print
```

**Expected Output (Example):**
```
/interface vlan print
Flags: X - disabled, R - running
 #    NAME                                MTU   MAC-ADDRESS        VLAN-ID  INTERFACE
 0  R vlan-64                              1500  XX:XX:XX:XX:XX:XX  64       ether1

/ip address print
Flags: X - disabled, I - invalid, D - dynamic
 #   ADDRESS            NETWORK         INTERFACE         
 0   192.168.88.1/24    192.168.88.0    ether2            
 1   31.246.237.1/24   31.246.237.0   vlan-64
```

### 2. Step 2: Generate a Self-Signed Certificate

We'll use MikroTik's certificate generation tool to create a self-signed certificate. This will be used for HTTPS access to the Hotspot login page.

**Before:**
```
/certificate print
```

**Expected Output (Example):**
```
Flags: K - private-key, A - authority, D - dynamic
 #   NAME                                SUBJECT                                                                   
```

**Action:**
- Generate a self-signed certificate named `hotspot-cert` for the IP address of your hotspot interface, valid for a specific time (e.g., 365 days), and with appropriate key usage. In real-world situations, you'd typically use your domain here. Using your IP is acceptable for initial testing. Replace 31.246.237.1 with the correct IP address of the vlan-64. Also, be aware that IP addresses can be seen as less secure than fully qualified domain names.
```
/certificate add name=hotspot-cert common-name=31.246.237.1 key-usage=tls-server,digital-signature,key-encipherment days-valid=365
```
* `/certificate add`: Creates a new certificate.
    * `name`: Sets the name of the certificate.
    * `common-name`: Sets the subject of the certificate which should match the hostname or IP address the certificate is to be used on.
    * `key-usage`: Specifies the intended purposes of the key. Common options include `tls-server` for HTTPS servers and `tls-client` for client authentication. Multiple key usages can be set using comma-separated values.
    * `days-valid`: Specifies how long the certificate should be valid from the time of generation in days.
- This command generates both the private key and the certificate.

**After:**
```
/certificate print
```

**Expected Output (Example):**
```
Flags: K - private-key, A - authority, D - dynamic
 #   NAME                                SUBJECT                     
 0  KA hotspot-cert                    CN=31.246.237.1
```
- The `KA` flag indicates that the certificate has a private key and is marked as authority because the certificate is self-signed.

### 3. Step 3: Enable HTTPS on Hotspot Interface

Now we will set the previously generated certificate to be used by the hotspot's HTTPS login feature.

**Before:**
```
/ip hotspot print
```

**Expected Output (Example):**
```
Flags: X - disabled, I - invalid
 #   NAME                                 INTERFACE           PROFILE             
```

**Action:**
- First, create a hotspot profile named `hotspot-profile` and bind it to the interface `vlan-64`.
```
/ip hotspot profile add name=hotspot-profile html-directory=hotspot
/ip hotspot add name=hotspot1 interface=vlan-64 profile=hotspot-profile
```
  * `/ip hotspot profile add`: Creates a new hotspot profile that is used to customize a Hotspot's settings.
    * `name`: Specifies the name of the hotspot profile.
    * `html-directory`: Sets the directory where the custom hotspot web pages are stored.
  * `/ip hotspot add`:  Enables a hotspot on a given interface using a defined profile.
    * `name`: Sets the name of the hotspot.
    * `interface`: Specifies the interface that the hotspot will be running on.
    * `profile`: Specifies which profile will be used.

- Now set the HTTPS certificate in use by the hotspot profile.
```
/ip hotspot profile set hotspot-profile https-certificate=hotspot-cert
```
 * `/ip hotspot profile set`: Changes the settings of a given hotspot profile.
   *  `https-certificate`: Specifies the certificate to use for HTTPS access to the Hotspot login page.

**After:**
```
/ip hotspot print
```
```
/ip hotspot profile print
```

**Expected Output (Example):**
```
Flags: X - disabled, I - invalid
 #   NAME                                 INTERFACE           PROFILE
 0 R hotspot1                             vlan-64             hotspot-profile

Flags: * - default
 #   NAME                                 COOKIE-L   SESSION-T  LOGIN-T    KEEP-A... UPLINK-B   HTML-D
 0 * hotspot-profile                      1d         1d         5m         5m      
```
and the following can be seen in the profile detail
```
    [..]
    use-radius: no
    https-certificate: hotspot-cert
    https-port: 443
    [..]
```

### 4. Step 4: Optional: Enable HTTPS Login Only

To enhance security further, disable HTTP and force all logins to use HTTPS.

**Before:**
```
/ip hotspot profile print
```
**Action:**

- Configure the Hotspot profile to only use HTTPS logins.
```
/ip hotspot profile set hotspot-profile login-by=https
```

* `/ip hotspot profile set`: Changes the settings of a given hotspot profile.
  *  `login-by`: Sets the login methods available. Values could include `http`,`https`, and `http-chap`.

**After:**
```
/ip hotspot profile print
```

**Expected Output (Example):**

```
    [..]
    login-by: https
    https-certificate: hotspot-cert
    https-port: 443
    [..]
```

## Complete Configuration Commands:

Here's the complete set of commands to implement the setup:

```
/interface vlan add name=vlan-64 vlan-id=64 interface=ether1
/ip address add address=31.246.237.1/24 interface=vlan-64

/certificate add name=hotspot-cert common-name=31.246.237.1 key-usage=tls-server,digital-signature,key-encipherment days-valid=365

/ip hotspot profile add name=hotspot-profile html-directory=hotspot
/ip hotspot add name=hotspot1 interface=vlan-64 profile=hotspot-profile
/ip hotspot profile set hotspot-profile https-certificate=hotspot-cert
/ip hotspot profile set hotspot-profile login-by=https
```

## Common Pitfalls and Solutions:

*   **Certificate Not Trusted:** Self-signed certificates are not trusted by browsers. Users will see a warning, which they can bypass (though not advisable). Using a certificate from a trusted CA will solve this issue.
*   **Incorrect Common Name:** If the certificate's common name does not match the hostname or IP address users access, they will see certificate errors. Ensure your hostname or IP is the same as the `common-name` in the generated certificate.
*   **Expired Certificate:** If the `days-valid` period expires, you will get an SSL error. Regenerate a new certificate, and change the `https-certificate` parameter for the given hotspot profile.
*   **Incorrect Key Usage:** Verify that you included the `tls-server` key usage when creating the certificate if you are using it for HTTPS. If not you will get a certificate error.
*   **Hotspot Not Working After Certificate Change:** If the hotspot service does not start after changing a certificate, check the logs for any errors related to certificates, and try a restart of the service. `/system reboot`.

## Verification and Testing Steps:

1.  **Access the Hotspot Login Page:** Connect to the hotspot network and open a web browser. Navigate to `https://31.246.237.1` in the address bar.
2.  **Certificate Warning:** You'll likely see a browser warning stating the connection is not private because of the self-signed certificate. Proceed to the login page if you would like to use the hotpot.
3.  **Successful HTTPS Connection:** Observe the padlock icon in the address bar (although marked with a warning).
4.  **Test HTTP Login:** If you did not disable the HTTP login, navigate to `http://31.246.237.1`. You should see the login page. If you enabled `login-by=https`, you should be redirected to the HTTPS login page.
5.  **Check Certificate Details:** View the certificate details by clicking on the padlock. Verify that the certificate's `common-name`, and validity period are correct.

## Related Features and Considerations:

*   **Certificate Authority (CA) Certificates:** For production environments, obtaining a certificate signed by a trusted CA is recommended. This avoids browser warnings and enhances trust. Import the CA certificate using the `/certificate import` command, and select the newly imported certificate in the hotspot profile.
*   **Custom Hotspot Pages:** Customize your login page with your company logo and branding by modifying the HTML content in the `/flash/hotspot/` directory.
*   **Hotspot Features:** Configure other hotspot features such as user profiles, walled garden, and rate limiting.
*   **ACME Clients:** MikroTik supports ACME (Automatic Certificate Management Environment) clients that can automatically get a Let's Encrypt certificate.

## MikroTik REST API Examples:

While generating certificates using the CLI is simpler for most cases, you can manage certificates through the MikroTik REST API. Here are a few examples using the API endpoint `/certificate`:

**Create a self-signed certificate**

**API Endpoint:** `https://<router-ip>/rest/certificate`
**Request Method:** `POST`
**Example JSON Payload:**

```json
{
    "name": "hotspot-cert-api",
    "common-name": "31.246.237.1",
    "key-usage": "tls-server,digital-signature,key-encipherment",
    "days-valid": 365
}
```
**Expected Response:**

A successful response would be a 200 OK with a JSON object including the certificate details. A 400 will be returned if parameters are missing.

**Get certificate information:**
**API Endpoint:** `https://<router-ip>/rest/certificate`
**Request Method:** `GET`

**Example response**
```
[
  {
    "id": "*10",
    "name": "hotspot-cert",
    "common-name": "31.246.237.1",
     "key-usage": "tls-server,digital-signature,key-encipherment",
     "days-valid": "365"
   }
]

```
**Example response (if there are errors)**
```
{
  "error": "invalid command"
}
```

**Set certificate in hotspot profile:**

**API Endpoint:** `https://<router-ip>/rest/ip/hotspot/profile/<profile-id>`
**Request Method:** `PATCH`

**Example JSON Payload:**
```json
{
    "https-certificate": "hotspot-cert-api"
}
```

**Expected Response:**

A successful response would be a 200 OK. A 400 will be returned if the resource is not found, or the parameters are invalid.

**Error Handling:**
*   **Authentication Issues:** If the API request fails, confirm you have the correct API credentials with proper permissions.
*   **Parameter Errors:** If the API returns a 400 error, review the parameters and make sure they are valid and have the correct type. Check the API documentation for correct parameter usage.
*   **Rate Limiting:** If you make too many API calls, you might be rate limited. Be respectful of API call frequency.

## Security Best Practices

*   **Use CA-Signed Certificates:** Avoid self-signed certificates in production; use a CA certificate instead.
*   **HTTPS Only:** Enable HTTPS login only, and disable HTTP.
*   **Strong Passwords:** Use strong passwords on your MikroTik router and the API user.
*   **Limit API Access:** Do not expose the API to the internet.
*   **Regular Updates:** Keep RouterOS updated to patch any security vulnerabilities.
*   **Review Logs:** Regularly review the MikroTik logs for any security incidents.

## Self Critique and Improvements

This is a basic setup, suitable for testing and small-scale use. Here are some improvements:

*   **Automated Certificate Management:** Implement an ACME client for automated certificate renewal.
*   **Advanced Hotspot Customizations:** Use more advanced features of the Hotspot, such as multiple login methods.
*   **Traffic Shaping and QoS:** Implement traffic shaping and QoS for better bandwidth management.
*   **Comprehensive Logging:** Set up logging to an external server for more robust log analysis.
*   **Monitoring:** Set up a monitoring system to track key parameters like CPU, memory, and network traffic.

## Detailed Explanations of Topic:

Certificates are digital documents that bind a public key to an identity. They are used to verify the identity of a device or server in an encrypted communication. The most common format is the X.509 standard.

**Key Types:**
*   **Self-Signed Certificate:** A certificate signed with its own private key and is not signed by a trusted CA. They are suitable for internal testing, but not for production environments where trust is important.
*   **CA-Signed Certificate:** A certificate issued by a trusted CA (Certificate Authority). These are trusted by web browsers and devices.

**Key Concepts:**

*   **Public Key:** A key that can be freely distributed and is used to encrypt data or verify digital signatures.
*   **Private Key:** A key known only to the owner, used to decrypt data or digitally sign it.
*   **Common Name (CN):** The fully qualified domain name or the IP address that the certificate is issued for.
*   **Subject Alternative Names (SAN):** Additional hostnames or IP addresses that the certificate should be valid for.
*   **Key Usage:** Restrictions on the type of uses a certificate's key is intended for (e.g., TLS server, digital signature).
*   **Certificate Signing Request (CSR):** A file sent to the CA that contains a public key and information about the owner of the certificate.
*   **Certificate Chain:** A set of certificates starting with a trusted root CA and connecting down to the certificate of the device or server.
*   **Trust Store:**  A local storage of trusted CA certificates that are used to verify other certificates.

## Detailed Explanation of Trade-offs

*   **Self-Signed vs CA-Signed:** Self-signed certificates are free and quick to generate, but lack trust. CA-signed certificates are trusted but cost money and require a bit more configuration.
*   **HTTPS vs HTTP:** HTTPS is encrypted, protecting user data, while HTTP is unencrypted and vulnerable. The performance overhead of HTTPS is minimal on modern hardware.
*   **ACME vs Manual Certificate Management:** ACME provides automatic certificate generation and renewal, saving time and effort. Manual management is fine for infrequent use but is prone to errors.
*   **Login-by Method:** Enabling just `https` login method provides maximum security, at the expense of not allowing the insecure, and less compatible `http` method.
*   **Key Usage Parameters:** The correct parameters should be used, to properly secure the service in use. For a TLS based web service, `tls-server` should be enabled. For signing data, the `digital-signature` key usage is appropriate.

## Configuration for Specific RouterOS Versions:

*   The above configuration applies to both RouterOS 6.48 and RouterOS 7.
*   If using older versions of RouterOS, there may be differences in the commands and functionality. Please refer to the relevant RouterOS documentation for those specific versions. The general steps should remain the same, but some of the sub-parameters might be different.
*   In RouterOS v7, the certificate store is slightly different, and there are added features for ACME clients, and more advanced key usage options.
*   The REST API examples use the `/rest` endpoint, which works on both RouterOS 6.x and 7.x. If you are using a very old RouterOS version, the endpoint might be different, or even not present.

By following these detailed steps, you should be able to successfully implement certificates for your MikroTik hotspot network, enhancing security and user experience. Remember to adjust the parameters according to your specific requirements.

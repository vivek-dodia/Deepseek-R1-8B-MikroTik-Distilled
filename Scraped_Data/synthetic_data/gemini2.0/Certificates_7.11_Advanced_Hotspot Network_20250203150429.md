Okay, let's dive into a detailed configuration for managing certificates on a MikroTik RouterOS device, focusing on a hotspot network using the specified subnet (51.184.196.0/24) and interface (ether-10), within the advanced level.

## Scenario Description:

This configuration focuses on enabling secure communication for a hotspot network using certificates. Specifically, we will be generating a self-signed certificate and installing it for use with services like the hotspot's HTTPS login page and potentially secure management protocols. We are targeting a scenario where you need to generate and manage your own certificates, rather than rely on certificates from third-party authorities. The primary goal is to secure communication channels within the hotspot network that are currently unencrypted.

## Implementation Steps:

Here's a step-by-step guide, including CLI and Winbox instructions, before and after configuration states, and the effect each step is intended to have:

**1. Step 1: Generating a Self-Signed Certificate**

   * **Purpose:** We need a certificate to enable TLS/SSL encryption. A self-signed certificate means we're acting as our own Certificate Authority (CA). This is suitable for internal networks and testing, but for production facing networks, a certificate signed by a trusted CA is recommended.
   * **Before Configuration:** No certificates are present. If using Winbox, navigate to `System -> Certificates` and see an empty list or default system certificates. In CLI, running `/certificate print` will show an empty list or very limited entries.

        ```mikrotik
        /certificate print
        Flags: K - key, L - crl, CA - certificate authority, T - trusted;
        Columns: NAME, SUBJECT, FINGERPRINT, VALID-FROM, VALID-TO, TRUSTED
        ```
   * **CLI Configuration:** We use the `certificate generate-self-signed` command to generate a new self-signed certificate.

        ```mikrotik
        /certificate
        add name=hotspot-cert common-name=hotspot.local days-valid=365 key-usage=tls-server
        ```

        * `name=hotspot-cert`: Sets the name of our certificate for easy identification.
        * `common-name=hotspot.local`: The domain name for our certificate. Replace this with your actual domain or a suitable hostname.
        * `days-valid=365`: Sets the validity period of the certificate to one year.
        * `key-usage=tls-server`: Indicates this certificate is intended for server-side TLS. Other common options include `tls-client`, or `digital-signature`.

    * **Winbox Configuration:**
        1. Navigate to `System -> Certificates`.
        2. Click the `+` button (add new certificate).
        3. In the `New Certificate` window:
           - Set `Name`: `hotspot-cert`
           - Select `Generate Self-Signed Certificate`.
           - Set `Common Name`: `hotspot.local`
           - Set `Days Valid`: `365`
           - Check the box next to `key-usage` and add `tls-server` from dropdown.
           - Click `Apply` and then `OK`.

    * **After Configuration:** A new certificate with the specified details will be added to the router. You can view it in the CLI or Winbox interface.

        ```mikrotik
        /certificate print
        Flags: K - key, L - crl, CA - certificate authority, T - trusted;
        Columns: NAME, SUBJECT, FINGERPRINT, VALID-FROM, VALID-TO, TRUSTED
        #   NAME            SUBJECT        FINGERPRINT                      VALID-FROM      VALID-TO        TRUSTED
        0 K hotspot-cert    CN=hotspot.local 13:2E:A4:56:....:12:D7    2023-10-26      2024-10-25      no
        ```

    * **Expected Effect:** We now have a self-signed certificate that can be used by other MikroTik services.

**2. Step 2: Enabling HTTPS for the Hotspot Login Page**

   * **Purpose:** To secure user login pages on the hotspot using TLS/SSL via the generated certificate.
   * **Before Configuration:** The hotspot's login page is likely using HTTP, without encryption.
   * **CLI Configuration:** We modify the hotspot server's configuration to use our certificate:

       ```mikrotik
        /ip hotspot profile
        set [find name=default] https=yes ssl-certificate=hotspot-cert
        ```
        *  `[find name=default]`: Selects the 'default' hotspot profile. If you use different profiles, select the profile you wish to modify.
        * `https=yes`: Enables HTTPS.
        * `ssl-certificate=hotspot-cert`: Sets the previously generated certificate for HTTPS.

    * **Winbox Configuration:**
       1. Navigate to `IP -> Hotspot -> Server Profiles`.
       2. Double-click the profile you wish to modify (usually `default`).
       3. On the `General` Tab, check `HTTPS`.
       4. Select `hotspot-cert` in the `SSL Certificate` dropdown list.
       5. Click `Apply` and then `OK`.

    * **After Configuration:** The hotspot's login page will now be accessible over HTTPS, using the generated certificate.
    * **Expected Effect:** Users accessing the hotspot login page will see a secure connection, albeit one with a self-signed certificate warning in their browser, as browsers will not automatically trust self-signed certificates.

**3. Step 3: Verify Certificate Usage**

    * **Purpose:** To confirm that the certificate is correctly used by the Hotspot service
    * **Before Configuration:**  The Hotspot is configured to use the certificate, but verification is needed
    * **CLI Configuration:** We can check the hotspot configuration to see if it is using the certificate
         ```mikrotik
          /ip hotspot profile print detail
         ```
    * **Winbox Configuration:**
        1. Navigate to `IP -> Hotspot -> Server Profiles`.
        2. Double-click the profile you configured.
        3. Verify the `SSL Certificate` is set to your certificate.
    * **After Configuration:** The output shows that the certificate is linked correctly with the hotspot server profile.

## Complete Configuration Commands:

```mikrotik
# Generate self-signed certificate
/certificate
add name=hotspot-cert common-name=hotspot.local days-valid=365 key-usage=tls-server

# Enable HTTPS for hotspot and set the certificate
/ip hotspot profile
set [find name=default] https=yes ssl-certificate=hotspot-cert

# Example of disabling https if needed
#/ip hotspot profile
#set [find name=default] https=no

# Example to check hotspot profile config
/ip hotspot profile print detail
```

## Common Pitfalls and Solutions:

* **Certificate Not Trusted:** Browsers will display warnings about self-signed certificates.  This is normal but needs user acknowledgement to proceed to the login page. To resolve, acquire a trusted certificate from a CA.
* **Incorrect Common Name:** If the `common-name` doesn't match the URL users are trying to access, the browser might show errors. Ensure the name in the certificate is correct for the URL.
* **Certificate Expired:** The certificate will become invalid after the expiration date. Generate or renew it before expiry.
* **Certificate Not Applied:**  Ensure that the `ssl-certificate` property in the hotspot profile is set to the correct certificate name. Use the `print detail` command for verifying this.
* **Hotspot Not Working:** If HTTPS fails, double-check that the hotspot service itself is working and other factors are not the cause. `log print file=hotspot.log` can be useful here.
* **High CPU/Memory:** Certificate generation or frequent usage of TLS can increase CPU usage on lower-end devices. In rare cases, if you have thousands of concurrent clients, then it could become an issue.  Monitor your system resources ( `/system resource print`) and optimize or upgrade if needed.

## Verification and Testing Steps:

1. **Access Hotspot Login:** Attempt to connect to the hotspot and access the login page using a web browser.
2. **Check HTTPS:** Verify that the address bar shows HTTPS, not HTTP.
3. **Examine the Certificate:** View the certificate details in your browser by clicking on the padlock icon and ensure it displays the `common-name` of your self-signed cert.
4. **CLI verification**
    * Use `certificate print` to verify the certificate is correctly generated, valid and active.
    * Use `/ip hotspot profile print detail` to verify the certificate is linked to the profile.
5. **Ping test**
   * Ping the gateway of the hotspot to make sure the hotspot server is reachable.
6.  **Torch**
   * Use torch on the interface (`/tool torch interface=ether-10`) to see incoming/outgoing traffic and verify if you see TLS traffic.

## Related Features and Considerations:

* **Trusted Certificates:**  For a more secure setup, purchase a certificate from a trusted Certificate Authority (CA). Import the certificate in the certificate store and use it similarly to self-signed ones.
* **Certificate Revocation Lists (CRLs):** You can configure CRLs to revoke certificates in the event of compromise, although this is less common with self-signed certificates and more common with external CA.
* **Secure Management Access:**  Use certificates to secure RouterOS management protocols (Winbox, SSH, API) for added security.
* **Hotspot Customization:** Combine certificate configuration with custom hotspot login pages, terms of service and other customizations.
* **RouterOS API:** Use the MikroTik API to manage certificates programmatically.

## MikroTik REST API Examples:

Here is how you can generate a self-signed certificate, and enable https on the hotspot server profile using the Mikrotik API:

```bash
# Replace with your RouterOS API endpoint, username and password
API_URL="https://<router_ip>/rest"
USER="<api_user>"
PASS="<api_password>"

# Generate self-signed certificate using the /certificate endpoint
curl -k -H "Content-Type: application/json" \
-u "${USER}:${PASS}" \
-X POST \
-d '{
  "command": "/certificate/add",
  "name": "hotspot-cert",
  "common-name": "hotspot.local",
  "days-valid": 365,
  "key-usage": "tls-server"
}' \
"${API_URL}"

#Enable HTTPS for the hotspot
curl -k -H "Content-Type: application/json" \
-u "${USER}:${PASS}" \
-X POST \
-d '{
    "command": "/ip/hotspot/profile/set",
    ".id": "*1",
    "https": "yes",
    "ssl-certificate": "hotspot-cert"
}' \
"${API_URL}"

#Get all certificates on the system, note the /print after the /certificate endpoint
curl -k -H "Content-Type: application/json" \
-u "${USER}:${PASS}" \
-X POST \
-d '{
  "command": "/certificate/print"
}' \
"${API_URL}"

# Get hotspot profile using the /print endpoint
curl -k -H "Content-Type: application/json" \
-u "${USER}:${PASS}" \
-X POST \
-d '{
  "command": "/ip/hotspot/profile/print",
  "detail": true
}' \
"${API_URL}"

```

*   **API Endpoint:** Replace `<router_ip>` with your RouterOS device's IP address.
*   **Authentication:** Replace `<api_user>` and `<api_password>` with your MikroTik API username and password. Ensure an API user is created with sufficient permissions.
*   **JSON Payload:** The `command` key specifies the MikroTik command to execute.  The rest of the payload maps to the MikroTik command parameters.
*   **HTTP Method:** Use `POST` to execute the command on the router.
*   **Error Handling:** Check the HTTP response code. A 200 response usually indicates success. If there is an error, the response body will contain an error message.
*   **Response:** The output will contain the results of the executed command as json objects.

## Security Best Practices

* **Use Strong Private Keys:** Ensure that your private key is strong. This means generating a private key using proper encryption. (This is mostly automated within Mikrotik)
* **Limit Access to Certificates:** Restrict access to the router and its certificates to authorized users and administrators only. Do not store the certificate private key insecurely.
* **Use Trusted CAs for Public Facing Services:** For production use, particularly for services available to the general public, use certificates issued by a well known and trusted certificate authority to ensure maximum browser and system compatibility.
* **Regularly Monitor and Update:** Monitor the status of your certificates for validity periods and update your RouterOS regularly.

## Self Critique and Improvements

* **Complexity:** The self-signed nature simplifies the initial implementation but requires acknowledging browser security warnings.
* **Scalability:** This setup is fine for a small hotspot but might not scale well for very large networks.
* **Automation:**  For larger deployments, you'd need more automation for certificate generation and distribution.  Use the RouterOS API to automate certificate generation, or implement tools such as acme.sh to integrate Let's Encrypt.
* **Clarity:** This guide tries to offer practical configuration with detailed steps. Further improvement can be made by having diagrams and more user friendly instructions.
* **HTTPS only:** Only HTTPS is enabled in this scenario, for full compatibility with older clients HTTP may need to be enabled, this comes with a security risk. It should be considered based on the needs of the network.
* **No CRL:** No CRL is configured for this self-signed certificate as it is mostly for internal use, in a real-world implementation a CRL should be considered for public facing networks.

## Detailed Explanations of Topic

Certificates in MikroTik RouterOS are X.509 certificates that enable TLS/SSL encryption and authentication. They are primarily used for securing communication channels, such as the router's management interfaces (Winbox, SSH, API), VPN services, and captive portal login pages. A certificate consists of a public key (shared with others) and a private key (kept secret). They can be either self-signed (generated by the device) or signed by a trusted Certificate Authority (CA).

## Detailed Explanation of Trade-offs

*   **Self-Signed vs. Trusted Certificates:**
    *   **Self-Signed:**  Easy to generate but not trusted by browsers, which will issue security warnings. Useful for internal networks or testing. No cost associated.
    *   **Trusted:**  Issued by trusted CAs, automatically trusted by browsers, more professional, requires a purchase/payment.
*   **Certificate Validity Period:** Shorter validity periods (e.g., 1 year) require more frequent renewals but are generally more secure. Longer periods are convenient but risk compromise.
*   **TLS Versions and Ciphers:**  Using the correct TLS version and strong ciphers can greatly enhance the security of TLS communication, but may also impact compatibility with older systems.
* **Key Lengths:** Choosing larger key lengths for certificates increases security, but they increase resource consumption for encryption.

## Configuration for Specific RouterOS Versions:

This configuration is compatible with RouterOS 7.11 as well as 6.48 and higher 7.x versions. There are no specific commands or parameters in this configuration that would not be available on these versions. If you are using an older version such as RouterOS v6.x, then it is recommended to upgrade to the latest stable branch for improved security and functionality.

This comprehensive guide covers the intricacies of generating and managing certificates in a MikroTik environment, especially for a hotspot network. Remember, securing your network with proper encryption is crucial for protecting your users and your network infrastructure.

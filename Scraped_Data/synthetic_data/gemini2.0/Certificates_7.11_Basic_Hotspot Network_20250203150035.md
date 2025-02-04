Okay, let's dive deep into certificates on MikroTik RouterOS, focusing on a Hotspot network scenario with a specific subnet and interface. We'll cover all the instructions you provided with detailed explanations, examples, and best practices.

## Scenario Description:

We are configuring certificates on a MikroTik router that is acting as a gateway for a Hotspot network. This router has an interface named `bridge-91` that connects to the local network with the subnet `70.150.29.0/24`. We need to generate and use certificates for various secure services (e.g., HTTPS for the Hotspot login page, API access, etc.). This configuration will be at a basic level.

## Implementation Steps:

### Detailed Explanation of Topic

Before we begin, let's understand the basic concepts of certificates in MikroTik RouterOS. Certificates are digital documents that verify the identity of a server or client. They are essential for secure communication using protocols like HTTPS. In MikroTik, you can create:

-   **Self-signed certificates:** Created by the router itself, useful for testing or internal networks.
-   **Certificates signed by a Certificate Authority (CA):** Obtained from a trusted third party, suitable for production environments.

This document will focus on creating self-signed certificates as the example, because it is a basic configuration.

### Implementation Steps

**1. Step 1: Initial Router Configuration & Interface Verification**

*   **Goal:** Ensure the `bridge-91` interface exists and is properly configured. This is our starting point. We will not create or modify bridge configuration in this document.
*   **Action:** Use Winbox or the CLI to confirm `bridge-91` exists and is active.

    **CLI (before step):**
    ```
    /interface bridge print
    ```

    **Example Output (before step):**
    ```
    Flags: X - disabled, R - running
    0  R name="bridge1" mtu=1500 actual-mtu=1500 l2mtu=1598 arp=enabled
          mac-address=7C:6A:83:22:4B:7F protocol-mode=none priority=0x8000
          auto-mac=yes admin-mac=00:00:00:00:00:00
    1    name="bridge-91" mtu=1500 actual-mtu=1500 l2mtu=1598 arp=enabled
          mac-address=7C:6A:83:22:4B:80 protocol-mode=none priority=0x8000
          auto-mac=yes admin-mac=00:00:00:00:00:00
    ```
    **Winbox GUI:** Navigate to `Bridge > Bridges` to view existing bridges, and confirm `bridge-91` is there.
*   **Explanation:** We start by verifying that our target interface, `bridge-91` is correctly setup, to ensure any configuration after this step can be used by that interface.

**2. Step 2: Generate Self-Signed Certificate**

*   **Goal:** Create a new self-signed certificate.
*   **Action:** Use the following CLI command to generate a new certificate.

    **CLI Command:**
    ```
    /certificate add name=my-router-cert common-name="router.local" subject-alt-name="DNS:router.local,IP:70.150.29.1" days-valid=365 key-usage=tls-server
    ```
    **CLI (after step):**
    ```
    /certificate print
    ```
    **Example Output (after step):**
    ```
     Flags: K - private-key, T - trusted, A - authority
     0   KT  name="my-router-cert" common-name="router.local" subject-alt-name="DNS:router.local,IP:70.150.29.1"
              fingerprint="12:34:56:78:90:AB:CD:EF:12:34:56:78:90:AB:CD:EF:12:34:56:78" key-usage=tls-server,digital-signature
              issuer="my-router-cert" serial-number="0000000000000000" not-before=sep/26/2023 10:00:00 not-after=sep/25/2024 10:00:00
    ```

    **Winbox GUI:**
    * Go to `System > Certificates`
    * Click `Add`, configure the properties and click `Apply`.

    **Parameter Explanation:**

    | Parameter         | Description                                                                                     |
    | :---------------- | :---------------------------------------------------------------------------------------------- |
    | `name`           | A descriptive name for the certificate.                                                         |
    | `common-name`      | The fully qualified domain name or IP address that will be associated with the certificate. |
    | `subject-alt-name` | Alternate names, such as DNS entries or IP addresses, for use with this certificate.          |
    | `days-valid`     | The number of days the certificate will be valid.                                                |
    | `key-usage`       | The specific purposes for which the certificate can be used.                                    |

    **Note:** The common name should correspond to the hostname of your router, or be a valid FQDN if a FQDN is used to address your router. The subject alternate name contains the IP address used by the router to interact with the LAN.
*   **Explanation:**
        - The `name` field is used as an identifier of the certificate
        - The `common-name` is the name that is used to verify if the certificate is valid. It must match the actual domain name used to access the server or service.
        - The `subject-alt-name` allows clients to use other names or IP addresses to verify the certificate, if the client does not support server name identification.
        - The `days-valid` sets the expiration date of the certificate. After that time, the certificate is no longer valid.
        - The `key-usage` specifies how the certificate is going to be used. In this case `tls-server` means the certificate will be used by the server side of a TLS connection.
        - A self-signed certificate does not require a CA, because the issuer is itself, the router.

**3. Step 3: Configure Hotspot to Use Certificate**
*   **Goal:** Configure Hotspot to use the newly created certificate.
*   **Action:** Update the hotspot profile settings to point to `my-router-cert`.
    **CLI Command:**
    ```
    /ip hotspot profile set [find name=default-hotspot] ssl-certificate=my-router-cert
    ```
    **CLI (after step):**
    ```
        /ip hotspot profile print
    ```
    **Example Output (after step):**
    ```
    Flags: * - default
     0  * name="default-hotspot" hotspot-address=10.5.50.0/24 dns-name="" html-directory=hotspot
           http-proxy=0.0.0.0:0 use-radius=no radius-address=0.0.0.0 radius-secret=""
           radius-accounting=no accounting=no mac-cookie-timeout=10m transparent-proxy=no
           add-mac-cookie=no mac-format=XX:XX:XX:XX:XX:XX split-user-domain=no
           login-by=http-chap,http-pap,mac,cookie,http-sh,https ssl-certificate=my-router-cert
           smtp-server=0.0.0.0:0 smtp-starttls=no trial-uptime=0s
           rate-limit="" keepalive-timeout=10m nas-id="" idle-timeout=none
    ```
     **Winbox GUI:**
        *   Go to `IP > Hotspot > Profiles`
        *   Select profile and open it
        *   Select `my-router-cert` in the `Ssl certificate` dropdown
        *   Click `Apply`.

    **Parameter Explanation:**
    | Parameter          | Description                                                               |
    | :----------------- | :------------------------------------------------------------------------ |
    | `ssl-certificate` | Specifies which certificate to use for the Hotspot's HTTPS connections.    |

*   **Explanation:**
     - The `ssl-certificate` parameter configures the hotspot service to use the generated `my-router-cert`.
     - From this point onward, any TLS connection using the hotspot will use the specified certificate.

**4. Step 4: Enable API to Use Certificate (Optional)**
* **Goal:** Configure the API to use the newly created certificate.
* **Action:** Enable and configure the API to use the `my-router-cert` certificate.

    **CLI Command:**
    ```
    /ip api set enabled=yes certificate=my-router-cert
    ```

    **CLI (after step):**
    ```
    /ip api print
    ```

    **Example Output (after step):**
    ```
    enabled: yes
    port: 8729
    certificate: my-router-cert
    allow-from: 0.0.0.0/0
    read-timeout: 10s
    write-timeout: 10s
    legacy-mode: no
    ```

    **Winbox GUI:**
        *  Go to `IP > API`
        * Check the `Enabled` check box.
        * Select the certificate in the `Certificate` dropdown
        * Click `Apply`.

    **Parameter Explanation:**
     | Parameter       | Description                                                                  |
     | :-------------- | :--------------------------------------------------------------------------- |
     | `enabled`       | Enables or disables the API server.                                        |
     | `certificate`   | Specifies the certificate used by the API server for HTTPS connections.     |

*  **Explanation:**
     - The `enabled` parameter activates the API endpoint.
     - The `certificate` parameters sets the certificate used to authenticate the API communication.
     - From this point onward, any TLS connection using the API will use the specified certificate.

## Complete Configuration Commands:

```
/certificate add name=my-router-cert common-name="router.local" subject-alt-name="DNS:router.local,IP:70.150.29.1" days-valid=365 key-usage=tls-server
/ip hotspot profile set [find name=default-hotspot] ssl-certificate=my-router-cert
/ip api set enabled=yes certificate=my-router-cert
```

## Common Pitfalls and Solutions:

*   **Problem:** Clients report invalid certificate warnings.
    *   **Solution:** This is expected with self-signed certificates. Install the certificate as a trusted certificate on the client device. Alternatively, use a certificate signed by a trusted CA.
*   **Problem:**  Certificate does not work in Hotspot Login page
    *   **Solution:** Verify the `common-name` is the same one that is used by the user to access the login page of the Hotspot. If a FQDN is used, the `common-name` must be the FQDN that is used. Verify the `subject-alt-name` contains the IP Address used by the router to interact with the LAN.
*   **Problem:** High CPU usage after enabling HTTPS on the Hotspot.
    *   **Solution:** The generation of keys and encrypted data has a high CPU cost. The more users interact with the service, the more resources are used. Monitor router resource utilization.
*   **Problem:**  Certificate expired.
    *   **Solution:** Generate a new certificate using the steps provided in this document, and ensure that `days-valid` is set to a higher value.
*  **Problem:** API not accessible with HTTPS
    *  **Solution:** Ensure API is enabled, and the certificate is configured correctly.
*  **Security Issue:** Self-signed certificates are inherently less secure than those from a CA.
    *   **Solution:** Always use a CA-signed certificate in a production environment if possible. Self-signed certificates must be explicitly trusted by all clients, and can be a security concern.
*   **Security Issue:** Certificates without Subject Alternative Names (SANs) will cause problems for some modern browsers and clients.
    * **Solution:** Ensure your certificate has a correct subject alt name.

## Verification and Testing Steps:

1.  **Hotspot HTTPS Verification:**
    *   Connect to the Hotspot network via WiFi.
    *   Open a web browser and try to access a non-HTTPS website.
    *   The browser will be redirected to the Hotspot login page. The URL should be `https://<your-router-ip>/login` (where `<your-router-ip>` is `70.150.29.1`). Verify that the connection is encrypted using HTTPS and the certificate is used. Check the certificate details to ensure they match the certificate you generated (`my-router-cert`). If the browser shows a certificate warning, that means the certificate is valid but is not trusted by the browser. This is expected when using self signed certificates.
2. **API Verification:**
    *   Use a tool like `curl` or `Postman` to access the API:
        ```bash
        curl -k -u "api_user:api_password" https://70.150.29.1/
        ```
        * `-k` bypasses certificate verification if the certificate is self-signed.
        *  `-u "api_user:api_password"` Provides the username and password used to connect to the api.
        * The API response should be returned.
3. **Certificate Inspection:**
    *   Use the CLI to check certificate details:

        ```
        /certificate print detail
        ```

        Verify all attributes of the certificate. Pay attention to the `not-before` and `not-after` to verify if the certificate is valid, the common-name, subject-alt-name and issuer.

## Related Features and Considerations:

*   **Certificate Revocation Lists (CRLs):** For advanced scenarios, you can manage CRLs to invalidate compromised certificates.
*   **Let's Encrypt Integration:** You can automate the generation of free, trusted certificates using Let's Encrypt.
*   **User Manager Integration:** Combine this certificate setup with user management features.
*   **Custom Certificate Storage:** You can store the certificate in a dedicated storage if required.
*   **RouterOS Scripting:** Use RouterOS scripting to automate certificate renewal and management.
*   **Impact:** The use of HTTPS for the hotspot service improves the security of the connection between the client device and the hotspot gateway.

## MikroTik REST API Examples (if applicable):

While the direct API calls for certificate *generation* aren't available, you can *read* and *modify* certificate settings. The API supports only the settings from the `/certificate` menu.

Here's an example of how to retrieve certificate information via API:

**API Endpoint:** `/certificate`

**Request Method:** `GET`

**Example (using `curl`):**

```bash
curl -k -u "api_user:api_password" https://70.150.29.1/rest/certificate
```

**Expected Response (JSON):**

```json
[
  {
    ".id": "*0",
    "name": "my-router-cert",
    "common-name": "router.local",
    "subject-alt-name": "DNS:router.local,IP:70.150.29.1",
    "key-usage": "tls-server,digital-signature",
    "fingerprint": "12:34:56:78:90:AB:CD:EF:12:34:56:78:90:AB:CD:EF:12:34:56:78",
    "issuer": "my-router-cert",
    "serial-number": "0000000000000000",
    "not-before": "sep/26/2023 10:00:00",
    "not-after": "sep/25/2024 10:00:00",
     "private-key": "true",
    "trusted": "true",
    "authority": "false"
  }
]
```
**Parameter Description:**
- `name`: The name of the certificate.
- `common-name`: The fully qualified domain name or IP address associated with the certificate.
- `subject-alt-name`: Alternate names for use with the certificate.
- `key-usage`: Specific purposes of the certificate.
- `fingerprint`: The fingerprint of the certificate.
- `issuer`: The entity that issued the certificate (in this case, itself for a self-signed cert).
- `serial-number`: The serial number of the certificate.
- `not-before`: The date and time when the certificate becomes valid.
- `not-after`: The date and time when the certificate becomes invalid.
- `private-key`: True if the private key exists
- `trusted`: True if the certificate is trusted
- `authority`: True if it is a CA certificate

**Handling API Errors:**

*   API errors will typically return a status code (e.g., 401 for unauthorized, 404 for not found) with a JSON body detailing the problem.
*   Always check the status code for errors.

**API for setting certificate for hotspot (Example)**

**API Endpoint:** `/ip/hotspot/profile/`

**Request Method:** `PUT`

**Example (using `curl`):**
```
curl -k -u "api_user:api_password" -H "Content-Type: application/json" -X PUT -d '{
    "ssl-certificate":"my-router-cert"
}' https://70.150.29.1/rest/ip/hotspot/profile/*0
```

**Expected Response (JSON):**
```
{
    "message": "updated"
}
```

**Parameter Description:**
-   `ssl-certificate`: The name of the certificate to use in the hotspot profile.
-   `*0`: The ID of the profile to modify. This ID can be read from the previous API request.
- Error Handling: If there are errors, they will be returned in a JSON format, and can be handled as part of the error handling logic.

## Security Best Practices:

*   **Strong Private Key Passphrases:** Protect private keys with strong passphrases.
*   **Regular Certificate Renewal:** Renew certificates before expiration to avoid service disruptions.
*   **Use CA-Signed Certificates:** Use trusted CAs instead of self-signed certificates in production.
*   **Limit API Access:** Configure the `allow-from` parameter on `/ip/api` to restrict API access to trusted networks.
*   **Secure API Credentials:** Ensure that the credentials used to access the API are stored securely.

## Self Critique and Improvements:

This configuration is basic and suitable for small Hotspot networks, internal testing, or laboratory usage.  However, it lacks advanced features for security and real-world applications, such as:

*   **Automated Renewal:** We're not automating certificate renewal. This can be done through scripting or by using the Let's Encrypt integration.
*   **Certificate Revocation:** No CRL management which is critical for production.
*   **Advanced Key Management:** There is no implementation of hardware security modules or PKCS#11 for enhanced key management.
*   **Error Handling:** API Error handling could be improved.
*   **Resource Usage:** This configuration lacks monitoring for high CPU usage during encryption.
*   **Limited Security:** Self-signed certificates pose a security risk.
*   **Lack of automation:** The steps to generate the certificate are done manually, which can be improved to use a script or other automated process.

**Potential Improvements:**
    *   Automate the certificate renewal using a script.
    *   Use the letsencrypt feature to generate certificates automatically.
    *   Implement monitoring of CPU usage.
    *   Implement certificate revocation process.

## Detailed Explanation of Trade-offs:

*   **Self-Signed vs. CA-Signed Certificates:**
    *   **Self-signed:** Easier to generate but less secure, not trusted by default, and require manual installation on clients.
    *   **CA-signed:** More secure, trusted by most browsers and devices, but require a purchase and more complex configuration. Tradeoff is security versus ease of setup.
*   **Certificate Key Length:**  Longer key lengths are more secure but require more processing power. A 2048-bit RSA key is a good balance.
*   **Certificate Validity Period:**  Shorter validity periods improve security by reducing the window of exploitation if the key is compromised, but increase the frequency of certificate renewal.
*   **API Security:** Open API access to the router is useful for administration and automation but can be a security risk, which is the tradeoff between security and convenience.

## Configuration for Specific RouterOS Versions:

This configuration is compatible with RouterOS versions 7.x and 6.48 as requested. If using a very old version (6.47 or older), ensure that the `/certificate` menu is fully implemented, and that the `subject-alt-name` and `key-usage` parameters are supported.

Let me know if you have other questions or specific scenarios you'd like to explore!

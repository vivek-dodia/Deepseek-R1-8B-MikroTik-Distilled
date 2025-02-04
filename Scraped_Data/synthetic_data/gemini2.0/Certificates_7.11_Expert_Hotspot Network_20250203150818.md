Okay, let's dive deep into certificates on MikroTik RouterOS 7.11 within the context of a Hotspot Network scenario. We'll focus on a practical and robust implementation for the given subnet and interface.

## Scenario Description:

This scenario involves setting up a Hotspot network on a MikroTik router using the interface `ether-99`, assigned to the subnet `21.88.186.0/24`. We'll configure and utilize certificates for secure authentication, particularly focusing on enabling HTTPS for the Hotspot login page and potentially other services. This is crucial for protecting user credentials and ensuring a secure browsing experience.

## Implementation Steps:

Here's a step-by-step guide, explaining each action with CLI examples and effects:

### 1. Generate a Self-Signed Certificate:

*   **Why:** A self-signed certificate is needed as a base certificate for the router’s web-server and other services that require TLS/SSL. This avoids using an external CA for testing and internal setups.
*   **Before:** No certificate exists. You can check this by going to `/certificate print`.
*   **Command:**
    ```mikrotik
    /certificate add name=hotspot-cert common-name="21.88.186.1" key-usage=digital-signature,key-encipherment,tls-server validity=3650 days=3650
    ```
*   **Explanation:**
    *   `add`: Creates a new certificate.
    *   `name=hotspot-cert`: Sets the name of the certificate to `hotspot-cert`.
    *   `common-name="21.88.186.1"`: Sets the common name, typically the IP address, hostname, or domain name of the server, in this case, we are using the main IP address.
    *   `key-usage=digital-signature,key-encipherment,tls-server`: Specifies the intended usage of the certificate for server authentication.
    *   `validity=3650 days`: Sets the certificate validity for 10 years.
*   **After:** A self-signed certificate named "hotspot-cert" is added to the certificate store, this will have a `status=pending` that will switch to `status=valid` once it is issued by its own private CA.
*   **Winbox Equivalent:**
    * Navigate to `System > Certificates`.
    * Click the "+" button.
    * Fill out the parameters Name and Common Name, enable `key-encipherment` and `tls-server` key-usage.
    * Click Apply then Sign.

### 2. Configure the Hotspot Server to Use the Certificate:

*   **Why:** This step links the created certificate to your hotspot profile.
*   **Before:** The Hotspot uses the default non-TLS setup. You can check the current hotspot profile configuration under `/ip hotspot profile print`.
*   **Command:**
    ```mikrotik
    /ip hotspot profile set [find name=hsprof1] ssl-certificate=hotspot-cert
    ```
*   **Explanation:**
    *   `set`: Modifies an existing setting.
    *   `[find name=hsprof1]`: Find the hotspot profile name, usually it will be 'hsprof1', be sure to confirm the profile name.
    *   `ssl-certificate=hotspot-cert`: Specifies the certificate to use for TLS/SSL connections.
*   **After:** The hotspot service now uses the newly generated certificate and will use TLS for secure login. When users browse to the hotspot page, the connection should be encrypted.
*   **Winbox Equivalent:**
    * Navigate to `IP > Hotspot > Hotspot Profiles`.
    * Select the profile you are using for your Hotspot.
    * In the "General" tab, Select your `ssl-certificate`

### 3. (Optional) Import a CA-Signed Certificate:
*   **Why:** For production environments, a CA-signed certificate provides greater trust. For public hotspot it is recommended to get one from a trusted CA.
*   **Before:** Assuming no CA-signed certificate is present, check by `/certificate print`, or in the Winbox `System>Certificates`.
*   **Steps (CLI):**
    1.  Obtain your CA-signed certificate (.crt or .pem) and the corresponding private key (.key or .pem) and upload them to the router. You can achieve this using tools like scp or sftp. The file name and paths below are placeholders.
    2. Import the certificate with:

        ```mikrotik
        /certificate import file-name=my_domain_certificate.crt password=""
        /certificate import file-name=my_domain_key.key password="<private_key_password_if_any>"
        ```

        **Explanation**:

        -  `import`: Imports a certificate.
        -  `file-name`: Sets the name of the file that has to be imported from `/files`
        -  `password`: If the file is encrypted, provide the password here.

    3. Ensure the CA Root certificate is also imported if it's not present.
        ```mikrotik
        /certificate import file-name=my_domain_root_certificate.crt password=""
        ```
* **After**:  The CA-signed certificate should be available, and the status should change from `pending` to `valid`. You can view this by running `/certificate print` or through winbox.
* **Winbox Equivalent:**
    * Navigate to `System > Certificates`.
    * Click the "Import" button.
    * Browse and select the `.crt` or `.pem` certificate file.
    * Click "Import".
    * Repeat these steps to import the private key `key`.
    * Repeat these steps to import the root certificate, if required.

### 4. Configure Hotspot to use the CA-Signed Certificate (if imported):
* **Why**: Use your CA-Signed certificate for production environments and avoid potential browser security warnings.
* **Before**: Hotspot is using the self-signed certificate created earlier or default settings.
* **Command (replacing `my_domain_certificate` with the actual certificate name)**:
```mikrotik
/ip hotspot profile set [find name=hsprof1] ssl-certificate=my_domain_certificate
```

* **After**: Hotspot now uses the CA-Signed Certificate, ensuring a secure and trusted experience for users.
* **Winbox Equivalent:**
    * Navigate to `IP > Hotspot > Hotspot Profiles`.
    * Select the profile you are using for your Hotspot.
    * In the "General" tab, Select the desired `ssl-certificate`.

## Complete Configuration Commands:

Here's the complete set of MikroTik CLI commands to implement the above configuration:

```mikrotik
# Step 1: Create a Self Signed Certificate
/certificate add name=hotspot-cert common-name="21.88.186.1" key-usage=digital-signature,key-encipherment,tls-server validity=3650 days=3650

# Step 2: Configure Hotspot to use the Certificate
/ip hotspot profile set [find name=hsprof1] ssl-certificate=hotspot-cert

# (Optional) Import a CA-Signed Certificate
# /certificate import file-name=my_domain_certificate.crt password=""
# /certificate import file-name=my_domain_key.key password="<private_key_password_if_any>"
# /certificate import file-name=my_domain_root_certificate.crt password=""

# Step 3: Configure Hotspot to use the CA-Signed Certificate (if imported)
# /ip hotspot profile set [find name=hsprof1] ssl-certificate=my_domain_certificate

# Note: Always adapt the certificate name and hotpost profile names as needed.
```

## Common Pitfalls and Solutions:

1.  **Invalid Certificate:**
    *   **Problem:** Incorrect file format or corrupted files during import.
    *   **Solution:** Double check the file format, ensure correct CA chain and key are present. Re-upload the file using a secure connection (e.g., sftp or winbox). Check the certificate status using `/certificate print`.

2.  **Certificate Status:**
    *   **Problem:** Certificate status is not "valid".
    *   **Solution:** Check the `status` column using `/certificate print`. A common cause is a missing intermediate certificate. Ensure all certificates in the chain are imported. Also make sure the current time and date is correct using `/system clock`.

3.  **Browser Certificate Warnings:**
    *   **Problem:** Browser shows "not secure" warnings with self-signed certificates.
    *   **Solution:**  This is expected with self-signed certificates. For production, use a CA-signed certificate. You can also manually install the self-signed cert in your browser, however, this is not recommended for Hotspot environments.

4. **Missing or Incorrect Key Usage**
    * **Problem**: Certificate is created without the required key usage attributes.
    * **Solution**: Make sure to include key-usage attributes such as `key-usage=digital-signature,key-encipherment,tls-server` when generating or importing the certificate.

5. **Incorrect Profile**
   * **Problem**: The certificate isn't being used on the correct hotspot profile.
   * **Solution**: Check in `/ip hotspot profile print` to make sure the right profile is selected.

6.  **Resource Issues:**
    *   **Problem:** High CPU or memory usage due to many encrypted connections.
    *   **Solution:**  Monitor CPU and memory usage using `/system resource print`. Ensure adequate resources, especially if the router is managing high traffic or a lot of hotspot users. Consider offloading more intensive tasks to dedicated hardware if needed.

7.  **Expired Certificates:**
    *   **Problem:** Certificate validity has expired.
    *   **Solution:**  Check the validity period using `/certificate print`. Re-generate or renew the certificate before it expires. Remember to import the new certificate and set the hotspot to use the new cert.

## Verification and Testing Steps:

1.  **Check Certificate Status:**
    ```mikrotik
    /certificate print
    ```
    *   Ensure the `status` for the relevant certificate is `valid`.
2.  **Access the Hotspot Login Page:**
    *   Connect a device to the Hotspot.
    *   Open a web browser and try to access any non-HTTPS website. You should be redirected to the Hotspot login page over HTTPS.
    *   Verify that the browser shows a secure (lock) icon in the address bar (if using a trusted certificate) or acknowledge that you trust the self-signed certificate.
3. **Inspect the Webserver Certificate using `openssl`**:

    Connect via openssl s_client to your router's webserver port (`80 or 443`). Note: you will need to have the certificate installed on your router first.

    ```bash
    openssl s_client -connect <Router IP>:443
    ```

    You can then inspect the certificate information in the output, this will tell you if your router is serving the correct certificate.
4. **RouterOS logs**:

   Check the system logs using:
   ```mikrotik
   /log print
   ```
    Look for warnings or errors regarding the certificate or the hotspot.
5. **Debug level logging**:
   Enable debug logs for the `hotspot` topic.
   ```mikrotik
   /system logging add topics=hotspot action=memory
   /system logging print
   ```
   Then check your memory logs using `/log print memory`

## Related Features and Considerations:

1.  **Multiple Certificates:** MikroTik supports multiple certificates which are used for different services. You could have one for Hotspot, one for WebFig, one for IPSec VPN etc.
2.  **Let's Encrypt Integration:** For production setups, leverage MikroTik's built-in Let's Encrypt functionality to automatically obtain and renew free certificates.
3.  **Certificate Revocation Lists (CRLs):**  For enterprise setups, implement CRLs to manage compromised certificates.
4.  **HTTPS for WebFig/Winbox:** Extend this concept to secure the router's management interface (WebFig/Winbox) by configuring the appropriate certificate in `/ip service`.
5.  **API Access with Certificates:** Certificates can be used to authenticate access to the MikroTik REST API.
6.  **RADIUS Authentication:** When integrating with RADIUS, you can utilize certificates for the secure TLS tunnel and enhance security.
7.  **Traffic Control (QoS):**  Ensure that the encryption process is not overloading your router using `/queue simple` or `/queue tree`.

## MikroTik REST API Examples:

The MikroTik API does not directly manipulate raw certificate files, instead, the certificates must be imported using the cli or winbox. We can still inspect existing certificates via the API:

```bash
# Example GET request to fetch certificates
curl -k -u admin:<your_admin_password> https://<your_router_ip>/rest/certificate
```

**Response**

```json
[
    {
        "id": "*1",
        "name": "hotspot-cert",
        "common-name": "21.88.186.1",
        "key-usage": "digital-signature, key-encipherment, tls-server",
        "validity": "3650 days",
        "status": "valid",
        "subject": "CN=21.88.186.1",
        "issuer": "CN=21.88.186.1",
        "serial-number": "xxxxxxxxxxxxx",
        "fingerprint": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
         ... (other params)
    }
  , {
      "id": "*2",
      "name": "my_domain_certificate",
      "common-name": "example.com",
      "key-usage": "digital-signature, key-encipherment, tls-server",
      "validity": "365 days",
       "status": "valid",
       ... (other params)
    }
]
```
**Example of reading certificate details**

```bash
curl -k -u admin:<your_admin_password> https://<your_router_ip>/rest/certificate/*1
```
**Response**

```json
{
    "id": "*1",
        "name": "hotspot-cert",
        "common-name": "21.88.186.1",
        "key-usage": "digital-signature, key-encipherment, tls-server",
        "validity": "3650 days",
        "status": "valid",
        "subject": "CN=21.88.186.1",
        "issuer": "CN=21.88.186.1",
        "serial-number": "xxxxxxxxxxxxx",
        "fingerprint": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
         ... (other params)
}
```
**Example of reading all certificates**
```bash
curl -k -u admin:<your_admin_password> https://<your_router_ip>/rest/certificate
```
**Response**
```json
[
    {
        "id": "*1",
        "name": "hotspot-cert",
        "common-name": "21.88.186.1",
        "key-usage": "digital-signature, key-encipherment, tls-server",
        "validity": "3650 days",
        "status": "valid",
        "subject": "CN=21.88.186.1",
        "issuer": "CN=21.88.186.1",
        "serial-number": "xxxxxxxxxxxxx",
        "fingerprint": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
         ... (other params)
    }
  , {
      "id": "*2",
      "name": "my_domain_certificate",
      "common-name": "example.com",
      "key-usage": "digital-signature, key-encipherment, tls-server",
      "validity": "365 days",
       "status": "valid",
       ... (other params)
    }
]
```
**Explanation:**

*   `-k`:  Allows insecure connections (self-signed certificate). Remove for production.
*   `-u admin:<your_admin_password>`: Provides the username and password for authentication.
*   `https://<your_router_ip>/rest/certificate`: The API endpoint for certificates.
*  `id`: id of the entry we want to read details of. If missing will list all entries.

**Error Handling:**

*   A failed authentication will result in a `401 Unauthorized` error.
*   If the resource is not found it will return `404 Not Found`.
*   If there is an error, the response body will include a JSON payload with a `message` field detailing the error.

## Security Best Practices:

1.  **Use CA-Signed Certificates:** Always use CA-signed certificates for public services to avoid browser warnings and ensure trust.
2.  **Secure Key Management:** Ensure your private keys are stored securely, ideally on the router, and never expose or share them.
3.  **Regular Certificate Renewal:** Keep track of the certificate's expiration date and renew it well in advance. Automated tools like Let's Encrypt greatly simplify this process.
4.  **Strong Passwords:** Use strong passwords for the router's user accounts and when importing certificates, if you use password protected keys.
5.  **Restricted Access:** Limit access to the router using firewall rules to only allow access from trusted networks, especially for remote management.
6.  **Regular RouterOS Updates:** Keep your RouterOS version up to date to patch any security vulnerabilities.
7.  **Disable unused services:** Make sure to disable any unused services.
8.  **Monitor Logs:** Frequently monitor your system and service logs for any security breaches, or malicious activities.

## Self Critique and Improvements:

This configuration provides a solid foundation for securing a Hotspot network with certificates. However, there are areas for further improvement:

*   **Automation:** The manual import/creation of certificates can be automated using scripts and API calls.
*   **Let's Encrypt:** Integrating Let's Encrypt for automated certificate renewal would significantly reduce manual administration overhead.
*   **More Complex Configurations**: This configuration is a basic setup and doesn't go into depth on features like RADIUS or other aspects of more complex hotspot implementations.
*  **Detailed Troubleshooting:** The troubleshooting sections could be improved further to include specific debug commands or advanced monitoring.

## Detailed Explanations of Topic

**Certificates:**

A digital certificate is an electronic "passport" that allows users to verify the identity of online resources, such as websites and applications. They act as a way to encrypt data that is sent over the network, which makes it harder for third-parties to intercept and modify the information. Certificates play a crucial role in secure internet communications by encrypting and securing data transmitted between clients and servers. These digital documents are critical for establishing trust and privacy online. They are used in TLS/SSL protocols, which provide an encrypted communication channel for web browsing, emails, VPNs and various other online services. Certificates are issued by Certificate Authorities (CAs), which are trusted third-party organizations.

**Key Components of a Certificate:**

1.  **Subject**:  The entity to whom the certificate is issued, for example a router, a domain, or a user.
2.  **Public Key**: Used to encrypt data that can only be decrypted with the corresponding private key.
3.  **Issuer**: The entity (CA) that issued the certificate.
4.  **Validity Period**: The timeframe in which the certificate is considered valid.
5.  **Signature**: A digital signature from the CA verifying the certificate’s integrity and authenticity.
6.  **Serial Number**: A unique number assigned by the CA to differentiate the certificate.
7.  **Key Usage**: Specifies the purpose of the certificate, such as for digital signatures, key encipherment, or server authentication.
8.  **Common Name:** The most important parameter of the certificate, usually the domain or IP address associated with the certificate.

**Types of Certificates:**

1.  **Self-Signed Certificates:** Issued by the same entity whose identity it verifies. Useful for testing or internal networks. Not recommended for public-facing services due to lack of trust.
2.  **CA-Signed Certificates:** Issued by trusted Certificate Authorities (CAs). Browsers and other clients already trust CAs.  Recommended for websites and other public services.

## Detailed Explanation of Trade-offs

**Self-Signed vs. CA-Signed Certificates:**

*   **Self-Signed Certificates:**
    *   **Advantages:** Easy to generate and free.
    *   **Disadvantages:** Not trusted by browsers, require manual exception handling by end users, not suitable for public-facing services and can give a false sense of security.
    *   **Trade-off:** Quick setup for testing and internal use but lack of trust is a security risk.

*   **CA-Signed Certificates:**
    *   **Advantages:** Trusted by browsers, enhances security, essential for public-facing services.
    *   **Disadvantages:** Requires obtaining and renewing from a CA, costs money, can require more complex validation steps.
    *   **Trade-off:** Provides trust and security for public services at the expense of time and financial cost.

**Certificate Validity Period:**

*   **Long Validity:**
    *   **Advantages:** Less frequent renewal, easier administration.
    *   **Disadvantages:**  Higher risk if key is compromised, not best practice for security.
    *   **Trade-off:** Easier management but higher risk.
*   **Short Validity:**
    *   **Advantages:** Reduced risk from compromised keys, encourages best practice.
    *   **Disadvantages:** Requires more frequent renewal.
    *   **Trade-off:** More secure but more work.

**Key Usage Parameters:**

*   **Digital Signature:** Used to verify the origin and integrity of data.
*   **Key Encipherment:** Used to encrypt data for secure transmission.
*   **TLS Server:** Used to authenticate a server in TLS connections.
*   **TLS Client**: Used to authenticate the client in TLS connections.

**Trade-off:** Selecting the right key usage is important for proper security and functionality. Ensure that you select them according to your specific needs.

**MikroTik Certificate Management:**

MikroTik has a simple certificate management system, and it offers support for:

*   Generating self-signed certificates.
*   Importing existing certificates.
*   Configuring multiple certs per service.
*   Integration with Let's Encrypt for automated certificate management.
*   Certificate Revocation List management (CRL).

**Trade-off:** MikroTik's approach simplifies certificate management, but lacks some of the features of more complex systems. The main trade-off is ease of management vs more complex fine-grained control.

## Configuration for Specific RouterOS Versions:
This configuration is designed for RouterOS 7.11, and is fully compatible with the 7.x and 6.48 RouterOS versions. Most commands and parameters are supported, making the transition across these versions seamless. If using a different version, verify the specific command parameters in the RouterOS documentation as minor adjustments may be required, especially for very old versions of ROS.

This detailed documentation should equip you with a thorough understanding of how to use certificates within your MikroTik Hotspot network. Let me know if you have any more questions or would like to explore additional aspects of this setup.

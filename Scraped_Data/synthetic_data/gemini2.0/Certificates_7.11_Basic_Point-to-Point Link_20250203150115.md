Okay, let's dive deep into configuring certificates on MikroTik RouterOS for a point-to-point link scenario, specifically focusing on a basic configuration for RouterOS 7.11 (also covering 6.48 and 7.x) with interface `wlan-41` and subnet `220.120.159.0/24`.

## Scenario Description:

This configuration addresses the need to secure communication over a point-to-point wireless link (or any link, but `wlan-41` is the interface) by using digital certificates for authentication and encryption. This scenario is relevant for small to medium-sized businesses or any network where a secure connection between two points is essential.  This configuration would be a first step towards implementing secure protocols like HTTPS, IPSec and VPNs like SSTP and WireGuard, but we are focusing solely on certificate management in this document.  The actual implementation of these protocols is outside the scope of this document.

## Implementation Steps:

This setup involves three primary phases: generating a Certificate Authority (CA) certificate, generating a server certificate, and verifying and using them. While we could use self-signed certificates, which are insecure in most cases, I will be showing the generation of a basic root CA and a basic server certificate, which is more common.

### Step 1: Generating a Certificate Authority (CA) Certificate
This step creates the root CA certificate that will be used to sign server certificates.

*   **Why is this needed?** A CA certificate acts as the root of trust. It validates the authenticity of other certificates.
*   **Before Configuration:** You should have a basic network configuration and access to the RouterOS terminal (via SSH, WebFig, or Winbox).
*   **CLI Command:**

    ```mikrotik
    /certificate add name=myCA common-name="My Root CA" key-usage=key-cert-sign,crl-sign,digital-signature subject-alt-name=DNS:myca.local,IP:192.168.88.1  days-valid=3650
    ```
    *   `/certificate add`:  This command adds a new certificate.
    *   `name=myCA`: Assigns a name to the certificate.
    *   `common-name="My Root CA"`: Sets the common name.
    *   `key-usage=key-cert-sign,crl-sign,digital-signature`: Specifies the CA role (sign other certs).
    *    `subject-alt-name=DNS:myca.local,IP:192.168.88.1`: Alternative subject names (for verification of the cert's identity)
    *   `days-valid=3650`: Sets certificate validity to 10 years (3650 days).  Note that longer validity times are more convenient but increase the risk if a compromise occurs.  I would recommend a shorter time, such as 1 or 2 years for most cases.
*  **Winbox GUI:**  In Winbox, you can do the following steps:
    * Go to *System* -> *Certificates*.
    * Click the "+" button to add a new certificate.
    * Fill in the "Name" field (myCA), the "Common Name" field (My Root CA), the "Days Valid" field (3650) and the "Key Usage" field (key-cert-sign,crl-sign,digital-signature) and finally, the "Subject Alt Name" field with both the DNS and IP (DNS:myca.local,IP:192.168.88.1)
    * Click "Apply" and then "Sign"
*   **After Configuration:** A CA certificate named `myCA` will be created, but it is not signed.  It has to be signed by itself, effectively making it the root of trust.
*  **CLI Command (Sign the CA Certificate):**
    ```mikrotik
    /certificate sign myCA
    ```
* **Winbox GUI**: Select the newly created certificate in the *System* -> *Certificates* panel and click on "Sign".

### Step 2: Generating a Server Certificate
This step creates a server certificate which is signed by the CA to enable secure connections, using the `wlan-41` interface.

*   **Why is this needed?** The server certificate is used to authenticate the server (router) itself.  In order to trust the server, we need to ensure it has been signed by a trusted authority.
*   **Before Configuration:** You should have successfully completed the CA certificate creation.
*   **CLI Command:**
    ```mikrotik
    /certificate add name=server-wlan41 common-name="wlan41.mycompany.local" key-usage=tls-server subject-alt-name=DNS:wlan41.mycompany.local,IP:220.120.159.1 days-valid=1825
    ```
     *   `/certificate add`:  This command adds a new certificate.
    *   `name=server-wlan41`: Assigns a name to the server certificate.
    *   `common-name="wlan41.mycompany.local"`: Sets the common name of the server.
     *  `key-usage=tls-server`:  Specifies the server role of the certificate.
    *   `subject-alt-name=DNS:wlan41.mycompany.local,IP:220.120.159.1`: Alternative subject names (for verification).  Note that the IP address should be an IP used for the specific interface.
    *   `days-valid=1825`: Sets certificate validity to 5 years (1825 days).
*  **Winbox GUI**: In Winbox, you can do the following steps:
    * Go to *System* -> *Certificates*.
    * Click the "+" button to add a new certificate.
    * Fill in the "Name" field (server-wlan41), the "Common Name" field (wlan41.mycompany.local), the "Days Valid" field (1825), the "Key Usage" field (tls-server) and the "Subject Alt Name" field (DNS:wlan41.mycompany.local,IP:220.120.159.1)
    * Click "Apply"

*   **After Configuration:** A server certificate is generated, but it needs to be signed by the CA.
*  **CLI Command (Sign the server certificate using the CA):**
    ```mikrotik
    /certificate sign server-wlan41 ca=myCA
    ```
     * `sign server-wlan41`: sign the certificate `server-wlan41`.
     * `ca=myCA`: the CA certificate to use for signing, namely, `myCA`.
* **Winbox GUI**: Select the newly created certificate in the *System* -> *Certificates* panel and click on "Sign".  In the "Signing Certificate" dialog select `myCA` and click on "Sign".

### Step 3: Exporting Certificates (Optional)
This step shows how to export the CA certificate for use in other devices.  This step is *not* required on the router that contains the server certificate.

*   **Why is this needed?** If you plan on connecting to the router, the CA needs to be trusted by the client, by importing the CA cert onto the client.
*   **Before Configuration:** You must have successfully completed step 1.
*   **CLI Command:**
    ```mikrotik
    /certificate export-certificate myCA export-passphrase="" file-name=myCA.crt
    ```
        *   `/certificate export-certificate myCA`: Export the `myCA` certificate.
        *  `export-passphrase=""`: The passphrase for exporting, this is optional.
        *  `file-name=myCA.crt`: The output file name (available via *Files* menu in Winbox or via `/file print` in the CLI).
* **Winbox GUI:** You can do the following steps:
    * Go to *System* -> *Certificates*.
    * Select the myCA certificate.
    * Click on "Export".
    * Leave the passphrase empty and click on "Export".
    * Go to *Files*.  The new file `myCA.crt` can be downloaded from here.

*   **After Configuration:** A `myCA.crt` file (which can be downloaded from the files menu in Winbox) that contains the root CA certificate is created.
* **Important Note:** Keep the CA certificate secure as a compromised CA can be used to create rogue server certificates, undermining the entire chain of trust. The private key of the CA is stored securely on the device and is not exported. The `export-passphrase` parameter is used when the certificate is stored using PKCS#12 format. The exported file is a simple X.509 (.crt) file.

## Complete Configuration Commands:

```mikrotik
# Step 1: Generate CA Certificate
/certificate add name=myCA common-name="My Root CA" key-usage=key-cert-sign,crl-sign,digital-signature subject-alt-name=DNS:myca.local,IP:192.168.88.1 days-valid=3650
/certificate sign myCA

# Step 2: Generate Server Certificate
/certificate add name=server-wlan41 common-name="wlan41.mycompany.local" key-usage=tls-server subject-alt-name=DNS:wlan41.mycompany.local,IP:220.120.159.1 days-valid=1825
/certificate sign server-wlan41 ca=myCA

# Step 3 (Optional): Export CA Certificate
/certificate export-certificate myCA export-passphrase="" file-name=myCA.crt
```

## Common Pitfalls and Solutions:

*   **Problem:** Certificate fails to sign.
    *   **Solution:** Double-check that the certificate signing CA is correct, and the CA has been correctly signed first. Verify that the date and time are correct on the router, as validity windows of certificates may be time sensitive.
*   **Problem:** Incorrect `key-usage` parameter.
    *   **Solution:** Ensure the correct role, e.g., `key-cert-sign` for CAs, and `tls-server` for server certs.
*   **Problem:** Mismatched common name or subject-alt-name.
    *   **Solution:** Ensure common name and subject-alt-name match the hostname or IP address.
*   **Problem:** Clients cannot verify the server certificate.
    *   **Solution:** Ensure the root CA certificate has been imported on the client device. Verify the server certificate is signed by the root CA.
* **Security Issue:** Exporting the root CA certificate without passphrase.
    * **Solution:** Always use strong passphrase to protect your certificate files if you choose to use PKCS12 format and protect the certificate from unauthorized use. The `export-passphrase` parameter will encrypt the private key as part of the generated certificate. When using the X.509 certificate, be sure to protect access to the file as well.

## Verification and Testing Steps:

1.  **Check Certificate Status:**
    ```mikrotik
    /certificate print
    ```
    *   Verify `A` (Active) flag for `myCA` and `server-wlan41`.
    *   Verify the `valid-from` and `valid-to` dates.
2.  **Check Flags:**

  Make sure that all flags are correct.
      * `K`: private key is present.
      * `A`: certificate is active and valid.
      * `T`: certificate is trusted (for root CA, this is automatically flagged).
      * `D`: certificate is for dynamic use.

3.  **Verify with a Client (Optional):** To see if the certificate is trusted, configure an application like a VPN or web server to use the `server-wlan41` certificate, and connect to that service from a client. Note that this is beyond the scope of this document, but necessary to fully verify that certificates are in place. Make sure to import the CA certificate onto the client so that it trusts the server certificate.

## Related Features and Considerations:

*   **Certificate Revocation Lists (CRLs):** Consider using CRLs to revoke compromised certificates.
*   **ACME protocol:**  Automated certificate management using ACME (Automatic Certificate Management Environment) simplifies the process of certificate provisioning and revocation, however it is not suitable for cases when a local certificate is needed.
*   **RouterOS VPNs:** Certificates are essential for configuring secure VPNs like IPsec and SSTP on MikroTik.
*   **Secure Web Server:** Certificates are used to secure access to the RouterOS WebFig interface.
* **Resource Usage:** Certificates themselves do not use a lot of resources, but protocols that use the certificate (like TLS) can. It would be prudent to monitor CPU usage if implementing VPNs or other resource intensive services that use certificates.

## MikroTik REST API Examples (if applicable):

As of RouterOS 7.11, there is no direct REST API endpoint to generate certificates using the `/certificate` resource. The API is more geared towards monitoring and fetching existing certificates. While we could potentially implement custom scripting to achieve that goal, we'll focus on viewing and exporting existing certificates.

**Viewing Certificates:**

*   **API Endpoint:** `/certificate`
*   **Request Method:** `GET`
*   **Example Response (JSON):**
    ```json
    [
        {
            "id": "*0",
            "name": "myCA",
            "common-name": "My Root CA",
            "key-usage": "key-cert-sign,crl-sign,digital-signature",
            "subject-alt-name": "DNS:myca.local,IP:192.168.88.1",
            "days-valid": "3650",
            "valid-from": "2024-05-17T14:01:00+00:00",
            "valid-to": "2034-05-17T14:01:00+00:00",
            "flags": "KATD"
        },
       {
            "id": "*1",
            "name": "server-wlan41",
            "common-name": "wlan41.mycompany.local",
            "key-usage": "tls-server",
            "subject-alt-name": "DNS:wlan41.mycompany.local,IP:220.120.159.1",
            "days-valid": "1825",
            "valid-from": "2024-05-17T14:02:00+00:00",
            "valid-to": "2029-05-17T14:02:00+00:00",
            "flags": "KA"
        }
    ]
    ```
* **Description:** This would return the certificate information of all certificates, including information about validity, and key usage.

**Exporting a Certificate:**
* **API Endpoint:** `/certificate/export`
* **Request Method:** POST
* **Example JSON Payload:**
```json
 {
  "id": "*0",
  "file-name":"myCA-api.crt"
  }
```
* **Example Response (JSON):**  This call does not return anything directly in the response. Instead the API will create the new file in the `/files` folder.
* **Description:** The "id" field will export the certificate associated with the given ID (e.g. `*0` for myCA). The "file-name" parameter is optional.  If no file-name is provided, the certificate name will be used as the filename.  Once the API call is completed successfully, a new file will be created in the `/files` folder with the name provided.  The API call is not able to export the private key in a secure way, and does not offer options for password protection of the private key.

**Error Handling**
*   If a parameter is wrong, the API will return a `400` error code.  If the certificate `id` is invalid a `404` error code would be returned.

## Security Best Practices:

*   **Secure Private Key:**  Never export private keys unless absolutely necessary, and then use the PKCS#12 format with a strong passphrase, where the key will be encrypted. The private key of a CA should always remain secured.
*   **Limited Access:**  Restrict access to the RouterOS device and its configuration to authorized users, using strong passwords and different user levels.
*   **Regular Updates:** Keep RouterOS updated to patch any security vulnerabilities.
*   **Certificate Validation:** Validate certificates properly when configuring services that use certificates (such as a VPN or a secure webserver).
*   **Export certificates securely**: When exporting a certificate, ensure to use a secure transfer mechanism, such as SCP, SFTP, or other encrypted protocols.

## Self Critique and Improvements:

This configuration provides a basic foundation for certificate management. It could be improved by adding the following:

*   **Automated Certificate Renewal:** Setting up scripts or tools for automated certificate renewal would be beneficial to reduce the risk of expired certificates.
*   **More Robust Key Sizes:** Using higher key sizes, e.g. 4096 bits for RSA or equivalent would increase the security.
*  **More Certificate Fields:** Adding extra certificate fields (such as organizational unit) would increase the granularity of the generated certificate.
*   **Implementing Certificate Revocation:** Implementing Certificate Revocation Lists (CRLs) to invalidate compromised certificates would significantly improve security.
*   **Certificate Chain Validation:** Ensure all parts of a chain are properly configured.

## Detailed Explanations of Topic:

Certificates are digital documents that are used to verify identities. A certificate contains a public key, which can be used to encrypt data, and information about the identity of its owner. The certificate is signed by a trusted third party (a Certificate Authority), which ensures the integrity of the certificate and that it is issued to the claimed owner. The key is associated with the identity of the owner, so a secure communication can take place. Certificates are used for securing various services, such as web servers, email servers, and VPNs, with mechanisms such as TLS to establish a chain of trust, providing encryption and authentication between parties. Certificates can be used for authentication only, encryption only, or both.

## Detailed Explanation of Trade-offs:

*   **Self-Signed vs. CA-Signed:** Self-signed certificates are easier to create, but they are not trusted by default by any device. CA-signed certificates, although harder to generate, are trusted if the CA certificate is trusted. CA signed certificates are highly recommended to be used on any network where security is important.
*   **Certificate Validity Period:** Longer validity periods are convenient, but pose a higher risk if a certificate is compromised. Shorter periods force more frequent renewals, which increases operational overhead.
*   **Key Size:** Larger keys are more secure but require more computational power. Smaller keys are less secure but faster. In most modern routers the default sizes are usually sufficient for most needs.
*  **Curve Used for Signing:** Using elliptic curves (ECDSA), rather than the RSA algorithm, results in smaller certificate sizes and faster signature processing for the same level of security.
*   **Using CRLs vs OCSP:** CRLs are lists of certificates that have been revoked, and must be downloaded and checked by the client. Online Certificate Status Protocol (OCSP) allows for real-time checking, which is generally preferred, but requires an OCSP responder. For the vast majority of basic setups, the use of CRLs is not required.
*  **Single Certificate vs Certificate Chains:** When connecting to public web servers, multiple certificates are used in a chain. For example, a client must trust a root CA, to trust an intermediate CA, to trust the server certificate. Usually, for basic setups, the use of a single CA certificate is sufficient.
*  **Public vs Private CA:** A public CA is trusted by almost all clients and operating systems. A private CA has the same structure, however, the client will need to manually install the CA certificate to be able to trust certificates signed by that private CA. This is the scenario that has been shown in this document.

## Configuration for Specific RouterOS Versions:

This configuration is compatible with MikroTik RouterOS 6.48 and 7.x versions, however, I am focusing specifically on RouterOS 7.11. The certificate generation and signing commands have not significantly changed between these versions. The API call to export a certificate is available from RouterOS 7.0 onwards.

Let me know if you need any further clarifications or adjustments!

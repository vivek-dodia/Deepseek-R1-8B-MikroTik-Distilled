Okay, let's create comprehensive documentation for handling certificates on a MikroTik RouterOS device (v6.48 and 7.x), specifically focusing on a basic SOHO setup with the `wlan-3` interface on the `218.234.138.0/24` subnet. While we aren't going to use the IP address for the certificate itself, we will keep the subnet in mind as that might be relevant later for other things we might want to do.

## Scenario Description:

This document describes how to generate a self-signed certificate on a MikroTik router, primarily for demonstration and testing purposes. This is common in SOHO environments for securing web interfaces, APIs, or other services running on the router itself. In the context of our network, this allows management of the device using a certificate over the `wlan-3` interface.  While this isn't a requirement for the network configuration, understanding certificate generation and usage is important for later more advanced use-cases.

## Implementation Steps:

Here's a step-by-step guide to generating and viewing a self-signed certificate.

**1. Step 1: Check Existing Certificates**

   *   **Explanation:** Before creating a new certificate, it's always good to check what certificates are already present on the router. This allows for a better understanding of the device's state and can prevent conflicts.
   *   **CLI Command (before):**
        ```mikrotik
        /certificate print
        ```
   *   **Winbox GUI:** Navigate to System > Certificates.
   *   **Expected Result (before):** Output will likely be empty if no certificates have been created yet, or will list existing certificates if there are any. The output would look something like:
        ```
        Flags: K - private-key, I - issued, A - authority, T - trusted
        #   NAME                                    SUBJECT                                  FINGERPRINT
        ```
        or if certificates exist, something like:

        ```
        Flags: K - private-key, I - issued, A - authority, T - trusted
        #   NAME                                    SUBJECT                                  FINGERPRINT
        0 K   test-cert                            CN=test-cert                                  12:34:56:78:90:AB:CD:EF:12:34:56:78:90:AB:CD:EF
        ```
   *   **Action:** Note any existing certificates, if any.

**2. Step 2: Generate a Self-Signed Certificate**

   *   **Explanation:** This step creates a new self-signed certificate. We use a basic configuration suitable for testing purposes.  We will give this certificate a name of "my-test-cert" so we can find it later.
   *   **CLI Command:**
        ```mikrotik
        /certificate add name=my-test-cert common-name=my-test-cert generate-key=yes key-usage=digital-signature,key-encipherment
        ```
   *   **Winbox GUI:**
        1.  Navigate to System > Certificates.
        2.  Click the "+" button.
        3.  In the "New Certificate" window:
            *   Enter a name (e.g., `my-test-cert`).
            *   Enter the "Common Name" (e.g., `my-test-cert`).
            *   Ensure "Generate Key" is checked.
            *   Under "Key Usage" select "digital-signature" and "key-encipherment".
            *   Click "Apply" and then "OK".
   *   **Parameters Explanation:**
       | Parameter     | Description                                                                                             | Example Value                       |
       |---------------|---------------------------------------------------------------------------------------------------------|------------------------------------|
       | `name`        | A descriptive name for the certificate                                                                    | `my-test-cert`                     |
       | `common-name` | The Common Name (CN) for the certificate (e.g., a hostname)                                              | `my-test-cert`                     |
       | `generate-key`| Indicates that a new private key should be generated along with the certificate                        | `yes`                              |
       | `key-usage`    | Specifies the allowed uses of the private key; `digital-signature` enables data signing, `key-encipherment` encryption | `digital-signature,key-encipherment`  |
   *   **Expected Result:** The router will generate a new certificate and associated private key.
   *   **CLI Command (after):**
        ```mikrotik
        /certificate print
        ```
   *   **Expected Result (after):** Output will display the newly created certificate with the flags `K` (private key) and `I` (issued).
        ```
        Flags: K - private-key, I - issued, A - authority, T - trusted
        #   NAME                                    SUBJECT                                  FINGERPRINT
        0 KI  my-test-cert                         CN=my-test-cert                             12:34:56:78:90:AB:CD:EF:12:34:56:78:90:AB:CD:EF
        ```
   *   **Action:** Note the fingerprint for later verification.

**3. Step 3: Exporting the Certificate**
    *   **Explanation:**  While this isn't strictly necessary for the purpose of this document (as the certificate will be used by the router for its internal services), it is a good step to show how to export certificates. This might be required for other use-cases, such as using the certificate with client software for secure access. We can export the certificate in PEM format (base64 encoded)
    *   **CLI Command:**
        ```mikrotik
        /certificate export-certificate my-test-cert export-passphrase="" file-name="my-test-cert"
        ```
    *   **Winbox GUI:**
       1. Navigate to System -> Certificates.
       2. Find the certificate named "my-test-cert" and click on it.
       3. Click on the "Export" button.
       4.  In the "Export Certificate" window:
          * Under the "File name" field type in "my-test-cert".
          * Ensure the "Export Passphrase" is empty.
          * Ensure that "Export Format" is set to "pem"
          * Click "Export"

   *   **Parameters Explanation:**
       | Parameter            | Description                                                                                             | Example Value  |
       |----------------------|---------------------------------------------------------------------------------------------------------|----------------|
       | `name`              | The name of the certificate to be exported                                                            | `my-test-cert` |
       | `export-passphrase`   | Password to be used for encrypting the exported certificate                                          | ``             |
       | `file-name`        | The file name for the exported certificate. If the file already exists, it will be overwritten | `my-test-cert`|
    *   **Expected Result:** The router will have created a file called `my-test-cert.pem` in the router's files.
   *  **Action:** The certificate is now available to download under `/files`. It can be downloaded using Winbox by clicking on the files tab, finding the file `my-test-cert.pem` and dragging it to a local file explorer window.

**4. Step 4: Verification of exported Certificate**

   *   **Explanation:** This step verifies the newly generated certificate, by looking at its contents and checking for basic validity.  A basic way to do this is to use a tool such as `openssl`.
    *   **CLI Command (local Linux/MacOS/Windows with openssl):**
         ```bash
         openssl x509 -in my-test-cert.pem -text -noout
         ```
   *   **Expected Result:** The output should include details of the certificate that are consistent with the configuration settings.
   *   **Action:** Inspect the certificate subject, issuer, and validity period.

## Complete Configuration Commands:

```mikrotik
/certificate
add name=my-test-cert common-name=my-test-cert generate-key=yes key-usage=digital-signature,key-encipherment
print
export-certificate my-test-cert export-passphrase="" file-name="my-test-cert"
```

## Common Pitfalls and Solutions:

*   **Problem:**  `error loading certificate` during certificate creation.
    *   **Solution:**  Ensure the RouterOS version supports the chosen key size and algorithms. Try re-creating with a shorter key size, if that's the cause.
*   **Problem:** Certificate not being recognized by clients.
    *   **Solution:** Self-signed certificates are not trusted by default. Clients require manual addition of the certificate to their trust stores or to disable the certificate check. You'll need to download the certificate and install it.
*   **Problem:** Mismatched common name, resulting in warnings about the site not being secure.
    *   **Solution:** Ensure the common name matches the domain or IP address used to access the router.  Make sure you use a *proper* public certificate for use in production.
*   **Problem:**  "Error: key has weak algorithm"
    *   **Solution:** Newer RouterOS versions and later TLS versions do not permit weak algorithms.  Ensure that the key is a strong algorithm that is supported by the router. If the configuration is being done on a very old router, there might not be enough resources or supported algorithms to generate this.
* **Problem:** The Router does not have the resources required to generate the key.
    * **Solution:** This is rare, but can occur on older Mikrotik hardware. The solution is to generate the certificate on a faster device (such as a linux machine), and then import the certificate to the router.

## Verification and Testing Steps:

1.  **Check Certificate Existence:** Use `/certificate print` to see the created certificate.
2.  **Check Certificate Details:** Use `/certificate print detail` to inspect the details of the generated certificate, including the public key.
3.  **Download and Examine Certificate:** Download the exported certificate and verify using `openssl` as outlined above.

## Related Features and Considerations:

*   **Certificate Authority (CA):** For a more secure setup, obtain a certificate from a trusted CA. This will avoid the browser warnings about self-signed certificates.
*   **ACME Client:** MikroTik routers support ACME clients for automatically obtaining certificates from providers like Let's Encrypt.  This is the *best* way to secure your router with a valid certificate. This topic is outside of the scope of this documentation, but will be included in future documents.
*   **Certificate Usage:** Use the certificate to secure various services like the router's web interface (`/ip service`), the API, or any other service running on the router requiring SSL/TLS.
*   **Resource Usage:** Generating certificates is a CPU intensive task. Check CPU usage using `/system resource print`.
* **Multiple certificates:** MikroTik routers support multiple certificates. Each of those can be used for a different purpose. Make sure you know which certificate you need when configuring router services.
* **Password Protect Private Keys:** Make sure to use a strong password to protect the private key when generating or exporting it, when possible. While the router protects this key internally, additional protection is a good practice. This particular document exports without a password since this is for a demonstration and a self-signed certificate is not particularly sensitive, but production systems should always have additional password protection, if supported.
* **Certificate Renewal:** Certificates expire, plan to renew or replace before they do expire.

## MikroTik REST API Examples:

Note: MikroTik RouterOS API does not support the certificate generation function. The API calls are primarily useful for exporting certificates or using the already generated certificates for services like RouterOS's API itself.

*   **Retrieving Certificate List:**
    *   **Endpoint:** `/certificate`
    *   **Method:** `GET`
    *   **Example Command:**
        ```bash
        curl -k -u admin:password 'https://your-router-ip/rest/certificate'
        ```
    *   **Expected Response:** JSON payload containing the certificate list details.

        ```json
        [
          {
            ".id": "*1",
            "name": "my-test-cert",
            "subject": "CN=my-test-cert",
            "issuer": "CN=my-test-cert",
            "valid-from": "2024-05-23T22:25:47Z",
            "valid-to": "2025-05-23T22:25:47Z",
            "fingerprint": "12:34:56:78:90:AB:CD:EF:12:34:56:78:90:AB:CD:EF",
            "flags": "KI"
          }
        ]
        ```
*   **Exporting Certificate (API is limited to what is exposed by RouterOS):**

    *  **Endpoint:** `/certificate/export-certificate`
    *   **Method:** `POST`
    *   **Example Command:**
    ```bash
    curl -k -u admin:password -H "Content-Type: application/json" -d '{"name": "my-test-cert", "export-passphrase": ""}' 'https://your-router-ip/rest/certificate/export-certificate'
    ```
        * **Note:** This will not return a PEM file, instead you would need to download the file using the `/file` REST endpoint after the command has been executed.
    *   **Example JSON Payload:**
        ```json
          {
              "name": "my-test-cert",
              "export-passphrase": ""
          }
        ```
    *   **Expected Response:**  A 200 success return code. Use `/file` API call to retrieve the exported certificate file.
* **Error Handling**
    * When using a REST API call, be sure to check the response to see if there was any error in your request, for instance an invalid format, or missing parameter. Be sure to check the HTTP return codes in order to ensure your request worked as expected.

## Security Best Practices

*   **Private Key Protection:** Protect private keys, using a password if possible. Never expose private keys in logs or in other unencrypted files.
*   **Strong Passwords:** Use strong passwords when generating keys. While this is done automatically internally, this is good practice if you are exporting the private key.
*   **Self-Signed Limitations:** Understand that self-signed certificates are not trusted by default. Use CAs for production.
*   **Certificate Revocation:**  For non self-signed certificates, ensure that you are aware of the Certificate Revocation processes.
*   **TLS Protocol Selection:** Ensure that TLS v1.2 is enabled, and v1.3 if possible. Avoid older versions of TLS and SSL.

## Self Critique and Improvements:

*   **Improvement:** The current configuration provides a basic method for creating a self-signed certificate. While this is enough for the basic scope of the document, a real world example would require obtaining a public certificate via a real CA or an ACME client.
*   **Improvement:** Enhance the document with details on using the generated certificate for securing specific services, for example the web interface.
*   **Improvement:** Incorporate sections on certificate renewal and lifecycle management.
*   **Improvement:** Add detailed troubleshooting steps for the REST API calls.
*   **Improvement:** Add a more detailed section on public certificate generation and use, including ACME clients.
*   **Improvement:** Include detailed section about more specific Key Usage and Extended Key Usage parameters.
*   **Improvement:** Add a more detailed section about the trade-offs between RSA, ECDSA and EdDSA.
*   **Improvement:** Add more information about file management via the API

## Detailed Explanations of Topic

Certificates are digital documents used to establish identity and secure communications on the internet. They employ public key cryptography to ensure that data remains private, can be verified, and its origin can be confirmed.

*   **Public Key Infrastructure (PKI):** Certificates are part of PKI, which consists of Certificate Authorities (CAs), registration authorities, and users.
*   **Types of Certificates:**
    *   **Self-signed certificates:** Generated by the user, not trusted by default. Useful for internal testing.
    *   **CA-signed certificates:** Issued by trusted CAs, trusted by most browsers and devices.
*   **Certificate Contents:** Certificates contain:
    *   Subject (identifies the certificate owner).
    *   Issuer (identifies the certificate authority).
    *   Public key (used for encryption).
    *   Validity period.
    *   Digital signature (to verify authenticity).
    *   Key Usage.

## Detailed Explanation of Trade-offs

*   **Self-Signed vs. CA-Signed Certificates:**
    *   **Self-Signed:** Simple to generate, free, not trusted, causes browser warnings. Good for internal or testing environments.
    *   **CA-Signed:** More complex to obtain (requires a CA), not free, trusted by default, provides stronger security assurances. Essential for public-facing services.
* **RSA vs ECC Certificates**
    * **RSA** RSA certificates have a more established and wider support.
    * **ECC** ECC has lower key sizes compared to RSA, which translates to lower resource usage and higher performance.
* **Key Size**
    * Larger key sizes provide more security, but need more processing and resources. Use the largest key size that is supported by the system and client devices.
* **Password Protecting Private Keys**
    * Password protection adds an extra layer of security, but creates additional complexity in the management of the certificate.

## Configuration for Specific RouterOS Versions:

The above commands and information are generally applicable to both RouterOS v6.48 and v7.x. Note, however, that very old RouterOS releases before 6.48 may have different commands, such as not using `add` or having other key algorithm limitations. Always consult the specific RouterOS documentation for the version you are using. For example, versions before 6.x used the command `certificate import` instead of `certificate add`.  In addition, older releases might not support newer crypto algorithms such as ECC certificates.

Let me know if you have any other questions or scenarios you'd like to explore!

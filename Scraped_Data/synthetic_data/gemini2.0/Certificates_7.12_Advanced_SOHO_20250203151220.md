Okay, let's dive deep into configuring certificates on a MikroTik RouterOS device, specifically focusing on RouterOS 7.12 (though concepts apply to 6.48 and 7.x) within a SOHO context using the specified subnet and interface name. This configuration will center on generating a self-signed certificate for secure router access, a common task even in smaller environments.

## Scenario Description:

This document outlines the process of generating a self-signed certificate on a MikroTik router for HTTPS access (WebFig, API), and potentially for secure VPN services. This certificate will secure communication with the router, preventing eavesdropping of sensitive information. Our target subnet is 60.34.24.0/24, and we will be focusing on actions around interface `bridge-28`, though the certificate configuration itself isn't directly tied to any interface.

## Implementation Steps:

### Step 1: Check Existing Certificates (Optional)

Before creating a new certificate, it's good practice to check if there are any existing certificates. This prevents accidental overwriting and helps understand the current state.

**CLI:**

```
/certificate print
```

**Winbox:**
Navigate to System > Certificates. Examine the existing certificate list.

**Before:** (Assuming no certificate currently exists or you have a default router self-signed certificate)

```
Flags: K - private-key, A - authority, T - trusted
 #   NAME                                SUBJECT                FINGERPRINT                    INVALID   
```

**Explanation:**
This command lists all configured certificates on the router. In this example, if nothing is present, we will see no output. The `flags` indicate if the certificate has a private key (K), acts as an authority (A), or is trusted(T).

### Step 2: Generate a New Certificate

We'll generate a self-signed certificate. This certificate will be used to secure access to the router's web interface (WebFig), API access, and potentially other services.

**CLI:**

```
/certificate add name=myroutercert common-name=router.local key-usage=digital-signature,key-encipherment,tls-server  days-valid=365
```

**Winbox:**
Navigate to System > Certificates, click the "+" button. Fill out the fields as indicated below, and click Apply.

*   **Name:** `myroutercert`
*   **Common Name:** `router.local`
*   **Key Usage:** Select "digital-signature", "key-encipherment", and "tls-server"
*   **Days Valid:** 365

**After:**

```
Flags: K - private-key, A - authority, T - trusted
 #   NAME                                SUBJECT                FINGERPRINT                    INVALID   
 0   myroutercert                       CN=router.local        XXXXXXXX...                      no   
```

**Explanation:**
This command creates a new certificate named `myroutercert` with a `common-name` of `router.local`. The `key-usage` specifies how the certificate can be used (digital signature for verification, key encipherment for encryption, and tls-server for server authentication in TLS). The `days-valid` determines how long the certificate is valid before it expires (365 days, about a year).

*Note*:  While a domain-name-like common name (router.local) is recommended, it doesn't have to be a real DNS record to function. Using an IP address for the common name works as well, but can lead to browser warnings.

### Step 3: Enable the Certificate for HTTPS Service

Now that we have a certificate, we need to tell the router's HTTPS service to use it.

**CLI:**

```
/ip service set www-ssl certificate=myroutercert
```

**Winbox:**
Navigate to IP > Services, find `www-ssl`, and select the newly created `myroutercert` from the "Certificate" drop-down list. Then click Apply.

**Before:** (Assuming the default certificate or no certificate was selected).
In winbox, the 'Certificate' field of `www-ssl` would either be empty or 'default'.

**After:**
In winbox, the 'Certificate' field of `www-ssl` would now be `myroutercert`.

**Explanation:**
This command assigns the `myroutercert` certificate to the `www-ssl` service (used for HTTPS access to WebFig). It tells the router to use this certificate when setting up an HTTPS connection. If you leave this field empty, the default router self-signed certificate is used.

### Step 4: Verify HTTPS Access

After enabling the certificate, verify that the router’s web interface is accessible over HTTPS using the specified IP address or hostname.

## Complete Configuration Commands:

```
# Check existing certificates
/certificate print

# Generate a self-signed certificate
/certificate add name=myroutercert common-name=router.local key-usage=digital-signature,key-encipherment,tls-server days-valid=365

# Assign the certificate to the HTTPS service
/ip service set www-ssl certificate=myroutercert
```

**Parameter Explanations:**

| Command / Parameter      | Description                                                                |
| :----------------------- | :------------------------------------------------------------------------- |
| `/certificate print`     | Lists all certificates configured on the router.                           |
| `/certificate add`        | Adds a new certificate.                                                   |
| `name`                    | Specifies the name for the certificate (e.g., `myroutercert`).             |
| `common-name`             | The subject's name (e.g., `router.local`, or an IP address).               |
| `key-usage`              | Specifies the intended usage of the certificate key (e.g., digital signature, key encipherment, tls server, tls client). |
| `days-valid`             | The number of days the certificate is valid for (e.g., 365 for one year). |
| `/ip service set`        | Modifies properties of IP services.                                        |
| `www-ssl`               | Refers to the web-ssl service, used for HTTPS access to WebFig and API.       |
| `certificate`           | Specifies the certificate to use for the service.                         |

## Common Pitfalls and Solutions:

*   **Browser Warning:** Self-signed certificates are not trusted by default by browsers. Browsers will display a warning message that you'll need to bypass. To remedy this, you need to get a trusted certificate signed by a certificate authority, or manually import the certificate into the browser’s trusted root store which is an unnecessary extra step for a SOHO network.
*   **Certificate Not Applied:** If the WebFig still shows a default certificate, check that the `certificate` parameter is correctly set in the `www-ssl` service, with the correct certificate name.
*   **Incorrect Key Usage:** If you encounter issues, verify that the `key-usage` includes the needed flags. For TLS, `digital-signature`, `key-encipherment` and `tls-server` are needed.
*   **Certificate Expired:** The certificate will become invalid once the `days-valid` period has passed. You'll need to create and apply a new certificate.
*   **Private Key Not Present:** If you get an error relating to a missing private key, this means that the private key was not generated at the same time as the certificate. This is because the 'K' flag for private key was not present. Ensure that 'K' is present in the output of `/certificate print` by generating a new certificate again with the correct options and the correct key-usage.
*   **Resource Usage**: Generating a self-signed certificate takes negligible CPU usage in a SOHO scenario.
*   **DNS Issues:** Incorrect common name values can lead to browser warnings when browsing to different domains than what the certificate was created with.

## Verification and Testing Steps:

1.  **HTTPS Web Access:** Open a web browser and navigate to `https://<router-ip-address>` or `https://router.local` if you have set a local DNS entry pointing to your router. You should see the WebFig interface, but initially, you will see a warning about an untrusted certificate. Accept the warning, and proceed. The address bar should show HTTPS with a lock icon (albeit likely marked as untrusted or insecure).
2.  **Certificate Information:** Click on the lock icon in your browser's address bar. View the certificate details. You should see the certificate information you provided, especially the `common-name` you set (e.g., `router.local`).
3. **API access**: Try an api call using https. If the api doesn't connect, or certificate issues arise, ensure `www-ssl` is the correct service and that `api-ssl` is enabled with the correct certificate if you are using that instead.
4.  **Check `certificate print`:** Run `/certificate print` again. Ensure the `INVALID` column shows "no" for your certificate and that the `K` flag is present.
5.  **Torch Tool (Optional):** You can use the `/tool torch` command, to check the connections to your web interface. Specifically filtering by protocol `tcp` and destination port `443`, and viewing that packets are received via `https` on the `bridge-28` interface.

## Related Features and Considerations:

*   **Certificate Authority (CA) Signed Certificates:** While self-signed certificates are fine for personal use, for production environments where the router will be accessed by many users, using a certificate from a trusted CA is highly recommended. MikroTik can import certificates in the `.pem` or `.crt` format.
*   **Let's Encrypt:**  MikroTik does not have built-in Let's Encrypt support, however, there are scripts which can automate this process. This would allow for automated certificate generation and renewal.
*   **VPN Services:** The certificate can be used for VPN services like IPsec, L2TP, SSTP, or OpenVPN to create a more secure connection, or to enforce client side authentication. You can set the `certificate` option for these protocols as well using the certificate we have generated.
*   **Hotspot Certificates**: The certificate can be used for a captive portal if one exists, for example as a part of a hotspot.

## MikroTik REST API Examples:

Here are a few relevant REST API examples assuming you have the API enabled and authenticated:

**1. Get Certificate List:**

*   **Endpoint:** `/certificate`
*   **Method:** `GET`
*   **Example `curl` Command:**

    ```bash
    curl -k -u admin:<your_password> -H 'Content-Type: application/json' https://<router-ip-address>/rest/certificate
    ```

*   **Expected Response:**

    ```json
    [
      {
        ".id": "*0",
        "name": "myroutercert",
        "subject": "CN=router.local",
        "fingerprint": "XXXXXXXX...",
        "invalid": "no",
        "flags": "K"
      }
     ]
    ```
    **Note**: Replace `<your_password>` and `<router-ip-address>` with actual values.

**2. Add a New Certificate:**

*   **Endpoint:** `/certificate`
*   **Method:** `POST`
*   **Example JSON Payload:**

    ```json
    {
        "name": "myroutercert2",
        "common-name": "router2.local",
        "key-usage": "digital-signature,key-encipherment,tls-server",
        "days-valid": 365
    }
    ```
*   **Example `curl` Command:**

    ```bash
    curl -k -u admin:<your_password> -H 'Content-Type: application/json' -d '{"name": "myroutercert2", "common-name": "router2.local", "key-usage": "digital-signature,key-encipherment,tls-server", "days-valid": 365 }' https://<router-ip-address>/rest/certificate
    ```
*   **Expected Response:** (201 Created, and details of the new certificate)

    ```json
    {
    ".id":"*1",
    "name":"myroutercert2",
    "subject":"CN=router2.local",
    "fingerprint":"YYYYYYY....",
    "invalid":"no",
    "flags":"K"
    }
    ```

**3. Set WWW-SSL Certificate:**

*   **Endpoint:** `/ip/service/www-ssl`
*   **Method:** `PATCH` (or `PUT`)
*   **Example JSON Payload:**

    ```json
    {
      "certificate": "myroutercert"
    }
    ```
*   **Example `curl` Command:**

    ```bash
      curl -k -u admin:<your_password> -H 'Content-Type: application/json' -X PATCH -d '{"certificate":"myroutercert"}' https://<router-ip-address>/rest/ip/service/www-ssl
    ```

*   **Expected Response:** (200 OK) or (204 No Content) depending on the routerOS version.

**Error Handling:**

*   API errors will usually return a HTTP status code outside of 200-299 range.
*   The response may have a `message` field in JSON, which contains further details.
*   Incorrect parameters in API calls, will respond with code 400 Bad Request.

## Security Best Practices

*   **Key Usage:** Always restrict the `key-usage` flag to the intended purposes. Avoid giving unnecessary rights.
*   **Keep RouterOS Updated:** Vulnerabilities in software may be exploited. Maintain a regularly updated system.
*   **Restrict Web Access:** Consider disabling the web interface on the WAN interface or limit access by IP address.
*   **Secure API Access:** Use strong credentials, or disable it completely when not needed.
*   **Secure Certificate Storage:** Keep the private key secret, protect it from accidental exposure.
*   **Trusted certificates:** Avoid self-signed certificates where possible. If you must use self-signed certificates for SOHO type connections, consider using an internal CA that is self-signed to reduce browser errors.

## Self Critique and Improvements

*   **Automation:** This configuration is manual. Automating the certificate generation (with tools like Let's Encrypt) would make the system more robust and require less manual maintenance.
*   **Certificate Renewal:** The self-signed certificate requires manual renewal. An automated solution for renewal and certificate rotation would be ideal, or certificates with much longer validity periods can be used.
*   **Specific Key Sizes:** Explicitly specifying the key size (e.g., `key-size=2048` or `key-size=4096`) can be done for added security.
*   **Subject Alternative Names (SANs):** Adding SANs would allow the certificate to be valid for other domain names, or IP addresses. These would need to be defined in the certificate generation process.

## Detailed Explanations of Topic:

Certificates in MikroTik RouterOS are fundamental for securing communication. A certificate serves as a digital identity card, proving the identity of a server or client. The certificate is created together with a private key and a public key, used for encryption.

**Types of Certificates:**

*   **Self-Signed:** Created by the router, not signed by a certificate authority. Suitable for internal use or SOHO networks.
*   **CA-Signed:** Signed by a trusted certificate authority (CA), which verifies the identity of the server. Preferred for public-facing services.

**Certificate Anatomy:**

*   **Subject:** Contains the details of the certificate holder (typically includes common-name (CN)).
*   **Public Key:** Used to encrypt data that can only be decrypted by the private key.
*   **Private Key:** Used to decrypt data and to sign data. This key must be kept secure.
*   **Validity Period:** Defines the time the certificate is valid.
*   **Key Usage:** Defines what the key can be used for.
*   **Authority:** Certificates have a CA/Authority that can verify and sign certificates to be trustworthy.

**MikroTik Certificate Management:**

*   Certificates can be imported, exported, or generated within RouterOS.
*   The `certificate` resource `/certificate` allows creating, listing, importing, exporting and modifying certificates.
*   Services like `www-ssl` use the specified certificate for TLS communication.

## Detailed Explanation of Trade-offs:

*   **Self-signed vs. CA-signed:** Self-signed certificates are free and easy to generate, but not trusted by browsers. CA-signed certificates are trusted, but cost money and may require more complex setup. The trade-off is between convenience and trust.
*   **Key Sizes:** Larger key sizes increase security, but may increase CPU load. 2048 bits is a good balance.
*   **Validity Period:** Longer validity periods reduce management overhead, but they also present a longer timeframe for which a compromised key may be used, this is traded against practicality.
*   **Key Usage:** Giving fewer rights is safer, but may be less convenient. Only provide what is needed to avoid unnecessary risks.
*   **TLS versions:** Although not part of this configuration, TLS versions can also be configured, and it should be kept in mind that older TLS versions are not secure, and should not be used where possible.

## Configuration for Specific RouterOS Versions:

This configuration is designed for RouterOS 7.12 and is generally applicable to versions 6.48 and 7.x. There should be no differences between these versions in relation to certificates.

*Important Note*: This document assumes a basic level of familiarity with MikroTik RouterOS. Remember to back up your router configurations before making major changes. Remember to replace `<router-ip-address>` and `<your_password>` with your router’s actual IP address and password in the examples given.

This thorough documentation provides a complete guide to generating and using self-signed certificates on MikroTik devices for securing access to WebFig and API access within a SOHO environment. The explanation covers practical implementation, security considerations, and potential pitfalls to help you confidently implement a secure and functional network configuration.

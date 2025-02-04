# Document Information
Title: Certificates
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/2555969/Certificates,

# Content
# Overview
```
/certificate
```
The general menu is used to manage certificates, add templates, issue certificates, and manage CRL and SCEP Clients.
# Certificate Template
Certificate templates are used to prepare a desired certificate for signing.
Certificate template is deleted right after a certificate is signed or a certificate request command is executed
```
/certificate
add name=CA-Template common-name=CAtemp key-usage=key-cert-sign,crl-sign
add name=Server common-name=server
add name=Client common-name=client
```
To print out certificates:
```
[admin@4k11] /certificate> print detail
Flags: K - private-key; L - crl; C - smart-card-key; A - authority; I - issued, R - revoked; E - expired; T - trusted
0         name="CA-Template" key-type=rsa common-name="CAtemp" key-size=2048 subject-alt-name="" days-valid=365 key-usage=key-cert-sign,crl-sign
1         name="Server" key-type=rsa common-name="server" key-size=2048 subject-alt-name="" days-valid=365
key-usage=digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client
2         name="Client" key-type=rsa common-name="client" key-size=2048 subject-alt-name="" days-valid=365
key-usage=digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client
```
# Certificate properties
Property | Description
----------------------
common-name(string) | Certificate common name
copy-from(name) | Certificate name from which to copy general settings
country(string) | Certificate issuer country
days-valid(days Default: 365) | Days certificate will be valid after signing
digest-algorithm(md5 | sha1 | sha256 | sha384 | sha512Default:sha256) | Certificate public key algorithm
key-size(1024 | 1536 | 2048 | 4096 | 8192 | prime256v1 | secp384r1 | secp521r1Default:2048) | Certificate public key size
key-usage(code-sign | crl-sign | decipher-only | dvcs | encipher-only     key-cert-sign | ocsp-sign | tls-client |content-commitment | data-encipherment | digital-signature | email-protect | key-agreement | key-encipherment | timestamp | tls-serverDefault: digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client) | Certificate usage
locality(string) | Certificate issuer locality
name(string) | Certificate name
organization(string) | Certificate issuer organization
state(string) | Certificate issuer state
subject-alt-name(DNS: | IP: | email:) | Certificate subject alternative name
trusted(no| yes Default:) |
unit(string) | Certificate issuer organizational unit
key-usage(code-sign | crl-sign | decipher-only | dvcs | encipher-only     key-cert-sign | ocsp-sign | tls-client |content-commitment | data-encipherment | digital-signature | email-protect | key-agreement | key-encipherment | timestamp | tls-serverDefault: digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client)
locality(string)
name(string)
organization(string)
state(string)
subject-alt-name(DNS: | IP: | email:)
trusted(no| yes Default:)
unit(string)
# Certificate read-only properties
After a certificate is signed, most of a certificate template properties are converted to read-only (exceptnameandtrusted)
Property | Description
----------------------
serial-number | Certificate serial number
fingerprint |
akid | Certificate authority ID
skid | Certificate subject ID
invalid-before | Date and time before which a certificate expired
invalid-after | Date and time after which a certificate expired
expires-after |
key-type |
ca | Certificate authority common name
expires-after
# Sign Certificate
Certificates should be signed. In the following example, we will sign certificates and add CRL URL for the server certificate:
```
/certificate
sign CA-Template
sign Client
sign Server ca-crl-host=192.168.88.1 name=ServerCA
```
Let`s check is the certificates are signed:
```
[admin@MikroTik] /certificate> print
Flags: K - private-key; L - crl; A - authority; T - trusted
Columns: NAME, COMMON-name, FINGERPRINT
# NAME         COMMON  FINGERPRINT
0  K AT  CA-Template  CAtemp  0c7aaa7607a4dde1bbf33deaae6be7bac9fe4064ba47d64e8a73dcefad6cfc38
1  K AT  Client       client  b3ff25ecb166ea41e15733a7493003f3ea66310c10390c33e98fe32364c3659f
2  KLAT  ServerCA     server  152b88c9d81f4b765a59e2302e01efd1fbf11ceeed6e59f4974e87787a5bb980
```
For a video example clickhere.
# Export Certificate
It is possible to export client certificates with keys and CA certificates in two formats - PEM or PCKS12.
Property | Description
----------------------
export-passphrase(stringDefault: none) | Passphrase that will be used for exported certificate private key encryption.
file-name(stringDefault: cert_export_[Certificate name].crt/key/pkcs12) | Exported certificate file name.
type(pem | pkcs12Default: pem) | Exported certificate type.In case of PEM, certificate will be exported with CRT extension, if export-passphrase is specified, also encrypted private KEY file will be exported.In case of PKCS12, certificate will be exported with P12 extension, if export-passphrase is specified, exported certificate will contain encryted private key.
Exported certificate type.
In case of PEM, certificate will be exported with CRT extension, if export-passphrase is specified, also encrypted private KEY file will be exported.
In case of PKCS12, certificate will be exported with P12 extension, if export-passphrase is specified, exported certificate will contain encryted private key.
```
/certificate
export-certificate CA-Template
export-certificate ServerCA export-passphrase=yourpassphrase
export-certificate Client export-passphrase=yourpassphrase
```
Exported certificates are available under the/filesection:
```
[admin@MikroTik] > file print
Columns: NAME, TYPE, SIZE, CREATION-TIME
# NAME                         TYPE        SIZE  CREATION-TIME
0  skins                        directory         jan/19/2019 00:00:04
1  flash                        directory         jan/19/2019 01:00:00
2  pub                          directory         jan/19/2019 02:42:16
3  cert_export_CA-Template.crt  .crt file   1119  jan/19/2019 04:15:21
4  cert_export_ServerCA.crt     .crt file   1229  jan/19/2019 04:15:42
5  cert_export_ServerCA.key     .key file   1858  jan/19/2019 04:15:42
6  cert_export_Client.crt       .crt file   1164  jan/19/2019 04:15:55
7  cert_export_Client.key       .key file   1858  jan/19/2019 04:15:55
```
# Import Certificate
To import certificates, certificates must be uploaded to a device using one of the file upload methods.
Certificates must be imported as a file.
Supported arePEM, DER, CRT, PKCS12 formats.
Property | Description
----------------------
name(stringDefault: file-name_number) | A certificate name that will be shown in the certificate manager
file-name(string) | A file name that will be imported
passphrase(stringDefault: none) | File passphrase if there is such
trusted(yes | noDefault: yes) | Addstrustedflag for imported certificate
```
[admin@MikroTik] > /certificate/import file-name=certificate_file_name name=name_example passphrase=file_passphrase
certificates-imported: 2
private-keys-imported: 1
files-imported: 1
decryption-failures: 0
keys-with-no-certificate: 0
[admin@MikroTik] > /certificate/print
Flags: K - PRIVATE-KEY; T - TRUSTED
Columns: NAME, COMMON-NAME
# NAME            COMMON-NAME
0 KT name_example    cert
1  T name_example_1  ca
```
# Settings
/certificate settingsallows configuring Certificate Revocation List (CRL) settings.
By default, CRL is not utilized, and certificates are not verified for revocation status.
Property | Description
----------------------
crl-download(yes | noDefault: no) | Whether to automatically download/update CRL
crl-store(ram | sytemDefault: ram) | Where to store downloaded CRL informationCRL will be automatically renewed every hour for certificates which have "trusted=yes" using http protocol (ldap and ftp is currently unsupported)
crl-use(yes | noDefault: no) | Whether to use CRL
Where to store downloaded CRL information
CRL will be automatically renewed every hour for certificates which have "trusted=yes" using http protocol (ldap and ftp is currently unsupported)
Anexampleon importing a root certificate.
# Let's Encrypt certificates
RouterOS v7 has Let's Encrypt (letsencrypt) certificate support for the 'www-ssl' service. To enable the Let's Encrypt certificate service with automatic certificate renewal, use the 'enable-ssl-certificate' command:
```
/certificate enable-ssl-certificate dns-name=my.domain.com
```
Note that the DNS name must point to the router and port TCP/80 must be available from the WAN. If the dns-name is not specified, it will default to the automatically generated/ip cloudname (ie.http://example.sn.mynetname.net)
# Different acme servers
Support has been added starting from 7.15beta7, you can use not only Let's Encrypt certificate service, but any other you like.
# Server properties
Property | Description
----------------------
directory-url(string) | ACME directory url.
eab-hmac-key(string) | HMAC key for ACME External Account Binding (optional).
eab-kid(string) | Key identifier (optional).
Key identifier (optional).
# Example:
```
/certificate/enable-ssl-certificate directory-url=https://acme.zerossl.com/v2/DV90 dns-name=mydomain.abc eab-hmac-key=4ac7xuxAdV4mIncwIIEhLjExsFZ4v1rWgDkX4SKXD25pMVtF85GZJYSF8UKXUOjzSr2g3-v4lhL57NHFaQ42Ff eab-kid=GHWaP2_Ghx73vcU8ricAKU
```
Watch avideoon Let's encrypt setup.
# SCEP
SCEP is using HTTP protocol and base64 encoded GET requests. Most of the requests are without authentication and cipher, however, important ones can be protected if necessary (ciphered or signed using a received public key).
SCEP client in RouterOS will:
The SCEP server supports the issuance of one certificate only. RouterOS supports also renew and next-ca options:
The client polls the server for any changes, if the server advertises that the next-ca is available, then the client may request the next CA or wait until CA almost expires and then request the next-ca.
The RouterOS client by default will try to use POST, AES, and SHA256 if the server advertises that. If the above algorithms are not supported, then the client will try to use 3DES, DES and SHA1, MD5.
SCEP certificates are renewed when 3/4 of their validity time has passed.
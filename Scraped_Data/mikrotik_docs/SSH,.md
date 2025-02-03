---
title: SSH
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/132350014/SSH,
crawled_date: 2025-02-02T21:09:27.682020
section: mikrotik_docs
type: documentation
---

* 1SSH Server1.1Properties1.2Enabling PKI authentication
* 2SSH Client2.1Simple log-in to remote host2.2Log-in from certain IP address of the router2.3Log-in using RSA public/private key2.4Executing remote commands
* 3SSH exec3.1Retrieve information
* 1.1Properties
* 1.2Enabling PKI authentication
* 2.1Simple log-in to remote host
* 2.2Log-in from certain IP address of the router
* 2.3Log-in using RSA public/private key
* 2.4Executing remote commands
* 3.1Retrieve information
# SSH Server
RouterOS has built in SSH (SSH v2) server that is enabled by default and is listening for incoming connections on port TCP/22. It is possible to change the port and disable the server underServicesmenu.
## Properties
Sub-menu:/ip ssh
```
/ip ssh
```
Property | Description
----------------------
allow-none-crypto(yes|no; Default:no) | Whether to allow connection if cryptographic algorithms are set to none.
always-allow-password-login(yes | no; Default:no) | Whether to allow password login at the same time when public key authorization is configured for a user.
ciphers(3des-cbc| aes-cbc | aes-ctr | aes-gcm | auto | null;Default:auto) | Allow to configure SSH ciphers.
forwarding-enabled(both | local | no | remote; Default:no) | Allows to control which SSH forwarding method to allow:no - SSH forwarding is disabled;local - Allow SSH clients to originate connections from the server(router), this setting controls also dynamic forwarding;remote - Allow SSH clients to listen on the server(router) and forward incoming connections;both - Allow both local and remote forwarding methods.
host-key-size(1024 | 1536 | 2048 | 4096 | 8192; Default:2048) | RSA key size when host key is being regenerated.
host-key-type(ed25519|rsa; Default:rsa) | Select host key type
strong-crypto(yes | no; Default:no) | Use stronger encryption, HMAC algorithms, use bigger DH primes and disallow weaker ones:use 256 and 192 bit encryption instead of 128 bits;disable null encryption;use sha256 for hashing instead of sha1;disable md5;use 2048bit prime for Diffie-Hellman exchange instead of 1024bit.
Allow to configure SSH ciphers.
* no - SSH forwarding is disabled;
* local - Allow SSH clients to originate connections from the server(router), this setting controls also dynamic forwarding;
* remote - Allow SSH clients to listen on the server(router) and forward incoming connections;
* both - Allow both local and remote forwarding methods.
* use 256 and 192 bit encryption instead of 128 bits;
* disable null encryption;
* use sha256 for hashing instead of sha1;
* disable md5;
* use 2048bit prime for Diffie-Hellman exchange instead of 1024bit.
Commands
Property | Description
----------------------
export-host-key(key-file-prefix) | Export public and private RSA/Ed25519 to files. Command takes two parameters:key-file-prefix- used prefix for generated files, for example, prefix 'my' will generate files 'my_rsa', 'my_rsa.pub' etc.passphrase- private key passphrase
import-host-key(private-key-file) | Import and replace private RSA/Ed25519 key from specified file. Command takes two parameters:private-key-file- name of the private RSA/Ed25519 key filepassphrase- private key passphrase
regenerate-host-key() | Generated new and replace current set of private keys (RSA/Ed25519) on the router. Be aware that previously imported keys might stop working.
Export public and private RSA/Ed25519 to files. Command takes two parameters:
* key-file-prefix- used prefix for generated files, for example, prefix 'my' will generate files 'my_rsa', 'my_rsa.pub' etc.
* passphrase- private key passphrase
* private-key-file- name of the private RSA/Ed25519 key file
* passphrase- private key passphrase
## Enabling PKI authentication
Example of importing public key for useradmin
Generate SSH keys on the client device(the device you will connect from). Upload the public SSH key to the router and import it.
```
/user ssh-keys import public-key-file=id_rsa.pub user=admin
```
# SSH Client
Sub-menu:/system ssh
```
/system ssh
```
## Simple log-in to remote host
It is able to connect to remote host and initiate ssh session. IP address supports both IPv4 and IPv6.
```
/system ssh 192.168.88.1
/system ssh 2001:db8:add:1337::beef
```
In this case user name provided to remote host is one that has logged into the router. If other value is required, thenuser=<username>has to be used.
```
/system ssh 192.168.88.1 user=lala
/system ssh 2001:db8:add:1337::beef user=lala
```
## Log-in from certain IP address of the router
```
/system ssh 192.168.88.1 src-address=192.168.89.2
/system ssh 2001:db8:add:1337::beef src-address=2001:db8:bad:1000::2
```
in this case, ssh client will try to bind to address specified and then initiate ssh connection to remote host.
## Log-in using RSA public/private key
Example of importing private key for useradmin
First, export currently generated SSH keys to a file:
```
/ip ssh export-host-key key-file-prefix=admin
```
Two filesadmin_rsaandadmin_rsa.pubwill be generated. The pub file needs to be trusted on the SSH server side (how to enable SSH PKI on RouterOS) The private key has to be added for the particular user.
```
/user ssh-keys private import user=admin private-key-file=admin_rsa
```
After the public key is installed and trusted on the SSH server, a PKI SSH session can be created.
```
/system ssh 192.168.1.1
```
Watch how to:
## Executing remote commands
To execute remote command it has to be supplied at the end of log-in line
```
/system ssh 192.168.88.1 "/ip address print"
/system ssh 192.168.88.1 command="/ip address print"
/system ssh 2001:db8:add:1337::beef "/ip address print"
/system ssh 2001:db8:add:1337::beef command="/ip address print"
```
For example, sending command"/ip address \n add address=1.1.1.1/24"to MikroTik router will fail.
```
"/ip address \n add address=1.1.1.1/24"
```
# SSH exec
Sub-menu:/system ssh-exec
```
/system ssh-exec
```
Commandssh-execis a non-interactive ssh command, thus allowing to execute commands remotely on a device via scripts and scheduler.
## Retrieve information
The command will return two values:
* exit-code: returns 0 if the command execution succeeded
* output: returns the output of remotely executed command
Example:Code below will retrieve interface status of ether1 from device 10.10.10.1 and output the result to "Log"
```
:local Status ([/system ssh-exec address=10.10.10.1 user=remote command=":put ([/interface ethernet monitor [find where name=ether1] once as-value]->\"status\")" as-value]->"output")
:log info $Status
```
Watch how toexecute commands through SSH.
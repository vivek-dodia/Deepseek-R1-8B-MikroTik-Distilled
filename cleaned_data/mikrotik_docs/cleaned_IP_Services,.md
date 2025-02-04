# Document Information
Title: IP Services
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/328229/IP+Services,

# Content
# Services
This section lists protocols and ports used by various MikroTik RouterOS services. It helps you to determine why your MikroTik router listens to certain ports, and what you need to block/allow in case you want to prevent or grant access to certain services.
The default services are:
Property | Description
----------------------
telnet | Telnet service
ftp | FTP service
www | Webfig HTTP service
ssh | SSH service
www-ssl | Webfig HTTPS service
api | API service
winbox | Responsible for Winbox tool access, as well as Tik-App smartphone app and Dude probe
api-ssl | API over SSL service
# Properties
Note that it is not possible to add new services, only existing service modifications are allowed.
Property | Description
----------------------
address(IP address/netmask | IPv6/0..128; Default: ) | List of IP/IPv6 prefixes from which the service is accessible.
certificate(name; default:none) | The name of the certificate used by a particular service. Applicable only for services that depend on certificates (www-ssl, api-ssl)
name(name; default:none) | Service name
port(integer: 1..65535; Default: ) | The port particular service listens on
To restrict Winbox service access to the device only from the192.168.88.0/24subnet, we have to configure the following:
```
[admin@MikroTik] > ip service set [find name~"winbox"] address=192.168.88.0/24
[admin@MikroTik] > ip service print
Flags: X - disabled, I - invalid
# NAME PORT ADDRESS CERTIFICATE
0 telnet 23
1 XI ftp 21
2 XI www 80
3 ssh 22
4 XI www-ssl 443 none
5 XI api 8728
6 winbox 8291 192.168.88.0/24
7 XI api-ssl 8729 none
```
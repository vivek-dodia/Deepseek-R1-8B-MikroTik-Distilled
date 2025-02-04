# Document Information
Title: WebFig
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/328131/WebFig,

# Content
# Introduction
WebFig is a web-based RouterOS utility that allows you to monitor, configure and troubleshoot the router. It is designed as an alternative of WinBox, both have similar layouts and both have access to almost any feature of RouterOS.
As Webfig is platform-independent, it can be used to configure a router directly from various devices without the need for software developed for specific platforms. In other words, there is no need to install additional software.
WebFig allows performing three basic actions:
# Connecting to a Router
As we already know from theFirst Time Configurationsection, the device by defaulthas usernameadminandno passwordconfigured. Simply open a Web browser and in the search bar type device IP address which by default is192.168.88.1.Be sure your device has IP address from the same network, for example, 192.168.88.2 otherwise Layer3 communication will not work.
# Enable HTTPS
For HTTPS to work properly, you need to specify a valid certificate that WebFig can use. You can use a certificate that is issued by a trusted Certificate Authority (CA) or you can create your own root CA and generate self-signed certificates.
To generate your own certificates and enable HTTPS access, you must configure the following:
Create your own root CA on your router and sign it
```
[admin@MikroTik] > certificate add name=local-cert common-name=local-cert key-usage=key-cert-sign,crl-sign
[admin@MikroTik] > certificate sign local-cert
progress: done
```
Create a new certificate for WebFig (non-root certificate)
```
[admin@MikroTik] > certificate add name=webfig common-name=192.168.88.1
[admin@MikroTik] > certificate sign webfig
progress: done
[admin@MikroTik] > certificate print
Flags: K - private-key; A - authority; T - trusted
Columns:NAME        COMMON-NAME     FINGERPRINT
0  KAT  local-cert  local-cert      9b6363d033c4b2e6893c340675cfb8d1e330977526dba347a440fabffd983c5d
1  KAT  webfig      192.168.88.1    9f84ac2979bea65dccd02652056e5559bcdf866f8da5f924139d99453402bd02
```
Enablewww-ssland specify to use the newly created certificate for WebFig
```
[admin@MikroTik] > ip service
set www-ssl certificate=webfig disabled=no
```
You can now visithttps://192.168.88.1and securely configure your router.
# The "Terminal"
The "Terminal" or Command Line Interface (CLI) in WebFig is located in the top right corner. It offers the same functionality as the "New Terminal" in the WinBox GUI.
# Skins
WebFigDesign Skinis a handy tool to make the interface more user-friendly. It is not a security tool. If the user has sufficient rights it is possible to access hidden features by other means.
# Designing skins
If the user has sufficient permissions (the group has the policy "policy" and "sensitive" to edit permissions)Design Skinbutton becomes available. Pressing that toggle button will open interface editing options.
To prevent the user from accessing theDesign Skinmenu, disable policy "policy" and "sensitive" under the user group configuration.
Possible operations are:
# Skin design examples
If you need to limit the user for some services
Add a limit to the RADIUS Service.
The result will be only those services, that are pointed in the "Limit" field.
# Using skins
To use skins you have to assign the skin to the group. When that is done, users of that group will automatically use the selected skin as their default when logging into WebFig or WinBox.
```
/user/group/set your_group_name skin=your_skin
```
If it is required to use created skin on another router you can copy files totheskinsfolder on the other router. On the new router, it is required to add copied skin to the user group to use it.
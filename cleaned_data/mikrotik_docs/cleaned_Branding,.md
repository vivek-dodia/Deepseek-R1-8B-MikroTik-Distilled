# Document Information
Title: Branding
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/69664784/Branding,

# Content
RouterOS allows slight system customization with the help of a branding package (modify default configuration, LCD logo, WebFig homepage, etc.).
This is a special system package, which you can generate from within yourmikrotik.comaccount, in the account section "Branding maker". The resulting file will have a .dpk extension and can be installed by all the same means as an .npk package.
To install the package on a router, branding package has to upload to it and then a router has to reboot, Netinstall tool can be used for the same effect.
The generated package can be installed in any RouterOS version.
# Options
Options that can be configured using a branding package:
# Custom files
Custom files such as the WebFig login page, WebFig logo, hotspot, skins, Default configuration, LCD logo, Custom files and CAPs mode script can be included in the branding package.
# WebFig login page
The WebFig login page is a customized default RouterOS login interface that appears when accessing the router's IP address. This page can be customized to meet branding or functional requirements.
Customization Files:
```
/index2.html
```
```
/assets/style.css
```
```
/assets/script.js
```
Required Elements for thescript.js:
```
script.js
```
```
<form id="login">
```
```
<input id="name" data-defaultuser="admin">
```
```
admin
```
```
<input id="password">
```
```
<div id="error">
```
```
index2.html
```
# WebFig logo
RouterOS WebFig page (configuration page) logo. To overwrite the MikroTik logo on the WebFig login page, upload your custom logo named "mikrotik_logo.png".
# hotspot
Hotspot login page logo. The file must be named "logobottom.png".
# skins
# Default configuration
A RouterOS default configuration file that will override RouterOS default configuration. This configuration will persist even after a RouterOS reset. Factory passwords can be reapplied using the read-only variables$defconfPasswordand$defconfWifiPassword(access to factory passwords is available starting RouterOS 7.10).
# LCD logo
LCD logo will be displayed on devices equipped with LCD screen. A Logo size cannot be larger than 160px width and 72px height. CCR1xxx series has white (0xffffff) background, 2011 series have black (0x000000) background.
# Custom files
Custom files will be copied into a folder named "branding" and will be accessible from within RouterOS.
# CAPs mode script
A RouterOS CAPs mode script that will override RouterOS default CAPs mode script. It is possible to reapply the factory passwords by utilizing the read-only variables$defconfPasswordand$defconfWifiPassword(available starting from RouterOS 7.15).
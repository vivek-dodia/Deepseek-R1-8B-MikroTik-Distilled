---
title: Branding
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/69664784/Branding,
crawled_date: 2025-02-02T21:09:16.459830
section: mikrotik_docs
type: documentation
---

RouterOS allows slight system customization with the help of a branding package (modify default configuration, LCD logo, WebFig homepage, etc.).
This is a special system package, which you can generate from within yourmikrotik.comaccount, in the account section "Branding maker". The resulting file will have a .dpk extension and can be installed by all the same means as an .npk package.
To install the package on a router, branding package has to upload to it and then a router has to reboot, Netinstall tool can be used for the same effect.
The generated package can be installed in any RouterOS version.
# Options
Options that can be configured using a branding package:
* Router name- branding package name, device identity andplatform namein RouterOS, can only be one word, don't use spaces or special characters;
* Company URL-value that appears in the console when you connect to RouterOS device;
* Manual URL- documentation link, which can be opened inWebFig;
* ASCII Logo-a text logo that is shown when logging into the command line interface, i.e. Telnet, SSH, WinBox Terminal. A logo can be created in thebranding makeror copied from any other plaintext editor. A logo height cannot be larger than 8 lines, width is not limited, but note that in anarrow terminal window a logo might be distorted.
* Hide "Mikrotik" from SNMP information-MikroTik name will be hidden in SNMP information;
* Do not run script on install- do not run Default configuration script on branding package install;
* Hide Default configuration prompt- hide Default configuration prompt after configuration reset(available starting from RouterOS 7.15)
* Hide default caps-mode-script- hide default caps-mode-script(available starting from RouterOS 7.15)
# Custom files
Custom files such as the WebFig login page, WebFig logo, hotspot, skins, Default configuration, LCD logo, Custom files and CAPs mode script can be included in the branding package.
### WebFig login page
The WebFig login page is a customized default RouterOS login interface that appears when accessing the router's IP address. This page can be customized to meet branding or functional requirements.
* Customization Files:/index2.html: Main template for the login page./assets/style.css:  MikroTik RouterOS stylesheet./assets/script.jsis responsible for handling the login functionality andcontains code that gives the button interactivity.
* Required Elements for thescript.js:Form for Login:<form id="login">Username Field:<input id="name" data-defaultuser="admin">Theadminvalue can be changed to another username or left blank.Password Field:<input id="password">Error Display Section:<div id="error">
* Here is an example of a user-customized login page with a "Show Password" button, achieved using a modifiedindex2.htmlalong with additionalcssandjsfiles.The HTML file must be named "index2.html" and should use properly nested HTML to ensure compatibility with all browsers.
* The uploaded images or JavaScript files must reference to the same path as the index file, no custom folder names can be used.
Customization Files:
* /index2.html: Main template for the login page.
* /assets/style.css:  MikroTik RouterOS stylesheet.
* /assets/script.jsis responsible for handling the login functionality andcontains code that gives the button interactivity.
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
* Form for Login:<form id="login">
* Username Field:<input id="name" data-defaultuser="admin">Theadminvalue can be changed to another username or left blank.
* Password Field:<input id="password">
* Error Display Section:<div id="error">
```
<form id="login">
```
```
<input id="name" data-defaultuser="admin">
```
* Theadminvalue can be changed to another username or left blank.
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
### WebFig logo
RouterOS WebFig page (configuration page) logo. To overwrite the MikroTik logo on the WebFig login page, upload your custom logo named "mikrotik_logo.png".
### hotspot
Hotspot login page logo. The file must be named "logobottom.png".
### skins
### Default configuration
A RouterOS default configuration file that will override RouterOS default configuration. This configuration will persist even after a RouterOS reset. Factory passwords can be reapplied using the read-only variables$defconfPasswordand$defconfWifiPassword(access to factory passwords is available starting RouterOS 7.10).
### LCD logo
LCD logo will be displayed on devices equipped with LCD screen. A Logo size cannot be larger than 160px width and 72px height. CCR1xxx series has white (0xffffff) background, 2011 series have black (0x000000) background.
### Custom files
Custom files will be copied into a folder named "branding" and will be accessible from within RouterOS.
### CAPs mode script
A RouterOS CAPs mode script that will override RouterOS default CAPs mode script. It is possible to reapply the factory passwords by utilizing the read-only variables$defconfPasswordand$defconfWifiPassword(available starting from RouterOS 7.15).
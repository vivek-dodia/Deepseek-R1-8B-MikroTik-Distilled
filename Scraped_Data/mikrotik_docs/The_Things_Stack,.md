---
title: The Things Stack
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/67633276/The+Things+Stack,
crawled_date: 2025-02-02T21:14:24.719985
section: mikrotik_docs
type: documentation
---

* 1Selecting a region
* 2Registering gateway
* 3UDP protocol gateway registration3.1UDP scenario RouterOS settings
* 4LNS and CUPS protocol gateway registration4.1LNS scenario RouterOS settings4.2CUPS scenario RouterOS settings
* 5Verification
* 3.1UDP scenario RouterOS settings
* 4.1LNS scenario RouterOS settings
* 4.2CUPS scenario RouterOS settings
# Selecting a region
The Things Stackis a new version of The Things network.
Choose your region and login with The Things network account or other credentials.
# Registering gateway
Once logged in, navigate to "Go to gateways":
Register a gateway by clicking on the "+ Register gateway" button:
# UDP protocol gateway registration
Fill in the blank spaces. InputGateway EUI. Make sure to select a correct frequency plan. Do not enable "Require authenticated connection" option (it is used for LNS and CUPS)!
In RouterOS,Gateway EUIvalue can be found under "IoT>LoRa>Devices>Gateway ID"):
For additional information check theirdocumentationpage.
## UDP scenario RouterOS settings
Double-check that the correct TTN server is selected by the LoRa device (in RouterOS) and that the server setting uses "UDP" protocol:
# LNS and CUPS protocol gateway registration
Fill in the blank spaces. InputGateway EUI. Make sure to select a correct frequency plan. Enable "Require authenticated connection" and the follow-up (for LNS) "Generate API key for LNS" and (for CUPS) "Generate API key for CUPS" options:
In RouterOS,Gateway EUIvalue can be found under "IoT>LoRa>Devices>Gateway ID":
After clicking on "Register gateway" button, you should be prompted to download the keys. Download them.
To view LNS and CUPS keys, inspect download files. LNS key should also be visible under the"LoRa Basics Station LNS authentication Key" field:
For additional information check theirdocumentationpage.
## LNS scenario RouterOS settings
Make sure that the correct TTN server is selected, that the correct port is configured (TTN expects LNS over 8887), that LNS protocol is chosen, that the LNS key (from the "LoRa Basics Station LNS authentication Key" field) is input and that "SSL" checkbox is enabled:
The last step is to download and importRoot Certificates. The page has links to the required file.
After the certificate file was downloaded, drag and drop it into the RouterOS file menu and import the certificate list:
This should make the certificate list trusted:
## CUPS scenario RouterOS settings
Make sure that the correct TTN server is selected, that the correct port is configured (TTN expects CUPS over 443), that CUPS protocol is chosen, that the CUPS key is input and that "SSL" checkbox is enabled:
The last step is to download and importRoot Certificates. The page has links to the required file.
After the certificate file was downloaded, drag and drop it into the RouterOS file menu and import the certificate list:
This should make the certificate list trusted:
# Verification
If everything is configured in correctly, right after you enable the LoRa interface in RouterOS ("IoT>LoRa>Devices>Enable"):
You should see the gateway connection "Live data" update:
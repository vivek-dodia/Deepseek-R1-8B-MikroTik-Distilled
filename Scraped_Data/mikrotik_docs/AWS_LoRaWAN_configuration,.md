---
title: AWS LoRaWAN configuration
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/232816782/AWS+LoRaWAN+configuration,
crawled_date: 2025-02-02T21:14:18.154613
section: mikrotik_docs
type: documentation
---

* 1AWS - Registering the gateway1.1Step 1 - add gateway1.2Step 2 - configure your gateway
* 2RouterOS - Connecting the gateway2.1Uploading and importing certificates2.2Server configuration2.2.1LNS scenario2.2.2CUPS scenario2.3Connection verification
* 1.1Step 1 - add gateway
* 1.2Step 2 - configure your gateway
* 2.1Uploading and importing certificates
* 2.2Server configuration2.2.1LNS scenario2.2.2CUPS scenario
* 2.3Connection verification
* 2.2.1LNS scenario
* 2.2.2CUPS scenario
Before we proceed with the settings, you need to create an account in the AWS system. You can find more information on how to do that following thislink.
After you are logged-in, go toServices>IoT Coresection on the portal.
# AWS - Registering the gateway
The first step is to register the LoRaWAN gateway.
Navigate to theGatewayssection (underLPWAN devices).
Click on the "Add gateway" button.
## Step 1 - add gateway
* Input the gateway's EUI;
* Select device's frequency band;
* Configure optional fields if required;
Finish the step by clicking on the "Add gateway" once again.
In RouterOS settings, gateway's EUI and frequency plan can be checked underIoT>LoRa>Devicestab:
## Step 2 - configure your gateway
* Generate a gateway certificate ("Create certificate" button), and download the certificate file and private key files ("Download certificate files" button);
* Copy CUPS and LNS endpoints and download server trust certificates ("Download server trust certificates" button);
* Add suggested gateway permissions;
Finish the step by clicking on "Submit".
You will be redirected to the page where your newly created gateway should appear.
# RouterOS - Connecting the gateway
## Uploading and importing certificates
Before we proceed with the setup, you need to downloadAmazon Root CAand upload it, together with the gateway certificate file and its key, into the RouerOS file list menu:
After the files were uploaded, import the certificates, one by one (underSystem>Certificates):
Make sure to upload the gateway certificate first and then its key (so that the gateway certificate has both K-key and T-trusted flags present). In the end, you should have all 3 file imported, like so:
## Server configuration
### LNS scenario
Navigate to theIoT>LoRa>Serverstab and add a new server:
* Name the server;
* Input LNS endpoint address (without "wss://" and ":443");
* Select LNS protocol;
* Change port to "443";
* Enable SSL checkbox;
* Select gateway certificate.
```
wss://
```
```
:443
```
Make sure to apply newly configured server underIoT>LoRa>Devicestab:
And then,enablethe LoRa interface.
### CUPS scenario
Navigate to theIoT>LoRa>Serverstab and add a new server:
* Name the server;
* Input CUPS endpoint address (without "https://" and ":443");
* Select CUPS protocol;
* Change port to "443";
* Enable SSL checkbox;
* Select gateway certificate.
```
https://
```
```
:443
```
Make sure to apply newly configured server underIoT>LoRa>Devicestab:
And then,enablethe LoRa interface.
## Connection verification
If everything is configured correctly, you should see "connected" status on the AWS portal:
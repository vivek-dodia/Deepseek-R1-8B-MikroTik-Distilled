# Document Information
Title: AWS LoRaWAN configuration
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/232816782/AWS+LoRaWAN+configuration,

# Content
Before we proceed with the settings, you need to create an account in the AWS system. You can find more information on how to do that following thislink.
After you are logged-in, go toServices>IoT Coresection on the portal.
# AWS - Registering the gateway
The first step is to register the LoRaWAN gateway.
Navigate to theGatewayssection (underLPWAN devices).
Click on the "Add gateway" button.
# Step 1 - add gateway
Finish the step by clicking on the "Add gateway" once again.
In RouterOS settings, gateway's EUI and frequency plan can be checked underIoT>LoRa>Devicestab:
# Step 2 - configure your gateway
Finish the step by clicking on "Submit".
You will be redirected to the page where your newly created gateway should appear.
# RouterOS - Connecting the gateway
# Uploading and importing certificates
Before we proceed with the setup, you need to downloadAmazon Root CAand upload it, together with the gateway certificate file and its key, into the RouerOS file list menu:
After the files were uploaded, import the certificates, one by one (underSystem>Certificates):
Make sure to upload the gateway certificate first and then its key (so that the gateway certificate has both K-key and T-trusted flags present). In the end, you should have all 3 file imported, like so:
# Server configuration
# LNS scenario
Navigate to theIoT>LoRa>Serverstab and add a new server:
```
wss://
```
```
:443
```
Make sure to apply newly configured server underIoT>LoRa>Devicestab:
And then,enablethe LoRa interface.
# CUPS scenario
Navigate to theIoT>LoRa>Serverstab and add a new server:
```
https://
```
```
:443
```
Make sure to apply newly configured server underIoT>LoRa>Devicestab:
And then,enablethe LoRa interface.
# Connection verification
If everything is configured correctly, you should see "connected" status on the AWS portal:
# Thread Information
Title: Thread-214191
Section: RouterOS
Thread ID: 214191

# Discussion

## Initial Question
Here is a typical setup: (I hope this is enough, else I will have to reset the router and send the .RSC here)ISP Modem (LAN1) --> Mikrotik Router (Ether1)The ISP modem:has DHCP server enabled - capable of providing IP to any devices that would connect to it.The Mikrotik Router:Bridge Name: Bridge1Bridge1 Ports: Ether1, Wifi1DHCP Client: Bridge1 (able to acquire IP from the ISP Modem)I just don't have records of the version of the ROS I had, but when it was still working, any devices that connects to the WIFI1 gets an IP address from the ISP Modem. As of now, only the DHCP Client can get the IP. The devices that connects to WIFI isn't able to get an IP. When I accessed the ISP modem, it can detect the device the is connected wireless from WIFI1 but it has no IP. If I connect the same device wirelessly to the ISP modem, the device is able to get an IP from the ISP modem. My current ROSversion is 7.17. Please advise. Thank you! ---

## Response 1
That's not a lot to go about. What model? What was the working version? Do you do capsman? Is the bridge using vlan-filtering? If so are the interfaces tagged or not? Do you have firewall rules that could get in the way?I think the config with the sensitive bits removed would be a good thing here. ---

## Response 2
I don't know the answer to the questions. I better do the factory reset and setup the router again. I'll send over the config shortly. ---

## Response 3
For some reason when I do the command to export a file to create the .rsc, the file only contains the model and serial number. I attached the backup file instead. ---

## Response 4
I just found out that it does work in this configuration (newly reset). It would only mean that there is something wrong with my long time configuration. ---
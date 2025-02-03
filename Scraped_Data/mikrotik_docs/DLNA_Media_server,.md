---
title: DLNA Media server
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/237699479/DLNA+Media+server,
crawled_date: 2025-02-02T21:15:30.767450
section: mikrotik_docs
type: documentation
---

DLNA is a set of protocols that enables networked devices to share digital media, including videos, photos, and music. Central to the operation of DLNA is the UPnP (Universal Plug and Play) architecture, which facilitates the discovery and control of network devices.
DLNA and UPnP work in tandem to provide a seamless media sharing experience. UPnP supports device discovery and control on the network through protocols like the Simple Service Discovery Protocol (SSDP) and others such as SOAP (Simple Object Access Protocol) for control messages and XML for device and service descriptions. In the context of DLNA, UPnP serves as the foundation, allowing various devices like TVs, computers, and mobile devices to connect and share media content efficiently.
In RouterOS, enable the media server and share movies or music with your household media devices, such as TVs or player apps in your PC, such as the popular VLC.
# Server settings
Property | Description
----------------------
allowed-hostname | To restrict access to specific hostnames.
allowed-ip | To limit access to specified IP addresses
friendly-name | The name that will be displayed for the DLNA server on the network.
interface | Specifies the network interface that the DLNA server will use
path | The file path where the media content is stored and will be served from.
disabled | Specifies if entry is disabled
# Configuration examples
Creating a DLNA server
```
/ip media add friendly-name=Mikrotik interface=bridge1 path=usb1
```
Creating multiple DLNA servers with limitations. Usage example - Limit children's TV access only to child-friendly media, located in folder "usb1/kids"
```
/ip media add friendly-name=adults interface=bridge1 path=usb1/adults allowed-hostname=ADULTS_TV
/ip media add friendly-name=kids interface=bridge1 path=usb1/kids allowed-hostname=KIDS_TV
```
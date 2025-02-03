---
title: Container - HomeAssistant
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/204341276/Container+-+HomeAssistant,
crawled_date: 2025-02-02T21:15:25.122393
section: mikrotik_docs
type: documentation
---

* 1Introduction
* 2Summary
* 3Container configuration3.1Container mode3.2Networking3.3Environment variables and mounts3.4Getting image3.5Starting the container3.6Home-Assistant setup
* 4Resources
* 3.1Container mode
* 3.2Networking
* 3.3Environment variables and mounts
* 3.4Getting image
* 3.5Starting the container
* 3.6Home-Assistant setup
# Introduction
The introduction of the container feature into the RouterOS made it possible to run all kinds of servers for all sorts of tasks inside the router. This is especially relevant for people, who want to reduce the number of devices in their network. Instead of running a server on a separate device/machine, why not run it inside the router?
In this guide, we will showcase how to install and hostHome-Assistantserver on RouterOS.
Home-Assistant is a very popular platform that is used to collect statistics from different sensors and supports differentintegrations.
# Summary
Make sure to study ourcontainerguide before proceeding with the configuration. Make sure to check thedisclaimerandrequirementssections to understand all the risks and necessary steps you might be required to do.
You can find supported architectures by following thelink.
At the time, when the guide was published,home-assistantimage was available for ARM32, ARM64, and AMD64 (CHR and x86) devices.
Based on the information from theirsite, recommended minimal requirements are:
* 2 GB RAM
* 32 GB Storage
Recommended does not mean set in stone, and we will be running this onL009UiGSthat has 512 MB RAM and a USB slot for the required storage. It is advised using recommended hardware specifications, but for testing, and low amounts of data, you can get by with 512+ MB RAM.
# Container configuration
Sub-menu:/container
```
/container
```
note:containerpackage is required.
## Container mode
Enable container mode:
```
/system/device-mode/update container=yes
```
You will need to confirm the device-mode with a press of the reset button, or a cold reboot, if using container on X86.
## Networking
Add veth interface:
```
/interface/veth/add name=veth2 address=172.19.0.2/24 gateway=172.19.0.1
```
Create a bridge for both containers and add veth interfaces to it:
```
/interface/bridge/add name=ha
/ip/address/add address=172.19.0.1/24 interface=ha
/interface/bridge/port add bridge=ha interface=veth2
```
Forward TCP 8123 for home-assistant management (where 192.168.88.1 is the device's LAN IP address) if NAT is required (optional):
```
/ip firewall nat add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=8123 protocol=tcp to-addresses=172.19.0.2 to-ports=8123
```
## Environment variables and mounts
Per the home-assist documentation, define mounts for the configuration files (where,/usb1is our external USB storage folder):
```
/usb1
```
```
/container mounts add dst=/config name=ha_config src=/usb1/ha_config
```
Create an environmental variable for home-assistant:
```
/container envs add key=TZ name=ha_env value=America/Los_Angeles
```
## Getting image
To simplify the configuration, we will get the images from an external library.
Make sure that you have "Registry URL" set accordingly, limit RAM usage (if necessary), and set up a directory for the images:
```
/container/config/set registry-url=https://registry-1.docker.io tmpdir=/usb1/pull
```
Pull home-assistant image and wait for it to be extracted:
```
/container/add remote-image=homeassistant/home-assistant:latest interface=veth2 root-dir=/usb1/ha mounts=ha_config envlist=ha_env logging=yes
```
After running the command, RouterOS should start "extracting" the package. Check "File System" for newly created folders and monitor container status with the command/container/print.
```
/container/print
```
## Starting the container
After you make sure that the container has been added and the status changed tostatus=stoppedafter using/container/print→ you can initiate it:
```
status=stopped
```
```
/container/print
```
```
/container/start 0
```
## Home-Assistant setup
Open your preferred web browser and access the Home-Assistant management portal by specifying management port ":8123":
Proceed with the setup. More information is explained in theHome-Assistant onboarding guide.
# Resources
Just running theHome Assistanton L009 (without any load/traffic) takes up ~300 MB of RAM:
```
/system resource print
                   uptime: 4m27s
                  version: 7.13.3 (stable)
               build-time: Jan/24/2024 13:16:46
         factory-software: 7.10
              free-memory: 143.0MiB
             total-memory: 448.0MiB
                      cpu: ARM
```
With the load, it will increase, but for testing, on this specific board, it should be enough.
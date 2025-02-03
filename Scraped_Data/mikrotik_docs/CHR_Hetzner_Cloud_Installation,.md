---
title: CHR: Hetzner Cloud Installation
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/263749814/CHR+Hetzner+Cloud+Installation,
crawled_date: 2025-02-02T21:08:56.629497
section: mikrotik_docs
type: documentation
---

Hetzner Cloudis a cloud computing platform that allows users to run virtual machines (VMs) in the cloud. It offers scalable infrastructure and a range of pre-configured Linux distributions. However, for those needing advanced networking features, Hetzner Cloud is also a great platform for deployingRouterOS CHR (Cloud Hosted Router).CHR is a MikroTik product that provides a fully functional RouterOS installation in a virtual environment, ideal for cloud-based routing, VPN services, and other network management tasks. By running RouterOS CHR on Hetzner Cloud, users can leverage powerful networking tools with the flexibility and scalability of a cloud environment.
* Create a Hetzner Cloud ServerBegin by creating a new server on Hetzner Cloud. Any of the available server options will work.
* Activate Rescue SystemIn the Hetzner Cloud admin interface, activate theEnable Rescuesystem by selecting"ENABLE RESCUE & POWER CYCLE"Choose 'linux64' as the Rescue OS.The system will display a username and password. Use these credentials to log into the rescue system via SSH.
* Install CHR (Cloud Hosted Router)Once logged into the rescue system, download the CHRRAWdisk image and write it over the system disk of the cloud server using the following command:curl -Lhttps://download.mikrotik.com/routeros/7.15.3/chr-7.15.3.img.zip| funzip | dd of=/dev/sda bs=1M
Create a Hetzner Cloud ServerBegin by creating a new server on Hetzner Cloud. Any of the available server options will work.
Activate Rescue System
* In the Hetzner Cloud admin interface, activate theEnable Rescuesystem by selecting"ENABLE RESCUE & POWER CYCLE"
* Choose 'linux64' as the Rescue OS.
* The system will display a username and password. Use these credentials to log into the rescue system via SSH.
Install CHR (Cloud Hosted Router)
* Once logged into the rescue system, download the CHRRAWdisk image and write it over the system disk of the cloud server using the following command:
* curl -Lhttps://download.mikrotik.com/routeros/7.15.3/chr-7.15.3.img.zip| funzip | dd of=/dev/sda bs=1M
Reboot the Server
After the installation is complete, reboot the server by issuing therebootcommand.
```
reboot
```
Make sure to keep your RouterOS updated and follow best security practices to maintain the safety and performance of your server.
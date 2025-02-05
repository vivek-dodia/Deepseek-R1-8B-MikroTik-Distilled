# Repository Information
Name: mikrotik-router

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/melon-branding/mikrotik-router.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: README.MD
================================================
![Melon Branding](img/melonbrandinglogo.png)
# MikroTik Instruction
This document might help you to understand how to setup some part of the MikroTik router.
## How To Add New Device
The way we adding new device to the setup is divided by its type:
* Wired (any devices that plug cable directly to the MikroTik router)
* Wireless (any devices that connect to the MikroTik router through its WiFi)
### Wired (Cable)
TBC
### Wireless (WiFi)
![DHCP Server Menu](img/dhcpserverleases.png)
- Click `IP (1) -> DHCP Server (2)`, to open DHCP Server window.
- Click `Lease (3)` tab, and you will see *leases* list like above image.
#### Action Menu (4)
- `+` for creating new lease
- `-` for deleting selected lease
- `✓` for enabling selected lease
- `x` for disabling selected lease
#### Lease example (5)
From the image above,we can see
- `Sisi Laptop` as the *comment*
- `192.168.200.6` as the IP Address that we planned to give it to the device
- `38:00:25:4B:21:39` as the **Wifi MAC Address/Physical Address** of the device
![DHCP Lease Detail Example](img/newdhcplease.png)
#### To create new list
1. Click `+` action menu
2. Set planned *address* with prefix `192.168.200.`, the last number can be range from `2` to `254` that available OR
   have not been assigned yet to any device. For example `192.168.200.6`
   was assigned to `Sisi Laptop`, so you can't use it to any other device.
3. Set the Wifi MAC Address/Physical of the target device. Don't know how to get one? Google it! 😊
4. To name the lease on the list, you need to put comment on top of it. Click the `Comment` button to enter one.
5. A simple way to replicate any *lease* is to select it and then click the `Copy` button. New window will be appeared
   and you can change the IP Address and MAC Address accordignly
#### Important Notes
- One IP will only serve for one device. Which means, once it is assigned to another device it should not be available
  for any other devices.
- Disabling a *lease* will make the device not able to get the IP Address. Not having IP Address means no internet for
  the device.
- Either deleting a *lease*, it always better to disable it and create a new one. Unless, you already know that the
  device will not be connected again to the network.
## How To Manage Bandwidth
![Queues List](img/queueslist.png)
- Click `Queues (1) -> Simple Queues (2)`, it will show list like the above.
- These queues will control the bandwidth for every *IP Address*.
![Queues Detail General](img/queuedetail1.png)
1. Select and double-click it will pop new window for its detail. You can put:
    - `Name` to tag the *queue* on the list,
    - `Target` as the IP Address that its bandwidth will be limited,
    - `Max Limit (Target Upload)` as maximum bandwidth for upload in Mega-Bit per second,
    - `Max Limit (Target Download)` as maximum bandwidth for download in Mega-Bit per second.
2. Dst (Destination) should be set to `ether1`, as `ether1` is our cable to connect to the main router (at the time I
   write this is Biznet router) which connected to the Internet.
![Queues Detail Advanced](img/queuedetail2.png)
1. Change to `Advanced` tab to change some of other settings.
2. These, `Target Upload` and `Target Download` will be the *IP Address*
   floor limit (not minimum, because bandwidth can be lower than these numbers sometime).
3. Priority starts from 1 (highest) and 8 (lowest).
#### Important Notes
- Max limit is the maximum bandwidth for the given IP Address
- Target Upload/Download is the minimum bandwidth for the given IP Address
- Any bandwidth limit will be fulfilled when the bandwidth is provided from the main Router (e.g. You subscribe Biznet
  for 150 Mega-Bit per second, you can only use up to 150 Mega-Bit in total)
- Mega-Bit = 1/8 Mega-Bytes.
- `Queues` = bandwidth management, assigning IP Address to have a bandwidth limit.
- `Leases` = connection management, assigning MAC/Physical Address to an IP Address.
## Credits
[MikroTik](https://mikrotik.com/)
© 2021 [Melon Branding](http://melonbranding.com/). All rights reserved.
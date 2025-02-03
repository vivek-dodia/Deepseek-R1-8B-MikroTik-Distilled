---
title: CHR: installing on VirtualBox
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/262864931/CHR+installing+on+VirtualBox ,
crawled_date: 2025-02-02T20:25:20.309827
section: mikrotik_docs
type: documentation
---

# CHR VirtualBox installation.Video instruction
* Download VirtualBox: Install the latest version of VirtualBox from the official website.
* Download CHR Image: Download and unpack the latest Stable or Testing version of the CHR (Cloud Hosted Router) VDI image from theMikroTik website.
Download VirtualBox: Install the latest version of VirtualBox from the official website.
Download CHR Image: Download and unpack the latest Stable or Testing version of the CHR (Cloud Hosted Router) VDI image from theMikroTik website.
## Step 1: Create a New Virtual Machine
* Launch the VirtualBox application.
* Create a New VM:Click onNewto create a new virtual machine.
Launch the VirtualBox application.
Create a New VM:
* Click onNewto create a new virtual machine.
Click onNewto create a new virtual machine.
* Name and Operating System:
* Name and Operating System:
* Name: Enter a name for your VM (e.g., MikroTik_CHR).Type: SelectLinux.Version: SelectOther Linux (64-bit).
* Name: Enter a name for your VM (e.g., MikroTik_CHR).Type: SelectLinux.Version: SelectOther Linux (64-bit).
* Name: Enter a name for your VM (e.g., MikroTik_CHR).
* Type: SelectLinux.
* Version: SelectOther Linux (64-bit).
Name: Enter a name for your VM (e.g., MikroTik_CHR).
Version: SelectOther Linux (64-bit).
* ClickNext.
* ClickNext.
ClickNext.
## Step 2: Configure Memory Size
* Memory Size: Allocate memory for the VM. It is recommended to allocate at least 256 MB of RAM (since RouterOS 7.15.1).
* Processors:Select the desired quantity of CPUs.
* ClickNext.
## Step 3: Create a Virtual Hard Disk
* Virtual Hard Disk:Select "Use an existing Hard Disk File"Add the downloaded VDI image fileClickChoose.
* Select "Use an existing Hard Disk File"
* Add the downloaded VDI image file
* ClickChoose.
* ClickNext.
* ClickNext.
Check the settings and clickFinish.
## Step 4: Configure Virtual Machine Settings
* Settings: Select your newly created VM and click onSettings.
* System: Go to theSystemtab and uncheckFloppy,Opticalin the Boot Order section.
* Processors:Go to theProcessortab.Select the desired quantity of CPUs.
* Network:Go to theNetworktab.
* Go to theProcessortab.
* Select the desired quantity of CPUs.
* Go to theNetworktab.
* Adapter 1: Enable the network adapter and attach it toBridged AdapterorNAT(depending on your network setup).
* Adapter 1: Enable the network adapter and attach it toBridged AdapterorNAT(depending on your network setup).
## Step 5: Start the Virtual Machine
* Start VM: ClickStartto boot your new virtual machine.
* Login: After the VM reboots, you will see the CHR login prompt. The default login credentials are:Username:adminPassword: (blank)
* Username:admin
* Password: (blank)
```
admin
```
* Initial Configuration: Configure the CHR as per your network requirements using the MikroTik CLI or WebFig.
Congratulations! You have successfully installed MikroTik CHR on VirtualBox. You can now proceed with configuring your network settings and using the full features of MikroTik RouterOS.
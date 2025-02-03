---
title: CHR Vultr installation
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/146997259/CHR+Vultr+installation,
crawled_date: 2025-02-02T21:08:59.393287
section: mikrotik_docs
type: documentation
---

Vultr has more thantwo dozen data center locationswhere you can choose to deploy MikroTik CHR for the bestthroughput and latency.Follow these steps to install MikroTik CHR at Vultr.
# Step 1: Deploy a server in rescue mode
In this step, you'll deploy a new server at Vultr with SystemRescue, a bootable Linux ISO.
* Deploya newCloud Computeinstance.
* Choose the location with the best performance for your needs. You can use Vultr'snetwork-looking glassto test the throughput and latency of any location.
* Select theISO Librarytab in theServer Imagesection.
* ChooseSystemRescue x64.
* Choose a server size withenough bandwidth allowancefor your requirements.
* Give the server a hostname, and a label, and then clickDeploy Now.
When the server finishes deploying, proceed to the next step.
# Step 2: Write the CHR image to the disk
* In your web browser, navigate to theMikroTik download page.
* Locate the latest Stable RAW CHR disk image. Vultr requires version7.2.3 Stableor later.
* Right-click the floppy disk icon to copy the URL. Don't download the image now, you'll download it to the server in a later step.
* Navigate to the server's information page in theVultr customer portal.
* Connect to theweb console.
* In the web console, download the CHR image to the server with "wget". If you copied the download URL to your clipboard, you cansend it to the serverthrough the web console.Substitute your version for x.x.x in the examples that follow.# wget https://download.mikrotik.com/routeros/x.x.x/chr-x.x.x.img.zip
* Unzip the downloaded file.# unzip chr-x.x.x.img.zip
* Write the MikroTik CHR image to the server's disk with dd.# dd if=chr-x.x.x.img of=/dev/vda
Substitute your version for x.x.x in the examples that follow.
```
# wget https://download.mikrotik.com/routeros/x.x.x/chr-x.x.x.img.zip
```
Unzip the downloaded file.
```
# unzip chr-x.x.x.img.zip
```
Write the MikroTik CHR image to the server's disk with dd.
```
# dd if=chr-x.x.x.img of=/dev/vda
```
* ifis the image that you unzipped in the previous step.ofis the server's disk:  /dev/vda.
* ifis the image that you unzipped in the previous step.
* ofis the server's disk:  /dev/vda.
This procedure takes a couple of minutes; proceed to the next step when complete.
# Step 3: Connect to MikroTik CHR
* Navigate to the server'ssettings page.
* Choose theCustom ISOmenu, then clickRemove ISO. The server will reboot.
* Connect to theweb console.
* Log in as admin. There is no password set, so pressEnterat the prompt.
* View the software license, then choose a new, strong password.
* Close the web console, then open a terminal on your local computer.
* SSH as admin to the server's IP address.$ ssh admin@192.0.2.2
* Enter the strong password you set in the prior step.
SSH as admin to the server's IP address.
```
$ ssh admin@192.0.2.2
```
This completes the basic installation. Pleasesecure your MikroTik CHR routerand consult thedocumentationto configure the server for production use. Visit Vultr site forconfiguration manualand for theirfirewallfeatures.
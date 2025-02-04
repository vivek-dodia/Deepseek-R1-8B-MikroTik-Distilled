# Document Information
Title: CHR Vultr installation
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/146997259/CHR+Vultr+installation,

# Content
Vultr has more thantwo dozen data center locationswhere you can choose to deploy MikroTik CHR for the bestthroughput and latency.Follow these steps to install MikroTik CHR at Vultr.
# Step 1: Deploy a server in rescue mode
In this step, you'll deploy a new server at Vultr with SystemRescue, a bootable Linux ISO.
When the server finishes deploying, proceed to the next step.
# Step 2: Write the CHR image to the disk
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
This procedure takes a couple of minutes; proceed to the next step when complete.
# Step 3: Connect to MikroTik CHR
SSH as admin to the server's IP address.
```
$ ssh admin@192.0.2.2
```
This completes the basic installation. Pleasesecure your MikroTik CHR routerand consult thedocumentationto configure the server for production use. Visit Vultr site forconfiguration manualand for theirfirewallfeatures.
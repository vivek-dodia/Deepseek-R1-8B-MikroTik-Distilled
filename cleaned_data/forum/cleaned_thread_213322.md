# Thread Information
Title: Thread-213322
Section: RouterOS
Thread ID: 213322

# Discussion

## Initial Question
Dear all, I have some problems with my MikroTik Routers. I plan to upgrade all MKT devices from version 6.46.6 to 7.16.1. I have tried this on two of them and encountered issues during the upgrade. However, my MKT Router is upgrading to the stable version of 7.16.1, but after the upgrade, some of my routing tables, such as static routes, OSPF configurations, and even my default gateway, have changed unexpectedly. If anyone has any ideas on how to handle this problem, please let me know. Thank you in advance. ---

## Response 1
Have a look at this Help page:https://help.mikrotik.com/docs/spaces/R ... h+examples ---

## Response 2
Why do you want to upgrade?Any reason not sticking to V6 and upgrade to 6.49.13 (which is current LTS)? ---

## Response 3
Hmmmm perhaps join the latest century............. take advantage of wireguard and other features......... ---

## Response 4
If anyone has any ideas on how to handle this problem, please let me know. Thank you in advance.I would tryfirst upgrade to latest v6 (6.49.13)then instead of straight to 7.16.1 try something like 7.3then 7.12.1then 7.16.1Might work.... might not.... But sometimes large jumps in firmware cause issues.Andrew ---

## Response 5
I have some problems with my MikroTik Routers. I plan to upgrade all MKT devices from version 6.46.6 to 7.16.1.I think that MT would recommend you to use ROS built-in updater (under /system/packages/update).As already mentioned, there will be a few steps:while running 6.46.6, upgrade it to latest long-term:/system package updateset channel=long-termcheckinstall... after reboot verify that device is running 6.49.13 (if I remember correctly that's current v6 LTS) and do routerboot upgrade by executing/system routerboard upgradeand reboot again.while running v6 LTS, upgrade it to v7:/system package updateset channel=upgradecheckinstall... after reboot verify that device is running v7 (most probably it'll go directly to 7.12.1) and do routerboot upgrade and reboot againwhile running 7.12.1, upgrade to latest stable v7 by running/system/package/updatecheckinstall... and after reboot check that device is running 7.16.1 (or whatever latest v7 stable version). Upgrade routerboot again.I wholeheartedly recommend you to check storage consumption before executing every bullet on the list above and stop doing the procedure if free space drops much below 500-800KiB.As to handling routing config: IIRC the config converter for routing protocols (OSPF, BGP) is far from complete, so you'll have to check correct syntax for v7 in manuals ... and do the conversion manually (essentially ditch the old config entirely and configure it from scratch). ---

## Response 6
Hmmmm perhaps join the latest century............. take advantage of wireguard and other features.........Assumption is the mother...Though I totally agree with your arguments, I really want to know from the TS. ---
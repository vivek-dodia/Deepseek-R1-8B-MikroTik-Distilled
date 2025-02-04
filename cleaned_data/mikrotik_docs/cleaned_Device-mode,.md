# Document Information
Title: Device-mode
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/93749258/Device-mode,

# Content
Thedevice-modeis a feature which sets specific limitations on a device, or limits access to specific configuration options. Such feature is required in order to protect your router and network from attackers who might in some way gain access to your router and use it as a gateway for attacks to other networks. By protecting your device in such a way, even if an attacker manages to gain access to your unprotected device, he will not be able to use it in order to abuse your or any other network.
There are three available modes:advanced,home and basic.Device modes are factory pre-installed to routers, if the router is manufactured and shipped with MikroTik RouterOS v7.17 or later.Advanced (previously called enterprise)mode is assigned to CCR and 1100 series devices,homemode is assigned to home routers and basic mode to any other type of device.For devices running versions prior to RouterOS version 7.17, all devices use theadvanced/enterprisemode.
```
[admin@MikroTik] > system/device-mode/print
mode: advanced
allowed-versions: 7.13+,6.49.8+
flagged: no
flagging-enabled: yes
scheduler: yes
socks: yes
fetch: yes
pptp: yes
l2tp: yes
bandwidth-test: yes
traffic-gen: no
sniffer: yes
ipsec: yes
romon: yes
proxy: yes
hotspot: yes
smb: yes
email: yes
zerotier: yes
container: no
install-any-version: no
partitions: no
routerboard: yes
attempt-count: 0
```
The device-mode can be changed by the user, but remote access to the device is not enough to change it. After changing the device-mode, you need to confirm it, by pressing a button on the device itself, or perform a "cold reboot" - that is, unplug the power. When the change is confirmed, regardless of confirmation mode, thedevice will be rebooted!
```
[admin@MikroTik] > system/device-mode/update mode=home
update: please activate by turning power off or pressing reset or mode button
in 5m00s
-- [Q quit|D dump|C-z pause]
```
If no power off or button press is performed within the specified time, the mode change is canceled. If another update command is run in parallel, both will be canceled.
In order to protect your device against attacker who might silently gain access to your router, abuse it with some scripts and simply try to wait until you will reboot your router and not even know that at that time you are accepting changes requested by some intruder, you can "update" mode only three times. There is a counter which will count how many update attempts are made and will not allow any more updates. This counter can be reset only when administrator does power-cycle the router or press a button when seeing such a warning on mode settings update attempt (same as with accepting any updates).
```
[admin@MikroTik] > system/device-mode/update container=yes
update: too many unsuccessful attempts, turn off power or reboot by pressing reset or mode button in 4m55s to reset attempt-count
```
The following commands are available in the/system/device-modemenu:
Property | Description
----------------------
get | Returns value that you can assign to variable or print on the screen.
print | Shows the active mode and its properties.
update | Applies changes to the specified properties, see below.
get
Returns value that you can assign to variable or print on the screen.
# Available device-mode modes
There are three device modes available for configuration (mode=advanced is default one), each mode has a subset of features that are not allowed when it is used. Note thatthere is no mode, which has all features enabled. Certain features need to be enabled even if you have "advanced" mode enabled. See section "Feature clarification" for more details about what each option means. So, as per the below table it can be seen that "traffic-gen, container, partitions, routerboard" features are always disabled, unless specifically enabled by the admin user.
Mode | Description ofdisabledfeatures
-------------------------------------
advanced (default) | traffic-gen, container,install-any-version, partitions, routerboard
basic | socks, bandwidth-test, traffic-gen, proxy, hotspot, zerotier, container,install-any-version, partitions, routerboard
home | scheduler, socks, fetch, bandwidth-test, traffic-gen, sniffer, romon, proxy, hotspot, email, zerotier, container,install-any-version, partitions, routerboard
socks, bandwidth-test, traffic-gen, proxy, hotspot, zerotier, container,install-any-version, partitions, routerboard
# List of available properties
Property | Description
----------------------
scheduler, socks, fetch, pptp, l2tp, bandwidth-test, traffic-gen, sniffer, ipsec, romon, proxy, hotspot, smb, email, zerotier, container,install-any-version, partitions, routerboard(yes | no) | The list of available features, which can be controlled with thedevice-modeoption. See section "Feature clarification" for more details about what each option means.
activation-timeout(default:5m); | The reset button or power off activation timeout can be set in range 00:00:10 .. 1d00:00:00. If the reset button is not pressed (or cold reboot is not performed) during this interval, the update will be canceled.
flagging-enabled(yes | no; Default:yes) | Enable or disable theflaggedstatus. See below for a detailed description.
flagged(yes | no; Default:no) | RouterOS employs various mechanisms to detect tampering with it's system files. If the system has detected unauthorized access to RouterOS, the status "flagged" is set to yes. If "flagged" is set to yes, for your safety, certain limitations are put in place. See below chapter for more information.
mode:(basic, home, advanced; default:advanced); | Allows choosing from available modes that will limit device functionality.By default,advancedmode allows options excepttraffic-gen, container, partitions,install-any-version, routerboard.So to use these features, you will need to turn it on by performing a device-mode update.By default,homemode disables the following features:scheduler, socks, fetch, bandwidth-test, traffic-gen, sniffer, romon, proxy, hotspot, email, zerotier, container,install-any-version, partitions, routerboard.
Property
Description
By default,advancedmode allows options excepttraffic-gen, container, partitions,install-any-version, routerboard.So to use these features, you will need to turn it on by performing a device-mode update.
By default,homemode disables the following features:scheduler, socks, fetch, bandwidth-test, traffic-gen, sniffer, romon, proxy, hotspot, email, zerotier, container,install-any-version, partitions, routerboard.
More specific control over the available features is possible. Each of the features controlled by device-mode can be specifically turned on or off.
For instanceschedulerwon't allow to perform any action at system scheduler. Used device-mode disables all listed features, for instancemode=home is used, butzerotieris required for your setup, device-mode update /system device-mode update zerotier=yes will be required with the physical access to device to push the button or cut the power.
```
[admin@MikroTik] > system/device-mode/update mode=home email=yes
[admin@MikroTik] > system/device-mode/update mode=advanced zerotier=no
```
If the update command specifies any of the modeparameters, this update replaces the entire device-mode configuration. In this case, all "per-feature" settings will be lost, except those specified with this command. For instance:
```
[admin@MikroTik] > system/device-mode/update mode=home email=yes fetch=yes
[admin@MikroTik] > system/device-mode/print config
mode: home
fetch: yes
email: yes
[admin@MikroTik] > system/device-mode/update mode=advanced sniffer=no
-- reboot --
[admin@MikroTik] > system/device-mode/print config
mode: advanced
sniffer: no
```
We see that fetch = yes and email = yes is missing, as they were overriden with the mode change. However, specifying only "per-feature" settings will change only those:
```
[admin@MikroTik] > system/device-mode/update hotspot=no
-- reboot --
[admin@MikroTik] > system/device-mode/print config
mode: advanced
sniffer: no
hotspot: no
```
If the feature is disabled, an error message is displayed for interactive commands:
```
[admin@MikroTik] > system/device-mode/print config
mode: advanced
sniffer: no
hotspot: no
[admin@MikroTik] > tool/sniffer/quick
failure: not allowed by device-mode
```
However, it is possible to add the configuration to a disabled feature, but there will be a comment showing the disabled feature in the device-mode:
```
[admin@MikroTik] > ip hotspot/add interface=ether1
[admin@MikroTik] > ip hotspot/print
Flags: X, S - HTTPS
Columns: NAME, INTERFACE, PROFILE, IDLE-TIMEOUT
# NAME      INTERFACE  PROFILE  IDLE-TIMEOUT
;;; inactivated, not allowed by device-mode
0 X hotspot1  ether1     default  5m
```
# Feature clarification
Feature | Clarification of which menus become unavailable
bandwidth-test | /tool bandwidth-test/tool bandwidth-server/tool speed-test
routerboard | /system routerboard settings(except auto-upgrade option)
container | all container functionality
install-any-version | RouterOS will no longer allow for you to install RouterOS version below versions listed under "allowed-versions" attribute.
email | /tool e-mail
fetch | /tool fetch
hotspot | /ip hotspot
ipsec | /ip ipsec
l2tp | /interface l2tp-server/interface l2tp-client
partitions | /partitionsdoes not allow to change count of partitions. If your router is unable to boot, it will still be able to boot into your other partitions. No restriction for crash recovery.
pptp | /interface pptp-server/interface pptp-client
proxy | /ip proxy
romon | /tool romon
scheduler | /system scheduler
smb | /ip smb
sniffer | /tool sniffer
socks | /ip socks
traffic-gen | /tool traffic-generator/tool flood-ping/tool ping-speed
zerotier | /zerotier
/tool bandwidth-test/tool bandwidth-server
/tool speed-test
install-any-version
RouterOS will no longer allow for you to install RouterOS version below versions listed under "allowed-versions" attribute.
/interface l2tp-server
/interface l2tp-client
/partitions
does not allow to change count of partitions. If your router is unable to boot, it will still be able to boot into your other partitions. No restriction for crash recovery.
/interface pptp-server
/interface pptp-client
/tool traffic-generator
/tool flood-ping
/tool ping-speed
# Allowed versions
Device mode lists in its parameters an argument called "allowed-versions". This is a list of versions which MikroTik considers as secure and which ones do not include any serious vulnerabilities which could be used by an attacker. This list can be updated to versions which includes some major changes in RouterOS below which downgrade should not be allowed.This setting does not depend on the installed RouterOS version and works as a separate mechanism, in order to disallow attacker to downgrade version step-by-step in order to reach some vulnerable RouterOS release. This means that if you upgrade RouterOS to a release where a newer "allowed-versions" list is available, oldest list will be overwritten. If you downgrade RouterOS, "allowed-versions" list will not change and will remain updated to the latest list.
This list is ignored, if device-mode "install-any-version" is enabled.
# Flagged status
Along with thedevice-mode feature, RouterOS now can analyze the whole configuration at system startup, to determine if there are any signs of unauthorized access to your router. If suspicious configuration is detected, the suspicious configuration will be disabled and theflaggedparameter will be set to "yes". The device has now a Flagged state and enforces certain limitations.
```
[admin@MikroTik] > system/device-mode/print
mode: advanced
flagged: yes
sniffer: no
hotspot: no
```
If the system has this flagged status, the current configuration works, but it is not possible to perform the following actions:bandwidth-test, traffic-generator, sniffer, as well as configuration actions that enable or create new configuration entries (it will still be possible to disable or delete them) for the following programs:system scheduler, SOCKS proxy, pptp, l2tp, ipsec, proxy, smb.When performing the aforementioned actions while the router has the flagged state, you will receive an error message:
```
[admin@MikroTik] > /tool sniffer/quick
failure: configuration flagged, check all router configuration for unauthorized changes and update device-mode
[admin@MikroTik] > /int l2tp-client/add connect-to=1.1.1.1 user=user
failure: configuration flagged, check all router configuration for unauthorized changes and update device-mode
```
To exit the flagged state, you must perform the command "/system/device-mode/update flagged=no". The system will ask to either press a button, or issue a hard reboot (cut power physically or do a hard reboot of the virtual machine).Important!Although the system has disabled any malicious looking rules, which triggered the flagged state, it is crucial to inspect all of your configuration for other unknown things, before exiting the flagged state. If your system has been flagged, assume that your system has been compromised and do a full audit of all settings before re-enabling the system for use. After completing the audit, change all the system passwords and upgrade to the latest RouterOS version.
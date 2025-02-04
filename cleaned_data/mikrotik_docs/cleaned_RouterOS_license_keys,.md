# Document Information
Title: RouterOS license keys
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/328149/RouterOS+license+keys,

# Content
# 2Overview3System Requirements4RouterOS license key levels4.1CHR License Levels4.2Prepaid Key5How to Purchase a RouterOS license key6How to Convert prepaid key to licence key for x867Replacement Key8Obtaining Licenses and Working With Them8.1Where can I buy a RouterOS license key?8.2If I have purchased my key elsewhere8.3If I have a license and want to put it on another account?8.4If I have lost a license on my device?9Using the License9.1Can I Format or Re-Flash the drive?9.2How many computers can I use the License on?9.3Can I temporary use the HDD for something else, other than RouterOS?9.4Can I move the license to another HDD?9.5Must I type the whole key into the router?9.6Can I install another OS on my drive and then install RouterOS again later?9.7I lost my RouterBOARD, can you give me the license to use on another system?9.8Licenses Purchased from Resellers9.9I am not using the software, can you terminate my license?9.10Is this possible to upgrade or transfer my x86 license to a CHR license
# Overview
MikroTik hardware routers that run RouterOS come preinstalled with a RouterOS license, if you have purchased a RouterOS based device, nothing must be done regarding the license.
For X86 systems (i.e. PC devices), you need to obtain a license key. Each x86 system has a unique identifier calledSoftware ID, which is used for licensing.
The license key is a block of symbols that needs to be copied from yourmikrotik.comaccount, or from the email you received in, and then it can be pasted into the router. You can paste the key anywhere in the terminal, or by clicking "Paste key" in WinBox License menu. A reboot is required for the key to take effect.
Licensing information can be read from CLI system console:
```
[admin@RB1100] > /system license print
software-id: "43NU-NLT9"
nlevel: 6
features:
[admin@RB1100] >
```
or from equivalentWinBox,WebFigmenu.
# System Requirements
The minimum required RAM depends on interface count and CPU count. You can get an approximate number by using the following formula:
# RouterOS license key levels
After installation RouterOS runs intrial mode. You have 24 hours to register for Level 1 (Free demo) or purchase a Level 4,5 or 6 license and paste a valid key.
```
[admin@MikroTik] /system license> print
software-id: TRPC-YYR2
expires-in: 23h48m24s
```
Level 3 is a wireless station (client or CPE) only license.For x86 PCs, Level3 is not available for purchase individually.
Level 2 was a transitional license from old legacy (pre 2.8) license format. These licenses are not available any more, if you have this kind of license, it will work, but to upgrade it - you will have to purchase a new license.
The difference between license levels is shown in the table below:
Level number | 0 (Trial mode) | 1 (Free Demo) | 3 (WISP CPE) | 4 (WISP) | 5 (WISP) | 6 (Controller)
---------------------------------------------------------------------------------------------------
Price | no key | registration required | not for sale | $45 | $95 | $250
Wireless AP mode (PtMP) | 24h trial | - | no | yes | yes | yes
PPPoE tunnels | 24h trial | 1 | 200 | 200 | 500 | unlimited
PPTP tunnels | 24h trial | 1 | 200 | 200 | 500 | unlimited
L2TP tunnels | 24h trial | 1 | 200 | 200 | 500 | unlimited
OVPN tunnels | 24h trial | 1 | 200 | 200 | unlimited | unlimited
EoIP tunnels | 24h trial | 1 | unlimited | unlimited | unlimited | unlimited
VLAN interfaces | 24h trial | 1 | unlimited | unlimited | unlimited | unlimited
Queue rules | 24h trial | 1 | unlimited | unlimited | unlimited | unlimited
HotSpot active users | 24h trial | 1 | 1 | 200 | 500 | unlimited
User manager active sessions | 24h trial | 1 | 10 | 20 | 50 | Unlimited
Bonding interfaces | 24h trial | 1 | unlimited | unlimited | unlimited | unlimited
RADIUS | 24h trial | - | unlimited | unlimited | unlimited | unlimited
All Licenses:
# CHR License Levels
License levels described until now do not apply to Cloud Hosted Routers (CHRs). CHR is a RouterOS version intended for running as a virtual machine. It has its own 4 license levels as well as trial where you can test any of the paid license levels for 60 days.
60-day free trial license is available for all paid license levels. To get the free trial license, you have to have an account onMikroTik.comas all license management is done there.
Perpetual is a lifetime license (buy once, use forever). It is possible to transfer a perpetual license to another CHR instance. A running CHR instance will indicate the time when it has to access the account server to renew it's license. If the CHR instance will not be able to renew the license it will behave as if the trial period has ran out and will not allow an upgrade of RouterOS to a newer version.
After licensing a running trial system, youmustmanually run the/system license renewcommand from the CHR to make it active. Otherwise the system will not know you have licensed it in your account. If you do not do this before the system deadline time, the trial will end and you will have to do a complete fresh CHR installation, request a new trial and then license it with the license you had obtained.
```
/system license renew
```
License | Speed limit | Price | Description
-------------------------------------------
Free | 1Mbit | FREE | The free license level allows CHR to run indefinitely. It is limited to 1Mbps upload per interface. All the rest of the features provided by CHR are available without restrictions. To use this, all you have to do is download disk image file from our download page and create a virtual guest.
P1 | 1Gbit | $45 | P1 (perpetual-1) license level allows CHR to run indefinitely. It is limited to 1Gbps upload per interface. All the rest of the features provided by CHR are available without restrictions. It is possible to upgrade from P1 to P10 or P-Unlimited. Once the upgrade is purchased at the full price, the former license will become available for later use on your account.
P10 | 10Gbit | $95 | P10 (perpetual-10) license level allows CHR to run indefinitely. It is limited to 10Gbps upload per interface. All the rest of the features provided by CHR are available without restrictions.It is possible to upgrade from P10 to P-Unlimited. Once the upgrade is purchased at the full price, the former license will become available for later use on your account.
P-Unlimited | Unlimited | $250 | The p-unlimited (perpetual-unlimited) license level allows CHR to run indefinitely. It is the highest tier license and it has no enforced limitations.
60-day Trial |  | FREE | In addition to the limited Free installation, you can also test the increased speed of P1/P10/PU licenses with a 60 trial.You will have to have an account registered onMikroTik.com. Then you can request the desired license level for trial from your router that will assign your router ID to your account and enable a purchase of the license from your account. All the paid license equivalents are available for trial. A trial period is 60 days from the day of acquisition, after this time passes, your license menu will start to show "Limited upgrades", which means that RouterOS can no longer be upgraded.Notethat if you plan to purchase the selected license, you must do itbefore60 days trial ends. If your trial has ended, and there are no purchases within 2 months, the device will no longer appear in your MikroTik account. You will have to make a new CHR installation to make a purchase within the required time frame.To request a trial license, you must run the command "/system license renew" from the CHR device command line. You will be asked for the username and password of yourmikrotik.comaccount.
P1 (perpetual-1) license level allows CHR to run indefinitely. It is limited to 1Gbps upload per interface. All the rest of the features provided by CHR are available without restrictions. It is possible to upgrade from P1 to P10 or P-Unlimited. Once the upgrade is purchased at the full price, the former license will become available for later use on your account.
P10 (perpetual-10) license level allows CHR to run indefinitely. It is limited to 10Gbps upload per interface. All the rest of the features provided by CHR are available without restrictions.It is possible to upgrade from P10 to P-Unlimited. Once the upgrade is purchased at the full price, the former license will become available for later use on your account.
$250
In addition to the limited Free installation, you can also test the increased speed of P1/P10/PU licenses with a 60 trial.
You will have to have an account registered onMikroTik.com. Then you can request the desired license level for trial from your router that will assign your router ID to your account and enable a purchase of the license from your account. All the paid license equivalents are available for trial. A trial period is 60 days from the day of acquisition, after this time passes, your license menu will start to show "Limited upgrades", which means that RouterOS can no longer be upgraded.
Notethat if you plan to purchase the selected license, you must do itbefore60 days trial ends. If your trial has ended, and there are no purchases within 2 months, the device will no longer appear in your MikroTik account. You will have to make a new CHR installation to make a purchase within the required time frame.
To request a trial license, you must run the command "/system license renew" from the CHR device command line. You will be asked for the username and password of yourmikrotik.comaccount.
```
/system license renew
```
# Prepaid Key
A Prepaid Key is a type of license key you can purchase in advance for MikroTik products, such as the CHR, or convert into a license key to apply to an x86 system's Software ID. It allows you to buy a license without immediately assigning it to a specific device. Once you have a Prepaid Key, you can use it to upgrade a CHR or later convert it into a license key by providing the device's Software ID.
# How to Purchase a RouterOSlicense key
Access the "Purchase a RouterOS License Key" Section.
Enter License Key Information: Paste the Software ID of the device;
Review and Complete Your Purchase
Congratulations! You have successfully purchased a RouterOS license key.
# How to Convert prepaid key to licence key for x86
Purchase a RouterOSPrepaid Key
Purchase a RouterOS Prepaid key if you haven't already.
Access the "Make a Key from Prepaid Key" Section
Navigate to the "Make a key from prepaid key" section in your account.
Select and Convert the Prepaid Key
Select the desired prepaid key from the list.
Input theSoftware IDof the x86 device you need to license, or theSoftware IDof the router to upgrade the licence level.
Press "Generate".
Confirmation Message
A message will appear: "Successfully converted prepaid key to a new licence!".
Apply the License Key
Copy the generated license key.
Paste it into the x86 device to apply the license.
Congratulations! You have successfully converted a prepaid key to a license key for your x86 device.
# Replacement Key
A Replacement Key is a special key issued by the MikroTik support team in case of an x86 HDD failure or if an x86 instance running RouterOS has lost its license. It costs $10 and can be issued once per original key.
Note that before issuing such key, MikroTik Support can ask you to prove that the old drive has failed, in some cases, this means sending us the dead drive.
Replacement key request
1)Go to your account management inmikrotik.comand fill the "support contact form" or write a direct e-mail tosupport@mikrotik.com
Please provide detailed information about why replacement key is required
2)Send required info to MikroTik support department.
3)Re-check your account after support staff has confirmed that replacement key has been added to your account. Select the section "Make a key from replacement key"
4)Select the appropriate license level on which you wish to perform the replacement
5)Enter the new "software-ID"
6)Proceed to checkout by pressing "Add license replacement to cart" and finish the payment
7)An e-mail will be sent to your profile containing the new license.
You can also find the newly generated key in the section "Search and view all keys" under the folder "Purchased YYYY" where "YYYY" is the current Year
# Obtaining Licenses and Working With Them
# Where can I buy a RouterOS license key?
MikroTik devices come preinstalled with a license and no purchase is needed.
To obtain a higher level license, or to obtain a license for ax86 PC installation, you must register anaccount on our webpage, and in there, use the optionPurchase a RouterOS license key.
# If I have purchased my key elsewhere
You must contact the company who sold you the license, they will provide the support.
# If I have a license and want to put it on another account?
You can give access to keys with the help ofVirtual Folders
The only kind of licenses, that could be transferred to another Account is a prepaid key. Prepaid keys got as a gift from the Training are not transferable.To transfer purchased prepaid key navigate to "Transfer prepaid keys" in the section "ROUTEROS KEYS" on your MikroTik Account.
# If I have lost a license on my device?
If for some reason you have lost license from your router, upgrade router to the latest RouterOS version available and use "Request license key" in yourmikrotik.comaccount. Use soft-id and serial number available under System/License menu in RouterOS when requesting license. Apply received license or contactsupport@mikrotik.comif request feature do not work.
# Using the License
# Can I Format or Re-Flash the drive?
Formatting, and Re-Imaging the drive with non-MikroTik tools (like DD and Fdisk) will destroy your license! Be very careful and contact MikroTik support before doing this. It is not recommended, as MikroTik support might deny your request for a replacement license. For this use MikroTik provided tools - Netinstall or CD-install that are freely available from our download page.
# How many computers can I use the License on?
The RouterOS license can be used only in one system, at the same time. The License is bound to the HDD it is installed on, but you have the ability to move the HDD to another computer system. You cannot move the License to another HDD, neither can you format or overwrite the HDD with the RouterOS license. It will be erased from the drive, and you will have to get a new one. If you accidentally removed your license, contact the support team for help.
# Can I temporary use the HDD for something else, other than RouterOS?
As stated above, no.
# Can I move the license to another HDD?
If your current HDD drive is destroyed, or can no longer be used, it is possible to transfer the license to another HDD. You will have to request a replacement key (see below) which will cost 10$
# Must I type the whole key into the router?
No, simply copy it and paste in the menuSystem→License → Paste Keyand Confirm to reboot.
Or paste it to the CLI and press "Y" to reboot.
# Can I install another OS on my drive and then install RouterOS again later?
No, because if you use formatting, partitioning utilities or tools that do something to the MBR, you will lose the license and you will have to make a new one. This process is not free (see Replacement Key above)
# I lost my RouterBOARD, can you give me the license to use on another system?
MikroTik hardware comes with an embedded license. You cannot move this license to a new system in any way, this includes any upgrades applied to the MikroTik router while it was still working.
# Licenses Purchased from Resellers
The keys that you purchase from other vendors and resellers are not in your account. Yourmikrotik.comaccount only contains licenses purchased from MikroTik directly.
# I am not using the software, can you terminate my license?
The licenses are stand alone keys and MikroTik does not have any remote control over your devices. Therefore, we are unable to verify if you use your license or not. This is why MikroTik cannot terminate any issued licenses.
# Is this possible to upgrade or transfer my x86 license to a CHR license
It is not possible to upgrade the x86 license to a CHR license. You will need to purchase a new license for the CHR.
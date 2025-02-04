# Thread Information
Title: Thread-1122081
Section: RouterOS
Thread ID: 1122081

# Discussion

## Initial Question
As the images belowBut both auto and manual negotation working without issuessAnd here is my nics model, one is sriov and the other is physical passtrough ---

## Response 1
same problem after updating to 7.17rc3any guide to get this message "unsupported speed" removed , and what it indicate ? ---

## Response 2
Did you upgrade both RouterOS and firmware?Did you manually set interface speed? ---

## Response 3
Did you upgrade both RouterOS and firmware?Did you manually set interface speed?just updated the mikrotik os through the system package update . ---

## Response 4
It is strongly recommended to upgrade the bootloader after RouterOS update. To upgrade the bootloader, execute command "/system routerboard upgrade" in CLI, followed by a reboot. Alternatively, navigate to the GUI System → RouterBOARD menu and click the "Upgrade" button, then reboot the device.https://help.mikrotik.com/docs/spaces/R ... stallation ---

## Response 5
If he's using Mellanox NICs he's obviously using either ROSx86 on bare metal or CHR. You can't update RouterBOARD firmware on either.@geekera1n, nanobahr: contactsupport@mikrotik.comand link them to this thread. ---

## Response 6
problem disappeared after downgraded back to Mikrotik v7.16.2 stable ---

## Response 7
same problem after updating to 7.17rc3any guide to get this message "unsupported speed" removed , and what it indicate ?What Mellanox NIC model are u using? ---

## Response 8
same problem after updating to 7.17 ---

## Response 9
same problem, but with Intel X520-DA27.16.2 - ok7.17 - unsupported speed.everything works, it's not critical, I hope they fix it later ---

## Response 10
Same problem here.Maybe fixed inv7.18beta2?*) ethernet - improved link speed reporting on 2.5G-baseT and 10Gbase-T ports; ---

## Response 11
Same problem here.Maybe fixed inv7.18beta2?*) ethernet - improved link speed reporting on 2.5G-baseT and 10Gbase-T ports;noalso have this bug ---

## Response 12
I’m encountering the same issue! I upgraded to RouterOS v7.17 and Winbox 4 simultaneously and initially assumed it was a display bug in Winbox 4. However, it appears to be a problem with RouterOS v7.17. I’m running CHR on RouterOS and upgraded from v7.16.2 to v7.17. The NIC I’m using is a CX4121A (Mellanox ConnectX-4 Lx). Although the interface status shows “unsupported speed,” the link itself functions normally. Interestingly, when I enable Auto Negotiation, the “unsupported speed” message disappears, but the link speed fails to negotiate properly. This NIC has a known long-standing issue with auto-negotiation, so I have always configured the speed manually. The sudden appearance of the “unsupported speed” message is therefore quite confusing. ---

## Response 13
Mikrotik support says that this will be fixed when the v7.18beta3 comes out. ---
# Thread Information
Title: Thread-1122711
Section: RouterOS
Thread ID: 1122711

# Discussion

## Initial Question
photo_2025-01-29_22-41-23.pngHello everyone. I noticed that after updating the firmware to 7.17, a strange symbol appeared in the current firmware field, similar to (U+2642 ♂ male sign). Has anyone else had the same problem? What do you think it is? An Easter egg from the developers, a firmware glitch, something else? ---

## Response 1
Nice find ---

## Response 2
This is because you do not align the factory firmware, and new firmware have some misalignment...Install exactly 7.6, upgrade the firmware, reboot to be sure current firmware is 7.6 then install this:https://box.mikrotik.com/f/3bd8cc7b2a6545228377/?dl=1Next you can install correctly 7.17https://help.mikrotik.com/docs/spaces/R ... bootloader ---

## Response 3
This is because you do not align the factory firmware, and new firmware have some misalignment...Thank you! I'll try and write what happens ---

## Response 4
Install exactly 7.6, upgrade the firmware, reboot to be sure current firmware is 7.6 then install this:Please tell me in what cases is it necessary to carry out such an alignment? For all old devices with old firmware? Or for certain versions of old firmware? ---

## Response 5
Install exactly 7.6, upgrade the firmware, reboot to be sure current firmware is 7.6 then install this:Please tell me in what cases is it necessary to carry out such an alignment? For all old devices with old firmware? Or for certain versions of old firmware?The Wiki page mentions:If your RouterOS is v7, your factory-firmware version is lower than 7.6 and your device displays the message → The "protected routerboot" feature requires a backup-routerboot upgradeIf your RouterOS version is v6 and you get the same prompt ---

## Response 6
Please tell me in what cases is it necessary to carry out such an alignment? For all old devices with old firmware? Or for certain versions of old firmware?I do it as standard procedure on any upgrade, but as soon as it is referrred to in the release notes you should. ---
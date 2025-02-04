# Thread Information
Title: Thread-1118352
Section: RouterOS
Thread ID: 1118352

# Discussion

## Initial Question
I bougt a new router.Exported de setting the old oneImported to new oneNearly work fineI have lots of static ip address in DHCP server. The new router gives new IP addres instead the fixed IPs- I must delete all the fixed IP and create it again with same MAC address.My Thecnology:delete the fixed IPfind the device with same MAC addresMake staticModify to needed IP address ---

## Response 1
Ok, anything we can help you with? ---

## Response 2
Ok, anything we can help you with?Is there less complicated solution? ---

## Response 3
Something isn't working while importing the old config. Hard to say what it is.You could reset the new device (what exact device do you use) without default config and then import the old config (which device was that).It should work (at least, DHCP leases are exportable and importable. ---

## Response 4
Something isn't working while importing the old config. Hard to say what it is.You could reset the new device (what exact device do you use) without default config and then import the old config (which device was that).It should work (at least, DHCP leases are exportable and importable.THX ---

## Response 5
How in particular did you export and import config? Did you usebackupandrestorecommands ... orexportandimport? If the former ... then it's known (apparently not well though) that binary backups (results ofbackup) are not intended to move config from one device to another one. Specially so if source and target devices are not same model. Even if both devices are same model there are a few quirks which can interfere with normal operations after restoring configuration on target device. ---

## Response 6
Looks like the ones that are duplicated (where they got new IP) the static entry does not have a server name associated with it. e.g. dhcp1Fix that up and you should be fine. ---
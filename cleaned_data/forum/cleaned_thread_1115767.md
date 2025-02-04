# Thread Information
Title: Thread-1115767
Section: RouterOS
Thread ID: 1115767

# Discussion

## Initial Question
I'm not sure what I did (or if I did anything), but now I get this:
```
[david@RoutyMcRouterson]>/ipv6/dhcp-clientexport# 2024-10-15 14:52:33 by RouterOS 7.16# software id = U9U9-RERG## model = RB5009UG+S+# serial number =#errorexporting"/ipv6/dhcp-client"(timeout)If I do
```

```
/ipv6/dhcp-clientprintit just hangs. If I try to remove any config under /ipv6/dhcp-client, it just hangs. If I try to re-create the config in there I get errors that there are duplicates. In WinBox, the IPv6/DHCP client page is blank.I have also tried
```

```
/ipv6/dhcp-client/remove[find]and
```

```
/ipv6/dhcp-client/remove[findinterface=ether8]but it just hangs.How can I reset things?

---
```

## Response 1
The behaviour you're describing means, that configuration is not actually disappearing, rather CLI has problems retrieving it. I'm not sure what is the best way to get out of this state. If nobody else chimes in, you may want to contactsupport@mikrotik.com(it may take a while before you get a meaningful answer though). ---

## Response 2
If a system reset configuration fail, netinstall the device, the internal config database is corrupted.Do not use backup because already have corrupted files inside.For reconfig just use old export. ---

## Response 3
Yes, the only way to fix it is to restore from a backup. Obviously this is problematic... ---

## Response 4
How can I reset things?I had a similar problem when upgrading to 7.16. Rolling back the firmware to 7.15 made this item work again.Upgrading to 7.16 causes the problem, for example, if you had the ipv6 dhcp client described and disabled. ---

## Response 5
Next time, partition the device (2 partitions), and before you upgrade copy the active partition to the other one.When the upgrade fails, select the other partition as active and reboot and you have your original version and config back.(when it does not boot at all, you can powercycle it during boot and it will automatically change the active partition) ---
# Document Information
Title: Partitions
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/328103/Partitions,

# Content
# Summary
Partitioning is supported on ARM, ARM64, MIPS, TILE, and PowerPC RouterBOARD type devices.
It is possible to partition NAND flash, allowing to install own OS on each partition and specify primary and fallback partitions.
If a partition should fail for some reason (failed upgrade, problematic configuration introduced, software problem), the next partition will boot instead. This can be used as an interactive backup where you keep a verified working installation and upgrade only some secondary partition. If you upgrade your configuration, and it proves to be good, you can use the "save config" button to copy it over to other partitions.
Minimum partition sizes:
The maximum number of allowed partitions is 8.
```
[admin@1009up] > /partitions/print
Flags: A - ACTIVE; R - RUNNING
Columns: NAME, FALLBACK-TO, VERSION, SIZE
# NAME FALL VERSION SIZE
0 AR part0 next RouterOS v7.1beta4 Dec/15/2020 15:55:11 128MiB
```
# Commands
Property | Description
----------------------
activate(<partition>) | Assigns another partition as Active. This option is available if the "partitions" setting is enabled in device mode (since RouterOS 7.17).
repartition(integer) | Will reboot the router and reformat the NAND, leaving only active partition.
copy-to(<partition>) | ClonerunningOS with the config to specified partition. Previously stored data on the partition will be erased.
save-config-to(<partition>) | Clonerunning-configon a specified partition. Everything else is untouched.
restore-config-from(<partition>) | Copy config from specified partition torunningpartition
Assigns another partition as Active. This option is available if the "partitions" setting is enabled in device mode (since RouterOS 7.17).
# Properties
Property | Description
----------------------
name(string; Default: ) | Name of the partition
fallback-to(etherboot | next | <partition-name>; Default:next) | What to do if an active partition fails to boot:etherboot- switch to etherbootnext'- try next partitionfallback to the specified partition
# Read-only
Property | Description
----------------------
active(yes | no) | Partition is active
running(yes | no) | Currently running partition
size(integer[MiB]) | Partition size
version(string) | Current RouterOS version installed on the partition
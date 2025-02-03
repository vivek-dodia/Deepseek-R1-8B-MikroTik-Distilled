---
title: Resource
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/40992875/Resource,
crawled_date: 2025-02-02T21:15:08.095960
section: mikrotik_docs
type: documentation
---

# Summary
## General
```
/system resource
```
The general resource menu shows overall resource usage and router statistics like uptime, memory usage, disk usage, version, etc.
It also has several sub-menus for more detailed hardware statistics like PCI, IRQ, and USB.
```
[admin@MikroTik] > system/resource/print 
                   uptime: 29s
                  version: 7.11.2 (stable)
               build-time: Aug/31/2023 13:55:47
         factory-software: 7.6
              free-memory: 94.2MiB
             total-memory: 224.0MiB
                      cpu: ARM
                cpu-count: 2
            cpu-frequency: 800MHz
                 cpu-load: 2%
           free-hdd-space: 93.5MiB
          total-hdd-space: 128.5MiB
  write-sect-since-reboot: 85
         write-sect-total: 222100
               bad-blocks: 0%
        architecture-name: arm
               board-name: hAP ax lite LTE6
                 platform: MikroTik
```
Properties
All properties are read-only
Property | Description
----------------------
architecture-name(string) | CPU architecture
bad-blocks(percent) | Shows percentage of bad blocks on the NAND.
board-name(string) | RouterBOARD model name
build-time(string) | Installed RouterOS version build-time
cpu(string) | CPU model that is on the board
cpu-count(integer) | Number of CPUs present on the system. Each core is a separate CPU, Intel HT is also a separate CPU.
cpu-frequency(string) | Current CPU frequency
cpu-load(percent) | Percentage of used CPU resources. Combines all CPUs. Per-core CPU usage can be seen inCPU submenu
factory-software(string) | Minimal RouterOS version
free-hdd-space(string) | Free space on hard drive or NAND
free-memory(string) | The unused amount of RAM
platform(string) | Platform name
total-hdd-space(string) | Size of the hard drive or NAND
total-memory(string) | Amount of installed RAM
uptime(time) | Time interval passed since boot-up
version(string) | Installed RouterOS version number
write-sect-since-reboot(integer) | A number of sector writes in HDD or NAND since the router was last time rebooted
write-sect-total(integer) | A number of sector writes in total
## CPU
```
/system resource cpu
```
This submenu shows per-cpu usage, as long as IRQ and Disk usage.
```
[admin@RB1100test] /system resource cpu> print 
CPU LOAD IRQ DISK 
0 5% 0% 0% 
[admin@RB1100test] /system resource cpu>
```
Properties
Read-only properties
Property | Description
----------------------
cpu(integer) | Identification number of CPU which usage is shown.
load(percent) | CPU usage in percents
irq(percent) | IRQ usage in percents
disk(percent) | Disk usage in percents
## IRQ
```
/system resource irq
```
The menu shows all used IRQs on the router. It is possible to set upIRQ load balancingon multicore systems by assigning IRQ to a specific core. IRQ assignments are done by hardware and cannot be changed from RouterOS. For example, if all Ethernets are assigned to one IRQ, then you have to deal with hardware: upgrade motherboards BIOS, reassign IRQs manually in BIOS, if none of the above helps then change the hardware.
### Properties
Property | Description
----------------------
cpu(auto | integer; Default: ) | Specifies which CPU is assigned to the IRQ.auto- pick CPU based on a number of interrupts. UsesNAPIto optimize interrupts.
* auto- pick CPU based on a number of interrupts. UsesNAPIto optimize interrupts.
Read-only properties
Property | Description
----------------------
active-cpu(integer) | Shows active CPU in multicore systems.
count(integer) | A number of interrupts. On ethernet interfaces interrupt=packet.
irq(integer) | IRQ identification number
users(string) | Process assigned to IRQ
### IRQ Load Balancing
## USB
```
/system resource usb
```
This menu displays all available USB controllers on the board. The menu is available only if at least one USB controller is present.
```
[admin@MikroTik] /system resource usb> print detail 
0 device="2:1" name="RB400 EHCI" serial-number="rb400_usb" vendor-id="0x1d6b" 
device-id="0x0002" speed="480 Mbps" ports=2 usb-version="2.00" 
1 device="1:1" name="RB400 OHCI" serial-number="rb400_usb" vendor-id="0x1d6b"
 device-id="0x0001" speed="12 Mbps" ports=2 usb-version="1.10"
```
### Properties
Property | Description
----------------------
device(string) | 
device-id(hex) | Hexadecimal device ID
name(string) | Descriptive name of the device retrieved from the driver
ports(integer) | How many ports are supported by the USB controller
serial-number(string) | 
speed(string) | Max USB speed that can be used (480Mbps for USBv2 and 12Mbps for USBv1)
usb-version(string) | Identifies max supported USB version
vendor(string) | Device manufacturer's name.
vendor-id(hex) | Hexadecimal vendor ID
## PCI
```
/system resource pci
```
PCI submenu shows the information about all PCI devices on the board
```
[admin@RB1100test] /system resource pci> print 
# DEVICE VENDOR NAME IRQ 
0 06:00.0 Attansic Technology Corp. unknown device (rev: 192) 18 
1 05:00.0 Freescale Semiconductor Inc MPC8544 (rev: 17) 0 
2 04:00.0 Attansic Technology Corp. unknown device (rev: 192) 17 
3 03:00.0 Freescale Semiconductor Inc MPC8544 (rev: 17) 0 
4 02:00.0 Attansic Technology Corp. unknown device (rev: 192) 16 
5 01:00.0 Freescale Semiconductor Inc MPC8544 (rev: 17) 0 
6 00:00.0 Freescale Semiconductor Inc MPC8544 (rev: 17) 0
```
### Properties
All properties are read-only
Property | Description
----------------------
category(string) | PCI device type, for example,ethernet controller
device(string) | 
device-id(hex) | Hexadecimal device ID
io(hex-hex) | I/O memory range
irq(integer) | IRQ assigned to the device
memory(hex-hex) | Memory range
name(string) | Descriptive name of the device retrieved from the driver
vendor(string) | Device manufacturer's name.
vendor-id(hex) | Hexadecimal vendor ID
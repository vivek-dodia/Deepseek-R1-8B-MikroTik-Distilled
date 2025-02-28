# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212040

# Discussion

## Initial Question
Author: Sat Oct 26, 2024 1:24 am
``` 2 device="00:05.0" name="Virtio network device (rev: 0)" vendor="Red Hat, Inc." category="Ethernet controller" vendor-id="0x1af4" device-id="0x1000" irq=10 memory=0xC000E000-0xC000FFFF io=0x2080-0x20BF 3 device="00:05.1" name="Virtio network device (rev: 0)" vendor="Red Hat, Inc." category="Ethernet controller" vendor-id="0x1af4" device-id="0x1000" irq=10 memory=0xC000C000-0xC000DFFF io=0x2040-0x207F 4 device="00:05.2" name="Virtio network device (rev: 0)" vendor="Red Hat, Inc." category="Ethernet controller" vendor-id="0x1af4" device-id="0x1000" irq=11 memory=0xC000A000-0xC000BFFF io=0x2000-0x20DF 5 device="00:06.0" name="T540-CR Unified Wire Ethernet Controller [VF] (rev: 0)" vendor="Chelsio Communications Inc" category="Ethernet controller" vendor-id="0x1425" device-id="0x5803" irq=0 memory=0xC0012000-0xC0012FFF, 0xC0000000-0xC01FFFFF, 0xC0008000-0xC0009FFF ``` ``` [admin@lab1.i.lfns.org.uk] /system> /interface/print Flags: R - RUNNING Columns: NAME, TYPE, ACTUAL-MTU, MAC-ADDRESS # NAME TYPE ACTUAL-MTU MAC-ADDRESS 0 R ether1 ether 1500 06:00:00:00:05:08 1 R ether2 ether 1500 06:00:00:00:05:09 2 R ether3 ether 1500 06:00:00:00:05:0C 3 R lo loopback 65536 00:00:00:00:00:00 [admin@lab1.i.lfns.org.uk] /system> ``` hello, i have RouterOS x86 running in a virtual machine (bhyve on FreeBSD 15.0). the virtual machine has four Ethernet PCI network devices:
```
however, while the "Virtio" devices are detected correctly, the Chelsio VF is not:
```

```
i assume this is because the kernel is missing a driver for this card.  is there some kind of HCL for RouterOS x86 that lists supported drivers?  or is it worth asking MikroTik support to add the appropriate driver?unfortunately i can't use CHR as it doesn't support bhyve (because MikroTik apparently wrongly believe it's paravirtualisation).


---
```

## Response 1
Author: Sat Oct 26, 2024 3:14 am
``` [admin@lab1.i.lfns.org.uk] > /system/resource/print uptime: 4m7s version: 7.16.1 (stable) build-time: 2024-10-10 14:03:32 factory-software: 7.1 free-memory: 291.1MiB total-memory: 512.0MiB cpu: AMD cpu-count: 1 cpu-frequency: 3699MHz cpu-load: 0% free-hdd-space: 71.2MiB total-hdd-space: 89.2MiB write-sect-since-reboot: 880 write-sect-total: 880 architecture-name: x86_64 board-name: CHR FreeBSD BHYVE platform: MikroTik [admin@lab1.i.lfns.org.uk] > /system/resource/pci/print Columns: DEVICE, VENDOR, NAME, IRQ # DEVICE VENDOR NAME IRQ 0 00:00.0 Network Appliance Corporation unknown device (rev: 0) 0 1 00:04.0 unknown unknown (rev: 0) 0 2 00:05.0 Red Hat, Inc. Virtio network device (rev: 0) 10 3 00:05.1 Red Hat, Inc. Virtio network device (rev: 0) 10 4 00:05.2 Red Hat, Inc. Virtio network device (rev: 0) 11 5 00:06.0 Chelsio Communications Inc T540-CR Unified Wire Ethernet Controller [VF] (rev: 0) 0 6 00:1f.0 Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II] (rev: 0) 0 [admin@lab1.i.lfns.org.uk] > /interface/print Flags: R - RUNNING Columns: NAME, TYPE, ACTUAL-MTU, MAC-ADDRESS # NAME TYPE ACTUAL-MTU MAC-ADDRESS 0 R ether1 ether 1500 06:00:00:00:05:08 1 R ether2 ether 1500 06:00:00:00:05:09 2 R ether3 ether 1500 06:00:00:00:05:0C 3 R lo loopback 65536 00:00:00:00:00:00 [admin@lab1.i.lfns.org.uk] > ``` thanks jaclaz, this works a lot better than the x86 image (if only for improved licensing :-)unfortunately though, it still does not seem to include the driver for the T540 VF:
```
i didn't see anything in all_packages that seems relevant either.


---
```

## Response 2
Author: Sat Oct 26, 2024 10:57 am
Yep, it’s also up to the host OS drivers to enable SR-IOV support.correct. host OS has SR-IOV enabled, this is working in all virtual machines on this host except for RouterOS VM.The virtual machine can check if SR-IOV is available, but if you try to turn it on without driver support, you’ll just get an error or warning.right. please read my original post, which is about whether RouterOS x86 / CHR has driver for Chelsio T540-CR VF device. i do not get error or warning, but device does not appear in /interface/print.this is nothing to do with FreeBSD - question is whether RouterOS has driver for this device. ---

## Response 3
Author: Sat Oct 26, 2024 11:07 am
please read my original post, which is about whether RouterOS x86 / CHR has driver for Chelsio T540-CR VF device. i do not get error or warning, but device does not appear in /interface/print. this is nothing to do with FreeBSD - question is whether RouterOS has driver for this device.This is where you might be misunderstanding things. It’s all about the virtual machine support at the host OS level, not the guest OS.RouterOS x86 and CHR are completely different. RouterOS x86 is for bare-metal installations, while CHR is designed for virtual machines that require proper support for virtual drivers. If the virtual drivers in the virtual host and its host OS aren’t set up correctly, you won’t be able to use them in CHR. ---

## Response 4
Author: Sat Oct 26, 2024 11:20 am
``` 1? 3!media ~% lspci -v 00:00.0 Host bridge: Network Appliance Corporation Device 1275 Flags: bus master, fast devsel, latency 0 Capabilities: <access denied> 00:04.0 Non-Volatile memory controller: Device fb5d:0a0a (prog-if 02 [NVM Express]) Flags: bus master, fast devsel, latency 0 Memory at 800004000 (64-bit, non-prefetchable) [size=16K] Memory at c000e000 (32-bit, non-prefetchable) [size=8K] Capabilities: <access denied> Kernel driver in use: nvme 00:05.0 SCSI storage controller: Red Hat, Inc. Virtio filesystem Subsystem: Red Hat, Inc. Device 0009 Flags: bus master, fast devsel, latency 64, IRQ 18 I/O ports at 2000 [size=512] Memory at c000c000 (32-bit, non-prefetchable) [size=8K] Capabilities: <access denied> Kernel driver in use: virtio-pci 00:06.0 Non-Volatile memory controller: Device fb5d:0a0a (prog-if 02 [NVM Express]) Flags: bus master, fast devsel, latency 0 Memory at 800000000 (64-bit, non-prefetchable) [size=16K] Memory at c000a000 (32-bit, non-prefetchable) [size=8K] Capabilities: <access denied> Kernel driver in use: nvme 00:07.0 Ethernet controller: Chelsio Communications Inc T540-CR Unified Wire Ethernet Controller [VF] Subsystem: Chelsio Communications Inc Device 0000 Flags: bus master, fast devsel, latency 0 Memory at c0010000 (32-bit, non-prefetchable) [size=4K] Memory at c0000000 (32-bit, non-prefetchable) [size=32K] Memory at c0008000 (32-bit, non-prefetchable) [size=8K] Capabilities: <access denied> Kernel driver in use: cxgb4vf 00:1f.0 ISA bridge: Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II] Flags: bus master, fast devsel, latency 0 4!media ~% ``` ``` [ 1.021179] cxgb4vf 0000:00:07.0: Using assigned MAC ACL: 06:00:00:00:05:a2 [ 1.024707] cxgb4vf 0000:00:07.0: eth0: Chelsio VF NIC PCIe MSI-X [ 7.057836] cxgb4vf 0000:00:07.0: eth0: passive DA port module inserted [ 7.057847] cxgb4vf 0000:00:07.0 eth0: link up, 10Gbps, full-duplex, RX/TX PAUSE ``` ``` # ip addr show dev eth0 2: eth0: <BROADCAST, MULTICAST, UP, LOWER_UP> mtu 9000 qdisc mq state UP qlen 1000 link/ether 06:00:00:00:05:a2 brd ff:ff:ff:ff:ff:ff ``` let me provide an example from a non-RouterOS Linux system, which is a VM with a T540 VF PCI passthrough device.we can see the device in lspci:
```
'00:07.0 Ethernet controller: Chelsio Communications Inc T540-CR Unified Wire Ethernet Controller [VF]' - this is our Virtual Function device, exposed from the host via PCI passthrough.and you can see lspci says "Kernel driver in use: cxgb4vf" - meaning the Linux kernel in the VM has attached the "cxgb4vf" driver to this device.and in "dmesg" we can see the Linux kernel has detected this as a network device:
```

```
and indeed this network device shows up in Linux:
```

```
the problem i'm reporting in this thread is that, apparently, the RouterOS kernel is missing "cxgb4vf" driver, so it cannot detect the PCI device as a network interface.


---
```

## Response 5
Author: [SOLVED]Mon Oct 28, 2024 3:41 pm
``` [admin@lab1.i.lfns.org.uk] > /ip/neighbor/print Columns: INTERFACE, ADDRESS, MAC-ADDRESS, IDENTITY, VERSION, BOARD # INTERFACE ADDRESS MAC-ADDRESS IDENTITY VERSION BOARD 0 ether2 fe80::400:ff:fe00:50a 06:00:00:00:05:0A lab2.i.lfns.org.uk 7.16.1 (stable) 2024-10-10 14:03:32 CHR 1 ether3 fe80::400:ff:fe00:50b 06:00:00:00:05:0B lab3.i.lfns.org.uk 7.16.1 (stable) 2024-10-10 14:03:32 CHR 2 ether4 fe80::400:ff:fe00:5a3 06:00:00:00:05:A3 lab1.i.lfns.org.uk 7.17_ab236 (development) 2024-10-28 12:06:23 CHR 3 ether4 fe80::400:ff:fe00:601 74:4D:28:08:81:F6 c1.i.lfns.org.uk 7.16 (stable) 2024-09-20 13:00:27 CRS309-1G-8S+ [admin@lab1.i.lfns.org.uk] > ``` today MikroTik support sent me a development release (7.17_ab236) which adds support for the T540 VF! so hopefully this will be in 7.17.0.i did notice a strange bug where the router can see itself in /ip/neighbor/print:
```
but i think (based on a recent converstaion with Chelsio support) that this is a hardware bug in the NIC's switch chip, not a RouterOS bug.  we'll see how it actually works when i get around to testing it properly.
```
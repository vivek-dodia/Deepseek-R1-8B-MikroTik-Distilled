# Document Information
Title: MikroTik wired interface compatibility
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/220233794/MikroTik+wired+interface+compatibility,

# Content
# MikroTik SFP/SFP+/SFP28/QSFP+/QSFP28 compatibility
This article shows the compatibility of MikroTik devices with SFP, SFP+, SFP28, QSFP+, and QSFP28 transceivers. It features detailed compatibility tables that provide valuable insights into which transceivers are suitable for use with MikroTik devices. Additionally, some practical configuration examples are provided using the RouterOS CLI to set different data transmission rates.For more detailed descriptions of properties, please refer to theEthernetuser manual.
# 1G SFP
Model | S-RJ01 | S-85DLC05D | S-31DLC20D | S-3553LC20D | S-55DLC80D | S-4554LC80D | SFP CWDM | SFP1m/3mDAC | S+AO0005AOC | SFP281m/3mDAC
CCR1072-1G-8S+ | + | + | + | + | + | + | + | + | + | +
CCR1036-12G-4S | + | + | + | + | + | + | + | + | + | +
CCR1036-8G-2S+ | + | + | + | + | + | + | + | + | + | +
CCR1016-12S-1S+ | +1 | +1 | +1 | +1 | +1 | +1 | + | + | + | +
CCR1009-7G-1C | + | + | + | + | + | + | + | + | + | +
CCR1009-8G-1S-1S+ | + | + | + | + | + | + | + | + | + | +
CCR1009-7G-1C-1S+ | + | + | + | + | + | + | + | + | + | +
CCR2004-1G-2XS-PCIe | - | - | - | - | - | - | - | - | - | -
CCR2004-1G-12S+2XS | + | + | + | + | + | + | + | + | + | +
CCR2004-16G-2S+ | + | + | + | + | + | + | + | + | + | +
CCR2116-12G-4S+ | + | + | + | + | + | + | + | + | + | +
CCR2216-1G-12XS-2XQ | + | + | + | + | + | + | + | + | + | +
CRS125-24G-1S | + | + | + | + | + | + | + | + | + | +
CRS305-1G-4S+ | + | + | + | + | + | + | + | + | + | +
CRS309-1G-8S+ | + | + | + | + | + | + | + | + | + | +
CRS312-4C+8XG | - | + | + | + | + | + | + | + | + | +
CRS318-1Fi-15Fr-2S | + | + | + | + | + | + | + | + | + | +
CRS318-16P-2S+ | + | + | + | + | + | + | + | + | + | +
CSS318-16G-2S+ | + | + | + | + | + | + | + | + | + | +
CRS320-8P-8B-4S+ | + | + | + | + | + | + | + | + | + | +
CRS326-4C+20G+2Q+ | + | + | + | + | + | + | + | + | + | +
CRS326-24S+2Q+ | + | + | + | + | + | + | + | + | + | +
CRS354-48G/P-4S+2Q+ | + | + | + | + | + | + | + | + | + | +
CRS520-4XS-16XQ | + | + | + | + | + | + | + | + | + | +
CRS518-16XS-2XQ | + | + | + | + | + | + | + | + | + | +
CRS510-8XS-2XQ | + | + | + | + | + | + | + | + | + | +
CSS/CRS326-24G-2S+ | + | + | + | + | + | + | + | + | + | +
CRS317-1G-16S+ | + | + | + | + | + | + | + | + | + | +
CRS328-4C-20S-4S+ | + | + | + | + | + | + | + | + | + | +
CRS328-24P-4S+ | + | + | + | + | + | + | + | + | + | +
CRS226-24G-2S+ | - | +2 | +2 | +2 | +2 | +2 | + | + | + | +
CRS212-1G-10S-1S+ | +1 | +1 | +1 | +1 | +1 | +1 | + | + | + | +
CRS210-8G-2S+ | - | +2 | +2 | +2 | +2 | +2 | + | + | + | +
CRS112-8G/P-4S | + | + | + | + | + | + | + | + | + | +
CRS109-8G-1S | + | + | + | + | + | + | + | + | + | +
CRS106-1C-5S/FiberBox | + | + | + | + | + | + | + | + | + | +
RB5009 | + | + | + | + | + | + | + | + | + | +
RB4011 | + | + | + | + | + | + | + | + | + | +
RB3011 | + | + | + | + | + | + | + | + | + | +
RB2011 | + | + | + | + | + | + | + | + | + | +
L009 | + | + | + | + | + | + | + | +14 | +14 | +14
RB260/CSS106 | + | + | + | + | + | + | + | + | + | +
RB922/921 | + | + | + | + | + | + | + | + | + | +
RB953GS | + | + | + | + | + | + | + | + | + | +
hAP AC | + | + | + | + | + | + | + | + | + | +
hEX PoE/PowerBox Pro | + | + | + | + | + | + | + | + | + | +
hEX S | + | + | + | + | + | + | + | + | + | +
RBFTC11 | + | +8 | +8 | +8 | +8 | +8 | +8 | +8 | +8 | +8
FTC11XG | + | + | + | + | + | + | + | + | + | +
LHG XL 52 ac | - | + | + | + | + | + | + | + | + | +
RBD22/D23mANTBox 52 15s/NetMetal ac² | - | + | + | + | + | + | + | + | + | +
L22/mANTBox ax 15sL23/NetMetal ax | + | +15 | +15 | +15 | +15 | +15 | +15 | +14 | +14 | +14
GPEN21 | + | + | + | + | + | + | + | + | + | +
CSS610 | + | + | + | + | + | + | + | + | + | +
CRS310-1G-5S-4S+/netFiber 9 | + | + | + | + | + | + | + | + | + | +
CRS310-8G+2S+IN | + | + | + | + | + | + | + | + | + | +
mANTBox 52 15s/NetMetal ac²
L22/mANTBox ax 15sL23/NetMetal ax
# 10G SFP+/25G SFP28
Model | S+RJ10 | S+85DLC03D | S+31DLC10D | S+2332LC10D | SFP+ CWDM | SFP+1m/3mDAC | S+AO0005AOC | Q+BC0003-S+ | XQ+BC0003-XS+ | SFP281m/3mDAC | SFP28XS+31LC10D | SFP28XS+2733LC15D | SFP28XS+85LC01D
CCR1072-1G-8S+ | + | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CCR1036-12G-4S | - | + | + | + | + | + | + | - | - | + | + | + | +
CCR1036-8G-2S+ | + | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CCR1016-12S-1S+ | +10 | + | + | + | + | + | + | +1,5 | +1,5 | + | + | + | +
CCR1009-7G-1C | - | + | + | + | + | + | + | - | - | + | + | + | +
CCR1009-8G-1S-1S+ | +10 | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CCR1009-7G-1C-1S+ | + | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CCR2004-1G-2XS-PCIe | + | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CCR2004-1G-12S+2XS | +11 | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CCR2004-16G-2S+ | + | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CCR2116-12G-4S+ | + | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CCR2216-1G-12XS-2XQ | + | + | + | + | + | + | + | + | + | + | + | + | +
CRS125-24G-1S | - | + | + | + | + | + | + | - | - | + | + | + | +
CRS305-1G-4S+ | +7 | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CRS309-1G-8S+ | +4 | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CRS312-4C+8XG | + | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CRS318-1Fi-15Fr-2S | - | + | + | + | + | + | + | - | - | + | + | + | +
CRS318-16P-2S+ | + | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CSS318-16G-2S+ | + | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CRS320-8P-8B-4S+ | + | + | + | + | + | + | + | + | + | + | + | + | +
CRS326-4C+20G+2Q+ | + | + | + | + | + | + | + | + | + | + | + | + | +
CRS326-24S+2Q+ | +6 | + | + | + | + | + | + | + | + | + | + | + | +
CRS354-48G/P-4S+2Q+ | + | + | + | + | + | + | + | + | + | + | + | + | +
CRS520-4XS-16XQ | + | + | + | + | + | + | + | + | + | + | + | + | +
CRS518-16XS-2XQ | + | + | + | + | + | + | + | + | + | + | + | + | +
CRS510-8XS-2XQ | + | + | + | + | + | + | + | + | + | + | + | + | +
CSS/CRS326-24G-2S+ | + | + | + | + | + | + | + | +5 | +5 | + | +9 | +9 | +
CRS317-1G-16S+ | +3 | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CRS328-4C-20S-4S+ | +10 | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CRS328-24P-4S+ | + | + | + | + | + | + | + | +5 | +5 | + | +9 | +9 | +
CRS226-24G-2S+ | + | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CRS212-1G-10S-1S+ | +10 | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CRS210-8G-2S+ | + | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CRS112-8G/P-4S | - | + | + | + | + | + | + | - | - | + | + | + | +
CRS109-8G-1S | - | + | + | + | + | + | + | - | - | + | + | + | +
CRS106-1C-5S/FiberBox | - | + | + | + | + | + | + | - | - | + | + | + | +
RB5009 | + | + | + | + | + | + | + | +5 | +5 | + | + | + | +
RB4011 | + | + | + | + | + | + | + | + | + | + | + | + | +
RB3011 | - | + | + | + | + | + | + | - | - | + | + | + | +
RB2011 | - | + | + | + | + | + | + | - | - | + | + | + | +
L009 | - | +14 | +14 | +14 | +14 | +14 | +14 | +14 | +14 | +14 | +14 | +14 | +14
RB260/CSS106 | - | + | + | + | + | + | + | - | - | + | + | + | +
RB922/921 | - | + | + | + | + | + | + | - | - | + | + | + | +
RB953GS | - | + | + | + | + | + | + | - | - | + | + | + | +
hAP AC | - | + | + | + | + | + | + | - | - | + | + | + | +
hEX PoE/PowerBox Pro | - | + | + | + | + | + | + | - | - | + | + | + | +
hEX S | - | + | + | + | + | + | + | - | - | + | + | + | +
RBFTC11 | - | +8 | +8 | +8 | +8 | +8 | +8 | - | - | +8 | +8 | +8 | +8
FTC11XG | + | + | + | + | + | + | + | +5 | +5 | + | + | + | +
LHG XL 52 ac | - | + | + | + | + | + | + | - | - | + | + | + | +
RBD22/D23mANTBox 52 15s/NetMetal ac² | - | + | + | + | + | + | + | - | - | + | + | + | +
L22/mANTBox ax 15sL23/NetMetal ax | - | +14 | +14 | +14 | +14 | +14 | +14 | +14 | +14 | +14 | +14 | +14 | +14
CSS610 | + | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CRS310-1G-5S-4S+/netFiber 9 | +10 | + | + | + | + | + | + | +5 | +5 | + | + | + | +
CRS310-8G+2S+IN | + | + | + | + | + | + | + | +5 | +5 | + | + | + | +
SFP28XS+85LC01D
mANTBox 52 15s/NetMetal ac²
# 40G QSFP+
Model | QSFP+Q+DA0001 | Q+85MP01D | Q+BC0003-S+
CRS326-4C+20G+2Q+ | + | + | +
CRS326-24S+2Q+ | + | + | +
CRS354-48G/P-4S+2Q+ | + | + | +
CRS504-4XQ-IN | + | + | +
CRS504-4XQ-OUT | +13 | + | +13
CRS510-8XS-2XQ | + | + | +
CRS518-16XS-2XQ | + | + | +
CRS520-4XS-16XQ | + | + | +
CCR2216-1G-12XS-2XQ | + | + | +
# 100G QSFP28
Model | XQ+31LC10D | XQ+31LC02D | XQ+85MP01D | XQ+DA0001 | XQ+DA0003 | XQ+BC0003-XS+ | XQ+CM0000-XS+
CRS326-4C+20G+2Q+ | - | - | + | + | + | + | +
CRS326-24S+2Q+ | - | - | + | + | + | + | +
CRS354-48G/P-4S+2Q+ | - | - | + | + | + | + | +
CRS504-4XQ-IN | + | + | + | + | + | + | +
CRS504-4XQ-OUT | + | + | + | +13 | +13 | +13 | +
CRS510-8XS-2XQ | + | + | + | + | + | + | +
CRS518-16XS-2XQ | + | + | + | + | + | + | +
CRS520-4XS-16XQ | + | + | + | + | + | + | +
CCR2216-1G-12XS-2XQ | + | + | + | + | + | + | +
Legend |
Color codes: | Not supported | Check notes below
# S-RJ01
Table that states in what link rates if mounted in specific MikroTik devices S-RJ01 module will be able to work. Use these modules only withauto-negotiationenabled, forced link speeds are not supported. They will negotiate to correct duplex and highest possible rate.
Model | 1000 | 100 | 10
RB5009 | + | + | +
RB4011 | + | + | +
RB3011 | + | + | +
RB922 | + | + | +
RB921 | + | + | +
hAP ac | + | + | +
hEX PoE | + | + | +
hEX S | + | - | -
RB953 | +/+ | -/+ | -/+
RB2011 | + | - | -
RB260/CSS106 | + | - | -
RBFTC11 | + | - | -
LHG XL 52 ac | - | - | -
RBD22/D23mANTBox 52 15s/NetMetal ac² | - | - | -
CRS106 | + | + | +
CRS112 | + | + | +
CRS125/CRS109 | + | + | +
CRS212 | + | + | +
CRS226/CRS210 | - | - | -
CSS/CRS305-1G-4S+ | + | + | +
CSS/CRS309-1G-8S+ | + | + | +
CRS318-1Fi-15Fr-2S | + | + | +
CRS318-16P-2S+ | + | + | +
CSS/CRS326-24G-2S+ | + | + | +
CRS354 | + | + | +
CSS/CRS328-4C-20S-4S+ | + | + | +
CSS/CRS328-24P-4S+ | + | + | +
CSS/CRS317-1G-16S+ | + | + | +
CRS326-4C+20G+2Q+ | + | + | +
CRS326-24S+2Q+ | + | + | +
CSS610 | + | + | +
FTC11XG | + | + | +
CRS310-1G-5S-4S+/netFiber 9 | + | + | +
CRS310-8G+2S+IN | + | + | +
CCR1009 | +/+ | +/+ | +/+
CCR1016-12S-1S+ | + | + | +
CCR1036-12G-4S | + | + | +
CCR1036-8G-2S+ | + | + | +
CCR1072-1G-8S+ | + | + | +
mANTBox 52 15s/NetMetal ac²
# 10 Gigabit Ethernet
# S+RJ10
Use these modules only in 10G SFP+ ports withauto-negotiationenabled, forced link speeds and configurable link speed advertisements are not supported. They will negotiate to correct duplex and highest possible rate. For proper S+RJ10 module installation and recommended use case scenarios, please readS+RJ10 General Guidance.
Speed | Cable type | S+RJ10 to Ethernet port
--------------------------------------------
10BASE-T | Cat5e/6 | 100m
100BASE-T | Cat5e/6 | 100m
1000BASE-T | Cat5e/6 | 100m
2.5GBASE-T | Cat5e/6 UTP | 100m
2.5GBASE-T | Cat5e/6 STP | 100m
5GBASE-T | Cat5e/6 | 100m
10GBASE-T | Cat6/7 | 30m
The latest revision of S+RJ10 contains "/r2" by the end of serial number. It comes with following improvements:
Link Speed | Max MTU
--------------------
10Gbps | 10218
5Gbps | 10218
2.5Gbps | 10218
1000Mbps | 1504
100Mbps | 1504
10Mbps | 1504
# CRS312-4C+8XG
10GE ports maximum supported cable length.
Speed | Cable type | 10 Gigabit Ethernet ports
----------------------------------------------
10BASE-T | Cat5e/6 | 100m
100BASE-T | Cat5e/6 | 100m
1000BASE-T | Cat5e/6 | 100m
2.5GBASE-T | Cat5e/6 | 100m
5GBASE-T | Cat5e/6 | 100m
10GBASE-T | Cat6/7 | 30m
# SFP interface compatibility with 100M optical transceivers
SFP interface on the listed devices is compatible withfast ethernet fiberlinks.
Compatible devices (interface):
# SFP+ interface compatibility with 1G optical transceivers
For MikroTik devices with SFP+ interface that support both 10G and 1G link rate, following settings must be set on both linked devices for required interfaces. These settings only relate when optical SFP transceivers are used. In order to get them working in 1G link rate, use the following configuration:
```
# Since RouterOS v7.12
/interface ethernet set sfp-sfpplus1 auto-negotiation=no speed=1G-baseX
# Older RouterOS
/interface ethernet set sfp-sfpplus1 auto-negotiation=no speed=1Gbps full-duplex=yes
```
Devices which SFP+ ports support 1G links:
Devices which SFP+ interfaces can be used only for 10G links:
# SFP+ interface compatibility with 10G/25G optical transceivers
MikroTik devices with SFP+ ports can establish 10G links using 10G/25G optical fiber transceivers, however additional SFP Rate Select setting must be configured to avoid data corruption during transmission. The following settings are required on the SFP+ interface:
```
# Since RouterOS v7.12
/interface ethernet set sfp-sfpplus1 auto-negotiation=no speed=10G-baseSR-LR sfp-rate-select=low
# Older RouterOS
/interface ethernet set sfp-sfpplus1 auto-negotiation=no speed=10Gbps full-duplex=yes sfp-rate-select=low
```
This requirement applies to MikroTik 10G/25G modules:
# SFP+/SFP28 interface compatibility with 2.5G transceivers
The 2.5G link rate support is implemented since RouterOS v7.3. MikroTik devices with SFP+ and SFP28 interfaces that support 2.5G link rate require following settings to be set on both linked device interfaces.
```
# Since RouterOS v7.12
/interface ethernet set sfp-sfpplus1 auto-negotiation=no speed=2.5G-baseX
# Older RouterOS
/interface ethernet set sfp-sfpplus1 auto-negotiation=no speed=2.5Gbps full-duplex=yes
```
Devices which support 2.5G links in SFP/SFP+/SFP28 ports:
# QSFP+/QSFP28 interface supported link rates
In RouterOS, QSFP+ and QSFP28 interfaces are designed to handle high-speed data transmission by utilizing multiple channels. Each QSFP+ or QSFP28 interface is divided into four sub-interfaces, each corresponding to a transmission channel necessary for proper operation.
Below are examples of how QSFP+ and QSFP28 interfaces appear in RouterOS:
```
# QSFP+
/interface ethernet print
Flags: R - RUNNING
Columns: NAME, MTU, MAC-ADDRESS, ARP, SWITCH
# NAME            MTU  MAC-ADDRESS        ARP      SWITCH
1   qsfpplus1-1    1500  48:8F:5A:B6:09:8C  enabled  switch1
2   qsfpplus1-2    1500  48:8F:5A:B6:09:8D  enabled  switch1
3   qsfpplus1-3    1500  48:8F:5A:B6:09:8E  enabled  switch1
4   qsfpplus1-4    1500  48:8F:5A:B6:09:8F  enabled  switch1
# QSFP28
/interface ethernet print
Flags: R - RUNNING
Columns: NAME, MTU, MAC-ADDRESS, ARP, SWITCH
# NAME         MTU  MAC-ADDRESS        ARP      SWITCH
1   qsfp28-1-1  1500  DC:2C:6E:9E:11:14  enabled  switch1
2   qsfp28-1-2  1500  DC:2C:6E:9E:11:15  enabled  switch1
3   qsfp28-1-3  1500  DC:2C:6E:9E:11:16  enabled  switch1
4   qsfp28-1-4  1500  DC:2C:6E:9E:11:17  enabled  switch1
```
Configuration and monitoring for these sub-interfaces may vary based on factors such as auto-negotiation, advertised speeds, and the type of transceiver (e.g., break-out cable or single fiber). The following sections will provide guidance on the configuration necessary for each use case.
# QSFP+
For MikroTik CRS3xx series devices, QSFP+ interfaces support the following link speeds:
Link Configuration:
Starting from RouterOS version 7.12, in addition to choosing the right transmission rate, it's important to specify the correct link mode. For example, you might useCR4for DAC(Direct Attach Copper) orSR4-LR4for optical fiber.
Configuration Examples:
For RouterOS v7.12 and later:
```
# 1x40G - DAC
/interface ethernet set qsfpplus1-1 auto-negotiation=no speed=40G-baseCR4
# 1x40G - Optical
/interface ethernet set qsfpplus1-1 auto-negotiation=no speed=40G-baseSR4-LR4
# 4x10G - DAC
/interface ethernet set qsfpplus1-1 auto-negotiation=no speed=10G-baseCR
/interface ethernet set qsfpplus1-2 auto-negotiation=no speed=10G-baseCR
/interface ethernet set qsfpplus1-3 auto-negotiation=no speed=10G-baseCR
/interface ethernet set qsfpplus1-4 auto-negotiation=no speed=10G-baseCR
# 4x10G - Optical
/interface ethernet set qsfpplus1-1 auto-negotiation=no speed=10G-baseSR-LR
/interface ethernet set qsfpplus1-2 auto-negotiation=no speed=10G-baseSR-LR
/interface ethernet set qsfpplus1-3 auto-negotiation=no speed=10G-baseSR-LR
/interface ethernet set qsfpplus1-4 auto-negotiation=no speed=10G-baseSR-LR
```
For RouterOS versions earlier than v7.12:
```
# 1x40G - DAC/Optical
/interface ethernet set qsfpplus1-1 auto-negotiation=no speed=40Gbps full-duplex=yes
# 4x10G - DAC/Optical
/interface ethernet set qsfpplus1-1 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface ethernet set qsfpplus1-2 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface ethernet set qsfpplus1-3 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface ethernet set qsfpplus1-4 auto-negotiation=no speed=10Gbps full-duplex=yes
```
# QSFP28
For MikroTik CRS5xx series and CCR2216 devices, QSFP28 interfaces support the following link speeds:
Link Configuration:
Starting from RouterOS version 7.12, in addition to choosing the right transmission rate, it's important to specify the correct link mode. For example, you might useCR4for DAC(Direct Attach Copper) orSR4-LR4for optical fiber.
Configuration Examples:
For RouterOS v7.12 and later:
```
# 1x100G - DAC
/interface ethernet set qsfp28-1-1 auto-negotiation=no speed=100G-baseCR4
# 1x100G - Optical
/interface ethernet set qsfp28-2-1 auto-negotiation=no speed=100G-baseSR4-LR4
# 2x50G - DAC
/interface ethernet set qsfp28-1-1 auto-negotiation=no speed=50G-baseCR2
/interface ethernet set qsfp28-1-3 auto-negotiation=no speed=50G-baseCR2
# 2x50G - Optical
/interface ethernet set qsfp28-1-1 auto-negotiation=no speed=50G-baseSR2-LR2
/interface ethernet set qsfp28-1-3 auto-negotiation=no speed=50G-baseSR2-LR2
# 4x25G - DAC
/interface ethernet set qsfp28-1-1 auto-negotiation=no speed=25G-baseCR
/interface ethernet set qsfp28-1-2 auto-negotiation=no speed=25G-baseCR
/interface ethernet set qsfp28-1-3 auto-negotiation=no speed=25G-baseCR
/interface ethernet set qsfp28-1-4 auto-negotiation=no speed=25G-baseCR
# 4x25G - Optical
/interface ethernet set qsfp28-1-1 auto-negotiation=no speed=25G-baseSR-LR
/interface ethernet set qsfp28-1-2 auto-negotiation=no speed=25G-baseSR-LR
/interface ethernet set qsfp28-1-3 auto-negotiation=no speed=25G-baseSR-LR
/interface ethernet set qsfp28-1-4 auto-negotiation=no speed=25G-baseSR-LR
```
For RouterOS versions earlier than v7.12:
```
# 1x100G - DAC/Optical
/interface ethernet set qsfp28-1-1 auto-negotiation=no speed=100Gbps full-duplex=yes
# 4x25G - DAC/Optical
/interface ethernet set qsfp28-1-1 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface ethernet set qsfp28-1-2 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface ethernet set qsfp28-1-3 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface ethernet set qsfp28-1-4 auto-negotiation=no speed=25Gbps full-duplex=yes
```
# QSFP+/QSFP28 interface compatibility with breakout cables
MikroTik devices can establish links between QSFP+/QSFP28 and SFP+/SFP28 ports using breakout cables.
Configuration Examples:
For RouterOS v7.12 and later:
```
# QSFP+ - DAC
/interface ethernet set qsfpplus1-1 auto-negotiation=no speed=10G-baseCR
/interface ethernet set qsfpplus1-2 auto-negotiation=no speed=10G-baseCR
/interface ethernet set qsfpplus1-3 auto-negotiation=no speed=10G-baseCR
/interface ethernet set qsfpplus1-4 auto-negotiation=no speed=10G-baseCR
# QSFP+ - Optical
/interface ethernet set qsfpplus1-1 auto-negotiation=no speed=10G-baseSR-LR
/interface ethernet set qsfpplus1-2 auto-negotiation=no speed=10G-baseSR-LR
/interface ethernet set qsfpplus1-3 auto-negotiation=no speed=10G-baseSR-LR
/interface ethernet set qsfpplus1-4 auto-negotiation=no speed=10G-baseSR-LR
# QSFP28 - DAC
/interface ethernet set qsfp28-1-1 auto-negotiation=no speed=25G-baseCR
/interface ethernet set qsfp28-1-2 auto-negotiation=no speed=25G-baseCR
/interface ethernet set qsfp28-1-3 auto-negotiation=no speed=25G-baseCR
/interface ethernet set qsfp28-1-4 auto-negotiation=no speed=25G-baseCR
# QSFP28 - Optical
/interface ethernet set qsfp28-1-1 auto-negotiation=no speed=25G-baseSR-LR
/interface ethernet set qsfp28-1-2 auto-negotiation=no speed=25G-baseSR-LR
/interface ethernet set qsfp28-1-3 auto-negotiation=no speed=25G-baseSR-LR
/interface ethernet set qsfp28-1-4 auto-negotiation=no speed=25G-baseSR-LR
```
It is also possible to use QSFP28 to 2x50G QSFP28 Breakout Cables:
```
# 2x50G - DAC
/interface ethernet set qsfp28-1-1 auto-negotiation=no speed=50G-baseCR2
/interface ethernet set qsfp28-1-3 auto-negotiation=no speed=50G-baseCR2
# 2x50G - Optical
/interface ethernet set qsfp28-1-1 auto-negotiation=no speed=50G-baseSR2-LR2
/interface ethernet set qsfp28-1-3 auto-negotiation=no speed=50G-baseSR2-LR2
```
Or to configure different speed rates for each QSFP+/QSFP28 sub-interfaces:
```
# QSFP28 - DAC
/interface ethernet set qsfp28-1-1 auto-negotiation=no speed=25G-baseCR
/interface ethernet set qsfp28-1-2 auto-negotiation=no speed=25G-baseCR
/interface ethernet set qsfp28-1-3 auto-negotiation=no speed=10G-baseCR
/interface ethernet set qsfp28-1-4 auto-negotiation=no speed=10G-baseCR
# QSFP28 - Optical
/interface ethernet set qsfp28-1-1 auto-negotiation=no speed=25G-baseSR-LR
/interface ethernet set qsfp28-1-2 auto-negotiation=no speed=25G-baseSR-LR
/interface ethernet set qsfp28-1-3 auto-negotiation=no speed=10G-baseSR-LR
/interface ethernet set qsfp28-1-4 auto-negotiation=no speed=10G-baseSR-LR
```
For RouterOS versions earlier than v7.12:
```
# QSFP+ - DAC/Optical
/interface ethernet set qsfpplus1-1 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface ethernet set qsfpplus1-2 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface ethernet set qsfpplus1-3 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface ethernet set qsfpplus1-4 auto-negotiation=no speed=10Gbps full-duplex=yes
# QSFP28 - DAC/Optical
/interface ethernet set qsfp28-1-1 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface ethernet set qsfp28-1-2 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface ethernet set qsfp28-1-3 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface ethernet set qsfp28-1-4 auto-negotiation=no speed=25Gbps full-duplex=yes
```
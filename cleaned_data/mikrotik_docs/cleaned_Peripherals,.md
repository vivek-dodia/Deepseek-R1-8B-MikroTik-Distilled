# Document Information
Title: Peripherals
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/13500447/Peripherals,

# Content
This article describes supported add-on peripherals for RouterBOARD hardware devices.
# Cellular modems
RouterOS v7 supported cellular modems:
Please note:
# Cellular modems
Model | vendor-id | device-id | Tested RouterOS version | Comments | Format
---------------------------------------------------------------------------
Alcatel IK40 |  |  | v6.41RC11 | LTE interface, Modem can be configured only through modems configuration WEB page. | USB
Alcatel IK41 |  |  | v6.48 | Config-less LTE interface | USB
Android usb tethering interface |  |  | v6.7 | Some settings are ignored. | USB
AnyData ADU-E630WH |  |  | v6 | ( aka "USB Wireless HSDPA/UMTS 2.1GHz GSM/GPRS/EGPRS 900/17000MHz/CDMA 1x EVDO Rev.A") | USB
Anteniti 3372h-153 |  |  | 7.12 |  | USB
BandRich C501 |  |  | v5.25 and v6.0 |  | USB
CinterionLTE Modem | 0x1e2d | 0x0061 | v7.14 and higher | LTE interface, Some settings are ignored. Not full SMS functionality. | MiniPCI-e
D-link DWM-157 | 0x2001 | 0x7d02 | v6.xx | Works! Data Channel: 2, Info Channel: 3,Modem Init: AT+CFUN=1, vendor-id="0x2001" device-id="0x7d02" Some info from modem: > H/W Ver.: B1, F/W Ver.: 2.0.1eu, revision: +CGMR: MOLY.WR8.W1231.DC.WG.MP.V3, 2013/04/09 02:08 Different HW revisions might not work with RouterOS | USB
D-link DWM-222 |  |  | v6.38 | Multiple modem versions with same marketing name exist, only H/W ver: A1 supported as config-less LTE interface | USB
Dell DW5821e |  |  | v7.4beta4 and higher | MBIM driver. Revision: T77W968.F1.0.0.5.2.VZ.013 044 | M.2
Dell DW5821e-eSIM | 0x413c | 0x81e0 | 7.11 and higher | MBIM driver. FW: T77W968.F1.0.0.5.2.GC.013. "at-chat" support added | M.2
DELL T99W175 | 0x05c6 | 0x90d5 | 7.16 and higher | MBIM driver. FW: T99W175.F0.1.0.0.9.GC.004. "at-chat" support added | M.2
Dell Wireless 5530 HSPA |  |  | v6.1 and higher | Data channel 0, Info channel 0, init: AT+CFUN=1 (needs manualy change profile by command AT*ENAP=1,1) | MiniPCI-e
Ericsson F5521gw |  |  | v6.x and higher |  | MiniPCI-e
Fibocom FM150-AE/FM150-NA | 0x2cb7 | 0x0111 | v7.1beta5 | MBIM driver. Revision: 89603.1000.00.01.01.03 | M.2
Fibocom NL-952-EAU |  |  | v7.1beta5 | MBIM driver. Revision: 19600.7000.00.04.01.05 | M.2
Marvell PXA1802 based modems | 0x1286 | 0x4e31 | v7.2.2 |  | mini-PCIe
Huawei E153 |  |  | v6.31< and higher |  | USB
Huawei E171 |  |  | v6.xx | Works! ppp interface, vendorid=0x12d1 deviceid=0x140c | USB
Huawei e3131 |  |  | v6.xx and higher | ppp interface | USB
Huawei E3372h, E5576h, E8372h | 0x12d1 | 0x14db | v6.8 | Config-less LTE interface for modems with vendor-id="0x12d1" device-id="0x14db"Models with suffixes -320 and -608 will not work with RouterOS v6, please use v7 insteadModels with suffixes -325 works only with arm cpu | USB
Huawei E3276-150 |  |  | v6.xx | ppp interface | USB
Huawei E3351 |  |  | v6.24 and higher |  | USB
Huawei E3531 |  |  | v6.24 or 6.40RC25 | There are different versions of this modem E3531-6 works from version 6.40RC25 as ppp, mbim supported only from RouterOS V7 | USB
Huawei e398 |  |  | v6.xx and higher | ppp interface | USB
Huawei E5377 |  |  | v6.36.1 | MIFI unit. No serial support, but works with IP on LTE interface | USB
Huawei E5673s-609 |  |  | v6.xx | LTE interface | USB
Huawei K5160 |  |  | v6.37v7.0beta6 | v6 and v7 - config-less LTE interfacev7 - by default will try to use modem in MBIM mode | USB
Huawei K5161 |  |  | v6.47 | Config-less LTE interface | USB
Huawei ME909s-120 |  |  | v6.28 | Recommended modem firmware version 11.617.24.00.00To reduce LTE interface IP subnet mask to /32 configure modem with at-chat command:/interface lte at-chat [find] input="AT^CUSTFEATURE=3,1" | MiniPCI-e
Huawei ME909u-521 |  |  | v6.11 |  | MiniPCI-e
Huawei MU609 |  |  | v6.11 |  | MiniPCI-e
Huawei MU709s-2 |  |  | v6.28 |  | MiniPCI-e
Huawei MS2372h-517 |  |  | v7.12beta3 | ppp/serial interface | USB
Jaton MT421e |  |  | v6.40RC32 | LTE interface with Ethernet emulation (no configuration possible), LTE supported bands 42/43 | MiniPCI-e
Netgear Unite Explore 815S |  |  | v6.41 | MIFI unit. No serial support, but works with IP on LTE interface. | USB
Novatel USB730L |  |  | v6.41RC6 | LTE interface | USB
Olivetti Olicard 500 |  |  | v6.41RC11 | ppp interface | USB
Quectel EC20/EC21 |  |  | v6.xx | ppp interface, there is page in wiki about Quectel:article | MiniPCI-e
Quectel BG77 | 0x2c7c | 0x0700 | v6.47 | Serial/PPP interface, single AT/modem channel | OEM module
Quectel BG95-M3 |  |  | v6.47 | Serial/PPP interface, single AT/modem channelWill not work in wAP R ac boards. | mini-PCIe
Quectel BG96 |  |  | v6.45 | Serial/PPP interface, 2x AT/modem channels | mini-PCIe
Quectel EC25-EU | 0x2c7c | 0x0125 | v6.42 | ppp/LTE interface, there is page in wiki about Quectel ppp mode:articleRouterOS v6  CDC-ECM mode - LTE interface receive address in modems internal network.RouterOS v7 MBIM mode -  LTE interface uses APN IP address. | MiniPCI-e
Quectel EG25-G | 0x2c7c | 0x0125 | 6.48.3 | RouterOS v6  CDC-ECM mode - LTE interface receive address in modems internal network.RouterOS v7 MBIM mode -  LTE interface uses APN IP address.In some boards may be required to disable SIM hot plug detection:/interface lte set [find] modem-init="AT+QSIMDET=0,1" | MiniPCI-e
Quectel EM12-G | 0x2c7c | 0x0512 | v7.1beta5 | MBIM driver | m.2
Quectel EP06 |  |  | v6.42 | ppp/LTE interface, there is page in wiki about Quectel:article | MiniPCI-e
Quectel RM500Q-GL | 0x2c7c | 0x0800 | v7.1beta6 | MBIM driver | m.2
Quectel RM500Q-AE | 0x2c7c | 0x0800 | v7.1beta6 | MBIM driver | m.2
Quectel RM502Q-AE | 0x2c7c | 0x0800 | v7.1beta5 | MBIM driver | m.2
Quectel RM510Q-GL | 0x2c7c | 0x0800 | 7.9 | MBIM driver | m.2
Quectel UC15 |  |  | v6.xx | Works, ppp interface | MiniPCI-e
Quectel UC20 |  |  | v6.xx | Works, ppp interface | MiniPCI-e
R11e-4G | 0x2cd2 | 0x0003 | v6.42 | LTE interface. Supports multiple APN passthrough. | MiniPCI-e
R11e-LTE6 | 0x2cd2 | 0x0004 | v6.39.2 | LTE interface. Supports multiple APN passthrough. | MiniPCI-e
R11e-LTE | 0x2cd2 | 0x0001 | v6.39.2 | LTE interface. Supports multiple APN passthrough. | MiniPCI-e
Sierra Netgear AirCard 320U |  |  | 6.41 | Customer tested the modem with firmware 03.05.23 | USB
Sierra wireless MC73xx |  |  | v6.xx(ppp) v7.xx (LTE) | Works! PPP interface. And starting with v7.xx it will support LTE interface with modem switched to expose the MBIM interface. MC7304 tested with firmware SWI9X15C_05.05.67.00 | MiniPCI-e
Sierra Wireless MC7430 |  |  | v6.xx and higher | Data channel 2, Info channel 2, Modem init: AT+CGATT=0, Dial-command: AT+CGATT=1;D*99# , also needs 3.0 pins isolated (PINS:23,25,27,31,33) | MiniPCI-e
Sierra Wireless MC74xx |  |  | v7.1 | Basic functionality support for modems with MBIM interface/USB composition | mini-PCIe
Sierra Wireless MC7455 |  |  | v7.3beta37 | MBIM mode with extended support for USB compositions:1009 - diag,modem,mbim100D - diag,nmea,modem,mbim | mini-PCIe
Sierra Wireless MC7710/MC7700/MC7750 |  |  | v5.25, v6.0 and 6.40RC43 | If modem uses firmware 3.5 it should be upgraded to 3.5.23.2 firmware release in order to work in RouterOS correctly again. | MiniPCI-e
SIMcom SIM5360 |  |  | v6.xx | Works! Using PPP interface, vendor-id="0x05c6" device-id="0x9000" | MiniPCI-e / USB w/ converter
SIMcom SIM7100 | 0x1e0e | 0x9001 | v6.xx(ppp) v7.xx (LTE) | Works! PPP interface. And starting with v7.xx it will support LTE interface. | MiniPCI-e / USB w/ converter
SIMCom SIM8202G-M.2 |  |  | v7.11 | MBIM driver supported: AT+CUSBCFG=usbid,1e0e,901e | m.2
SXT LTE |  |  | v6 | LTE interface. Old version of SXT LTE | Built-in
Tele2.ru LTE-D402 |  |  | v6.47 | Config-less LTE interface |
Telecom NZ T-Stick ZTE MF-181 |  |  | v6.0rc13 | Data Channel=2, Info Channel=2, APNinternet.telecom.co.nz, PHONE=*99# . Tested ok for both data and SMS on CCR1016-12G | USB
Telit FN980m |  |  | v7.5 | AT# USBCFG=2 | m.2
Telit LE910 | 0x1bc7 | 0x1201 | v6.xx | ppp interface | MiniPCI-e
Telit LE910C1 |  |  | v6.46 | Non-configurable from RouterOS | MiniPCI-e
Telit LM940 |  |  | v6.44 | LTE interface in some cases needs 3.0 pins isolated (PINS:23,25,27,29,31,33) | MiniPCI-e
Telit LM960 |  |  | v6.46 | LTE interface in some cases needs 3.0 pins isolated (PINS:23,25,27,29,31,33) | MiniPCI-e
TPS (Turning Point Solution) GCT450 |  |  | v6.48 | Config-less LTE interface | MiniPCI-e
Vodafone (Huawei) K4203 |  |  | v7.xx | Not supported in ROS v6, but as this modem supports MBIM drivers support will be possible in ROS v7. | USB
Vodafone K4201-Z |  |  | v6.8 | Some settings are ignored. LTE interface. | USB
Vodafone K4305 |  |  | v6.7 | Some settings are ignored. | USB
Vodafone K5160 |  |  | v6.37 | Some settings are ignored. | USB
Yota LU150 |  |  | v5.22 and v6.4 | Some settings are ignored. | USB
Yota wifi modem |  |  | v6.7 | Some settings are ignored. | USB
Yota WLTUBA-107 |  |  | v6.0 | Some settings are ignored. | USB
ZTE 821D |  |  | v6.x | Set Info channel = 1, Data channel = 3, Dial command=ATDT | USB
ZTE AC5730 |  |  | v6.x |  | USB
ZTE ME3630-E |  |  | v6.40RC26 | ppp and LTE interface | MiniPCI-e
ZTE MF110 |  |  | v6.28 and higher | Set info channel = 2, data channel = 2, Dial command=ATM1L3DT | USB
ZTE MF823 |  |  | v6.8 | Some settings are ignored. For some devices it's needed to enter in FACTORY mode to change operating state. | USB
ZTE MF825A |  |  | v6.xx | Some settings are ignored. | USB
ZTE MF827 |  |  | v6.8 | Some settings are ignored. | USB
ZTE MF832S |  |  | v7.10 | Config-less support, may require to set some settings using at-chat or modem init string | USB
ZTE MF90 |  |  | v6.44beta32 and higher | LTE interface | USB
Multiple modem versions with same marketing name exist, only H/W ver: A1 supported as config-less LTE interface
Config-less LTE interface for modems with vendor-id="0x12d1" device-id="0x14db"
Models with suffixes -320 and -608 will not work with RouterOS v6, please use v7 instead
Models with suffixes -325 works only with arm cpu
v6.37
v7.0beta6
v6 and v7 - config-less LTE interface
v7 - by default will try to use modem in MBIM mode
Huawei MU709s-2
Huawei MS2372h-517
Serial/PPP interface, single AT/modem channel
Will not work in wAP R ac boards.
ppp/LTE interface, there is page in wiki about Quectel ppp mode:article
RouterOS v6  CDC-ECM mode - LTE interface receive address in modems internal network.
RouterOS v7 MBIM mode -  LTE interface uses APN IP address.
RouterOS v6  CDC-ECM mode - LTE interface receive address in modems internal network.
RouterOS v7 MBIM mode -  LTE interface uses APN IP address.
In some boards may be required to disable SIM hot plug detection:
```
/interface lte set [find] modem-init="AT+QSIMDET=0,1"
```
Basic functionality support for modems with MBIM interface/USB composition
MBIM mode with extended support for USB compositions:
For some modems with USB3.0 support in some cases USB3.0 pins need to be isolated to ensure correct initialization:
# SFP modules
Brand | Model | Rate | Connector/Cable type | Wavelength | Tested with | Works / Doesn't
----------------------------------------------------------------------------------------
MikroTik | S-85DLC05D | 1,25G | Dual LC, MM | 850nm | *Check:SFP/SFP+ compatibility reference table | Natively supported
MikroTik | S-31DLC20D | 1,25G | Dual LC, SM | 1310nm | *Check:SFP/SFP+ compatibility reference table | Natively supported
MikroTik | S-35LC20D | 1,25G | BiDi LC, SM | Tx:1310nm/Rx:1550nm | *Check:SFP/SFP+ compatibility reference table | Natively supported
MikroTik | S-53LC20D | 1,25G | BiDi LC, SM | Tx:1550nm/Rx:1310nm | *Check:SFP/SFP+ compatibility reference table | Natively supported
MikroTik | S-RJ01 | 1000/100/10 | RJ45, Cat5/Cat6 | N/A | *Check:SFP/SFP+ compatibility reference table | Natively supported
Axiom | AXG91632 | 1000BASE-LX | Dual LC | 1310nm | CRS125-24G-1S-RM | Works!
Finisar | FCLF-8521-3 | 10/100/1000 | RJ45, Cat6 | N/A | RB2011LS-IN | Works!
Finisar | FCLF-8521-3-MD | 10/100/1000 | RJ45, Cat6 | N/A | RB2011LS-IN | Works!
Finisar | FTRJ8519P1BNL-B1 | 10/100/1000 1.25 Gb/s 1000Base-SX Ethernet | Dual LC, MM | 850nm | RB2011LS-IN | Works!
Finisar | FTLF8519P2BNL | 10/100/1000 1.25 Gb/s 1000Base-SX Ethernet | Dual LC, MM | 850nm | RB2011LS-IN | Works!
Finisar | FTRJ1319P1BTL | 1.25Gb/s 1000Base-LX Ethernet | Dual LC, SM | 1310nm | CCR1009-8G-1S-1S+ and CCR1009-7G-1C-1S+ | Works!
Unica | SFP-1.25G-T | 1000M | RJ45, Cat6 | N/A | RB2011LS-IN | Works!
Dell | FTLX8571D3BCL | 1,25G | Dual LC, MM | 850nm | RB2011LS-IN | Works!
Unica | GP-3124-L2CD-C | 1,25G | Dual LC, MM | 1310nm | RB2011LS-IN | Works!
Cisco | GLC-T | 1.25G | RJ45, Cat6 | N/A | RB2011LS-IN | Works!
Cisco | GLC-SX-MM | 1000BASE-SX SFP transceiver module for MMF, 1.25G | Dual LC, MM | 850nm | RB2011LS-IN | Works!
Cisco | SFP-GE-L | 1000BASE-LX/LH SFP transceiver module for SMF, 1.25G | Dual LC, SM | 1300nm | Various MT hardware | Works!
6COM | 6C-SFP-T | 10/100/1000 | RJ45, Cat6 | N/A | RB2011LS-IN | Works!
6COM | 6C-WDM-0210BSD | 1,25G | BiDi SC, SM | Tx:1550nm/Rx:1310nm | RB2011LS-IN | Works!
6COM | 6C-WDM-0210ASD | 1,25G | BiDi SC, SM | Tx:1310nm/Rx:1550nm | RB2011LS-IN | Works!
6COM | 6C-SFP-0310D | 1,25G | Dual LC, MM | 1310nm | RB2011LS-IN | Works!
6COM | 6C-SFP-0301D | 1,25G | Dual LC, MM | 850nm | RB2011LS-IN | Works!
Ingellen | INSP-T(10/100/1000) | 10/100/1000 | RJ45, Cat6 | N/A | RB2011LS-IN | Works!
Ingellen | INSPL-53-BX | 1,25G | BiDi LC, MM | 1550/1310 | RB2011LS-IN | Works!
Ingellen | INSPL-35-BX | 1,25G | BiDi LC, MM | 1310/1550 | RB2011LS-IN | Works!
Ingellen | INSP-LX-SM | 1,25G | Dual LC, SM | 1310nm | RB2011LS-IN | Works!
Ingellen | INSP-SX-MM | 1,25G | Dual LC, MM | 850nm | RB2011LS-IN | Works!
AXCEN | AXGT-R1T4-05I1 | 10/100/1000 | RJ45, Cat6 | N/A | RB2011LS-IN | Works!
AXCEN | AXGD-37А4-0531 | 1,25G | BiDi LC, MM | Tx:1550nm/Rx:1310nm | RB2011LS-IN | Works!
AXCEN | AXGD-16А4-0531 | 1,25G | BiDi LC, MM | Tx:1310nm/Rx:1550nm | RB2011LS-IN | Works!
AXCEN | AXGD-1354-0531 | 1,25G | Dual LC, MM | 1310nm | RB2011LS-IN | Works!
AXCEN | AXGD-5854-0511 | 1,25G | Dual LC, MM | 850nm | RB2011LS-IN | Works!
TP-Link | TL-SM311LS | 1,25G | Dual LC, SM | 1310nm | RB2011LS-IN | Works!
TP-Link | TL-SM311LM | 1,25G | Dual LC, MM | 850nm | CCR1036 12G-4S | Works!
OPTIC | OPTIC-SFP-3524S-02-SC | 1,25G | BiDi SC, SM | Tx:1310nm/Rx:1550nm | RB2011UAS-RM, RB260GS | Works!
OPTIC | OPTIC-SFP-5324S-02-SC | 1,25G | BiDi SC, SM | Tx:1550nm/Rx:1310nm | RB2011UAS-RM, RB260GS | Works!
OPTIC | OPTIC-SFP-S1203-L3302-LC | 1,25G | BiDi LC, SM | Tx:1310nm/Rx:1550nm | RB2011UAS-RM, RB260GS | Works!
OPTIC | OPTIC-SFP-S1205-L3302-LC | 1,25G | BiDi LC, SM | Tx:1550nm/Rx:1310nm | RB2011UAS-RM, RB260GS | Works!
ROBOFiber | SFP-7120-55 | 1,25G | Dual LC, SM | 1550nm | CCR1036-12G-4S, RB2011 | Works!
ROBOFiber | SFP-7120-WA | 1,25G | BiDi LC, MM | Tx:1490nm/Rx:1550nm | CCR, RB2011 | Works!
ROBOFiber | SFP-7120-WB | 1,25G | BiDi LC, MM | Tx:1550nm/Rx:1490nm | CCR, RB2011 | Works!
Enguity | SFP-3647603KM.b1310 XT | 1,25G | BiDi LC, SM | Tx:1310nm/Rx:1550nm | CCR, RB2011, RB260GS | Works!
Enguity | SFP-3647603KM.b1550 XT | 1,25G | BiDi LC, SM | Tx:1550nm/Rx:1310nm | CCR, RB2011, RB260GS | Works!
Enguity | SFP-3647610KM.b1490 XT | 1,25G | BiDi LC, SM | Tx:1490nm/Rx:1550nm | CCR, RB2011, RB260GS | Works!
Enguity | SFP-3647610KM.b1550 XT | 1,25G | BiDi LC, SM | Tx:1550nm/Rx:1490nm | CCR, RB2011, RB260GS | Works!
AdvOptics MSA | GLC-SX-MM | 1,25G | BiDi LC, MM | Tx:1310nm/Rx:1310nm | CCR, RB2011, RB260GS | Works!
AdvOptics MSA | GLC-ZX-SM | 1,25G | BiDi LC, SM | Tx:1310nm/Rx:1310nm | CCR, RB2011, RB260GS | Works!
Proline | GLC-BX-D20-PRO | 1,25G | BiDi LC, SM | Tx:1490nm/Rx:1310nm | CRS125 | Works!
Proline | GLC-BX-D40-PRO | 1,25G | BiDi LC, SM | Tx:1310nm/Rx:1490nm | CRS125 | Works!
Foundry Networks | E1MG-BXU-AC | 1,25G | BiDi LC, SM | Tx:1310nm/Rx:1490nm | RB3011UiAS, hAP ac | Works!
Avago | SFBR-5799APZ | 1,25G | Dual LC, MM | 850nm | CRS326, CRS112 | Works in 1Gbps mode!
Eltex | NTU-SFP-100 | 1,25G | SC | N/A | RB4011iGS+ | Works!
# SFP+ modules
Brand | Model | Distance | Rate | Connector/Cable type | Wavelength | Tested with | Works / Doesn't
---------------------------------------------------------------------------------------------------
MikroTik | S+85DLC03D | 300m | 10G | Dual LC, MM | 850nm | All MikroTik products with SFP/SFP+ interfaces | Natively supported
MikroTik | S+31DLC10D | 10km | 10G | Dual LC, SM | 1310nm | All MikroTik products with SFP/SFP+ interfaces | Natively supported
MikroTik | S+23LC10D | 10km | 10G | BiDi LC, SM | Tx:1270nm/Rx:1330nm | All MikroTik products with SFP/SFP+ interfaces | Natively supported
MikroTik | S+32LC10D | 10km | 10G | BiDi LC, SM | Tx:1330nm/Rx:1270nm | All MikroTik products with SFP/SFP+ interfaces | Natively supported
MikroTik | S+DA0001 | 1m | 10G | Twinax Copper | N/A | All MikroTik products with SFP/SFP+ interfaces | Natively supported
MikroTik | S+DA0003 | 3m | 10G | Twinax Copper | N/A | All MikroTik products with SFP/SFP+ interfaces | Natively supported
MikroTik | S+RJ10 | various, depending on link rate. Check brochure for more details | 10G/5G/2.5G/1G/100M/10M | RJ45 - Cat5E/Cat6/Cat7 | N/A | All MikroTik products with SFP+ interfaces | Natively supported
Atop | APSP55B30CDL40 | 40km | 10G | Dual LC, SM | 1550nm | CRS series, CCR series devices with SFP+ interfaces | Does NOT work!
Cisco | SFP-10G-LR | 10km | 10G | Dual LC, SM | 1310nm | RB2011LS-IN | Works!
Dell (Finisar) | FTLX8571D3BCL | 300m | 10G | Dual LC, MM | 850nm | Most of SFP/SFP+ MikroTik products | Works!
Juniper (Finisar) | FTLX8571D3BCL-J1 | 300m | 10G | Dual LC, MM | 850nm | Most of SFP/SFP+ MikroTik products | Works!
Intel (Finisar) | FTLX8571D3BCV-IT | 300m | 10G | Dual LC, MM | 850nm | Most of SFP/SFP+ MikroTik products | Works!
OEM (Juniper?) | EX-SFP-10GE-SR-OEM | 300m | 10G | Dual LC, MM | 850nm | Most of SFP/SFP+ MikroTik products | Works!
Fiberstore | SFP-10G31-40 | 40km | 10G | Dual LC, SM | 1310nm | CRS series, CCR series devices with SFP+ interfaces | Works!
Fiberstore | SFP-10G55-40 | 40km | 10G | Dual LC, SM | 1310nm | CRS series, CCR series devices with SFP+ interfaces | Works!
Fiberstore | SFP-10G32-40 | 40km | 10G | BiDi LC, SM | Tx:1330nm/Rx:1270nm | CRS series, CCR series devices with SFP+ interfaces | Works!
Fiberstore | SFP-10G23-40 | 40km | 10G | BiDi LC, SM | Tx:1270nm/Rx:1330nm | CRS series, CCR series devices with SFP+ interfaces | Works!
Optech | OPAK-TX1-00-C | 30m | 10G | RJ45 - Cat 6a/7 Cable | N/A | CCR, CCR, CSS series devices with SFP+ interfaces | Works, starting with v6.40rc20 RouterOS build.
ProLabs | SFP-10G-T-C | 30m | 10G | RJ45 - Cat 6a/7 Cable | N/A | CCR, CCR, CSS series devices with SFP+ interfaces | Works, starting with v6.40rc20 RouterOS build.
* No labels
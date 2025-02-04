# Document Information
Title: Software Specifications
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/19136707/Software+Specifications,

# Content
# Hardware Support
MikroTik made devices:RouterOS is  compatible with MikroTik hardware it comes preinstalled on. Even MikroTik devices that are no longer manufactured, can run the latest RouterOS versions and will receive software updates. There are a few exceptions to this for the very oldest product lines.The latest RouterOS v7 is not compatible with all MIPS-LE family of devices (such as RB100, series, some RB700 series devices etc. please check the architecture of the device in question). It is also not compatible with MikroTik devices that have 32MB of RAM or less, but a minimum of 64MB is suggested. In short, there is no set limit on software compatibility or upgrades. Even devices that are no longer manufactured for 20 years, will still receive software updates, as long as they have enough RAM and are not based on a MIPS-LE CPU.
3rd party devices:RouterOS can also be run on 3rd party devices if they meet the following requirements:
# Installation
# Configuration
# Backup/Restore
# Firewall
# Routing
# MPLS
# VPN
# Wireless
# DHCP
# Hotspot
# QoS
# Proxy
# Tools
# Other features
# Kernel version
# Supported Encryptions
RouterOS 7 is used for the management of network (telecommunication) devices.
RouterOS 7 includes encryption features (components), intended for data (information) security, passed through telecommunication channels and device control channels.
All encryption features (components) are an integral part of RouterOS 7 and can not be changed by the end-users.
RouterOS 7 is intended for installation by end-users without significant support from the vendor.
RouterOS 7 uses the following security protocols:
Supported security protocol | Encryption algorithm | Maximum key length
-----------------------------------------------------------------------
IPSec | DES | 56 bit
3DES | 168 bit
AES | 128, 192, 256 bit
Blowfish | 448 bit
Twofish | 256 bit
Camelia | 128, 192, 256 bit
PPTP (with MPPE) | RC4 | 128 bit
L2TP (with MPPE) | RC4 | 128 bit
SNMP | DES | 56 bit
AES | 128 bit
SSH | Blowfish | 128 bit
3DES | 192 bit
AES | 128, 192, 256 bit
SSTP | AES | 256 bit
RC4 | 128 bit
Used in WinBox connection (nameless) | AES | 128 bit
WEP | RC4 | 104 bit
WPA-TKIP | RC4 | 128 bit
WPA2-TKIP | RC4 | 128 bit
WPA-AES | AES | 128 bit
WPA2-AES | AES | 128 bit
HTTPS | NULL, RC4, DES, DES40, 3DES, AES | 128, 192, 256 bit
IPSec
SSH
SSTP
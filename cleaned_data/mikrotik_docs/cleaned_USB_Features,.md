# Document Information
Title: USB Features
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/130220183/USB+Features,

# Content
# Summary
Sub-menu:/system routerboard usbPackage:system (v6, v7)
```
/system routerboard usb
```
```
ystem (v6, v7)
```
This article describes RouterBoard device supported USB features.
# USB Power Reset
USB power reset turns off USB port power for a specified time. It is useful when 3G/LTE modem needs to be restarted but there is no physical access to it.
Available properties:
For example, turn off USB port power for 10 seconds:
```
/system routerboard usb power-reset duration=10s
```
RouterBoards with multiple USB buses also require a bus specified in order to do a USB power reset.Available properties:
# USB Port Type
RB912UAG and RB953GS have partially shared USB port and miniPCIe slot. Due to hardware restrictions it is possible to use only one at the time for 3G/LTE modem.
```
[admin@MikroTik] > /system routerboard usb set type=
USB-type-A  mini-PCIe
```
Available properties:
# USB Port Mode
RB2011 series, CRS1xx series, and mAP have micro USB port which operates in host mode when USB device is attached through USB OTG cable. Some vendor cables require forced host mode to recognize connected device.
Available properties:
# RouterBoard USB Port Limitations
Some RouterBoard devices have notable USB port limitations.
* RB mAP 2n - does not support USB Power Reset* RB750UP - does not support USB Power Reset* RB751U-2HnD - does not support USB Power Reset* RB751G-2HnD - does not support USB Power Reset* RB411U - does not support USB Power Reset* RB411UAHR - does not support USB Power Reset and USB Powering (USB power injectoris required)* RB433UAH - does not support USB Power Reset* RB435G - does not support USB Power Reset* RB493G - does not support USB Power Reset and USB Powering (USB power injectoris required)
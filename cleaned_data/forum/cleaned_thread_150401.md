# Thread Information
Title: Thread-150401
Section: RouterOS
Thread ID: 150401

# Discussion

## Initial Question
Just curious, what Linux version will/is ROS v7 be running under the hood ?(Noting v6 is running v3.3.5) ---

## Response 1
As far as I read from other post, 4.x ---

## Response 2
It is even possible that there will be v7 linux kernel for v7 routerOs ---

## Response 3
It is even possible that there will be v7 linux kernel for v7 routerOsYes, i think everything is possible abtuet The last 5 years... ---

## Response 4
Version kernel 4.14.131 RouterOS 7 ---

## Response 5
AFAIK. Because Tile(ra) architecture (CCR) support is dropped after kernel v4.14.x ---

## Response 6
AFAIK. Because Tile(ra) architecture (CCR) support is dropped after kernel v4.14.xAccording to Normisthey don't use kernel's support for Tile so this won't affect them: ---

## Response 7
It's version 5.6.3.(You can check it in ros npk package (lib/modules/xxx) ---

## Response 8
```
[admin@MikroTik] > /system/package/print 
Columns: NAME, VERSION, BUILD-TIME, SIZE
# NAME      VERSION  BUILD-TIME           SIZE   
0 routeros  7.16.1   2024-10-10 14:03:32  11.7MiB

[admin@MikroTik] > /system/resource/usb/print 
Columns: DEVICE, VENDOR, NAME, SPEED
# DEVICE  VENDOR                NAME                  SPEED
0 3-0     Linux 5.6.3 xhci-hcd  xHCI Host Controller   5000
1 1-0     Linux 5.6.3 ehci_hcd  EHCI Host Controller    480
2 2-0     Linux 5.6.3 xhci-hcd  xHCI Host Controller    480
3 1-1     Fibocom               FG621 Module            480

---
```
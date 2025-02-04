# Thread Information
Title: Thread-1115778
Section: RouterOS
Thread ID: 1115778

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
[admin@MikroTik]>/system/package/printColumns:NAME,VERSION,BUILD-TIME,SIZE# NAME      VERSION  BUILD-TIME           SIZE0routeros7.16.12024-10-1014:03:3211.7MiB[admin@MikroTik]>/system/resource/usb/printColumns:DEVICE,VENDOR,NAME,SPEED# DEVICE  VENDOR                NAME                  SPEED03-0Linux5.6.3xhci-hcd  xHCIHostController500011-0Linux5.6.3ehci_hcd  EHCIHostController48022-0Linux5.6.3xhci-hcd  xHCIHostController48031-1FibocomFG621Module480

---
```
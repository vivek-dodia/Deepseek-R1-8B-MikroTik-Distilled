# Thread Information
Title: Thread-1113969
Section: RouterOS
Thread ID: 1113969

# Discussion

## Initial Question
Hi all, I'm trying to mount a usbstick using NFS from rose to a linux client (ubuntu 24.04):on routeros:- formated usb1 using ext4
```
/disk/setusb1 nfs-sharing=yes[andreas@router-ddhome1]/disk>/disk/printFlags:B-BLOCK-DEVICE;M-MOUNTED;n-NFS-SHARINGColumns:SLOT,MODEL,SERIAL,INTERFACE,SIZE,FREE,FS,RAID-MASTER#     SLOT  MODEL                    SERIAL            INTERFACE                  SIZE           FREE  FS    RAID-MASTER0BMnusb1SanDiskU3CruzerMicro432433165750B307USB2.00480Mbps39139404803769630720ext4  none- mounting to linux client kind of works..
```

```
root@testbox2:~#mount-t nfs4192.168.105.1:/ /mnt/root@testbox2:~#ls-l/mnt/total4drwxrwxrwx3root root4096Dec621:53usb1
root@testbox2:~#ls-l/mnt/usb1
ls:cannot open directory'/mnt/usb1':Operationnotpermittedbut I'm not able to list or access files within usb1Mounting to a 2nd routeros device as a nfs client is working.I'm using routeros v7.16.2.Any hints?best regards,Andreas

---
```

## Response 1
Anything in dmesg?If you create a file from the second ros and look at the uid of the file, does it show as 0? ---

## Response 2
Byexample from doc:nfs root directory should be content ofusb1, not root withusb1dir inside.mkdir /mnt/usb1mount -t nfs4 192.168.105.1:/ /mnt/usb1ls -l /mnt/usb1Edit: or not... (then it should not be possible to have multiple disks mounted over nfs)Did you try with
```
mount-t nfs4192.168.105.1:/usb1 /mnt/usb1?Also check if files on disk are accessible in ROS and if TCP port 2049 is accessible from IP of device where mount is performed, from docs:NFS uses port TCP/2049. If the port is not available in disk print detail you will see the state stuck at  nfs-state="mounting"

---
```

## Response 3
Also check if files on disk are accessible in ROS and if TCP port 2049 is accessible from IP of device where mount is performed, from docs:NFS uses port TCP/2049. If the port is not available in disk print detail you will see the state stuck at nfs-state="mounting"Seems you nailed it - I got to the manpage forexportsand it states that the default is to not allow mounting a device within an exported path.
```
crossmntThisoptionissimilar to nohide but it makes it possibleforclients to access all filesystems mounted on a filesystem markedwithcrossmnt.Thuswhena child filesystem"B"ismounted on a parent"A",setting crossmnt on"A"has a similar effect to setting"nohide"on B.Withnohide the child filesystem needs to be explicitly exported.Withcrossmnt it neednot.Ifa childofa crossmnt fileisnotexplicitly
          exported,thenit will be implicitly exportedwiththe sameexportoptionsasthe parent,exceptforfsid=.Thismakes it impossible  tonotexporta  childofa crossmnt filesystem.Ifsome butnotall subordinate filesystemsofa parent are to be exported,thenthey must be ex‐plicitly exportedandthe parent shouldnothave crossmntset.Thenocrossmnt option can explictly disable crossmntifit was previouslyset.Thisisrarely useful.

---
```

## Response 4
hi all, yes tried also:
```
root@testbox2:~#mount-t nfs4192.168.105.1:/usb1 /mnt/usb1
mount.nfs4:Operationnotpermittedfor192.168.105.1:/usb1 on /mnt/usb1

root@testbox2:~#nc-z-v192.168.105.12049Connectionto192.168.105.12049port[tcp/nfs]succeeded!disk on router doesn't show obvious errors.
```

```
[andreas@router-ddhome1]>/disk/printFlags:B-BLOCK-DEVICE;M-MOUNTED;n-NFS-SHARINGColumns:SLOT,MODEL,SERIAL,INTERFACE,SIZE,FREE,FS,RAID-MASTER#     SLOT  MODEL                    SERIAL            INTERFACE                  SIZE           FREE  FS    RAID-MASTER0BMnusb1SanDiskU3CruzerMicro432433165750B307USB2.00480Mbps39139404803769630720ext4  noneno dmesg errors found..best,Andreas

---
```

## Response 5
Try adding--verboseparam onmountcommand to see if any message appears that can be helpful for troubleshooting. Also try with adding-o sys=secparam tomountif error is related to security permissions, on most distributions this is default option. ---

## Response 6
hi all, I was testing from a VM running on my host and access the NFS Server using a host-NAT network. If i used a just routed client everything works fine.
```
root@debian:/home/user# mount -t nfs4 192.168.105.1:/usb1 /mnt/root@debian:/home/user# ls -l /mnt/total404-rw-r--r--1root root393183Dec623:49cert-manager.yaml.16-rw-r--r--1root root3445Dec623:53default.yml
drwx------2root root16384Dec623:39lost+foundThis is fine for me. Thanks for your help!Andreas

---
```
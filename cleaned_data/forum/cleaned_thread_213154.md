# Thread Information
Title: Thread-213154
Section: RouterOS
Thread ID: 213154

# Discussion

## Initial Question
Hi all, I'm trying to mount a usbstick using NFS from rose to a linux client (ubuntu 24.04):on routeros:- formated usb1 using ext4
```
/disk/set usb1 nfs-sharing=yes

[andreas@router-ddhome1] /disk> /disk/print
Flags: B - BLOCK-DEVICE; M - MOUNTED; n - NFS-SHARING
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS, RAID-MASTER
#     SLOT  MODEL                    SERIAL            INTERFACE                  SIZE           FREE  FS    RAID-MASTER
0 BMn usb1  SanDisk U3 Cruzer Micro  432433165750B307  USB 2.00 480Mbps  3 913 940 480  3 769 630 720  ext4  none- mounting to linux client kind of works..
```

```
root@testbox2:~# mount -t nfs4 192.168.105.1:/ /mnt/
root@testbox2:~# ls -l /mnt/
total 4
drwxrwxrwx 3 root root 4096 Dec  6 21:53 usb1
root@testbox2:~# ls -l /mnt/usb1
ls: cannot open directory '/mnt/usb1': Operation not permittedbut I'm not able to list or access files within usb1Mounting to a 2nd routeros device as a nfs client is working.I'm using routeros v7.16.2.Any hints?best regards,Andreas

---
```

## Response 1
Anything in dmesg?If you create a file from the second ros and look at the uid of the file, does it show as 0? ---

## Response 2
Byexample from doc:nfs root directory should be content ofusb1, not root withusb1dir inside.mkdir /mnt/usb1mount -t nfs4 192.168.105.1:/ /mnt/usb1ls -l /mnt/usb1Edit: or not... (then it should not be possible to have multiple disks mounted over nfs)Did you try with
```
mount -t nfs4 192.168.105.1:/usb1 /mnt/usb1?Also check if files on disk are accessible in ROS and if TCP port 2049 is accessible from IP of device where mount is performed, from docs:NFS uses port TCP/2049. If the port is not available in disk print detail you will see the state stuck at  nfs-state="mounting"

---
```

## Response 3
Also check if files on disk are accessible in ROS and if TCP port 2049 is accessible from IP of device where mount is performed, from docs:NFS uses port TCP/2049. If the port is not available in disk print detail you will see the state stuck at nfs-state="mounting"Seems you nailed it - I got to the manpage forexportsand it states that the default is to not allow mounting a device within an exported path.
```
crossmnt
          This option is similar to nohide but it makes it possible for clients to access all filesystems mounted on a filesystem marked with  crossmnt.
          Thus when a child filesystem "B" is mounted on a parent "A", setting crossmnt on "A" has a similar effect to setting "nohide" on B.

          With nohide the child filesystem needs to be explicitly exported.  With crossmnt it need not.  If a child of a crossmnt file is not explicitly
          exported, then it will be implicitly exported with the same export options as the parent, except for fsid=.  This makes it impossible  to  not
          export  a  child  of a crossmnt filesystem.  If some but not all subordinate filesystems of a parent are to be exported, then they must be ex‐
          plicitly exported and the parent should not have crossmnt set.

          The nocrossmnt option can explictly disable crossmnt if it was previously set.  This is rarely useful.

---
```

## Response 4
hi all, yes tried also:
```
root@testbox2:~# mount -t nfs4 192.168.105.1:/usb1 /mnt/usb1
mount.nfs4: Operation not permitted for 192.168.105.1:/usb1 on /mnt/usb1

root@testbox2:~# nc -z -v 192.168.105.1 2049
Connection to 192.168.105.1 2049 port [tcp/nfs] succeeded!disk on router doesn't show obvious errors.
```

```
[andreas@router-ddhome1] > /disk/print
Flags: B - BLOCK-DEVICE; M - MOUNTED; n - NFS-SHARING
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS, RAID-MASTER
#     SLOT  MODEL                    SERIAL            INTERFACE                  SIZE           FREE  FS    RAID-MASTER
0 BMn usb1  SanDisk U3 Cruzer Micro  432433165750B307  USB 2.00 480Mbps  3 913 940 480  3 769 630 720  ext4  noneno dmesg errors found..best,Andreas

---
```

## Response 5
Try adding--verboseparam onmountcommand to see if any message appears that can be helpful for troubleshooting. Also try with adding-o sys=secparam tomountif error is related to security permissions, on most distributions this is default option. ---

## Response 6
hi all, I was testing from a VM running on my host and access the NFS Server using a host-NAT network. If i used a just routed client everything works fine.
```
root@debian:/home/user# mount -t nfs4 192.168.105.1:/usb1 /mnt/
root@debian:/home/user# ls -l /mnt/
total 404
-rw-r--r-- 1 root root 393183 Dec  6 23:49 cert-manager.yaml.16
-rw-r--r-- 1 root root   3445 Dec  6 23:53 default.yml
drwx------ 2 root root  16384 Dec  6 23:39 lost+foundThis is fine for me. Thanks for your help!Andreas

---
```
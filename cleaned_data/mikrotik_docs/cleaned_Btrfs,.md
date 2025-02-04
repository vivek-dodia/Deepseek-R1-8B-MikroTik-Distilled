# Document Information
Title: Btrfs
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/295239711/Btrfs,

# Content
# Summary
Btrfs is a feature-rich copy-on-write file system, most significant features are the following:
# Examples
# Two disk Btrfs-RAID (RAID1)
In case you want to create a reliable data storage solution with just two disks (for example, NAS), then you can follow this these steps to successfully create a RAID1 array with Btrfs:
```
/disk print
```
```
<disk-name-1>
```
```
/disk format-drive <disk-name-1> file-system=btrfs
```
```
/disk/btrfs/filesystem print
```
```
/disk/btrfs/filesystem set [find where present-devs=<disk-name-1>] label=BtrfsRAID
```
```
/disk/btrfs/filesystem/add-device [find where present-devs=<disk-name-1>] device=<disk-name-2>
```
```
/disk/btrfs/filesystem balance-start [find where label=BtrfsRAID] data-profile=raid1 metadata-profile=raid1 system-profile=raid1
```
```
mount-filesystem=no
```
```
/disk set <disk-name-2> mount-filesystem=no
```
```
/disk set <disk-name-1> mount-point-template=BtrfsRAID
```
```
/BtrsRAID/
```
With a reliable storage solution such as Btrfs-RAID consider adding useful features to your RouterOS device by following the suggested guides below:
# Creating subvolumes
The main benefit of creating subvolumes is to organize data on your Btrfs main (root) subvolume. Consider subvolumes as folders with features of a partition, while still sharing the total disk space between all subvolumes. You can later use these subvolumes for much more advanced tasks and it is recommended to create subvolumes when you have large amounts of different types of data, especially that requires frequent backups. Follow the guide to setup a few example subvolumes:
```
/disk print
```
```
<disk-name-1>
```
```
/disk format-drive <disk-name-1> file-system=btrfs
```
```
/disk/btrfs/filesystem set [find where present-devs=<disk-name-1>] label=BtrfsDisk
```
```
/disk set <disk-name-1> mount-point-template=BtrfsDisk
```
```
Documents
```
```
BtrfsDisk
```
```
/disk/btrfs/subvolume/add name=Documents fs=BtrfsDisk
```
```
Photos
```
```
BtrfsDisk
```
```
/disk/btrfs/subvolume/add name=Photos fs=BtrfsDisk
```
```
/disk/btrfs/subvolume/print
```
```
/BtrfsDisk/Documents
```
```
/BtrfsDisk/Photos
```
# Creating snapshots
Snapshots are space efficient way to create backups for your data. By creating a snapshot you save the current state of your data which you can later access.
# NAME
0 BtrfsDisk
1 BtrfsDisk/Documents
2 BtrfsDisk/Photos
3 BtrfsDisk/Documents/document1.txt
4 BtrfsDisk/Photos/photo1.jpg
/disk/btrfs/subvolume/add read-only=yes parent=Photos fs=BtrfsDisk  name=Snapshots/Photos-22012025
# NAME
0 BtrfsDisk
1 BtrfsDisk/Documents
2 BtrfsDisk/Photos
3 BtrfsDisk/Snapshots
4 BtrfsDisk/Documents/document1.txt
5 BtrfsDisk/Photos/photo1.jpg
6 BtrfsDisk/Snapshots/Documents-22012025
7 BtrfsDisk/Snapshots/Photos-22012025
8 BtrfsDisk/Snapshots/Documents-22012025/document1.txt
9 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg
# NAME
0 BtrfsDisk
1 BtrfsDisk/Documents
2 BtrfsDisk/Photos
3 BtrfsDisk/Snapshots
4 BtrfsDisk/Documents/document1.txt
5 BtrfsDisk/Documents/document2.txt
6 BtrfsDisk/Photos/photo1.jpg
7 BtrfsDisk/Photos/photo2.jpg
8 BtrfsDisk/Snapshots/Photos-22012025
9 BtrfsDisk/Snapshots/Documents-22012025
10 BtrfsDisk/Snapshots/Documents-22012025/document1.txt
11 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg
/disk/btrfs/subvolume/add read-only=yes parent=Photos fs=BtrfsDisk  name=Snapshots/Photos-23012025
# NAME
0 BtrfsDisk
1 BtrfsDisk/Documents
2 BtrfsDisk/Photos
3 BtrfsDisk/Snapshots
4 BtrfsDisk/Documents/document1.txt
5 BtrfsDisk/Documents/document2.txt
6 BtrfsDisk/Photos/photo1.jpg
7 BtrfsDisk/Photos/photo2.jpg
8 BtrfsDisk/Snapshots/Photos-22012025
9 BtrfsDisk/Snapshots/Documents-22012025
10 BtrfsDisk/Snapshots/Documents-23012025
11 BtrfsDisk/Snapshots/Photos-23012025
12 BtrfsDisk/Snapshots/Documents-22012025/document1.txt
13 BtrfsDisk/Snapshots/Documents-23012025/document1.txt
14 BtrfsDisk/Snapshots/Documents-23012025/document2.txt
15 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg
16 BtrfsDisk/Snapshots/Photos-23012025/photo1.jpg
17 BtrfsDisk/Snapshots/Photos-23012025/photo2.jpg
/disk/btrfs/subvolume/remove [find where name=Photos-22012025]
```
[admin@MikroTik] > /file print
# NAME
0 BtrfsDisk
1 BtrfsDisk/Documents
2 BtrfsDisk/Photos
3 BtrfsDisk/Documents/document1.txt
4 BtrfsDisk/Photos/photo1.jpg
```
```
/Btrfs/Documents
```
```
/Btrfs/Photos/
```
```
/disk/btrfs/subvolume/print
```
```
Snapshots
```
```
/disk/btrfs/subvolume/add name=Snapshots fs=BtrfsDisk
```
```
Documents
```
```
Photos
```
```
/disk/btrfs/subvolume/add read-only=yes parent=Documents fs=BtrfsDisk  name=Snapshots/Documents-22012025
/disk/btrfs/subvolume/add read-only=yes parent=Photos fs=BtrfsDisk  name=Snapshots/Photos-22012025
```
```
[admin@MikroTik] > /file print
# NAME
0 BtrfsDisk
1 BtrfsDisk/Documents
2 BtrfsDisk/Photos
3 BtrfsDisk/Snapshots
4 BtrfsDisk/Documents/document1.txt
5 BtrfsDisk/Photos/photo1.jpg
6 BtrfsDisk/Snapshots/Documents-22012025
7 BtrfsDisk/Snapshots/Photos-22012025
8 BtrfsDisk/Snapshots/Documents-22012025/document1.txt
9 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg
```
```
[admin@infra1.mikrotikls.lv] > /file print
# NAME
0 BtrfsDisk
1 BtrfsDisk/Documents
2 BtrfsDisk/Photos
3 BtrfsDisk/Snapshots
4 BtrfsDisk/Documents/document1.txt
5 BtrfsDisk/Documents/document2.txt
6 BtrfsDisk/Photos/photo1.jpg
7 BtrfsDisk/Photos/photo2.jpg
8 BtrfsDisk/Snapshots/Photos-22012025
9 BtrfsDisk/Snapshots/Documents-22012025
10 BtrfsDisk/Snapshots/Documents-22012025/document1.txt
11 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg
```
```
/disk/btrfs/subvolume/add read-only=yes parent=Documents fs=BtrfsDisk  name=Snapshots/Documents-23012025
/disk/btrfs/subvolume/add read-only=yes parent=Photos fs=BtrfsDisk  name=Snapshots/Photos-23012025
```
```
[admin@MikroTik] > /file print
# NAME
0 BtrfsDisk
1 BtrfsDisk/Documents
2 BtrfsDisk/Photos
3 BtrfsDisk/Snapshots
4 BtrfsDisk/Documents/document1.txt
5 BtrfsDisk/Documents/document2.txt
6 BtrfsDisk/Photos/photo1.jpg
7 BtrfsDisk/Photos/photo2.jpg
8 BtrfsDisk/Snapshots/Photos-22012025
9 BtrfsDisk/Snapshots/Documents-22012025
10 BtrfsDisk/Snapshots/Documents-23012025
11 BtrfsDisk/Snapshots/Photos-23012025
12 BtrfsDisk/Snapshots/Documents-22012025/document1.txt
13 BtrfsDisk/Snapshots/Documents-23012025/document1.txt
14 BtrfsDisk/Snapshots/Documents-23012025/document2.txt
15 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg
16 BtrfsDisk/Snapshots/Photos-23012025/photo1.jpg
17 BtrfsDisk/Snapshots/Photos-23012025/photo2.jpg
```
```
/disk/btrfs/subvolume/remove [find where name=Documents-22012025]
/disk/btrfs/subvolume/remove [find where name=Photos-22012025]
```
# Transfer your snapshots
Btrfs allows to easily send a snapshot between two devices that is using Btrfs. In this example we will use two RouterOS devices running ROSE-storage package. The RouterOS device containing snapshots that need to be backed up is going to be calledRouterAand the RouterOS device that is going to receive backups is going to be calledRouterB.
```
RouterA
```
```
RouterB
```
/ip/ssh/regenerate-host-key
/file/sync/remove [find where local-path=admin_ed25519_pub.pem]
```
RouterA
```
```
RouterB
```
```
/ip ssh/set host-key-type=ed25519 strong-crypto=yes
/ip/ssh/regenerate-host-key
```
```
RouterA
```
```
/ip/ssh/export-host-key key-file-prefix=admin
```
```
RouterA
```
```
admin
```
```
/user/ssh-keys/private/import private-key-file=admin_ed25519.pem user=admin
```
```
RouterA
```
```
RouterB
```
```
/file/sync/add local-path=admin_ed25519_pub.pem remote-address=RouterB user=admin mode=upload
/file/sync/remove [find where local-path=admin_ed25519_pub.pem]
```
```
RouterB
```
```
btrsfstransfer
```
```
/user/add name=btrfstransfer group=write
```
```
RouterB
```
```
btrfstransfer
```
```
/user/ssh-keys/import public-key-file=admin_ed25519_pub.pem user=btrfstransfer
```
```
RouterA
```
```
send
```
```
/disk/btrfs/transfer add type=send fs=BtrfsDisk ssh-address=RouterB send-subvolumes=Documents-23012025 ssh-user=btrfstransfer ssh-receive-mount=BackupBtrfsDisk/Snapshots
```
```
BtrfsDisk
```
```
/disk/btrfs/filesystem print
```
```
RouterA
```
```
Documents-23012025
```
```
btrsfstransfer
```
```
RouterB
```
```
BackupBtrfsDisk
```
```
/disk/btrfs/filesystem print
```
```
RouterB
```
```
Snapshots
```
```
BackupBtrfsDisk
```
```
RouterB
```
```
receive
```
```
/disk/btrfs/transfer/add fs=BackupBtrfsDisk type=receive file=BackupBtrfsDisk/Snapshots
```
```
BackupBtrfsDisk
```
```
/disk/btrfs/filesystem print
```
```
RouterB
```
```
BackupBtrfsDisk/Snapshots
```
```
Snapshots
```
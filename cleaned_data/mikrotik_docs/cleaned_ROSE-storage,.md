# Document Information
Title: ROSE-storage
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/259031065/ROSE-storage,

# Content
ROSE (RouterOS Enterprise)package adds data center functionality to RouterOS - for supporting disk monitoring, improved formatting, RAIDs, rsync, iSCSI ,NVMe over TCP, NFS. This functionality currently is supported onarm, arm64, x86andtileplatforms.
# Storage Type
# Crypted
Drive or device used together with type=crypted to make "dm_crypt" encrypted storage.dm-cryptis a transparent disk encryption subsystem designed to provide encryption of block devices.
```
dm-crypt
```
# Properties
Property | Description
----------------------
slot(string;Default: ) | Name of the  file system
encryption-key(string;Default: ) | key used to decrypt
crypted-backend(string;Default: ) | Drive or partition to encrypt
# Configuration example:
To create a crypted file-system:
```
add crypted-backend=usb1 encryption-key=strong_key slot=crypted-usb1 type=crypted
```
After it's created format the file system and it's ready to go.
```
disk format-drive crypted-usb1 file-system=btrfs
```
# iSCSI
iSCSIallows accessing storage over an IP-based network. On initiator iSCSI device will appear as block device. RouterOS supports both target and initiator modes.
# Properties
Property | Description
----------------------
iscasi-address | IP address of the iSCSI target. (Host device IP)
iscasi-export | Disables/enables iSCASI on the host device
iscasi-iqn | unique identifier used to name iSCSI target. (In ROS the iqn is the same as slot name, can't be changed and needs to be configured only on the client device)
iscasi-port | network port used by the iSCSI target to listen for incoming connections from initiators. The default port for iSCSI traffic is 3260.
# Configuration example
Host
```
/disk
set pcie1-nvme1 iscsi-export=yes
```
Client
```
/disk
add type=iscsi iscsi-address=192.168.1.1 iscsi-iqn=pcie1-nvme1
```
# NFS
NFSallows sharing local directories over network. RouterOS currently supports NFS v4 only mode.
# Properties
Property | Description
----------------------
nfs-address | IP address of the NFS target. (host device IP)
nfs-share | Specify the folder to mount (client parameter)
nfs-sharing | Disable/enable NFS on the host device
# Configuration example
Host
```
/disk
set pcie1-nvme1 nfs-sharing=yes
```
Client
```
/disk
add type=nfs nfs-address=192.168.1.1
```
Linux client
```
mkdir /mnt/files
mount -t nfs 192.168.1.1:/ /mnt/files
```
# NVME over TCP
nvme-tcpallows accessing storage over network as NVMe block device on initiator side. On target side this device can be hdd/ssd/nvme or even raid array.
# Properties
Property | Description
----------------------
nvme-tcp-address | IP address of the NVME over TCP target. (host device IP)
nvme-tcp-export | Disable/enable NVME over TCP on the host device
nvme-tcp-host-name | This property specifies the hostname of the NVMe over TCP initiator. It can be used for identification and authentication purposes
nvme-tcp-name | This property specifies the name of the NVMe over TCP target or the connection name for reference purposes (needs to be the same as host slot name)
nvme-tcp-password | his property is used to specify the password for authenticating the NVMe over TCP connection, ensuring secure access.
nvme-tcp-port | This property specifies the network port used by the NVMe over TCP target to listen for incoming connections from initiators. The default port for NVMe over TCP traffic is 4420.
nvme-tcp-server-allow-host-name | This property specifies whether the NVMe over TCP server allows connections from specific hostnames, providing a mechanism for host-based access control.
nvme-tcp-server-password | This property specifies the password for the NVMe over TCP server, used for authenticating initiators connecting to the target.
nvme-tcp-server-port | This property specifies the network port used by the NVMe over TCP server to accept connections from initiators.
# Configuration example
Host
```
/disk
set pcie1-nvme2 nvme-tcp-export=yes nvme-tcp-port=4420
```
Client
```
/disk
add type=nvme-tcp nvme-tcp-address=192.168.1.1 nvme-tcp-name=pcie1-nvme1
```
Linux client
Load kernel module
```
modprobe nvme_tcp
```
Discover available nvme-tcp targets
```
nvme discover -t tcp -a 192.168.1.1 -s 4420
```
Discovery Log Number of Records 1, Generation counter 2
=====Discovery Log Entry 0======
trtype:  tcp
adrfam:  ipv4
subtype: nvme subsystem
treq:    not specified, sq flow control disable supported
portid:  4420
trsvcid: 4420
subnqn:  pcie1-nvme1
traddr:  10.155.166.7
sectype: none
```
subnqn should match the slot name and will be used as -n parameter:
```
nvme connect -t tcp -a 192.168.1.1 -s 4420 -n pcie1-nvme1
```
Block devices now should be available:
```
ls /dev/nvme*
```
/dev/nvme0  /dev/nvme0n1  /dev/nvme-fabrics
```
To disconnect:
```
nvme disconnect -d /dev/nvme0
```
where /dev/nvme0 previously mounted device, or disconnect all:
```
nvme disconnect-all
```
# Ramdisk
RAMdisk - allows using part of RAM as attached device (block device). If compared to tmpfs - this allows using RAM as part of raid, or any other configuration where device instead of folder is required.
# Properties
Property | Description
----------------------
ramdisk-size | Size of the block device you want to create
# Configuration example
```
/disk
disk add type=ramdisk ramdisk-size=500M
```
# SMB
SMBis a popular file-sharing protocol. ROSE package currently supports SMB2.1 SMB3.0, SMB3.1.1 dialects (SMB1 is not supported due to security vulnerabilities)
# Properties
Property | Description
----------------------
smb-address | IP address of the SMB server
smb-password | SMB password
smb-share | Name of the share you want to connect to
smb-user | SMB user
# Configuration example
Client
```
add smb-address=10.155.145.11 smb-share=share1 smb-user=user smb-password=password type=smb
```
Server-side configuration can be found -SMB
# Tmpfs
TMPFS - allows using part of RAM as filesystem (can't be used as block device)
# Properties
Property | Description
----------------------
tmpfs-max-size | Size of the block device you want to create
# Configuration example
```
add type=tmpfs tmpfs-max-size=10G
```
# RAID
RAID (Redundant Array of Independent Disks) technology allows storing data on multiple drives - improving data transfer performance, data protection or both by combining them into logical units.
# Properties
Property | Description
----------------------
raid-type | RAID type used (levels 0,1,4,5,6,linear and nested RAID.)
raid-chunk-size | The size of the chunks or stripes used in the RAID array.
raid-device-count | The number of devices (disks) included in the RAID array.
raid-master | Created RAID master block device the disks are added to.
raid-max-component-size | The maximum size of an individual component or disk in the RAID array.
raid-member-failed | Sets the drive in a failed state in RAID array. Used if there is a need to change a non-failed drive
raid-role | Defines the role of each device within the RAID array.
Sets the drive in a failed state in RAID array. Used if there is a need to change a non-failed drive
# Configuration example (RAID6):
This is an example on how to configure RAID, it will be the same procedure in most of RAID types
Create the RAID block device (In this example, RAID 6)
```
add raid-device-count=20 raid-type=6 slot=raid1 type=raid
```
Add drives to this raid
```
set nvme1 raid-master=raid1 raid-role=0
set nvme2 raid-master=raid1 raid-role=1
set nvme3 raid-master=raid1 raid-role=2
set nvme4 raid-master=raid1 raid-role=3
set nvme5 raid-master=raid1 raid-role=4
set nvme6 raid-master=raid1 raid-role=5
set nvme7 raid-master=raid1 raid-role=6
set nvme8 raid-master=raid1 raid-role=7
set nvme9 raid-master=raid1 raid-role=8
set nvme10 raid-master=raid1 raid-role=9
set nvme11 raid-master=raid1 raid-role=10
set nvme12 raid-master=raid1 raid-role=11
set nvme13 raid-master=raid1 raid-role=12
set nvme14 raid-master=raid1 raid-role=13
set nvme15 raid-master=raid1 raid-role=14
set nvme16 raid-master=raid1 raid-role=15
set nvme17 raid-master=raid1 raid-role=16
set nvme18 raid-master=raid1 raid-role=17
set nvme19 raid-master=raid1 raid-role=18
set nvme20 raid-master=raid1 raid-role=19
```
Format the RAID block device
```
disk> format-drive raid1 file-system=btrfs
```
And the result should look similar to this
```
21 BM        type=raid slot="raid1" slot-default="" parent=none uuid="f457bc79-7408-489b-8850-85923e900452" fs=btrfs model="RAID6 2-parity-disks"
size=17 283 541 893 120 free=17 283 538 190 336 raid-type=6 raid-device-count=20 raid-max-component-size=none raid-chunk-size=1M raid-master=none
raid-state="clean" nvme-tcp-export=no iscsi-export=no nfs-sharing=no smb-sharing=no media-sharing=no media-interface=none
```
# RAID 0
All data is written evenly over all disks in this RAID, this configuration does not provide any fault tolerance but provides best performance.
# RAID 1
Same data is written in all drives (data is mirrored), this configuration provides best fault tolerance, but performance wise write speeds will be equal to slowest disk used in array.
# RAID 4
Block-level data is striped to a dedicated disk where parity bits are stored. Performance will be limited to a parity writing speed.
# RAID 5
Block-level data is striped evenly over the available disks. Can be recovered from 1 disk failure.
# RAID 6
Block-level data is striped evenly over the available disks. Can be recovered from 2 disk failures.
# RAID Linear
Data is appended over multiple disks combining them into single large disk. Provides no redundancy and is limited to single disk read/write speed.
# Nested RAID
Combination of multiple RAID configurations into other RAID. For example RAID 10 (RAID 1+0) combines disk mirroring (RAID 1) and disk striping (RAID 0)
# Configuration example
In this example I'm using 20 SSD drives and configuring in RAID (RAID 1+0)
Create a RAID 1 block
```
add raid-device-count=2 raid-type=1 slot=raid10 type=raid
```
Crete two RAID 0 blocks and add them to set the master-raid the previously created RAID 1 block (name=raid10)
```
add raid-device-count=10 raid-master=raid10 raid-role=0 raid-type=0 slot=raid0 type=raid
add raid-device-count=10 raid-master=raid10 raid-role=1 raid-type=0 slot=raid1 type=raid
```
Add drives to each RAID block
```
set nvme1 raid-master=raid1 raid-role=0
set nvme2 raid-master=raid1 raid-role=1
set nvme3 raid-master=raid1 raid-role=2
set nvme4 raid-master=raid1 raid-role=3
set nvme5 raid-master=raid1 raid-role=4
set nvme6 raid-master=raid1 raid-role=5
set nvme7 raid-master=raid1 raid-role=6
set nvme8 raid-master=raid1 raid-role=7
set nvme9 raid-master=raid1 raid-role=8
set nvme10 raid-master=raid1 raid-role=9
set nvme11 raid-master=raid0 raid-role=0
set nvme12 raid-master=raid0 raid-role=1
set nvme13 raid-master=raid0 raid-role=2
set nvme14 raid-master=raid0 raid-role=3
set nvme15 raid-master=raid0 raid-role=4
set nvme16 raid-master=raid0 raid-role=5
set nvme17 raid-master=raid0 raid-role=6
set nvme18 raid-master=raid0 raid-role=7
set nvme19 raid-master=raid0 raid-role=8
set nvme20 raid-master=raid0 raid-role=9
```
After this format, the raid10 block
```
format-drive raid10 file-system=btrfs
```
After formating you should see the free space and use the block
```
23 BM        type=raid slot="raid10" slot-default="" parent=none uuid="ec3344f4-1662-49ab-b899-db1aaa217b0f" fs=btrfs model="RAID1 mirrored" size=9 601 967 652 864
free=9 597 901 369 344 raid-type=1 raid-device-count=2 raid-max-component-size=none raid-master=none raid-state="clean" nvme-tcp-export=no
iscsi-export=no nfs-sharing=no smb-sharing=no media-sharing=no media-interface=none
```
# RSYNC
rsync(Remote Sync) is a powerful file synchronization and file transfer program used in Unix-based systems. It allows for efficient transfer and synchronization of files and directories between different systems or within the same system.If you make changes in a file only changes to files are transferred, reducing data transfer volume. RouterOS RSYNC implementation uses ipsec for data transfer (if password is set). When configured you will see dynamic ipsec entries.
```
rsync
```
Rsync settings can be found in file/sync menu
IPSec dynamic entry example:
```
# PEER                     TUNNEL  SRC-ADDRESS       DST-ADDRESS       PROTOCOL  ACTION   LEVEL    PH2-COUNT
;;; file-sync-10.155.145.11
1  D  file-sync-10.155.145.11  no      10.155.145.17/32  10.155.145.11/32  tcp       encrypt  require          1
/ip/ipsec/peer> print
0  D  name="file-sync-10.155.145.11" address=10.155.145.11/32 local-address=10.155.145.17 profile=default exchange-mode=main send-initial-contact=yes
/ip/ipsec/identity> print
0 D  ;;; file-sync-10.155.145.11
peer=file-sync-10.155.145.11 auth-method=pre-shared-key secret="secret" generate-policy=no
```
# Properties
Property | Description
----------------------
local-path | File/folder path. Used for modeUploadto set the path of the file/folder to upload to the device
mode | Sets if you want to download/upload the file (direction of the sync)
password | Target device password
remote-address | Target devices IP
remote-path | File/folder path. Used with modedownloadto set the path of the target device to be downloaded
user | Target device password
password
remote-address
remote-path
user
# Configuration example
Basic configuration is really easy, on the host device you need to add the file you want to sync to another device, the ip, user/password and the mode.
```
/file sync
add local-path=/ipv6route.txt.rsc mode=upload remote-address=192.168.88.2 remote-path=RAID/
```
If configured correctly, you will see on the host device:
```
0 192.168.88.2  upload  /ipv6route.txt.rsc  RAID/        in sync
```
And on the client device:
```
# REMOTE-ADDRESS   MODE      LOCAL-PATH  REMOTE-PATH         STATUS
0 D 192.168.88.1 download  RAID/       /ipv6route.txt.rsc  in sync
```
# Self-Encryption Drives
For using SED - drives have to beOpal-compliant. Please consult drive manufacturers documentation to find out if particular drive supports this feature before buying drives.RouterOS addso (supported inactive)orO (supported active)flags for supported drives:
```
/disk print
Flags: B - BLOCK-DEVICE; M, F - FORMATTING; o - TCG-OPAL-SELF-ENCRYPTION-SUPPORTED
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS, RAID-MASTER
# SLOT   MODEL                  SERIAL           INTERFACE                   SIZE             FREE  FS    RAID
0 BMo sata1  Samsung SSD 860 2.5in  S3Z9NX0N414510L  SATA 6.0 Gbps  1 000 204 886 016  983 351 111 680  ext4  none
1 BMo sata2  Samsung SSD 860        S5GENG0N307602J  SATA 6.0 Gbps  1 000 204 886 016  983 351 128 064  ext4  none
2 BMO sata3  Samsung SSD 860        S5GENG0N307604H  SATA 6.0 Gbps  1 000 204 886 016  983 351 128 064  ext4  none
3 BMO sata4  Samsung SSD 860 2.5in  S4CSNX0N838150B  SATA 6.0 Gbps  1 000 204 886 016  983 351 128 064  ext4  none
```
To set TCG-OPAL-SELF-ENCRYPTION:
```
/disk
disk set sata1 self-encryption-password=securepassword
```
to unset:
```
/disk
disk unset sata1 self-encryption-password
```
or
```
/disk
disk set sata1 !self-encryption-password
```
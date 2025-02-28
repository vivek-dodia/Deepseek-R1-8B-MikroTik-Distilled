# Thread Information
Title: Thread-1123480
Section: RouterOS
Thread ID: 1123480

# Discussion

## Initial Question
Is it possible to create a bit-by-bit image of a Mikrotik device and mount it on another OS, like Linux?I need to perform a forensic analysis on a Mikrotik device, but I was unable to extract the filesystem from the flash storage.Any technical articles por general guides on what to do/learn will be helpful. Thanks. ---

## Response 1
I hope it isn't possible... I know some thieves across the street who try to do just that! ---

## Response 2
Seehttps://blog.redcrowlab.com/dumping-firmware/,https://ivanorsolic.github.io/post/hardwarehacking1/ ---

## Response 3
Aside from updating, what can be done to prevent someone from making such forensic bit-by-bit images and make sure there is plenty of variance? ---

## Response 4
Generally by restricting physical access to device, using cabinets with locks, security guards on premises... ---

## Response 5
Aside from updating, what can be done to prevent someone from making such forensic bit-by-bit images and make sure there is plenty of variance?You can update as much as you want, if the hypothetical hacker interested in the secrets you store on your router has physical access to the device for enough time, It Is game over, physical extraction from a memory chip Is and will always be possible, as It uses exactly the same mechanisms that allow you to store and retrieve data on/from It.Then, extracting from these data meaningful info may be easier or more difficult, but in theory It Is always possible. ---

## Response 6
I was able to dump the MTD devices contents, by PXE booting the device using a OpenWRT firmware using this guide:https://openwrt.org/toh/mikrotik/common. After running binwalk on each dump file, a SquashFS filesystem was found:
```
root@debian:/home/kauedg/Downloads/mtd# binwalk OpenWrt.mtd5.binDECIMAL       HEXADECIMAL     DESCRIPTION--------------------------------------------------------------------------------208000x5140Squashfsfilesystem,little endian,version4.0,compression:xz,size:5570552bytes,587inodes,blocksize:262144bytes,created:2025-01-1609:19:3556061400x558AFCxz compressed data56680860x567CF6xz compressed data56701600x568510xz compressed data56724580x568E0Axz compressed data56732640x569130xz compressed data56770420x569FF2xz compressed data56793040x56A8C8xz compressed data56797180x56AA66xz compressed data57725390x5814FBxz compressed data57726430x581563xz compressed data71875940x6DAC8Axz compressed data73810670x70A04BNeighborlytext,"neighbor discovery-settings set discover-interface-list=LAN /tool mac-server set allowed-interface-list=LAN"73825740x70A62ENeighborlytext,"neighbor discovery-settings set discover-interface-list=!dynamicc"Then I tried unsquashing the filesystem but got stuck at these errors:
```

```
root@debian:/home/kauedg/Downloads/mtd# unsquashfs _OpenWrt.mtd5.bin.extracted/5140.squashfsLseekfailed becauseInvalidargument
read_block:failed to read block@0x701000056100000read_id_table:failed to read id table block
FATAL ERROR:Filesystem corruption detectedI also unsquashing the filesystem from the RouterOS NPK image file used to flash the device and I was able to get a filesystem:
```

```
root@debian:/home/kauedg/Downloads/mtd# unsquashfs _routeros-7.17-smips.npk.extracted/1000.squashfsParallelunsquashfs:Using8processors425inodes(416blocks)to write

created393files
created162directories
created32symlinks
created0devices
created0fifos
created0sockets
created0hardlinks

root@debian:/home/kauedg/Downloads/mtd# ll squashfs-root/total64Kdrwxr-xr-x16root root4.0KJan1606:19.drwxr-xr-x5root root4.0KJan2119:09..drwxr-xr-x2root root4.0KJan1606:19bin
drwxr-xr-x8root root4.0KJan1606:19bndl
drwxr-xr-x2root root4.0KJan1606:19boot
drwxr-xr-x2root root4.0KJan1606:19dev
lrwxrwxrwx1root root11Jan1606:19dude->/flash/dude
drwxr-xr-x2root root4.0KJan1606:19etc
drwxr-xr-x2root root4.0KJan1606:19flash
drwxr-xr-x3root root4.0KJan1606:19home
drwxr-xr-x3root root4.0KJan1606:19lib
drwxr-xr-x5root root4.0KJan1606:19nova
lrwxrwxrwx1root root9Jan1606:19pckg->/ram/pckg
drwxr-xr-x2root root4.0KJan1606:19proc
drwxr-xr-x2root root4.0KJan1606:19ram
lrwxrwxrwx1root root9Jan1606:19rw->/flash/rw
drwxr-xr-x2root root4.0KJan1606:19sbin
drwxr-xr-x2root root4.0KJan1606:19sys
lrwxrwxrwx1root root7Jan1606:19tmp->/rw/tmp
drwxr-xr-x5root root4.0KJan1606:19var
```

```
I'm looking for a way to unsquash the dumped filesystem without errors.

---
```

## Response 7
Try with extractbinwalkcommand line option:
```
binwalk--run-as=root-eOpenWrt.mtd5.binThis should extract any supported extractable data found in image includingSquashfs.

---
```

## Response 8
I think unsquash Is very "strict" and expects a "sound" filesystem and throws a fit even if minor issues are found.I cannot remember if a tool for recovery/fix exists, something *like* dmde which Is excellent for other filesystems.7-zip should be capable of reading a squashfs and in some cases It may be more tolerant.There may be ways to decompress the single zlib blocks and then reassemble the stuff, but provided that It works, It can usually work for text contents and similar - given the nature of squashfs - fragmentation should not be and issue, but beginning and end of files, even using trid or file to detect signatures will required a lot of manuale work with a hex viewer/editor. ---

## Response 9
Try with extractbinwalkcommand line option:
```
binwalk--run-as=root-eOpenWrt.mtd5.binThis should extract any supported extractable data found in image includingSquashfs.Yes, that's exactly how I'm extracting the mtd's dump content. It creates a file named [XXXX].squashfs and tries to unsquash it automatically but it only gives an empty directory. When I try unsquashing it manually, I get the "Lseek failed because Invalid argument" error stated above.

---
```

## Response 10
I think unsquash Is very "strict" and expects a "sound" filesystem and throws a fit even if minor issues are found.I cannot remember if a tool for recovery/fix exists, something *like* dmde which Is excellent for other filesystems.7-zip should be capable of reading a squashfs and in some cases It may be more tolerant.There may be ways to decompress the single zlib blocks and then reassemble the stuff, but provided that It works, It can usually work for text contents and similar - given the nature of squashfs - fragmentation should not be and issue, but beginning and end of files, even using trid or file to detect signatures will required a lot of manuale work with a hex viewer/editor.Using 7z was a great idea but no cigar
```
root@debian:/home/kauedg/Downloads/mtd# 7z l _OpenWrt.mtd5.bin.extracted/5140.squashfs7-Zip[64]16.02:Copyright(c)1999-2016IgorPavlov:2016-05-21p7zipVersion16.02(locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64bits,8CPUsIntel(R)Core(TM)i7-8565UCPU@1.80GHz(806EB),ASM,AES-NI)Scanningthe driveforarchives:1file,5570552bytes(5440KiB)Listingarchive:_OpenWrt.mtd5.bin.extracted/5140.squashfsERROR:_OpenWrt.mtd5.bin.extracted/5140.squashfs:opening:E_FAILErrors:1SystemERROR:E_FAILI found this OpenWRT forum post (https://forum.archive.openwrt.org/viewt ... p?id=67564) about using a tool named nand-dump-tool.py (https://github.com/Hitsxx/NandTool/blob ... mp-tool.py)to separate the OOB area but I'm still searching how to get the "ID code" parameter for a Mikrotik hAP lite (RB941-2nD)

---
```

## Response 11
Could be that MT uses non-standard Squashfs for devices or it was not correctly dumped or fs is corrupted on flash. I know for sure that from CHR image Squashfs can be extracted withbinwalk, done it many times. ---

## Response 12
Could be that MT uses non-standard Squashfs for devices or it was not correctly dumped or fs is corrupted on flash. I know for sure that from CHR image Squashfs can be extracted withbinwalk, done it many times.I dumped using both OpenWRT's MTD backup function and dd tool. Also dumped with dd the /etc/mtdXro and /etc/mtdblockX devices. All files with same sequential number are the same, so unless there's some gotcha on the acquisition itself, I believe their integrity is ok. Filesystem can't be corrupt on flash because I've freshly reflashed the device with Mikrotik's released RouterOS for the device, and, as I stated before, I dumped the filesystem from the npk file succesfully.I'm following thishttps://fastcall.medium.com/dumping-fir ... 7e819199fdarticle regarding OOB, because I think it's causing the errors. ---

## Response 13
[double post] ---

## Response 14
Nice find.The related blog post:https://www.j-michel.org/blog/2014/05/2 ... p-to-filesexplains in detail how the oob/spare data works, and on the main page:https://github.com/Hitsxx/NandTool/tree/masterit is clear that you can use oob and page size instead of chip ID (as it seems that there is no Winbond entry in the small program database of chips).The "normal" mtd should have a way to show (detected/guessed) sizes.The flash should be however a Winbond W25Q128JVSM, though finding the right values in the datasheet;https://www.winbond.com/hq/product/code ... =W25Q128JVseems not easy/immediate.But with a hex viewer it should be identifiable. ---

## Response 15
Nice find.The related blog post:https://www.j-michel.org/blog/2014/05/2 ... p-to-filesexplains in detail how the oob/spare data works, and on the main page:https://github.com/Hitsxx/NandTool/tree/masterit is clear that you can use oob and page size instead of chip ID (as it seems that there is no Winbond entry in the small program database of chips).The "normal" mtd should have a way to show (detected/guessed) sizes.The flash should be however a Winbond W25Q128JVSM, though finding the right values in the datasheet;https://www.winbond.com/hq/product/code ... =W25Q128JVseems not easy/immediate.But with a hex viewer it should be identifiable.That's exactly the flash chip model. I got to the same datasheet as you did, but I'm inexperienced with flash chips. Could you help me identify the page and OOB size for this one?I found this in the datasheet:The W25Q128JV array is organized into 65, 536 programmable pages of 256-bytes eachBut I can't find a reference to OOB anywhere in it. ---

## Response 16
Neither can I, but again, with a hex viewer and a little patience it should be easy to identify the oob, see here another example:https://redballoonsecurity.com/flash-dump/ ---

## Response 17
Some older topichttps://forum.archive.openwrt.org/viewt ... p?id=70636, but here is stated 16-byte OOB but for different MTD model of same brand with same size.Also as I see herehttps://openwrt.org/docs/techref/flashOpenWrt hasnanddumpwhich printsmtdinfo, like "Block size 131072, page size 2048, OOB size 64", alsoNand-dump-tool.pyshould print OOB size according to thislinefrom source code.If you missed it from dump tool, try to dump again and see. ---

## Response 18
Re-thinking about it, I believe you can also attempt "brute-forcing" the values.It is not like there are tens or hundreds of possibilities, the single oob record cannot logically be smaller than 8 bytes, and more likely is either 16 or 32 bytes (i don't think that odd values or non multiples of 8 or 16 are used), grouped maybe in sets of 4 or 8.The size of your dump in bytes, minus 65536*256= 16, 777, 216 is the total of oob space.Let's say that your dump is 17, 301, 504.The difference is 524, 288.That can be:65, 536x8 -> page size 25632, 768x16-> page size 51216, 384x32-> page size 10248, 192x64-> page size 20484, 096x128-> page size 40962, 048x256-> page size 8192 <- improbableRunning that python script five or six times with these values (and with the parameter "guess" or double the times, once with "adjacent" and once with "separate") shouldn't take much time. ---

## Response 19
I was writing a long write-up on how I was troubleshooting the issue on the OOB but I found out something else was the problem. I downloaded the newest version available for squashfs-tools (https://github.com/plougher/squashfs-tools), compiled it with the tracing function enabled and fiddled around with the two squashfs files I dumped: the one from the RouterOS firmware npk file and the one I extracted from the device using nanddump, after flashing it.I checked if the information about the files could be read
```
# ./unsquashfs -s ../../_routeros-7.17.1-smips.npk.extracted/1000.squashfssquashfs:read_bytes:readingfromposition0x0,bytes96Founda valid SQUASHFS4:0superblock on../../_routeros-7.17.1-smips.npk.extracted/1000.squashfs.Creationorlastappend timeThuJan3008:26:562025Filesystemsize5743084bytes(5608.48Kbytes/5.48Mbytes)CompressionxzBlocksize262144Filesystemisexportable via NFSInodesare compressedDataiscompressedUids/Gids(Idtable)are compressedFragmentsare compressedTailendsarenotpackedintofragmentsXattrsarenotstoredDuplicatesare removedNumberoffragments51Numberofinodes593Numberofids1squashfs:sBlk.s.inode_table_start0x57706csquashfs:sBlk.s.directory_table_start0x57848esquashfs:sBlk.s.fragment_table_start0x579dacsquashfs:sBlk.s.lookup_table_start0x57a1d6squashfs:sBlk.s.id_table_start0x57a1e4squashfs:sBlk.s.xattr_id_table_start0xffffffffffffffff# ./unsquashfs -s ../../_mtd5.nanddump.bin.extracted/7534D0.squashfssquashfs:read_bytes:readingfromposition0x0,bytes96Founda valid SQUASHFS4:0superblock on../../_mtd5.nanddump.bin.extracted/7534D0.squashfs.Creationorlastappend timeThuJan3008:26:562025Filesystemsize5743084bytes(5608.48Kbytes/5.48Mbytes)CompressionxzBlocksize262144Filesystemisexportable via NFSInodesare compressedDataiscompressedUids/Gids(Idtable)are compressedFragmentsare compressedTailendsarenotpackedintofragmentsXattrsarenotstoredDuplicatesare removedNumberoffragments51Numberofinodes593Numberofids1squashfs:sBlk.s.inode_table_start0x57706csquashfs:sBlk.s.directory_table_start0x57848esquashfs:sBlk.s.fragment_table_start0x579dacsquashfs:sBlk.s.lookup_table_start0x57a1d6squashfs:sBlk.s.id_table_start0x57a1e4squashfs:sBlk.s.xattr_id_table_start0xffffffffffffffffThe only difference was the filename
```

```
# diff <(./unsquashfs -s ../../_mtd5.nanddump.bin.extracted/7534D0.squashfs) <(./unsquashfs -s ../../_routeros-7.17.1-smips.npk.extracted/1000.squashfs)2c2<Founda valid SQUASHFS4:0superblock on../../_mtd5.nanddump.bin.extracted/7534D0.squashfs.--->Founda valid SQUASHFS4:0superblock on../../_routeros-7.17.1-smips.npk.extracted/1000.squashfs.This is the initial output from the npk file listing:
```

```
# ./unsquashfs -l ../../_routeros-7.17.1-smips.npk.extracted/1000.squashfs | headsquashfs:read_bytes:readingfromposition0x0,bytes96squashfs:read_id_table:no_ids1squashfs:read_bytes:readingfromposition0x57a1e4,bytes8squashfs:read_bytes:readingfromposition0x57a1de,bytes2squashfs:read_block:block@0x57a1de,4uncompressed bytes
squashfs:read_bytes:readingfromposition0x57a1e0,bytes4squashfs:read_bytes:readingfromposition0x57a1d6,bytes8squashfs:read_fragment_table:51fragments,reading1fragment indexesfrom0x579dacsquashfs:read_bytes:readingfromposition0x579dac,bytes8squashfs:read_bytes:readingfromposition0x579c1a,bytes2[...]This is the full output for the mtd5 dumped file:
```

```
# ./unsquashfs -l ../../_mtd5.nanddump.bin.extracted/7534D0.squashfssquashfs:read_bytes:readingfromposition0x0,bytes96squashfs:read_id_table:no_ids1squashfs:read_bytes:readingfromposition0x57a1e4,bytes8squashfs:read_bytes:readingfromposition0xffffffffffffffff,bytes2Lseekfailed becauseInvalidargument
read_block:failed to read block@0xffffffffffffffffread_id_table:failed to read id table block
FATAL ERROR:Filesystem corruption detectedI manually checked the superblock section (96 bytes) and found out that the value 0xffffffffffffffff is in the "Xattr table" field, which the documentation (https://dr-emann.github.io/squashfs/squashfs.html) says"The Xattr table, fragment table and export table are optional. If they are omitted from the archive, the respective fields indicating their position must be set to 0xFFFFFFFFFFFFFFFF (i.e. all bits set)."Now let's compare both files' headers
```

```
# xxd -l 96 ../../_routeros-7.17.1-smips.npk.extracted/1000.squashfs00000000:687371735102000000629b6700000400hsqsQ....b.g....00000010:3300000004001200c0020100040000003...............00000020:5c0bd81000000000eca1570000000000\.........W.....00000030:e4a1570000000000ffff ffff ffff ffff..W.............00000040:6c705700000000008e84570000000000lpW.......W.....00000050:ac9d570000000000d6a1570000000000..W.......W.....# diff <(xxd -l 96 ../../_mtd5.nanddump.bin.extracted/7534D0.squashfs) <(xxd -l 96 ../../_routeros-7.17.1-smips.npk.extracted/1000.squashfs)#They are the same, right? When I try to unsquash the firmware's file, it runs without problems, but the absolutely same header, even with the -no-xattrs option, can't be read from the extracted file. I event checked the "flags" field and the bit for the option "Xattrs are stored uncompressed" was disabled and the bit for "There are no Xattrs in the archive was enabled"
```

```
# ./unsquashfs -l -no-xattrs ../../_mtd5.nanddump.bin.extracted/7534D0.squashfssquashfs:read_bytes:readingfromposition0x0,bytes96squashfs:read_id_table:no_ids1squashfs:read_bytes:readingfromposition0x57a1e4,bytes8squashfs:read_bytes:readingfromposition0xffffffffffffffff,bytes2Lseekfailed becauseInvalidargument
read_block:failed to read block@0xffffffffffffffffread_id_table:failed to read id table block
FATAL ERROR:Filesystem corruption detectedIs this a unsquashfs command bug or what?

---
```

## Response 20
No idea, but from what you posted it seems that in one case, just after reading at 0x57a1e4:squashfs: read_bytes: reading from position 0x57a1e4, bytes 8it "skips" to :squashfs: read_bytes: reading from position 0xffffffffffffffff, bytes 2so the issue is probably in the 8 bytes @0x57a1e4. ---

## Response 21
@kauedg Just by having same superbock in both images it doesn't mean that other data in image isn't corrupt.By log it is corrupted inode table.Analisis by trace log and source:8 bytes for inode table positions are read and stored inid_index_tablefrom position 0x57a1e4, call stack:https://github.com/plougher/squashfs-to ... hfs.c#L659https://github.com/plougher/squashfs-to ... h-4.c#L509
```
...squashfs:read_bytes:readingfromposition0x57a1e4,bytes8And it fails when reading table bytes by iterating positions, log call stack:https://github.com/plougher/squashfs-to ... h-4.c#L530https://github.com/plougher/squashfs-to ... hfs.c#L761https://github.com/plougher/squashfs-to ... hfs.c#L665https://github.com/plougher/squashfs-to ... hfs.c#L659https://github.com/plougher/squashfs-to ... hfs.c#L699https://github.com/plougher/squashfs-to ... h-4.c#L527
```

```
squashfs:read_bytes:readingfromposition0xffffffffffffffff,bytes2Lseekfailed becauseInvalidargument
read_block:failed to read block@0xffffffffffffffffread_id_table:failed to read id table block...By this,id_index_tableis corrupt, since logged position is @0xffffffffffffffff (max unsigned long long) which is result of invalid value for its data type and such position in file is invalid (Lseek failed...). So as @jaclaz mentioned at 0x57a1e4 position 8 bytes are corrupt, where inode table positions are stored.Did you strip correctly OOB data from image? Squashfs superblock is located in first 96 bytes and OOB data will not corrupt it if MTD page size is larger, which is.

---
```

## Response 22
Spoiler alert: I DID IT.This is the short version, if someone wants a longer, detailed write-up, let me know and I'll post it here.Step 1: Trim the beginning of the file, until 0x10000
```
# dd if=mtd5.nanddump.bin of=mtd5_trimmed bs=1 skip=65536Step 2: I noticed there were 16 0xFF separators every 65520 bytes (OOB?). Remove it.
```

```
# ./nand-dump-tool.py -i dumps/mtd5_trimmed -o dumps/mtd5_step2 --page-size 65520 --oob-size 16 --save-oob dumps/mtd5_step2_oob --layout separateStep 3: Remove OOB
```

```
# ./nand-dump-tool.py -i dumps/mtd5_step2 -o dumps/mtd5_step3 --page-size 1024 --oob-size 16 --save-oob dumps/mtd5_step3_oob --layout separateStep 4: Fix offset to file's sections0x57A1E4 - 0x5711e0 = 0x9000 (36864)
```

```
# dd if=/dev/zero bs=1 count=36864 | tr "\000" "\377" > mtd5_new# dd if=mtd5_step3 bs=1 count=16321536 >> mtd5_newStep 5: Execute the patched unsquashfs, with tracing enabled, ignoring the offset after reading the superblock
```

```
# ./unsquashfs -s -o 7681232 ../../mtd5_newsquashfs:READING...squashfs:read_bytes:readingfromposition0x7534d0,bytes96Founda valid SQUASHFS4:0superblock on../../mtd5_new.Creationorlastappend timeThuJan3008:26:562025Filesystemsize5743084bytes(5608.48Kbytes/5.48Mbytes)CompressionxzBlocksize262144Filesystemisexportable via NFSInodesare compressedDataiscompressedUids/Gids(Idtable)are compressedFragmentsare compressedTailendsarenotpackedintofragmentsXattrsarenotstoredDuplicatesare removedNumberoffragments51Numberofinodes593Numberofids1squashfs:sBlk.s.inode_table_start0x57706csquashfs:sBlk.s.directory_table_start0x57848esquashfs:sBlk.s.fragment_table_start0x579dacsquashfs:sBlk.s.lookup_table_start0x57a1d6squashfs:sBlk.s.id_table_start0x57a1e4squashfs:sBlk.s.xattr_id_table_start0xffffffffffffffff# ./unsquashfs -l -o 7533568 -ig -f ../../mtd5_newsquashfs-root
squashfs-root/bin
squashfs-root/bin/bash
squashfs-root/bin/catlog
squashfs-root/bin/gosh
squashfs-root/bin/login
squashfs-root/bin/pakp
squashfs-root/bin/sh
squashfs-root/bin/shell
squashfs-root/bndl
squashfs-root/bndl/advanced-tools
squashfs-root/bndl/advanced-tools/home
squashfs-root/bndl/advanced-tools/home/web
squashfs-root/bndl/advanced-tools/home/web/webfig
squashfs-root/bndl/advanced-tools/home/web/webfig/advtool-b6a18e54d46e.jg.gz
squashfs-root/bndl/advanced-tools/home/web/webfig/advtool.info
squashfs-root/bndl/advanced-tools/home/web/webfig/advtool.jg.gz
squashfs-root/bndl/advanced-tools/nova
squashfs-root/bndl/advanced-tools/nova/bin
squashfs-root/bndl/advanced-tools/nova/bin/ddns
squashfs-root/bndl/advanced-tools/nova/bin/fping
squashfs-root/bndl/advanced-tools/nova/bin/macscan
squashfs-root/bndl/advanced-tools/nova/bin/netwatch
squashfs-root/bndl/advanced-tools/nova/bin/pspeed
squashfs-root/bndl/advanced-tools/nova/bin/scanner
squashfs-root/bndl/advanced-tools/nova/bin/wakeonlan
squashfs-root/bndl/advanced-tools/nova/lib
squashfs-root/bndl/advanced-tools/nova/lib/console
squashfs-root/bndl/advanced-tools/nova/lib/console/1166016512.memsquashfs-root/bndl/dhcp
squashfs-root/bndl/dhcp/home
squashfs-root/bndl/dhcp/home/web
squashfs-root/bndl/dhcp/home/web/webfig
squashfs-root/bndl/dhcp/home/web/webfig/dhcp-5540fe7f653a.jg.gz
squashfs-root/bndl/dhcp/home/web/webfig/dhcp.info
squashfs-root/bndl/dhcp/home/web/webfig/dhcp.jg.gz
squashfs-root/bndl/dhcp/lib
squashfs-root/bndl/dhcp/lib/libudhcp.so
squashfs-root/bndl/dhcp/nova
squashfs-root/bndl/dhcp/nova/bin
squashfs-root/bndl/dhcp/nova/bin/dhcp
squashfs-root/bndl/dhcp/nova/bin/dhcpclient
squashfs-root/bndl/dhcp/nova/lib
squashfs-root/bndl/dhcp/nova/lib/console
squashfs-root/bndl/dhcp/nova/lib/console/1128267776.memsquashfs-root/bndl/hotspot
squashfs-root/bndl/hotspot/home
squashfs-root/bndl/hotspot/home/web
squashfs-root/bndl/hotspot/home/web/hotspot
squashfs-root/bndl/hotspot/home/web/hotspot/alogin.html
squashfs-root/bndl/hotspot/home/web/hotspot/api.json
squashfs-root/bndl/hotspot/home/web/hotspot/css
squashfs-root/bndl/hotspot/home/web/hotspot/css/style.css
squashfs-root/bndl/hotspot/home/web/hotspot/error.html
squashfs-root/bndl/hotspot/home/web/hotspot/errors.txt
squashfs-root/bndl/hotspot/home/web/hotspot/favicon.ico
squashfs-root/bndl/hotspot/home/web/hotspot/img
squashfs-root/bndl/hotspot/home/web/hotspot/img/password.svg
squashfs-root/bndl/hotspot/home/web/hotspot/img/user.svg
squashfs-root/bndl/hotspot/home/web/hotspot/login.html
squashfs-root/bndl/hotspot/home/web/hotspot/logout.html
squashfs-root/bndl/hotspot/home/web/hotspot/md5.js
squashfs-root/bndl/hotspot/home/web/hotspot/radvert.html
squashfs-root/bndl/hotspot/home/web/hotspot/redirect.html
squashfs-root/bndl/hotspot/home/web/hotspot/rlogin.html
squashfs-root/bndl/hotspot/home/web/hotspot/status.html
squashfs-root/bndl/hotspot/home/web/hotspot/xml
squashfs-root/bndl/hotspot/home/web/hotspot/xml/WISPAccessGatewayParam.xsd
squashfs-root/bndl/hotspot/home/web/hotspot/xml/alogin.html
squashfs-root/bndl/hotspot/home/web/hotspot/xml/error.html
squashfs-root/bndl/hotspot/home/web/hotspot/xml/flogout.html
squashfs-root/bndl/hotspot/home/web/hotspot/xml/login.html
squashfs-root/bndl/hotspot/home/web/hotspot/xml/logout.html
squashfs-root/bndl/hotspot/home/web/hotspot/xml/rlogin.html
squashfs-root/bndl/hotspot/home/web/webfig
squashfs-root/bndl/hotspot/home/web/webfig/hotspot-f1e2e1d4af99.jg.gz
squashfs-root/bndl/hotspot/home/web/webfig/hotspot.info
squashfs-root/bndl/hotspot/home/web/webfig/hotspot.jg.gz
squashfs-root/bndl/hotspot/lib
squashfs-root/bndl/hotspot/lib/modules
squashfs-root/bndl/hotspot/lib/modules/5.6.3squashfs-root/bndl/hotspot/lib/modules/5.6.3/modules.dep.hotspot
squashfs-root/bndl/hotspot/lib/modules/5.6.3/net
squashfs-root/bndl/hotspot/lib/modules/5.6.3/net/ipv4
squashfs-root/bndl/hotspot/lib/modules/5.6.3/net/ipv4/unicl.ko
squashfs-root/bndl/hotspot/nova
squashfs-root/bndl/hotspot/nova/bin
squashfs-root/bndl/hotspot/nova/bin/hotspot
squashfs-root/bndl/hotspot/nova/etc
squashfs-root/bndl/hotspot/nova/etc/radius
squashfs-root/bndl/hotspot/nova/etc/radius/hotspot.x3
squashfs-root/bndl/hotspot/nova/lib
squashfs-root/bndl/hotspot/nova/lib/console
squashfs-root/bndl/hotspot/nova/lib/console/1132462080.memsquashfs-root/bndl/ipv6
squashfs-root/bndl/ipv6/home
squashfs-root/bndl/ipv6/home/web
squashfs-root/bndl/ipv6/home/web/webfig
squashfs-root/bndl/ipv6/home/web/webfig/ipv6-b898739b568b.jg.gz
squashfs-root/bndl/ipv6/home/web/webfig/ipv6.info
squashfs-root/bndl/ipv6/home/web/webfig/ipv6.jg.gz
squashfs-root/bndl/ipv6/nova
squashfs-root/bndl/ipv6/nova/bin
squashfs-root/bndl/ipv6/nova/bin/ippool6
squashfs-root/bndl/ipv6/nova/bin/radvd
squashfs-root/bndl/ipv6/nova/lib
squashfs-root/bndl/ipv6/nova/lib/console
squashfs-root/bndl/ipv6/nova/lib/console/1212153856.memsquashfs-root/bndl/ipv6/nova/lib/route
squashfs-root/bndl/ipv6/nova/lib/route/ipv6.rp
squashfs-root/bndl/ppp
squashfs-root/bndl/ppp/home
squashfs-root/bndl/ppp/home/web
squashfs-root/bndl/ppp/home/web/webfig
squashfs-root/bndl/ppp/home/web/webfig/ppp-0185abe62dd5.jg.gz
squashfs-root/bndl/ppp/home/web/webfig/ppp.info
squashfs-root/bndl/ppp/home/web/webfig/ppp.jg.gz
squashfs-root/bndl/ppp/lib
squashfs-root/bndl/ppp/lib/modules
squashfs-root/bndl/ppp/lib/modules/5.6.3squashfs-root/bndl/ppp/lib/modules/5.6.3/kernel
squashfs-root/bndl/ppp/lib/modules/5.6.3/kernel/drivers
squashfs-root/bndl/ppp/lib/modules/5.6.3/kernel/drivers/net
squashfs-root/bndl/ppp/lib/modules/5.6.3/kernel/drivers/net/ppp
squashfs-root/bndl/ppp/lib/modules/5.6.3/kernel/drivers/net/ppp/ppp_async.ko
squashfs-root/bndl/ppp/lib/modules/5.6.3/kernel/drivers/net/ppp/ppp_deflate.ko
squashfs-root/bndl/ppp/lib/modules/5.6.3/kernel/drivers/net/ppp/ppp_generic.ko
squashfs-root/bndl/ppp/lib/modules/5.6.3/kernel/drivers/net/ppp/ppp_mppe.ko
squashfs-root/bndl/ppp/lib/modules/5.6.3/kernel/drivers/net/ppp/ppp_synctty.ko
squashfs-root/bndl/ppp/lib/modules/5.6.3/kernel/drivers/net/ppp/pppoe.ko
squashfs-root/bndl/ppp/lib/modules/5.6.3/kernel/drivers/net/ppp/pppox.ko
squashfs-root/bndl/ppp/lib/modules/5.6.3/misc
squashfs-root/bndl/ppp/lib/modules/5.6.3/misc/ovpn.ko
squashfs-root/bndl/ppp/lib/modules/5.6.3/misc/pppoefp.ko
squashfs-root/bndl/ppp/lib/modules/5.6.3/misc/sstp.ko
squashfs-root/bndl/ppp/lib/modules/5.6.3/modules.dep.ppp
squashfs-root/bndl/ppp/lib/modules/5.6.3/net
squashfs-root/bndl/ppp/lib/modules/5.6.3/net/l2tp.ko
squashfs-root/bndl/ppp/lib/modules/5.6.3/net/pptp.ko
squashfs-root/bndl/ppp/nova
squashfs-root/bndl/ppp/nova/bin
squashfs-root/bndl/ppp/nova/bin/ppp
squashfs-root/bndl/ppp/nova/bin/ppp-worker
squashfs-root/bndl/ppp/nova/etc
squashfs-root/bndl/ppp/nova/etc/net-remote
squashfs-root/bndl/ppp/nova/etc/net-remote/ppp.x3
squashfs-root/bndl/ppp/nova/etc/radius
squashfs-root/bndl/ppp/nova/etc/radius/ppp.x3
squashfs-root/bndl/ppp/nova/lib
squashfs-root/bndl/ppp/nova/lib/console
squashfs-root/bndl/ppp/nova/lib/console/1090519040.memsquashfs-root/bndl/ppp/nova/lib/profiler
squashfs-root/bndl/ppp/nova/lib/profiler/ppp.p
squashfs-root/bndl/security
squashfs-root/bndl/security/home
squashfs-root/bndl/security/home/web
squashfs-root/bndl/security/home/web/webfig
squashfs-root/bndl/security/home/web/webfig/secure-0a49065a769f.jg.gz
squashfs-root/bndl/security/home/web/webfig/secure.info
squashfs-root/bndl/security/home/web/webfig/secure.jg.gz
squashfs-root/bndl/security/lib
squashfs-root/bndl/security/lib/modules
squashfs-root/bndl/security/lib/modules/5.6.3squashfs-root/bndl/security/lib/modules/5.6.3/kernel
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/crypto
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/crypto/blowfish_common.ko
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/crypto/blowfish_generic.ko
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/crypto/camellia_generic.ko
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/crypto/chacha20poly1305.ko
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/crypto/echainiv.ko
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/crypto/twofish_common.ko
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/crypto/twofish_generic.ko
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/net
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/net/ipv4
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/net/ipv4/ah4.ko
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/net/ipv4/esp4.ko
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/net/key
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/net/key/af_key.ko
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/net/xfrm
squashfs-root/bndl/security/lib/modules/5.6.3/kernel/net/xfrm/xfrm_user.ko
squashfs-root/bndl/security/lib/modules/5.6.3/modules.dep.security
squashfs-root/bndl/security/nova
squashfs-root/bndl/security/nova/bin
squashfs-root/bndl/security/nova/bin/ipsec
squashfs-root/bndl/security/nova/bin/ipsec-worker
squashfs-root/bndl/security/nova/bin/ssh
squashfs-root/bndl/security/nova/bin/sshd
squashfs-root/bndl/security/nova/etc
squashfs-root/bndl/security/nova/etc/radius
squashfs-root/bndl/security/nova/etc/radius/security.x3
squashfs-root/bndl/security/nova/etc/services
squashfs-root/bndl/security/nova/etc/services/security.x3
squashfs-root/bndl/security/nova/lib
squashfs-root/bndl/security/nova/lib/console
squashfs-root/bndl/security/nova/lib/console/1077936128.memsquashfs-root/boot
squashfs-root/dev
squashfs-root/dude
squashfs-root/etc
squashfs-root/etc/license
squashfs-root/etc/qca9531L-7.17.1.fwfsquashfs-root/etc/termcap
squashfs-root/flash
squashfs-root/home
squashfs-root/home/web
squashfs-root/home/web/assets
squashfs-root/home/web/assets/400.woff2squashfs-root/home/web/assets/700.woff2squashfs-root/home/web/assets/script-bd71a1293274.js
squashfs-root/home/web/assets/style-692511ab2675.csssquashfs-root/home/web/bth-files.html
squashfs-root/home/web/favicon.png
squashfs-root/home/web/favicon.svg
squashfs-root/home/web/graph.css
squashfs-root/home/web/help
squashfs-root/home/web/help/license.html
squashfs-root/home/web/index2.html
squashfs-root/home/web/license.txt
squashfs-root/home/web/logo.png
squashfs-root/home/web/mikrotik_logo.svg
squashfs-root/home/web/robots.txt
squashfs-root/home/web/webfig
squashfs-root/home/web/webfig/curve255-541e54a862be.js
squashfs-root/home/web/webfig/icons.info
squashfs-root/home/web/webfig/icons.png
squashfs-root/home/web/webfig/icons24.info
squashfs-root/home/web/webfig/icons24.png
squashfs-root/home/web/webfig/icons32.info
squashfs-root/home/web/webfig/icons32.png
squashfs-root/home/web/webfig/index.html
squashfs-root/home/web/webfig/list
squashfs-root/home/web/webfig/master-e24161e0bd73.js
squashfs-root/home/web/webfig/roteros-d7ce214a2753.jg.gz
squashfs-root/home/web/webfig/roteros.info
squashfs-root/home/web/webfig/roteros.jg.gz
squashfs-root/home/web/winbox
squashfs-root/lib
squashfs-root/lib/libc.so
squashfs-root/lib/libeap.so
squashfs-root/lib/libjson.so
squashfs-root/lib/librappsup.so
squashfs-root/lib/libubox.so
squashfs-root/lib/libuc++.so
squashfs-root/lib/libucrypto.so
squashfs-root/lib/libufiber.so
squashfs-root/lib/libuhttp.so
squashfs-root/lib/libumsg.so
squashfs-root/lib/liburadius.so
squashfs-root/lib/libuxml++.so
squashfs-root/lib/libwww.so
squashfs-root/lib/libxml.so
squashfs-root/lib/libz.so
squashfs-root/lib/modules
squashfs-root/lib/modules/5.6.3squashfs-root/lib/modules/5.6.3/drivers
squashfs-root/lib/modules/5.6.3/drivers/charsquashfs-root/lib/modules/5.6.3/drivers/char/ar7100wdt.ko
squashfs-root/lib/modules/5.6.3/drivers/char/ticker.ko
squashfs-root/lib/modules/5.6.3/drivers/net
squashfs-root/lib/modules/5.6.3/drivers/net/ag7240.ko
squashfs-root/lib/modules/5.6.3/drivers/net/ath8327.ko
squashfs-root/lib/modules/5.6.3/drivers/net/aths16.ko
squashfs-root/lib/modules/5.6.3/drivers/net/imq.ko
squashfs-root/lib/modules/5.6.3/drivers/net/packet_hook.ko
squashfs-root/lib/modules/5.6.3/drivers/net/phy_helper.ko
squashfs-root/lib/modules/5.6.3/drivers/net/sram.ko
squashfs-root/lib/modules/5.6.3/drivers/net/switch.ko
squashfs-root/lib/modules/5.6.3/drivers/net/vxlan2.ko
squashfs-root/lib/modules/5.6.3/kernel
squashfs-root/lib/modules/5.6.3/kernel/arch
squashfs-root/lib/modules/5.6.3/kernel/arch/mips
squashfs-root/lib/modules/5.6.3/kernel/arch/mips/crypto
squashfs-root/lib/modules/5.6.3/kernel/arch/mips/crypto/chacha-mips.ko
squashfs-root/lib/modules/5.6.3/kernel/arch/mips/crypto/poly1305-mips.ko
squashfs-root/lib/modules/5.6.3/kernel/arch/mips/oprofile
squashfs-root/lib/modules/5.6.3/kernel/arch/mips/oprofile/oprofile.ko
squashfs-root/lib/modules/5.6.3/kernel/crypto
squashfs-root/lib/modules/5.6.3/kernel/crypto/arc4.ko
squashfs-root/lib/modules/5.6.3/kernel/crypto/des_generic.ko
squashfs-root/lib/modules/5.6.3/kernel/crypto/sha1_generic.ko
squashfs-root/lib/modules/5.6.3/kernel/crypto/sha512_generic.ko
squashfs-root/lib/modules/5.6.3/kernel/drivers
squashfs-root/lib/modules/5.6.3/kernel/drivers/net
squashfs-root/lib/modules/5.6.3/kernel/drivers/net/bonding
squashfs-root/lib/modules/5.6.3/kernel/drivers/net/bonding/bonding.ko
squashfs-root/lib/modules/5.6.3/kernel/drivers/net/macvlan.ko
squashfs-root/lib/modules/5.6.3/kernel/drivers/net/slip
squashfs-root/lib/modules/5.6.3/kernel/drivers/net/slip/slhc.ko
squashfs-root/lib/modules/5.6.3/kernel/drivers/net/vrf.ko
squashfs-root/lib/modules/5.6.3/kernel/drivers/net/wireguard
squashfs-root/lib/modules/5.6.3/kernel/drivers/net/wireguard/wireguard.ko
squashfs-root/lib/modules/5.6.3/kernel/lib
squashfs-root/lib/modules/5.6.3/kernel/lib/crc-ccitt.ko
squashfs-root/lib/modules/5.6.3/kernel/lib/crypto
squashfs-root/lib/modules/5.6.3/kernel/lib/crypto/libarc4.ko
squashfs-root/lib/modules/5.6.3/kernel/lib/crypto/libblake2s-generic.ko
squashfs-root/lib/modules/5.6.3/kernel/lib/crypto/libblake2s.ko
squashfs-root/lib/modules/5.6.3/kernel/lib/crypto/libchacha20poly1305.ko
squashfs-root/lib/modules/5.6.3/kernel/lib/crypto/libcurve25519-generic.ko
squashfs-root/lib/modules/5.6.3/kernel/lib/crypto/libcurve25519.ko
squashfs-root/lib/modules/5.6.3/kernel/lib/crypto/libdes.ko
squashfs-root/lib/modules/5.6.3/kernel/lib/ts_bm.ko
squashfs-root/lib/modules/5.6.3/kernel/lib/ts_kmp.ko
squashfs-root/lib/modules/5.6.3/kernel/lib/zlib_deflate
squashfs-root/lib/modules/5.6.3/kernel/lib/zlib_deflate/zlib_deflate.ko
squashfs-root/lib/modules/5.6.3/kernel/lib/zlib_inflate
squashfs-root/lib/modules/5.6.3/kernel/lib/zlib_inflate/zlib_inflate.ko
squashfs-root/lib/modules/5.6.3/kernel/net
squashfs-root/lib/modules/5.6.3/kernel/net/8021qsquashfs-root/lib/modules/5.6.3/kernel/net/8021q/8021q.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebt_802_3.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebt_arp.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebt_arpreply.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebt_dnat.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebt_ip.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebt_ip6.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebt_limit.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebt_mark.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebt_mark_m.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebt_pkttype.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebt_redirect.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebt_snat.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebt_stp.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebt_vlan.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebtable_filter.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebtable_nat.ko
squashfs-root/lib/modules/5.6.3/kernel/net/bridge/netfilter/ebtables.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv4
squashfs-root/lib/modules/5.6.3/kernel/net/ipv4/ip_tunnel.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv4/netfilter
squashfs-root/lib/modules/5.6.3/kernel/net/ipv4/netfilter/ip_tables.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv4/netfilter/ipt_REJECT.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv4/netfilter/iptable_filter.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv4/netfilter/iptable_mangle.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv4/netfilter/iptable_nat.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv4/netfilter/iptable_raw.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv4/netfilter/nf_defrag_ipv4.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv4/netfilter/nf_nat_h323.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv4/netfilter/nf_nat_pptp.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv4/netfilter/nf_reject_ipv4.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv4/udp_tunnel.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/ah6.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/esp6.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/ip6_udp_tunnel.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/ipv6.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/netfilter
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/netfilter/ip6_tables.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/netfilter/ip6t_NPT.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/netfilter/ip6t_REJECT.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/netfilter/ip6t_eui64.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/netfilter/ip6t_ipv6header.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/netfilter/ip6table_filter.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/netfilter/ip6table_mangle.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/netfilter/ip6table_nat.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/netfilter/ip6table_raw.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/netfilter/nf_defrag_ipv6.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/netfilter/nf_reject_ipv6.ko
squashfs-root/lib/modules/5.6.3/kernel/net/ipv6/tunnel6.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nf_conntrack.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nf_conntrack_ftp.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nf_conntrack_h323.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nf_conntrack_irc.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nf_conntrack_netlink.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nf_conntrack_pptp.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nf_conntrack_rtsp.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nf_conntrack_sip.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nf_conntrack_tftp.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nf_nat.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nf_nat_ftp.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nf_nat_irc.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nf_nat_rtsp.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nf_nat_sip.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nf_nat_tftp.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/nfnetlink.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/x_tables.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_CT.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_DSCP.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_HL.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_MASQUERADE.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_NETMAP.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_REDIRECT.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_TCPMSS.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_addrtype.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_connbytes.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_connmark.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_conntrack.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_dscp.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_hashlimit.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_helper.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_hl.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_length.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_mac.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_mark.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_multiport.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_nat.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_physdev.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_policy.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_realm.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_statistic.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_string.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_tcpmss.ko
squashfs-root/lib/modules/5.6.3/kernel/net/netfilter/xt_tcpudp.ko
squashfs-root/lib/modules/5.6.3/kernel/net/sched
squashfs-root/lib/modules/5.6.3/kernel/net/sched/sch_cake.ko
squashfs-root/lib/modules/5.6.3/kernel/net/sched/sch_codel.ko
squashfs-root/lib/modules/5.6.3/kernel/net/sched/sch_fq_codel.ko
squashfs-root/lib/modules/5.6.3/kernel/net/sched/sch_htb.ko
squashfs-root/lib/modules/5.6.3/kernel/net/sched/sch_red.ko
squashfs-root/lib/modules/5.6.3/kernel/net/unix
squashfs-root/lib/modules/5.6.3/kernel/net/unix/unix.ko
squashfs-root/lib/modules/5.6.3/kernel/net/xfrm
squashfs-root/lib/modules/5.6.3/kernel/net/xfrm/xfrm_algo.ko
squashfs-root/lib/modules/5.6.3/misc
squashfs-root/lib/modules/5.6.3/misc/btest.ko
squashfs-root/lib/modules/5.6.3/misc/flash.ko
squashfs-root/lib/modules/5.6.3/misc/jiffies.ko
squashfs-root/lib/modules/5.6.3/misc/ledgroup.ko
squashfs-root/lib/modules/5.6.3/misc/logring.ko
squashfs-root/lib/modules/5.6.3/misc/mesh.ko
squashfs-root/lib/modules/5.6.3/misc/panics.ko
squashfs-root/lib/modules/5.6.3/misc/rb.ko
squashfs-root/lib/modules/5.6.3/misc/romon.ko
squashfs-root/lib/modules/5.6.3/misc/snif.ko
squashfs-root/lib/modules/5.6.3/misc/traffic_gen.ko
squashfs-root/lib/modules/5.6.3/misc/ulog.ko
squashfs-root/lib/modules/5.6.3/modules.dep.system
squashfs-root/lib/modules/5.6.3/net
squashfs-root/lib/modules/5.6.3/net/bridge
squashfs-root/lib/modules/5.6.3/net/bridge/bridge2.ko
squashfs-root/lib/modules/5.6.3/net/bridge/bridge2_netfilter.ko
squashfs-root/lib/modules/5.6.3/net/bridge/ebt_snif.ko
squashfs-root/lib/modules/5.6.3/net/bridge/ebt_ulog.ko
squashfs-root/lib/modules/5.6.3/net/ipv4
squashfs-root/lib/modules/5.6.3/net/ipv4/netfilter
squashfs-root/lib/modules/5.6.3/net/ipv4/netfilter/ipt_SAME.ko
squashfs-root/lib/modules/5.6.3/net/ipv4/netfilter/ipt_TARPIT.ko
squashfs-root/lib/modules/5.6.3/net/ipv4/netfilter/ipt_psd.ko
squashfs-root/lib/modules/5.6.3/net/ipv4/netfilter/ipt_snif.ko
squashfs-root/lib/modules/5.6.3/net/ipv4/netfilter/ipt_ulog.ko
squashfs-root/lib/modules/5.6.3/net/netfilter
squashfs-root/lib/modules/5.6.3/net/netfilter/nf_conntrack_ipv4.ko
squashfs-root/lib/modules/5.6.3/net/netfilter/nf_conntrack_ipv6.ko
squashfs-root/lib/modules/5.6.3/net/netfilter/xt_ein.ko
squashfs-root/lib/modules/5.6.3/net/netfilter/xt_layer7.ko
squashfs-root/lib/modules/5.6.3/net/netfilter/xt_misc.ko
squashfs-root/lib/modules/5.6.3/net/netfilter/xt_tls.ko
squashfs-root/lib/modules/5.6.3/net/sched
squashfs-root/lib/modules/5.6.3/net/sched/cls_fw.ko
squashfs-root/lib/modules/5.6.3/net/sched/cls_linear.ko
squashfs-root/lib/modules/5.6.3/net/sched/proto_agr.ko
squashfs-root/lib/modules/5.6.3/net/sched/sch_agr.ko
squashfs-root/lib/modules/5.6.3/net/sched/sch_pcq.ko
squashfs-root/lib/modules/5.6.3/net/sched/sch_sfq.ko
squashfs-root/lib/valgrind
squashfs-root/nova
squashfs-root/nova/bin
squashfs-root/nova/bin/agent
squashfs-root/nova/bin/arpd
squashfs-root/nova/bin/backup
squashfs-root/nova/bin/bridge2
squashfs-root/nova/bin/btest
squashfs-root/nova/bin/cerm
squashfs-root/nova/bin/cerm-worker
squashfs-root/nova/bin/cloud
squashfs-root/nova/bin/crossfig
squashfs-root/nova/bin/detnet
squashfs-root/nova/bin/discover
squashfs-root/nova/bin/email
squashfs-root/nova/bin/fileman
squashfs-root/nova/bin/ftpd
squashfs-root/nova/bin/graphing
squashfs-root/nova/bin/havecardbus
squashfs-root/nova/bin/igmpproxy
squashfs-root/nova/bin/installer
squashfs-root/nova/bin/ippool
squashfs-root/nova/bin/keyman
squashfs-root/nova/bin/kidcontrol
squashfs-root/nova/bin/led
squashfs-root/nova/bin/letsencrypt
squashfs-root/nova/bin/loader
squashfs-root/nova/bin/log
squashfs-root/nova/bin/login
squashfs-root/nova/bin/logmaker
squashfs-root/nova/bin/macping
squashfs-root/nova/bin/mactel
squashfs-root/nova/bin/mepty
squashfs-root/nova/bin/mesh
squashfs-root/nova/bin/mode
squashfs-root/nova/bin/modprobed
squashfs-root/nova/bin/moduler
squashfs-root/nova/bin/mproxy
squashfs-root/nova/bin/mtget
squashfs-root/nova/bin/natpmp
squashfs-root/nova/bin/net
squashfs-root/nova/bin/ntp
squashfs-root/nova/bin/panicsl
squashfs-root/nova/bin/parser
squashfs-root/nova/bin/ping
squashfs-root/nova/bin/portman
squashfs-root/nova/bin/profiler
squashfs-root/nova/bin/quickset
squashfs-root/nova/bin/radius
squashfs-root/nova/bin/resolver
squashfs-root/nova/bin/resolver_ctl
squashfs-root/nova/bin/romon
squashfs-root/nova/bin/route
squashfs-root/nova/bin/rtrace
squashfs-root/nova/bin/sermgr
squashfs-root/nova/bin/sertcp
squashfs-root/nova/bin/sniffer
squashfs-root/nova/bin/snmp
squashfs-root/nova/bin/socks
squashfs-root/nova/bin/ssld
squashfs-root/nova/bin/sstore
squashfs-root/nova/bin/sys2
squashfs-root/nova/bin/telnet
squashfs-root/nova/bin/telser
squashfs-root/nova/bin/tftpd
squashfs-root/nova/bin/traceroute
squashfs-root/nova/bin/trafficgen
squashfs-root/nova/bin/trafflow
squashfs-root/nova/bin/undo
squashfs-root/nova/bin/upnp
squashfs-root/nova/bin/user
squashfs-root/nova/bin/vrrp
squashfs-root/nova/bin/watchdog
squashfs-root/nova/bin/wproxy
squashfs-root/nova/bin/www
squashfs-root/nova/etc
squashfs-root/nova/etc/leds
squashfs-root/nova/etc/leds/system.x3
squashfs-root/nova/etc/lognames
squashfs-root/nova/etc/logo
squashfs-root/nova/etc/manual-url
squashfs-root/nova/etc/net-remote
squashfs-root/nova/etc/net-remote/system.x3
squashfs-root/nova/etc/pciinfo
squashfs-root/nova/etc/pciinfo/system.x3
squashfs-root/nova/etc/radius
squashfs-root/nova/etc/radius/system.x3
squashfs-root/nova/etc/services
squashfs-root/nova/etc/services/system.x3
squashfs-root/nova/etc/system_names
squashfs-root/nova/etc/system_names/system.x3
squashfs-root/nova/etc/upnp
squashfs-root/nova/etc/upnp/logo16.gif
squashfs-root/nova/etc/upnp/logo32.gif
squashfs-root/nova/etc/upnp/logo48.gif
squashfs-root/nova/etc/upnp/osinfo.xml
squashfs-root/nova/etc/upnp/wancommonifcfg.xml
squashfs-root/nova/etc/upnp/wanipconn.xml
squashfs-root/nova/etc/url
squashfs-root/nova/etc/user
squashfs-root/nova/etc/user/system.x3
squashfs-root/nova/etc/www
squashfs-root/nova/etc/www/system.x3
squashfs-root/nova/lib
squashfs-root/nova/lib/console
squashfs-root/nova/lib/console/1073741824.memsquashfs-root/nova/lib/console/logo.txt
squashfs-root/nova/lib/console/sublogo.txt
squashfs-root/nova/lib/defconf
squashfs-root/nova/lib/defconf/defconf
squashfs-root/nova/lib/defconf/defconf-caps
squashfs-root/nova/lib/defconf/defconf-wps-sync
squashfs-root/nova/lib/defconf/get-custom-defconf
squashfs-root/nova/lib/profiler
squashfs-root/nova/lib/profiler/system.p
squashfs-root/nova/lib/xmlnames2
squashfs-root/nova/logs
squashfs-root/nova/store
squashfs-root/pckg
squashfs-root/proc
squashfs-root/ram
squashfs-root/rw
squashfs-root/sbin
squashfs-root/sbin/nandfix
squashfs-root/sbin/sysinit
squashfs-root/sys
squashfs-root/tmp
squashfs-root/varsquashfs-root/var/cm
squashfs-root/var/deinstall
squashfs-root/var/locksquashfs-root/var/pckg
squashfs-root/var/pdb
squashfs-root/var/post
squashfs-root/var/run
squashfs-root/var/tmpWhile extracting, the program threw some errors:
```

```
# ./unsquashfs -o 7533568 -ig -f ../../mtd5_newParallelunsquashfs:Using8processors430inodes(423blocks)to write


xz uncompress failedwitherror code7xz uncompress failedwitherror code7xz uncompress failedwitherror code7xz uncompress failedwitherror code7xz uncompress failedwitherror code7xz uncompress failedwitherror code7writer:failed to read/uncompress file squashfs-root/nova/lib/console/1073741824.memwriter:failed to read/uncompress file squashfs-root/nova/lib/console/1073741824.memwriter:failed to read/uncompress file squashfs-root/nova/lib/console/1073741824.memwriter:failed to read/uncompress file squashfs-root/nova/lib/console/1073741824.memwriter:failed to read/uncompress file squashfs-root/nova/lib/console/1073741824.memwriter:failed to read/uncompress file squashfs-root/nova/lib/console/1073741824.mem[===========================================================================================================================================================================|]853/853100%created398files
created163directories
created32symlinks
created0devices
created0fifos
created0sockets
created0hardlinksSo I checked whether all the files matched the unsquashing output of the original npk file:
```

```
# tree squashfs-root > ../../mtd5_new.tree# tree ../../_routeros-7.17.1-smips.npk.extracted/squashfs-root/ > ../../npk.tree# diff --suppress-common-lines -y ../../npk.tree ../../mtd5_new.tree../../_routeros-7.17.1-smips.npk.extracted/squashfs-root/|squashfs-root│││├──1073741824.mem<164directories,429files|164directories,428filesThe only issue was extracting the file /nova/lib/console/1073741824.mem, which I'm working on right now. I'll also try reproducing it on another dump file I have here.Any help will be appreciated on extracting the /nova/lib/console/1073741824.mem file.

---
```

## Response 23
So, there are two "layers".1024+16=104063*1040=6552065520+16=65536Interesting.It would make sense to have these extra 16 bytes at the end of a group of "sectors" to "get even" to a multiple of 1024, 64*1024=65536. ---

## Response 24
So, there are two "layers".1024+16=104063*1040=6552065520+16=65536Interesting.It would make sense to have these extra 16 bytes at the end of a group of "sectors" to "get even" to a multiple of 1024, 64*1024=65536.Later I'll check if the 0xff separators where introduced by the nanddump tool. I got another dump done with dd which doesn't have this. The steps above are only good for the dump I tried first, unfortunately. Now I'm trying to figure out where all the offsets come from, without knowing the value an address should have beforehand. ---

## Response 25
I don't know, but the math sounds similar to the way some of the enterprise SSD's or HD's drives are made (many of these are formatted with 520 or 528 bytes instead of the usual 512).The actual "cell" (or sector group) size on the device should be anyway 4096 bytes or a multiple, and these drives can usually (with some spells and magic commands) be converted back to 512 bytes/sector, so some form of "slack" must exist, either 8 bytes every 32768 or 16 bytes every 65536. I believe. ---
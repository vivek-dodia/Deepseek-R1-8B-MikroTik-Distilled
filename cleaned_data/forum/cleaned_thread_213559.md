# Thread Information
Title: Thread-213559
Section: RouterOS
Thread ID: 213559

# Discussion

## Initial Question
Howdy!I have configured the DHCPv6 client as below:
```
/ipv6 dhcp-clientaddinterface=ether1 pool-name=0request=address,prefixuse-interface-duid=yesuse-peer-dns=noThis seems to work as my ISP sends me both an address and a prefix
```

```
/ipv6/dhcp-client>/ipv6/dhcp-client/printColumns:INTERFACE,STATUS,REQUEST,PREFIX,ADDRESS# INTERFACE  STATUS  REQUEST  PREFIX                         ADDRESS0ether1     bound   address2a07:6aa1:5:202c::/64,47m31s2a07:6aa1:5:1031::3,47m31sprefixbut it seems like RouterOS never assignes the recived address on ether1 as I would expect:
```

```
/ipv6/address/printFlags:D-DYNAMIC;G-GLOBAL,L-LINK-LOCALColumns:ADDRESS,INTERFACE,ADVERTISE,VALID#    ADDRESS                                    INTERFACE  ADVERTISE  VALID0D::1/128lono1DL fe80::1afd:74ff:fe27:d4c/64ether1no2DL fe80::1afd:74ff:fe27:d4d/64bridgeno3DG fd0a:1a81:cbdf:d546:1afd:74ff:fe27:d4d/64bridgeno11m58sIs this behaviour correct? Are my expectations wrong?

---
```

## Response 1
Which ROS version? Only newer v7 versions correctly display dynamic IPv6 addresses and routes, older versions (including all v6 versions) omit them from print command. Addresses and routes are there or else IPv6 wouldn't work in certain aspects. ---

## Response 2
Ah my bad to not include that information from the beginning.This is 7.16.2.
```
/system/resource/printuptime:4w3d4h51m9sversion:7.16.2(stable)build-time:2024-11-2612:09:40factory-software:6.46.3free-memory:190.1MiBtotal-memory:256.0MiBcpu:MIPS1004KcV2.15cpu-count:4cpu-frequency:880MHzcpu-load:1%free-hdd-space:5.0MiBtotal-hdd-space:16.0MiBwrite-sect-since-reboot:4188438write-sect-total:34195686architecture-name:mmips
               board-name:hEX
                 platform:MikroTik

---
```

## Response 3
To me, it doesn't seem correct. On 7.14.3, I have got the following:
```
[me@myTik]>ipv6/dhcp-client/printColumns:INTERFACE,STATUS,REQUEST,PREFIX,ADDRESS# INTERFACE  STATUS  REQUEST  PREFIX                                ADDRESS0ether1     bound   address2xxx:xxxx:xxxx:4a63::/64,56w2d8h8m8s2xxx:xxxx:yyyy:yyyy:0:ffff:a0c:4a63,56w2d8h8m8sprefix[me@myTik]>ipv6/address/printwhereglobalFlags:D-DYNAMIC;G-GLOBALColumns:ADDRESS,FROM-POOL,INTERFACE,ADVERTISE#    ADDRESS                                FROM-POOL  INTERFACE  ADVERTISE0G2xxx:xxxx:xxxx:4a63::1/64isp        bridge6    yes1DG2xxx:xxxx:yyyy:yyyy:0:ffff:a0c:4a63/128ether1no

---
```

## Response 4
Thanks for the replies!Enabled "Add Default Route" for the DHCP Client and then directly disabled it again. This caused the addresses to get assigned.Maybe the client was stuck in some state and forced to restart when I fiddled it.Problem solved - should I report it as a bug? ---

## Response 5
Most likely yes, but if you haven't created a supout.rif file while it was still misbehaving, chances that gents in Riga will be able to do anything about it are way lower. ---
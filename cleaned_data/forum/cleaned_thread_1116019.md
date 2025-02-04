# Thread Information
Title: Thread-1116019
Section: RouterOS
Thread ID: 1116019

# Discussion

## Initial Question
Hello all anons and MT staff.Can somebody confirmaddress-list-extra-timeoption working for dns cache?Got some asics (~600)- they're requestrin dns a lot.Using RB951U, ROS 7.16.2 FW 7.16.2. CPU load 80-100%Asics are given RB as dns server via dhcp. DNS ttl is set to 8d, address-list-extra-time is set to 1d, but cached dns entries show ttl several minutes.And RB have to make tons of dns requests to ISP's servers.
```
[admin@gw-nsk-asic-mt]<SAFE>/sys reso pr
                   uptime:1h18m2sversion:7.16.2(stable)build-time:2024-11-2612:09:40factory-software:6.46.6free-memory:73.0MiBtotal-memory:128.0MiBcpu:MIPS74KcV4.12cpu-count:1cpu-frequency:600MHzcpu-load:97%free-hdd-space:109.6MiBtotal-hdd-space:128.0MiBwrite-sect-since-reboot:510write-sect-total:23986bad-blocks:0%architecture-name:mipsbe
               board-name:RB951Ui-2HnDplatform:MikroTik
```

```
[admin@gw-nsk-asic-mt]<SAFE>/ip dns p
                      servers:10.104.241.42,10.104.241.50dynamic-servers:10.104.241.42,10.104.241.50use-doh-server:verify-doh-cert:nodoh-max-server-connections:5doh-max-concurrent-queries:50doh-timeout:5sallow-remote-requests:yes
          max-udp-packet-size:4096query-server-timeout:2squery-total-timeout:10smax-concurrent-queries:512max-concurrent-tcp-sessions:128cache-size:4096KiBcache-max-ttl:1w1daddress-list-extra-time:1dvrf:main
           mdns-repeat-ifaces:cache-used:38KiBFor example:
```

```
[admin@gw-nsk-asic-mt]<SAFE>/ip dns ca p deFlags:S-static0type=CNAME data=ltcssl.f2pool.com.cdn.cloudflare.net.name="ltcssl.f2pool.com"ttl=2m26s4type=CNAME data=ltc.sr.f2pool.com.name="ltc-na.f2pool.com"ttl=3m14s5type=CNAME data=ltc.sr.f2pool.com.name="ltc-euro.f2pool.com"ttl=3m14saddress-list-extra-time:1dttl=2m26s, ttl=3m14swhy?

---
```

## Response 1
"address-list-extra-time" works in combination with "address-list" of static dns entries. It has no effect on these dynamic entries you printed. see docs on the topic over here:https://help.mikrotik.com/docs/spaces/R ... 748767/DNS ---

## Response 2
"address-list-extra-time" works in combination with "address-list" of static dns entries. It has no effect on these dynamic entries you printed. see docs on the topic over here:https://help.mikrotik.com/docs/spaces/R ... 748767/DNSI thoroughly read and even searched this document, but whereexactlyat that man page is that written? ---
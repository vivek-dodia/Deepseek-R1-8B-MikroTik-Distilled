# Thread Information
Title: Thread-1114009
Section: RouterOS
Thread ID: 1114009

# Discussion

## Initial Question
Hello, not completely newbie .. but not master in mk.To test the adlist system, I created a network configuration with two virtual machines under virtualbox .The first is a MikroTik router (version 7.17rc2 ) and the second is a freshly installed Ubuntu Desktop.Current configuration:The MikroTik router receives an IP address from my local network: 192.168.88.21.The router distributes IP addresses on the 192.168.89.1-254 network.The Ubuntu Desktop gets the IP address 192.168.89.254.Ping between router and Internet: OK.DNS resolution: OK (verified with pingwww.nasa.com)On Ubuntu :ip a :
```
1:lo:<LOOPBACK,UP,LOWER_UP>mtu65536qdisc noqueue state UNKNOWNgroupdefaultqlen1000link/loopback00:00:00:00:00:00brd00:00:00:00:00:00inet127.0.0.1/8scope host lo
       valid_lft forever preferred_lft forever
    inet6::1/128scope host noprefixroute 
       valid_lft forever preferred_lft forever2:enp0s3:<BROADCAST,MULTICAST,UP,LOWER_UP>mtu1500qdisc pfifo_fast state UPgroupdefaultqlen1000link/ether08:00:27:3c:cb:05brd ff:ff:ff:ff:ff:ff
    inet192.168.89.254/24brd192.168.89.255scopeglobaldynamicnoprefixroute enp0s3
       valid_lft1489secpreferred_lft1489secAdd blocking lists (see attached configuration).Test performed with the “Can You Block It? WEBSITE:https://canyoublockit.com.Ads are not blockedI enclose the export of my configuration for further analysis. Thanks in advance for your help.

---
```

## Response 1
I don't see enabled setting "allow remote requests" in your router.make sure Ubuntu clears the DNS cache it might have in the system, also clear router DNS cachetry also these sites:https://d3ward.github.io/toolz/adblockhttps://adblock-tester.com ---

## Response 2
I don't see enabled setting "allow remote requests" in your router.Thanks ! Much better with !What a fool I am ! ---
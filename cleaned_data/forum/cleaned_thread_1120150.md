# Thread Information
Title: Thread-1120150
Section: RouterOS
Thread ID: 1120150

# Discussion

## Initial Question
I'm using a RB5009, and want to use cloud as my ddns, after trying to enable the cloud, i get this in cloud status, 
```
>/ip cloudprintddns-enabled:yes
  ddns-update-interval:none
           update-time:nodns-name:***.sn.mynetname.net
                status:updating...back-to-home-vpn:revoked-and-disabledI'm comfirm My router time is correctly using ntp, didn't work.try to enable and disable static domain cloud2.mikrotik.com and cloud.mikrotik.com but still didn't work.allow firewall on udp 15252, 53 and 123 to enable the router can received data,  but still didn't work.does anyone know what am I config wrong, hoping to get answer.Thank you.

---
```

## Response 1
Hi, 1. Does your router resolves properly that DNS names?2. Can you ping the World from CLI?3. Set "update interval" to eg. 5 min instead of "none". ---
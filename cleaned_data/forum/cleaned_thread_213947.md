# Thread Information
Title: Thread-213947
Section: RouterOS
Thread ID: 213947

# Discussion

## Initial Question
I'm adding RB5009U to hAP ax3 and CRS3xx fleet.Bridge VLAN Filtering for multiple VLAN/subnets is working; no switching issuesIPv4/IPv6 routing and firewall are working; RouterOS package upgrades work.hAP ax3 has WAN interface; all RB5009U ports are on default bridge.All RB5009U interfaces are in WAN interface list; no WAN interface.Both devices can ping *.pool.ntp.org hosts.All IPv4 LAN subnets are private.hAP ax3 NTP diagnostics:
```
[admin@mtc53uiga]>/system/ntp/client/exportterse;/system/ntp/client/printwithout-paging# 2025-01-16 10:06:59 by RouterOS 7.16.2# software id = KQPZ-KUKS## model = C53UiG+5HPaxD2HPaxD# serial number = xxxxxx/system ntp clientsetenabled=yes/system ntp client serversaddaddress=0.pool.ntp.org/system ntp client serversaddaddress=1.pool.ntp.org/system ntp client serversaddaddress=2.pool.ntp.org/system ntp client serversaddaddress=3.pool.ntp.org
         enabled:yes
            mode:unicast
         servers:0.pool.ntp.org,1.pool.ntp.org,2.pool.ntp.org,3.pool.ntp.org
             vrf:main
      freq-drift:14.543PPM
          status:synchronizedsynced-server:3.pool.ntp.org
  synced-stratum:2system-offset:-0.072ms[admin@mtc53uiga]>/tool ping count=4address=0.pool.ntp.org
  SEQ HOST                                     SIZE TTL TIME       STATUS0198.23.249.167565552ms62us1198.23.249.167565552ms97us2198.23.249.167565550ms413us3198.23.249.167565551ms342ussent=4received=4packet-loss=0%min-rtt=50ms413usavg-rtt=51ms478usmax-rtt=52ms97usRB5009U NTP diagnostics:
```

```
[admin@mtrb5009a]/system/ntp/client>/system/ntp/client/exportterse;/system/ntp/client/printwithout-paging# 2025-01-16 10:04:12 by RouterOS 7.16.2# software id = KWPA-GEH1## model = RB5009UG+S+# serial number = xxxxxx/system ntp clientsetenabled=yes/system ntp client serversaddaddress=0.pool.ntp.org/system ntp client serversaddaddress=1.pool.ntp.org/system ntp client serversaddaddress=2.pool.ntp.org/system ntp client serversaddaddress=3.pool.ntp.org
     enabled:yes
        mode:unicast
     servers:0.pool.ntp.org,1.pool.ntp.org,2.pool.ntp.org,3.pool.ntp.org
         vrf:main
  freq-drift:-0.368PPM
      status:waiting[admin@mtrb5009a]/system/ntp/client>/tool ping count=4address=0.pool.ntp.org
  SEQ HOST                                     SIZE TTL TIME       STATUS0162.159.200.123565216ms944us1162.159.200.123565218ms26us2162.159.200.123565217ms98us3162.159.200.123565217ms63ussent=4received=4packet-loss=0%min-rtt=16ms944usavg-rtt=17ms282usmax-rtt=1RB5009U NTP  client waits forever and system log topics clock,ntp are both silent.Does NTP  client require a public IPv4 address?

---
```

## Response 1
I observed similar issue but with time.google.com. I switched to other set of NTP servers for MikroTik devices and had no issues since. I also confirmed that while this is happening, I am able to query this NTP server from other devices with no issues.Does NTP client require a public IPv4 address?It does not. ---

## Response 2
Bah, humbug! Works when after adding default gateway IP address (hAP ax3 running NTP server). Good enough to move forward.You know, I should disable the firewall since I just presumed it was not in play. Thanks for the reply, helps the mind work here. ---

## Response 3
Well, now I know disabling every firewall rule has no effect. ---
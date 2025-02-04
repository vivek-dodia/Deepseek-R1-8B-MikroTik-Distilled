# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 207618

# Discussion

## Initial Question
Author: Tue May 14, 2024 9:08 pm
``` [admin@foo-gw]>/ping::1count=2Columns:SEQ, STATUS SEQ STATUS0packet rejected1packet rejected ``` ``` [admin@foo-gw]>/ipv6/settings/printdisable-ipv6:noforward:yes accept-redirects:yes-if-forwarding-disabled accept-router-advertisements:yes max-neighbor-entries:16384 ``` Having IPv6 problems with a CHR RouterOS, 7.14.3 on a virtual host at Hetzner. IPv6 configs (IPIPv6 on top of wireguard tunnels) that work on several physical routers fail on the CHR.Even pinging lo fails, which works on all physical routers:
```
Settings:
```

```
Any ideas what exactly is failing if /ping ::1 does not work?


---
```

## Response 1
Author: Wed May 15, 2024 2:33 pm
``` /ipv6/firewall/filteraddaction=accept chain=input dst-address=::1place-before=0 ``` Please do the following to make sure:
```
And try again. I had similar issue and that was how I realized it was the firewall.


---
```

## Response 2
Author: Wed May 15, 2024 5:08 pm
``` /ipv6/firewall/filteraddaction=accept chain=input dst-address=::1place-before=0 ``` Please do the following to make sure:
```
And try again. I had similar issue and that was how I realized it was the firewall.Tried, not helping. Tried also removing all entries from firewall. Will spawn up another virtual server to see if the problem can be reproduced.


---
```

## Response 3
Author: [SOLVED]Thu May 16, 2024 11:18 pm
Solved. Stupid user error as usual. Some forgotten obscure pre-wireguard era IPSec test years ago, not relevant until now when IPv6 was deployed:/ip/ipsec/policy/print...1 android-ikev2-peer yes ::/0 ::/0 all encrypt unique 0Lesson learned: always check firewall rulesandIPSec policies. Thanks to kind souls trying to help.
# Thread Information
Title: Thread-1117045
Section: RouterOS
Thread ID: 1117045

# Discussion

## Initial Question
I am not sure what the problem is here. Right now it looks as if I remove multiple routes to fast after each other, the routing table gets broken.The result is that the default route gets lost, also the router is no longer accessible via Winbox, even MAC access. After about 10 seconds the routeris accessible again via MAC/IP but the default route is lost. ROS 6.48.3 on a CCR2004.My current solution is to place a delay of 1 second between the /ip route remove commands.Is this a known problem or am I doing something wrong?Thanks for any inputdksoftHere is my configuration. I configure dhcp-client on an interface and execute a script if the interfaces is bound. On un-bound, the routes get removed.First configuration fails:
```
:if($bound="0")do={/ip firewall manglesetdisabled=yes[find comment="HETZNER by DHCP client"]# PLEASE LOOK HERE/ip routeremove[find comment="HETZNER by DHCP client"]}else={:if($bound="1")do={/ip firewall manglesetdisabled=no[find comment="HETZNER by DHCP client"]/ip routeadddst-address=0.0.0.0/0gateway=$"gateway-address"pref-src=$"lease-address"routing-mark=HETZNER_rt comment="HETZNER by DHCP client"/ip routeadddst-address=136.x.y.z/28gateway=HETZNER pref-src=$"lease-address"routing-mark=HETZNER_rt comment="HETZNER by DHCP client"}Second configuration (uses a :foreach loop) also fails:
```

```
:if($bound="0")do={/ip firewall manglesetdisabled=yes[find comment="HETZNER by DHCP client"]# PLEASE LOOK HERE:foreachitemin=[/ip route find comment="HETZNER by DHCP client"]do={/ip routeremove$item}}else={:if($bound="1")do={/ip firewall manglesetdisabled=no[find comment="HETZNER by DHCP client"]/ip routeadddst-address=0.0.0.0/0gateway=$"gateway-address"pref-src=$"lease-address"routing-mark=HETZNER_rt comment="HETZNER by DHCP client"/ip routeadddst-address=136.x.y.z/28gateway=HETZNER pref-src=$"lease-address"routing-mark=HETZNER_rt comment="HETZNER by DHCP client"}Third configuration (uses a :foreach loop and delay) works reliable:
```

```
:if($bound="0")do={/ip firewall manglesetdisabled=yes[find comment="HETZNER by DHCP client"]# PLEASE LOOK HERE:foreachitemin=[/ip route find comment="HETZNER by DHCP client"]do={/ip routeremove$item:delay1000ms}}else={:if($bound="1")do={/ip firewall manglesetdisabled=no[find comment="HETZNER by DHCP client"]/ip routeadddst-address=0.0.0.0/0gateway=$"gateway-address"pref-src=$"lease-address"routing-mark=HETZNER_rt comment="HETZNER by DHCP client"/ip routeadddst-address=136.x.y.z/28gateway=HETZNER pref-src=$"lease-address"routing-mark=HETZNER_rt comment="HETZNER by DHCP client"}

---
```

## Response 1
Have different approach, do not delete rule, simply disable/update them...Is the first time I read something like this, I remove/add multiple route on device with 500.000 routes and never have problems (till now).Better if you put full export, without omit anything, just censore username, password, mail etc. and real IP..... ---

## Response 2
Your header (removing routes too fast) -- is problem I'm coping now.But i'ts not your problem. Really, when i removing routes in script -- it hangs, routes in table duplicated (numbers duplicated). And it gets impossible to remove such duplicated records with error message
```
nosuch item(4)Until I kill routing process (ROS7)
```

```
/routing/stats/process/kill0Bit it is only in ROS7. In ROS6 all ok.Try add some logging in your scripts, like/log info message="interface bound"and for unbound respectively. And you will see the real problem.Also, to see more, add error catching (: do {...} on-error={...}) with logging. In ROS6 there no way to find error message, in ROS7 it's possible to catch error message.In my case (In ROS7 too)  unbounding happens just before bounding in case of rebinding lease:when host (android phone on wifi) leaving -- nothing happens until lease expired (there will be no problems).But when host come back -- lease unbond and bound immediately. And it looks like scripts executing almost in parallel. So I solve it by add 1 second delay before bound code. This way running unbond code can finish.

---
```

## Response 3
sounds like bad scripts,,,,,,Do what rextended recommended/export file=anynameyouwish ( minus router serial number, any public WANIP information, keys, long dhcp leases etc. ) ---
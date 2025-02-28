# Thread Information
Title: Thread-211174
Section: RouterOS
Thread ID: 211174

# Discussion

## Initial Question
I have an odd situation and hoping someone can help me find a fix.My clients are seeing degraded performance with IPv6 connections, but only when connected to a WLAN. here is a little about my setup:hEX S routerAruba 1930 switchAruba AP22 access pointsInternet is 250/25 capped by my ISP under a cheaper plan, fibre to the premises is gigabit.When I test on a wired client, speeds are 250mbps down on IPv4 and IPv6, but when I test on a wireless client, speeds are less than 150mbps on IPv6, but full 250mbps on IPv4. CPU on the hEX seems fine.I have tested the wireless network by running a local speed test server and can easily reach 600mbps, so this is fine. Client behaviour is consistent across device and OS (Windows, Mac, iPhone, Android).The weirdest part is that if I ask my ISP to provision a full 1gbps for testing, the issue with slow IPv6 goes away, and I am able to get ~300mbps IPv6 on a wireless client (understanding this is the limit for hEX without fasttrack on IPv6).So what I can’t figure out is why when I am on the more affordable plan, the connection suffers but only for wireless clients on IPv6. Any ideas?Happy to post my config, but it is pretty standard - firewall very similar to the documentation, with queue on outbound traffic only. Have tested with queue disabled and no measurable difference. Single LAN, one VLAN for security network, DHCP and RA on main LAN only. Behaviour consistent across routerOS 7.15 and 7.16, have not tested older versions.If I replace the hEX S with the router supplied by my ISP, the speeds on IPv6 over WLAN is no longer degraded and matches the IPv4 speed, so it seems to be something to do with either routerOS, configuration, or my hEX S hardware. ---

## Response 1
Update - this has been resolved.I have upgraded to routerOS 7.18beta2 and theonlyconfig change I made is enabling Fast Track on IPv6. The issue has completely gone away and the MikroTik HeX S is back to outperforming my ISP supplied router on both IPv4 and IPv6 connections. ---
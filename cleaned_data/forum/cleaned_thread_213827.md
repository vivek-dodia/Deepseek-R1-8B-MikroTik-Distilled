# Thread Information
Title: Thread-213827
Section: RouterOS
Thread ID: 213827

# Discussion

## Initial Question
Still loving my MikroTik Chateau Pro AX and have some questions about it:- Where is the Gratuitous ARP option? I saw it once, but then lost it. I want to disable that completely and only allow 2 ARP types - request and reply. This is mostly because some clients, such as Apple TV, impersonate other devices by design (via Bonjour) and are sometimes detected as spoofs.- How to get DoH to work without any cleartext DNS bootstrapping? IP URL (such ashttps://1.1.1.1/dns-query) is the way to do it, but router is unable to resolve any addresses with any DoH IP URL's.- How do I perform full and utter sanitation/purge/scrub? This router preserves backup files, logs, and some other data after factory reset.- Are there any plans to add some wizards for some basic functions, such as VLAN creation? I knew what I was getting when I bought this router and didn't mind going through learning process of creating new bridges, interfaces, etc., but I think there should be a simple wizard to be utilized first and then configure manually if necessary.- Are there custom configurations that can be downloaded from some kind of database? For example, there is factory/default (defaultcon) configuration. I wish there was one just like that, but have each port assigned untagged VLAN by default. ---

## Response 1
Most of these are answered in the manual- there are actually 5 arp modes. Gratuitous ARP:https://help.mikrotik.com/docs/spaces/R ... tuitousARP- add static DNS entry for the DoH server namehttps://help.mikrotik.com/docs/spaces/R ... HTTPS(DoH)- Reinstall via Netinstallhttps://help.mikrotik.com/docs/spaces/R ... Netinstall- There are a few wizards already, for things that are basic enough to get wizards, like DHCP serverhttps://help.mikrotik.com/docs/spaces/R ... DHCP-Setup- There are millions of potential configs for each device type, you could have other number of ports, other order of ports etc. This would not work in MikroTik world. ---
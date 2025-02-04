# Thread Information
Title: Thread-62741
Section: RouterOS
Thread ID: 62741

# Discussion

## Initial Question
It would be good idea to add WINS server in ROS, it will boost small office networks.Now you need to make metarouter from openwrt to create wins server on ros. It's not easy and buggy way. ---

## Response 1
I like that idea+1 ---

## Response 2
+1 It's a very useful thing. ---

## Response 3
-1. Not needed anymore? Is there any case where a decently modern windows still falls back to WINS? ---

## Response 4
Unfortunately yes. For example if you merge different office locations within OSPF over p2p wire guard links. In that case you have different networks in most cases, and to get for SMB share, printers etc to live across offices you still have to rely on WINS. ---

## Response 5
WINS is a31-year-old, obsolete Microsoft legacy serviceand an implementation of the NetBIOS Name Service (NBNS) that was needed for MS Windows 95 and earlier versions. Starting with Windows XP in2001, newer versions switched to using DNS, so WINS isn’t really necessary anymore.Since it’s no longer supported, Microsoft recommends decommissioning WINS:https://learn.microsoft.com/en-us/windo ... s/wins-top ---

## Response 6
Unfortunately yes. For example if you merge different office locations within OSPF over p2p wire guard links. In that case you have different networks in most cases, and to get for SMB share, printers etc to live across offices you still have to rely on WINS.Or use Active Directory (either MS or Samba). If it's just browsing file shares and printers, you should be able to use a GRE or EoIP tunnel over your WG P2P links, and enable Mikrotik's newer /ip/dns's mDNS repeater over GRE.Now, ideally, you'd be able to make static entries for DNS-SD - which also allow SMB browsing – but Mikrotik's DNS server does not support static PTR records, which are need for "static mDNS" (which is called DNS-SD). But DNS-SD records in DNS server is actually more similar to WINS's LMHOSTS approach - but that isn't an option. ---

## Response 7
Cosnider Active Directory, Domain Master Browser service.https://en.wikipedia.org/wiki/Domain_Master_Browser ---

## Response 8
FWIW, one should at least be aware that WINS has several security vulnerabilities that Microsoft hasn’t and won’t patch. If possible, I’d avoid WINS altogether.That said, it’s possible to run WINS in parallel while implementing IP-based name resolution using, for example, Samba as an Active Directory Domain ControllerorMicrosoft Active Directory Domain Services(AD DS) ---
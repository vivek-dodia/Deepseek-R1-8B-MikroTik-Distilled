# Thread Information
Title: Thread-1120689
Section: RouterOS
Thread ID: 1120689

# Discussion

## Initial Question
Dear team ,We have encountered an issue related to NAT on the MikroTik router. Please find the explanation below, we have configured NAT on the MikroTik router to enable internet access. Subsequently, we disabled the public IP and expected the internet connection to time out. However, the devices still have internet reachability even after the public IP was disabled. Could you kindly help us understand why this is occurring, and provide guidance on how to resolve this issue? ---

## Response 1
NAT relies on Connection tracking, this can sometime prevent the connection timing out.otherwise, I don`t think we have enough Information to correctly identify the Problem.../export file=anynameyouwish ( minus router serial number, any public WANIP information, keys etc.) ---

## Response 2
NAT is connection tracking thing and as long as connection is active, NAT will do its job. And will do the inverse for return packets if they get delivered to router.There are two possibilities for SRC NAT: action=src-nat and action=masquerade. There are two important differences between both possibilities:when WAN link gets dropped (I guess this means L2 or L1 failure, e.g. ethernet link loss), masquerade will clear connection table and thus dropping all active connections. src-nat will not and if link re-establishes "soon enough", connections will resume after a short hiccup.when using masquerade, it'll use whatever IP address is active on WAN interface when new NATed connection gets estsblished. So if address changes, NATed connections will follow (as old connections die and new connections get created). And I assume (but I never tried) if there isn't aporopriate IP address available, masquerade won't work (and un-NATed packets might leak to internet side)When using src-nat, then translated IP address is "hard coded" and NAT doesn't care about IP address on WAN interface or lack of there of. So removing/changing WAN IP address doesn't affect NAT at all.And then, even if you use masquerade, when you disable WAN IP address, existing connections will work as long as ISP router can deliver packets to your router. E.g. in case of "plain" IP over ethernet, upstream touter will send packets to your router as long as it has MAC address of your router's WAN interface in its ARP table (which can be minutes). Or even longer if your WAN technology and topology is not so "plain". ---
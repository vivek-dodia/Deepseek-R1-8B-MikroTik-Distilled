# Thread Information
Title: Thread-214132
Section: RouterOS
Thread ID: 214132

# Discussion

## Initial Question
It was just brought to my attention but I am not finding a word from Mikrotik about this:thehackernews.com/2025/01/13000-mikrotik-routers-hijacked-by.htmlApparently, it is just 2 days old discovery and details are scarce. ---

## Response 1
that "news" arised since January 14i think is mostly click-bait ---

## Response 2
Well, knowing that my network is "mostly" protected is not the acceptable state for meKnowing that there were multiple vulnerabilities exploited in Miktotik devices in the recent years makes me jump once I read news about new issues affecting Mikrotik...I own multiple devices from this vendor so I am obviously interested to know that these are reasonably secure and the manufacturer takes all necessary steps to avoid situations like this. ---

## Response 3
Details are not scarce, they are not existing.That routers with credentials admin/blank (or admin/admin and similar) can be easily accessed (or bruteforced for simple, common passwords) is not "news", and the referenced CVE (from 2023) is founded on the same basic issue, from its description:https://nvd.nist.gov/vuln/detail/CVE-2023-30799DescriptionMikroTik RouterOS stable before 6.49.7 and long-term through 6.48.6 are vulnerable to a privilege escalation issue. A remote andauthenticatedattacker can escalate privileges from admin to super-admin on the Winbox or HTTP interface. The attacker can abuse this vulnerability to execute arbitrary code on the system.(highlighting is mine)Whilst the privilege escalation was (is) only possible on 6.49.7 and earlier, the problem with user "admin" and no or easily guessable password remains if users does not change.The good Mikrotik guys started replacing admin/blank with admin/<complex unique password> to "force" users to better protect users setups, but nothing can be done for older devices and we have reports of routers compromised within seconds/minutes from being connected to the internet "accidentally" when not in a more secure login state, last example (jFYI):viewtopic.php?t=211182 ---

## Response 4
That's good, then! I keep all my devices updated/patched and not directly accessible from Internet, with default account disabled. ---

## Response 5
Still falling everytime into the same stupid speeches.Are you able to understand well what is written???MikroTik RouterOS stable before 6.49.7 and long-term through 6.48.6 are vulnerable to a privilege escalation issue.A remoteand authenticatedattacker can escalate privilegesfrom admin to super-adminon the Winbox or HTTP interface.The attacker can abuse this vulnerability to execute arbitrary code on the system.Do you know what it means to be alreadyauthenticated as admin???Who cares about vulnerability when those whoMUST be authenticatedcanalready do whatever the f–k they want, like install old RouterOS version vulnerable to x, y and z???Wrong concern.How does an attacker have REMOTE (or local) access as ADMIN???So...With these simple considerations, therefore, there is NO secure version of RouterOS, because if an INCOMPETENT administrator leaves the ports open, does not delete "admin" and sets a stupid password, any attacker can reinstall a vulnerable version of RouterOS and hack the router. ---

## Response 6
viewtopic.php?t=213997Author of the news mentioned in quoted topic (not the author of the topic) busily hides how old articles are referenced to "prove" the fact of article existence and makes an imperssion that it's something new => clickbite. ---

## Response 7
Still falling everytime into the same stupid speeches.Are you able to understand well what is written???MikroTik RouterOS stable before 6.49.7 and long-term through 6.48.6 are vulnerable to a privilege escalation issue.A remoteand authenticatedattacker can escalate privilegesfrom admin to super-adminon the Winbox or HTTP interface.The attacker can abuse this vulnerability to execute arbitrary code on the system.Do you know what it means to be alreadyauthenticated as admin???Who cares about vulnerability when those whoMUST be authenticatedcanalready do whatever the f–k they want, like install old RouterOS version vulnerable to x, y and z???Wrong concern.How does an attacker have REMOTE (or local) access as ADMIN???So...With these simple considerations, therefore, there is NO secure version of RouterOS, because if an INCOMPETENT administrator leaves the ports open, does not delete "admin" and sets a stupid password, any attacker can reinstall a vulnerable version of RouterOS and hack the router.So, the current version 6.49.17 and 7.17 of ROS are presumably not affected by these previously discovered vulnerabilities assuming the default admin user is disabled and replaced with once with complex password, management access to router restricted to specific private IPs (so no SSH/Winbox from WAN), firewall is properly configured, unused ports and services disabled, inter-VLAN traffic restricted... ---

## Response 8
Yes, that’s the correct understanding. It’s just as protected as a router should be by default. Opening services to the internet involves major risks, bug or not. This applies to all types of routers, not just Mikrotik. ---

## Response 9
So, the current version 6.49.17 and 7.17of ROS are presumably not affected by these previously discovered vulnerabilities assuming the default admin user is disabled and replaced with once with complex password, management access to router restricted to specific private IPs (so no SSH/Winbox from WAN), firewall is properly configured, unused ports and services disabled, inter-VLAN traffic restricted...Exactly but are ok from 6.49.8 and up, 7.13 and up.On 7.17 downgrade to some hackable version are forbidden until device-mode is not changed, but if you downgrade to 7.13...7.16 you can still downgrade again to 6.x or 7.xThe downlimit is the version shipped with the device (is also a limit for netinstall).Often the most exploited bug is the same password in router 7.17 equal to the password the user had in 6.44...... ---
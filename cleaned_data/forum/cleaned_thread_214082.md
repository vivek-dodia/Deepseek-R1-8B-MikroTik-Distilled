# Thread Information
Title: Thread-214082
Section: RouterOS
Thread ID: 214082

# Discussion

## Initial Question
I’m uncertain whether this issue started after the iOS update (possibly) or the RouterOS update (currently 7.17). Everything worked fine a few weeks ago before upgrading iOS and RouterOS.This is a very strange issue, and I’m not sure how to debug it effectively.Here’s what I’ve observed:• MacOS -> VPN: Everything works.• MacOS -> USB Phone Hotspot/Tethering -> VPN: Everything works.• iOS on WiFi -> VPN: Everything works.• iOS on Mobile Data (4G/5G) -> VPN: It connects, but some websites (e.g., google.com, Cloudflare-protected websites) don’t work. Others, like nba.com, work without issues.Additional details:• Enabling or disabling Private Relay makes no difference.• Tested with multiple mobile carriers across Europe and several iPhones, all running iOS 18.2.1.I suspect this might be related to HSTS or a similar mechanism, but I’m unsure.Can anyone confirm or deny this? Any suggestions on where to look or what to test would be greatly appreciated.Thanks ! ---

## Response 1
Found a solution here:viewtopic.php?t=207052 ---
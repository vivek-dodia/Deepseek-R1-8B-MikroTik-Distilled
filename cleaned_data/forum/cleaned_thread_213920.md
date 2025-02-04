# Thread Information
Title: Thread-213920
Section: RouterOS
Thread ID: 213920

# Discussion

## Initial Question
Hi have a strange issue with radius stats on our Splynx platform. We utilise DHCP and Dual stack giving clients a cgnat ipv4 address and a publicly routable ipv6 address.However upload and download on a clients connection is exactly 50/50 , on the radius usage it shows the ipv6 ingress exactly the same as the ipv4 egress. Splynx says they pulling the accounting stats directly from the mikrotik BNG so the fault is not on Splynx.I'd like to know if anyone else has come across this phenomenon?Login In Out Start at Time IP MAC NAS Actions000189 72089.15 MB 2326.54 MB 07/01/2025 06:47:45 117:17:46 0.0.0.0(2c0f3100:76::/64) 8866391A095C cb-bng1-dbn-za000189 2326.92 MB 72089.70 MB 05/01/2025 14:04:25 237:41:05 100.64.0.122 8866391A095C cb-bng1-dbn-za ---

## Response 1
pretty strange, but i upgraded my BNG from 7.16.1 to 7.17 and the issue is now fixed. ---
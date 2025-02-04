# Thread Information
Title: Thread-1120133
Section: RouterOS
Thread ID: 1120133

# Discussion

## Initial Question
Hello, Working from home, using a VPN, I route trafic destined for our office IP range through the VPN by default.I'd like to extend this to our customer sites who are solely identifiable by dns names made up as: <clientnumber>.d.company.comIs there a way to route traffic going to <anything>.d.company.com through the vpn?I used to have a separate network that routes all traffic through the company, but prefer to just use my general network and route based on destination IP/DNS. ---

## Response 1
With an address list and some mangling, it's possible to route through the VPN. But first, an exported config to see the type of VPN, if there are other active routing rules and/or mangling, etc., would be appreciated:export file=anynameyouwish(minus sensitive info) ---
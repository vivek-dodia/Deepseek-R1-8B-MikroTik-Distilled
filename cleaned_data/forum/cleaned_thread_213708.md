# Thread Information
Title: Thread-213708
Section: RouterOS
Thread ID: 213708

# Discussion

## Initial Question
Can i change Zerotier port number (from default 9993) if this port is blocked somewhere upstream?Thank you ---

## Response 1
There is documentation:https://help.mikrotik.com/docs/spaces/R ... ParametersIf I may ask: why ZeroTier? ---

## Response 2
I already read documentation. And it states that it listens on port 9993. So if i change this port, will Zerotier still work?Why zerotier? Easier acess to devices behind NAT. Also EoIP works quite nice over it. ---

## Response 3
You can if you want... it's on the "zt1" instances, so it applies to all connect ZT networks that use the instance. Theoretically, changing the default likely make ZT hole punching scheme go through an extra step internally, but cannot imagine it be significant. ---

## Response 4
It would appear the zerotier network assumes default port number which does not appear changeable as that may be set on zerotier servers??However they also communicate on two other ports, a random high number port based somewhat on zerotier address and also another high random port number if you permitUPNP or NAT-PMP.https://docs.zerotier.com/routertips ---

## Response 5
Ok, i will see if it still works in censorship oriented countries. If not, i will change the port number and see if it makes any difference at all.Thank you ---
# Thread Information
Title: Thread-1122444
Section: RouterOS
Thread ID: 1122444

# Discussion

## Initial Question
We just ordered a brand new CCR2116-12G-4S+ to replace a CCR1016 but when getting it up in the rack yesterday I came across with all ports from ether1 to ether12 flapping after I connect more than 1 cable to it. When there is only 1 cable connected this doesn't happen. Initially tought it was something with the fact the 2 first ports I connected were to same other device for a bonding, but tested with cables to other routers and switches and the issue always begins after attaching 2nd cable not mattering on which port or which device is on other end.I am using ether13 as management port. Unlike ether1~12, it's not connected to switch chip and is the only Ethernet port that doesn't flap. Log just shows every port with cable attached going down and up, nothing more. Interval between flaps vary from seconds to minutes. Port LEDs turn off and on.I intended to use SFP+ port but decided to stop CCR2116 deployment just after caught this issue, so didn't managed to see if it happens to SFP+ ports as well.CCR2116 is running RouterOS 7.10 and was configured from scratch.Any thoughts on what should I look or just send it to RMA? ---

## Response 1
if you are using RJ-45 Interfaces, or sfp copper dac cables, consider the posibility of some electrical problem at the sitealso confirm your Routeros VersionandSystem Routerboard Current Version ---

## Response 2
if you are using RJ-45 Interfaces, or sfp copper dac cables, consider the posibility of some electrical problem at the siteCat 5e cables in RJ-45 interfaces. Never had any issue like this before, having CCR, CRS, CSS and a lot of other devices in this rack. I will test it out of the rack anyway.also confirm your Routeros VersionandSystem Routerboard Current VersionBoth are 7.10. Gonna try 7.8 just to be sure, as I read of other kinds of instabilities that seem to have appeared post 7.8. ---

## Response 3
Same thing here running 7.1.2 just started this morning.... ---

## Response 4
any solution for this yet?, because I have the same problem!????????????????????????????????????? ---
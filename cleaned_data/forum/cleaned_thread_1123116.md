# Thread Information
Title: Thread-1123116
Section: RouterOS
Thread ID: 1123116

# Discussion

## Initial Question
Can I power 2 hAP's from a hEX PoE lite that is powered by PoE?I need to find a solution where there is no 220V. The idea is to power one hEX via PoE in and then power 2 wAP's from the PoE out ports.Any ideas? ---

## Response 1
Define the exact models you intend to use, hAP or wAP?The hex poe lite can output up to 1 A per Port ( but max 2 A on all four PoE out ports), so you can have as much as 24W per device using 24V Power adapter.The hAP Is 5 W.The wAP Is (was) 4 W.The hex poe lite itself Is 3 W.So you have plenty of slack, the total will be around 15 W.Of course you need to verify how many amperes the 24 V Power supply can provide, but the one provided with the hex poe lite Is 2.5 A, so 60W.It Is also needed to calculate the power loss due to the lengths of the various cables, but It should not be much.What doubts do you have? ---

## Response 2
Hello jaclazThank you for the reply.The units that will be connected to the hEX PoE lite are two wAP ac (msipbe)It should be OK if I use the PS that comes with the hEX PoE lite. As I see it I will use 2x4W plus 1x3W.It is just a matter of placing the units in the right places as it is a pace issue also. Total cable length would be about 15mI should be OKThanx again ---

## Response 3
I see a problemhex poe litePoE out Passive PoEwap ac mipsbePoE in 802.3af/at ---

## Response 4
HmmHave to look in to thatThankx for the comment ---

## Response 5
I see a problemhex poe litePoE out Passive PoEwap ac mipsbePoE in 802.3af/atPotential problem but probably not.Test first before mounting. ---

## Response 6
Values need to be corrected, but final result doesn't change.The wAPac:https://mikrotik.com/product/RBwAPG-5HacT2HnDhas 12W max power.They will work just fine with passive poE at 24V (the device accepts range11-57V, Mikrotik devices do work with passive PoE, when their specs indicate 802.3af/at it means that they additionally can be active powered, voltage below 37 or 44 V is not 802.3af/at compliant ).So it will be 3+12+12=27<60 W that the hap poe lite can deliver.At 24v, with normal cat5e cable, you can expect for 12 W:http://poe-world.com/Calculator/23.50 V at 10 m23 V at 20 m22.50 V at 30 m22 V at 40 min the last, worst case, you will loose some 1 W, so 3+12+1+12+1=29 W, still well below the 60W. (powering the hex directly).If you have a "reasonable" 20 m between the power supply and the hex, you will have at first approximation 30W load on that cable, so the voltage at the hex will be around 21.5V, re -running the 40 m 12W with 21.5 V as source the loss becomes 1.3 W per device, so 3+12+1.3+12+1.3=29.6 W you will lose 3.2 W on the 20 m, so 3+3.2+12+1.3+12+1.3=32.8 W<60W.You will need a poe injector *like* the RBPOE:https://mikrotik.com/product/RBPOEor the RBGPOE:https://mikrotik.com/product/RBGPOEto "convert" the hex poe lite power supply into a poe power supply.And here comes the question, the wAP ac has 10/100/1000 port, the hap poe lite ports are only 10/100, are you sure that you want a max 100 connection? ---

## Response 7
Valid remark.But maybe not really that much of a problem with mipsbe version of wap ac ? You can't use wave2 drivers. ---

## Response 8
Valid remark.But maybe not really that much of a problem with mipsbe version of wap ac ? You can't use wave2 drivers.Wouldn't the 5 GHz radios be capable of saturating the 100 Mbit cable connection?In any case the injector should be RBGPOE, so that the devices can be updated.It would also be a good idea to use cat 6 cable instead of cat 5e, nowadays. ---

## Response 9
They should and probably will.But not as much as when using wave2 drivers.Hex Poe light will definitely be bottle neck in such a setup. ---
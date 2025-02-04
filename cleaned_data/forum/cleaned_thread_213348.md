# Thread Information
Title: Thread-213348
Section: RouterOS
Thread ID: 213348

# Discussion

## Initial Question
Hi, I have seen the RB5009 (https://mikrotik.com/product/rb5009upr_s_in) has PoE-IN and PoE-OUTbut not at the same time :/If you’re using PoE-out to power other devices, the board will choose the source with the highest voltage (DC jack or the 2-pin connector) to power those.They say DC jack, 2-pin butNOTPoE-IN...But I have seen a few guys did a "hack":https://www.reddit.com/r/mikrotik/comme ... ?rdt=51148As far as I see, they used a PoE-Injector to "split" the power to the DC jack/2-pin and power the PoE-OUT-bus that way.I have same setup like on the picture with POE-injector and it sucessfully powers RB5009 + hAP AX² + hAP AX² + cAP AX.My question, can I power from my central CRS328 (with UPS) with such an injector the RB5009 and via that, an additional cAPax?If yes, which config on the CRS328? PoE Auto or forced? Voltage High or Low? ---

## Response 1
I believe the CRS328 works at 48V, so it will output on a PoE port 450 mA.That makes the power output on that port 48V*0.45A=21.6W.It is basically a "beefy" 802.3af (specs are 12.95 W, actually 15.40W since it is the PSE) or a "skinny" 802.3at (specs are 25.50 W, actually 30W since it is the PSE) level.https://en.wikipedia.org/wiki/Power_over_EthernetEven if you find a "high" voltage power supply (and you somehow fit it in the CRS328 and the device can actually work at 57V) 57V*0.45A=25.65W, and you have to consider some loss due to the length of the ethernet cable.The RB5009 from specs needs at least 16 W.The cAP Ax from specs needs at least 11 W.Total (at least) 27 W.No way you can power both from a single CRS328 port. (it may work because of the actual power needs of the RB5009 and of the cAP Ax are a little less than specs in real life, but it is not advised)And in theory not even a "proper" external 802.3at power supply, you would need an 802.3bt (specs are 51W for Type 3) one and a corresponding splitter.PoE is a mess, and Mikrotik's PoE is even worse. ---

## Response 2
I believe the CRS328 works at 48V....The CRS328 "brochure" specs 53V, thus PoE port should provide up to ~24W (not 30W as mentioned in specs.and brochure).This does not change anything for OP though.Agree on all your points ---

## Response 3
The CRS328 "brochure" specs 53V, thus PoE port should provide up to ~24W (not 30W as mentioned in specs.and brochure).This does not change anything for OP though.Good catch.So on the product page it has:Max out per port output (input 18-30 V) 1000 mAMax out per port output (input 30-57 V) 450 mAOn the brochure it is specified 26V/53V and:Each port can provide up to 30 W with high voltage, and 26 W with low voltage power output.Strange math.26*1=26->26W OK53*0.45=23.85-> 30WTo make 30 W out of 53V one would need 570 mA as 53*0.57=30, 21but if the brochure is correct and the product page is wrong, 30W would be good for the specific OP case, as it would be the needed 27W+10%. ---

## Response 4
I will let you knowHow was the Reddit-guy able to do this:...it sucessfully powers RB5009 + hAP AX² + hAP AX² + cAP AXThats even more I would need. ---

## Response 5
I don't think it is a chain, more like hAP AX² + hAP AX² + cAP AX connected to three ports of the same RB5009. ---

## Response 6
I tested and it works!I cut off the end of the RBGPOE (https://mikrotik.com/product/RBGPOE) and connected to DC2 as shown here:https://www.reddit.com/r/mikrotik/comme ... ?rdt=51148The "barrel DC-input" is empty, only because I had no male-male-gender-changer for the PoE-Injector.CRS328 with RB5009only(PoE "forced on" [auto doesNOTwork] and set voltage to high [low works too but tested with RB5009 only]):crs328+rb5009.jpgCRS328 with RB5009 + cAPax (picture shows again CRS328-port):crs328+rb5009+capax.jpgAnd finally RB5009 + cAPax + everything else (TV, NUC, RetroPi, DSL-Modem, ATA) picture shows agian CRS328-port:crs328+rb5009+capax+everything-else.jpgThis is the cAPax-port on the RB5009:capax.jpg ---

## Response 7
RB5009 8.7<16 WcAP AX 6.4 <11 W8.7+6.4=15.1 < 27 W15.1+(some activity)=16.8 < 27 WIf the RB5009 goes high on CPU while the CAP is also loaded it has to be seen how much more power is needed. ---
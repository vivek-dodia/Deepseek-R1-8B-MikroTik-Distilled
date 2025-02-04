# Thread Information
Title: Thread-213272
Section: RouterOS
Thread ID: 213272

# Discussion

## Initial Question
Hi Mikrotik, I wanted to say I bought the L009 because I needed the 8 ports. Previous device was a hexS.I powered the hexS via my central CRS328 and the hexS powered my cAPax. Worked great and everything was supplied via my central UPS. I hoped the same for the L009...But unfortunately the L009 does not behave like the hexS and the cAPax did not come up. Why do you make such incompatibilities in your devices? WHY can not simply a MT PoE device power another MT PoE device... Why passive PoE and the other active af/at-PoE? Why always so complicated? Why not everytime at least af/at-PoE?And another point is extremely annyoing: You can only disable the eth1 LEDs! Come on, designed the L009 some unpaid intern on its way to school?! Why on earth do you build into that device LEDs who can light up a whole room and then only allowing to disable the eth1 LEDs? My whole room is lit in the night and why only eth1?!The rest of the L009 is good in my opinion, the red colour is not my colour - grey or black would have match better IMHO, but okay. But the PoE and LED things made my really think who on earth designed this? Someone who will/has never used such a device in its home... Every cheapo-China-device has at least a bit more comfort. Again, come on guys, only eth1?!?! O_o Shame on you for this and for the brightest LEDs you found probably in China... The money these bright LEDs cost, you could have spend into an af/at-PoE-borad/converter and used normal LEDs :/ ---

## Response 1
Folks familiar with POE ensure the standards used match their needs....As far as LEDs go tape is cheap. Stop whining. ---

## Response 2
Set aside the whining, I don't see a difference between hexs and L009:Hex s:https://mikrotik.com/product/hex_sPoweringDetailsNumber of DC inputs 2 (DC jack, PoE-IN)DC jack input Voltage 12-57 VMax power consumption 24 WMax power consumption without attachments 6 WCooling type PassivePoE in 802.3af/atPoE in input Voltage 12-57 VPoE-outDetailsPoE-out ports Ether5PoE out Passive PoE up to 57VMax out per port output (input 18-30 V) 500 mAMax out per port output (input 30-57 V) 500 mAMax total out (A) 500 mAL009:https://mikrotik.com/product/l009uigs_rmPoweringDetailsNumber of DC inputs 2 (DC jack, PoE-IN)DC jack input Voltage 24-56 VMax power consumption 40 WMax power consumption without attachments 8 WCooling type PassivePoE in 802.3af/atPoE in input Voltage 24-56 VPoE-outDetailsPoE-out ports Ether8PoE out Passive PoEMax out per port output (input 18-30 V) 1 AMax out per port output (input 30-57 V) 450 mAMax total out (A) 1 ABoth devices have PoE in 802.3af/at and PoE out passive.So what can be done with the first should be doable with the second.the difference between 500 and 450 mA (500mA@48V=24W, 450 mA@48V=21.6 W) shouldn't make a difference when powering a Cap Ax which should need 11W (unless tha Cap Ax is powering something else.. ---

## Response 3
Set aside the whining, I don't see a difference between hexs and L009:I don't have either hEX S nor L009 ... so only guessing: it could be that L009 doesn't allow PoE out if it's powered via PoE in ... while hEX S did? The fact is that PoE 802.3 comes with some stringent spcifications (which MT mostly doesn't adhere to, but that's yet another story) about amount of power that PSE has to be able to offer ... ip to 350mA for 802.3 af (which is the lowest spec in the family). When device is powered via 802.3 PoE PSE, it can't really know what kind of spec the PSE supports, so it can't count on getting more than "agreed" ... in principle 802.3 at/bt device can "request" certain amount of power (specially so if using LLDP handshake) and request 8W higher power (8W is specced "own consumption"). And I guess with decent PoE chip that can happen. But as I already wrote, MT tends to cut corners left and right when it comes to PoE (802.3 PoE even more) and I can only hope that they improve in this area for future devices. ---

## Response 4
Yep, I was trying to highlight that from specs there is no apparent difference between the two devices.OP had all the rights in the world to believe that the L009 could replace the hex S (maybe there is some different setting for the PoE out port to check?).So the good Mikrotik guys - besides their "peculiar" way to implement 802.3af/at - are seemingly not documenting properly the different (strange) behaviour of the two devices (besides omitting that the PoE in can also be passive).I would say that even "folks familiar with POE" would have fallen for this. ---

## Response 5
Yep, I was trying to highlight that from specs there is no apparent difference between the two devices.OP had all the rights in the world to believe that the L009 could replace the hex S (maybe there is some different setting for the PoE out port to check?).So the good Mikrotik guys - besides their "peculiar" way to implement 802.3af/at - are seemingly not documenting properly the different (strange) behaviour of the two devices (besides omitting that the PoE in can also be passive).I would say that even "folks familiar with POE" would have fallen for this.Anyone familiar with POE on mikrotik, buys a TPLINK or whatever poe capable switch or a separate injector from any brand (with an eye to the standards used and the wattage required) ---

## Response 6
@anavThe whole point is that someone familiar with PoE and specifically with Mikrotik, and even more specifically with the hex S, could be easily tricked by the mis-documentation Mikrotik provides (besides their - let's saycreative- claim that these devices are 802.3af/at compliant). ---

## Response 7
Disagree, the hex refresh only states passive poe in and a voltage of 12-28v. No standard mentioned.The hex poe states: It also supportspassive PoE inputandpassive or 802.3af/at PoE output.Ethernet ports 2-5 can power other PoE capable deviceswith the same voltage as applied to the unit. Less power adapters and cables to worry about! It can powerat/af mode B (4, 5+)(7, 8-)compatible devices, if 48-57input voltage is used.It clearly states what its capable of! and the limitations, and it FAILs to state the watts per port or total budget.I will agree its not clear and confusing, and all the more reason to avoid. ---

## Response 8
Disagree, the hex refresh only states passive poe in and a voltage of 12-28v. No standard mentioned.I think you are the first one to talk of the hex refresh.To recap:1) OP had a hex S that was PoE powered and powered in cascade.a cap AX2) then he replaced the hex S with a L009, but the L009 could not power the (same) cap AX3) the hex S and the L009 have the SAME specs regarding PoE in and out (with a slight difference with amount of current in output, which is irrelevant since the cap AX needs half the amount of current)The documentation of both the devices at hand (the hex S and the L009) DOES NOT state that the PoE in on either device can be either 802.3af/at or passive (this is something that is NOT written on the product page) and BTW the page for the cap AX as well states PoE in as 802.3af/at ONLY:https://mikrotik.com/product/cap_axPoweringDetailsNumber of DC inputs 2 (PoE-IN, DC jack)DC jack input Voltage 18-57 VMax power consumption 36 WMax power consumption without attachments 11 WCooling type PassivePoE in 802.3af/atPoE in input Voltage 18-57 VOne needs to infer that since the device accepts 18-57 V PoE in and the 802.3af/at standard (the one that Mikrotik does not fully complies to) has a minimum-minimum voltage of 37 for af or 42.5 for at, then the device can also be powered by passive power, but is not explicitly written anywhere on the page.Still the basic issue remains, if the same cap AX can be powered (passive) by a hex s and cannot be powered (passive) by a L009, it means that the (passive) PoE out of the hex s is *somehow* different from the (passive) power of the L009, notwithstanding the fact that they are equally (mis-) described on their respective pages. ---

## Response 9
Just tried with wAP AX (which is even further down in power requirements but normally also 802.3af/at only): it will power on using L009 but you have to set POE on ether8 to forced on. Not auto on. ---

## Response 10
Just tried with wAP AX (which is even further down in power requirements but normally also 802.3af/at only): it will power on using L009 but you have to set POE on ether8 to forced on. Not auto on.Yep, that's why I asked:(maybe there is some different setting for the PoE out port to check?). ---

## Response 11
You dont get it...HexS: The port #5 can power other passive PoE capable devices with the same voltage as applied to the unitThere is no such standard as passive POE, as soon as one reads that the red flag goes up, no mention of any standard there..... and limited by input as well...................In the writeup for the L1009 the only mention of poe is being powered by 5009 capable poe ports. ( and 5009 writeup states poe out of 802.3 af/at )The L10009 POE-in states 802.3 af/at but its poe out is passive --> no standard........Most importantly The CAPAX........... clearly statesit needs 802.3 af/at for iNPUT on poe. clearly the L1009 does not output 802.3 af/at!Why it worked on the hexS is a mystery to me, it should not have. ---

## Response 12
The negotiation part does not fly when connected to L009.But it works when you "skip that part", hence forced on.With "auto on" it gives an error message (on my setup it does). ---

## Response 13
@anavAgain, though not stated on the docs, when a device is said to be 802.3af/at compliant AND it accepts 18-57 V the good Mikrotik guys imply that it can be also powered passive (at the typical 24 V or 48V ).And again, the cap AX was powered (passive) from the previous hex S (that only provides passive PoE out), evidently as holvoeth suggested the (basic) negotiation for passive PoE does not work on the L009 in the same manner as it does on the hex S.. (but in holvoeth's experiment iit could also be the Wap AX that behaves differently) ---

## Response 14
I was already thinking that as well but I don't have a cAP AX lying around here.Although given wAP AX and cAP AX are both 802.3af/at devices, I am going to (carefully) assume it's just that forced on setting which should make it work.OP can easily test it. ---

## Response 15
Agree with the sentiment here – Mikrotik PoE support is all over the place & poorly documented. While the RB5009/L009 form factor is great, there really is no "PoE switch" in this form...But the L009 is a replacement for the RB2011, not the [old] HexS, per se... ---

## Response 16
Oh yes.RB5009PrShould be 802.3 af/at compliant. ---
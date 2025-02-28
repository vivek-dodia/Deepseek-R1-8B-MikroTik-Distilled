# Thread Information
Title: Thread-1120379
Section: RouterOS
Thread ID: 1120379

# Discussion

## Initial Question
Does anyone know which devices work well with Verizon cellular data service in NY, USA?I need Internet connectivity at a location and the only established provider is Spectrum Cable with a base cost of $50/month (plus taxes and fees, over $60/month).I am hoping that the the MT LTE/5G devices are ready and reliable enough to use as an alternative.I already use Verizon for other services and (I think) I can add a hotspot data line for $10/month (for 100GB).The goal is to provide Internet connectivity (wired and wifi) for web surfing, media streaming, environmental sensors and controls, etc. throughout a 1000 sq-ft house. ---

## Response 1
There are at least two different tasks to do:1. device that plays well with LTE2. how to cover 1000 sq-ft house with WiFi.The second is non trivial as it heavily depends on a structure of the building. ---

## Response 2
There are at least two different tasks to do:1. device that plays well with LTE2. how to cover 1000 sq-ft house with WiFi.The second is non trivial as it heavily depends on a structure of the building.Luckily, I have a reasonable amout of experience to handle #2. Pretty sure a single hAPax, for example, would have it just fine (wood frame rectangular house).#1 is what I have no experience with and everything I read says it is very (to me) complicated, possibly involving registering the sim in some other device before moving it to an MT device, and likely relying on a lot of hope. ---

## Response 3
Maybe this thread:viewtopic.php?p=1082937can give you some ideas. ---

## Response 4
Maybe this thread:viewtopic.php?p=1082937can give you some ideas.Thank you.I think the thread, and the threads referenced therein, do not point to an MT device that is definetly compatible with Verizon Wireless in the USA.I don't know what to conclude about this. ---

## Response 5
I think the thread, and the threads referenced therein, do not point to an MT device that is definetly compatible with Verizon Wireless in the USA.Exactly.It seems like such device does not exist (yet) in the Mikrotik product range. ---

## Response 6
None work "great" and no 5G options for US.The LTE6 will work okay with AT&T, albeit 5G and limited to CAT6 speeds - but it does at least couple CA modes for AT&T. And LTE6 may work for Verizon, in some areas, but it's without Verizon's Band 13 – which VZW widely deployed/uses – there be no CA.The only option is the Chateau LTE6-US. That does have Verizon's Band 13 – unlikely the other LTE6 models. Now... while it has the bands for Verizon, you will very likely not be able to use IMEI for the Chateau to enable Verizon SIM – so for Verizon you'd have to active the SIM using another device, and then move the SIM to Chateau (and same for other Mikrotik LTE6 devices too). None are "certified" by Verizon, so they won't enable any Mikrotik modem. But if you put a working SIM into an LTE6, it's likely work for Verizon but still limited. And, LTE6 models don't use LTE Band 66 or Band 30, which are pretty common these days for AT&T/Verizon, why I say "none work great".You can check the bands an area using cellmapper.com & compare those with Mikrotik's offerings. But basically any of the LTE12 or LTE16 or 5G models will not work in the US. ---

## Response 7
None work "great" and no 5G options for US.The LTE6 will work okay with AT&T, albeit 5G and limited to CAT6 speeds - but it does at least couple CA modes for AT&T. And LTE6 may work for Verizon, in some areas, but it's without Verizon's Band 13 – which VZW widely deployed/uses – there be no CA.The only option is the Chateau LTE6-US. That does have Verizon's Band 13 – unlikely the other LTE6 models. Now... while it has the bands for Verizon, you will very likely not be able to use IMEI for the Chateau to enable Verizon SIM – so for Verizon you'd have to active the SIM using another device, and then move the SIM to Chateau (and same for other Mikrotik LTE6 devices too). None are "certified" by Verizon, so they won't enable any Mikrotik modem. But if you put a working SIM into an LTE6, it's likely work for Verizon but still limited. And, LTE6 models don't use LTE Band 66 or Band 30, which are pretty common these days for AT&T/Verizon, why I say "none work great".You can check the bands an area using cellmapper.com & compare those with Mikrotik's offerings. But basically any of the LTE12 or LTE16 or 5G models will not work in the US.Thank you for the detailed answer.I remember reading this quite a while ago. I supposed I was hoping the situation had changed.I am not inclined to buy a Chateau LTE6-US knowing I will have to register the sim card in a different device and then hope is works and continues to work. ---

## Response 8
Understandable. I regularly complain about this. But it has not improved for North American LTE/5G users — and newer LTE devices are even worse the older ones. The original CAT6 modems at least worked with AT&T and T-Mobile... but newer "refreshed" LTE devices, generally with "(2024)" in name, will NOT work in US since the new ones lack even bands 2/12. ---
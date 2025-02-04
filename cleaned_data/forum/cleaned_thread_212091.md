# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 212091

# Discussion

## Initial Question
Author: Mon Oct 28, 2024 10:41 am
At the moment our whole house is covered from a centrally located RB4011. However the coverage is marginal in one of the front rooms and not particularly good in the other. So I need another device, either move the RB towards the front and add the new AP at the back, or vice versa.Either way the AP will be mounted in eaves space or similar so can't be directly mains powered. The neatest way would be to power it from the RB, removing the need for power injector or indeed any sort of mains PSU.But as far as I can see all the dedicated APs need 802.3af etc, whereas PoE out on the RB is passive, Have I missed so something? Or does this mean I'll need to use something like one of the small routers and just configure it for wireless only.Thanks. ---

## Response 1
Author: [SOLVED]Mon Oct 28, 2024 10:42 am
Well nearly all MikroTik APs support passive PoE input, so it's not an issue. If you use another brand, you might need an additional PoE switch then. ---

## Response 2
Author: Mon Oct 28, 2024 11:06 am
Well nearly all MikroTik APs support passive PoE input, so it's not an issue.Thanks. Just to be specific both CAP AX and WAP AX data sheets state "PoE in .. 802.3af/at". Can they in fact also be powered by passive PoE?I could be misunderstanding, is it the case that devices listed as using passive PoE don't support the af/at signalling and therefore won't enable power from an 802.3af device? ---

## Response 3
Author: Mon Oct 28, 2024 11:09 am
Thanks. Just to be specific both CAP AX and WAP AX data sheets state "PoE in .. 802.3af/at". Can they in fact also be powered by passive PoE?Yes ---

## Response 4
Author: Mon Oct 28, 2024 11:58 am
Brilliant, thanks to both of you.
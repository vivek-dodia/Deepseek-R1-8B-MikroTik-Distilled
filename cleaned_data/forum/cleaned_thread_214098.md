# Thread Information
Title: Thread-214098
Section: RouterOS
Thread ID: 214098

# Discussion

## Initial Question
Hi, Can You add option to set PoE status on boot? For example: i have PoE "forced on" on eth2, but when there is a power outage, after restarting the port will be off. (you can set on, off, previous state - on boot). Just like in smart plug ---

## Response 1
You can add a script in scheduler, it has an option to run at startup (and interval must be 0), see:https://help.mikrotik.com/docs/spaces/R ... /Scheduler ---

## Response 2
I concur with @jaclazYou can use a Script / Schedule to automatically set the PoE Status on startup.Script-Exemple to set PoE-Status for a specific Interface (for exemple ether5 to forced-on)
```
/interface/ethernet/setether5 poe-out=forced-onScript-Exemple to set PoE-Status for ALL Interfaces (for exemple ALL Ethernet that support PoE to forced-on)
```

```
foreachiin=[/interface/ethernet/poe/find]do={/interface/ethernet/set$i poe-out=forced-on}

---
```

## Response 3
This is not a solution, becouse:"startup - execute the script 3 seconds after the system startup."3 seconds is too lateI use poe out as relay status changer ---

## Response 4
Hi, Can You add option to set PoE status on boot? For example: i have PoE "forced on" on eth2, but when there is a power outage, after restarting the port will be off. (you can set on, off, previous state - on boot). Just like in smart plugNever happen to me, hardware and RouterOS used?Fundamental details that everyone uselessly omit or do not ask before reply. ---

## Response 5
I set forced-on on PoE out. If You turn off power, its normaly that poe doesn't work. Relay change it status (power back). But when system boot, last state of PoE will be set (in my case to forced-on) and this cut the power and mikroik goes to off, relay cut off power. And I have some kind of bootloopWhen I can change PoE to - off on startup the bootloop will not happenRouterOS: 6.49.17Routerboard mAP ---

## Response 6
I don't understand.Can you draw a schematic of how this relay is connected?In any case the scheduler script can be made to check the current status and act depending on that. ---

## Response 7
It doesn't matter how the relay is connected for be powered from mAP when is forced-on, but what does it do (the relay)?Is the contact normally open or normally closed?What does the contact control?The relay change power source of the mAP?Be more specific. ---

## Response 8
I made a simple test for acu from a buffer power supplywhen I set "forced-on" eth2 the relay cuts off the power supply from the mains and the script periodically checks the voltage from battery. When the voltage drops to about 10.5V (from 12) the test ends and the script changes PoE to "off" and change relay state.But when I have a broken battery, I have a bootloop, because mAP sets the last state at startup - "forced-on" on eth2The solution is possiblity too set state of PoE after power outage. Mikrotik can do this:) I believe on it ---

## Response 9
So you are using the NC contacts of the relay on the (connected to mains) power supply to power the mAP.Then, when you set the device on "forced on", you open the contact and power to the mAP comes from the battery (in parallel or enabled from the NO contact?).When the voltage becomes too low (from battery) the script should set the PoE to off, thus re-enabling powering from power supply.But if the battery breaks, the mAP becomes not powered, the relay NC returns to its normal state, powering the device (that reboots) from power supply.The PoE is forced-on as this was the last state before reboot, and thus the power is cut again and you enter into the reboot loop.Did I get it right? ---

## Response 10
Yes.Battery is connected to buffer power supply.the relay is for cutting off the mains power supply ---

## Response 11
I wouldn't count too much on Mikrotik changing the behaviour of the boot sequence.You can probably get around with a more sophisticated circuit, or, simpler, use a "time delay" relay.I have seen el-cheapo ones (low power, but you don't need that much current) on sale on Aliexpress for a few $/€, they are called YS-RT1Q, YS-RT1C, YS-RT1K, YS-RT1T, YS-RT1M, various different models with different behaviours:https://it.aliexpress.com/item/1005005948375298.htmlyou probably want the YS-RT1C and put its contact in parallel to your relay, when you apply power it bypasses, closed, the forced poe one (that is still open) for n seconds, then it opens, giving the time to operate the forced poe commands. ---

## Response 12
Rethinking about it, it would make more sense to use a toggle/latch relay.The mechanical ones are not suitable because they remember the last state they were on when power goes out (battery broken or exhausted), but I believe that electronic ones that default to either on or off at boot do exist.Electronic experts or enthusiasts will probably have a fit, but there is a purely electromechanical circuit that could do, with two two poles relays, I am attaching it just in case.T_flip_flop.pngThe .txt is the file that can be used in the simulator athttps://www.falstad.com/circuit/circuitjs.htmlso that one can play with it. ---
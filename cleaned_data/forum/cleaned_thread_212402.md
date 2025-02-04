# Thread Information
Title: Thread-212402
Section: RouterOS
Thread ID: 212402

# Discussion

## Initial Question
If I have a10Gbps SFP+in a RB5009 or CCR2116 and connect it to a device with a 2.5Gbps port, there is loss of TCP packets over 1Gbps.The 10Gbps coppert SFP+ module 'auto negotiates' down to 2.5Gbps -- the remote site reports 2.5Gbps, but the RB5009 and CCR2116 report 10Gbps (incorrect!).When using that port, UDP will flow through at expected speeds, but TCP gets retransmits and bottlenecks down to 100 - 200Mbps:TCP-Bottleneck.pngInterestingly, if I run a speedtest limited to 1Gbps (by plugging in a device into a 1gbps port on the RB5009) and then send backed through the RB5009 and out the 10Gbps port, I can get 1Gbps symmetric with TCP. The 'bottleneck' only starts happening at over 1Gbps.ADVICE: DO NOT USE 10GBPS copper SFP+ to connect to 2.5Gbps ports!I am running 7.15.3 - Will there be a fix in future releases to show a port at '2.5Gbps' when that is what the SFP negotiates at? That may fix the issue.(Image above is from a UBNT Wave antenna blue is RX on the Mikoritk SFP+ port, Purple is TX on the port. Note the low speeds with TCP TX.) ---

## Response 1
Given the routers are fairly powerful.For the outbound traffic, you can probably attach some sort of queue to the sfp+ interface.Queues based on cake are usually easy, perhaps fqcodel might be better in this case butI am no expert on queues. (I have had success with red queues in the past)Set it up with packet-mark=no-mark and all the other packet marks you use (if any).Start with a maximum limit of 2.5GAnd see how that goes. ---

## Response 2
As mentioned by yourself a better option, get a 2.5G ethernet sfp to plug into the router.Much cheaper and cooler than the 10G device.fs.com have them. ---

## Response 3
To use 2.5G device the SFP+ Ethernet port has to be configured on the Mikrotik device in a specific way - it's described in the MT Docuhttps://help.mikrotik.com/docs/spaces/R ... ansceiversIt actually refers specifically to 2.5GB transceivers, but it is likewise applicable to 10G transceivers intended to operate with a 2.5G link speed.In short, turn off auto negotiation and set link speed to 2.5G-baseX. I had to learn that as well in a hard way and after spending lots of hours in troubleshooting to get the connection working reliably as a 2.5G link. ---
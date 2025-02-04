# Thread Information
Title: Thread-214337
Section: RouterOS
Thread ID: 214337

# Discussion

## Initial Question
Has anyone ever supported Allen & Heath mixer boards and attempted to run theirDSNAKEprotocol over MikroTik switches?Here is an articlethat states it should be possible.I'm running into slight issues and wonder if you could help me make it work. Two switches, standard VLAN configuration.I have the mixer’s DSnake port connected to switch1 (CRS326). Switch1 is connected via 10G fiber to Switch2 (CRS328). The AR2412 is connected to Switch2. All on a private VLAN. Running rOS ver 7.17.About every 30 seconds, the yellow Lnk/Err light stops flashing yellow, and goes steady red (for error) for 5 seconds.When the Mixer and AR2412 are connected directly, using the same shielded cat6a cables, the Lnk/Err light only flashes yellow, which means all is good. Of note, when the light goes red, audio does not stop, at least not in my test.Any tips? ---

## Response 1
Disclaimer: I don't know a thing about dSNAKE.Once I had a closer look at a pair of USB/DP extender which uses UTP cables between them. They speak ethernet frames, so placing switch in between (with dedicated VLAN as well) still allowed them to communicate. Even though officially using ethernet switches in between is not supported.What I observed was huge number of MAC addresses appearing in switch's FDB. My speculation is that these devices use ethernet frame structure, but don't adhere to proper ethernet header structure ... they simply fill ethernet frames, including frame headers, with payload. So basically (ab)using ethernet hardware (MII) as cheap L1 for their own communication.Observed behaviour for sure can fill up FDB (and quickly) and switch is more than right to signal error state ... while still forwarding frames but without using FDB (which essentially means they start to behave as high-speed VLAN-aware ethernet hub, forwarding all frames to all eligible ports). ---

## Response 2
Excellent points mkx. Do you know if MikroTik hardware can be configured to play nice with that?Hereis another article from Allen & Health, that their support team states applies to dSNAKE as well.They state two things that could be my issue. One, force 100Mbps. Two, some fiber SFP modules don't have the time accuracy their clock based protocol requires. ---

## Response 3
I can't comment on 100BaseTx and SFP modules. So it remains to comment on compatibility with MT gear: if their solutions are truly L2 compatible with ethernet, then it shouldn't be a problem at all to use any kind of ethernet switch in between (apart from the timing constraints ... every switch can add some delay and increase delay jitter), be it dumb or managed, VLANs or no VLANs. The KVM extenders I described in my previous post were clearly not L2 ethernet compliant devices.I've had my share of disappointments when it comes to how electronics designers understand networking though ... ---
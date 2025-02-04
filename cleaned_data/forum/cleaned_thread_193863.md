# Thread Information
Title: Thread-193863
Section: RouterOS
Thread ID: 193863

# Discussion

## Initial Question
Hallo @everyone.I want to secure a DarkFiber (Layer 2) with 2 powerfull MikroTik Router with IPsec.Setup:2x CCR2004-1G-12S+2XS2x XS+27LC15D SingleMode 10GbitDarkFiber distance 6kmFirst attempt:Layer2 Connect with EoIP Tunnel:
```
0name="eoip-tunnel-destinationA"mtu=autoactual-mtu=1458l2mtu=65535mac-address=02:B1:B6:4A:B7:33arp=enabled arp-timeout=autoloop-protect=defaultloop-protect-status=off 
      loop-protect-send-interval=5sloop-protect-disable-time=5mlocal-address=0.0.0.0remote-address=172.31.0.14tunnel-id=2keepalive=10s,10dscp=inherit clamp-tcp-mss=yes dont-fragment=noipsec-secret="ipsecsecret"allow-fast-path=noIPsec Profile
```

```
0*name="default"hash-algorithm=sha256 enc-algorithm=aes-256dh-group=modp1024 
     lifetime=1dproposal-check=obey nat-traversal=yes dpd-interval=2mdpd-maximum-failures=5Now here the results:Bandwidth Test (tcp receive)direct: 3.2 Gbps (CPU Load 70%)over EoIP Tunnel 966 Mbps (CPU Load 46%)Question:- Are there any Options for Performance improvement?- other Method (MAC Secure)?- going up to Layer 3?Thanks.

---
```

## Response 1
As you mentioned macsec (IEEE 802.1AE). However, as the documentation is not up to date, it's hard to say anything about the implementation and performance. I'd email Mikrotik and ask. Why not test it yourself using /interface/macsec (WinBox interface). I think many, including myself, would be very interested in the results. ---

## Response 2
i`ve tried MAC Secure.But the Performance with the given Hardware is unacceptable:155 Mbit on 100% CPU Load. ---

## Response 3
To bad, it probably due to pure sw encryption. However, since they haven't published any information yet, one can hope they are actively working on hardware offloading support. ---

## Response 4
Is there any other Option i have missed?Are DarkFiber Connections over Public Areas always unsecured? ---

## Response 5
Not really but Arista, Cisco, Juniper (and many others) all have decent macsec enabled switches.The requirement for dark fiber encryption often depends on the level of perimeter protection that exists, the ability of L2 intrusion detection and so forth. However it all depends the business case itself and what level of security it requires which is usually where one start digging around. ---

## Response 6
It really depends on your use case. Most apps secure sensitive traffic at Layer 3 using SSL, including Internet traffic, email, local websites and databases, etc. What's left on most LANs are traditional peer-to-peer or server-client traffic that may or may not be encrypted (file servers, VoIP, cameras and access systems, etc.).In a previous job, we had lots of lit circuits, where the customer (a cell phone provider or other large business) would hand off a connection to us, we'd haul it over our network at Layers 1+2, then hand it to them at the remote end. In the middle would be conversion from 1G to 10G, multiple VLAN tags, conversions from 1310nm or 1550nm to any number of DWDM wavelengths, then back again. We didn't run encryption on any of it, and I doubt they did too (carriers maybe, businesses probably not). But then, there may have been a lot of that going on on their side at Layer 3 that we didn't know (or care to know) about.With lit services, it would have been relatively easy for us (the telco) to put the port into mirror mode and monitor things without the customer knowing. (Mirroring is done all the time for testing and circuit validation). Part of your job as the provider is to maintain your customer's security. If you don't trust the provider to securely handle your service (locked buildings, monitored circuits, cameras, proper employee training, etc.), then you don't use them, or you encrypt at Layer 2 and take the performance hit.That all said, this is dark fiber, i.e. you're the only one with electronics on the pair. So the provider's primarily responsible for physical access. It's not an easy task for someone who isn't familiar with your setup to doallof the following:Find the fibers you're usingFind a spot where there isn't a jacket on the fiberAttach a laser-detection device that grips each fiber just enough to see if there's light on it without completely stopping the flow of traffic (difficult)Said device has to be able to decode whatever laser(s) you're using (any wavelength, transmission rate) and capture Ethernet packets (super expensive, if it exists)Do this undetected by any human at either end or anywhere along the telco route (nearly impossible unless they're an insider)For somebody to be able to successfully pull this off, they'dhaveto be an insider, either from your company or from the provider, and would need intimate knowledge of everything about the connection: laser wavelength and modulation, locations of splice points and handoffs, and the aforementioned equipment. Or they'd have to be a government with all the spy movie gadgets. Even then, your lasers would detect a drop in signal levels if somebody so much as put a light finder on a fiber. (You can't see light on glass unless it's bent enough to force some of it to jump the core, which causes loss.)Unless you believe your company could be targeted by high tech government types or untrustworthy employees/contractors, I'd say running security at Layer 2 may be overkill. (Honestly, if an outsider can get past Layer 1 security in this scenario, decrypting the stream's going to be a cakewalk.) ---

## Response 7
Many thanks for this very detailed explain to use (or not use) encryption on a DarkFiber. This is a point of view of a Provider - i guess.On our side as a Customer we take care on every personal Data we save on our encryptetd Storage. We have to - because this is the Law.On the other Hand we secure every single Port on all our Switches with Portsecurity. (Inhouse)But outside? For example:In case of a missreading of an Network Engineer, our Fiber goes to another Customer and he get Access to our Network and read some Metadata (not really personal data) and publish this to a news company..... YOU have to go.Is this an unreal or possible scenario?Maybe.Who did measure the signal on fiber all the time to detect a signal loss of bended core? Are there known limits for example? ---

## Response 8
It's very hard to tell from your description, but a general advice is to implement layered security to ensure there is no single point of vulnerability and in your particular case it might mean end-to-end L2 security (aka zero trust)However, anyone working in the industry is aware that security is a complex thing and usually quite expensive to implement, so my advice is to hire a skilled security expert to get it right from the start according to the client's requirements.Also, this forum might not the best place for this kind of discussions.Ps..Regarding "In case of a missreading of an Network Engineer, our Fiber goes to another Customer" - This is hardly a problem with dark fiber if the fiber cable is placed and routed correctly according to best practices and current regulations. L2 IDS works if correcty implemented. ---

## Response 9
With physical plant, there's no way they can "accidentally" redirect it to another customer and have things work. You'll know if the connection between the two goes down (or if it never comes up). Sure, any two 1550nm 10G SMF modules should talk to each other, but unless the other customer has the exact same network settings that you do, nothing's going to happen (plus their stuff won't work either).In other words, alotof things have to happen in order for this particular attack vector to succeed.The switches and routers generally show stats from the SFP when you select the SFP+ interface itself, or type "/interface/ethernet/monitor <name of sfp interface>".This is from a 1330 SFP. You can see that it's a 20km capable SFP and RX power is essentially 0 (this run of dark fiber is only a couple hundred meters long).
```
name:sfp4-uplink
                    status:link-okauto-negotiation:donerate:10Gbpsfull-duplex:yes
           tx-flow-control:norx-flow-control:noname:sfp4-uplink
                    status:link-okauto-negotiation:donerate:10Gbpsfull-duplex:yes
           tx-flow-control:norx-flow-control:noadvertising:link-partner-advertising:sfp-module-present:yes
               sfp-rx-loss:nosfp-tx-fault:nosfp-type:SFP-or-SFP+sfp-connector-type:LC
        sfp-link-length-sm:20kmsfp-vendor-name:OEM
    sfp-vendor-part-number:AXB32-192-20sfp-vendor-revision:A
         sfp-vendor-serial:CSGXXXXXXXX
    sfp-manufacturing-date:22-05-31sfp-wavelength:1330nmsfp-temperature:41Csfp-supply-voltage:3.327Vsfp-tx-bias-current:34mAsfp-tx-power:-0.277dBmsfp-rx-power:-0.006dBmeeprom-checksum:goodIf this is visible via SNMP (I don't know, I haven't tried), you could poll for it and graph it.  The signal should remain within a 2-3dB range over the course of a year due to temperature variations, and would change slightly with the weather, if at all.  If you see a sudden change (drop), you'd want to alarm on that.

---
```

## Response 10
@Ollis, some follow-up questions:1) what speed are you aiming for?2) just curious but did you even look at theCCR2004 specsbefore buying the unit?3) why are you so eager to implement all this yourself when you (at least seem to) lack the necessary skills or experience covering all the levels of network security needed in this case?It might sound harsh but that is absolutely not my intention, I'm just trying to understand. ---

## Response 11
@LarsaThanks for focusing on the right topic.1) The Best Performance we can get for the budget- see 3)2) The CCR2004 was picked up - because of the best choice in IPSec Performance3)This Thread was started to figure out if this is a way to go with MikroTik Hardware. My goal was a Solution without the need of an expensive (and very well known) macsec Hardware.I was focused on EoIP with IPsec. Test Results are good for comparison - but we don´t live in a 512kbit Packetsize only.So i want to open my mind for other Solutions and Listen to experienced Users.My search on the web does not found a Solution like this. Maybe this is not a way to go.I hope this help to figure out my decisions. (and it must be hard to read for english native) ---

## Response 12
Hey, no problem!As I see it, it's more about optimizing IPsec rather than Dark Fiber itself. Unfortunately, I have no experience on how to optimize IPsec using a CCR2004, so my advice is to start a new thread with, for example, "How to optimized IPSec for maximum throughput P2P using CCR2004?". I think you should consider to email Mikrotik and ask about the most optimal setting as well.Things you can investigate yourself and also include as background in the new thread are, for example:- how the test itself is performed like tools, how the tools are configured, from where do you run the tests, protocol (udp/tcp), packet size in relation to the tunnel MTU and so on.- tunnel configuration.- how the load is distributed over the cores.- different IPSec encryption algorithms used.- with or without firewall (connection tracking on/off).- I'm sure I've forgotten several other parameters..EDIT:1. If you are going to email Mikrotik, why not take the opportunity to ask about macsec hardware offload in the same time.2. Once you find the optimal settings, please feel free to post the configuration to benefit others with similar issues on a CCR2004. ---

## Response 13
Not really but Arista, Cisco, Juniper (and many others) all have decent macsec enabled switches....if it is just for MACsec securing dark fibre and need to stay on a budget (sort of) consider a look towards the fs.com S5800-48F4SRit supports MACsec wirespeed ---

## Response 14
The problem is probably not the encryption. It's the encapsulation. Mikrotik doens't have any support for hardware-encapsulation. Most of them just have offload for the encryption. ---

## Response 15
Go buy a 2nd hand switch starting with Cisco Catalyst 3560X onwards , 4xxx / cisco industrial( IE series) switch as they hardware offload'ed macsec.Even Juniper's got a good collection of macsec enabled switches.You can even buy off the shelf dedicated MACSEC media converters now-a-days :https://www.extremenetworks.com/product ... ec-adapterFrom testing Mikrotik's current MACSEC as of 7.17 is single threaded and is quite poor performance.Its strange that MT's favorite chip supplier MARVELL didn't offer MT one of there chips that has MACSEC integrated, as they have boat-loads of supported switching chips with it available. ---

## Response 16
You can even buy off the shelf dedicated MACSEC media converters now-a-days :https://www.extremenetworks.com/product ... ec-adapter...which requires an additional license for MACsec operation AND an extreme-networks host switch to even manage this adapter. ---

## Response 17
Its strange that MT's favorite chip supplier MARVELL didn't offer MT one of there chips that has MACSEC integrated, as they have boat-loads of supported switching chips with it available.I'm pretty sure that Marvell isn't denying MT to use some of their MACSEC-enabled switch chips ... it's probably MT's (commercial) decission to go with cheaper switch chips (and implement MACSEC as software-only feature until prices of hardware drop low enough). ---
# Thread Information
Title: Thread-1122851
Section: RouterOS
Thread ID: 1122851

# Discussion

## Initial Question
Hello everyone, I have a question and I would like some help from you.Imagine the scenario like the image above, I have 3 switches, Switch1 Switch2 Switch3, all are CRS317, they are physically connected as in the image. The connection in red is a transport that was contracted from another internet provider (ISP) so that I can have a ring network. The problem is that RSTP doesn't work in these cases, so I had the idea of ​​using VXLAN. The transport ISP gives me a vlan to be configured on both switches, I configured these vlans, configured an IP on them, and they are already communicating, logically this configuration is via the CPU.My question is the following, if I make a VXLAN, over these IPs, which are over vlan at CPU level, when the VXLAN works, will it work via Switch CHIP or also via CPU and then consume all the CPU? Remembering that I will test with v7.18beta to test the VXLAN HWI'm in doubt because these IPs are on top of a vlan and then vlxan over these IPs ---

## Response 1
be aware beta version is not meant to be used in production networks ---

## Response 2
The HW-offload VXLAN support is very basic right now. I couldn't get it to pass tagged traffic coming into the same VLAN from other switches, only untagged traffic (from another port) tagged into the VLAN that the VXLAN is assigned to.So there's still some work to be done. Having it ride over another VLAN is definitely not going to work. ---

## Response 3
The HW-offload VXLAN support is very basic right now. I couldn't get it to pass tagged traffic coming into the same VLAN from other switches, only untagged traffic (from another port) tagged into the VLAN that the VXLAN is assigned to.So there's still some work to be done. Having it ride over another VLAN is definitely not going to work.but do you think that the VXLAN tunnel, closed over a VLAN, in the tunnel just normal traffic without vlan, would work? ---

## Response 4
but do you think that the VXLAN tunnel, closed over a VLAN, in the tunnel just normal traffic without vlan, would work?The only thing you can do is lab it up and give it a try. EdPa put an example of something that works on the 7.18b2 thread. I tried it on a pair of 309's and it works as described/configured. ---
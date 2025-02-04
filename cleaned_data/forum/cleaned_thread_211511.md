# Thread Information
Title: Thread-211511
Section: RouterOS
Thread ID: 211511

# Discussion

## Initial Question
Test scenario: Two interfaces in the same VRF. This VRF is part of an MPLS L3VPN, but the test scenario is just between two nodes connected to two different VLANs, two different subnets, same VRF routing between each other. Instead of getting the expected line-rate routing, it all appears to be going through the CPU which jumps to 100% and provides abysmal performance.Is this per expectation? Are there plans to fix it? Does VRF HW offload work on any MikroTik hardware?Thanks! ---

## Response 1
Hi, Unfortunately, L3HW doesn't support VRF yet. The hardware (switch chip) supports it, but the feature has not yet been implemented in RouterOS. There are plans to add VRF L3HW, but I cannot share the ETA at the moment of writing. ---

## Response 2
Hi, Unfortunately, L3HW doesn't support VRF yet. The hardware (switch chip) supports it, but the feature has not yet been implemented in RouterOS. There are plans to add VRF L3HW, but I cannot share the ETA at the moment of writing.Any chance of an ETA now? on CCR2216 99% of people will most likely use some form of VRF which kills any form of L3HW from being available.I watch ever beta being released just to see if this feature is available. ---
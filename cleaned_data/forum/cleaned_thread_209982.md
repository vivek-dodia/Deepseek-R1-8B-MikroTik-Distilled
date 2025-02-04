# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 209982

# Discussion

## Initial Question
Author: [SOLVED]Thu Aug 08, 2024 12:47 am
``` https://www.youtube.com/watch?v=c2sAA6jMjCY ``` You need a single vlan aware bridge to take advantage the switch chip and activate L3 hardware offload if you need intervlan routing, remember CRS is geared toward a switch with limited routing capabilityThis is a great guide
```
Mikrotik is very verbose compare to any other L3 switch in the market, I know it's confusing at first


---
```

## Response 1
Author: Sat Aug 17, 2024 10:50 pm
``` https://www.youtube.com/watch?v=c2sAA6jMjCY ``` You need a single vlan aware bridge to take advantage the switch chip and activate L3 hardware offload if you need intervlan routing, remember CRS is geared toward a switch with limited routing capabilityThis is a great guide
```
Mikrotik is very verbose compare to any other L3 switch in the market, I know it's confusing at firstSorry for the long delay - I needed time to finish some projects and test this. This was a perfect fix. My CSV transfer rate was 256+Mbps ( easily doubled ) and I haven't tried direct LUN but my CPU stayed under 35% during the transfer.Also, the video you sent me helped me understand MikroTik's VLAN logic and utilization ( which I had done wrong before this video ).So, double thank you - because you helped me see how to implement VLAN and Layer-3 networking correctly - which I have wanted to explore anyway.
```
# Thread Information
Title: Thread-1113681
Section: RouterOS
Thread ID: 1113681

# Discussion

## Initial Question
H All, At our main site, we have a 500 Mbps link to our ISP. An issue arises when our on-prem server runs a backup sync to the cloud, which saturates the link. This leads to the ISP policing our traffic and dropping packets. These dropped packets affect call quality for other sites using the CUCM servers hosted at the main site.I’ve proposed a plan involving traffic marking and queuing to manage this, but I’m looking for any suggestions for improvement or potential issues.Variables:192.168.0.1 (CUCM Publisher)192.168.0.2 (CUCM Subscriber)192.168.10.1 (Benetas cloud Server)192.168.20.1 (On-Prem server)Wan interface: ether1Model: RB3011UiAS, Version: 6.47.10Stage 1: Mark packetsVOIP:
```
/ip firewall mangleaddchain=forward src-address=192.168.0.1action=mark-packetnew-packet-mark=CUCM-Publisherpassthrough=yesaddchain=forward dst-address=192.168.0.1action=mark-packetnew-packet-mark=CUCM-Publisherpassthrough=yesaddchain=forward src-address=192.168.0.2action=mark-packetnew-packet-mark=CUCM-Subscriberpassthrough=yesaddchain=forward dst-address=192.168.0.2action=mark-packetnew-packet-mark=CUCM-Subscriberpassthrough=yesBackup traffic:
```

```
/ip firewall mangleaddchain=forward src-address=192.168.10.1dst-address=192.168.20.1action=mark-packet \new-packet-mark=backup-sync-traffic passthrough=yesaddchain=forward src-address=192.168.20.1dst-address=192.168.10.1action=mark-packet \new-packet-mark=backup-sync-traffic passthrough=yesStage 2: General shaper
```

```
/queue treeaddname="WAN-Shaper"parent=ether1 packet-mark=no-mark max-limit=480M\
            limit-at=480Mburst-limit=480Mburst-threshold=460Mburst-time=20s\
            bucket-size=0.005priority=1Stage 3: Other shapersVOIP
```

```
/queue treeaddname="CUCM-Publisher"parent=WAN-Shaperpacket-mark=CUCM-Publisher\
            max-limit=20Mlimit-at=10Mpriority=1addname="CUCM-Subscriber"parent=WAN-Shaperpacket-mark=CUCM-Subscriber\
            max-limit=20Mlimit-at=10Mpriority=1Backup:
```

```
/queue treeaddname="Backup-Server-Limit"parent=WAN-Shaperpacket-mark=backup-sync-traffic \
            max-limit=100Mlimit-at=50Mburst-limit=100Mburst-threshold=90M\
            burst-time=15spriority=8Thanks in advance for any assistance

---
```

## Response 1
As a start, I would be inclined to just put a single cake queue attached to the WAN interface, to see how well (or not) it works.(With no packet marking for shaping)Set it up for 500M, and a bucket size of 0.005-0.01, (or your settings) and see how it goes.You will need to create a new queue type using the cake base type, with near default settings.You will need it to match on packet-mark=no-mark, and any other packet marks you might currently use if any.You should not need to disable fast path processing (if enabled) with this setup.Cake seems be fairly clever at managing traffic. ---

## Response 2
Thanks for your reply @rplantI just had a look at the CAKE documentationhere(i hadnt heard or configured it before), it looks like the feature is only available in version 7?The following queue kinds CoDel, FQ-Codel, andCAKEavailable since RouterOS version 7.1beta3. ---

## Response 3
Sorry, I should read things a bit more thoroughly.Unfortunately, the 3011 seems to not be great under v7.Perhaps what you have will be good.Though I do not understand why you have a limit of 100M on the backup traffic.You will likely need to add all the packet marks to the parent (WAN-Shaper) so it gets them all.Presumably there is also a bunch of other traffic which you could also put below the parent queue.(Probably with queue matching no-mark, and perhaps priority 2 ) ---

## Response 4
One other thought,(Somewhat more like my original thought)You could perhaps make a new pcq type queue, based on pcq-upload-default, but with a 24 mask.(So everything from 10.0.1.x will be counted together)Then back to no marking, and fast track allowed.The low rate lans will be prioritised over the high rate (busy) lan. ---

## Response 5
Though I do not understand why you have a limit of 100M on the backup traffic.100M was just an arbitrary number that i was going to play around with.Also i was a little confused byyou could perhaps make a new pcq type queue, based on pcq-upload-default, but with a 24 mask.(So everything from 10.0.1.x will be counted together)Then back to no marking, and fast track allowed.The low rate lans will be prioritised over the high rate (busy) lan.Would it be something like this?QUEUE TYPE:
```
/queue typeaddname=PCQ-Upload-24kind=pcq pcq-classifier=dst-address pcq-rate=10Mpcq-total-limit=500000/queue typeaddname=PCQ-Download-24kind=pcq pcq-classifier=src-address pcq-rate=10Mpcq-total-limit=500000QUEUE TREE:
```

```
/queue treeaddname=Uploadparent=globalqueue=PCQ-Upload-24max-limit=500Mpacket-mark=no-mark/queue treeaddname=Downloadparent=globalqueue=PCQ-Download-24max-limit=500Mpacket-mark=no-markThen play around with the pcq-rate?

---
```

## Response 6
I was thinking of something like./queue typeadd kind=pcq name=pcq-upload-24 pcq-classifier=src-address pcq-dst-address-mask=24 pcq-src-address-mask=24It just groups each /24 lan subnet together so the large upload machines get lumped together.On testing, you may find the pcq-upload-default works better for you.At this stage I would perhaps not attempt putting QOS on downloads as well, I doubt if you will have much spare cpu, 500M is quite quick.(But I could easily be wrong) ---

## Response 7
Thanks @rplantI will try that and see how it goes. Thanks again! ---
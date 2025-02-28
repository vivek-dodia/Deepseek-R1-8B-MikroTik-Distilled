# Thread Information
Title: Thread-1123414
Section: RouterOS
Thread ID: 1123414

# Discussion

## Initial Question
Hi, I am using ATL + hAP ac³.Recently I experienced an Internet disconnection. I immediately connected to the ATL via SSH and tried to check the signal strength using the monitor command. However, it returned a "sim not present" message. The ATL itself seems to work fine - no errors in log, I can access all functions and commands, so I don't expect the ATL hardware to have failed (right?). It is always powered via a UPS, so there are no surges, there have been no thunders either (it is winter time here).Is it possible that the MNO has somehow deactivated the SIM card (sound highly unlikely but who knows)? Or would the message in that case be different?Since the ATL is mounted on a high pole (difficult to reach and difficult to dismount) andifactual SIM replacement is necessary, I decided to ask for advice here first.So, what do you say? ---

## Response 1
The mobile ISPs use different approaches, but typically either the SIM is banned from logging into the network or just the data service is suspended. I hazily remember some old SIMs were treated as "invalid" in a phone but I have never seen the phone to see a SIM as absent. So if you give the ATL a power cycle and nothing changes, I am afraid you'll have to climb. I hazily remember there used to be issues with SIM thickness in the past, and also if you touched the contact area of the SIM with bare hand when handling it, a thin layer of corrosion may have built up. ---

## Response 2
Thanks for the feedback.I tried power cycling before posting here without success. I have not touched the electric contacts of the SIM card. I am always careful not to do that.Something strange happened though - a few hours after posting here, the ATL magically started working again. The log shows a few link up/down messages within ~15 minutes, after which there is stable link up.It is a mystery to me. If the SIM card was temporarily deactivated by MNO, then the "sim not present" message is surely misleading. If it was a poor electric contact, I really see no physical factors related to it. The disconnect happened late at night, there were no unusual atmospheric phenomena. The reconnect happened at noon on the next day. I have been using this hardware for about 2 years and this has never happened before. ---

## Response 3
Could be temperature related ... IIRC your ATL is high in the mountains where night temperatures might be quite low. And if some moisture entered ATL, it could add water condensation to the "happy mix". ---

## Response 4
the ATL magically started working againThat indeed reinforces trustI hate this kind of mysteries. Condensation or an insect? I've heard of a spider squatting in a satellite receiver LNA but he did not interrupt electrical contacts, just changed the capacity/inductance of something there, changing the parameters of a frequency filter.So a misleading error message sounds more likely to me. Do you happen to have the complete status message? Tx/Rx state would be interesting, it should be disabled if the modem sees the SIM as absent. ---

## Response 5
ETA: It just happened again - "sim not present" and no way to make it work.Could be temperature related ... IIRC your ATL is high in the mountains where night temperatures might be quite low. And if some moisture entered ATL, it could add water condensation to the "happy mix".Hi again, mkx!It is not really high. The altitude is less than 1000 m. Just a rural area with some hills.I thought about temperature but it still makes no sense. It is fairly warm now (about 10C) and there are no extreme temperature drops at night.Moisture - theoretically, maybe, but I don't see how it could possibly enter. The cap is pretty tight, the rubber sealing around the cable which enters the SIM compartment is also quite good.FWIW, I tried knocking hard on the metal pole (in case vibration might trigger mechanically electric contact) - nothing changed. Still "sim not present". Disabling/enabling the interface and hard rebooting didn't help either.[...] or an insect?It can't enter. On the ATL there are no gaps allowing that.So a misleading error message sounds more likely to me. Do you happen to have the complete status message? Tx/Rx state would be interesting, it should be disabled if the modem sees the SIM as absent.Where do I check for this info? ---

## Response 6
Where do I check for this info?/interface/lte/monitor lte1 ---

## Response 7
/interface/lte/monitor lte1
```
;;;simnotpresent
    status:simnotpresent
     model:EG18-EA
  revision:EG18EAPAR01A13M4G
      imei:<hiddenforprivacy reasons>That's the whole output.

---
```

## Response 8
Hm, so it apparently depends on the particular modem type:[me@myTik] > /interface/lte/monitor lte1status: radio offpin-status: SIM not insertedfunctionality: tx and rx rf circuit disabledmanufacturer: "MikroTik"model: "R11e-LTE"revision: "MikroTik_CP_2.160.000_v021"imei: <hidden for privacy reasons>My device is running ROS 7.16.2., what about yours? ---

## Response 9
My device is running ROS 7.16.2., what about yours?7.16.1BTW, I tried to be clever and did a bandwidth test between the hAP and the ATL, hoping that it may raise the temperature of ATL's CPU (as this loads it to 100%), thus raising the temperature near the SIM card slot (simulating daytime temperature, in case this is the reason), thus probably triggering electrical contact. Witty me LOL. It didn't work though (10 min test) ---

## Response 10
Still "sim not present".This morning is a little frosty. I am waiting to see if daily temperature might change something.I suppose it would have been good if these devices had eSIM. ---

## Response 11
I would recommend reaching out to MikroTik support for guidance. They might be willing to assist with troubleshooting. Enabling "lte, debug" logging could also provide more insights, but it’s important to know what to look for. Alternatively, the issue could be hardware-related, such as a loose SIM or a defect. In any case, it would be best to rule out software-related causes before climbing up the pole. ---

## Response 12
I would recommend reaching out to MikroTik support for guidance. They might be willing to assist with troubleshooting.I have done that already and sent a supout.rif as they asked for it. I am waiting for further feedback.Enabling "lte, debug" logging could also provide more insights, but it’s important to know what to look for.Support instructed me to do that too.Alternatively, the issue could be hardware-related, such as a loose SIM or a defect.ATL-related would be quite unfortunate. SIM-related (needing a SIM replacement) is much more acceptable, although reaching the SIM slot in my case is still not easy.In any case, it would be best to rule out software-related causes before climbing up the pole.That's what I am trying to do.FWIW, regarding what was discussed above, support said:While SIM deactivation by the MNO is rare, if that were the case, you would typically see an error indicating "registration failed" rather than "SIM not present." ---

## Response 13
Do you remember if it was a "proper sized" SIM or a smaller one with an adapter?There are reports (not only on Mikrotik hardware) of issues with the latter, see:viewtopic.php?t=211182&hilit=sim#p1099231viewtopic.php?t=211182&hilit=sim#p1099285but it depends on type/model (and probably manufacturer) of the actual SIM socket, I have seen an installer of elevators/alarms that puts a bit of electrician sticky tape on the back on the SIM and then "forces" it in the slot, but there is the risk of bending the pins. ---
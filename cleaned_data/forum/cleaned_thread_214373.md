# Thread Information
Title: Thread-214373
Section: RouterOS
Thread ID: 214373

# Discussion

## Initial Question
Our LtAP LTE6 works really well, the connection to the outside world through the SIM card is perfect, however the range of the wifi signal is only about 6-7 meters. I'm guessing that's not normal or is it? In any case is there some sort of a hardware setting for increasing the range? ---

## Response 1
Remove house walls/floors? ---

## Response 2
Remove house walls/floors?Oh it's a wooden house with practically no wallsSo my guess is that this isn't really an issue, the signal gets really weak on the same floor. ---

## Response 3
Remove house walls/floors?Oh it's a wooden house with practically no wallsSo my guess is that this isn't really an issue, the signal gets really weak on the same floor.Weird LOS should be good. Makes me think of some antenna orientation issue or more likely interference on the chosen frequency from something ?? ---

## Response 4
What I'm not sure is what is the expected range? Without any obstacles how far should the signal be good enough? ---

## Response 5
LOS easily 30 metres ---

## Response 6
Okay, then something is really not okay ...Any ideas on how to debug this? ---

## Response 7
Wifi is not my forte but posting the config is a good starting place./export file=anynameyouwish ( minus device serial number, any public WANIP information, keys etc. )_ ---

## Response 8
What do/interface wireless monitor wlan1and/interface wireless scan wlan1 background=yesshow? ---

## Response 9
The LtAP has a small 2GHz antenna inside, so it far from best for Wi-Fi performance in my limited experience with them.But @sindy is right, some data help. But my guess be "distance=" under Advanced, should be "indoor" - if not that can cause a lot flakiness. To check, go to "Wireless", then interface, then hit the "Advanced" button, then under in HT tab that appears , there is a "distance=" setting. In older default configuration, that used to be "dynamic" — but for normal Wi-Fi it should be "indoor". If that's wrong Wi-Fi will suck.Now you can wire-up pigtails to MMCX connectors on board (if I recall right), and use an external antennas be another option too. ---
# Thread Information
Title: Thread-211485
Section: RouterOS
Thread ID: 211485

# Discussion

## Initial Question
Hi.Devices= QRT5 (PTP)Using superchannel and no country.Band: 5GHz, Channel Width =20MhzScan List=4920-6100On Station-Bridge (Far End Antenna) I cannot use "Used Frequency" as it disconnects the link and also I cannot see the result. So I use /interface wireless scan wlan1 rounds=1 save-file=scan1The scan1 file lists Frequencies only between 4920 and 5380 MHz. It is same for all Mikrotik we use in different locations. My question is why scan1 file doesn't include frequencies beyond 5380MHz. Are there extra parameters?Thank you ---

## Response 1
check that in addition to the country you have entered the installation on outdoor to enable the outdoor frequencies ---

## Response 2
Thanks you for reply.Yes I had set installation:outdoor and "no country set" to get scan of as many Radio signals as possible ---

## Response 3
What ROS version ?There was a change in ROS 7.14 where "no country" results in "Latvia". ---

## Response 4
Both installation and country is there to comply with regulations.It has, afaik, nothing to do with scan results.Is it possible there are no radios in the neighbourhood transmitting at those frequencies? ---
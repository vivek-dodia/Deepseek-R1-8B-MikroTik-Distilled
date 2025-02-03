---
title: Spectral scan
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/139526162/Spectral+scan,
crawled_date: 2025-02-02T21:14:05.697782
section: mikrotik_docs
type: documentation
---

* 1Introduction
* 2Console2.1Spectral History2.2Spectral Scan
* 3The Dude
* 2.1Spectral History
* 2.2Spectral Scan
# Introduction
The spectral scan can scan all frequencies supported by your wireless card, and plot them directly in the console. The exact frequency span depends on the card. Allowed ranges on r52n: [4790; 6085], [2182; 2549].
A wireless card can generate 4us long spectral snapshots for any 20mhz wide channel. This is considered a single spectral sample.
To improve data quality spectrum is scanned with 10mhz frequency increments, which means doubled sample coverage at each specific frequency (considering 20mhz wide samples).
# Console
## Spectral History
```
/interface wireless spectral-history <wireless interface name>
```
Plots spectrogram. Legend and frequency ruler is printed every 24 lines. Numbers in the ruler correspond to the value at their leftmost character position. Power values that fall in different ranges are printed as different colored characters with the same foreground and background color, so it is possible to copy and paste the terminal output of this command.
* value-- select value that is plotted on the output. 'interference' is special as it shows detected interference sources (affected by the 'classify-samples' parameter) instead of power readings, and cannot be made audible;
* interval-- interval at which spectrogram lines are printed;
* duration-- terminate command after a specified time. default is indefinite;
* buckets-- how many values to show in each line of a spectrogram. This value is limited by the number of columns in the terminal. It is useful to reduce this value if using 'audible';
* average-samples-- Number of 4us spectral snapshots to take at each frequency, and calculate average and maximum energy over them. (default 10);
* classify-samples-- Number of spectral snapshots taken at each frequency and processed by the interference classification algorithm. Generally, more samples give more chance to spot certain types of interference (default 50);
* range--2.4ghz - scan the whole 2.4ghz band;5ghz - scan the whole 5ghz band;current-channel - scan current channel only (20 or 40 MHz wide);range - scan specific range;
* 2.4ghz - scan the whole 2.4ghz band;
* 5ghz - scan the whole 5ghz band;
* current-channel - scan current channel only (20 or 40 MHz wide);
* range - scan specific range;
* audible=yes-- play each line as it is printed. There is a short silence between the lines. Each line is played from left to right, with higher frequencies corresponding to higher values in the spectrogram.
## Spectral Scan
```
/interface wireless spectral-scan <wireless interface name>
```
Continuously monitor spectral data. This command uses the same data source as 'spectral-history', and thus shares many parameters.
Each line displays one spectrogram bucket -- frequency, the numeric value of power average, and a character graphic bar. A bar shows average power value with ':' characters and average peak hold with '.' characters. Maximum is displayed as a lone floating ':' character.
* show-interference-- add a column that shows detected interference sources;
Types of possibly classified interference:
* Bluetooth-headset
* Bluetooth-stereo
* cordless-phone
* microwave-oven
* CWA
* video-bridge
* wifi
# The Dude
The Dude is a free network monitoring and management program by MikroTik. Youcan download it here.
The Dude has a built-in capability to run graphical Spectral Scan from any of your RouterOS devices with a supported wireless card. Simply select this device in your Dude map, right click and choose Tools -> Spectral Scan.
This will bring up the Spectral Scan GUI with various options and different view modes:
# Document Information
Title: Spectral scan
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/139526162/Spectral+scan,

# Content
# Introduction
The spectral scan can scan all frequencies supported by your wireless card, and plot them directly in the console. The exact frequency span depends on the card. Allowed ranges on r52n: [4790; 6085], [2182; 2549].
A wireless card can generate 4us long spectral snapshots for any 20mhz wide channel. This is considered a single spectral sample.
To improve data quality spectrum is scanned with 10mhz frequency increments, which means doubled sample coverage at each specific frequency (considering 20mhz wide samples).
# Console
# Spectral History
```
/interface wireless spectral-history <wireless interface name>
```
Plots spectrogram. Legend and frequency ruler is printed every 24 lines. Numbers in the ruler correspond to the value at their leftmost character position. Power values that fall in different ranges are printed as different colored characters with the same foreground and background color, so it is possible to copy and paste the terminal output of this command.
# Spectral Scan
```
/interface wireless spectral-scan <wireless interface name>
```
Continuously monitor spectral data. This command uses the same data source as 'spectral-history', and thus shares many parameters.
Each line displays one spectrogram bucket -- frequency, the numeric value of power average, and a character graphic bar. A bar shows average power value with ':' characters and average peak hold with '.' characters. Maximum is displayed as a lone floating ':' character.
Types of possibly classified interference:
# The Dude
The Dude is a free network monitoring and management program by MikroTik. Youcan download it here.
The Dude has a built-in capability to run graphical Spectral Scan from any of your RouterOS devices with a supported wireless card. Simply select this device in your Dude map, right click and choose Tools -> Spectral Scan.
This will bring up the Spectral Scan GUI with various options and different view modes:
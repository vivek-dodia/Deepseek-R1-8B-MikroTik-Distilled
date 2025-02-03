---
title: Reset Button
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/24805498/Reset+Button,
crawled_date: 2025-02-02T21:08:45.126683
section: mikrotik_docs
type: documentation
---

# Introduction
The RouterOS password can only be reset by reinstalling the RouterOS or using the reset button (or jumper hole) in case the hardware is RouterBOARD. For X86(CHR) devices, only a complete reinstall will clear the password, along with any other configuration. For RouterBOARD devices, several methods exist, depending on the device model.
# Reset From RouterOS
If you still have access to your router and want to recover its default configuration, then you can:
* Run the command"/system reset-configuration"from a command-line interface;
* Do it fromtheSystem -> Reset Configurationmenu in the graphical user interface;
# Using Reset Button
RouterBOARD devices are fitted with a reset button which has several functions:
* Loading the backup RouterBOOT loaderHold this button before applying power, and release it after three seconds since powering, to load the backup boot loader. This might be necessary if the device is not operating because of a failed RouterBOOT upgrade. When you have started the device with the backup loader, you can either set RouterOS toforce backup loaderin the RouterBOARD settings or have a chance to reinstall the failed RouterBOOT from a ".fwf" file (total of3 seconds)
* Resetting the RouterOS configurationHold this button until the LED light starts flashing, and release the button to reset RouterOS configuration to default.
* Enabling CAPs modeTo connect this device to a wireless network managed by CAPsMAN, keep holding the button for 5 more seconds, LED turns solid, release now to turn on CAPs mode. It is also possible to enable CAPs mode via the command line, to do so run the command"/system reset-configuration caps-mode=yes";
* Starting the RouterBOARD in Netinstall modeOr keep holding the button for 5 more seconds until the LED turns off, then release it to make the RouterBOARD look for Netinstall servers. You can also simply keep the button pressed until the device shows up in the Netinstall program on Windows.
# How to reset configuration
1) Unplug the device from power;
2) Press and hold the button right after applying power;
Note: hold the button until the LED will start flashing;
3) Release the button to clear the configuration;
# Jumper hole reset
Older RouterBOARD models are also fitted with a reset jumper hole. Some devices might need an opening of the enclosure, RB750/RB951/RB751 have the jumper hole under one of the rubber feet of the enclosure.
Close the jumper with a metal screwdriver, and boot the board until the configuration is cleared:
## Jumper reset for older models
Thebelowimage shows the location of the Reset Jumper on older RouterBOARDs like RB133C:
## WPS
Some devices have WPS button, or reset button with WPS functionality to reach and control access for Wireless networks without logging into the device, so that client can connect without password. Specific models use WPS sync function to connect with each other. Detailed information on WPS and reset button functionality for each model are described inUser Manuals
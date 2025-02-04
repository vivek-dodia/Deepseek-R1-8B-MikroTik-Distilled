# Document Information
Title: Reset Button
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/24805498/Reset+Button,

# Content
# Introduction
The RouterOS password can only be reset by reinstalling the RouterOS or using the reset button (or jumper hole) in case the hardware is RouterBOARD. For X86(CHR) devices, only a complete reinstall will clear the password, along with any other configuration. For RouterBOARD devices, several methods exist, depending on the device model.
# Reset From RouterOS
If you still have access to your router and want to recover its default configuration, then you can:
# Using Reset Button
RouterBOARD devices are fitted with a reset button which has several functions:
# How to reset configuration
1) Unplug the device from power;
2) Press and hold the button right after applying power;
Note: hold the button until the LED will start flashing;
3) Release the button to clear the configuration;
# Jumper hole reset
Older RouterBOARD models are also fitted with a reset jumper hole. Some devices might need an opening of the enclosure, RB750/RB951/RB751 have the jumper hole under one of the rubber feet of the enclosure.
Close the jumper with a metal screwdriver, and boot the board until the configuration is cleared:
# Jumper reset for older models
Thebelowimage shows the location of the Reset Jumper on older RouterBOARDs like RB133C:
# WPS
Some devices have WPS button, or reset button with WPS functionality to reach and control access for Wireless networks without logging into the device, so that client can connect without password. Specific models use WPS sync function to connect with each other. Detailed information on WPS and reset button functionality for each model are described inUser Manuals
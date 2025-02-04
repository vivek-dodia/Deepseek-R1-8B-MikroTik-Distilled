# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 211316

# Discussion

## Initial Question
Author: [SOLVED]Sat Sep 28, 2024 10:41 pm
Use netinstall for 7.15.3 (or whichever ROS version you decide to start with). Don't mess with netinstalling v6, upgrading from v6 to v7 leaves (hidden) v6 setup on device which consumes (precious) space.When doing netinstall, select both routeros and wifi-qcom-ac packages in the same step, this avoids some possible gotchas later on (such as not applying default config for wifi).After you get into ROS after netinstall, don't forget to upgrade routerboot (the "BIOS" part) in /system/routerboot ...
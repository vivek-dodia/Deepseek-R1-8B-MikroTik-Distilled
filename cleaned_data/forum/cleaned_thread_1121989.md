# Thread Information
Title: Thread-1121989
Section: RouterOS
Thread ID: 1121989

# Discussion

## Initial Question
Hello All, Using ROS 7 for first time. I set ntp client and the router picks up the time. I set /sys clock time-zone-autodetect to Yes, but the time zone name stays at manual and the clock doesn't update. It's still at GMT.Am I missing something basic?Thanks! ---

## Response 1
Are you running the latest stable version (7.17, or 7.16.2)? e.g. Some devices come with older versions, and I want to say there was some bug someplace in TZ auto-detect and/or NTP in older versions.FWIW, Mikrotik has a build in time sync in /ip/cloud, so there is not a specific need to use your own NTP server to get time, unless you want to. But the defaults should get time/time-zone out-of-the-box. ---

## Response 2
Well, it's certainly not doing what it's supposed to be doing. I now have two RouterOS 7 devices - a Chateau LTE6 and a hAP AX3 - and both happily show me GMT time, even though TZ autodetect is set to yes. Th hAP AX3 is running 7.17 updated this morning. On the new hAP AX3 I did not set any NTP settings. It's straight out of the box and updated.Anybody have any ideas? ---
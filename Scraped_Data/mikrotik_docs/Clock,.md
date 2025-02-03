---
title: Clock
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/40992866/Clock,
crawled_date: 2025-02-02T21:12:35.809884
section: mikrotik_docs
type: documentation
---

# Introduction
RouterOS uses data from theTZ database, Most of the time zones from this database are included, and have the same names. Because local time on the router is used mostly for timestamping and time-dependent configuration, and not for historical date calculations, time zone information about past years is not included. Currently, only information starting from 2005 is included.
Following settings are available in the/system clockconsole path and in the "Time" tab of the "System > Clock" WinBox window.
Startup date and time isjan/02/1970 00:00:00[+|-]gmt-offset.
# Properties
Property | Description
----------------------
time(HH:MM:SS); | whereHH- hour 00..24,MM- minutes 00..59,SS- seconds 00..59).
date(mmm/DD/YYYY); | wheremmm- month, one ofjan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec,DD- date, 00..31,YYYY- year, 1970..2037):dateandtimeshow current local time on the router. These values can be adjusted using thesetcommand. Local time cannot, however, be exported, and is not stored with the rest of the configuration.
time-zone-name(manual, or name of time zone; default value:manual); | Name of the time zone. As most of the text values in RouterOS, this value is case sensitive. Special valuemanualappliesmanually configured GMT offset, which by default is00:00with no daylight saving time.
time-zone-autodetect(yesorno; default: yes); | Feature available from v6.27. If enabled, the time zone will be set automatically.
time(HH:MM:SS);
whereHH- hour 00..24,MM- minutes 00..59,SS- seconds 00..59).
Configuration
## Active time zone information
* dst-active(yesorno>; read-only property): This property has the valueyeswhile daylight saving time of the current time zone is active.
* gmt-offset([+|-]HH:MM- offset in hours and minutes; read-only property): This is the current value of GMT offset used by the system, after applying base time zone offset and active daylight saving time offset.
## Manual time zone configuration
These settings are available in/system clock manualconsole path and in the "Manual Time Zone" tab of the "System > Clock" WinBox window. These settings have an effect only whentime-zone-name=manual. It is only possible to manually configure single daylight saving time period.
* time-zone,dst-delta([+|-]HH:MM- time offset in hours and minutes, leading plus sign is optional; default value:+00:00) : While DST is not active use GMT offsettime-zone. While DST is active use GMT offsettime-zone+dst-delta.
* dst-start,dst-end(mmm/DD/YYYY HH:MM: SS- date and time, either date or time can be omitted in thesetcommand; default value:jan/01/1970 00:00:00): Local time when DST starts and ends.
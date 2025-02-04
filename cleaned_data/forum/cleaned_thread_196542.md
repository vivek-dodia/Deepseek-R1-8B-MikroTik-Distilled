# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 196542

# Discussion

## Initial Question
Author: Sun May 28, 2023 5:21 pm
``` :local Flag :set Flag [/user-manager session find where flags=""] :user-manager session print where flags="" :if([:len $Flag] > 0) do={/user-manager session remove $Flag} ``` Hey allI want to remove nonactive session in /user-manager session and I got this code so far but it's not working and I don't know how to get it right.
```
---
```

## Response 1
Author: Thu Nov 14, 2024 6:52 am
MikroTik script to clean up inactive User Manager sessions while preserving active connections.# Script to cleanup inactive User-Manager sessions# Add this script to your scheduler to run every 24 hours:local cleanupLog do={# Get current time for logging:local currentTime [/system clock get time]:local currentDate [/system clock get date]# Log start of cleanup process:log info "Starting User-Manager session cleanup at $currentTime on $currentDate"# Counter for removed sessions:local removedCount 0# Get all sessions without active flag:foreach session in=[/user-manager session find where active=no] do={# Remove the inactive session/user-manager session remove $session:set removedCount ($removedCount + 1)}# Log completion with count of removed sessions:log info "User-Manager session cleanup completed. Removed $removedCount inactive sessions"}# Execute the cleanup function$cleanupLog# Add this to scheduler using:# /system scheduler# add interval=24h name=userman-cleanup on-event="/system script run userman-cleanup" \# start-date=jan/01/2024 start-time=02:00:00This script does the following:1. Creates a function cleanupLog that:o Gets current time and date for logging purposeso Logs the start of the cleanup processo Counts removed sessionso Finds and removes all inactive sessionso Logs completion with the number of sessions removed2. Uses the RouterOS v7 user-manager commands to safely remove only inactive sessions3. Includes detailed logging for monitoring and troubleshooting4. Preserves all active sessions (those with the A flag)To implement this:1. Create a new system script:/system script add name=userman-cleanup source=<paste the script content>2. Add it to the scheduler to run every 24 hours (suggested at 2 AM):/system scheduler add interval=24h name=userman-cleanup on-event="/system script run userman-cleanup" start-date=jan/01/2024 start-time=02:00:003. You can also run it manually to test:/system script run userman-cleanupEnjoy.
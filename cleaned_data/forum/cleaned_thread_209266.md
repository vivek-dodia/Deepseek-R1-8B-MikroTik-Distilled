# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 209266

# Discussion

## Initial Question
Author: [SOLVED]Sat Jul 13, 2024 11:52 pm
``` { :local Result [/tool fetch url=https://ipconfig.io/json as-value output=user]; :if ( $Result->"status" = "finished" ) do={ :local Data [:deserialize from=json value=($Result->"data")]; :log info ("Your IP address is " . $Data->"ip"); :log info ("You are located in " . $Data->"country" . " (" . $Data->"country_iso" . ")"); }; } ``` Hey, I have been struggling to understand how to use the :deserialize and I got one good example of usage which I am sharing:
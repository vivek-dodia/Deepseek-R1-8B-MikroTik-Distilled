# Thread Information
Title: Thread-1114645
Section: RouterOS
Thread ID: 1114645

# Discussion

## Initial Question
Hi, Trying to defina an array to loop trafic type with kid-control feature in MKT 7.16but get confued with how to define array this is my code and know that Forum guru halped me a lot to get to this pointand i am really happy for his help again.This is my code:{:global abc [:toarray "youtube, google, amazon"]:foreach abuserid in=[/ip/kid-control/device/find activity ~"$abc" ] do={:do {:log info "Websites are $abc"/ip/firewall/address-list/add list=ABUSERSIP address=[/ip/kid-control/device/get $abuserid ip-address] timeout=1h#:log info "Abuser ID is $abuserid"} on-error { :log info "IP already added"}}}This example work to get type of traffic from kind-control "without the line : global abc [:toarray] and replacing $abc with "youtube"this way::global my_array [:to array "youtube, google, amazon"]other say:global abc {"youtube", "google","amazon"}there are many way suposedly but none work as expected:The intention is 1st loop check for activity youtube and save ip address to address list2nd loop check for activity google and add ip found to the address list3rd loop check for activity amazon and add to address listand so on ...the code above :global abc [:toarray "...} gives no error nor does the :log info ""Websites are ..." does not appearso the definition is wrong or i am doing something wrong.Running ROS 7.16Thank you ---

## Response 1
~ is for a regular expression, not an array...So you can use a string with a valid regex like::global abc "youtube|google|amazon" ---

## Response 2
~ is for a regular expression, not an array...So you can use a string with a valid regex like::global abc "youtube|google|amazon"You solve everything with such an ease.Thank you ---
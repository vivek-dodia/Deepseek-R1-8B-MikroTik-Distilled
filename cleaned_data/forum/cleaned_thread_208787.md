# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 208787

# Discussion

## Initial Question
Author: [SOLVED]Thu Jun 27, 2024 2:27 pm
``` /ip dhcp-server lease :if ($leaseBound = 1 && [ get [ find where mac-address=$leaseActMAC ] dynamic ] = true) do={ :do { :tool fetch url="https://api.telegram.org/botXXXXX/sendMessage\?chat_id=XXXX&text=The following MAC address [$leaseActMAC] received an IP address [$leaseActIP] from the DHCP Server [$leaseServerName]" keep-result=no :log info "Sent DHCP alert for MAC $leaseActMAC" } on-error={:log error "Failed to send alert via Telegram"} } ``` Hi, I have a small script (can't recall from where I got it to be honest), but seems that after one of latest upgrades it stopped working:
```
can you please help me fix it ? I know that issue is with "if" loop, but I can't figure out what exactly.
```
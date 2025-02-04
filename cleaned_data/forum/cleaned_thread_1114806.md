# Thread Information
Title: Thread-1114806
Section: RouterOS
Thread ID: 1114806

# Discussion

## Initial Question
Hi, I'm trying to access the WiFi scan capability via the REST API.Below is the CLI command I'm trying to access which conducts a scan and prints the detected SSIDs etc to the terminal. I'm trying to perform the same via REST API.[admin@MikroTik] > interface/wireless/scan wlan1Flags: A - ACTIVE; P - PRIVACYColumns: ADDRESS, SSID, CHANNEL, SIG, NF, SNRADDRESS SSID CHANNEL SIG NF SNR(output removed)I have successfully connected to the API but after a lot of research can't work out how to send this command to the API. I can send other commands such as:GET:http://ip/rest/interface/wirelesswhich prints wireless interface stats, but I can't seem to trigger a scan.I've triedhttp://ip/rest/interface/wireless/scanbut I get{"detail": "no such command","error": 400,"message": "Bad Request"}Has anyone got any ideas or managed to achieve this?Thank you ---

## Response 1
I think you need to pass the interface as an argument to the command. If the interface is enabled (I am using wlan1 for this example), this works for me on 7.17rc3 with device 4011:
```
curl-k-u admin:<password>-X POST https://<ip>/rest/interface/wireless/scan --data '{".id": "wlan1", "rounds": "1"}' -H "content-type: application/json"For CLI processing during debug, I actually run this to clean up the json response and make it a little more human readable:
```

```
curl-k-u admin:<password>-X POST https://<ip>/rest/interface/wireless/scan --data '{".id": "wlan1", "rounds": "1"}' -H "content-type: application/json" | jq "."

---
```
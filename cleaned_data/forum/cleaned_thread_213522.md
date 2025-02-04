# Thread Information
Title: Thread-213522
Section: RouterOS
Thread ID: 213522

# Discussion

## Initial Question
I have a network with a Wireless Wire Cube Pro that's working flawlessly, except for some curious ssh behavior. During setup nothing in the configuration was changed except the admin login password. Factory configuration worked without modification.In the device's log, viewed with WinBox 3.41, I see many failed attempts to login via sshfrom the device's own IP addresses. For example, the device in question has IP addresses 192.168.0.250 and 192.168.88.2, and I see:
```
login failure for user admin from 192.168.0.250 via winbox
login failure for user admin from 192.168.88.2 via winboxrepeating at somewhat random intervals approximating once a minute.  I see similar log messages on the other device (IP 192.168.0.251 and 192.168.88.3) as wellClearly there's some background process running on the devices that didn't get the message about the password changing.What do I need to fix here?

---
```

## Response 1
I think this is a case of "Never mind..." (as immortalized by Miss Emily Litella)I traced this to the Dude, who seems to have portscanned the entire network and is now probing everything he could find. ---

## Response 2
What ranges are you getting and speeds, and how does it hold up with heavy rain or snow??Is the 5ghz backup good, what range?? ---
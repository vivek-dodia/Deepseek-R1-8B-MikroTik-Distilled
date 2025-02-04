# Thread Information
Title: Thread-1122958
Section: RouterOS
Thread ID: 1122958

# Discussion

## Initial Question
Not totally true. I only receive sms messages if I "set receive-enabled=n ; set receive-enabled=y "If I just have "receive-enabled=y" nothing happens when a new message is sent to it's phone #. Only when I turn it off then back on do I receive pending messages.Anyone else with this issue or have a fix??Running: 6.44.3 ---

## Response 1
Thank you for your post. I have the exact same issue with the Chateau LTE6 ax. For me, disabling and then re-enabling SMS reception also results in receiving messages. Unfortunately, I don't believe anyone from MikroTik reads this forum or cares about software bugs. ---

## Response 2
I use this on my SXT LTE6 DeviceThis is how I have got round it.1/ Create System Script to Disable then Re-enable the SMS Receiving2/ Setup Schedule (SMS-Reset) to run at boot and subsequently every 5 mins thereafter
```
/system scriptadddont-require-permissions=noname=sms-reset owner=admin policy=\
ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="#\ this is required to receive SMS messages as bug found\r\
\n/tool sms set receive-enabled=no port=lte1 \r\
\n:delay 2s\r\
\n/tool sms set receive-enabled=yes port=lte1 secret=MySecret\r\
\n:delay 2s\r\
\n"
```

```
/system scheduleraddinterval=5mname=SMS-Reseton-event=sms-reset policy=\
ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
start-time=startupNot ideal, but it works.

---
```

## Response 3
The error still persists, RB will not accept sms. A simple script to scheduler for 10sec is enough
```
/tool smssetreceive-enabled=no:delay2s/tool smssetreceive-enabled=yes

---
```

## Response 4
Did anyone contact support about it ? ---

## Response 5
Tried to update the device(firmware) to newer version ?Seeing running: 6.44.3.Sorry don't know if @esj and @Świętopełek running the latest version and also hitting this fault.Also with LTE devices, are you running the latest version of firmware in the modem ? ---

## Response 6
Morning. I am on the latestmipsbeSXTR7.17 (stable)2025-01-16 08:19:287.11.2Modem 16121.1034.00.01.01.08My SMS is working FWIW ---
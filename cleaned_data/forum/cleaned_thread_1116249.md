# Thread Information
Title: Thread-1116249
Section: RouterOS
Thread ID: 1116249

# Discussion

## Initial Question
please i need help on how to write a script that will reset all couter of hotspot uptime limit. can anyone help me? please this is urgent. i am using RB1000, v3.6.Kenny ---

## Response 1
Please be more detailed in your request. ---

## Response 2
I have to reset the couter for all user of the hotspot in my organization morning. each user have a time limit of 3 hours per day on the hotspot. I want to know the script that resets this couter for all the users every morning.i hope this helps ---

## Response 3
```
/ip hotsport user reset-countersto reset counters for all users.To schedule this to run every day one minute before midnight:
```

```
/system scheduler add name="reset counters" start-date=jan/1/2009 start-time=23:59:00 interval=24h on-event="/ip hotspot user reset-counter"

---
```

## Response 4
im trying this but not working for me :S plz helpI need to reset all counters when i switch of routerboard ---

## Response 5
How is it not working? What have you tried? What are you expecting it to do, and what is it doing instead?It's a built in command. "It doesn't work" as the only statement from you makes it kind of hard to help you. Give more details. ---

## Response 6
How is it not working? What have you tried? What are you expecting it to do, and what is it doing instead?It's a built in command. "It doesn't work" as the only statement from you makes it kind of hard to help you. Give more details.Workedi forgot to set a mikrotik year. thank you ---

## Response 7
im trying this but not working for me :S plz helpI need to reset all counters when i switch of routerboardhiplease check router and your system date&time ---
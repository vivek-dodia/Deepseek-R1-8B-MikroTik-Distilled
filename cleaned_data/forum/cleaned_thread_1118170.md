# Thread Information
Title: Thread-1118170
Section: RouterOS
Thread ID: 1118170

# Discussion

## Initial Question
Hello, i use some CHR routers for experimenting new features in router os V7especially Cake and wireguardI have few CHR routers that will expire soon!what happens when the 60 days is expired, will it revert back and be throttled on 1mbps, or it will be normal and simply wont get new routeros versions!i read in the documentation, and I could not get a clear idea!especially when I read this :License UpdateIn '/system license' menu router will indicate the time next-renewal-at when it will attempt to contact server located on licence.mikrotik.com. Communication attempts will be performed once an hour after the date on next-renewal-at and will not cease until the server responds with an error. If deadline-at date is reached without successfully contacting the account server, the router will consider that license has expired and will disallow further software updates.However, router will continue to work with the same license tier as before.i d appreciate it if you could tell me how sure you are about the answer you give me! ---

## Response 1
You will fallback to free:The free license level allows CHR to run indefinitely. It is limited to 1Mbps upload per interface. All the rest of the features provided by CHR are available without restrictions. To use this, all you have to do is download the disk image file from our download page and create a virtual guest.60-day trialIn addition to the limited Free installation, you can also test the increased speed of P1/P10/PU licenses with a 60 trial.You will have to have an account registered on MikroTik.com. Then you can request the desired license level for trial from your router that will assign your router ID to your account and enable the purchase of the license from your account. All the paid license equivalents are available for trial.A trial period is 60 days from the day of acquisition after this time passes, your license menu will start to show "Limited upgrades", which means that RouterOS can no longer be upgraded.If you plan to purchase the selected license, you must do it within 60 days of the trial end date. If your trial ends, and there are no purchases within 2 months after it ended, the device will no longer appear in your MikroTik account.You will have to make a new CHR installation to make a purchase within the required time frame.After 120 days in total you can't upgrade RouterOS anymore and the best is to create a new Free config.https://help.mikrotik.com/docs/pages/vi ... d=18350234ps. why the big letters. If can read the small ones you don't have to make some, bigger. ---

## Response 2
After 120 days in total you can't upgrade RouterOS anymore and the best is to create a new Free config.I don't understand this step. What do you mean " create a new free config " .. a new CHR installation in VM ? ---

## Response 3
That is not true and topic is incorrectly marked as solvedIf you request a trial of the P1, P10 or PU license, it works with all features for 60 days, but after 60 days, RouterOS upgrade gets disabled. Limits do not get applied, it continues to work with no speed limit.You will fallback to freeThis is not mentioned in your own quoted documentation text, it does not happen. ---

## Response 4
That is not true and topic is incorrectly marked as solvedWHAT is not true?The help page:https://help.mikrotik.com/docs/spaces/R ... Router+CHRFree licensesThere are several options to use and try CHR free of charge.freeThe free license level allows CHR to run indefinitely. It is limited to 1Mbps upload per interface. All the rest of the features provided by CHR are available without restrictions. To use this, all you have to do is download the disk image file from our download page and create a virtual guest.60-day trialIn addition to the limited Free installation, you can also test the increased speed of P1/P10/PU licenses with a 60 trial.You will have to have an account registered on MikroTik.com. Then you can request the desired license level for trial from your router that will assign your router ID to your account and enable the purchase of the license from your account. All the paid license equivalents are available for trial. A trial period is 60 days from the day of acquisition after this time passes, your license menu will start to show "Limited upgrades", which means that RouterOS can no longer be upgraded.If you plan to purchase the selected license, you should do it within 60 days of the trial end date. If your trial ends, and there are no purchases within 2 months after it ended, the device will no longer appear in your MikroTik account. You will have to make a new CHR installation to make a purchase within the required time frame.it seems to meverysimilar to the msatter's post marked as "solved". ---

## Response 5
WHAT is not true?normis made it quite clear what was not true. His comment also contains the answer to OPs question: "what happens when CHR 60 days trial is expired!" ---

## Response 6
That is not true and topic is incorrectly marked as solvedIf you request a trial of the P1, P10 or PU license, it works with all features for 60 days, but after 60 days, RouterOS upgrade gets disabled. Limits do not get applied, it continues to work with no speed limit.So, to clarify, once the trial window has passed, the CHR continues to function as-is, except you won't be able to upgrade the OS version. That's it? ---

## Response 7
Simple reply to OP post: Unable to upgrade/update, and nothing else. ---
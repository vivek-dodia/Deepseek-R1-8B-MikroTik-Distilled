# Thread Information
Title: Thread-1119921
Section: RouterOS
Thread ID: 1119921

# Discussion

## Initial Question
Hi there, I've using the SMB feature for the last few years. It worked nicely and never had an issue. RouterOS introduced the latest SMB version in 7.14. So I updated the RouterOS version to 7.16.2. Since my new Mac Mini is not performing well with the older version of SMB.Now the SMB keeps unmounting after exactly 30 secs on Mac (Finder). and on Windows, it renews the connection every 30 seconds.I can see the Mikrotik logs report (screenshot):Screenshot 2024-12-27 at 3.14.03 AM.pngPlease investigate this matter and fix it.Thanks. ---

## Response 1
I've just updated 7.14.2 -> 7.16.2 and am having the same SMB problem now... ---

## Response 2
Now the SMB keeps unmounting after exactly 30 secs on Mac (Finder). and on Windows, it renews the connection every 30 seconds.I can see the Mikrotik logs report (screenshot):Are you connecting to SMB share via cable? Because I've noticed that via cable SMB shares works as intended, only when I mount SMB share on my Mac using Wi-Fi I get these disconnects.Will try to downgrade to 7.14.2. ---

## Response 3
After downgrading to 7.14.3 I get no disconnects using Wi-Fi with Intel Mac Pro 2019, so SMB connection to the router's USB disk is solid, can watch videos without any disconnects where as 7.16.2 kept disconnecting after like less than a minute. ---
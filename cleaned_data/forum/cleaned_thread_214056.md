# Thread Information
Title: Thread-214056
Section: RouterOS
Thread ID: 214056

# Discussion

## Initial Question
Hi, I'd love to try the Back to Home Feature. Therefore, I downloaded the app, entered my router IP (10.0.0.1) and my admin credentials - but after some seconds I get an error "connection refused".Mikrotik: CRS326-24G-2S+Version 7.17 (stable)Mobile Phone: iPhone 16 proBack to Home App Version: 0.9I can log in to the admin ui via the browser on my phone, so the connection should be possible.I can not see the attempt in the router logs.How could I debug this further? ---

## Response 1
Is the Mikrotik device acting as a router or a switch??How did you create the BTH VPN in the first place.Ensure you have access to the input chain for the IP address of your phone when connecting from the trusted WLAN. ---

## Response 2
I use RouterOS.I haven’t created a VPN or changed any other settings because, according to the wiki, that shouldn’t be necessary.Since I can access the web interface via the IP address on my phone using a browser, I would have assumed that the app should also have the appropriate access. ---

## Response 3
To create the Back to Home VPN tunnel, you have to connec to your home router's WiFi network from inside your house, then open the BTH app, provide the router login and password and follow the steps in the app. It will open up the access to your device during this process. Only after that you can access your router from other locations via this app. ---

## Response 4
To create the Back to Home VPN tunnel, you have to connec to your home router's WiFi network from inside your house, then open the BTH app, provide the router login and password and follow the steps in the app. It will open up the access to your device during this process. Only after that you can access your router from other locations via this app.Thanks for the help - i am inside my wifi an can connect to the admin ui via the browser, so i‘d think that the app should have access as well ---
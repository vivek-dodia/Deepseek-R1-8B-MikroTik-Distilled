# Thread Information
Title: Thread-213784
Section: RouterOS
Thread ID: 213784

# Discussion

## Initial Question
Hello, Anyone else nervous about MikroTik future with routers / firewall appliances. Yes, "route the world", but we've been begging and asking for USEFUL features and MikroTik keeps falling short... Such as... ROSE..... why?!Look -- UBT just released Unif Networks 9.0.. [https://blog.ui.com/article/unifi-netwo ... t-to-scale]When will MikroTik even support the free SNORT community service [IPS/IDS]... cambium is doing it with their NSE products.Yes, I understand we most likely have outgrown MikroTik for some of our deployments and customer needs. There will always be a place and use-case for MikroTik hardware or routers given their flexibility, but we need better usability within the software. ---

## Response 1
You can already use Snort with ROS. But how were you thinking of implementing IPS/IDS with Snort when almost all traffic is encrypted these days? ---

## Response 2
Yeah nervous that some giant Chinese company will buy MT out and start adding all those nifty features you desire, and of course a hidden back door to the red army. ---

## Response 3
Look -- UBT just released Unif Networks 9.0.. [https://blog.ui.com/article/unifi-netwo ... t-to-scale]U mean UBNT who have finally (after almost 10 years) added firewall zones and broke their promise of "license free"Don't get me wrong I don't hate on them but I also just don't get the hype about their services that (from my own experience till 2022 ) are subpar.Yes they used to fit the price but UBNT also has tripled in price recently!Compare old AP+FW with new AP+FW.To add: IPS/IDS without SSL decrypt is nothing more than IP Blocking.Thankfully UBNT added SSL decrypt after a few years.With our fortigates we run both Fortiguard and a secondary IDS.Let's not talk about UBNT Site magicEdit: "basic" routing is still needed nowadays.Customer of mine used to be running a sophos + router as VPN GW.Now switching out some FWs for UBNT but still a has to keep routers since the VPN performance is "less than optimal" ---

## Response 4
I will not use UBT products, however it is nice to see them finally releasing needful features. It would be nice to see MikroTik also do the same......We also use Fortigates and the SSL decrypt, etc.Camibum NSE is also soon to be doing auto-VPN to other NSE appliances [Same as Meraki Auto-VPN]. ---
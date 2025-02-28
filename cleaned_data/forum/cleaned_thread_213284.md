# Thread Information
Title: Thread-213284
Section: RouterOS
Thread ID: 213284

# Discussion

## Initial Question
I've been retired five years and I'm a little rusty, so be kind.Working on a project where I needed to arrange for Winbox (computer) and MT app (iPhone) access to a dumb wireless pass-through bridge (a wireless station, but I mean it doesn't route) that couldn't be reached by other means. I need to do it from time to time to add/remove entries in the wireless connect-list and security-profiles tables. Thought I might add a virtual AP to the radio through which I could use Winbox on it to do this. My early attempts failed, with "failed to establish secure connection" from the iPhone MT app.So I broke the problem down to basics: Winbox over Ethernet can access a MikroTik that has no configuration at all... but how minimal a configuration can you add to a wireless MikroTik in order to have wireless Winbox access?I grabbed a lab router and came up with the configuration below, and then I made a discovery: it works absolutely fine for Winbox running on a computer, but the MT iPhone app hangs for a while and then just gives up with no message. So apparently the app has additional requirements that real Winbox does not. Does anybody know what I would have to add to this configuration to make the iPhone app happy enough to log in properly?
```
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
add authentication-types=wpa2-psk mode=dynamic-keys name=MaintOwn supplicant-identity=""
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-g/n country=no_country_set disabled=no mode=ap-bridge \
    radio-name="Liberty Maint" security-profile=MaintOwn ssid="Liberty Maint" wps-mode=disabled
/ip pool
add name=MaintPool ranges=192.168.100.2/31
/ip dhcp-server
add address-pool=MaintPool interface=wlan1 name=MaintDHCP
/ip address
add address=192.168.100.1/24 interface=wlan1 network=192.168.100.0
/system note
set show-at-login=no

---
```

## Response 1
I remember the cactus LOL1. If remote ( not behind the router safely on the LAN ) you need a wireguard connection.a. manual setup --> standard wireguard app ( smartphone, or laptop )b. BTH setup --> need BTH APP on smartphhone and wireguard app on laptop.2. Mikrotik FULL APP, not the home app version.3. Connect first using wireguard, then run the MIKROTIK full app (smartphone), winbox if on laptop. ---

## Response 2
I gather Wireguard is a later version of the sort of thing we used to do with creating an L2TP login. But I'm not remote (it's a mobile router and I'm just feet away), and it can't even get onto the Internet before I've completed this massaging at each new location, so I don't believe it's a solution to my problem. I also can't reach it with Winbox/MT app from the LAN side (I did try) because it's behind a non-MT router that NATs. So my approach was to reach it directly through a virtual "maintenance AP" on its own radio... and it turned out to work perfectly with Winbox from my laptop, but not the iPhone MT app.The app I'm using is this one.I see two others officially "by Mikrotik" in the App Store -- MT Back to Home, and MT Beacon Manager, which seems to be for inventory tags. So I think I have the "pro model" app right?(UPDATE: And now the plot thickens, then clears!)In the process of grabbing the icon from the App Store for the above paragraph, I noticed the App Store was offering to download it to my laptop for me, even though it was an iPhone app. Then I remembered reading that the Apple Silicon laptops had the capability of running iPhone and iPad apps natively, though I had never before taken advantage of this. So I downloaded it for kicks, and what do you know -- the MT iPhone app talks to this router just fine when used from my laptop, but still not from my iPhone!So I figured the problem must be due to some detail of the iPhone wireless connection. All the obfuscations (private address, limit tracking, low data mode) were already disabled. I noticed that the Router IP field in the IPV4 section was blank, and verified the same behavior on my laptop, yet it doesn't seem to bother the laptop. I realized that I hadn't created a DHCP Networks entry, so I did that. The Router field appeared on the phone, but the app still didn't work. Noticing the DNS was also blank, I then created a tiny static DNS with just the router's own name and ID in it, just to fill in that field... and the app started working!Apparently, the MT app on the iPhone requires both those fields to be present (if either one is missing, it fails), whereas their lack doesn't seem to bother the app running on an Apple Silicon laptop.Thanks for your help. I thought I'd leave the answer here to help other people who may see a similar problem. ---

## Response 3
When you connect to the routers Wi-Fi on iPhone, and using the router's IP address is that what is not does not working?Or... is it the neighbors view that's not working?Also, you do NOT have /ip/dhcp-server/network... So check if you're getting a valid IP address on the iPhone in the same subnet.... I suspect you may be getting 0.0.0.0 address... ---

## Response 4
Prior to solving my problem, I was connecting to the SSID from the iPhone, and getting a valid IP address and netmask (but not a Router or DNS value). MT app would happily "discover" router (same as neighbor mechanism, I guess) but refused to log in with correct name and password, instead hanging for some time and then returning, saying either nothing or that it was unable to set up a secure connection. Providing the two missing values made the app work. ---

## Response 5
The mobile winbox does not have any other requirements, but what you describe usually happens if there is a network loop or an IP address conflict somewhere. ---
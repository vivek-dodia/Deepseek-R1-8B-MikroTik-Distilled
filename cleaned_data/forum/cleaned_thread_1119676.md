# Thread Information
Title: Thread-1119676
Section: RouterOS
Thread ID: 1119676

# Discussion

## Initial Question
RouterOS 7.14 and 7.14.1:I created roadwarrior wireguard peer config.I use IPv4 and IPv6, and a shared secret(PSK).The config file is thus a bit largerthan plain vanilla IPv4-only, thus the QR code blob is also bigger than the minimum sized one.The PSK and keys were generated on a Linux box with:
```
# Create Preshared Key (RouterOS 7.14.1 has 'preshared-key=auto' available)
> wg genpsk
KH8nrvx0cuczwE3R56qH5/vyLyHAEBv0QwogCA50ZjU=

# Create keys, first is the private key, then the public key
> wg genkey | tee /dev/tty | wg pubkey
+PENj+zzPfIsTmc35JMPqCEfNzJD56ecPgh8C+ol8GE=
7+C0DcBwtIozJXrZ7tjIbDRbtfgwRVnC/MPBmwe3Rms=RouterOS Winbox (3.40 64bit) client-config screen has several bugs, the WG-client config screen, including the data on the WG-client-.QR code, and the WG-client-QR code usability itself. I sent these to Mikrotik Support, and they just said "if there will be more, similar requests like yours, we will see how this can be added in future versions". Well, I sent seven (7) bug reports, and one (1) feature suggestion. I haven't heard back when I asked if those 7 bugs are now getting some attention and TLC.The QR code that is produced by ROS, is very big, and with Winbox, the full QR code does not fit into the QR code window. Please make the QR code a bit smaller (or the QR code window larger) so it fits the QR-code winbox window fully. The QR code can now only be scrolled wit the scroll bar, but that does not allow user to scan/copy the QR code into a phone WG peer config. (I attached a snipping to show the bug)I tried to see the QR code with winbox/terminal, "/interface/wireguard/peers/show-client-config 0", and the QR code is still too big to fit to any winbox terminal window. The resulted physical font of the QR code is again way too big.  That is a font issue, but also means QR code is hard to use.I tried to export the peer config and peer-QR-code into a file. The QR code is NOT exported to the file:"show-client-config 0 file=20240307-hemmo-wg-client-x20.txt" creates a file with the ASCII WG-client config, but the QR code is NOT in that file. That created config is wrong/broken, see next item.I had a working peer (peer 0). I copied that one (with winbox) and entered new public/private keys, new PSK, and new IPv4 and IPv6 addresses. The created client text configuration wrong (I had picture attahed). The QR code config is also equally wrong.  In Command Line, the actual Mikrotik side device configuration is ok, but the generated client-config screen is with wrong IPv4 address (192.168.177.X), with wrong mask (/24), without any client IPv6 addressing wrong . (Picture was attached)I created a brand new peer, as a second peer to a working Wireguard config. The installation goes as supposed, and the Mikrotik side config is correct. Now again looking at the "client config" text box, it is missing whole of the IPv6 address, the IPv4 is 192.168.177.X  addresses (which I had never used), the "client endpoint" (with :port ) gets :port:port , eg port repeated twice. And the generated QR code is equally broken with that same broken client config.Could you make the Winbox/Wireguard "client config" textWinbox window allowed to be copied to clipboard. Now you can see the config, but not copy it. The terminal/CLI screen  allows copy fine, but Winbox needs to allow that too in the GUI.When  doing winbox/terminal: "/interface/wireguard/peers> show-client-config 1", the output text config is indented with 4 spaces. For easier copy-paste experience, could you take that extra indentation out?The above 7 were bug reports.And then there was one feature request. Wireguard clients are easy to configure with the QR code, thus this is likely the best way to send configurations to a (remote) user. Getting the QR-code in PNG format, makes life a lot easier. So far, I created the WG-client configs manually, created a QR code (pink QR for girls), and had to jump many hoops to get there. Mikrotik could do all of that. So I asked this feature request:If possible, please allow the export of the QR code to a PNG file (or what is easiest for you). Now the ASCII QR-codes are very big, and to offer those to a non-computer-savy end user, leads the user not to be able to scan the ASCII QR-code.

---
```

## Response 1
QR code is fine for me. Maybe you need better screen resolution?You can also copy/paste the Client Config above the QR code to a text file of your choosing.OR you could take a screenshot of the QR Code and save to wherever you wantScreenshot 2024-03-14 130030.png ---

## Response 2
There is a bag actually.Client config and the QR code AllowedIPs are not match the Allowed Addresses from above.So the routes are wrong. ---

## Response 3
QR code is fine for me. Maybe you need better screen resolution?You can also copy/paste the Client Config above the QR code to a text file of your choosing.OR you could take a screenshot of the QR Code and save to wherever you wantAgain, with IPv6-addressing, and PSK, the QR-code does NOT fit in the QR-code window. Yes, I can copy it in two parts, stitch it, nice! Not good.Copy-paste client config from Winbox GUI configuration window, good luck. Have you even tried that yourself? Did you read what the client-config says, did you read how it does not work? No?And from your "working config", you can see how the Client-IPv4-address is 192.168.177.2/24. That is not your client config address, no.There were close to 10 issues there, listed there, so unless you understand how wireguard really works, it is not too helpful to copy buggy client configurations, and claim they work.There is also another bug in client-config: When a road warrior client config is suggested, it lists "[Interface] Listen Port=51820", even when "Client Listen Port" entry is emtpy. Roadwarriors do not usually want to listen to any port on their client device. ---

## Response 4
I see the same issues... sort of.The first time I saw QR in winbox it was (visually) good.Now I see in GUI an ASCI-version, way too big, and painted-QR in console, not selectable and not copyable.But yes: ListenPort is messed, address, allowed IPs... In short, only public key seems correct. ---

## Response 5
Hello, I have note this screen with my routerhow you can get this QR on winbox?I've use show client config, but the QR code genereted is bigger than the screen and don't accept to copy past it.QR code is fine for me. Maybe you need better screen resolution?You can also copy/paste the Client Config above the QR code to a text file of your choosing.OR you could take a screenshot of the QR Code and save to wherever you wantScreenshot 2024-03-14 130030.png ---
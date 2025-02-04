# Thread Information
Title: Thread-1114165
Section: RouterOS
Thread ID: 1114165

# Discussion

## Initial Question
Hello guys, I m gettting crazy currently.I have an working setup for hotspot. https is working and the rest also. But for wired devices - connected to interface 8 on hotspot bridge I cant get advertisment to work. I can access the dns via https, but not auto connection.routerboard: yesmodel: RB5009UPr+S+firmware-type: 70x0factory-firmware: 7.14current-firmware: 7.16.2upgrade-firmware: 7.16.2Any idea? ---

## Response 1
Okay. Can someone give me an idiot reward?The issue was that Windows 11 Client first makes an DNS lookup and after that somehow goes into redirect to hotspot. But because I was testing in an enviroment without uplink (dont ask), dns request didnt work. So I created a static a record for the public testing webseite and now I m getting redirects to hotspotportal page... ---

## Response 2
perfect. you can mark the post as solved. ---
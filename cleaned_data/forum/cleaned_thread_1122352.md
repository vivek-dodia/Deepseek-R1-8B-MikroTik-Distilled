# Thread Information
Title: Thread-1122352
Section: RouterOS
Thread ID: 1122352

# Discussion

## Initial Question
Hello, I have vpn ip 45.66.88.1 and i have two gatways 192.168.1.1 and 192.168.2.1The question is how can i make the public ip of the vpn works in two for exampleIp route add dst-address 45.66.88.1 gateway 192.168.1.1I cant do this second oneIp route add dst-address 45.66.88.1 gateway 192.168.2.1Because i already added the public on first gateway!Is there any vrf of any thing else can make my situation works? ---

## Response 1
policy routing if you want to use both routes at the same timehttps://help.mikrotik.com/docs/spaces/R ... cy+Routingor more simply set priority:ip ro add dst-address 45.66.88.1 gateway 192.168.1.1 distance=1ip ro add dst-address 45.66.88.1 gateway 192.168.2.1 distance=2 ---

## Response 2
policy routing if you want to use both routes at the same timehttps://help.mikrotik.com/docs/spaces/R ... cy+Routingor more simply set priority:ip ro add dst-address 45.66.88.1 gateway 192.168.1.1 distance=1ip ro add dst-address 45.66.88.1 gateway 192.168.2.1 distance=2Thanks for replay.Actually i dont have any default route so i dont have a ping on the ip i need make the ping in both ---
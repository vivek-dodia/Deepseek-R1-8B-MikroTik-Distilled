# Thread Information
Title: Thread-1118260
Section: RouterOS
Thread ID: 1118260

# Discussion

## Initial Question
Dear all, I've recently been testing the new "Push Routes" option in the OpenVPN server and thought I'd share some experience which might help others doing the same about what works and what does not. The Wiki help is pretty light on available information.The format of the string as noted by the winbox error if you enter it wrong is given as follows ...<network/IP><space><netmask><space><gateway><space><metric>You can enter multiple routes, by separating them with a comma.Now for the problems ...The latest OpenVPN client will only allow one of two things in the gateway being sent to it by the server, either the text "vpn_gateway" or the text "net_gateway" and therefore you cannot send an IP address to the client in the <gateway> field as this is just rejected. However the problem at the Mikrotik end is that the software only allows an IP address. This means that it is impossible to send a gateway from the server to the client until Mikrotik supports sending "vpn_gateway" or "net_gateway" then it's impossible to get a gateway through. On the same topic, because you cannot get a gateway through, you cannot get a metric through.The solution therefore is to only include the following in the route message ...<network/IP><space><netmask>This is accepted by the client and loads the route in with the gateway IP of the IP for the server end of the OpenVPN link so effectively routes the traffic back to the Mikrotik OpenVPN device to which it is connected.Not ideal, but a partially working solution until an alternative is found, all logged with support. ---

## Response 1
thanks for your opinions. even in the latest versions of ovpn when you specify the route it no longer accepts the gateway but the route is specified like this:
```
route192.168.20.0255.255.255.0

---
```

## Response 2
Dear all, I've recently been testing the new "Push Routes" option in the OpenVPN server and thought I'd share some experience which might help others doing the same about what works and what does not. The Wiki help is pretty light on available information.The format of the string as noted by the winbox error if you enter it wrong is given as follows ...<network/IP><space><netmask><space><gateway><space><metric>You can enter multiple routes, by separating them with a comma.Now for the problems ...The latest OpenVPN client will only allow one of two things in the gateway being sent to it by the server, either the text "vpn_gateway" or the text "net_gateway" and therefore you cannot send an IP address to the client in the <gateway> field as this is just rejected. However the problem at the Mikrotik end is that the software only allows an IP address. This means that it is impossible to send a gateway from the server to the client until Mikrotik supports sending "vpn_gateway" or "net_gateway" then it's impossible to get a gateway through. On the same topic, because you cannot get a gateway through, you cannot get a metric through.The solution therefore is to only include the following in the route message ...<network/IP><space><netmask>This is accepted by the client and loads the route in with the gateway IP of the IP for the server end of the OpenVPN link so effectively routes the traffic back to the Mikrotik OpenVPN device to which it is connected.Not ideal, but a partially working solution until an alternative is found, all logged with support.your client is windows? because i try on my chr push route not running and cannot push default route ---
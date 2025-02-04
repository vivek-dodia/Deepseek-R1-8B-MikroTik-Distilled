# Thread Information
Title: Thread-1118175
Section: RouterOS
Thread ID: 1118175

# Discussion

## Initial Question
In a remote management setting, is there an easy way to reliably find out which ethernet/sfp interface of one RouterOS device is physically connected to what ethernet/sfp interface on another RouterOS device? With all interfaces being part of a single bridge on each device. ---

## Response 1
IP>Neighbours will show the CDP, LLDP & MNDP information received by device ports, adding the Interface Name column provides the port name on the other devices.If the device in question is not configured to send discovery information then Bridge>Hosts shows the source MAC addresses received by device ports which you can manually match to the other devices addresses. ---
# Thread Information
Title: Thread-1116885
Section: RouterOS
Thread ID: 1116885

# Discussion

## Initial Question
Having some issue with firewall rule that supposed to open to port 2000 but from our main company router (mikrotik) its not communication with the client router? Any idea's that can lead me into punching that hole (figuratively) through the firewall so it can communicate with the client router so we can run the bandwidth test.Is there someone that has documentation as to how to setup this BT Server so I can test this out on client routers? ---

## Response 1
I too can't find any documentation on opening firewall ports but looking through the packet captures and sniffers and the initial btest starts with a TCP connection to port 2000 of the btest server. If the btest is using TCP for the test, everything should work as-is.If you're testing using UDP, I believe that this is what happens...After the initial TCP connection is established, and UDP is selected as the testing protocol, the server will tell the client to connect on a port higher then the one you specify in the Tools->BTest Server->Allocate UDP Ports From "XXXX", defaults to 2000. We'll just use port 2000 for this instance.The client will connect to the server on port 2000 using UDP to start a SEND speed test. If the client requests a RECEIVE speed test, the server connects back to the client on the source port that it used to make initial UDP connect to the server's port 2000. This port on the client seems to be between 2200-2300, but as I was testing further, the client started to use ports higher then 2300 and I keep needing to widen the UDP port allow range to allow the server to send data to the client.I'm now suspecting that to make UDP work, the firewall needs to be pretty permissive from 2000 through 64000.Hope that helps.-bdk ---

## Response 2
@Mikrotik: I just tried to setup a BTest Server hosted publicly and it's quite cumbersome to configure the firewalls of BOTH client and server, due to the unconventional approach outlinted by bdk above.If BTest is a client-server model, I do not expect that the server connects back to the client. This should all be outlined in the docs. (Behavior, directions of connections, used ports, difference in send/receive).I was also surprised at how much CPU BTest uses (at least in TCP mode; haven't tested UDP) - it's not really possible to test the actual speed/bandwidth of a router/device.It'd be nice if Mikrotik supports iperf. ---
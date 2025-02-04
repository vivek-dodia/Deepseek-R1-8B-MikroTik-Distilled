# Thread Information
Title: Thread-1123159
Section: RouterOS
Thread ID: 1123159

# Discussion

## Initial Question
Hi, when I set more than 8 RTSP service ports, because the customer has more than 8 webcam streams, the state changes to "invalid". Also the RTSP helper is no longer working. I am talking about "/ip firewall service-port set rtsp ports=....".Is there any way to have more ports?Thanksdksoft ---

## Response 1
If I am understanding your question, you are setting up the RTSP streams incorrectly in the router. The IP > Firewall > Service ports is services provided by the router itself. Webcam streams are not provided by the router, but rather by the camera. Should be NAT forwarding. ---

## Response 2
Sure, there is a NAT forwarding from a separate port to each webcam on the remote router before the cameras.
```
/ip firewall nataddaction=dst-nat chain=dstnat comment="Webcams Reolink"dst-port=8060in-interface-list=WAN protocol=tcp to-addresses=10.3.0.60to-ports=554But, as you might known, RTSP causes the same problem as FTP to be recognized by the statefull firewall as RTSP changes ports after the initial connection is setup. Therefore a helper is needed on the local router so that the firewall recognizes the ports to track that connection.
```

```
/ip firewall service-portsetrtsp disabled=noports=554,8060,8061,8062,8063,8064,8065,8066The problem is, that only 8 ports of the RTSP helper can be defined. I need more.Here you can see the problem:
```

```
/ip firewall service-portsetrtsp disabled=noports=554,8060,8061,8062,8063,8064,8065,8066,8067valueofports should havenomore than8elements

---
```

## Response 3
http://live555.com/proxyServer/ ---

## Response 4
http://live555.com/proxyServer/Thanks, it's a good idea to use a proxy which solved the problem itself.Live555 was tricky to install so I used go2rtc. It's only using one port 554 now. The camera is selected via the streams URL. Therefore it's easy scaleable. ---
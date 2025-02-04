# Thread Information
Title: Thread-1116692
Section: RouterOS
Thread ID: 1116692

# Discussion

## Initial Question
Hello everyone, I am trying to configure a reverse proxy with Mikrotik (rb3011 serving as a router) and HAProxy (intended for use as a reverse proxy). In essence, the goal is to create a list of blocked websites where a user on the local network, if attempting to access any of these sites, will be redirected to a local page. That part is okay, I wrote it just as an introduction for you to understand the context.I'm having trouble connecting Mikrotik with the VM where HAProxy is located. I tried adding a parent proxy and its port in IP -> Web Proxy, but I'm not sure if that's all that's needed. I apologize if this is a simple matter, I just can't figure it out based on the documentation.When I connect in this way and run tcpdump on port 80 (where HAProxy is listening) and try to openwww.google.comon the computer connected to Mikrotik, for which I set up a redirect to a local IP address, the request doesn't reach the HAProxy VM at all.I know the easiest solution is to redirect the hostname to a local IP address on the DNS server, but DNS can be easily overridden, so I wanted to handle it at the IP level.Initially, I tried to do everything on Mikrotik, added a list of blocked sites in layer7, created a mangle rule to extract IP addresses from that list, and set up redirection to a local IP within NAT. However, I didn't consider that many websites use HSTS, making it impractical to redirect all requests in that way.Thanks in advance to anyone who have any idea. ---

## Response 1
First. If the traffic is from the local network to the outside and has to go through a proxy. This is called such a proxy service and not reverse proxy.Secondly, you have redesigned the problem. Overwrite the DNS records of the domains you want to obstruct access to by overwriting the IP address of the web server on which you will have a page stating that the domain has been blocked.https://help.mikrotik.com/docs/spaces/R ... -DNSStaticFor exampleYour web server with the substituted site will have IP 10.0.0.1
```
/ip dnsstaticaddname=www.facebook.com address=10.0.0.1Of course there will be a problem with HTTPSWhich you will not jump over. Well, unless all customers agree to install your SSL CA on their devices.Otherwise you won't be able to pretend to be on facebook.comHappy new year!

---
```
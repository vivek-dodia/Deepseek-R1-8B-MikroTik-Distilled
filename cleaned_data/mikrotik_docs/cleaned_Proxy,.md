# Document Information
Title: Proxy
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/132350000/Proxy,

# Content
# 1Summary2Configuration examples2.1Transparent proxy configuration example2.2Proxy-based firewall – Access List3Enabling RAM or Store-based caching.3.1RAM proxy cache:3.2Store proxy cache:4Reference4.1General4.2Access List4.3Direct Access4.4Cache Management4.5Connections4.6Cache Inserts4.7Cache Lookups4.8Cache Contents5HTTP Methods5.1Options5.2GET5.3HEAD5.4POST5.5PUT5.6TRACESummary
MikroTik RouterOS performs proxying of HTTP and HTTP-proxy (for FTP and HTTP protocols) requests. The proxy server performs the Internet object cache function by storing requested Internet objects, i.e., data available via HTTP and FTP protocols on a system positioned closer to the recipient in the form of speeding up customer browsing by delivering them requested file copies from the proxy cache at local network speed. MikroTik RouterOS implements the following proxy server features:
A proxy server usually is placed at various points between users and the destination server (also known as the origin server) on the Internet.
AWeb proxy (cache)watches requests coming from clients, saving copies of the responses for itself. Then, if there is another request for the same URL, it can use the response that it has, instead of asking the origin server for it again. If the proxy has not requested a file, it downloads that from the original server.
There can be many potential purposes of proxy servers:
Allows filtering web content (by specific parameters, like source address, a destination address, port, URL, HTTP request method) scan outbound content, e.g., for data leak protection.
# Configuration examples
```
/ip/proxy
```
In MikroTik RouterOS, a proxy configuration is performed inthe/ip/proxymenu. See below how to enable the proxy on port 8080 and set up 192.168.88.254 as the proxy source address:
```
[admin@MikroTik] > ip/proxy/set enabled=yes port=8080 src-address=192.168.88.254
[admin@MikroTik] > ip/proxy/print
enabled: yes
src-address: 192.168.88.254
port: 8080
anonymous: no
parent-proxy: ::
parent-proxy-port: 0
cache-administrator: webmaster
max-cache-size: unlimited
max-cache-object-size: 2048KiB
cache-on-disk: no
max-client-connections: 600
max-server-connections: 600
max-fresh-time: 3d
serialize-connections: no
always-from-cache: no
cache-hit-dscp: 4
cache-path: web-proxy
```
# Transparent proxy configuration example
RouterOS can also act as a Transparent Caching server, with no configuration required in the customer’s web browser. A transparent proxy does not modify the requested URL or response. RouterOS will take all HTTP requests and redirect them to the local proxy service. This process will be entirely transparent to the user (users may not know anything about a proxy server that is located between them and the original server), and the only difference to them will be the increased browsing speed.
To enable the transparent mode, the firewall rule in destination NAT has to be added, specifying which connections (to which ports) should be transparently redirected to the proxy. Check proxy settings above and redirect us users (192.168.1.0/24) to a proxy server:
```
[admin@MikroTik] ip firewall nat> add chain=dstnat protocol=tcp src-address=192.168.1.0/24 dst-port=80 action=redirect to-ports=8080
[admin@MikroTik] ip firewall nat> print
Flags: X - disabled, I - invalid, D - dynamic
0   chain=dstnat protocol=tcp dst-port=80 action=redirect to-ports=8080
```
The web proxy can be used as a transparent and normal web proxy at the same time. In transparent mode, it is possible to use it as a standard web proxy, too. However, in this case, proxy users may have trouble reaching web pages that are accessed transparently.
# Proxy-based firewall – Access List
An access list is implemented in the same way as MikroTik firewall rules processed from the top to the bottom. The first matching rule specifies the decision of what to do with this connection. Connections can be matched by their source address, destination address, destination port, sub-string of the requested URL (Uniform Resource Locator), or request method. If none of these parameters is specified, every connection will match this rule.
If a connection is matched by a rule, the action property of this rule specifies whether a connection will be allowed or not (deny). If a connection does not match any rule, it will be allowed.
In this example assume that we have configured a transparent proxy server, it will block the websitehttp://www.facebook.com, we can always block the same for different networks by giving src-address:
```
/ip proxy access add src-address=192.168.1.0/24 dst-host=www.facebook.com action=deny
```
Users from network 192.168.1.0/24 will not be able to access the websitewww.facebook.com.
You can block also websites that contain specific words in the URL:
```
/ip proxy access add dst-host=:mail action=deny
```
This statement will block all websites which contain the word “mail” in the URL. Likewww.mail.com,www.hotmail.com,mail.yahoo.com, etc.
We can also stop downloading specific types of files like .flv, .avi, .mp4, .mp3, .exe, .dat, …etc.
```
/ip proxy access
add path=*.flv action=deny
add path=*.avi action=deny
add path=*.mp4 action=deny
add path=*.mp3 action=deny
add path=*.zip action=deny
add path=*.rar action=deny
```
Here are available also different wildcard characters, to create specific conditions and to match them by proxy access list. Wildcard properties (dst-host and dst-path) match a complete string (i.e., they will not match "example.com" if they are set to "example"). Available wildcards are '*' (match any number of any characters) and '?' (match any one character).
Regular expressions are also accepted here, but if the property should be treated as a regular expression, it should start with a colon (':').
To show that no symbols are allowed before the given pattern, we use the ^ symbol at the beginning of the pattern.
To specify that no symbols are allowed after the given pattern, we use the $ symbol at the end of the pattern.
# Enabling RAM or Store-based caching.
In this example, it will presume that you already have the proxy configured and working and you just want to enable caching. If a command/parameter detailed description is required check the reference section which is located right below the example section.
# RAM proxy cache:
Important commands:
```
[admin@MikroTik] /ip proxy> set max-cache-size=unlimited max-cache-object-size=50000KiB cache-on-disk=no
...
[admin@MikroTik] /ip proxy> print
enabled: yes
src-address: ::
port: 8080
anonymous: no
parent-proxy: 0.0.0.0
parent-proxy-port: 0
cache-administrator: webmaster
max-cache-size: unlimited  <-------
max-cache-object-size: 500000KiB  <-------
cache-on-disk: no  <-------
max-client-connections: 600
max-server-connections: 600
max-fresh-time: 3d
serialize-connections: no
always-from-cache: no
cache-hit-dscp: 4
cache-path: proxy-cache
```
# Store proxy cache:
Important commands:
```
[admin@MikroTik] > ip proxy set cache-on-disk=yes cache-path=/usb1/proxy/cache
[admin@MikroTik] > ip proxy print
enabled: yes
src-address: ::
port: 8080
anonymous: no
parent-proxy: 0.0.0.0
parent-proxy-port: 0
cache-administrator: webmaster
max-cache-size: unlimited  <-------
max-cache-object-size: 50000KiB  <-------
cache-on-disk: yes  <-------
max-client-connections: 600
max-server-connections: 600
max-fresh-time: 3d
serialize-connections: no
always-from-cache: no
cache-hit-dscp: 4
cache-path: usb1/proxy/cache  <-------
[admin@MikroTik] > file print
# NAME                                                           TYPE
0 skins                                                          directory
5 usb1/proxy                                                     directory
6 usb1/proxy/cache                                               web-proxy store   <-------
7 usb1/lost+found                                                directory
```
Check if a cache is working:
```
[admin@MikroTik] > ip proxy monitor
status: running
uptime: 2w20h28m25s
client-connections: 15
server-connections: 7
requests: 79772
hits: 30513
cache-used: 481KiB
total-ram-used: 1207KiB
received-from-servers: 4042536KiB
sent-to-clients: 4399757KiB
hits-sent-to-clients: 176934KiB
```
# Reference
List of all available parameters and commands per menu.
# General
```
/ip/proxy
```
Property | Description
----------------------
always-from-cache(yes | no; Default:no) | ignore client refresh requests if the content is considered fresh
anonymous(yes | no; Default:no) | If not set, the IP address of the client would be passed X-Forwarded-For header (could be accessed using HTTP_X_FORWARDED_FOR environment variable in remote servers)
cache-administrator(string; Default:webmaster) | Administrator's e-mail displayed on proxy error page
cache-hit-dscp(integer: 0..63; Default:4) | Automatically mark cache hit with the provided DSCP value
cache-on-disk(yes | no; Default:no) | Whether to store cache on disk
cache-path(string; Default:web-proxy) | A path where the cache will be stored, whencache-on-diskis enabled.
max-cache-object-size(integer: 0..4294967295[KiB]; Default:2048KiB) | Specifies the maximal cache object size, measured in kilobytes
max-cache-size(none | unlimited | integer: 0..4294967295[KiB]; Default:unlimited) | Specifies the maximal cache size, measured in kilobytes
max-client-connections(integer: Dynamic; Default:600) | Maximal number of connections accepted from clients (any further connections will be rejected)
max-fresh-time(time; Default:3d) | Maximal time to store a cached object. The validity period of an object is usually defined by the object itself, but in case it is set too high, you can override the maximal value
max-server-connections(integer: Dynamic; Default:600) | Maximal number of connections made to servers (any further connections from clients will be put on hold until some server connections will terminate)
parent-proxy(Ip4 | ip6; Default:0.0.0.0) | IP address and port of another HTTP proxy to redirect all requests to. If set to0.0.0.0parent proxy is not used.
parent-proxy-port(integer: 0..65535; Default:0) | Port that parent proxy is listening on.
port(integer: 0..65535; Default:8080) | TCP port the proxy server will be listening on. This port has to be specified on all clients that want to use the server as an HTTP proxy. A transparent (with zero configuration for clients) proxy setup can be made by redirecting HTTP requests to this port in the IP firewall using the destination NAT feature
serialize-connections(yes | no; Default:no) | Do not make multiple connections to the server for multiple client connections, if possible (i.e. server supports persistent HTTP connections). Clients will be served on the FIFO principle; the next client is processed when the response transfer to the previous one is completed. If a client is idle for too long (max 5 seconds by default), it will give up waiting and open another connection to the server
src-address(Ip4 | Ip6; Default:0.0.0.0) | A proxy will use a specified address when connecting to the parent proxy or website. If set to0.0.0.0then the appropriate IP address will be taken from the routing table.
# Access List
```
/ip/proxy/access
```
An access list is configured like regular firewall rules. Rules are processed from the top to the bottom. The first matching rule specifies the decision of what to do with this connection. There is a total of 6 classifiers that specify matching constraints. If none of these classifiers is specified, the particular rule will match every connection.
If a connection is matched by a rule, the action property of this rule specifies whether a connection will be allowed or not. If the particular connection does not match any rule, it will be allowed.
Property | Description
----------------------
action(allow | deny; Default:allow) | Specifies whether to pass or deny matched packets
dst-address(Ip4[-Ip4 | /0..32] | Ip6/0..128; Default:) | The destination address of the target server.
dst-host(string; Default:) | IP address or DNS name used to make a connection to the target server (this is the string user wrote in a browser before specifying the port and path to a particular web page
dst-port(integer[-integer[,integer[,...]]]: 0..65535; Default:) | List or range of ports the packet is destined to
local-port(integer: 0..65535; Default:) | Specifies the port of the web proxy via which the packet was received. This value should match one of the ports the web proxy is listening on.
method(any | connect | delete | get | head | options | post | put | trace; Default:) | The HTTP method used in the request (seeHTTP Methodssection at the end of this document)
path(string; Default:) | Name of the requested page within the target server (i.e. the name of a particular web page or document without the name of the server it resides on)
redirect-to(string; Default:) | In case of access is denied by this rule, the user shall be redirected to the URL specified here
src-address(Ip4[-Ip4 | /0..32] | Ip6/0..128; Default:) | The source address of the connection originator.
Read-only properties:
Property | Description
----------------------
hits(integer) | Count of requests that were matched by this rule
Wildcard properties (dst-host and dst-path) match a complete string (i.e., they will not match "example.com" if they are set to "example"). Available wildcards are '*' (match any number of any characters) and '?' (match any one character). Regular expressions are also accepted here, but if the property should be treated as a regular expression, it should start with a colon (':').
Small hints in using regular expressions:
It is strongly recommended to deny all IP addresses except those behind the router as the proxy still may be used to access your internal-use-only (intranet) web servers. Also, consult examples in Firewall Manual on how to protect your router.
# Direct Access
```
/ip/proxy/direct
```
Ifaparent-proxyproperty is specified, it is possible to tell the proxy server whether to try to pass the request to the parent proxy or to resolve it by connecting to the requested server directly. The direct Access List is managed just like the Proxy Access List described in the previous chapter except for the action argument.Unlike the access list, the direct proxy access list has a default action equal to deny. It takes place when no rules are specified or a particular request did not match any rule.
Property | Description
----------------------
action(allow | deny; Default:allow) | Specifies the action to perform on matched packets:allow- always resolve matched requests directly bypassing the parent routerdeny- resolve matched requests through the parent proxy. If no one is specified this has the same effect asallow.
dst-address(Ip4[-Ip4 | /0..32] | Ip6/0..128; Default:) | The destination address of the target server.
dst-host(string; Default:) | IP address or DNS name used to make a connection to the target server (this is the string user wrote in a browser before specifying port and path to a particular web page
dst-port(integer[-integer[,integer[,...]]]: 0..65535; Default:) | List or range of ports used by connection to the target server.
local-port(integer: 0..65535; Default:) | Specifies the port of the web proxy via which the packet was received. This value should match one of the ports the web proxy is listening on.
method(any | connect | delete | get | head | options | post | put | trace; Default:) | The HTTP method used in the request (seeHTTP Methodssection at the end of this document)
path(string; Default:) | Name of the requested page within the target server (i.e. the name of a particular web page or document without the name of the server it resides on)
src-address(Ip4[-Ip4 | /0..32] | Ip6/0..128; Default:) | The source address of the connection originator.
Read-only properties:
Property | Description
----------------------
hits(integer) | Count of requests that were matched by this rule
# Cache Management
```
/ip/proxy/cache
```
The cache access list specifies, which requests (domains, servers, pages) have to be cached locally by web proxy, and which do not. This list is implemented exactly the same way as the web proxy access list. The default action is to cache an object (if no matching rule is found).
Property | Description
----------------------
action(allow | deny; Default:allow) | Specifies the action to perform on matched packets:allow- cache objects from matched requestdeny- do not cache objects from matched request
dst-address(Ip4[-Ip4 | /0..32] | Ip6/0..128; Default:) | The destination address of the target server
dst-host(string; Default:) | IP address or DNS name used to make a connection to the target server (this is the string user wrote in a browser before specifying port and path to a particular web page
dst-port(integer[-integer[,integer[,...]]]: 0..65535; Default:) | List or range of ports the packet is destined to.
local-port(integer: 0..65535; Default:) | Specifies the port of the web proxy via which the packet was received. This value should match one of the ports the web proxy is listening on.
method(any | connect | delete | get | head | options | post | put | trace; Default:) | The HTTP method used in the request (seeHTTP Methodssection at the end of this document)
path(string; Default:) | Name of the requested page within the target server (i.e. the name of a particular web page or document without the name of the server it resides on)
src-address(Ip4[-Ip4 | /0..32] | Ip6/0..128; Default:) | The source address of the connection originator
Read-only properties:
Property | Description
----------------------
hits(integer) | Count of requests that were matched by this rule
# Connections
```
/ip/proxy/connections
```
This menu contains the list of current connections the proxy is serving.
Read-only properties:
Property | Description
----------------------
client() |
dst-address(Ip4 | Ip6) | IPv4/Ipv6 destination address of the connection
protocol(string) | Protocol name
rx-bytes(integer) | The number of bytes received by the client
server() |
src-address(Ip4 | Ip6) | Ipv4/ipv6 address of the connection originator
state(closing | connecting | converting | hotspot | idle | resolving | rx-header | tx-body | tx-eof | tx-header | waiting) | Connection state:closing- the data transfer is finished, and the connection is being finalizedconnecting- establishing toe connectionconverting- replacing header and footer fields in response or request packethotspot- check if hotspot authentication allows continuing (for hotspot proxy)idle- staying idleresolving- resolving the server's DNS namerx-header- receiving HTTP headertx-body- transmitting HTTP body to the clienttx-eof- writing chunk-end (when converting to chunked response)tx-header- transmitting HTTP header to the clientwaiting- waiting for transmission from a peer
tx-bytes(integer) | The number of bytes sent by the client
# Cache Inserts
```
/ip/proxy/inserts
```
This menu shows statistics on objects stored in a cache (cache inserts).
Read-only properties:
Property | Description
----------------------
denied(integer) | A number of inserts were denied by thecaching list.
errors(integer) | Number of disk or other system-related errors
no-memory(integer) | Number of objects not stored because there was not enough memory
successes(integer) | A number of successful cache inserts.
too-large(integer) | Number of objects too large to store
# Cache Lookups
```
/ip/proxy/lookup
```
This menu shows statistics on objects read from cache (cache lookups).
Read-only properties:
Property | Description
----------------------
denied(integer) | Number of requests denied by theaccess list.
expired(integer) | Number of requests found in cache, but expired, and, thus, requested from an external server
no-expiration-info(integer) | Conditional request received for a page that does not have the information to compare the request with
non-cacheable(integer) | Number of requests requested from the external servers unconditionally (as their caching is denied by the cache access list)
not-found(integer) | Number of requests not found in the cache, and, thus, requested from an external server (or parent proxy if configured accordingly)
successes(integer) | Number of requests found in the cache.
# Cache Contents
```
/ip/proxy/cache-contents
```
This menu shows cached contents.
Read-only properties:
Property | Description
----------------------
file-size(integer) | Cached object size
last-accessed(time) |
last-accessed-time(time) |
last-modified(time) |
last-modified-time(time) |
uri(string) |
# HTTP Methods
# Options
This method is a request for information about the communication options available on the chain between the client and the server identified by theRequest-URI. The method allows the client to determine the options and (or) the requirements associated with a resource without initiating any resource retrieval
# GET
This method retrieves whatever information identified by the Request-URI. If the Request-URI refers to a data processing process then the response to the GET method should contain data produced by the process, not the source code of the process procedure(-s), unless the source is the result of the process.
The GET method can become a conditional GET if the request message includes an If-Modified-Since, If-Unmodified-Since, If-Match, If-None-Match, or If-Range header field. The conditional GET method is used to reduce the network traffic specifying that the transfer of the entity should occur only under circumstances described by conditional header field(-s).
The GET method can become a partial GET if the request message includes a Range header field. The partial GET method intends to reduce unnecessary network usage by requesting only parts of entities without transferring data already held by the client.
The response to a GET request is cacheable if and only if it meets the requirements for HTTP caching.
# HEAD
This method shares all features of GET method except that the server must not return a message-body in the response. This retrieves the metainformation of the entity implied by the request which leads to its wide usage of it for testing hypertext links for validity, accessibility, and recent modification.
The response to a HEAD request may be cacheable in the way that the information contained in the response may be used to update the previously cached entity identified by that Request-URI.
# POST
This method requests that the origin server accept the entity enclosed in the request as a new subordinate of the resource identified by the Request-URI.
The actual action performed by the POST method is determined by the origin server and usually is Request-URI dependent.
Responses to POST method are not cacheable, unless the response includes appropriate Cache-Control or Expires header fields.
# PUT
This method requests that the enclosed entity be stored under the supplied Request-URI. If another entity exists under specified Request-URI, the enclosed entity should be considered as an updated (newer) version of that residing on the origin server. If the Request-URI is not pointing to an existing resource, the origin server should create a resource with that URI.
If the request passes through a cache and the Request-URI identifies one or more currently cached entities, those entries should be treated as stale. Responses to this method are not cacheable.
# TRACE
This method invokes a remote, application-layer loop-back of the request message. The final recipient of the request should reflect the message received back to the client as the entity-body of a 200 (OK) response. The final recipient is either the origin server or the first proxy or gateway to receive a Max-Forwards value of 0 in the request. A TRACE request must not include an entity.
Responses to this method MUST NOT be cached.
# Document Information
Title: Netwatch
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/8323208/Netwatch,

# Content
# Summary
Netwatch monitors the state of hosts on the network. Monitoring can be done with the following probe types:1) ICMP - pings to a specified IP address - hosts, with an option to adjust threshold values2) Simple - uses ping, without use of advanced metrics3) TCP conn, to test the TCP connection4) HTTP GET/HTTPS GET, request against a server you are monitoring5) DNS - sends DNS query to DNS server and checks for response.For each entry in the Netwatch table, you can specify an IP address, ping interval, and console scripts. The main advantage of Netwatch is its ability to issue arbitrary console commands on host state changes.
# Properties
Sub-menu:/tool/netwatch
```
/tool/netwatch
```
Property | Description
----------------------
host(Default:"") | The IP address of the server to be probed. Formats:-ipv4-ipv4@vrf-ipv6-ipv6@vrf-ipv6-linklocal%interface- domain name(for type=dns)
type(icmp| tcp-conn | http-get |http-get | dns |simple;Default:simple) | Type of the probe:-icmp- (ping-style) series of ICMP request-response with statistics-tcp-conn- test TCP connection (3-way handshake) to a server specified by IP and port-http-get- do an HTTP Get request and test for a range of correct replies-https-get- do an HTTP Get request and test for a range of correct replies-dns- do a specified DNS query for domain name- simple - simplified ICMP probe, with fewer options than "ICMP" type, used for backward compatibility with the older Netwatch version
interval(Default:10s) | The time interval between probe tests
timeout(Default:3s) | Max time limit to wait for a response
src-address(Default:"") | Source IP address which the Netwatch will try to use in order to reach the host. If address is not present, then the host will be considered as "down".
start-delay(Default:3s) | Time to wait before starting probe (on add, enable, or system start)
startup-delay(Default:5m) | Time to wait until starting Netwatch probe after system startup
up-script(Default:"") | Script to execute on the event of probe state change 'fail' --> 'OK'
down-script(Default:"") | Script to execute on the event of probe state change 'OK' --> 'fail'
test-script(Default:"") | Script to execute at the end of every probe test
The IP address of the server to be probed. Formats:
-ipv4-ipv4@vrf-ipv6-ipv6@vrf-ipv6-linklocal%interface- domain name(for type=dns)
```
@
```
```
@
```
```
%
```
Type of the probe:-icmp- (ping-style) series of ICMP request-response with statistics-tcp-conn- test TCP connection (3-way handshake) to a server specified by IP and port-http-get- do an HTTP Get request and test for a range of correct replies-https-get- do an HTTP Get request and test for a range of correct replies-dns- do a specified DNS query for domain name- simple - simplified ICMP probe, with fewer options than "ICMP" type, used for backward compatibility with the older Netwatch version
The time interval between probe tests
Max time limit to wait for a response
Source IP address which the Netwatch will try to use in order to reach the host. If address is not present, then the host will be considered as "down".
Time to wait before starting probe (on add, enable, or system start)
Time to wait until starting Netwatch probe after system startup
Script to execute on the event of probe state change 'fail' --> 'OK'
Script to execute on the event of probe state change 'OK' --> 'fail'
Script to execute at the end of every probe test
Netwatch executes scripts as *sys user, so any defined global variable in the Netwatch script will not be readable by for an example a scheduler or other users
It is possible to disable permission checking for RouterOS scripts under/system/scriptsmenu. This is useful when Netwatch does not have enough permissions to execute a script, though this decreases overall security. It is recommended to assign proper permissions to a script instead.
# Type-specific options
All config options specific to one probe type (e.g. icmp's packet-interval) are ignored for other probe types.
# ICMP probe options
Property | Description
----------------------
packet-interval(Default:50ms) | The time between ICMP-request packet send
packet-count(Default:10) | Total count of ICMP packets to send out within a single test
packet-size(Default:54(IPv4) or54(IPv6)) | The total size of the IP ICMP packet
thr-rtt-max(Default: 1s) | Fail threshold for rtt-max (a value above thr-max is a probe fail)
thr-rtt-avg(Default:100ms) | Fail threshold for rtt-avg
thr-rtt-stdev(Default:250ms) | Fail threshold for rtt-stdev
thr-rtt-jitter(Default:1s) | Fail threshold for rtt-jitter
thr-loss-percent(Default:85.0%) | Fail threshold for loss-percent
thr-loss-count(Default:4294967295(max)) | Fail threshold for loss-count
ttl(Default;255) | Manually set time to live value for ICMP packet
accept-icmp-time-exceeded(yes|no; Defaultno) | If the ICMP "time exceeded" message should be considered a valid response
# TCP-CONNECT
Property | Description
----------------------
port(Default:80) | TCP port (for both tcp-conn and http-get probes)
# TCP-CONNECT pass-fail criteria
Property | Description
----------------------
thr-tcp-conn-time(Default:00:05...00:30) | Fail threshold for tcp-connect-time, the configuration uses microseconds, if the time unit is not specified (s/m/h), log and status pages display the same value in milliseconds.
# HTTP-GET probe options
Property | Description
----------------------
port(Default:80) | TCP port (for both tcp-conn and http-get probes)
# HTTPS-GET probe options
Property | Description
----------------------
port(Default:443) | TCP port (for both tcp-conn and http-get probes)
certificate(Default:"") | Certificate from local store that should be used for host verification.
check-certificate(yes|no; Defaultno) | Enables trust chain validation from local certificate store.
# HTTP-GET/HTTPS-GET probe pass/fail criteria
Property | Description
----------------------
thr-http-time(Default:10s) | Fail threshold for http-resp-time
http-code-min(Default:100) | OK/fail criteria for HTTP response code.
http-code-max(Default:299) | Response in the range [http-code-min,http-code-max] is a probe pass/OK; outside - a probe fail. Seemozilla-http-statusorrfc7231
```
http-code-min
```
```
http-code-max
```
# DNS probe options
Property | Description
----------------------
host(Default:"") | DNS name that should be resolved.
record-type(A|AAAA|MX|NS; Default:A) | Record type that will be used for DNS probe.
dns-server | The DNS server that the probe should send its requests to, if not specified it will use the value from "/ip dns".
```
/ip dns
```
# Probe statistics/variables
You can view statistics and use these variables in scripting, keep in mind that variables containing "-" must be written like this, for example, "done-tests" would be $"done-tests"
# Generic:
Property | Description
----------------------
name | user added name for the Netwatch entry
comment | user added comment
host | host that was probed
type | probe type
interval | interval
timeout | timeout
since | The last time the status change happened
status | The current status of probe
done-tests | total count of probe tests already done so far
failed-tests | count of failed probe tests
user added comment
host that was probed
probe type
interval
timeout
The last time the status change happened
The current status of probe
count of failed probe tests
# ICMP:
Property | Description
----------------------
sent-count | ICMP packets sent out
response-count | Matching/valid ICMP packet responses received
loss-count | number of lost packets
loss-percent | number of lost packets in percent
rtt-avg | mean value of rtt (packet roundtrip time)
rtt-min | min rtt
rtt-max | max rtt
rtt-jitter | jitter ( = max - min) of rtt
rtt-stdev | standard deviation of rtt
# TCP:
Property | Description
----------------------
tcp-connect-time | time taken to establish a TCP connection
# HTTP:
Property | Description
----------------------
http-status-code | HTTP response status code (200 OK, 404 Not Found, etc.). Seemozilla-http-statusorRFC7231
# HTTPS:
Property | Description
----------------------
http-status-code | HTTP response status code (200 OK, 404 Not Found, etc.). Seemozilla-http-statusorRFC7231
# DNS:
Property | Description
----------------------
ip | IP address - the result ofArecord-type probe
ip6 | IPv6 address - the result ofAAAArecord-type probe
mail-servers | Mail servers along with their priority - the result ofMXrecord-type probe
name-servers | Name servers - the result ofNSrecord-type probe
# Logs
On each probe's OK/fail state change:
# Status
Command/tool/netwatch/printwill show the current status of Netwatch andread-onlyproperties:
# Quick Example
Here we will use a simple ICMP check to host with IP 8.8.8.8:
```
[admin@MikroTik] > /tool/netwatch add host=8.8.8.8 interval=30s up-script=":log info \"Ping to 8.8.8.8 successful\""
```
Afterward, in the logging section we can see Netwatch executed script:
```
[admin@MikroTik] > log print where message~"8.8.8.8"
08:03:26 script,info Ping to 8.8.8.8 successful
```
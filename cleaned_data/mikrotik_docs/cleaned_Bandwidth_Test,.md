# Document Information
Title: Bandwidth Test
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/7962644/Bandwidth+Test,

# Content
# Summary
```
Sub-menu: /tool
Packages required: system
```
The Bandwidth Tester can be used to measure the throughput to another MikroTik router (either wired or wireless) and thereby help to discover network "bottlenecks".
The TCP test uses the standard TCP protocol with acknowledgments and follows the TCP algorithm on how many packets to send according to latency, dropped packets, and other features in the TCP algorithm. Please review the TCP protocol for details on its internal speed settings and how to analyze its behavior. Statistics for throughput are calculated using the entire size of the TCP data stream. As acknowledgments are an internal working of TCP, their size and usage of the link are not included in the throughput statistics. Therefore this statistic is not as reliable as the UDP statistic when estimating throughput.
The UDP tester sends 110% or more packets than currently reported as received on the other side of the link. To see the maximum throughput of a link, the packet size should be set for the maximum MTU allowed by the links which is usually 1500 bytes. There is no acknowledgment required by UDP; this implementation means that the closest approximation of the throughput can be seen.
# Bandwidth Test Server
```
Sub-menu: /tool bandwidth-server
```
Property | Description
----------------------
allocate-udp-ports-from(integer 1000..64000; Default:2000) | Beginning of UDP port range
authenticate(yes | no; Default:yes) | Communicate only with authenticated clients
enabled(yes | no; Default:yes) | Defines whether bandwidth server is enabled or not
max-sessions(integer 1..1000; Default:100) | Maximal simultaneous test count
Example
Bandwidth Server:
```
[admin@MikroTik] /tool bandwidth-server> print
enabled: yes
authenticate: yes
allocate-udp-ports-from: 2000
max-sessions: 100
[admin@MikroTik] /tool bandwidth-server>
```
Active sessions:
```
[admin@MikroTik] /tool bandwidth-server session> print
# CLIENT          PROTOCOL DIRECTION USER
0 35.35.35.1      udp      send      admin
1 25.25.25.1      udp      send      admin
2 36.36.36.1      udp      send      admin
[admin@MikroTik] /tool bandwidth-server session>
```
To enablebandwidth-testserver without client authentication:
```
[admin@MikroTik] /tool bandwidth-server> set enabled=yes authenticate=no
[admin@MikroTik] /tool bandwidth-server> print
enabled: yes
authenticate: no
allocate-udp-ports-from: 2000
max-sessions: 100
[admin@MikroTik] /tool bandwidth-server>
```
# Bandwidth Test Client
```
Sub-menu: /tool bandwidth-test
```
Property | Description
----------------------
address(IP address | IPv6 prefix[%interface]; Default:) | IP address of host
direction(both | receive | transmit; Default:receive) | Direction of data flow
duration(time; Default:) | Duration of the test
interval(time: 20ms..5s; Default:1s) | Delay between reports (in seconds)
local-tx-speed(integer 0..18446744073709551615; Default: ) | Transfer test maximum speed (bits per second)
local-udp-tx-size(integer: 28..64000) | Local transmit packet size in bytes
password(string; Default:"") | Password for the remote user
protocol(udp | tcp; Default:udp) | Protocol to use
random-data(yes | no; Default:no) | If random-data is set to yes, the payload of the bandwidth test packets will have incompressible random data stream so that links that use data compression will not distort the results (this is CPU intensive and random-data should be set to no for low speed CPUs)
remote-tx-speed(integer 0..18446744073709551615; Default: ) | Receive test maximum speed (bits per second)
remote-udp-tx-size(integer: 28..64000) | Remote transmit packet size in bytes
connection-count(integer 1..255; Default:) | Number of TCP connections to use
user(string; Default:"") | Remote user
direction(both | receive | transmit; Default:receive)
Example
To run 15-second long bandwidth-test to the10.0.0.32host sending and receiving1000-byte UDP packets and using usernameadminto connect:
```
[admin@MikroTik] /tool> bandwidth-test 10.0.0.32 duration=15s \
\... direction=both local-udp-tx-size=1000 protocol=udp \
\... remote-udp-tx-size=1000 user=admin
status: done testing
duration: 15s
tx-current: 272.8Mbps
tx-10-second-average: 200.3Mbps
tx-total-average: 139.5Mbps
rx-current: 169.6Mbps
rx-10-second-average: 164.8Mbps
rx-total-average: 117.0Mbps
lost-packets: 373
random-data: no
direction: both
tx-size: 1000
rx-size: 1000
[admin@MikroTik] /tool>
```
Link-local IPv6 example:
```
[admin@MikroTik] > /tool bandwidth-test fe80::34:23ff:fe6a:570c%local
status: running
duration: 5s
rx-current: 23.9Mbps
rx-10-second-average: 15.1Mbps
rx-total-average: 15.1Mbps
lost-packets: 0
random-data: no
direction: receive
rx-size: 1500
```
# Document Information
Title: Speed Test
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/8978571/Speed+Test,

# Content
# Introduction
The Speed Test is an easy test tool for measuring ping, jitter, TCP and UDP throughput from one MikroTik device, to another. The "speed-test" command is based on the Ping Tool and Bandwidth Test. In order to use this command - Bandwidth test server needs to be accessible.
# General interface properties
The speed-test is based on five configurable properties:
# Configuration Example
Bandwidth and speed tests should be conducted through the devices, not on them to ensure real-life simulation and not to overload the CPU on the devices under testing,(DUT) due to the traffic generating process.
To run a simple test from device A (192.168.88.1) to device B (192.168.88.2):
```
[admin@MikroTik] > /tool/speed-test address=192.168.88.1
status: done
time-remaining: 0s
ping-min-avg-max: 541us / 609us / 3.35ms
jitter-min-avg-max: 0s / 76us / 2.76ms
loss: 0% (0/100)
tcp-download: 921Mbps local-cpu-load:30%
tcp-upload: 920Mbps local-cpu-load:30% remote-cpu-load:25%
udp-download: 917Mbps local-cpu-load:6% remote-cpu-load:21%
udp-upload: 916Mbps local-cpu-load:20% remote-cpu-load:6%
```
If any of device CPU utilization during test reaches 100% warning message will appear:
```
[admin@MikroTik]] > /tool/speed-test address=192.168.88.1
;;; results can be limited by cpu, note that traffic generation/termination
performance might not be representative of forwarding performance
status: done
time-remaining: 0s
ping-min-avg-max: 541us / 609us / 3.35ms
jitter-min-avg-max: 0s / 76us / 2.76ms
loss: 0% (0/100)
tcp-download: 721Mbps local-cpu-load:78%
tcp-upload: 820Mbps local-cpu-load:100% remote-cpu-load:84%
udp-download: 906Mbps local-cpu-load:10% remote-cpu-load:54%
udp-upload: 895Mbps local-cpu-load:55% remote-cpu-load:12%
```
"test-duration" parameter allows changing the duration of all of the 5 tests:
* ) UDP send
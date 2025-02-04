# Thread Information
Title: Thread-1122816
Section: RouterOS
Thread ID: 1122816

# Discussion

## Initial Question
Greetings, colleagues, I want to optimize my connection tracking to lower CPU and active connections without reason. I have a ccr2116 running with fasttrack, 5Gbps of traffic and 217, 000 connections at peak times.What do you think about this modification?
```
generic-timeout=3m\# Reduce from 10 minutes to 3 minutestcp-established-timeout=30m\# Reduce from 1 day to 30 minutestcp-close-timeout=5m\# Reduce from 10 minutes to 5 minutestcp-time-wait-timeout=5m\# Reduce from 10 minutes to 5 minutestcp-syn-sent-timeout=1m\# Reduce from 5 minutes to 1 minutetcp-syn-received-timeout=1m\# Reduce from 5 minutes to 1 minutetcp-fin-wait-timeout=5m\# Keep at 5 minutestcp-last-ack-timeout=5m\# Keep at 5 minutestcp-close-timeout=5m\# Keep at 5 minutestcp-max-retransmit-timeout=5m\# Keep at 5 minutestcp-unacked-timeout=5m\# Keep at 5 minutesudp-timeout=15s\# Keep low for ephemeral trafficudp-stream-timeout=3m\# Keep at 3 minutes for UDP flowsicmp-timeout=10s\# Keep at 10 seconds

---
```

## Response 1
I'm not qualified to say anything about the other timeouts, but let me share a piece of advice regarding "tcp-established-timeout".I suggest setting it to 7440 seconds (2 hours 4 minutes) at a minimum due to RFC 5382 (NAT Behavioral Requirements for TCP).https://datatracker.ietf.org/doc/html/rfc5382#section-5Quoting from it:[...] Some end-hosts can be configured to send keep-alive packets on such idle connections; by default, such keep-alive packets are sent every 2 hours if enabled [RFC1122]. [...][...] In such cases, the value of the "established connection idle-timeout" MUST NOT be less than 2 hours 4 minutes. [...] ---
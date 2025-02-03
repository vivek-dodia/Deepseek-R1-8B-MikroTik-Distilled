---
title: PPP
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/328072/PPP,
crawled_date: 2025-02-02T21:11:28.023306
section: mikrotik_docs
type: documentation
---

* 1Overview
* 2Introduction2.1PPP Client2.2PPP Client example2.3PPP Server
* 2.1PPP Client
* 2.2PPP Client example
* 2.3PPP Server
# Overview
The Point-to-Point Protocol (PPP) provides a standard method for transporting multi-protocol datagrams over point-to-point links. PPP in RouterOS is based onRFC 1661 standard.
# Introduction
The basic purpose of PPP at this point is to transport Layer-3 packets across a Data Link layer point-to-point link.Packets between both peers are assumed to deliver in order.
PPP is comprised of three main components:
* A method for encapsulating multi-protocol datagrams.
* A Link Control Protocol (LCP) for establishing, configuring, and testing the data-link connection.
* A family of Network Control Protocols (NCPs) for establishing and configuring different network-layer protocols.
Detailed PPP packet processing in RouterOS you can see in thePacket Flow Diagram.
## PPP Client
```
/interface ppp-client
```
## PPP Client example
This is an example of how to add a client using an exposed serial port from an LTE modem.
```
/interface ppp-client add apn=yourapn dial-on-demand=no disabled=no port=usb2
```
The dial-on-demand should to be set to 'no' for a continuous connection.
## PPP Server
```
/interface ppp-server
```
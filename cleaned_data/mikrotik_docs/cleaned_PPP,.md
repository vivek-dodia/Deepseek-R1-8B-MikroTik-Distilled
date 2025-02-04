# Document Information
Title: PPP
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/328072/PPP,

# Content
# Overview
The Point-to-Point Protocol (PPP) provides a standard method for transporting multi-protocol datagrams over point-to-point links. PPP in RouterOS is based onRFC 1661 standard.
# Introduction
The basic purpose of PPP at this point is to transport Layer-3 packets across a Data Link layer point-to-point link.Packets between both peers are assumed to deliver in order.
PPP is comprised of three main components:
Detailed PPP packet processing in RouterOS you can see in thePacket Flow Diagram.
# PPP Client
```
/interface ppp-client
```
# PPP Client example
This is an example of how to add a client using an exposed serial port from an LTE modem.
```
/interface ppp-client add apn=yourapn dial-on-demand=no disabled=no port=usb2
```
The dial-on-demand should to be set to 'no' for a continuous connection.
# PPP Server
```
/interface ppp-server
```
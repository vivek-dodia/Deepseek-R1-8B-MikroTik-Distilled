---
title: PCQ example
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/137986099/PCQ+example,
crawled_date: 2025-02-02T21:10:45.811794
section: mikrotik_docs
type: documentation
---

Per Connection Queue (PCQ) is a queuing discipline that can be used to dynamically equalize or shape traffic for multiple users, using little administration. It is possible to divide PCQ scenarios into three major groups: equal bandwidth for a number of users, certain bandwidth equal distribution between users, and unknown bandwidth equal distribution between users.
# Equal Bandwidth for a Number of Users
Use PCQ type queue when you need to equalize the bandwidth [and set max limit] for a number of users. We will set the 64kbps download and 32kbps upload limits.
There are two ways how to make this: using mangle and queue trees, or, using simple queues.
1. Mark all packets with packet-marks upload/download: (let's consider that ether1-WAN is the public interface to the Internet and ether2-LAN is a local interface where clients are connected):
```
/ip firewall mangle add chain=prerouting action=mark-packet \
   in-interface=ether2-LAN new-packet-mark=client_upload
/ip firewall mangle add chain=prerouting action=mark-packet \
   in-interface=ether1-WAN new-packet-mark=client_download
```
2. Set up two PCQ queue types - one for download and one for upload.dst-addressis a classifier for the user's download traffic,andsrc-addressfor upload traffic:
```
dst-address
```
```
src-address
```
```
/queue type add name="PCQ_download" kind=pcq pcq-rate=64000 pcq-classifier=dst-address
/queue type add name="PCQ_upload" kind=pcq pcq-rate=32000 pcq-classifier=src-address
```
3. Finally, two queue rules are required, one for download and one for upload:
```
/queue tree add parent=global queue=PCQ_download packet-mark=client_download
/queue tree add parent=global queue=PCQ_upload packet-mark=client_upload
```
If you don't like using mangle and queue trees, you can skip step 1, do step 2, and step 3 would be to create one simple queue as shown here:
```
/queue simple add target=192.168.0.0/24 queue=PCQ_upload/PCQ_download
```
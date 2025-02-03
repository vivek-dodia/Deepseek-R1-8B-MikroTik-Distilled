---
title: Queue types
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/196345871/Queue+types,
crawled_date: 2025-02-02T21:10:48.551651
section: mikrotik_docs
type: documentation
---

# Overview
Queue type (also known as a queuing discipline) refers to the policy by which various data packets are managed in a network queue.
This policy determines which packet to send next from the queue when a data transmission has been completed. The queue type impacts how the network handles data traffic, which in turn affects factors such as the distribution of bandwidth among different flows, latency, and the handling of congestion.
Queue types can be simple or complex, and different types have different strengths and weaknesses. For example, a First In, First Out (FIFO) queue is simple and ensures fairness in the order of packet processing, but it can lead to issues such as head-of-line blocking. More complex queue types, such as those that implement fair queuing or congestion avoidance, can help manage network performance more effectively, but they may require more resources and configuration.
Therefore, the choice of queue type depends on the specific needs and characteristics of the network.
# Queue type introduction
* BFIFO (Byte-oriented First In, First Out):Features:BFIFO is a simple byte-oriented queuing discipline that sends out packets in the order they arrived and based on their size.Advantages:Simplicity and fairness in packet management.Disadvantages:BFIFO can lead to head-of-line blocking, where a large packet can delay all the smaller packets behind it. Also, there is no mechanism to prevent congestion or prioritize packets.
* PFIFO (Packet-oriented First In, First Out):Features:Like BFIFO but operates on a packet basis rather than bytes.Advantages:Easy to implement and understand. It's fair in terms of packet numbers.Disadvantages:Like BFIFO, it suffers from head-of-line blocking and doesn't have any congestion management mechanism.
* CAKE (Common Applications Kept Enhanced):Features:A comprehensive queue management system designed to combat bufferbloat and ensure fair queuing. It combines CoDel, FQ, and other technologies.Advantages:Excellent at managing latency under any network condition. It's particularly useful in consumer broadband connections.Disadvantages:More complex to configure than simpler queuing disciplines. Not ideal for all use cases, particularly where fine-tuned control is required.
* CoDel (Controlled Delay):Features:CoDel aims to improve bufferbloat by dropping packets to control queue delay.Advantages:Good at managing latency and avoiding bufferbloat.Disadvantages:CoDel on its own does not provide fair queuing.
* FQ_CoDel (Fair Queuing Controlled Delay):Features:Combines the latency management of CoDel with fair queuing.Advantages:Excellent latency management and fair distribution of bandwidth among flows. Generally considered a good default choice.Disadvantages:More complex than simpler queue disciplines, which can make it harder to configure.
* MQ_PFIFO (Multiqueue Packet First In, First Out):Features:MQ_PFIFO is an extension of PFIFO that supports multiple queues.Advantages:Allows different queues for different types or priorities of traffic.Disadvantages:Still suffers from head-of-line blocking and lacks a built-in congestion management mechanism.
* RED (Random Early Detection):Features:RED aims to anticipate and prevent congestion by randomly dropping packets before the queue becomes full.Advantages:Helps to prevent congestion and can improve overall network performance.Disadvantages:Configuration can be complex and needs to be tuned for the network's specific characteristics. Misconfiguration can lead to reduced performance.
* SFQ (Stochastic Fairness Queuing):Features:SFQ aims to ensure a fair distribution of resources among flows by assigning them to different dynamic queues.Advantages:Helps to prevent a single flow from dominating the connection.Disadvantages:SFQ does not manage latency or congestion. The number of queues can also increase memory usage.
BFIFO (Byte-oriented First In, First Out):
* Features:BFIFO is a simple byte-oriented queuing discipline that sends out packets in the order they arrived and based on their size.
* Advantages:Simplicity and fairness in packet management.
* Disadvantages:BFIFO can lead to head-of-line blocking, where a large packet can delay all the smaller packets behind it. Also, there is no mechanism to prevent congestion or prioritize packets.
PFIFO (Packet-oriented First In, First Out):
* Features:Like BFIFO but operates on a packet basis rather than bytes.
* Advantages:Easy to implement and understand. It's fair in terms of packet numbers.
* Disadvantages:Like BFIFO, it suffers from head-of-line blocking and doesn't have any congestion management mechanism.
CAKE (Common Applications Kept Enhanced):
* Features:A comprehensive queue management system designed to combat bufferbloat and ensure fair queuing. It combines CoDel, FQ, and other technologies.
* Advantages:Excellent at managing latency under any network condition. It's particularly useful in consumer broadband connections.
* Disadvantages:More complex to configure than simpler queuing disciplines. Not ideal for all use cases, particularly where fine-tuned control is required.
CoDel (Controlled Delay):
* Features:CoDel aims to improve bufferbloat by dropping packets to control queue delay.
* Advantages:Good at managing latency and avoiding bufferbloat.
* Disadvantages:CoDel on its own does not provide fair queuing.
FQ_CoDel (Fair Queuing Controlled Delay):
* Features:Combines the latency management of CoDel with fair queuing.
* Advantages:Excellent latency management and fair distribution of bandwidth among flows. Generally considered a good default choice.
* Disadvantages:More complex than simpler queue disciplines, which can make it harder to configure.
MQ_PFIFO (Multiqueue Packet First In, First Out):
* Features:MQ_PFIFO is an extension of PFIFO that supports multiple queues.
* Advantages:Allows different queues for different types or priorities of traffic.
* Disadvantages:Still suffers from head-of-line blocking and lacks a built-in congestion management mechanism.
RED (Random Early Detection):
* Features:RED aims to anticipate and prevent congestion by randomly dropping packets before the queue becomes full.
* Advantages:Helps to prevent congestion and can improve overall network performance.
* Disadvantages:Configuration can be complex and needs to be tuned for the network's specific characteristics. Misconfiguration can lead to reduced performance.
SFQ (Stochastic Fairness Queuing):
* Features:SFQ aims to ensure a fair distribution of resources among flows by assigning them to different dynamic queues.
* Advantages:Helps to prevent a single flow from dominating the connection.
* Disadvantages:SFQ does not manage latency or congestion. The number of queues can also increase memory usage.
In choosing a queue discipline, you'll need to consider the characteristics of your network and what you prioritize most, such as latency, fairness, simplicity, or congestion management.
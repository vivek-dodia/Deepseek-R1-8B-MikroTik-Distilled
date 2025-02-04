# Document Information
Title: Queue types
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/196345871/Queue+types,

# Content
# Overview
Queue type (also known as a queuing discipline) refers to the policy by which various data packets are managed in a network queue.
This policy determines which packet to send next from the queue when a data transmission has been completed. The queue type impacts how the network handles data traffic, which in turn affects factors such as the distribution of bandwidth among different flows, latency, and the handling of congestion.
Queue types can be simple or complex, and different types have different strengths and weaknesses. For example, a First In, First Out (FIFO) queue is simple and ensures fairness in the order of packet processing, but it can lead to issues such as head-of-line blocking. More complex queue types, such as those that implement fair queuing or congestion avoidance, can help manage network performance more effectively, but they may require more resources and configuration.
Therefore, the choice of queue type depends on the specific needs and characteristics of the network.
# Queue type introduction
BFIFO (Byte-oriented First In, First Out):
PFIFO (Packet-oriented First In, First Out):
CAKE (Common Applications Kept Enhanced):
CoDel (Controlled Delay):
FQ_CoDel (Fair Queuing Controlled Delay):
MQ_PFIFO (Multiqueue Packet First In, First Out):
RED (Random Early Detection):
SFQ (Stochastic Fairness Queuing):
In choosing a queue discipline, you'll need to consider the characteristics of your network and what you prioritize most, such as latency, fairness, simplicity, or congestion management.
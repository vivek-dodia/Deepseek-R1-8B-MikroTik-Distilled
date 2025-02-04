# Document Information
Title: PFIFO,BFIFO
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/196345880/PFIFO+BFIFO,

# Content
# PFIFO (Packet First-In, First-Out)
# Description:
PFIFO (Packet First-In, First-Out) is a queue management strategy that follows the basic queue logic. The main principle of PFIFO is that the first packet to arrive is the first packet to be transmitted out. This method is simple, and straightforward, and ensures that no packet receives preferential treatment over the others.
When packets enter the queue, they are placed at the end (tail) of the queue. As space becomes available for transmission, the packets at the front (head) of the queue are transmitted first. If the queue is full when a packet arrives, the packet is dropped or other policies are followed, depending on the overall queue management strategy in place.
# Characteristics:
Simplicity:PFIFO is one of the simplest forms of queue management. It doesn't require complex algorithms or significant computational resources. This makes it easy to implement and understand.
Fairness:All packets are treated equally, regardless of their source, destination, or content. The first packet in is the first one out.
No Prioritization:There's no inherent capability to prioritize certain types of traffic over others. While this ensures fairness, it can be a drawback when dealing with different types of network traffic that might need prioritization.
# Examples:
Imagine a line at the post office. Each person (packet) waiting in line represents a data packet waiting in the queue. The first person in line gets served first, then the next, and so on. If the post office is too busy and the line is full, any new person arriving would have to wait or leave (the packet is dropped).
# Conclusion:
While PFIFO is simple and straightforward, its lack of traffic prioritization capabilities can be a downside, especially when managing network traffic that contains different types of data. In these situations, more complex queue management algorithms, such as Priority Queuing (PQ), Class-Based Weighted Fair Queuing (CBWFQ), or Low Latency Queuing (LLQ), might be more suitable.
# BFIFO (Byte First-In, First-Out)
# Description:
BFIFO (Byte First-In, First-Out) is another queue management strategy, similar to PFIFO in its principle of operation, but with a key difference: BFIFO operates based on the size of packets, or bytes, rather than on the number of packets.
In a BFIFO system, when packets enter the queue, they are still placed at the end, and packets at the front are transmitted first. However, the queue size is calculated in bytes, not in number of packets. When the queue reaches its maximum byte size, any new packets that arrive are dropped, or other policies are followed.
# Characteristics:
Byte-Based:Unlike PFIFO, BFIFO calculates the queue size based on bytes, which allows for more precise control of bandwidth usage.
Fairness:BFIFO also ensures fairness as it treats all packets equally, regardless of their source, destination, or content.
No Prioritization:Similar to PFIFO, there's no inherent capability in BFIFO to prioritize certain types of traffic over others.
# Examples:
Consider a public bus as an example of a BFIFO system. The bus has a maximum capacity of passengers it can carry (similar to the byte size of the queue). Even if there is a line of people waiting (packets), if the bus is full, new passengers cannot get on (packets are dropped).
# Comparison: PFIFO vs. BFIFO
While both PFIFO and BFIFO are FIFO (First-In, First-Out) strategies and follow the basic queue logic, there are some differences:
Queue Size:PFIFO considers the queue size in terms of the number of packets, while BFIFO calculates the queue size in bytes. This means that BFIFO takes into account the size of each packet, which can allow for more accurate control of bandwidth usage.
Packet Dropping:In PFIFO, packets are dropped when the queue is full in terms of the number of packets. In BFIFO, packets are dropped when the byte size of the queue is exceeded, even if this means dropping a packet that is larger than the remaining space in the queue.
Fairness:Both PFIFO and BFIFO are fair in terms of the order of packet transmission – the first in is the first out. However, in a situation where packets are of different sizes, PFIFO could lead to a situation where a large packet takes up a lot of resources but is treated the same as a smaller packet. On the other hand, BFIFO's byte-based approach can provide more balanced resource usage.
Complexity:Both strategies are simple compared to more complex queuing strategies that prioritize certain types of traffic. However, BFIFO is slightly more complex than PFIFO because it requires tracking the total size of all packets in the queue.
Overall, the choice between PFIFO and BFIFO depends on the specific requirements of your network and the characteristics of your traffic.
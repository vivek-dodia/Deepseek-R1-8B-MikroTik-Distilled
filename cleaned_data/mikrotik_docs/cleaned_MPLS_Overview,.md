# Document Information
Title: MPLS Overview
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/40992794/MPLS+Overview,

# Content
# Overview
MPLS stands for MultiProtocol Label Switching. It kind of replaces IP routing - packet forwarding decision (outgoing interface and next-hop router) is no longer based on fields in IP header (usually destination address) and routing table, but on labels that are attached to packet. This approach speeds up the forwarding process because next-hop lookup becomes very simple compared to routing lookup (finding the longest matching prefix).
The efficiency of the forwarding process is the main benefit of MPLS, but it must be taken into account that MPLS forwarding disables the processing of network layer (e.g. IP) headers, therefore no network layer-based actions like NAT and filtering can be applied to MPLS forwarded packets. Any network-layer-based actions should be taken on ingress or egress of MPLS cloud, with the preferred way being ingress - this way, e.g. traffic that is going to be dropped anyway does not travel through the MPLS backbone.
In the simplest form, MPLS can be thought of as improved routing - labels are distributed by means of LDP protocol for routes that are active and a labeled packet takes the same path it would take if it was not labeled. A router that routes unlabeled packets using some route for which it has received a label from the next hop, imposes a label on the packet, and sends it to the next hop - gets MPLS switched further along its path. A router that receives a packet with a label it has assigned to some route changes the packet label with one received from the next hop of a particular route and sends a packet to the next hop. Label switched path ensures delivery of data to the MPLS cloud egress point. Applications of MPLS are based on this basic MPLS concept of label switched paths.
Another way of establishing label switching paths is traffic engineering tunnels (TE tunnels) by means of the RSVP-TE protocol. Traffic engineering tunnels allow explicitly routed LSPs and constraint-based path selection (where constraints are interface properties and available bandwidth).
Taking into account the complexity, new protocols, and applications that MPLS introduces and the differences of concepts that MPLS adds to routed/bridged networks, it is recommended to have an in-depth understanding of MPLS concepts before implementing MPLS in a production network. Some suggested reading material:
# Supported Features
Currently, RouterOS supports the following MPLS related features:
MPLS features that RouterOS DOES NOT HAVE yet:
* link/node protection
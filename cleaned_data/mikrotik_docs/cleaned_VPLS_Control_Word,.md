# Document Information
Title: VPLS Control Word
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/128974851/VPLS+Control+Word,

# Content
# Summary
VPLS allows remote sites to share an Ethernet broadcast domain by connecting sites throughpseudo-wires(PW)tunnels over a packet switching network (PSN). Since VPLS encapsulation adds additional overhead, each interface in LSP should be able to transmit a large enough packet.
Each ethernet chipset has hardware limitations on the maximum packet size that it can transmit. Even now there are Ethernets that support only one Vlan tag, meaning that the maximum packet size without Ethernet header and checksum (L2MTU) is 1504 bytes. Obviously, it is not enough to forward VPLS encapsulated Ethernet frame without fragmentation (at least 1524 L2MTU support is required). SeeMTU in RouterOSfor maximum supported L2MTUs on RouterBOADs.
Since not even all RouterBOARDs support enough L2MTU to transmit VPLS encapsulated packet without fragmentation, RouterOS has added Pseudowire Fragmentation and Reassembly (PWE3) support according to RFC 4623 using 4-byteControl Word (CW).
# Control Word Usage
In RouterOS, Control Word is used for packet fragmentation and reassembly inside the VPLS tunnel and is done by utilizing optionalControl Word (CW). CW is added between PW label (demultiplexor) and packet payload and adds an additional 4-byte overhead.
CW usage is controlled by the ofuse-control-wordparameter in VPLS configuration.
```
use-control-word
```
As you can seeControl Wordis divided into 5 fields:
According to RFC generation and processing of sequence numbers is optional.
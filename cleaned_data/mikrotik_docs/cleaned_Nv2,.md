# Document Information
Title: Nv2
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/122388485/Nv2,

# Content
# Overview
Nv2 protocol is a proprietary wireless protocol developed by MikroTik for use with Atheros 802.11 wireless chips. Nv2 is based on TDMA (Time Division Multiple Access) media access technology instead of CSMA (Carrier Sense Multiple Access) media access technology used in regular 802.11 devices.
TDMA media access technology solves hidden node problem and improves media usage, thus improving throughput and latency, especially in PtMP networks.
Nv2 is supported for Atheros 802.11n chips and legacy 802.11a/b/g chips starting from AR5212, but not supported on older AR5211 and AR5210 chips. This means that both - 11n and legacy devices can participate in the same network and it is not required to upgrade hardware to implement Nv2 in network.
Media access in Nv2 network is controlled by Nv2 Access Point. Nv2 AP divides time into fixed size "periods" which are dynamically divided into downlink (data sent from AP to clients) and uplink (data sent from clients to AP) portions, based on the queue state on AP and clients. Uplink time is further divided between connected clients based on their requirements for bandwidth. At the beginning of each period, AP broadcasts a schedule that tells clients when they should transmit and the amount of time they can use.
In order to allow new clients to connect, Nv2 AP periodically assigns uplink time for "unspecified" client - this time interval is then used by a fresh client to initiate registration to AP. Then AP estimates propagation delay between AP and client and starts periodically scheduling uplink time for this client in order to complete registration and receive data from client.
Nv2 implements dynamic rate selection on a per-client basis and ARQ for data transmissions. This enables reliable communications across Nv2 links.
For QoS Nv2 implements variable number of priority queues with built-in default QoS scheduler that can be accompanied with fine-grained QoS policy based on firewall rules or priority information propagated across network using VLAN priority or MPLS EXP bits.
Nv2 protocol limit is 511 clients per interface.
# Nv2 protocol implementation status
Nv2 has the following features:
# Compatibility and coexistence with other wireless protocols
Nv2 protocol is not compatible to or based on any other available wireless protocols or implementations, either TDMA based or any other kind. This implies thatonly Nv2 supporting and enabled devices can participate in Nv2 network.
Regular 802.11 devices will not recognize and will not be able to connect to Nv2 AP. RouterOS devices that have Nv2 support (that is - have RouterOS version 5.0rc1 or higher) will see Nv2 APs when issuing scan command, but will only connect to Nv2 AP if properly configured.
As Nv2 does not use CSMA technology it may disturb any other network in the same channel. In the same way other networks may disturb Nv2 network, because every other signal is considered noise.
The key points regarding compatibility and coexistence:
# How Nv2 compares with Nstreme and 802.11
# Nv2 vs 802.11
The key differences between Nv2 and 802.11:
# Nv2 vs Nstreme
The key differences between Nv2 and Nstreme:
# Configuring Nv2
wireless-protocolsetting controls which wireless protocol selects and uses. Note that the meaning of this setting depends on the interface role (either it is AP or client) that depends on interfacemodesetting. Find possible values ofwireless-protocoland their meaning in table below.
value | AP | client | unspecified | any | 802.11 | nstreme | Nv2 | Nv2-nstreme-802.11 | Nv2-nstreme
---------------------------------------------------------------------------------------------------
establish nstreme or 802.11 network based on oldnstremesetting | connect to nstreme or 802.11 network based on oldnstremesetting
same asunspecified | scan for all matching networks, no matter what protocol, connect using protocol of chosen network
establish 802.11 network | connect to 802.11 networks only
establish Nstreme network | connect to Nstreme networks only
establish Nv2 network | connect to Nv2 networks only
establish Nv2 network | scan for Nv2 networks, if suitable network found - connect, otherwise scan for Nstreme networks, if suitable network found - connect, otherwise scan for 802.11 network and if suitable network found - connect.
establish Nv2 network | scan for Nv2 networks, if suitable network found - connect, otherwise scan for Nstreme networks and if suitable network found - connect
Note thatwireless-protocolvaluesNv2-nstreme-802.11andNv2-nstremeDO NOTspecify some hybrid or special kind of protocol - these values are implemented to simplify client configuration when protocol of network that client must connect to can change. Using these values can help in migrating network to Nv2 protocol.
Most of Nv2 settings are significant only to Nv2 AP - Nv2 client automatically adapts necessary settings from AP. The following settings are relevant to Nv2 AP:
"sync-master" - works as nv2-mode=fixed-downlink (so uses nv2-downlink-ratio), but allows slaves to sync to this master; "sync-slave" - tries to sync to master (or already synced slave) and adapt period-size and downlink ratio settings from master.
The follwing settings are significant on both - Nv2 AP and Nv2 client:
# Migrating to Nv2
Usingwireless-protocolsetting aids in migration or evaluating Nv2 protocol in existing networks really simple and reduce downtime as much as possible. These are the recommended steps:
The basic troubleshooting guide:
# Nv2 AP Synchronization
This feature will let multiple MikroTik Nv2 APs on the same location to coexist in a better fashion by reducing the interference between each other. This feature will synchronize the transmit/receive time windows of APs in the same frequency, so that all synced MikroTik Nv2 APs transmits/receives at the same time. That allows to reuse the same wireless frequency on the location for multiple APs giving more flexibility in frequency planning.
To make Nv2 synced setup:
# Configuration example
Master AP:
```
/interface wireless set wlan1 mode=ap-bridge ssid=Sector1 frequency=5220 nv2-mode=sync-master nv2-preshared-key=clients1 nv2-sync-secret=Tower1
```
Slave AP:
```
/interface wireless set wlan1 mode=ap-bridge ssid=Sector2 frequency=5220 nv2-mode=sync-slave nv2-preshared-key=clients2 nv2-sync-secret=Tower1
```
Monitor interface on the Slave AP:
```
[admin@SlaveAP] /interface wireless> monitor wlan1
status: running-ap
channel: 5220/20/an
wireless-protocol: nv2
noise-floor: -110dBm
registered-clients: 1
authenticated-clients: 1
nv2-sync-state: synced
nv2-sync-master: 4C:5E:0C:57:84:38
nv2-sync-distance: 1
nv2-sync-period-size: 2
nv2-sync-downlink-ratio: 50
```
Debug logs on the Master AP:
```
09:22:08 wireless,debug wlan1: 4C:5E:0C:57:85:BE attempts to sync
```
Debug logs on the Slave AP:
```
09:22:08 wireless,debug wlan1: attempting to sync to 4C:5E:0C:57:84:38
09:22:09 wireless,debug wlan1: synced to 4C:5E:0C:57:84:38
```
# QoS in Nv2 network
QoS in Nv2 is implemented by means of variable number of priority queues. Queue is considered for transmission based on rule recommended by 802.1D-2004 - only if all higher priority queues are empty. In practice this means that at first all frames from queue with higher priority will be sent, and only then next queue is considered. Therefore QoS policy must be designed with care so that higher priority queues do not make lower priority queues starve.
QoS policy in Nv2 network is controlled by AP, clients adapt policy from AP. On AP QoS policy is configured withNv2-queue-countandNv2-qosparameters.Nv2-queue-countparameter specifies number of priority queues used. Mapping of frames to queues is controlled byNv2-qosparameter.
# Nv2-qos=default
In this mode outgoing frame at first is inspected by built-in QoS policy algorithm that selects queue based on packet type and size. If built-in rules do not match, queue is selected based on frame priority field, as inNv2-qos=frame-prioritymode.
# Nv2-qos=frame-priority
In this mode QoS queue is selected based on frame priority field. Note that frame priority field is not some field in headers and therefore it is valid only while packet is processed by given device. Frame priority field must be set either explicitly by firewall rules or implicitly from ingress priority by frame forwarding process, for example, from MPLS EXP bits. For more information on frame priority field see:
Queue is selected based on frame priority according to 802.1D recommended user priority to traffic class mapping. Mapping depends on number of available queues (Nv2-queue-countparameter). For example, if number of queues is 4, mapping is as follows (pay attention how this mapping resembles mapping used by WMM):
If number of queues is 2 (default), mapping is as follows:
If number of queues is 8 (maximum possible), mapping is as follows:
For other mappings, discussion on rationale for these mappings and recommended practices please see 802.1D-2004.
# Security in Nv2 network
Nv2 security implementation has the following features:
Being proprietary protocol Nv2 does not use security mechanisms of 802.11, therefore security configuration is different. Interface using Nv2 protocol ignoressecurity-profilesetting. Instead, security is configured by the following interface settings:
* Nv2-preshared-key- preshared key to use for authentication. Data encryption keys are derived from preshared key during 4-way handshake. Preshared key must be the same in order for 2 devices to establish connection. If preshared key will differ, connection will time out because remote party will not be able to correctly interpret key exchange messages.
# Repository Information
Name: tzsp-reader

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/gravadigital/tzsp-reader.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: example-ipfile.json
================================================
{
    "192.168.1.1":   "User 1",
    "192.168.1.2":   "User 2",
    "192.168.1.3":   "User 3",
    "192.168.1.4":   "User 4",
    "192.168.1.5":   "User 5"
}
================================================

File: README.md
================================================
# TZSP READER for Mikrotik.
Tzsp reader is a package reader coming from a mikrotik.
With this application you can easily see the consumption of the network in real time and monitor the traffic.
## beta:
This project is constantly changing in its state of beta
### Read the wiki:
[wiki is here!](https://github.com/gravadigital/tzsp-reader/wiki)
### Use
```
python tzsp-reader.py
```
#### options
* -h: show conections history log_panel_columns
### Prerequisites
before start you have to [configure sniffer](https://wiki.mikrotik.com/wiki/Manual:Tools/Packet_Sniffer) in the mikrotik.
### Screenshot
![screenshot](https://raw.githubusercontent.com/gravadigital/tzsp-reader/master/example/statistics.jpg)
### History ( -h option)
![screenshot](https://raw.githubusercontent.com/gravadigital/tzsp-reader/master/example/tzsp-reader.png)
## ChangeLog
### beta realease 0.0.5
* change consumption measurement
* add protocols statistics
* history with -h option
### beta realease 0.0.4
* Corrections in consumption measurement
### beta realease 0.0.3
* ipfile.json added to display labels for ips
* fix local ip filter
### beta release 0.0.2
* In this version you can monitor the traffic and view logs in real time of the requests
### Planned improvements for realease:
* Better traffic monitoring
* Handle resize
* List of main countries
* Colors alarms
* Statistics
* Database connection for long-term analysis
================================================

File: run.sh
================================================
#!/bin/bash
export DISPLAY=:0
gnome-terminal -e "python tzsp-reader.py" --full-screen --zoom=1.5 --hide-menubar
================================================

File: tzsp-reader.py
================================================
# -*- coding: utf-8 -*-
import socket
import os
import sys
import signal
import struct
import binascii
import json
import time
import math
import curses
import locale
from struct import *
from operator import itemgetter
starttime=time.time()
UDP_IP = "0.0.0.0"
UDP_PORT = 37008
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))
def signal_handler(signal, frame):
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
def eth_addr (a) :
  b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
  return b
def getType(typeData):
	types = {
		0:"Received tag list",
		1:"Packet for transmit",
		2:"Reserved",
		3:"Configuration",
		4:"Keepalive",
		5:"port opener"
	}
	return types[typeData]
def getProtocol(typeData):
	types = {
		0x01:"Ethernet",
		0x12:"IEE 802.11",
		0x77:"Prism Header",
		0x7F:"WLAN AVS"
	}
	return types[typeData]
def getTagType(type):
	types = {
		0x00: "TAG_PADDING",
		0x01: "TAG_END",
		0x0A: "TAG_RAW_RSSI",
		0x0B: "TAG_SNR",
		0x0C: "TAG_DATA_RATE",
		0x0D: "TAG_TIMESTAMP",
		0X0F: "TAG_CONTENTION_FREE",
		0X10: "TAG_DECRYPTED",
		0X11: "TAG_FCS_ERROR",
		0X12: "TAG_RX_CHANNEL",
		0X28: "TAG_PACKET_COUNT",
		0X29: "TAG_RX_FRAME_LENGTH",
		0X3C: "TAG_WLAN_RADIO_HDR_SERIAL"
	}
	return types[type]
def getEtherType(etherInt):
    types = {
        0x0600 : 'XNS Internet Datagram Protocol',
        0x0800 : 'Internet Protocol version 4 (IPv4)',
        0x0805 : 'X.25 Layer 3',
        0x0806 : 'Address Resolution Protocol (ARP)',
        0x0842 : 'Wake-on-LAN',
        0x08F0 : 'WiMax Mac-to-Mac',
        0x08FF : 'AX.25',
        0x0BAD : 'Vines IP',
        0x0BAF : 'Vines Echo',
        0x0C15 : 'ETHERTYPE_C15_HBEAT',
        0x1984 : 'Netmon Train',
        0x2001 : 'Cisco Group Management Protocol',
        0x22E5 : 'Gigamon Header',
        0x22EA : '802.1Qat Multiple Stream Reservation Protocol',
        0x22F0 : 'IEEE 1722 Audio Video Bridging Transport Protocol',
        0x22F1 : 'Robust Header Compression(RoHC)',
        0x22F3 : 'IETF TRILL Protocol',
        0x22F4 : 'Intermediate System to Intermediate System',
        0x2452 : 'IEEE 802.11 (Centrino promiscuous)',
        0x3C07 : '3Com NBP Datagram',
        0x3E3F : 'EPL_V1',
        0x4742 : 'ETHERTYPE_C15_CH',
        0x6000 : 'DEC proto',
        0x6001 : 'DEC DNA Dump/Load',
        0x6002 : 'DEC DNA Remote Console',
        0x6003 : 'DEC DNA Routing',
        0x6004 : 'DEC LAT',
        0x6005 : 'DEC Diagnostics',
        0x6006 : 'DEC Customer use',
        0x6007 : 'DEC LAVC/SCA',
        0x6558 : 'Transparent Ethernet bridging',
        0x6559 : 'ETHERTYPE_RAW_FR',
        0x8035 : 'Reverse Address Resolution Protocol',
        0x8038 : 'DEC LanBridge',
        0x8041 : 'DEC LAST',
        0x809B : 'AppleTalk (Ethertalk)',
        0x80D5 : 'SNA-over-Ethernet',
        0x80E1 : 'EtherNet/IP Device Level Ring',
        0x80F3 : 'AppleTalk Address Resolution Protocol (AARP)',
        0x8100 : 'VLAN-tagged frame (IEEE 802.1Q) and Shortest Path Bridging IEEE 802.1aq[8]',
        0x8133 : 'Juniper Netscreen Redundant Protocol',
        0x8137 : 'IPX',
        0x814C : 'SNMP over Ethernet, RFC 1089',
        0x80FF : 'Wellfleet Compression Protocol',
        0x8181 : 'Spanning Tree Protocol',
        0x81FD : 'Cabletron Interswitch Message Protocol',
        0x81FF : 'Cabletron SFVLAN 1.8 Tag-Based Flood',
        0x8204 : 'QNX Qnet',
        0x86DD : 'Internet Protocol Version 6 (IPv6)',
        0x872D : 'Cisco Wireless Lan Context Control Protocol',
        0x8783 : 'Motorola Media Independent Network Transport',
        0x8808 : 'Ethernet flow control',
        0x8809 : 'Slow Protocols',
        0x880B : 'ETHERTYPE_PPP',
        0x8819 : 'CobraNet',
        0x8847 : 'MPLS unicast',
        0x8848 : 'MPLS multicast',
        0x885A : 'Foundry proprietary',
        0x8863 : 'PPPoE Discovery Stage',
        0x8864 : 'PPPoE Session Stage',
        0x886C : 'HomePNA, wlan link local tunnel',
        0x886D : 'Intel ANS probe',
        0x886F : 'MS NLB heartbeat',
        0x8870: 'Jumbo Frames (Obsoleted draft-ietf-isis-ext-eth-01)',
        0x887B: 'HomePlug 1.0 MME',
        0x8881 : 'CDMA2000 A10 Unstructured byte stream',
        0x8884 : 'ATM over Ethernet',
        0x888E: 'EAP over LAN (IEEE 802.1X)',
        0x8892: 'PROFINET Protocol',
        0x8899: 'Realtek Layer 2 Protocols',
        0x889A: 'HyperSCSI (SCSI over Ethernet)',
        0x889B: 'CSM_ENCAPS Protocol',
        0x88A1: 'Telkonet powerline',
        0x88A2: 'ATA over Ethernet',
        0x88A4: 'EtherCAT Protocol',
        0x88A8: 'Provider Bridging (IEEE 802.1ad) & Shortest Path Bridging IEEE 802.1aq[8]',
        0x88AB: 'Ethernet Powerlink[citation needed]',
        0x88AD: 'XiMeta Technology',
        0x88AE: 'ETHERTYPE_BRDWALK',
        0x88B4: 'WAI Authentication Protocol',
        0x88B5: 'Local Experimental Ethertype 1',
        0x88B6: 'Local Experimental Ethertype 2',
        0x88B7: 'IEEE 802a OUI Extended Ethertype',
        0x88B8: 'GOOSE (Generic Object Oriented Substation event)',
        0x88B9: 'GSE (Generic Substation Events) Management Services',
        0x88BA: 'SV (Sampled Value Transmission)',
        0x88CA: 'Transparent Inter Process Communication',
        0x88C7: '802.11i Pre-Authentication',
        0x88CC: 'Link Layer Discovery Protocol (LLDP)',
        0x88CD: 'SERCOS III',
        0x88D2: 'CDMA2000 A10 3GPP2 Packet',
        0x88D8: 'Circuit Emulation Services over Ethernet (MEF8)',
        0x88D9: 'Link Layer Topology Discovery (LLTD)',
        0x88DC: '(WAVE) Short Message Protocol (WSM)',
        0x88DE: 'VMware Lab Manager',
        0x88E1: 'HomePlug AV MME[citation needed]',
        0x88E3: 'Media Redundancy Protocol (IEC62439-2)',
        0x88E5: 'MAC security (IEEE 802.1AE)',
        0x88E7: 'Provider Backbone Bridges (PBB) (IEEE 802.1ah)',
        0x88EE: 'Ethernet Local Management Interface (MEF16)',
        0x88F5: 'IEEE 802.1ak Multiple VLAN Registration Protocol',
        0x88F6: '802.1ak Multiple Mac Registration Protocol',
        0x88F7: 'Precision Time Protocol (PTP) over Ethernet (IEEE 1588)',
        0x88F8: 'Network Controller Sideband Interface',
        0x88FB: 'Parallel Redundancy Protocol (PRP)',
        0x8901: 'Flow Layer Internal Protocol',
        0x8902: 'IEEE 802.1ag Connectivity Fault Management (CFM) Protocol / ITU-T Recommendation Y.1731 (OAM)',
        0x8903: 'Data Center Ethernet (DCE) protocol(Cisco)',
        0x8906: 'Fibre Channel over Ethernet (FCoE)',
        0x8909: 'CiscoMetaData',
        0x890d: 'IEEE 802.11 data encapsulation',
        0x8911: 'LINX IPC Protocol',
        0x8914: 'FCoE Initialization Protocol',
        0x8917: 'Media Independent Handover Protocol',
        0x891D: 'TTEthernet Protocol Control Frame',
        0x8926: 'VN-Tag',
        0x892B: 'Schweitzer Engineering Labs Layer 2 Protocol',
        0x892F: 'High-availability Seamless Redundancy (HSR)',
        0x893F: '802.1br Bridge Port Extension E-Tag',
        0x8940: 'ETHERTYPE_ECP Edge Control Protocol',
        0x894F: 'Network Service Header',
        0x9000: 'Ethernet Configuration Testing Protocol[9]',
        0x9021: 'Real-Time Media Access Control',
        0x9022: 'Real-Time Configuration Protocol',
        0x9100: 'VLAN-tagged (IEEE 802.1Q) frame with double tagging',
        0xCAFE: 'Link Layer Topology Discovery (LLTD)',
        0xC0DE: 'eXpressive Internet Protocol',
        0xC0DF: 'Neighborhood Watch Protocol',
        0xD00D: 'Digium TDM over Ethernet Protocol',
        0xFCFC: 'ETHERTYPE_FCFT  used to transport FC frames+MDS hdr internal to Cisco MDS switch',
        0x8915: 'RDMA over Converged Ethernet (RoCE)',
        0x892D: 'bluecom Protocol',
    }
    if etherInt in types:
        return types[etherInt]
    else:
        return "UKNOW PROTOCOL: " + str(etherInt)
def processTag(tag,details=False):
	currentTag = None
	i = 0
	while currentTag not in [0x00, 0x01]:
 		currentTag = ord(tag[i])
		tagType = getTagType(ord(tag[0]))
		tagLength = 0
		if(tagType not in ["TAG_END","TAG_PADDING"]):
			tagLength = ord(tag[1])
		i = i + 1 + tagLength
		if details:
			print "tag type: %r" % tagType
			print "tag length: %r" % tagLength
	return i
def processUdpData(data,addr):
	headers = data[0:4]
        tags = data[4:]
        tagType = getType(ord(headers[1]))
        protocol = ord(headers[2]) * 256 + ord(headers[3])
        protocolStr = getProtocol(protocol)
        tagsLength = processTag(tags)
        #print "tags length: %r" % tagsLength
        eth_header = tags[tagsLength:(14+tagsLength)]
        eth_data = tags[(14+tagsLength):]
        etherType = getEtherType(ord(eth_header[12])*256 + ord(eth_header[13]))
        eth = unpack('!6s6sH' , eth_header)
        eth_protocol = socket.ntohs(eth[2])
        mac_details = 'Destination MAC : ' + eth_addr(eth_header[0:6]) + ' Source MAC : ' + eth_addr(eth_header[6:12]) + ' Protocol : ' + str(eth_protocol)
        packet = tags[15:]
        hexStr = "".join(tags[21:])
        iph = unpack('!BBHHHBBH4s4s',packet[:20])
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
        iph_length = ihl * 4
        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8]);
        d_addr = socket.inet_ntoa(iph[9]);
        connection_detail = ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
	return {"s_addr":s_addr,"d_addr":d_addr,"etherType":etherType,"len":len(eth_data),"connection_detail":connection_detail,"mac_details":mac_details}
def readIpFile(fileName='./ipfile.json'):
    if(os.path.isfile(fileName)):
        with open(fileName,'r') as configFile:
            ipNames = json.load(configFile)
        return ipNames
    else:
        return False
def Average(previusAverage = 0, value = 0, quantity = 1):
	return (float(previusAverage) * (int(quantity)-1) / int(quantity) ) + float(value) / int(quantity)
try:
    consumes = {}
    average_consumes = {}
    average_count = {}
    internal_conections = {}
    statistics = {"protocols":{},"packages_count":{}}
    encoding="utf-8"
    historyEnabled = False
    if "-h" in sys.argv:
            historyEnabled = True
    history_lines = []
    statistics_lines = []
    available = True
    stdscr = curses.initscr()
    ipNames = readIpFile()
    curses.nocbreak(); stdscr.keypad(1); curses.echo();
    curses.curs_set(0)
    stdscr.border(0)
    rows, columns = stdscr.getmaxyx()
    columns -= 2
    maxrows = (rows/2-3)
    consums_panel = curses.newpad((rows -2)/2, (columns -2)/2)
    consums_panel.border(0)
    average_panel = curses.newpad((rows -2)/2, (columns -2)/2)
    average_panel.border(0)
    log_panel = curses.newpad((rows - 2)/2, (columns - 2)/2)
    log_panel.border(0)
    danger_logs = curses.newpad((rows -2)/2, (columns -2)/2)
    danger_logs.border(0)
    log_panel_rows, log_panel_columns = log_panel.getmaxyx()
    log_panel_rows -= 2
    stdscr.refresh()
    consums_panel.refresh(0,0,1,2,rows,columns)
    average_panel.refresh(0,0,1,(columns/2) + 2 ,rows,columns)
    log_panel.refresh(0,0,(rows/2),2,rows+2,columns)
    danger_logs.refresh(0,0,(rows/2),(columns/2) + 2 ,rows+2,columns)
    line = 0
    consum_msg=[]
    average_msg=[]
    internal_conections_msg=[]
    while True:
        data, addr = sock.recvfrom(1024)
        consumesData = processUdpData(data,addr)
        if len(history_lines) > 100000:
            history_lines = history_lines[-1000:]
        history_lines.append(consumesData['connection_detail'].ljust(columns-5))
        if consumesData['etherType'] not in statistics['protocols']:
            statistics['protocols'][consumesData['etherType']] = 0
        statistics['protocols'][consumesData['etherType']] += 1
        timer = math.floor((time.time() % 2.0))
        if "192.168." in str(consumesData['d_addr']) and "192.168." in str(consumesData['s_addr']) and not str(consumesData['s_addr']).endswith(".1")  and not str(consumesData['d_addr']).endswith(".1") and not str(consumesData['d_addr']).endswith(".255") and not str(consumesData['s_addr']).endswith(".255"):
            ipSource = consumesData['s_addr']
            if(ipSource in ipNames):
                ipSource = ipNames[consumesData['s_addr']]
            ipDestination = consumesData['d_addr']
            if(ipDestination in ipNames):
                ipDestination = ipNames[consumesData['d_addr']]
            internalKey = ipSource+ ' to ' + ipDestination
            if internalKey not in internal_conections:
                internal_conections[internalKey] = 0
            internal_conections[internalKey] += 1
        if "192.168." in str(consumesData['d_addr']):
            d_addr = str(consumesData['d_addr'])
            size = consumesData['len']
            if d_addr not in consumes:
                consumes[d_addr] = 0
            consumes[d_addr] += size
        if timer == 1:
           available = True
        if timer == 0 and available == True:
            consum_msg = []
            average_msg = ["Promedio:"]
            internal_conections_msg = ["Conexiones Internas:"]
            for ip,size in sorted(consumes.items(), key=itemgetter(1), reverse=True):
                kbps_size = round((size/4)/1024)*6
                ipLabel = ip
                if(ip in ipNames):
                    ipLabel = ipNames[ip]
                if kbps_size != 0:
                    consum_msg.append(str("IP: " + ipLabel + " - " +  str(round((size/4)/1024)*6).strip() + " kb/s - " + str(size/2)).ljust((columns/2)-7))
                    if ip not in average_count:
                        average_count[ip] = 0
                    if ip not in average_consumes:
                        average_consumes[ip] = 0
                    if kbps_size > 0:
                        average_count[ip] += 1
                        average_consumes[ip] = Average(average_consumes[ip], kbps_size, average_count[ip])
                else:
                    consum_msg.append("".ljust(columns/2-7))
                consumes[ip] = 0
            for ip, average in sorted(average_consumes.items(), key = itemgetter(1), reverse = True):
                ipLabel = ip
                if(ip in ipNames):
                    ipLabel = ipNames[ip]
                if average > 0:
                    average_msg.append(str(ipLabel + " - " + str(round(average)).strip() + " kb/s").ljust((columns/2)-7))
            for label, count in sorted(internal_conections.items(), key = itemgetter(1), reverse = True):
                if count > 0:
                    internal_conections_msg.append(label + " - " + str(count).ljust(10))
            available = False
            j = 1
            for msg in consum_msg[:maxrows]:
                consums_panel.addstr(j,2,msg)
                j+=1
            m=1
            for msg in average_msg[:maxrows]:
                average_panel.addstr(m,2,msg)
                m+=1
            k=1
            for msg in internal_conections_msg[:maxrows]:
                danger_logs.addstr(k,2,msg)
                k+=1
        if historyEnabled:
            h = 1
            for log in history_lines[-(rows/2-3):]:
                log_panel.addstr(h,2,log.ljust(columns/2 - 7))
                h+=1
        else:
            statistics_lines = ["Statistics:"]
            for protocol,count in sorted(statistics['protocols'].items(), key=itemgetter(1), reverse=True):
                statistics_lines.append(protocol + " - uses: " + str(count))
            z = 1
            for msg in statistics_lines[:maxrows]:
                log_panel.addstr(z,2, msg.ljust(columns/2 - 7))
                z += 1
        consums_panel.refresh(0,0,1,2,rows,columns)
        average_panel.refresh(0,0,1,(columns/2) + 2 ,rows,columns)
        log_panel.refresh(0,0,(rows/2),2,rows+2,columns)
        danger_logs.refresh(0,0,(rows/2),(columns/2) + 2 ,rows+2,columns)
finally:
    curses.nocbreak();stdscr.keypad(0);curses.echo();
    curses.endwin()
    print("Bye :D")
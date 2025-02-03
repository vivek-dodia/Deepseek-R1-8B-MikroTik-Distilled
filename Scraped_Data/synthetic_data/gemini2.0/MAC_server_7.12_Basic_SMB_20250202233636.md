## A. MAC Server in MikroTik RouterOS 7.12 (SMB Configuration)

### 1. Configuration Scenario and Requirements

#### Overview
MikroTik's MAC server allows you to manage and track MAC addresses on your network, providing features such as limiting access based on MAC address, tracking devices, and detecting rogue devices.

#### Requirements
- MikroTik RouterBoard with RouterOS 7.12
- DHCP enabled on the network

### 2. Step-by-Step Implementation

#### Enable MAC Server
1. Go to `/ip mac-server` in Winbox.
2. Click on the "Enable" checkbox.

#### Add MAC Addresses
1. Click on the "Add" button.
2. Enter the MAC address in the "Address" field.
3. (Optional) Enter a comment in the "Comment" field.
4. Click "OK" to save the entry.

#### Bind MAC Addresses to IP Addresses
1. Go to `/ip dhcp-server` in Winbox.
2. Select the interface you want to bind MAC addresses to.
3. Click on the "Leases" tab.
4. Click on the "Add" button.
5. Enter the MAC address in the "MAC Address" field.
6. Enter the IP address you want to assign to the device in the "IP Address" field.
7. (Optional) Enter a comment in the "Comment" field.
8. Click "OK" to save the entry.

### 3. Complete Configuration Commands

```
/ip mac-server enable
/ip mac-server settings default-mac-policy=accept
/ip mac-server add address=00:00:5E:00:53:AF
/ip dhcp-server add address=192.168.1.10 mac-address=00:00:5E:00:53:AF
```

### 4. Common Pitfalls and Solutions

- **MAC address not recognized:** Ensure that the MAC address is entered correctly. Remember that MAC addresses are case-sensitive.
- **IP address conflict:** Check if the IP address you are trying to assign is already in use.
- **DHCP binding not working:** Verify that DHCP is enabled on the interface and that the device is requesting an IP address via DHCP.

### 5. Verification and Testing Steps

1. Check that the MAC server is enabled: `/ip mac-server print enabled`
2. Verify that the MAC address is added: `/ip mac-server print address`
3. Test IP address assignment by connecting a device with the MAC address you added.
4. Observe the MAC address in the DHCP lease list: `/ip dhcp-server lease print mac-address`

### 6. Related Features and Considerations

- **MAC scanning:** Use RoMON to scan for MAC addresses on your network.
- **MAC filtering:** Create firewall rules to allow or deny access based on MAC address.
- **MAC table:** View the MAC address table to track active devices on the network.

### 7. MikroTik REST API Examples

#### Create a MAC Server Entry
```
POST /api/ip/mac-server
{
  "address": "00:00:5E:00:53:AF"
}
```

#### Get MAC Server Entries
```
GET /api/ip/mac-server
```

#### Delete a MAC Server Entry
```
DELETE /api/ip/mac-server/00:00:5E:00:53:AF
```

### 8. Comprehensive Examples and Explanations

**8.1 IP Addressing**

- IPv4: `/ip address add address=192.168.1.1/24 interface=ether1`
- IPv6: `/ip address add address=2001:db8::1/64 interface=ether1`

**8.2 IP Pools**

- Create a DHCP pool: `/ip pool add name=MyPool ranges=192.168.1.10-192.168.1.20`

**8.3 IP Routing**

- Add a static route: `/ip route add dst-address=10.0.0.0/24 gateway=192.168.1.1`

**8.4 IP Settings**

- Set the DNS server: `/ip settings set dns-server=8.8.8.8`

**8.5 RoMON**

- Start a MAC scan: `romon mac scan interface=ether1`

**8.6 WinBox**

- Use WinBox to manage RouterOS remotely over the network.

**8.7 Certificates**

- Generate a self-signed certificate: `/certificate generate name=MyCert key-size=2048 ca=yes`

**8.8 PPP AAA**

- Configure PPP AAA for user authentication: `/ppp aaa add name=MyAAA server=192.168.1.1`

**8.9 RADIUS**

- Add a RADIUS server: `/radius add name=MyRADIUS server=192.168.1.1 secret=mysecret`

**8.10 User / User Groups**

- Create a user: `/user add name=user1 password=mypassword`

**8.11 Bridging and Switching**

- Create a bridge: `/bridge add name=MyBridge`

**8.12 MACVLAN**

- Configure MACVLAN: `/interface macvlan add name=MyMACVLAN interface=ether1 vlan-id=10`

**8.13 L3 Hardware Offloading**

- Enable L3 hardware offloading: `/interface set ether1 l3-hardware-offloading=on`

**8.14 MACsec**

- Configure MACsec: `/interface macsec add name=MyMACsec interface=ether1 macsec-key=mykey`

**8.15 Quality of Service**

- Create a queue: `/queue type=simple name=MyQueue target=ether1 packet-mark=1`

**8.16 Switch Chip Features**

- Configure port mirroring: `/interface switch port mirroring add destination=ether2 source=ether1`

**8.17 VLAN**

- Create a VLAN: `/vlan add name=MyVLAN vlan-id=10 interface=ether1`

**8.18 VXLAN**

- Configure VXLAN: `/interface vxlan add name=MyVXLAN remote-ip=192.168.1.10 local-ip=192.168.1.1 local-port=4789 remote-port=4789`

**8.19 Firewall and Quality of Service**

- Create a firewall rule: `/ip firewall add action=drop chain=input src-address=192.168.1.10`

**8.20 IP Services**

- Enable DHCP server: `/ip dhcp-server add interface=ether1 address-pool=MyPool`
- Enable DNS server: `/ip dns add listen-address=192.168.1.1`

**8.21 High Availability Solutions**

- Configure bonding: `/interface bonding add name=MyBond interfaces=ether1,ether2`

**8.22 Mobile Networking**

- Configure LTE interface: `/interface lte add name=MyLTE apn=myapn`

**8.23 Multi Protocol Label Switching - MPLS**

- Configure MPLS: `/mpls ldp add interface=ether1`

**8.24 Network Management**

- Enable SNMP: `/snmp enable`

**8.25 Routing**

- Configure OSPF: `/routing ospf add process=MyOSPF interface=ether1 area=0.0.0.0`

**8.26 System Information and Utilities**

- Get system information: `/system resource print`

**8.27 Virtual Private Networks**

- Configure WireGuard: `/interface wireguard add name=MyWireGuard private-key=myprivatekey`

**8.28 Wired Connections**

- Configure PoE-Out: `/interface set ether1 poe-out=active`

**8.29 Diagnostics, monitoring and troubleshooting**

- Enable flow monitoring: `/interface monitor-traffic add interface=ether1 target=file name=mytraffic.pcap`

**8.30 Extended features**

- Create a Container: `/container add os=linux name=MyContainer`
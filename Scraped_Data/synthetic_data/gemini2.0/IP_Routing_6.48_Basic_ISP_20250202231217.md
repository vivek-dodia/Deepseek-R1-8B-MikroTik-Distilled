## IP Routing for ISPs in MikroTik RouterOS 6.48

### IP Addressing (IPv4 and IPv6)

**Configuration Scenario:** Configure IPv4 and IPv6 addresses on an ISP router.

**Steps:**

1. Navigate to **IP > Addresses**
2. **Add New**
3. Select **Interface:** Ethernet or VLAN
4. Enter **IP Address** and **Prefix Length**
5. Check **DHCP Server** or **Address Override** for IPv6
6. Repeat for other interfaces

**Complete Configuration Commands:**

```
/ip address add interface=ether1 address=10.0.0.1/24
/ip address add interface=vlan10 address=192.168.10.1/24
/ip address add interface=ether2 address=2001:db8:1::1/64
/ip address add interface=vlan20 address=2001:db8:2::1/64 dhcp-server=yes
/ip address add interface=ether3 address=fd00::/64
```

### IP Pools

**Configuration Scenario:** Create IP pools for dynamic IP assignment.

**Steps:**

1. Navigate to **IP > Pool**
2. **Add New**
3. Enter **Name** and **Range**
4. Check **DHCP Server** and **DNS Server**
5. Configure **Lease Time** and **Other Routes**

**Complete Configuration Commands:**

```
/ip pool add name=internal-pool ranges=10.0.0.10-10.0.0.254
/ip pool set internal-pool dhcp-server=yes
/ip pool set internal-pool lease-time=24h
/ip pool set internal-pool other-routes=0.0.0.0/0
```

### IP Routing

**Configuration Scenario:** Configure IP routing on an ISP router.

**Steps:**

1. Navigate to **IP > Routes**
2. **Add New**
3. Enter **Destination**, **Gateway**, and **Distance**
4. Check **Check Gateway** to verify reachability
5. Configure **Scope** and **Routing Table**

**Complete Configuration Commands:**

```
/ip route add dst-address=0.0.0.0/0 gateway=10.1.1.1 distance=10
/ip route add dst-address=2001:db8::/32 gateway=2001:db8:1::1 distance=10
/ip route add dst-address=fd00::/128 gateway=fd01::1 distance=10
```

### IP Settings

**Configuration Scenario:** Modify advanced IP settings.

**Steps:**

1. Navigate to **IP > Settings**
2. Configure **IP Forwarding**: enables packet forwarding
3. Configure **Accept Redirect**: allows redirects from other routers
4. Configure **Assume Unsolicited Inbound**: handles unsolicited inbound connections

**Complete Configuration Commands:**

```
/ip settings set ip-forward=yes
/ip settings set accept-redirect=yes
/ip settings set assume-unsolicited-inbound=yes
```

### MAC Server

**Configuration Scenario:** Configure a MAC server for network device identification.

**Steps:**

1. Navigate to **IP > MAC Server**
2. **Add New**
3. Enter **Name** and **MAC Address**
4. Configure **Interface**, **DHCP Options**, and **VLAN ID**
5. Check **Static** for permanent entries

**Complete Configuration Commands:**

```
/ip mac-server add name=server1 mac-address=00:11:22:33:44:55
/ip mac-server set server1 dhcp-set-name=internal-dhcp
/ip mac-server set server1 vlan-id=10
```

### RoMON

**Configuration Scenario:** Enable Remote Monitoring (RoMON) for remote access.

**Steps:**

1. Navigate to **System > RoMON**
2. Enable **In** and **Web**
3. Configure **Port**, **Password**, and **Policy**
4. Restart RouterOS to apply changes

**Complete Configuration Commands:**

```
/system romon set enabled-in=yes
/system romon set enabled-web=yes
/system romon set port=8291
/system romon set password=mypassword
/system romon set policy=updated-full
```

### WinBox

**Configuration Scenario:** Enable WinBox tool access for remote management.

**Steps:**

1. Navigate to **Tools > WinBox**
2. Enable **Enable**
3. Configure **Port** and **Firewall Policy**

**Complete Configuration Commands:**

```
/tool winbox set enabled=yes
/tool winbox set port=8292
/tool winbox set policy=routed
```

### Certificates

**Configuration Scenario:** Configure SSL/TLS certificates for secure connections.

**Steps:**

1. Navigate to **System > Certificates**
2. **Import** or **Create New**
3. Enter **Name**, **Certificate Content**, and **Key Content**
4. Configure **Key Usage** and **Validity**

**Complete Configuration Commands:**

```
/certificate import file-name=server-certificate.pem
/certificate import file-name=server-key.pem
/certificate import file-name=client-certificate.pem
```

### PPP AAA

**Configuration Scenario:** Configure authentication, authorization, and accounting (AAA) for PPP connections.

**Steps:**

1. Navigate to **PPP > AAA**
2. **Add New**
3. Select **Service**
4. Configure **User**, **Password**, and **Profile**
5. Check **Enabled** and **Auto Reconnect**

**Complete Configuration Commands:**

```
/ppp aaa add service=pppoe secret=mypassword profile=default
/ppp aaa set pppoe enabled=yes auto-reconnect=yes
```

### RADIUS

**Configuration Scenario:** Use RADIUS server for user authentication and authorization.

**Steps:**

1. Navigate to **RADIUS**
2. Configure **Server Address**, **Port**, and **Shared Secret**
3. Configure **Timeout** and **Retry Intervals**
4. Check **Enabled**

**Complete Configuration Commands:**

```
/radius add server=10.1.1.1 port=1812 shared-secret=mysecret
/radius set server=10.1.1.1 timeout=5 retry-interval=3
/radius set enabled=yes
```

### User / User Groups

**Configuration Scenario:** Create user accounts and groups for access control.

**Steps:**

1. Navigate to **User Manager**
2. **Add New** User or Group
3. Enter **Username** and **Password**
4. Assign **Role** and **Permissions**

**Complete Configuration Commands:**

```
/user add name=admin password=mypassword
/group add name=admins
/user add name=user1 password=mypassword group=admins
```

### Bridging and Switching

**Configuration Scenario:** Configure bridging and switching features for layer 2 traffic management.

**Steps:**

1. Navigate to **Bridge**
2. **Add New**
3. Select **Ports**
4. Configure **Protocol Mode** (STP, RSTP, or MSTP)
5. Check **Learning** and **Forwarding**

**Complete Configuration Commands:**

```
/bridge add name=bridge1 ports=eth1 eth2
/bridge set bridge1 protocol-mode=rstp learning=yes forwarding=yes
```

### MACVLAN

**Configuration Scenario:** Create a MACVLAN interface to isolate virtual network traffic.

**Steps:**

1. Navigate to **Interface**
2. **Add New**
3. Select **Type** as MACVLAN
4. Configure **Parent** interface and **MAC Address**
5. Assign **IPv4/IPv6 Addresses**

**Complete Configuration Commands:**

```
/interface macvlan add name=macvlan1 mac-address=00:11:22:33:44:55 parent=ether1
/ip address add interface=macvlan1 address=10.10.10.1/24
```

### L3 Hardware Offloading

**Configuration Scenario:** Offload routing decisions to hardware for improved performance.

**Steps:**

1. Navigate to **IP > Offloading**
2. Check **Enable**
3. Configure **Queue Type** and **Interface**
4. Select **Offload Method** (FW4, IPV4, IPSEC, PPPOE)

**Complete Configuration Commands:**

```
/ip offload set enable=yes queue-type=classify
/ip offload set offload-method=ipv4
/ip offload add hardware-interface=ether1 offload-method=ipv4
```

### MACsec

**Configuration Scenario:** Enable Media Access Control security (MACsec) for data encryption.

**Steps:**

1. Navigate to **MACsec**
2. **Add New**
3. Select **Interface**
4. Configure **Cipher Suite** and **Key**
5. Check **Enable**

**Complete Configuration Commands:**

```
/macsec add interface
## IP Settings

### IP Addressing (IPv4 and IPv6)

**Configuration:**

```
/ip address add address=192.168.1.2/24 interface=ether1
/ip address add address=2001:db8::1/64 interface=ether1
```

**Explanation:**

- `/ip address add` is used to assign an IP address to an interface.
- `address` specifies the IP address to be assigned.
- `interface` specifies the interface to which the IP address is assigned.

### IP Pools

**Configuration:**

```
/ip pool add name=pool1 ranges=192.168.1.10-192.168.1.20
/ip dhcp-server add address-pool=pool1 interface=ether1
```

**Explanation:**

- `/ip pool add` creates an IP pool.
- `name` specifies the name of the pool.
- `ranges` specifies the range of IP addresses in the pool.
- `/ip dhcp-server add` adds a DHCP server to an interface and assigns the specified IP pool to it.

### IP Routing

**Configuration:**

```
/ip route add dst-address=192.168.2.0/24 gateway=192.168.1.1
/ip route add dst-address=2001:db8::200/64 gateway=2001:db8::100
```

**Explanation:**

- `/ip route add` is used to add a routing entry to the routing table.
- `dst-address` specifies the destination address of the routing entry.
- `gateway` specifies the gateway address for the routing entry.

### MAC Server

**Configuration:**

```
/ip dhcp-server lease add address=192.168.1.10 mac-address=00:11:22:33:44:55
```

**Explanation:**

- `/ip dhcp-server lease add` creates a static DHCP lease for a specified MAC address.
- `address` specifies the IP address to be assigned to the specified MAC address.
- `mac-address` specifies the MAC address to which the IP address is assigned.

### RoMON

**Configuration:**

```
/system romon-monitor set address=192.168.1.1 port=8291
```

**Explanation:**

- `/system romon-monitor set` configures the RoMON (read-only memory) monitor.
- `address` specifies the IP address of the device running RoMON.
- `port` specifies the port on which RoMON is listening for incoming connections.

### WinBox

**Configuration:**

```
winbox default-port=8292
```

**Explanation:**

- `winbox default-port` sets the default port for WinBox, a GUI management tool for MikroTik devices.

### Certificates

**Configuration:**

```
/certificate import file-name=certificate.crt certificate-name=mycert
```

**Explanation:**

- `/certificate import` imports an X.509 certificate from a file.
- `file-name` specifies the path to the certificate file.
- `certificate-name` specifies the name to be assigned to the certificate.

### PPP AAA

**Configuration:**

```
/ppp aaa set enabled=yes
/ppp aaa set group=mygroup
/ppp aaa set secret=mysecret
```

**Explanation:**

- `/ppp aaa set` configures PPP authentication, authorization, and accounting (AAA).
- `enabled` enables PPP AAA.
- `group` specifies the AAA group to be used for authentication.
- `secret` specifies the secret password for authentication.

### RADIUS

**Configuration:**

```
/radius add server=192.168.1.1 secret=mysecret ports=[1812...1813]
```

**Explanation:**

- `/radius add` adds a RADIUS server to the configuration.
- `server` specifies the IP address of the RADIUS server.
- `secret` specifies the shared secret between the MikroTik device and the RADIUS server.
- `ports` specifies the range of UDP ports to be used for RADIUS communication.

### User / User Groups

**Configuration:**

```
/user add name=myuser password=mypassword group=admins
/user group add name=admins add-member=myuser
```

**Explanation:**

- `/user add` creates a user account.
- `name` specifies the username.
- `password` specifies the user's password.
- `group` specifies the group to which the user belongs.
- `/user group add` creates a user group.
- `name` specifies the name of the group.
- `add-member` adds a user to the group.

### Bridging and Switching

**Configuration:**

```
/bridge add name=mybridge
/interface ethernet add name=ether2 bridge=mybridge
```

**Explanation:**

- `/bridge add` creates a bridge.
- `name` specifies the name of the bridge.
- `/interface ethernet add` adds an Ethernet interface to the specified bridge.

### MACVLAN

**Configuration:**

```
/interface macvlan add name=mymacvlan parent=ether1 vlan=10
```

**Explanation:**

- `/interface macvlan add` creates a MACVLAN interface.
- `name` specifies the name of the MACVLAN interface.
- `parent` specifies the parent interface for the MACVLAN interface.
- `vlan` specifies the VLAN ID for the MACVLAN interface.

### L3 Hardware Offloading

**Configuration:**

```
/interface ethernet set offload=rx
```

**Explanation:**

- `/interface ethernet set` configures various options for an Ethernet interface.
- `offload` sets the hardware offload options for the interface.
- `rx` enables hardware offloading for incoming traffic only.

### MACsec

**Configuration:**

```
/interface macsec set name=ether1 mode=strict
```

**Explanation:**

- `/interface macsec set` configures MACsec (MAC Security) for an interface.
- `name` specifies the name of the interface to be configured for MACsec.
- `mode` sets the MACsec mode.
- `strict` enforces MACsec protection for all traffic on the interface.

### Quality of Service

**Configuration:**

```
/queue simple add name=myqueue max-limit=1mb/s
/interface ethernet set queue=myqueue
```

**Explanation:**

- `/queue simple add` creates a simple queue.
- `name` specifies the name of the queue.
- `max-limit` specifies the maximum bandwidth limit for the queue.
- `/interface ethernet set` assigns the specified queue to an interface.

### Switch Chip Features

**Configuration:**

```
/switch chip feature pppoe-server add name=pppoe
```

**Explanation:**

- `/switch chip feature` configures various features for the switch chip.
- `pppoe-server` adds a PPPoE server feature to the switch chip.

### VLAN

**Configuration:**

```
/interface vlan add name=myvlan vlan-id=10
```

**Explanation:**

- `/interface vlan add` creates a VLAN interface.
- `name` specifies the name of the VLAN interface.
- `vlan-id` specifies the VLAN ID for the VLAN interface.

### VXLAN

**Configuration:**

```
/interface vxlan add name=myvxlan id=1000 src-address=192.168.1.101 dmac-address=01:02:03:04:05:06
```

**Explanation:**

- `/interface vxlan add` creates a VXLAN (Virtual eXtensible Local Area Network) interface.
- `name` specifies the name of the VXLAN interface.
- `id` specifies the VXLAN network identifier (VNI).
- `src-address` specifies the source IP address for the VXLAN interface.
- `dmac-address` specifies the multicast MAC address for the VXLAN interface.

### Firewall and Quality of Service

#### Connection Tracking

**Configuration:**

```
/ip firewall connection-tracking set conntrack-aging-timeout=600
```

**Explanation:**

- `/ip firewall connection-tracking set` configures various options for connection tracking.
- `conntrack-aging-timeout` sets the timeout (in seconds) for idle TCP connections.

#### Firewall

**Configuration:**

```
/ip firewall filter add action=drop in-interface=ether1 dst-address=192.168.1.0/24
```

**Explanation:**

- `/ip firewall filter add` adds a firewall rule.
- `action` specifies the action to be taken when a packet matches the rule.
- `in-interface` specifies the input interface for the rule.
- `dst-address` specifies the destination address for the rule.

#### Packet Flow in RouterOS

**Configuration:**

```
/system scheduler print
```

**Explanation:**

- `/system scheduler print
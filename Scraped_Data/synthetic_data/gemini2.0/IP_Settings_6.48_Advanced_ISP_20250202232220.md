## IP Settings

### IP Addressing

**IPv4 Configuration**

- Add an IPv4 address to an interface: `/ip address add address=<IPv4 address> interface=<interface name>`
- Example: `/ip address add address=192.168.1.1/24 interface=ether1`

- Remove an IPv4 address from an interface: `/ip address remove address=<IPv4 address> interface=<interface name>`
- Example: `/ip address remove address=192.168.1.2/24 interface=ether2`

- Set the default gateway: `/ip route add gateway=<gateway IP>`
- Example: `/ip route add gateway=192.168.1.254`

**IPv6 Configuration**

- Add an IPv6 address to an interface: `/ip address add address=<IPv6 address> interface=<interface name>`
- Example: `/ip address add address=2001:db8:85a3:08d3:1319:8a2e:0370:7334/64 interface=ether1`

- Remove an IPv6 address from an interface: `/ip address remove address=<IPv6 address> interface=<interface name>`
- Example: `/ip address remove address=2001:db8:85a3:08d3:1319:8a2e:0370:7335/64 interface=ether2`

- Set the default gateway: `/ip route add gateway=<gateway IP>`
- Example: `/ip route add gateway=2001:db8:85a3:08d3:1319:8a2e:0370:7334`

### IP Pools

- Create an IP pool: `/ip pool add name=<pool name> ranges=<IPv4/IPv6 range>`
- Example: `/ip pool add name=dhcp-pool ranges=192.168.1.100-192.168.1.200`

- Assign an IP pool to an interface: `/ip dhcp-server add interface=<interface name> address-pool=<pool name>`
- Example: `/ip dhcp-server add interface=ether1 address-pool=dhcp-pool`

### IP Routing

- Add a static route: `/ip route add dst-address=<destination network> gateway=<gateway IP>`
- Example: `/ip route add dst-address=10.0.0.0/24 gateway=192.168.1.254`

- Remove a static route: `/ip route remove dst-address=<destination network> gateway=<gateway IP>`
- Example: `/ip route remove dst-address=10.0.0.0/24 gateway=192.168.1.254`

### IP Settings

- Set the MTU: `/ip settings set mtu=<value>`
- Example: `/ip settings set mtu=1500`

- Enable IPv6 Neighbor Discovery: `/ip settings set nd-ra-interval=<interval>`
- Example: `/ip settings set nd-ra-interval=120`

### MAC Server

- Add a static MAC entry: `/ip arp add mac-address=<mac address> address=<IPv4 address>`
- Example: `/ip arp add mac-address=00:11:22:33:44:55 address=192.168.1.100`

- Remove a static MAC entry: `/ip arp remove mac-address=<mac address>`
- Example: `/ip arp remove mac-address=00:11:22:33:44:55`

### RoMON

- Enable RoMON: `/system romon enable`
- Set RoMON password: `/system romon set-password=<password>`

### WinBox

- Set the WinBox port: `/system winbox port=<port number>`
- Example: `/system winbox port=8291`

- Set the WinBox username and password: `/system identity set name=<username> password=<password>`
- Example: `/system identity set name=admin password=secret`

### Certificates

- Import a certificate: `/certificate import file-name=<path to certificate file>`

- Create a certificate signing request: `/certificate generate-request common-name=<common name>`

- Sign the certificate signing request: `/certificate sign-request certificate-request-filename=<path to CSR file>`

### PPP AAA

- Create a PPP user: `/ppp secret add name=<username> password=<password> profile=<profile name>`
- Example: `/ppp secret add name=user1 password=secret profile=default`

- Set the PPP user's IP address range: `/ppp secret set name=<username> profile=<profile name> local-address=<IP range>`
- Example: `/ppp secret set name=user1 profile=default local-address=10.0.0.10-10.0.0.20`

### RADIUS

- Create a RADIUS server: `/radius add server=<server IP> secret=<password>`
- Example: `/radius add server=10.0.0.1 secret=secret`

- Configure a PPP profile to use RADIUS authentication: `/ppp profile set name=<profile name> authentication=[pap|chap|mschap2] use-radius=yes radius-server=<server IP>`
- Example: `/ppp profile set name=default authentication=mschap2 use-radius=yes radius-server=10.0.0.1`

### User / User Groups

- Create a user: `/user add name=<username> password=<password>`
- Example: `/user add name=user1 password=secret`

- Create a user group: `/user group add name=<group name>`
- Example: `/user group add name=group1`

- Add a user to a group: `/user add user=<username> group=<group name>`
- Example: `/user add user=user1 group=group1`

### Bridging and Switching

- Create a bridge: `/bridge add name=<bridge name>`
- Example: `/bridge add name=bridge1`

- Add an interface to a bridge: `/interface bridge add interface=<interface name> bridge=<bridge name>`
- Example: `/interface bridge add interface=ether1 bridge=bridge1`

- Remove an interface from a bridge: `/interface bridge remove interface=<interface name> bridge=<bridge name>`
- Example: `/interface bridge remove interface=ether2 bridge=bridge1`

### MACVLAN

- Create a MACVLAN interface: `/interface mac-vlan add mac-address=<parent MAC address> interface=<parent interface name>`
- Example: `/interface mac-vlan add mac-address=00:11:22:33:44:55 interface=ether1`

- Set the MACVLAN interface's IP address: `/ip address add address=<IPv4 address> interface=<MACVLAN interface name>`
- Example: `/ip address add address=192.168.1.100/24 interface=mac-vlan1`

### L3 Hardware Offloading

- Enable L3 hardware offloading: `/ip offload ether1 enable`

### MACsec

- Create a MACsec interface: `/interface macsec add name=<interface name> rx-sa-index=<SA index> tx-sa-index=<SA index>`
- Example: `/interface macsec add name=eth
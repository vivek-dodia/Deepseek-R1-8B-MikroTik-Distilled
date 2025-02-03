## Layer 3 Routing on MikroTik RouterOS 6.48

### Configuration Scenario and Requirements

- Enable static and dynamic routing protocols on the router.
- Implement NAT for internet access using a public IP address.
- Configure access and trunk ports for client devices and inter-VLAN routing.

### Step-by-Step Implementation

#### 1. Enable Routing Protocols

- **Static Routing:**
  - Create a static route to a remote network:
    ```
    /ip route add dst-address=192.168.10.0/24 gateway=192.168.1.2
    ```
- **RIPng Routing:**
  - Enable RIPng for IPv6 routing:
    ```
    /ipv6 route ripng enable
    ```
  - Add a RIPng route to a remote IPv6 network:
    ```
    /ipv6 route add dst-address=2001:db8::/64 gateway=2001:db8:1::1
    ```

#### 2. Configure NAT

- Create a masquerade rule for outbound internet access:
  ```
  /ip firewall nat add chain=srcnat action=masquerade out-interface=ether1
  ```
- Add a public IP address to the masquerade rule:
  ```
  /ip firewall nat set [masquerade rule number] public-address=10.0.0.1
  ```

#### 3. Configure Access and Trunk Ports

- **Access Port:**
  - Create an access port for client devices:
    ```
    /interface bridge port add bridge=bridge1 interface=ether2
    ```
- **Trunk Port:**
  - Create a trunk port for inter-VLAN communication:
    ```
    /interface bridge port add bridge=bridge1 interface=ether3 trunk-ports=add all
    ```
  - Add VLANs to the trunk port:
    ```
    /interface bridge port set [trunk port number] vlan-filtering=add vlan1
    ```

#### 4. Enable VLANs

- Create a VLAN interface for VLAN 1:
  ```
  /interface vlan add interface=ether3 vlan-id=1
  ```
- Configure an IP address on the VLAN interface:
  ```
  /ip address add address=192.168.101.1/24 interface=vlan1
  ```

### Complete Configuration Commands

```
/ip route add dst-address=192.168.10.0/24 gateway=192.168.1.2
/ipv6 route ripng enable
/ipv6 route add dst-address=2001:db8::/64 gateway=2001:db8:1::1
/ip firewall nat add chain=srcnat action=masquerade out-interface=ether1
/ip firewall nat set [masquerade rule number] public-address=10.0.0.1
/interface bridge port add bridge=bridge1 interface=ether2
/interface bridge port add bridge=bridge1 interface=ether3 trunk-ports=add all
/interface bridge port set [trunk port number] vlan-filtering=add vlan1
/interface vlan add interface=ether3 vlan-id=1
/ip address add address=192.168.101.1/24 interface=vlan1
```

### Common Pitfalls and Solutions

- **No Internet Access:**
  - Verify that the masquerade rule is active and that the public IP address is correct.
- **VLAN Communication Issues:**
  - Ensure that the trunk port is configured correctly and that the VLAN IDs match on both sides.
- **Static Route Not Working:**
  - Check if the destination network is reachable via other routes or if the gateway IP address is correct.

### Verification and Testing Steps

- Ping the remote network from the router to verify static route connectivity.
- Test internet connectivity by accessing websites or performing a trace route.
- Configure a test device on VLAN 1 and verify connectivity to the VLAN and the internet.

### Related Features and Considerations

- **DHCP Server:**
  - Configure a DHCP server on the router to assign IP addresses to client devices.
- **Firewall Rules:**
  - Implement firewall rules to control access to specific networks or services.
- **Security Best Practices:**
  - Use strong passwords for all administrative accounts.
  - Disable unused services and ports to reduce the attack surface.
## IPv4 Addressing

### Configuration Scenario and Requirements

- Configure IPv4 addresses for multiple interfaces on a MikroTik RouterOS 7.11 router.

### Step-by-Step Implementation

1. **Connect to the router via WinBox or other management tool.**
2. **Go to the "IP" menu and select "Addresses".**
3. **Click on the "+" button to create a new IPv4 address.**
4. **Enter the desired IP address, subnet mask, and interface in the "Address", "Network", and "Interface" fields, respectively.**
5. **Click on the "Apply" button to save the changes.**

### Complete Configuration Commands

```
/ip address add address=192.168.1.1/24 interface=ether1
/ip address add address=192.168.2.1/24 interface=ether2
```

### Common Pitfalls and Solutions

- **Incorrect subnet mask:** Ensure that the subnet mask is specified correctly. An incorrect subnet mask can lead to network connectivity issues.
- **Duplicate IP addresses:** Avoid assigning the same IP address to multiple interfaces. This can cause IP address conflicts and network issues.

### Verification and Testing Steps

- **Ping the assigned IP addresses from another device on the network.**
- **Use the "ip address print" command to verify the configured IP addresses.**

### Related Features and Considerations

- **IP pools:** IP pools can be used to automatically assign IP addresses to devices on the network.
- **DHCP server:** A DHCP server can be configured to automatically assign IP addresses to devices on the network.
- **NAT:** Network address translation (NAT) can be used to translate private IP addresses to public IP addresses.

## IPv6 Addressing

### Configuration Scenario and Requirements

- Configure IPv6 addresses for multiple interfaces on a MikroTik RouterOS 7.11 router.

### Step-by-Step Implementation

1. **Connect to the router via WinBox or other management tool.**
2. **Go to the "IP" menu and select "Addresses".**
3. **Click on the "+" button to create a new IPv6 address.**
4. **Enter the desired IPv6 address and prefix length in the "Address" and "Prefix" fields, respectively.**
5. **Select the desired interface in the "Interface" field.**
6. **Click on the "Apply" button to save the changes.**

### Complete Configuration Commands

```
/ip address add address=2001:db8::1/64 interface=ether1
/ip address add address=2001:db8::2/64 interface=ether2
```

### Common Pitfalls and Solutions

- **Incorrect prefix length:** Ensure that the prefix length is specified correctly. An incorrect prefix length can lead to network connectivity issues.
- **Duplicate IPv6 addresses:** Avoid assigning the same IPv6 address to multiple interfaces. This can cause IP address conflicts and network issues.

### Verification and Testing Steps

- **Ping the assigned IPv6 addresses from another device on the network.**
- **Use the "ip address print" command to verify the configured IPv6 addresses.**

### Related Features and Considerations

- **IPv6 Neighbor Discovery:** Neighbor discovery is a protocol that allows IPv6 devices to automatically discover each other on the network.
- **IPv6 routing:** IPv6 routing can be configured to allow devices on the network to communicate with each other over IPv6.
- **DHCPv6:** DHCPv6 is a protocol that can be used to automatically assign IPv6 addresses to devices on the network.
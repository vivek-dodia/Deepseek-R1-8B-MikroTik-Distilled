## Layer3 Routing in RouterOS 6.48

### Configuration Scenario and Requirements

**Goal:** Configure Layer3 routing on a MikroTik router for an enterprise network with complex routing requirements.

**Requirements:**

- MikroTik router running RouterOS 6.48 or later
- Knowledge of IP addressing and routing protocols
- Network diagram and IP addressing scheme

### Step-by-Step Implementation

**1. Configure IP Addresses**

* Assign IP addresses to the router's interfaces:
```
/ip address add address=10.0.0.1/24 interface=ether1
/ip address add address=192.168.1.1/24 interface=ether2
```

**2. Enable Routing**

* Enable IP forwarding on the router:
```
/ip firewall enable forwarding=yes
```

**3. Configure Static Routes**

* Add static routes to specific networks:
```
/ip route add dst-address=172.16.0.0/24 gateway=10.0.0.254
/ip route add dst-address=default gateway=192.168.1.254
```

**4. Configure Dynamic Routing Protocols (Optional)**

* If needed, enable and configure dynamic routing protocols such as OSPF or BGP.

**5. Enable Traffic Shapers**

* To control bandwidth allocation, configure traffic shapers on specific interfaces:
```
/queue simple add name=ether1-tx interface=ether1 target=ingress max-limit=10000000
/queue simple add name=ether2-tx interface=ether2 target=ingress max-limit=20000000
```

**6. Implement Security Measures**

* Configure firewall rules to restrict access to the router and protect against unauthorized traffic:
```
/ip firewall filter add chain=input action=drop src-address=unknown
/ip firewall filter add chain=output action=accept
```

**7. Configure DNS and DHCP (Optional)**

* If needed, configure DNS and DHCP services on the router:
```
/ip dns set allow-remote-requests=yes
/ip dhcp-server add interface=ether2 address-pool=default range=192.168.1.10-192.168.1.250
```

### Complete Configuration Commands

```
# Configure IP addresses
/ip address add address=10.0.0.1/24 interface=ether1
/ip address add address=192.168.1.1/24 interface=ether2

# Enable routing
/ip firewall enable forwarding=yes

# Configure static routes
/ip route add dst-address=172.16.0.0/24 gateway=10.0.0.254
/ip route add dst-address=default gateway=192.168.1.254

# Configure traffic shapers
/queue simple add name=ether1-tx interface=ether1 target=ingress max-limit=10000000
/queue simple add name=ether2-tx interface=ether2 target=ingress max-limit=20000000

# Implement security measures
/ip firewall filter add chain=input action=drop src-address=unknown
/ip firewall filter add chain=output action=accept

# Configure DNS and DHCP (Optional)
/ip dns set allow-remote-requests=yes
/ip dhcp-server add interface=ether2 address-pool=default range=192.168.1.10-192.168.1.250
```

### Common Pitfalls and Solutions

- **Incorrect IP Addressing:** Ensure that IP addresses and subnet masks are configured correctly.
- **Disabled Routing:** Verify that IP forwarding is enabled in the firewall settings.
- **Misconfigured Static Routes:** Check the destination address and gateway settings of static routes.
- **Conflicting Firewall Rules:** Review firewall rules to avoid blocking legitimate traffic.
- **Improper Traffic Shaper Configuration:** Adjust traffic shaper limits to suit your bandwidth requirements.

### Verification and Testing Steps

1. Ping from a host on the network to verify connectivity.
2. Use the "route print" command to check the routing table.
3. Run "ip firewall filter print" to confirm the firewall rules.
4. Test bandwidth allocation using tools like iperf or wrk.

### Related Features and Considerations

* **Virtual Routing and Forwarding (VRF):** For advanced routing scenarios, consider using VRFs to isolate routing domains.
* **PPPoE Server:** Configure PPPoE if you need to provide dial-up internet access.
* **NAT:** Implement NAT (Network Address Translation) to allow internal devices to access the internet.
* **DHCP Relay:** Enable DHCP relay to forward DHCP requests to a centralized server.
* **Security Best Practices:** Regularly update RouterOS and implement strong passwords to protect against vulnerabilities.
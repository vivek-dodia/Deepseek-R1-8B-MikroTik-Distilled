# MikroTik RouterOS Documentation: IP Addressing (IPv4 and IPv6)

## **Introduction**
This documentation provides a comprehensive guide to configuring and managing IP addressing (IPv4 and IPv6) on MikroTik RouterOS version 6.x for a Small Office/Home Office (SOHO) network. It includes both Command Line Interface (CLI) and API examples for basic configurations.

---

## **1. IPv4 Addressing**

### **1.1 Assigning IPv4 Addresses to Interfaces**
To assign an IPv4 address to an interface, use the `/ip address` menu.

#### **CLI Example:**
```bash
/ip address add address=192.168.1.1/24 interface=ether1
```
- `address=192.168.1.1/24`: Specifies the IP address and subnet mask.
- `interface=ether1`: Specifies the interface to which the IP address is assigned.

#### **API Example:**
```bash
/ip/address/add
=address=192.168.1.1/24
=interface=ether1
```

---

### **1.2 Viewing IPv4 Addresses**
To view the list of configured IPv4 addresses:

#### **CLI Example:**
```bash
/ip address print
```

#### **API Example:**
```bash
/ip/address/print
```

---

### **1.3 Removing an IPv4 Address**
To remove an IPv4 address from an interface:

#### **CLI Example:**
```bash
/ip address remove [find address=192.168.1.1/24]
```

#### **API Example:**
```bash
/ip/address/remove
=.id=*1
```

---

### **1.4 Configuring DHCP Client for IPv4**
To configure an interface to obtain an IPv4 address via DHCP:

#### **CLI Example:**
```bash
/ip dhcp-client add interface=ether1
```

#### **API Example:**
```bash
/ip/dhcp-client/add
=interface=ether1
```

---

## **2. IPv6 Addressing**

### **2.1 Assigning IPv6 Addresses to Interfaces**
To assign an IPv6 address to an interface, use the `/ipv6 address` menu.

#### **CLI Example:**
```bash
/ipv6 address add address=2001:db8::1/64 interface=ether1
```
- `address=2001:db8::1/64`: Specifies the IPv6 address and prefix length.
- `interface=ether1`: Specifies the interface to which the IPv6 address is assigned.

#### **API Example:**
```bash
/ipv6/address/add
=address=2001:db8::1/64
=interface=ether1
```

---

### **2.2 Viewing IPv6 Addresses**
To view the list of configured IPv6 addresses:

#### **CLI Example:**
```bash
/ipv6 address print
```

#### **API Example:**
```bash
/ipv6/address/print
```

---

### **2.3 Removing an IPv6 Address**
To remove an IPv6 address from an interface:

#### **CLI Example:**
```bash
/ipv6 address remove [find address=2001:db8::1/64]
```

#### **API Example:**
```bash
/ipv6/address/remove
=.id=*1
```

---

### **2.4 Configuring DHCPv6 Client for IPv6**
To configure an interface to obtain an IPv6 address via DHCPv6:

#### **CLI Example:**
```bash
/ipv6 dhcp-client add interface=ether1
```

#### **API Example:**
```bash
/ipv6/dhcp-client/add
=interface=ether1
```

---

## **3. Dual-Stack Configuration (IPv4 and IPv6)**

### **3.1 Assigning Both IPv4 and IPv6 Addresses**
To configure an interface with both IPv4 and IPv6 addresses:

#### **CLI Example:**
```bash
/ip address add address=192.168.1.1/24 interface=ether1
/ipv6 address add address=2001:db8::1/64 interface=ether1
```

#### **API Example:**
```bash
/ip/address/add
=address=192.168.1.1/24
=interface=ether1

/ipv6/address/add
=address=2001:db8::1/64
=interface=ether1
```

---

### **3.2 Enabling IPv6 Neighbor Discovery**
To enable IPv6 Neighbor Discovery (ND) on an interface:

#### **CLI Example:**
```bash
/ipv6 nd add interface=ether1
```

#### **API Example:**
```bash
/ipv6/nd/add
=interface=ether1
```

---

## **4. Basic Troubleshooting**

### **4.1 Checking IP Connectivity**
To test connectivity using `ping`:

#### **CLI Example:**
```bash
/ping 192.168.1.1
/ping 2001:db8::1
```

#### **API Example:**
```bash
/ping
=address=192.168.1.1

/ping
=address=2001:db8::1
```

---

### **4.2 Viewing Routing Tables**
To view the IPv4 and IPv6 routing tables:

#### **CLI Example:**
```bash
/ip route print
/ipv6 route print
```

#### **API Example:**
```bash
/ip/route/print
/ipv6/route/print
```

---

## **5. Conclusion**
This guide covers the basic configuration of IPv4 and IPv6 addressing on MikroTik RouterOS 6.x for a SOHO network. By following these examples, you can set up and manage IP addresses, configure DHCP, and troubleshoot connectivity issues effectively.

For more advanced configurations, refer to the official MikroTik documentation or consult with a MikroTik Certified Engineer.

--- 

**Note:** Ensure that your MikroTik device is running RouterOS version 6.x, as some commands or features may differ in other versions.

## API Reference Cheat Sheet
```python
# Universal API Helper Function
def mikrotik_api_call(
    method: str,
    endpoint: str,
    data: dict = None,
    timeout: int = 10
) -> dict:
    '''
    Universal MikroTik API handler with error checking
    '''
    try:
        response = requests.request(
            method,
            f"https://{ROUTER_IP}/rest{endpoint}",
            auth=HTTPBasicAuth(API_USER, API_PASS),
            json=data,
            verify=SSL_VERIFY,
            timeout=timeout
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"API Error: {e.response.status_code} - {e.response.text}")
        return {"error": str(e)}
```

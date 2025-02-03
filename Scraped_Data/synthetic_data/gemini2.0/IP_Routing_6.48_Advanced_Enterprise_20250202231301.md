**Topic: IP Routing**

**Configuration Scenario and Requirements:**

* Configure IP routing on a MikroTik RouterOS 6.48 router to connect multiple networks.
* Implement static and dynamic routing protocols to manage network traffic.
* Utilize IP Pools and MAC servers to manage IP address assignments and MAC address learning.

**Step-by-Step Implementation:**

**1. Configure IP Addressing**

```
/ip address
add address=192.168.1.1/24 interface=ether1
add address=192.168.2.1/24 interface=ether2
```

**2. Configure IP Pools**

```
/ip pool
add name=pool1 ranges=192.168.1.10-192.168.1.20 interface=ether1
add name=pool2 ranges=192.168.2.10-192.168.2.20 interface=ether2
```

**3. Configure IP Routes**

**Static Routes:**

```
/ip route
add dst-address=10.0.0.0/24 gateway=192.168.1.2
add dst-address=20.0.0.0/24 gateway=192.168.2.2
```

**Dynamic Routes (OSPF):**

```
/routing ospf
set enabled=yes interface=ether1
set enabled=yes interface=ether2
set router-id=192.168.1.1
```

**4. Configure MAC Server**

```
/ip dhcp-server
set mac-server=yes interface=ether1
set mac-server=yes interface=ether2
```

**5. Configure RoMON**

```
/tool romon
set enabled=yes
set port=3333
```

**Complete Configuration Commands:**

```
/ip address
add address=192.168.1.1/24 interface=ether1
add address=192.168.2.1/24 interface=ether2

/ip pool
add name=pool1 ranges=192.168.1.10-192.168.1.20 interface=ether1
add name=pool2 ranges=192.168.2.10-192.168.2.20 interface=ether2

/ip route
add dst-address=10.0.0.0/24 gateway=192.168.1.2
add dst-address=20.0.0.0/24 gateway=192.168.2.2

/routing ospf
set enabled=yes interface=ether1
set enabled=yes interface=ether2
set router-id=192.168.1.1

/ip dhcp-server
set mac-server=yes interface=ether1
set mac-server=yes interface=ether2

/tool romon
set enabled=yes
set port=3333
```

**Common Pitfalls and Solutions:**

* **Overlapping IP Addresses:** Ensure that IP addresses on different interfaces do not overlap.
* **Invalid Gateway Addresses:** Verify that the gateway addresses specified in static routes are reachable.
* **Incorrect Route Preference:** Make sure that static routes have higher preference than dynamic routes.
* **MAC Address Conflicts:** Address MAC address conflicts by configuring the MAC server to learn and forward packets correctly.

**Verification and Testing Steps:**

* Ping IP addresses on different networks to verify connectivity.
* Use the "netstat" command to check for established connections and routing table entries.
* Run the "route print" command to display the current routing table.

**Related Features and Considerations:**

* **Policy Routing:** Configure traffic to be forwarded based on specific criteria.
* **VRF:** Divide the routing table into multiple instances (VRFs) to isolate traffic between different domains.
* **IPv6 Support:** Implement IPv6 routing to support next-generation networks.

**MikroTik REST API Examples:**

* **Get IP Routes:**

```
GET https://<router>/rest/api/ip/route
```

* **Create Static Route:**

```
POST https://<router>/rest/api/ip/route
Content-Type: application/json

{
  "dst-address": "10.0.0.0/24",
  "gateway": "192.168.1.2"
}
```
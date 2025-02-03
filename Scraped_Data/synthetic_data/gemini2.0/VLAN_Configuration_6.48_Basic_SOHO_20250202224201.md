## VLAN Configuration for SOHO Networks

**Configuration Scenario and Requirements**

* Create a separate VLAN for guest Wi-Fi access
* VLAN ID: 100
* VLAN Name: Guest
* Internet access allowed only to the main LAN (VLAN 1)

## Step-by-Step Implementation

**1. Create the VLAN Interface**

Create a new VLAN interface on the switch port where the guest Wi-Fi access point will connect.

```
/interface vlan add name=Guest vlan-id=100
```

**2. Configure the Switch Port**

Assign the VLAN interface to the switch port.

```
/interface switch port set switch1-port1 vlan=Guest
```

**3. Create DHCP Server for VLAN**

Create a DHCP server to assign IP addresses to devices connected to the guest Wi-Fi network.

```
/ip dhcp-server add address-pool=Guest interface=Guest range=192.168.100.10-192.168.100.254 lease-time=1h
```

**4. Configure the Firewall Rules**

Allow traffic only from the main LAN (VLAN 1) to the Internet.

```
/ip firewall filter add action=accept chain=forward in-interface-list=Guest out-interface-list=WAN
/ip firewall filter add action=drop chain=forward in-interface-list=Guest out-interface-list=!Guest
```

**5. Test the VLAN**

Connect a device to the guest Wi-Fi network and verify that it can access the Internet.

## Troubleshooting Common Pitfalls

* **Connectivity issues:** Ensure that the switch port is correctly assigned to the VLAN interface.
* **DHCP issues:** Verify that the DHCP server is running and that the IP address range is correct.
* **Firewall issues:** Check that the firewall rules are configured correctly to allow traffic from the VLAN to the Internet.

## Verification and Testing

* Use the following commands to verify the configuration:
    ```
    /interface vlan print
    /interface switch port print
    /ip dhcp-server print
    /ip firewall filter print
    ```
* Connect a device to the guest Wi-Fi network and check its IP address using `ifconfig` or `ip addr`.
* Test Internet connectivity by pinging an external IP address.

## Related Features and Considerations

* **VLAN Trunking:** Configure VLAN trunking if multiple VLANs need to be carried over a single physical link.
* **Security:** Implement additional security measures, such as access control lists (ACLs) and intrusion detection systems (IDS).
* **VLAN Management:** Use the MikroTik WebFig or RouterOS CLI to manage VLANs and monitor their traffic.

## MikroTik REST API Example

```
**Endpoint:** /interface/vlan
**Method:** POST

**Request body (JSON):**
```json
{
  "name": "Guest",
  "vlan-id": 100
}
```

**Expected response:**
```json
{
  "id": "1000",
  "name": "Guest",
  "vlan-id": 100
}
```
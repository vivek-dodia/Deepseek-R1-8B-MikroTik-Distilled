## IP Addressing (IPv4 and IPv6) in MikroTik RouterOS 7.11

### Configuration Scenario and Requirements

In this scenario, we will configure IPv4 and IPv6 addresses on a MikroTik router to enable internet connectivity and communication with other devices.

### Step-by-Step Implementation

#### IPv4

1. Connect to the router using WinBox or the CLI.
2. Go to `IP > Addresses`.
3. Click the `+` button to add a new address.
4. Configure the following parameters:
   - **Interface:** Select the interface you want to assign the address to.
   - **Address:** Enter the IP address you want to assign.
   - **Network:** Enter the network mask for the address.
5. Click `OK` to save the configuration.

#### IPv6

1. Go to `IP > Addresses`.
2. Click the `+` button to add a new address.
3. Configure the following parameters:
   - **Interface:** Select the interface you want to assign the address to.
   - **Address:** Enter the IPv6 address you want to assign.
   - **Prefix Length:** Enter the prefix length for the address (e.g., 64).
4. Click `OK` to save the configuration.

### Complete Configuration Commands

#### IPv4

```
ip address add address=192.168.1.1/24 interface=ether1
```

#### IPv6

```
ip address add address=2001:db8::1/64 interface=ether1
```

### Common Pitfalls and Solutions

- Make sure the interface you are assigning the address to is up and running.
- Ensure that the IP address you are assigning is not already in use on the network.
- If you are assigning an IPv6 address, make sure that the router supports IPv6.
- Check the firewall settings to ensure that traffic to and from the assigned IP addresses is allowed.

### Verification and Testing Steps

To verify the configuration, you can use the following commands:

#### IPv4

```
ip address print
```

#### IPv6

```
ip address print brief
```

You should see the newly assigned IP addresses in the output.

### Related Features and Considerations

- Subnetting
- DHCP
- Static routing
- Firewall

### MikroTik REST API Examples

#### IPv4 Address Creation

**API Endpoint:** `/ip/address/add`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "interface": "ether1",
  "address": "192.168.1.1/24"
}
```

**Expected Response:**

```json
{
  "id": "1"
}
```

#### IPv6 Address Creation

**API Endpoint:** `/ip/address/add`

**Request Method:** POST

**Example JSON Payload:**

```json
{
  "interface": "ether1",
  "address": "2001:db8::1/64"
}
```

**Expected Response:**

```json
{
  "id": "1"
}
```
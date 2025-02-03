**Technical MikroTik RouterOS Documentation for the MAC Server**

**Configuration Level:** Advanced

**Network Scale:** ISP

**1. Configuration Scenario and Requirements**

The MAC server feature in RouterOS allows you to manage and control access to your network based on the MAC addresses of connected devices. This is useful for ISPs who want to provide differentiated services or enforce policies on customer devices.

**2. Step-by-Step Implementation**

**2.1. Create a MAC Server**

Start by creating a new MAC server instance:

```
/ip mac-server
add name=my-mac-server
```

**2.2. Define MAC Address Binding**

Next, define the MAC addresses that are allowed to access the network:

```
/ip mac-server binding
add mac-address=00:01:02:03:04:05 server=my-mac-server
```

**2.3. Assign Default Server**

Set the default MAC server that will handle all other MAC addresses that are not explicitly defined:

```
/ip mac-server
set my-mac-server default
```

**3. Complete Configuration Commands**
- Create MAC server: `/ip mac-server add name=<server-name>`
- Define MAC address binding: `/ip mac-server binding add mac-address=<MAC-address> server=<server-name>`
- Set default server: `/ip mac-server set <server-name> default`

**4. Common Pitfalls and Solutions**

- Ensure that the MAC addresses defined in the binding list are correct and match the devices you want to allow access to.
- Avoid adding too many MAC addresses to the binding list, as this can slow down the MAC server process.
- Make sure to configure the default server to handle all other MAC addresses that are not explicitly defined.

**5. Verification and Testing Steps**

- Check the MAC server status: `/ip mac-server print`
- Test MAC address binding by connecting a device with a known MAC address to the network.
- Verify that the device can access the network as expected.

**6. Related Features and Considerations**

- MAC filtering: The MAC server can also be used for MAC filtering, which blocks access to devices based on their MAC addresses.
- RADIUS authentication: The MAC server can be integrated with RADIUS to perform authentication and authorization based on MAC addresses.
- IP tables: MAC server bindings can be used in conjunction with IP tables to create more complex access control rules.

**7. MikroTik REST API Examples**

**7.1. Get MAC Server List**

**API Endpoint:** `/ip/mac-server`
**Request Method:** GET

**Response:**

```
[
  {
    "comment": null,
    "default": false,
    "disabled": false,
    "hash": "4e7de864e9d3f93001d2a1d52d...",
    "name": "my-mac-server"
  }
]
```

**7.2. Create MAC Server Binding**

**API Endpoint:** `/ip/mac-server/binding`
**Request Method:** POST

**Request Body (JSON Payload):**

```
{
  "mac-address": "00:01:02:03:04:05",
  "server": "my-mac-server"
}
```

**Expected Response:**

```
{
  "retry": null,
  "time": 1672870295,
  "timeout": null
}
```

**Note:** The `time` field indicates the time when the binding was added.
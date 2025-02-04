# Document Information
Title: User Manager
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/2555940/User+Manager,

# Content
# Overview
User Manager is RADIUS server implementation in RouterOS which provides centralized user authentication and authorization to a certain service. Having a central user database allows better tracking of system users and customers. As a separate package, User Manager is available on all architectures except SMIPS, however, care must be taken due to limited free space available. It supports many different authentication methods including PAP, CHAP, MS-CHAP, MS-CHAPv2, EAP-TLS, EAP-TTLS, and EAP-PEAP. In RouterOS, DHCP, Dot1x, Hotspot, IPsec, PPP, and Wireless are features that benefit from User Manager the most. Each user can see their account statistics and manage available profiles using the WEB interface. Additionally, users can buy their own data plans (profiles) using the most popular payment gateway - PayPal making it a great system for service providers. Customized reports can be generated to ease processing by the billing department. User Manager works according to RADIUS standards defined inRFC2865andRFC3579.
User Manager is one of the RouterOS features, that is limited by the RouterOS license level. Depending on theLicense level, number of active sessions will be limited, including multiple connections per user (not unique accounts).
# Attributes
Sub-menu:/user-manager attribute
```
/user-manager attribute
```
RADIUS attributes are defined authorization, information, and configuration parameters that are passed between the RADIUS server and the client. User Manager allows sending customized attributes defined in the "attributes" menu. RouterOS has a set of predefined attributes already present, but it is also possible to add additional attributes if necessary. Predefined attributes:
Attribute | Vendor ID | Type ID | Value type | Packet type | Description | Value | Description | Value | Description | Value | Description | Value | Description
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Framed-IP-Address | 0 (standard) | 8 | ip address | Access-Accept | RFC2865 section 5.8
Framed-IP-Netmask | 0 (standard) | 9 | ip address | Access-Accept | RFC2865 section 5.9
Session-Timeout | 0 (standard) | 27 | integer (maximum value: 21474720) | Access-Accept, Access-Challenge | RFC2865 section 5.27
Idle-Timeout | 0 (standard) | 28 | integer | Access-Accept, Access-Challenge | RFC2865 section 5.28
Tunnel-Type | 0 (standard) | 64 | ValueDescription1Point-to-Point Tunneling Protocol (PPTP)2Layer Two Forwarding (L2F)3Layer Two Tunneling Protocol (L2TP)4Ascend Tunnel Management Protocol (ATMP)5Virtual Tunneling Protocol (VTP)6IP Authentication Header in the Tunnel-mode (AH)7IP-in-IP Encapsulation (IP-IP)8Minimal IP-in-IP Encapsulation (MIN-IP-IP)9IP Encapsulating Security Payload in the Tunnel-mode (ESP)10Generic Route Encapsulation (GRE)11Bay Dial Virtual Services (DVS)12IP-in-IP Tunneling13Virtual LAN | 1 | Point-to-Point Tunneling Protocol (PPTP) | 2 | Layer Two Forwarding (L2F) | 3 | Layer Two Tunneling Protocol (L2TP) | 4 | Ascend Tunnel Management Protocol (ATMP) | 5 | Virtual Tunneling Protocol (VTP) | 6 | IP Authentication Header in the Tunnel-mode (AH) | 7 | IP-in-IP Encapsulation (IP-IP) | 8 | Minimal IP-in-IP Encapsulation (MIN-IP-IP) | 9 | IP Encapsulating Security Payload in the Tunnel-mode (ESP) | 10 | Generic Route Encapsulation (GRE) | 11 | Bay Dial Virtual Services (DVS) | 12 | IP-in-IP Tunneling | 13 | Virtual LAN | Access-Accept | RFC2868 section 3.1RFC3580 section 3.31
1 | Point-to-Point Tunneling Protocol (PPTP)
2 | Layer Two Forwarding (L2F)
3 | Layer Two Tunneling Protocol (L2TP)
4 | Ascend Tunnel Management Protocol (ATMP)
5 | Virtual Tunneling Protocol (VTP)
6 | IP Authentication Header in the Tunnel-mode (AH)
7 | IP-in-IP Encapsulation (IP-IP)
8 | Minimal IP-in-IP Encapsulation (MIN-IP-IP)
9 | IP Encapsulating Security Payload in the Tunnel-mode (ESP)
10 | Generic Route Encapsulation (GRE)
11 | Bay Dial Virtual Services (DVS)
12 | IP-in-IP Tunneling
13 | Virtual LAN
Tunnel-Medium-Type | 0 (standard) | 65 | ValueDescription1IPv4 (IP version 4)2IPv6 (IP version 6)3NSAP4HDLC (8-bit multidrop)5BBN 18226802 (includes all 802 media plus Ethernet "canonical format")7E.163 (POTS)8E.164 (SMDS, Frame Relay, ATM)9F.69 (Telex)10X.121 (X.25, Frame Relay)11IPX12Appletalk13Decnet IV14Banyan Vines15E.164 with NSAP format subaddress | 1 | IPv4 (IP version 4) | 2 | IPv6 (IP version 6) | 3 | NSAP | 4 | HDLC (8-bit multidrop) | 5 | BBN 1822 | 6 | 802 (includes all 802 media plus Ethernet "canonical format") | 7 | E.163 (POTS) | 8 | E.164 (SMDS, Frame Relay, ATM) | 9 | F.69 (Telex) | 10 | X.121 (X.25, Frame Relay) | 11 | IPX | 12 | Appletalk | 13 | Decnet IV | 14 | Banyan Vines | 15 | E.164 with NSAP format subaddress | Access-Accept | RFC2868 section 3.2
1 | IPv4 (IP version 4)
2 | IPv6 (IP version 6)
3 | NSAP
4 | HDLC (8-bit multidrop)
5 | BBN 1822
6 | 802 (includes all 802 media plus Ethernet "canonical format")
7 | E.163 (POTS)
8 | E.164 (SMDS, Frame Relay, ATM)
9 | F.69 (Telex)
10 | X.121 (X.25, Frame Relay)
11 | IPX
12 | Appletalk
13 | Decnet IV
14 | Banyan Vines
15 | E.164 with NSAP format subaddress
Tunnel-Private-Group-ID | 0 (standard) | 81 | string | Access-Accept | RFC2868 section 3.6
Framed-Pool | 0 (standard) | 88 | string | Access-Accept | RFC2869 section 5.18
Framed-IPv6-Prefix | 0 (standard) | 97 | ipv6 prefix | Access-Accept | RFC3162 section 2.3
Framed-IPv6-Pool | 0 (standard) | 100 | string | Access-Accept | RFC3162 section 2.6
Delegated-IPv6-Prefix | 0 (standard) | 123 | ipv6 prefix | Access-Accept | RFC4818
Framed-IPv6-Address | 0 (standard) | 168 | ip address | Access-Accept | RFC6911 section 3.1
Mikrotik-Recv-Limit | 14988 (Mikrotik) | 1 | integer | Access-Accept | Total receive limit in bytes for the client.
Mikrotik-Xmit-Limit | 14988 (Mikrotik) | 2 | integer | Access-Accept | Total transmit limit in bytes for the client.
Mikrotik-Group | 14988 (Mikrotik) | 3 | string | Access-Accept | User's group for local users.HotSpot profile for HotSpot users.PPP profile for PPP users.
Mikrotik-Wireless-Forward | 14988 (Mikrotik) | 4 | integer | Access-Accept | Not forward the client's frames back to the wireless infrastructure if this attribute is set to "0" (wireless only).
Mikrotik-Wireless-Skip-Dot1x | 14988 (Mikrotik) | 5 | integer | Access-Accept | Disable 802.1x authentication for the particular wireless client if set to a non-zero value (wireless only).
Mikrotik-Wireless-Enc-Algo | 14988 (Mikrotik) | 6 | ValueDescription0No-encryption140-bit-WEP2104-bit-WEP3AES-CCM4TKIP | 0 | No-encryption | 1 | 40-bit-WEP | 2 | 104-bit-WEP | 3 | AES-CCM | 4 | TKIP | Access-Accept | WEP encryption algorithm( wireless only).
0 | No-encryption
1 | 40-bit-WEP
2 | 104-bit-WEP
3 | AES-CCM
4 | TKIP
Mikrotik-Wireless-Enc-Key | 14988 (Mikrotik) | 7 | string | Access-Accept | WEP encryption key for the client (wireless only).
Mikrotik-Rate-Limit | 14988 (Mikrotik) | 8 | string | Access-Accept | Datarate limitation for clients. The format is: rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]] from the point of view of the router (so "rx" is client upload, and "tx" is client download). All rates should be numbers with optional 'k' (1,000s) or 'M' (1,000,000s). If the tx-rate is not specified, the rx-rate is as tx-rate too. The same goes for tx-burst-rate and tx-burst-threshold and tx-burst-time. If both rx-burst-threshold and tx-burst-threshold are not specified (but burst-rate is specified), rx-rate and tx-rate are used as burst thresholds. If both rx-burst-time and tx-burst-time are not specified, 1s is used as default. Priority takes values 1..8, where 1 implies the highest priority, but 8 - the lowest. If rx-rate-min and tx-rate-min are not specified rx-rate and tx-rate values are used. The rx-rate-min and tx-rate-min values can not exceed rx-rate and tx-rate values.
Mikrotik-Realm | 14988 (Mikrotik) | 9 | string | Access-Request | If it is set in /radius menu, it is included in every RADIUS request as Mikrotik-Realm attribute. If it is not set, the same value is sent as in the MS-CHAP-Domain attribute (if MS-CHAP-Domain is missing, Realm is not included either).
Mikrotik-Host-IP | 14988 (Mikrotik) | 10 | ip address | Access-Request | The IP address of HotSpot client before Universal Client translation (the original IP address of the client).
Mikrotik-Mark-Id | 14988 (Mikrotik) | 11 | string | Access-Accept | Firewall mangle chain name (HotSpot only). The MikroTik RADIUS client upon receiving this attribute creates a dynamic firewall mangle rule with action=jump chain=hotspot and jump-target equal to the attribute value. Mangle chain name can have suffixes .in or .out, which will install rule only for incoming or outgoing traffic. Multiple Mark-id attributes can be provided, but only the last ones for incoming and outgoing are used.
Mikrotik-Advertise-URL | 14988 (Mikrotik) | 12 | string | Access-Accept | URL of the page with advertisements that should be displayed to clients. If this attribute is specified, advertisements are enabled automatically, including transparent proxy, even if they were explicitly disabled in the corresponding user profile. Multiple attribute instances may be sent by the RADIUS server to specify additional URLs which are chosen in a round-robin fashion.
Mikrotik-Advertise-Interval | 14988 (Mikrotik) | 13 | integer | Access-Accept | The time interval between two adjacent advertisements. Multiple attribute instances may be sent by the RADIUS server to specify additional intervals. All interval values are treated as a list and are taken one by one for each successful advertisement. If the end of the list is reached, the last value is continued to be used.
Mikrotik-Recv-Limit-Gigawords | 14988 (Mikrotik) | 14 | integer | Access-Accept | 4G (2^32) bytes of total receive limit (bits 32..63, when bits 0..31 are delivered in Mikrotik-Recv-Limit).
Mikrotik-Xmit-Limit-Gigawords | 14988 (Mikrotik) | 15 | integer | Access-Accept | 4G (2^32) bytes of total transmit limit (bits 32..63, when bits 0..31 are delivered in Mikrotik-Recv-Limit).
Mikrotik-Wireless-PSK | 14988 (Mikrotik) | 16 | string | Access-Accept |
Mikrotik-Total-Limit | 14988 (Mikrotik) | 17 | integer | Access-Accept |
Mikrotik-Total-Limit-Gigawords | 14988 (Mikrotik) | 18 | integer | Access-Accept |
Mikrotik-Address-List | 14988 (Mikrotik) | 19 | string | Access-Accept |
Mikrotik-Wireless-MPKey | 14988 (Mikrotik) | 20 | string | Access-Accept |
Mikrotik-Wireless-Comment | 14988 (Mikrotik) | 21 | string | Access-Accept |
Mikrotik-Delegated-IPv6-Pool | 14988 (Mikrotik) | 22 | string | Access-Accept | IPv6 pool used for Prefix Delegation.
Mikrotik-DHCP-Option-Set | 14988 (Mikrotik) | 23 | string | Access-Accept |
Mikrotik-DHCP-Option-Param-STR1 | 14988 (Mikrotik) | 24 | string | Access-Accept |
Mikrotik-DHCP-Option-Param-STR2 | 14988 (Mikrotik) | 25 | string | Access-Accept |
Mikrotik-Wireless-VLANID | 14988 (Mikrotik) | 26 | integer | Access-Accept | VLAN ID for the client (Wireless only).
Mikrotik-Wireless-VLANIDtype | 14988 (Mikrotik) | 27 | ValueDescription0802.1q1802.1ad | 0 | 802.1q | 1 | 802.1ad | Access-Accept | VLAN ID type for the client (Wireless only).
0 | 802.1q
1 | 802.1ad
Mikrotik-Wireless-Minsignal | 14988 (Mikrotik) | 28 | string | Access-Accept |
Mikrotik-Wireless-Maxsignal | 14988 (Mikrotik) | 29 | string | Access-Accept |
Mikrotik-Switching-Filter | 14988 (Mikrotik) | 30 | string | Access-Accept | Allows to create dynamic switch rules when authenticating clients with dot1x server.
Framed-IP-Address
Framed-IP-Netmask
Session-Timeout
Idle-Timeout
Tunnel-Type
Value | Description
-------------------
1 | Point-to-Point Tunneling Protocol (PPTP)
2 | Layer Two Forwarding (L2F)
3 | Layer Two Tunneling Protocol (L2TP)
4 | Ascend Tunnel Management Protocol (ATMP)
5 | Virtual Tunneling Protocol (VTP)
6 | IP Authentication Header in the Tunnel-mode (AH)
7 | IP-in-IP Encapsulation (IP-IP)
8 | Minimal IP-in-IP Encapsulation (MIN-IP-IP)
9 | IP Encapsulating Security Payload in the Tunnel-mode (ESP)
10 | Generic Route Encapsulation (GRE)
11 | Bay Dial Virtual Services (DVS)
12 | IP-in-IP Tunneling
13 | Virtual LAN
RFC2868 section 3.1
Tunnel-Medium-Type
Value | Description
-------------------
1 | IPv4 (IP version 4)
2 | IPv6 (IP version 6)
3 | NSAP
4 | HDLC (8-bit multidrop)
5 | BBN 1822
6 | 802 (includes all 802 media plus Ethernet "canonical format")
7 | E.163 (POTS)
8 | E.164 (SMDS, Frame Relay, ATM)
9 | F.69 (Telex)
10 | X.121 (X.25, Frame Relay)
11 | IPX
12 | Appletalk
13 | Decnet IV
14 | Banyan Vines
15 | E.164 with NSAP format subaddress
Tunnel-Private-Group-ID
Framed-Pool
Framed-IPv6-Pool
Delegated-IPv6-Prefix
User's group for local users.
HotSpot profile for HotSpot users.
PPP profile for PPP users.
Value | Description
-------------------
0 | No-encryption
1 | 40-bit-WEP
2 | 104-bit-WEP
3 | AES-CCM
4 | TKIP
Value | Description
-------------------
0 | 802.1q
1 | 802.1ad
Properties
Property | Description
----------------------
name(string; Default: ) | Name of the attribute.
packet-types(string; Default:access-accept) | access-accept - use this attribute in RADIUS Access-Accept messagesaccess-challenge - use this attribute in RADIUS Access-Challenge messages
type-id(integer:1..255; Default: ) | Attribute identification number from the specific vendor's attribute database.
value-type(string; Default: ) | hexip-address - IPv4 or IPv6 IP addressip6-prefix - IPv6 prefixmacrostringuint32
vendor-id(integer; Default:0) | IANA allocated a specific enterprise identification number.
# Database
Sub-menu:/user-manager database
```
/user-manager database
```
All RADIUS-related information is stored in a separate User Manager's database configurable under the "database" sub-menu. "Enabled" and "db-path" are the only parameters that are not stored in the User Manager's database and instead are stored in the main RouterOS configuration table meaning that these parameters will be affected by the RouterOS configuration reset. The rest of the configuration, session, and payment data is stored in a separate SQLite database on the FLASH storage of the device. When performing any actions with databases, it is advised to make a backup before and after any activity.
Properties
Property | Description
----------------------
db-path(string; Default: ) | Path to the location where database files will be stored.
Read-only properties
Property | Description
----------------------
db-size | The current size of the database.
free-disk-space | Free space left on the disk where the database is stored.
Commands
Property | Description
----------------------
load(name) | Restore previously created backup file in .umb format.
migrate-legacy-db(database-path; overwrite) | Convert the old User Manager (from RouterOS v6 or before) to the new standard. It is possible to overwrite the current database.
optimize-db() |
save(name; overwrite) | Save the current state of the User Manager database.
# Limitations
Sub-menu:/user-manager limitation
```
/user-manager limitation
```
Limitations are used by Profiles and are linked together by Profile-Limitations. RADIUS accounting and Interim updates must be enabled to seamlessly switch between multiple limitations or disconnect active sessions whendownload-limit,upload-limitoruptime-limitis reached.
To disconnect already active sessions from User Manager,acceptmust be set toyeson the RADIUS client side. If simultaneous session limits are not unlimited (shared-users) and it has reached the maximum allowed number, then the router will try to disconnect the older user session first.
User-Manager attempts to disconnect an active session before a new user will be accepted (when the appropriate limit is set), that's why in such setups it is suggested to use 1s for /radius client timeout.
Properties
Property | Description
----------------------
comment(string; Default: ) | Short description of the limitation.
download-limit(integer; Default:0) | The total amount of traffic a user can download in Bytes.
name(string; Default: ) | Unique name of the limitation.
rate-limit-burst-rx() | Part ofMT-Rate-LimitRADIUS attribute. Refer toQueues# SimpleQueue.
rate-limit-burst-threshold-rx() | Part ofMT-Rate-LimitRADIUS attribute. Refer toQueues# SimpleQueue.
rate-limit-burst-threshold-tx() | Part ofMT-Rate-LimitRADIUS attribute. Refer toQueues# SimpleQueue.
rate-limit-burst-time-rx() | Part ofMT-Rate-LimitRADIUS attribute. Refer toQueues# SimpleQueue.
rate-limit-burst-time-tx() | Part ofMT-Rate-LimitRADIUS attribute. Refer toQueues# SimpleQueue.
rate-limit-burst-tx() | Part ofMT-Rate-LimitRADIUS attribute. Refer toQueues# SimpleQueue.
rate-limit-min-rx() | Part ofMT-Rate-LimitRADIUS attribute. Refer toQueues# SimpleQueue.
rate-limit-min-tx() | Part ofMT-Rate-LimitRADIUS attribute. Refer toQueues# SimpleQueue.
rate-limit-priority() | Part ofMT-Rate-LimitRADIUS attribute. Refer toQueues# SimpleQueue.
rate-limit-rx() | Part ofMT-Rate-LimitRADIUS attribute. Refer toQueues# SimpleQueue.
rate-limit-tx() | Part ofMT-Rate-LimitRADIUS attribute. Refer toQueues# SimpleQueue.
reset-counters-interval(hourly|daily|weekly|monthly|disabled); Default:disabled) | The interval fromreset-counters-start-timewhen all associated user statistics are cleared.
reset-counters-start-time(datetime; Default: ) | Static date and time value from whichreset-counters-intervalis calculated.
transfer-limit(integer; Default:0) | The total amount of aggregated (download+upload) traffic in Bytes.
upload-limit(integer; Default:0) | The total amount of traffic a user can upload in Bytes.
uptime-limit(time; Default:00:00:00) | The total amount of uptime a user can stay active.
# Payments
Sub-menu:/user-manager payment
```
/user-manager payment
```
Information about all received payments is available in this section.
Read-only properties
Property | Description
----------------------
currency(string) | The currency used in the transaction.
method(string) | Service used for the transaction (currently PayPal only).
price(decimal) | Amount paid by the user.
profile(profile) | Name of the profile the user purchased.
trans-end(datetime) | Date and time when the transaction started.
trans-start(datetime) | Date and time when the transaction ended.
trans-status(string) | Status of the transaction. Possible statuses -started,pending,approved,declined,error,timeout,aborted,user approved. Onlyapprovedshould be considered as a complete transaction.
user(string; Default: ) | Name of the user who performed the transaction.
user-message(string; Default: ) |
# Profiles
Sub-menu:/user-manager profile
```
/user-manager profile
```
Properties
Property | Description
----------------------
comment(string; Default: ) | Short description of the entry.
name(string; Default: ) | Unique name of the profile.
name-for-users(string; Default: ) | Name of the profile that will be shown for users on the Web page.
override-shared-users(decimal | off | unlimited; Default:off) | Whether to allow multiple sessions with the same user name. This overrides theshared-userssetting.
price(decimal; Default:0.00) |
starts-when(assigned|first-auth; Default:assigned) | The time when does the profile become active.Assigned- immediately when a User Profile entry is created.First-auth- upon first authentication request from the user.
validity(time | unlimited; Default:unlimited) | The total amount of time a user can use this profile.
# Profile Limitations
Sub-menu:/user-manager profile-limitation
```
/user-manager profile-limitation
```
Profile-Limitations table links Limitations and Profiles together and defines their validity period. When multiple Limitations are assigned to the same Profile, a user must comply with all Limitations for the session to be established. This allows more complicated setups to be created, for example, separate monthly and daily bandwidth limits.
Properties
Property | Description
----------------------
comment(string; Default: ) | Short description of the entry.
from-time(time; Default:00:00:00) | Time of day when the limitation should start.
limitation(limitation; Default: ) | Name of already createdLimitation.
profile(profile; Default: ) | Name of already createdProfile.
till-time(time; Default:23:59:59) | Time of day when the limitation should end.
weekdays(day of week; Default:Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) | Day of the week when the limitation should be active.
# Routers
Sub-menu:/user-manager router
```
/user-manager router
```
Here you can define NAS devices that can use User Manager as a RADIUS server.
Properties
Property | Description
----------------------
coa-port(integer:1..65535; Default:3799) | Port number of CoA (Change of Authorization) communication.
address(IP/IPv6;Default: ) | IP address of the RADIUS client.
comment(string; Default: ) | Short description of the NAS.
disabled(yes | no; Default:no) | Controls whether the entry is currently active or not.
name(string; Default: ) | Unique name of the RADIUS client.
shared-secret(string; Default: ) | Used to secure communication between a RADIUS server and a RADIUS client.
Commands
Property | Description
----------------------
reset-counters() | Clear all statistics for specific RADIUS client.
# Sessions
Sub-menu:/user-manager session
```
/user-manager session
```
Sessions are logged only if accounting is enabled on NAS.
Read-only properties
Property | Description
----------------------
acct-session-id(string) | Unique identification of the accounting session.
active(yes | no) | Whether the session is currently used.
calling-station-id(string) | User's identifier, usually IP address or MAC address.
download(Bytes) | Amount of traffic downloaded.
ended(datetime) | Date and time when the session was closed. Empty for active sessions.
last-accounting-packet(datetime) | Date and time when the last accounting update was received.
nas-ip-address(IP address) | The IP address of the NAS.
nas-port-id(string) | Identifier of the NAS port that is authenticating the user.
nas-port-type(string) | The port type (physicalorvirtual) that is authenticating the user.
started(datetime) | Date and time when the session was established.
status(list of statuses) | Possible available statuses of a session:start -accounting messageStarthas been received,stop -accounting messageStophas been received,interim - Interim updatehas been received,close-acked- session is successfully closed,expired.
terminate-cause(string) | The reason why the session was closed.
upload(Bytes) | Amount of traffic uploaded.
uptime(time) | Total logged uptime on the session.
user(string) | Name of the user.
user-address(IP address) | IP address provided to the user.
# Settings
Sub-menu:/user-manager
```
/user-manager
```
Properties
Property | Description
----------------------
accounting-port(integer; Default:1813) | Port to listen for RADIUS accounting requests.
authentication-port(integer; Default:1812) | Port to listen for RADIUS authentication requests.
certificate(certificate; Default: ) | Certificate for use in EAP TLS-type authentication methods.
enabled(yes | no; Default:no) | Whether the User Manager functionality is enabled.
use-profiles(yes | no; Default:no) | Whether to useProfilesandLimitations. When set tono,onlyUserconfiguration is required to run User Manager.
# Advanced
Sub-menu:/user-manager advanced
```
/user-manager advanced
```
Properties
Property | Description
----------------------
paypal-allow(yes | no; Default:no) | Whether to enable PayPal functionality for User Manager.
paypal-currency(string; Default:USD) | The currency related topricesetting in which users will be billed.
paypal-password(string; Default: ) | The password of your PayPal API account.
paypal-signature(string; Default: ) | Signature of your PayPal API account.
paypal-use-sandbox(yes | no; Default:no) | Whether to use PayPal's sandbox environment for testing purposes.
paypal-user(string; Default: ) | Username of your PayPal API account.
web-private-password(string; Default: ) | Password for accessing/um/PRIVATE/section over HTTP.
web-private-username(string; Default: ) | Username for accessing/um/PRIVATE/section over HTTP.
# Users
Sub-menu:/user-manager user
```
/user-manager user
```
Properties
Property | Description
----------------------
attributes(array of attributes; Default: ) | Custom set ofAttributeswith their values that will additionally be added to Access-Accept messages.
caller-id(string; Default: ) | Allow user's authentication with a specificCalling-Station-Idvalue.
comment(string; Default: ) | Short description of the user.
disabled(yes | no; Default:no) | Controls whether the user can be used or not.
group(group; Default:default) | Name of theGroupthe useris associated to.
name(string; Default: ) | Username for session authentication.
otp-secret(string; Default: ) | A one-time password token that is attached to the password.
password(string; Default: ) | The password of the user for session authentication.
shared-users(integer | unlimited; Default:1) | The total amount of sessions the user can simultaneously establish.
Commands
Property | Description
----------------------
add-batch-users() | The command can generate multiple user accounts based on various parameters.
generate-voucher() | Generates a file based onvoucher-templatethat can be presented to the end user.
monitor() | Shows total statistics for a user. Stats includetotal-uptime,total-download,total-upload,active-sessions,actual-profile,attributes-details.
# User Groups
Sub-menu:/user-manager user group
```
/user-manager user group
```
User groups define common characteristics of multiple users such as allowed authentication methods and RADIUS attributes. There are two groups already present in User Manager calleddefaultanddefault-anonymous.
Properties
Property | Description
----------------------
attributes(array of attributes; Default: ) | Custom set ofAttributeswith their values that will additionally be added to Access-Accept messages for users in this group.
comment(string; Default: ) | Short description of the group.
inner-auths(list of auths; Default: ) | List of allowed authentication methods for tunneled (outer) authentication methods. Supported inner authentication methods -ttls-pap,ttls-chap,ttls-mschap1,ttls-mschap2,peap-mschap2.
name(string; Default: ) | Unique name of the group.
outer-auths(list of auths; Default: ) | List of allowed authentication methods. Supported outer authentication methods -pap,chap,mschap1,mschap2,eap-tls,eap-ttls,eap-peap,eap-mschap2.
# User Profiles
Sub-menu:/user-manager user-profile
```
/user-manager user-profile
```
This menu assigns users a profile and tracks the status of the profile. A single user can have multiple profiles assigned, however, only one can be used at the same time. A user will seamlessly be switched to the next profile when the currently active profile expires without dropping the user's session.
Properties
Property | Description
----------------------
profile(profile; Default: ) | Name of the profile to assign for user.
user(user; Default: ) | Name of the user to use particular profile.
Read-only properties
Property | Description
----------------------
end-time(datetime) | Date and time theUser Profilewill expire.
state(running active| running |used) | The current state of theUser Profile.Running active -currently used profile by the user.Running- a profile is ready to be used.Used- an expired profile that can no longer be activated.
Commands
Property | Description
----------------------
activate-user-profile() | Make aUser Profileentry active immediately.
# WEB Interface
Each user has access to his personal profile using a WEB interface. The WEB interface can be accessed by adding "/um/" directory to the router's IP or domain, for example,http://example.com/um/. Note that the WEB interface is affected by IP Services "www" and "www-ssl". The WEB interface can be customized using CSS, JavaScript, and HTML.
Customizable file reference
File | Description
------------------
css/login.css | Cascading style sheet file used in login prompt page.
css/user.css | Cascading style sheet file used in user's profile page.
img/PayPal_mark_37x23.gif | PayPal logo image.
img/ajax-loader.gif | Loading gif while processing page switching.
img/mikrotik_logo.png | MikroTik logo that is displayed on all pages.
js/generic.js | Javascript file used on all pages.
js/login.js | Javascript file used in login prompt page.
js/user.js | Javascript file used in user's profile page.
user/login_dynamic.html | Layout of the login prompt page.
user/user_dynamic.html | Layout of the user's profile page.
# Application Guides
# Batch user creation
It is possible to create multiple new users with randomly generated usernames and passwords. For example, the following command will generate 3 new users with 6 lowercase symbols as the username and 6 lowercase, uppercase, and numbers as the password.
```
/user-manager user
add-batch-users number-of-users=3 password-characters=lowercase,numbers,uppercase password-length=6 username-characters=lowercase username-length=6
```
The command generated users can be seen by printing the user's table:
```
/user-manager user print
Flags: X - disabled
0   name="olsgkl" password="86a6zH" otp-secret="" group=default shared-users=1 attributes=""
1   name="lkbwss" password="jaKY5V" otp-secret="" group=default shared-users=1 attributes=""
2   name="cwxbwu" password="a62yZd" otp-secret="" group=default shared-users=1 attributes=""
```
# Providing NAS with custom RADIUS attributes
It is possible to send additional RADIUS attributes during the authentication process to provide NAS with custom information about the session, such as what IP address should be assigned to the supplicant or what address pool to use for address assigning.
# Static IP address for a user
To assign the end user a static IP address,Framed-IP-Addressattribute can be used. When using static IP address allocation,shared-sessionsmust be set to 1 to prevent cases when a user has multiple simultaneous sessions, but there is only one IP address. For example:
```
/user-manager user
set [find name=username] shared-users=1 attributes=Framed-IP-Address:192.168.1.4
```
# Specifying address pool for a group of users
We can group up multiple similar users and assign RADIUS attributes to all of them at once. First of all, create a new group:
```
/user-manager user group
add name=location1 outer-auths=chap,eap-mschap2,eap-peap,eap-tls,eap-ttls,mschap1,mschap2,pap \
inner-auths=peap-mschap2,ttls-chap,ttls-mschap1,ttls-mschap2,ttls-pap attributes=Framed-Pool:pool1
```
The next step is to assign a user to the group:
```
/user-manager user
set [find name=username] group=location1
```
In this case, an IP address frompool1will be assigned to the user upon authentication - make surepool1is created on the NAS device.
# Using TOTP (time-based one-time password) for user authentication
User Manager supports time-based authentication token addition to the user's password field that is regenerated every 30 seconds.
TOTP works by having a shared secret on the supplicant (client) and the authentication server (User Manager). To configure TOTP on RouterOS, simply set theotp-secretfor the user. For example:
```
/user-manager user
set [find name=username] password=mypass otp-secret=mysecret
```
To calculate the TOTP token on the supplicant side, many widely available applications can be used, for example, Google Authenticator orhttps://totp.app/. Adding mysecretto the TOTP token generator will provide a new unique 6-digit code that must be added to the user password.
The following example will accept the user's authentication with a calculated TOTP token added to the common password until a new TOTP token is generated, for example,
```
User-Name=username
User-Password=mypass620872
```
# Exporting user credentials
# Printable login credentials for a single user
To generate a single user's printable voucher card, simply use thegenerate-vouchercommand. Specify the RouterOS ID number of the user or use thefindcommand to specify a username. A template is already included in User Manager's installation available in the Files section of your device. You can customize the template for your needs.
```
/user-manager user
generate-voucher voucher-template=printable_vouchers.html [find where name=username]
```
The generated voucher card is available by accessing the router using a WEB browser and navigating to/um/PRIVATE/GENERATED/vouchers/gen_printable_vouchers.html
By default, the printable card looks like this:
It is possible to use different variables when generating vouchers. Currently, supported variables are:
$(username) - Represents User Manager username$(password) - Password of the username$(userprofname) - Profile that is active for the particular user$(userprofendtime) - Profile validity end time if specified
# Multiple user credential export
It is possible to generate a CSV or XML file with multiple or all user credentials at once by using theexport.xmlorexport.csvasvoucher-template.
```
/user-manager user
generate-voucher voucher-template=export.xml [find]
```
The command generates an XML fileum5files/PRIVATE/GENERATED/vouchers/gen_export.xmlwhich can either be accessible by the WEB browser or any other file access tools.
```
<?xml version="1.0" encoding="UTF-8"?>
<users>
<user>
<username>olsgkl</username>
<password>86a6zH</password>
</user>
<user>
<username>lkbwss</username>
<password>jaKY5V</password>
</user>
<user>
<username>cwxbwu</username>
<password>a62yZd</password>
</user>
<user>
<username>username</username>
<password>secretpassword</password>
</user>
</users>
```
# Generating usage report
In cases where presentable network usage information is required by companies billing or legal team an automated session export can be created using thegenerate-reportcommand. The command requires an input of the report template - an example of the template is available inum5files/PRIVATE/TEMPLATES/reports/report_default.html. Example of the report generation:
```
/user-manager
generate-report report-template=report_default.html columns=username,uptime,download,upload
```
The generated report is available by accessing the router using a WEB browser and navigating to/um/PRIVATE/GENERATED/reports/gen_report_default.html
# Purchasing a profile
After logging into the user's private profile by accessing the router's/um/directory using a WEB browser, for example,http://example.com/um/,he will be able to see all availableProfilesin the respective menu. Profiles that have specifiedpricevalues will have aBuy this Profilebutton available.
After pressing theBuy this Profilebutton, the user will be asked to choose from available transaction service providers (currently only PayPal is available) and later redirected to PayPal's payment processing page.
When the payment is completed, the User Manager will ask PayPal to approve the transaction. After approval, the profile is assigned to the user and is ready to use.
# Migrating from RouterOS v6
When you upgrade your User Manager router from RouterOS v6 to the v7 the new User Manager will work with new database files and configuration. To continue using the old user, router, profile, etc. configuration you must manually execute the migrate command. To do so you must have files from the old User Manager server folder "user-manager" present. The folder can be renamed, but all the contents from the old installation must be transferred to the new v7 installation (you can move the old configuration from one router to another router with v7, you must copy "user-manager" folder). After that, all you need to do is execute this command - "/user-manager/database/migrate-legacy-db database-path=<path_to_old_user_manager_folder>".
The import process will try to convert such configuration - users, profiles, user-profiles, limitations, profile-limitations, user-counters, routers, and sessions.
# Application Examples
# Basic L2TP/IPsec server with User Manager authentication
User Manager configuration
Start off by enabling User Manager functionality.
```
/user-manager
set enabled=yes
```
Allow receiving RADIUS requests from the localhost (the router itself).
```
/user-manager router
add address=127.0.0.1 comment=localhost name=local shared-secret=test
```
Next, add users and their credentials that clients will use to authenticate to the server.
```
/user-manager user
add name=user1 password=password
```
Configuring RADIUS client
For the router to use the RADIUS server for user authentication, it is required to add a new RADIUS client that has the same shared secret that we already configured on User Manager.
```
/radius
add address=127.0.0.1 secret=test service=ipsec
```
L2TP/IPsec server configuration
Configure the IP pool from which IP addresses will be assigned to the users and assign it to the PPP Profile.
```
/ip pool
add name=vpn-pool range=192.168.99.2-192.168.99.100
/ppp profile
set default-encryption local-address=192.168.99.1 remote-address=vpn-pool
```
Enable the use of RADIUS for PPP authentication.
```
/ppp aaa
set use-radius=yes
```
Enable the L2TP server with IPsec encryption.
```
/interface l2tp-server server
set enabled=yes use-ipsec=required ipsec-secret=mySecret
```
That is it. Your router is now ready to accept L2TP/IPsec connections and authenticate them to the internal User Manager.
# MFA authentication for RouterOS user login
As User-Manager supports TOTP (time-based-one-time password), it is possible to setup so called MFA authentication for different services. Here will will look into RouterOS user authentication over User Manager (radius) with time based password, that is changed every 30 seconds.
Here are the necessary configuration options on your MikroTik router,
Enable to use RADIUS for /user menu, and set default-grop from /user group menu. Keep in mind that local /user database is checked first, and then RADIUS is contacted.
```
/user/aaa/set use-radius=yes default-group=full
```
Enable radius client for login service. As we run User Manager on the same router, 127.0.0.1 is used,
```
/radius/add address=127.0.0.1 service=login secret=mystrongsecret
```
Here are the configuration steps for User Manager,
Make sure you have added your managed devices to "Routers" menu,
```
/user-manager/router/add name=myrouter address=127.0.0.1 shared-secret=mystrongsecret
```
Add user to User-Manager user table with OTP secret parameter. Few more steps are required for proper OTP configuration.Pick OTP-secret name and convert it to base32 format (there are plenty of online converters from utf-8 to base32 format). For my configuration I use "mysupersecret", that in base32 would be NV4XG5LQMVZHGZLDOJSXI===
```
/user-manager/user/add name=mikrotik password=mysuperpassword otp-secret="NV4XG5LQMVZHGZLDOJSXI==="
```
Note, than in your favorite authenticator app, you will need to set user this key manually "NV4XG5LQMVZHGZLDOJSXI===", when adding new time password instance.
To login to your MikroTik device, open Winbox/Console and connect to your router address, use login:mikrotik and password:mysuperpasswordxxxxxx, where xxxxxx is 6 digit code from your favorite authentication app.
Password is changed every 30 seconds and it is available from your favorite app.
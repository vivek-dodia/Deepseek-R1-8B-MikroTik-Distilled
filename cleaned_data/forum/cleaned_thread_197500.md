# Thread Information
Title: Thread-197500
Section: RouterOS
Thread ID: 197500

# Discussion

## Initial Question
I have question. Is MT OVPN UDP implementation compatible with openvpn.net implementation ?I have following configuration on OpenVPN Server (OpenVPN 2.6.3 x86_64-pc-linux-gnu Debian 12)
```
server172.16.0.0255.255.255.0topology subnet
dev tun
proto tcp
port1194keepalive10120ca ca.crt
cert server.crt
key server.key
dh dh.pem

auth SHA256
data-ciphers AES-256-GCM:AES-256-CBC:AES-128-GCM:AES-128-CBC
data-ciphers-fallback AES-256-CBC
engine aesniOn TCP mode woks perfect (with Hardware Acceleration)ovpn.pngWhen I simply switch configuration to udp (replacing only one line):
```

```
proto udpConnection to MT OVPN client stopped working:ovpn1.pngSome logs from server:
```

```
2023-07-0214:37:13OpenVPN2.6.3x86_64-pc-linux-gnu[SSL(OpenSSL)][LZO][LZ4][EPOLL][PKCS11][MH/PKTINFO][AEAD][DCO]2023-07-0214:37:13library versions:OpenSSL3.0.930May2023,LZO2.102023-07-0214:37:13DCO version:N/A2023-07-0214:37:13TUN/TAP device tun0 opened2023-07-0214:37:13net_iface_mtu_set:mtu1500fortun02023-07-0214:37:13net_iface_up:settun0 up2023-07-0214:37:13net_addr_v4_add:172.16.0.1/24dev tun02023-07-0214:37:13CouldnotdetermineIPv4/IPv6protocol.UsingAF_INET2023-07-0214:37:13UDPv4linklocal(bound):[AF_INET][undef]:11942023-07-0214:37:13UDPv4link remote:[AF_UNSPEC]2023-07-0214:37:13InitializationSequenceCompleted2023-07-0214:37:190.0.0.0:50847Note:OpenSSLhardware crypto engine functionalityisnotavailable2023-07-0214:37:190.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:190.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_ACK_V1)2023-07-0214:37:200.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:210.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:220.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:230.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:240.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:250.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:260.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:270.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:280.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:290.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:300.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:310.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:320.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:330.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:340.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:350.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:360.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:370.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:380.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:390.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:400.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:410.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:420.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:430.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:440.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:450.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:460.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:470.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)2023-07-0214:37:480.0.0.0:50847TLSError:Unroutablecontrol packet receivedfrom[AF_INET]0.0.0.0:50847(si=3op=P_CONTROL_V1)^C2023-07-0214:37:51event_wait:Interruptedsystem call(fd=-1,code=4)2023-07-0214:37:51net_addr_v4_del:172.16.0.1dev tun02023-07-0214:37:51SIGINT[hard,]received,process exiting

---
```

## Response 1
Same problem here. And with a linux openvpn client, all works fine on UDP too. Only with mikrotik I have these problem. Did you find any solution? ---

## Response 2
I have the same problem. I haven't been able to win for a week. Please help me if there is a solution.I checked the date, changed the encryption settings, even changed the OpenVPN version. It's still an error.TLS Error: Unroutable control packet received from [AF_INET] (si=3 op=P_CONTROL_V1)RouterOS 7.12.1OpenVPN server 2.6.1-1ubuntu1.1 ---

## Response 3
Found a solution to the problem? I have exactly the same problem. Who can help? ---

## Response 4
I have this problem too, OpenVPN 2.6.3/Debian 12, RouterOS 7.13.4Are there any ideas anyone? ---

## Response 5
TLS Error: Unroutable control packet received from [AF_INET] (si=3 op=P_CONTROL_V1)I encountered and investigated this error and these are my conclusionsExplanation:The error, although looks like a TLS error, in fact is not caused directly by TLS and is NOT a routing problem as you might think. As I realised (to my understanding), the error is causes by the way the udp openvpn connection is implemented. Let me explain: udp is a connectionless protocol ( when a udp package is received there is no acknowledge message sent back as in tcp).The openvpn server has no means to discern if the connection was ended by the client or if the client is still connected and doesn't send anything. This thing happens also to the client when the interface is disabled clicking disable in the Mikrotik interface. The process is still working in the background and assumes that the connection is still valid (only the interface not reachable) and the process does not discard old connection data.So when you try to reconnect immediateley, the old connection data (negociated connection parameters) are still in memory but the other end doesn't know what to do with the packages he receives and shows the error:"TLS Error: Unroutable control packet received".In my case, when this happens, a solution is to wait for at least 30 seconds and then reconnect again. That way, the process clears old data (by timeout) and allows for a new connection to be established. If you keep trying to reconnect immediately (manually or automatically by disabeling/enabeling the interface), you will keep getting this error forever because every time you try to reconnect, the "keep alive" period on the other side is refreshed and the old data is NOT discarded.If the router has the check mark on the enable, he will try to reconnect automatically and every time it tries will get this error.In other terms, one ending considers the connection as valid, but the other end assumes that the connection has ended and tries a new connection with the same username. This is the cause of the error.Solution (work around):You have to disable auto connect, stop connection, wait at least 30 secondsand then reconnect.Another approach would be to restart the openvpn process and then reconnect (disabeling and enabeling the Mikrotik openvpn interface IS NOT ENOUGH, you have to wait 30 seconds).Note: in my case the router does not work with tls authentication on udp openvpn. For udp I use certificate+password as a security measure and it works like that. Nevertheless, even if tls-auth is not used, the before mentioned error appears (that's why I think it is a timeout error, not a tls authentication error). ---

## Response 6
Same here between Windows 11 OpenVPN client to Mikrotik OVPN server... Waiting 30 seconds and reconnect works but it isn't solution. ---

## Response 7
FIXEDI had the same issue. Fixed bydowngrading OpenVPN server from 2.6 to 2.5.11 ---
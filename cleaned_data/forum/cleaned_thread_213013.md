# Thread Information
Title: Thread-213013
Section: RouterOS
Thread ID: 213013

# Discussion

## Initial Question
RouterOS v7.16.2 machine IP address = 192.168.88.0/24. After installation please remember to carry out "syetem reboot". All ethernets and (wireless lans) of router are ported Hong Kong network (HK-Gateway). The following text was based on Dimitrije's article [1]. The purpose of this thread to let readers to know how to configure routers in order to know the way to get rid of the "blocked" area.Cautions:1. Line 73 (in the following script) abc.xyz.org should be modified to a right one.2. Lines 47-49, the firewall filter code should be placed before the drop line.3. Hong Kong MikroTik router listen-port=22555.4. Mainland China MikroTik router listen-port=13231.5. If 192.168.88.0/24 is changed to other value, please check line 90.6. If the router does not start correctly, you have to wait for few minutes.7. In Mainland China “persistent-keepalive=25” can be removed to keep traffic clean.#
```
########################################
# Step One: Wireguard Tunnel Setup
########################################

# On HK MikroTik
# Set up wireguard interface. This will also generate private/public keypair.
#/interface wireguard 
#add listen-port=22555 mtu=1420 name=wg-china comment="WG China"

#/interface wireguard print
#0  R ;;; WG China
#     name="wg-china" mtu=1420 listen-port=22555 
#     private-key="iBrbTYwkIK30+lDHMXlDWu9n3KUeA1XFJx+BjsbEHnA=" 
#     public-key="mE1t7D3LBfeJ8SkvVRyRsEuZhTo4gl59cgKFstYm92E=" 

/interface wireguard
 add listen-port=22555 mtu=1420 name=wg-china private-key=\
 "iBrbTYwkIK30+lDHMXlDWu9n3KUeA1XFJx+BjsbEHnA=" \
 comment="WG China"

############################################################

# On China MikroTik
# Set up Wireguard interface. This will also generate private/public keypair.
#/interface wireguard
#add listen-port=13231 mtu=1420 name=wg-hk

#/interface wireguard print
#0  R name="wg-hk" mtu=1420 listen-port=13231 
#    private-key="MADwYW6QTh77/z0fXN6kRdQIA+J7Q4dZURWHeoyi1GM=" 
#    public-key="+l7EoWoM3JIIRw2cKWZMPc/IdI4Qjrjt1YScZJ0ObmM=" 

/interface wireguard
add listen-port=13231 mtu=1420 name=wg-hk private-key=\
"MADwYW6QTh77/z0fXN6kRdQIA+J7Q4dZURWHeoyi1GM=" \
comment="WG HK"

######################################################
######################################################

# On HK MikroTik
/ip address
add address=10.1.200.1/24 comment="WG China" interface=wg-china \
    network=10.1.200.0

# The firewall filter must be placed before the drop line
/ip firewall filter
add action=accept chain=input comment="WG China" dst-port=22555 \
    in-interface=ether1 protocol=udp

# Set up China peer.
/interface wireguard peers
add name=china allowed-address=10.1.200.2/32 comment="WG China" \
    interface=wg-china public-key=\
    "+l7EoWoM3JIIRw2cKWZMPc/IdI4Qjrjt1YScZJ0ObmM=" \
     preshared-key="qAnHo8uMf5CrgqFP0XzyFHsG1EZW8+BWG8I3GW/rPUQ="

#######################################################

# On China MikroTik
# Assign address to the router on the new interface.
/ip address
add address=10.1.200.2/32 comment="Wireguard" interface=wg-hk \
    network=10.1.200.0

#/ip firewall filter
#add action=accept chain=input comment="Wireguard" dst-port=13231 \
#   protocol=udp

# Set up HK peer
/interface wireguard peers	
add name=hk allowed-address=0.0.0.0/0 comment="hk" \
    endpoint-address=abc.xyz.org endpoint-port=22555 \
    interface=wg-hk public-key=\
    "mE1t7D3LBfeJ8SkvVRyRsEuZhTo4gl59cgKFstYm92E=" \
    preshared-key="qAnHo8uMf5CrgqFP0XzyFHsG1EZW8+BWG8I3GW/rPUQ=" \
    persistent-keepalive=25

##########################################################
# Step Two: Routing the Traffic
##########################################################

# On China MikroTik
/routing table
add comment="For use by local clients" disabled=no fib name=wg-vpn

/routing rule
add action=lookup-only-in-table \
    comment="Local clients should use (only) Wireguard routing table" \
    disabled=no interface=bridge src-address=192.168.88.0/24 table=wg-vpn

/ip route
add dst-address=0.0.0.0/0 gateway=wg-hk routing-table=wg-vpn

/ip firewall nat \
add chain=srcnat out-interface=wg-hk action=masquerade 

### Open MSDOS  window input "curl http://myip.dnsomatic.com" to display HK IP address ###

#############################################
# Step Three: DNS 
#############################################

# On China MikroTik
/ip dns
set allow-remote-requests=yes servers=1.1.1.1,8.8.8.8

/ip dhcp-server network
set 0 dns-server=1.1.1.1,8.8.8.8

#must reboot once
# /system reboot

#################################################
# Step Four
#################################################

/ip firewall mangle
  add action=change-mss chain=forward new-mss=clamp-to-pmtu passthrough=yes protocol=tcp tcp-flags=syn
  add action=change-mss chain=output new-mss=clamp-to-pmtu passthrough=no protocol=tcp tcp-flags=syn

/system reboot

---
```

## Response 1
What is the purpose of this thread??Links to unknown sites are not recommended ---

## Response 2
Thanks for your interested comments.Your comments have been showed on the first thread. ---

## Response 3
Thank you verygood post, helped me a lot, there is almost none tutorial for this.internet is full of s2s but without tunneling all traffic from one end to main server. ---

## Response 4
topic under revision ---
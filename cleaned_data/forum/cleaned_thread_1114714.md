# Thread Information
Title: Thread-1114714
Section: RouterOS
Thread ID: 1114714

# Discussion

## Initial Question
Hi, I have a LAN (VLAN11) and a WLAN (VLAN12). All MT devices are in the LAN (VLAN11) for management. But it would be handy, if I could see the MNDP-frames in VLAN12 (WLAN), Winbox, too.Of course, I could create on each device an addition VLAN12-interface, but this is inconvenient.A smol reflector who simply re-broadcast all UDP, Port 5678 frams he receives on VLANx on VLANY would nice.Is there such a little software already out there? ---

## Response 1
Due to the connectionless nature of UDP, you might be able to do that with a singleswitch rule. Something like:
```
/interfaceethernetswitchrule
dst-port=5678protocol=udp vlan-id=11\
mirror=ether2new-vlan-id=12(Untried. I don’t use VLANs here.)

---
```

## Response 2
Thank you, unfortunately is the Switch/Mirror-thing to stupid to do this correctly...You can mirror frames, but only on one port and I use LAGs with at least 2 ports. LAGs are not under the switch menu visible. Worked not good/predictable for me :/I have 2 VLANs:LAN = VLAN101 (main MGMT for MT devices)WLAN = VLAN102 (WLAN with Winbox)IPs for the reflector are:10.88.101.2/24 (VLAN101)10.88.102.2/24 (VLAN102)I wrote a smol docker/phyton-contianer+script which does what I want.I share with you guys, if someone seeks such a solution too:Dockerfile:
```
# Use Python 3.11 slim as the base imageFROM python:3.11-slim# Set the working directory in the containerWORKDIR/app# Install required system dependenciesRUN apt-getupdate&&apt-getinstall-y libpcap-dev tcpdump&&apt-getclean# Copy the Python script to the containerCOPY udp_forwarder_bidirectional.py/app/# Install Python dependencies (Scapy)RUN pip install scapy# Define the entry pointCMD["python","udp_forwarder_bidirectional.py"]docker-compose.yml
```

```
version:"3.9"# Define the compose file versionservices:mndp-reflector:build:context:.# Current directory containing Dockerfile and scriptsdockerfile:Dockerfilecontainer_name:vlan101-vlan102-mndp-reflector
    restart:always
    cap_add:-NET_ADMIN# Allow the container to manage network interfaces-NET_RAW# Allow raw network packet manipulationcommand:python3/app/udp_forwarder_bidirectional.py# Start the Python scriptnetworks:vlan101:ipv4_address:10.88.101.2# Specific IP for VLAN101vlan102:ipv4_address:10.88.102.2# Specific IP for VLAN102networks:vlan101:external:true# Use the existing vlan101 networkvlan102:external:true# Use the existing vlan102 networkudp_forwarder_bidirectional.py
```

```
fromscapy.allimportEther,IP,UDP,sendp,Rawimportsocketimportthreading# Configuration from environment variablesimportos
SOURCE_INTERFACE_VLAN101=os.getenv("SOURCE_INTERFACE_VLAN101","eth0")TARGET_INTERFACE_VLAN102=os.getenv("TARGET_INTERFACE_VLAN102","eth1")SOURCE_INTERFACE_VLAN102=os.getenv("SOURCE_INTERFACE_VLAN102","eth1")TARGET_INTERFACE_VLAN101=os.getenv("TARGET_INTERFACE_VLAN101","eth0")SOURCE_PORT=int(os.getenv("SOURCE_PORT",5678))TARGET_PORT=int(os.getenv("TARGET_PORT",5678))BROADCAST_MAC="ff:ff:ff:ff:ff:ff"# Function to forward traffic from VLAN101 to VLAN102defforward_vlan101_to_vlan102():sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)sock.bind(("",SOURCE_PORT))print(f"Listening on {SOURCE_INTERFACE_VLAN101}, forwarding to {TARGET_INTERFACE_VLAN102}...")whileTrue:try:data,addr=sock.recvfrom(2048)print(f"[VLAN101 -> VLAN102] Received from {addr}: {data}")# Check if source port matchesifaddr[1]!=SOURCE_PORT:print(f"[VLAN101 -> VLAN102] Ignored packet from port {addr[1]}")continueether=Ether(dst=BROADCAST_MAC)ip=IP(src=addr[0],dst="255.255.255.255")# Keep source IP, set destination as broadcastudp=UDP(sport=SOURCE_PORT,dport=TARGET_PORT)payload=Raw(load=data)sendp(ether/ip/udp/payload,iface=TARGET_INTERFACE_VLAN102,verbose=False)print(f"[VLAN101 -> VLAN102] Sent to broadcast on {TARGET_INTERFACE_VLAN102}")exceptExceptionase:print(f"[VLAN101 -> VLAN102] Error: {e}")# Function to forward traffic from VLAN102 to VLAN101defforward_vlan102_to_vlan101_raw():sock=socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.htons(3))sock.bind((SOURCE_INTERFACE_VLAN102,0))print(f"Listening on {SOURCE_INTERFACE_VLAN102}, forwarding to {TARGET_INTERFACE_VLAN101}...")whileTrue:try:packet=sock.recv(2048)ether=Ether(packet)# Filter only UDP packets with the desired portsifUDPinetherandether[UDP].sport==SOURCE_PORTandether[UDP].dport==TARGET_PORT:sendp(ether,iface=TARGET_INTERFACE_VLAN101,verbose=False)print(f"[VLAN102 -> VLAN101] Forwarded UDP packet: {ether.summary()}")else:print(f"[VLAN102 -> VLAN101] Ignored non-matching packet")exceptExceptionase:print(f"[VLAN102 -> VLAN101] Error: {e}")# Start forwarding threadsthread_vlan101_to_vlan102=threading.Thread(target=forward_vlan101_to_vlan102,daemon=True)thread_vlan102_to_vlan101=threading.Thread(target=forward_vlan102_to_vlan101_raw,daemon=True)thread_vlan101_to_vlan102.start()thread_vlan102_to_vlan101.start()thread_vlan101_to_vlan102.join()thread_vlan102_to_vlan101.join()Finally I have my MNDP-frames from VLAN101 in VLAN102.edit from 14.12.2024, 22:48: Updated .py (old one matched on more than UDP/5678-traffic)

---
```
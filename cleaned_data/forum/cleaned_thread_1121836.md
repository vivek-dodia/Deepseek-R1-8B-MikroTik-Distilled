# Thread Information
Title: Thread-1121836
Section: RouterOS
Thread ID: 1121836

# Discussion

## Initial Question
Hi everyone, I’m using a MikroTik router configured for dual stack (IPv4 and IPv6), and I’d like to monitor WAN traffic. Specifically, I want to track download and upload data separately for IPv4 and IPv6 traffic.Has anyone set this up before?Is there a straightforward way to measure these statistics in RouterOS?Can the data be viewed in real-time or stored for historical tracking?Ideally, I’d like to integrate these stats with Home Assistant for visualization on a dashboard.I’d appreciate any advice or recommendations for tools or integrations that can help with this setup.Thanks in advance for your help! ---

## Response 1
IPv4 and IPv6 firewalls are distinct (already split). Every firewall rule counts the bytes and packets it matches. The GUI interfaces have graphs. ---

## Response 2
Any specific suggestions? ---

## Response 3
Any specific suggestions?The solution called: "Network Packet Broker (NPB)"."Out-of-Band monitoring" not "In-Band monitoring." ---
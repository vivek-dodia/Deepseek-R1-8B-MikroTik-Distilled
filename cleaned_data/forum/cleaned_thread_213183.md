# Thread Information
Title: Thread-213183
Section: RouterOS
Thread ID: 213183

# Discussion

## Initial Question
Hello, I have a problem with SNMP via WireGuard, I have launched a Zabbix server on my home network and I have 5-6 Mikrotiks on the local network and it intercepts them without any problems, however, on my two remote points, which are via WG, the server does not intercept them. I have ping from Zabbix to the routers and back. I also tried via snmpwalk from Linux on my desktop computer, but I still do not see them. I think the problem is something in the tunnel itself, but I do not know exactly where. The tunnel is launched between Mikrotiks. ---

## Response 1
you probably don't have the correct networks added on the client side/interface wireguard peersadd allowed-address=.........or a convergent community in snmp/snmp communityadd addresses=.... ---
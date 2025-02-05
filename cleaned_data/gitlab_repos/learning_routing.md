# Repository Information
Name: learning_routing

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/alarraz/learning_routing.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: abdel.md
================================================
hola
================================================

File: angel.md
================================================
#tituulo 
angel
================================================

File: configuracion_inicial_jardiel.md
================================================
Cambiar nombre y quitar master port
/interface ethernet
set [ find default-name=ether1 ] name=eth1 master-port=none
set [ find default-name=ether2 ] name=eth2 master-port=none
set [ find default-name=ether3 ] name=eth3 master-port=none
set [ find default-name=ether4 ] name=eth4 master-port=none
set [ find default-name=ether5 ] name=eth5 master-port=none
Cambiar nombre Router
/system identity set name=Mkt14
Cambiar bridge
/ip address set 0 interface=eth2
/ip bridge remove 0
Quitar dhcp server
/ip dhcp-server remove 0
================================================

File: Config_inicial_Abdel.md
================================================
# Cambiar nombre interfaces/quitar masterport
/interface ethernet> set [ find default-name=ether1 ] name=eth1
/interface ethernet> set [ find default-name=ether2 ] name=eth2
/interface ethernet> set [ find default-name=ether3 ] master-port=none name=eth3
/interface ethernet> set [ find default-name=ether4 ] master-port=none name=eth4
/interface ethernet> set [ find default-name=ether5 ] master-port=none name=eth5
# Cambiar nombre router
/system identity> set name=mkt10 
name: mkt10
# Cambiar bridge y quitar el otro
/ip address set 0 interface=eth2
# Quitar dhcp server
/ip dhcp-server remove 0
================================================

File: config_inicial_Ballarin
================================================
#Cambiar nombre y quitar master port
	/interface ethernet
	set [ find default-name=ether1 ] name=eth1 master-port=none
	set [ find default-name=ether2 ] name=eth2 master-port=none
	set [ find default-name=ether3 ] name=eth3 master-port=none
	set [ find default-name=ether4 ] name=eth4 master-port=none
	set [ find default-name=ether5 ] name=eth5 master-port=none
#Cambiar nombre Router
	/system identity set name=MKT05
#Cambiar bridge y quitar el otro
	/ip address set 0 interface=eth2
	/ip bridge remove 0
#Quitar dhcp server
	/ip dhcp-server remove 0
================================================

File: conf_incial_davidmellado.md
================================================
#Cambiar nombre interficies
/interface ethernet
set [ find default-name=ether1 ] name=eth01  
set [ find default-name=ether2 ] name=eth2   
set [ find default-name=ether3 ] name=eth3   
set [ find default-name=ether4 ] name=eth4   
set [ find default-name=ether5 ] name=eth5   
#Cambiar nombre interficie
/interface identity> name=mkt10
#Quitamos el master-port
set [ find default-name=ether1 ] name=eth01  master-port=none
set [ find default-name=ether2 ] name=eth2   master-port=none
set [ find default-name=ether3 ] name=eth3   master-port=none
set [ find default-name=ether4 ] name=eth4   master-port=none
set [ find default-name=ether5 ] name=eth5   master-port=none
#Para quitar el bridge
/interface bridge> remove0
#Para introducir bridge
/interface bridge
add admin-mac=D4:CA:6D:A4:E6:BB auto-mac=no l2mtu=1598 name=bridge-local \
    protocol-mode=rstp
/interface bridge port
add bridge=bridge-local interface=eth2
add bridge=bridge-local interface=wlan1
#Para quitar el dhcp-server
/dhcp-server> remove0
#Para introducir el dhcp-server
/ip dhcp-server network
add address=192.168.88.0/24 comment="default configuration" dns-server=\
    192.168.88.1 gateway=192.168.88.1
================================================

File: conf_incial_gonzalo.md
================================================
Cambiar nombre interficies
/interface ethernet>export
set [ find default-name=ether1 ] name=eth1 master-port=none
set [ find default-name=ether2 ] name=eth2 master-port=none
set [ find default-name=ether3 ] name=eth3 master-port=none
set [ find default-name=ether4 ] name=eth4 master-port=none
set [ find default-name=ether5 ] name=eth5 master-port=none
Cambiar nombre router:
/system identity
set name=mkt16
Cambiar la ip address dek puerto:
[admin@mkt16] /ip address> export
	/ip address
	add address=192.168.88.1/24 comment="default configuration" interface=eth2 \
    network=192.168.88.0
Quitar dirección ip:
[admin@mkt16] /ip address> remove 0
quitar bridge (no tengo router con wifi)
Quitar dhcp-server:
/ip dhcp-server> remove 0
Introducir dhcp server:
[admin@mkt16] /ip dhcp-server> export
/ip dhcp-server
add address-pool=default-dhcp disabled=no interface=eth2 name=default
/ip dhcp-server network
add address=192.168.88.0/24 comment="default configuration" dns-server=\
    192.168.88.1 gateway=192.168.88.1
================================================

File: conf_inicial_eduard.md
================================================
##Configuracio inicial Router
#Eduard Caballol
#Apagar NetworkManager
systemctl stop NetworkManager
#Asignar ip Targeta de red
ip a a 192.168.88.2/24 dev enp0s29u1u2
#Entrar en mikrotik
Telnet 192.168.88.1
login: admin
pasword: ---
# Resetear configuracion router desde "telnet 192.168.88.1"
/system reset-configuration
# Mostrar interfaces
/interface print
#Entrar en interface ethernet
/interface ethernet
# Cambiar nombre de las interfaces
set [ find default-name=ether1 ] name=eth1
set [ find default-name=ether2 ] name=eth2
set [ find default-name=ether3 ] name=eth3
set [ find default-name=ether4 ] name=eth4
set [ find default-name=ether5 ] name=eth5
#Quitar MasterPort:
set [ find default-name=ether2 ] master-port=none                           
set [ find default-name=ether4 ] master-port=none 
set [ find default-name=ether5 ] master-port=none 
set [ find default-name=ether1 ] master-port=none 
#Asignamos ip al eth2
/ip address set 0 interface=eth2
#Quitamos el puerto "bridge" 
/interface bridge remove 0
#Quitamos el dhcp-server
/ip dhcp-server remove 0
================================================

File: conf_inicial_francesc.md
================================================
﻿# Configuración inicial
```
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-b/g/n channel-width=\
    20/40mhz-ht-above distance=indoors l2mtu=2290 mode=ap-bridge ssid=\
    MikroTik-2FDE01
/interface ethernet
set [ find default-name=ether1 ] name=eth1 master-port=none
set [ find default-name=ether2 ] name=eth2 master-port=none
set [ find default-name=ether3 ] name=eth3 master-port=none
set [ find default-name=ether4 ] name=eth4 master-port=none
set [ find default-name=ether5 ] name=eth5 master-port=none
/ip neighbor discovery
set eth1 discover=no
/interface wireless security-profiles
set [ find default=yes ] authentication-types=wpa-psk,wpa2-psk group-ciphers=\
    tkip,aes-ccm mode=dynamic-keys supplicant-identity=MikroTik \
    unicast-ciphers=tkip,aes-ccm wpa-pre-shared-key=3BD2024BA288 \
    wpa2-pre-shared-key=3BD2024BA288
/ip hotspot user profile
set [ find default=yes ] idle-timeout=none keepalive-timeout=2m \
    mac-cookie-timeout=3d
/ip pool
add name=default-dhcp ranges=192.168.88.10-192.168.88.254
/port
set 0 name=serial0
/tool user-manager customer
add backup-allowed=yes disabled=no login=admin password="" \
    paypal-accept-pending=no paypal-allowed=no paypal-secure-response=no \
    permissions=owner signup-allowed=no time-zone=-00:00
/ip address
add address=192.168.88.1/24 comment="default configuration" interface=eth2 \
    network=192.168.88.0
/ip dhcp-client
add comment="default configuration" dhcp-options=hostname,clientid disabled=\
    no interface=eth1
/ip dns
set allow-remote-requests=yes
/ip dns static
add address=192.168.88.1 name=router
/ip firewall filter
add chain=input comment="default configuration" protocol=icmp
add chain=input comment="default configuration" connection-state=established
add chain=input comment="default configuration" connection-state=related
add action=drop chain=input comment="default configuration" disabled=yes \
    in-interface=eth1
add chain=forward comment="default configuration" connection-state=\
    established
add chain=forward comment="default configuration" connection-state=related
add action=drop chain=forward comment="default configuration" \
    connection-state=invalid
/system identity
set name=MKT15
/system lcd
set contrast=0 enabled=no port=parallel type=24x4
/system lcd page
set time disabled=yes display-time=5s
set resources disabled=yes display-time=5s
set uptime disabled=yes display-time=5s
set packets disabled=yes display-time=5s
set bits disabled=yes display-time=5s
set version disabled=yes display-time=5s
set identity disabled=yes display-time=5s
set wlan1 disabled=yes display-time=5s
set eth1 disabled=yes display-time=5s
set eth2 disabled=yes display-time=5s
set eth3 disabled=yes display-time=5s
set eth4 disabled=yes display-time=5s
set eth5 disabled=yes display-time=5s
/system leds
set 0 interface=wlan1
/system routerboard settings
set cpu-frequency=360MHz
/tool mac-server
set [ find default=yes ] disabled=yes
add interface=eth2
add interface=eth3
add interface=eth4
add interface=eth5
add interface=wlan1
/tool mac-server mac-winbox
set [ find default=yes ] disabled=yes
add interface=eth2
add interface=eth3
add interface=eth4
add interface=eth5
add interface=wlan1
```
================================================

File: conf_inicial_jesus_perez.md
================================================
/interface ethernet
set [ find default-name=ether1 ] name=ether1-gateway
set [ find default-name=ether2 ] name=ether2-master-local
set [ find default-name=ether3 ] master-port=ether2-master-local name=\
    ether3-slave-local
set [ find default-name=ether4 ] master-port=ether2-master-local name=\
    ether4-slave-local
set [ find default-name=ether5 ] master-port=ether2-master-local name=\
    ether5-slave-local
[admin@MikroTik] > 
[admin@MikroTik] > interface ethernet set [ find default-name=ether1 ] name=eth1 master-port=none
[admin@MikroTik] > interface ethernet set [ find default-name=ether2 ] name=eth2 master-port=none   
[admin@MikroTik] > interface ethernet set [ find default-name=ether3 ] name=eth3 master-port=none  
[admin@MikroTik] > interface ethernet set [ find default-name=ether4 ] name=eth4 master-port=none  
[admin@MikroTik] > interface ethernet set [ find default-name=ether5 ] name=eth5 master-port=none  
/interface ethernet
set [ find default-name=ether1 ] name=eth1
set [ find default-name=ether2 ] name=eth2
set [ find default-name=ether3 ] name=eth3
set [ find default-name=ether4 ] name=eth4
set [ find default-name=ether5 ] name=eth5
/interface wireless security-profiles
set [ find default=yes ] authentication-types=wpa-psk,wpa2-psk mode=\
    dynamic-keys wpa-pre-shared-key=46ED02934E92 wpa2-pre-shared-key=\
    46ED02934E92
[admin@mkt1] > ip address set 0 interface= ether2 
/interface bridge port
add bridge=bridge-local interface=eth2
add bridge=bridge-local interface=wlan1
/interface> /ip dhcp-server remove 0 
[admin@MikroTik] /interface> /system identity set name=mkt1
[admin@mkt1] /interface>   
[admin@mkt1] /interface wireless> remove
[admin@mkt1] > /ip firewall nat remove 0
[admin@mkt1] > /ip firewall filter disable
numbers: 3
[admin@mkt1] > /ip firewall filter disable
numbers: 6
================================================

File: conf_inicial_roger.md
================================================
# Configuración inicial
Apagar Network Manager
    systemctl stop NetworkManager
Asignar ip al puerto usb
    ip a a 192.168.88.204 dev enp0s29u1u2
Resetear configuracion router desde "telnet 192.168.88.1"
    /system reset-configuration
Mostrar interfaces
    /interface print
Cambiar nombre de las interfaces
    /interface set name=eth1 0
    /interface set name=eth2 1
    /interface set name=eth3 2
    /interface set name=eth4 3
    /interface set name=eth5 4
Asignamos ip al eth2
    /ip address set 0 interface=eth2
Quitamos el puerto "bridge"   !!antes asignar ip!!
    /interface bridge remove 0
Quitamos los masterport de los puertos
    /interface ethernet set [ find default-name=ether3 ] master-port=none name=eth3
    /interface ethernet set [ find default-name=ether4 ] master-port=none name=eth4
    /interface ethernet set [ find default-name=ether5 ] master-port=none name=eth5
Quitamos el dhcp-server
    /ip dhcp-server remove 0
Asignamos gateway del router
	/ip route add gateway=10.200.212.1 dst-address=0.0.0.0/0
================================================

File: conf_inicial_sergi.md
================================================
# Configuración inicial
Cambiar nombre router:
	/system identity 
	/system identity set name=mkt07
Cambiar nombre interfaces:
	/interface ethernet set [ find default-name=ether1 ] name=eth1
	/interface ethernet set [ find default-name=ether2 ] name=eth2
	/interface ethernet set [ find default-name=ether3 ] name=eth3
	/interface ethernet set [ find default-name=ether4 ] name=eth4
	/interface ethernet set [ find default-name=ether5 ] name=eth5
Quitar MasterPort:
	/interface ethernet set [ find default-name=ether2 ] master-port=none                           
	/interface ethernet set [ find default-name=ether3 ] master-port=none   
	/interface ethernet set [ find default-name=ether4 ] master-port=none 
	/interface ethernet set [ find default-name=ether5 ] master-port=none 
	/interface ethernet set [ find default-name=ether1 ] master-port=none 
Cambiar interface:
	/ip address print
		Flags: X - disabled, I - invalid, D - dynamic 
		 #   ADDRESS            NETWORK         INTERFACE                              
		 0   ;;; default configuration
			 192.168.88.1/24    192.168.88.0    bridge-local                           
	/ip address set 0 interface=eth2
	/ip address print
		Flags: X - disabled, I - invalid, D - dynamic 
		 #   ADDRESS            NETWORK         INTERFACE                              
		 0   ;;; default configuration
			 192.168.88.1/24    192.168.88.0    eth2        
Quitar Bridge:
	/interface bridge print
		Flags: X - disabled, R - running 
		 0  R name="bridge-local" mtu=1500 l2mtu=1598 arp=enabled 
			  mac-address=D4:CA:6D:B4:65:D5 protocol-mode=rstp priority=0x8000 
			  auto-mac=no admin-mac=D4:CA:6D:B4:65:D5 max-message-age=20s 
			  forward-delay=15s transmit-hold-count=6 ageing-time=5m 
	/interface bridge remove 0
	/interface bridge print
		Flags: X - disabled, R - running 
Quitar dhcp-server:
	/ip dhcp-server 
	/ip dhcp-server print
		Flags: X - disabled, I - invalid 
		 #   NAME     INTERFACE     RELAY           ADDRESS-POOL     LEASE-TIME ADD-ARP
		 0 I default  (unknown)                     default-dhcp     3d        
	/ip dhcp-server remove 0
	/ip dhcp-server print
		Flags: X - disabled, I - invalid 
		#   NAME     INTERFACE     RELAY           ADDRESS-POOL     LEASE-TIME ADD-ARP
Todas las instrucciones en un copy-paste:
```
/system identity set name=mkt07
/interface ethernet set [ find default-name=ether1 ] name=eth1 master-port=none
/interface ethernet set [ find default-name=ether2 ] name=eth2 master-port=none
/interface ethernet set [ find default-name=ether3 ] name=eth3 master-port=none
/interface ethernet set [ find default-name=ether4 ] name=eth4 master-port=none
/interface ethernet set [ find default-name=ether5 ] name=eth5 master-port=none
/ip address set 0 interface=eth2
/interface bridge remove 0
/ip dhcp-server remove 0
```
================================================

File: erik_mikrotic.md
================================================
# cambiar los nombres de las interfaces y sacarle el puente
	[admin@MikroTik] > /interface ethernet set [ find default-name=ether2 ] name=eth2 master-port=none
	[admin@MikroTik] > /interface ethernet set [ find default-name=ether3 ] name=eth3 master-port=none  
	[admin@MikroTik] > /interface ethernet set [ find default-name=ether4 ] name=eth4 master-port=none   
	[admin@MikroTik] > /interface ethernet set [ find default-name=ether5 ] name=eth5 master-port=none
# eliminar el dhcp server
	 /ip dhcp-server remove 0    
	 /ip dhcp-server network remove 0
#Cambiar nombre del router
	> system identity set name=mkt6
#Desactivar wifi
	> interface wireless disable 0
#Cambiar el bridge de interfaz
	ip address set 0 interface=eth2
#Eliminar el bridge
	interface bridge port export   
	interface bridge remove 0
#deshabilitar firewall3 y eliminar NAT 
	 ip firewall filter disable 3
	 ip firewall nat remove 0   
================================================

File: david.md
================================================
/interface ethernet
set [ find default-name=ether1 ] name=eth01  master-port=none
set [ find default-name=ether2 ] name=eth2   master-port=none
set [ find default-name=ether3 ] name=eth3   master-port=none
set [ find default-name=ether4 ] name=eth4   master-port=none
set [ find default-name=ether5 ] name=eth5   master-port=none
/interface wireless security-profiles
set [ find default=yes ] authentication-types=wpa-psk,wpa2-psk group-ciphers=\
    tkip,aes-ccm mode=dynamic-keys supplicant-identity=MikroTik \
    unicast-ciphers=tkip,aes-ccm wpa-pre-shared-key=46ED02B4A4AF \
    wpa2-pre-shared-key=46ED02B4A4AF
================================================

File: eduard.md
================================================
================================================

File: Erik_docbueno.md
================================================
Hola
================================================

File: examples_mikrotik.md
================================================
Asignamos las direcciones IP a las interfícies.
/ip address 
	add address=192.168.88.1/24 comment="default configuration" disabled=no \interface=eth2 \
	network=192.168.88.0
	add address=10.200.212.101/24 interface=eth5 network=10.200.212.0
	add address=172.17.101.1/24 disabled=no interface=eth3 network=\172.17.101.0
	add address=172.16.101.1/24 interface=bridge1 network=172.16.101.0
/ip firewall nat
add action=masquerade chain=srcnat disabled=no out-interface=eth5
/ip pool
add name=dhcp_pool1 ranges=172.16.109.100-172.16.109.254
/ip dhcp-server network
add address=172.16.101.0/24 dns-server=8.8.8.8 gateway=172.16.101.1
/ip dhcp-server
add address-pool=dhcp_pool1 disabled=no interface=bridge1 name=dhcp1
/ip route add distance=1 gateway=10.200.212.2 routing-mark=adsl
/ip route add distance=1 gateway=10.200.212.1 routing-mark=escola
/ip firewall mangle
add action=mark-routing chain=prerouting in-interface=bridge1 new-routing-mark=adsl src-address=172.16.104.0/24
add action=mark-routing chain=prerouting in-interface=eth3 new-routing-mark=escola src-address=172.17.104.0/24
#cambiar dns por el de la escuela, aseguraros que los servidores dhcp dan el 10.1.1.200
/ip dhcp-server network
add address=172.16.104.0/24 dns-server=10.1.1.200 gateway=172.16.104.1
add address=172.17.104.0/24 dns-server=10.1.1.200 gateway=172.17.104.1
#preparamos rutas con marcas
/ip route
add distance=1 gateway=10.200.212.2 routing-mark=adsl
add distance=1 dst-address=10.0.0.0/8 gateway=10.200.212.1 routing-mark=adsl
add distance=1 gateway=10.200.212.1 routing-mark=escola
add distance=1 gateway=10.200.212.1
/ip firewall mangle
add action=mark-routing chain=prerouting in-interface=bridge1 new-routing-mark=adsl src-address=\
    172.16.104.0/24
add action=mark-routing chain=prerouting in-interface=eth3 new-routing-mark=escola src-address=\
    172.17.104.0/24
add action=mark-packet chain=prerouting new-packet-mark=mirror src-address=10.1.1.188
/queue simple
add max-limit=128k/128k name=limit_down_wifi target=bridge1
/queue tree
add limit-at=100k max-limit=100k name=mirror_down packet-mark=mirror parent=global queue=default
================================================

File: gonzalo.md
================================================
hola
================================================

File: initialize_gitlab.md
================================================
#Pruebas con Gitlab
Esto es una prueba
	ssh-keygen
	#dar de alta la clave en gitlab
	rm -rf learning_routing
	git clone git@gitlab.com:alarraz/learning_routing.git
	ls learning_routing
	cd learning_routing
	geany mi_nombre.md
	git add mi_nombre.md
	git pull
	git commit -m "mi primer commit"
	git push
	ls learning_routing
	ls learning_routing
#Ejemplo para añadir fichero nuevo
Actualizo el repositorio:
	git pull
Añado el fichero a mi repositorio local (sólo la primera vez):
	git add conf_inicial/mifichero.md
Hacemos un commit 
(actualizamos los cambios en el repositorio local) y 
añadimos un comentario entre comillas y con las opciones 
-am:
	git commit -am "añado configuración inicial"
Actualizamos el repositorio remoto con nuestros cambios:
	git push
================================================

File: ivan.md
================================================
## Ivan Rallo
# Configuracion inicial
	Definir nombre de interfaz
		[admin@MikroTik]>/interface ethernet set [ find default-name=ether1 ] name=eth1 master-port=none
		[admin@MikroTik]>set [ find default-name=ether2 ] name=eth2 master-port=none
		[admin@MikroTik]>set [ find default-name=ether3 ] name=eth3 master-port=none
		[admin@MikroTik]>set [ find default-name=ether4 ] name=eth4 master-port=none
		[admin@MikroTik]>set [ find default-name=ether5 ] name=eth5 master-port=none
		[admin@MikroTik]>/ip address set 0 interface=eth2  
	Quitar el bridge
		[admin@MikroTik]>/interface bridge remove
	Quitar dhcp
		[admin@MikroTik]>/interface>/ip dhcp-server print
		[admin@MikroTik]>/interface>/ip dhcp-server remove 0
	Cambiar el nombre de identidad
		[admin@MikroTik]>/interface> /system identity set name=mkt2
	Desactivar wireless
		[admin@mkt2]>/interface wireless disable 0
	Eliminar nat y desactivar el filtro en el 3
		[admin@mkt2]>/ip firewall nat remove 0
		[admin@mkt2]>/ip firewall filter disable 3
================================================

File: jardiel.md
================================================
hola
================================================

File: jesus.md
================================================
ngfdf
================================================

File: radioenlace_mikrotik.md
================================================
# Configuración de routers mikrotik para radioenlace
## Configuración inicial
Si hemos de resetear el router hacemos:
	/system reset-configuration  no-defaults=yes
Primero ponemos una ip por defecto
	/ip address add address=192.168.88.1/24 interface=ether18
Creamos el puente entre interfaces wlan y ether12
	/interface bridge add name=puente
	/interface bridge port
	add bridge=puente interface=ether12
	add bridge=puente interface=wlan1
El radioenlace usará la red 172.16.88.0/24 y nuestro router será el .1:
	/ip address add address=172.16.88.1/24 interface=puente
================================================

File: roger.md
================================================
================================================

File: sergi.md
================================================
hola
================================================

File: test_vel_graph.py
================================================
import subprocess
import numpy as np
import matplotlib.pyplot as plt
#ip de Eduard
ip_dst = "10.200.211.203"
seconds = 2
num_bucles = 5
dades = []
username = "admin"
password = "Kirchoff"
port = 22
hostname = "10.200.211.203"
command = "ls"
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port=port, username=username, password=password)
stdin, stdout, stderr = client.exec_command(command)
s=stdout.read()
s.decode().split()
for i in range(num_bucles):
	cmd = "iperf -c {} -t {} -y C".format(ip_dst,seconds)
	out = subprocess.check_output(cmd.split())
	vel = round(int(out.strip().split(',')[-1])/1000000.0, 2)
	dades.append(vel)
	print(vel)
n_groups = num_bucles
#means_men = (20, 35, 30, 35, 27)
means_men = dades
std_men = (2, 3, 4, 1, 2)
# means_women = (25, 32, 34, 20, 25)
# std_women = (3, 5, 2, 3, 3)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.4
error_config = {'ecolor': '0.3'}
rects1 = plt.bar(index, means_men, bar_width,
                 alpha=opacity,
                 color='b',
                 yerr=std_men,
                 error_kw=error_config,
                 label='Men')
#rects2 = plt.bar(index + bar_width, means_women, bar_width,
                 #alpha=opacity,
                 #color='r',
                 #yerr=std_women,
                 #error_kw=error_config,
                 #label='Women')
plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Test de velocidad del radioenlace')
plt.xticks(index + bar_width, [str(v) for v in dades])
plt.legend()
plt.tight_layout()
plt.show()
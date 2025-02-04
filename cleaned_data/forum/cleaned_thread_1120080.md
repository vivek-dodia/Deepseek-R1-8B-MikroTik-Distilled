# Thread Information
Title: Thread-1120080
Section: RouterOS
Thread ID: 1120080

# Discussion

## Initial Question
HiI have problem to acces to mikrotik sxt lte with vlan mgmt.I have several vlans on bridge-LAN in main router RB5009vlan mgmt from sxt is added to bridge-LAN, dhcp server is setup, and ip is bound to sxt mgmt but i cant conect from winbox.sxt lte mgmt vlan ether 1 -> rb5009 ether3 vlan 200 mgmt (added to bridge-LAN)sxt lte passthrough ether 1 -> rb5009 ether 3 WAN_LTE
```
# 2025-01-11 21:57:53 by RouterOS 7.16.2# software id =## model = RB5009UPr+S+# serial number =/interfacebridgeaddframe-types=admit-only-vlan-tagged name=bridge-LAN vlan-filtering=yes/interfaceethernetset[finddefault-name=ether1]name=ether1-AP_PLACset[finddefault-name=ether2]mac-address=20:E5:2A:23:D2:A9 name=\
    ether2-WAN_SWset[finddefault-name=ether3]name=ether3-WAN_LTEset[finddefault-name=ether4]name=ether4-LANset[finddefault-name=ether5]name=ether5-LAG1set[finddefault-name=ether6]name=ether6-LAG1set[finddefault-name=ether7]name=ether7-LAG2set[finddefault-name=ether8]name=ether8-LAG2/interfacewireguardaddcomment=back-to-home-vpn listen-port=62827mtu=1420name=back-to-home-vpn/interfacevlanaddinterface=bridge-LAN name=VLAN_10_LAN vlan-id=10addinterface=bridge-LAN name=VLAN_20_KAM vlan-id=20addinterface=bridge-LAN name=VLAN_30_IOT vlan-id=30addinterface=bridge-LAN name=VLAN_40_TV vlan-id=40addinterface=bridge-LAN name=VLAN_100_MGMT vlan-id=100addinterface=ether3-WAN_LTE name=VLAN_100_MGMT_LTE vlan-id=10/interfacebondingaddmode=802.3adname=LAG_1_SW_RACK slaves=ether5-LAG1,ether6-LAG1 \
    transmit-hash-policy=layer-2-and-3addmode=802.3adname=LAG_2_SW_RACK_POE slaves=ether7-LAG2,ether8-LAG2 \
    transmit-hash-policy=layer-2-and-3/interfacelistaddname=LANaddname=WAN/ip firewall layer7-protocoladdname=knock1 regexp=addname=knock2 regexp=/ip pooladdname=pool-VLAN_10_LAN ranges=192.168.10.2-192.168.10.254addname=pool-VLAN_20_KAM ranges=192.168.20.2-192.168.20.254addname=pool-VLAN_30_IOT ranges=192.168.30.2-192.168.30.254addname=pool-VLAN_100_MGMT ranges=192.168.100.2-192.168.100.254addname=pool-VLAN_40_TV ranges=192.168.40.2-192.168.40.254/ip dhcp-serveraddadd-arp=yes address-pool=pool-VLAN_10_LANinterface=VLAN_10_LAN name=\
    DHCP_LAN_VLANaddadd-arp=yes address-pool=pool-VLAN_20_KAMinterface=VLAN_20_KAM name=\
    DHCP_KAM_VLANaddadd-arp=yes address-pool=pool-VLAN_30_IOTinterface=VLAN_30_IOT name=\
    DHCP_IOT_VLANaddadd-arp=yes address-pool=pool-VLAN_100_MGMTinterface=VLAN_100_MGMT name=\
    DHCP_MGMT_VLANaddadd-arp=yes address-pool=pool-VLAN_40_TVinterface=VLAN_40_TV name=\
    DHCP_TV_VLAN/snmp communityset[finddefault=yes]name=Zabbix/zerotiersetzt1 comment="ZeroTier Central controller - https://my.zerotier.com/"\
    name=zt1 port=9993/zerotierinterfaceaddallow-default=noallow-global=noallow-managed=yes disabled=noinstance=\
    zt1 name=zt_giolbas network=addallow-default=noallow-global=noallow-managed=yes disabled=noinstance=\
    zt1 name=zt_klozaw network=/interfacebridge portaddbridge=bridge-LANinterface=ether1-AP_PLAC pvid=100addbridge=bridge-LANinterface=LAG_1_SW_RACK pvid=100addbridge=bridge-LANinterface=LAG_2_SW_RACK_POE pvid=100addbridge=bridge-LANinterface=ether4-LAN pvid=10addbridge=bridge-LANinterface=VLAN_100_MGMT_LTE pvid=10/interfacebridge settingssetuse-ip-firewall-for-vlan=yes/ipv6 settingssetdisable-ipv6=yes/interfacebridge vlanaddbridge=bridge-LAN tagged=LAG_1_SW_RACK,LAG_2_SW_RACK_POE,bridge-LAN \
    vlan-ids=10,20,30,40addbridge=bridge-LAN untagged=ether1-AP_PLAC vlan-ids=100/interfacedetect-internetsetdetect-interface-list=WAN internet-interface-list=WAN lan-interface-list=\
    LAN wan-interface-list=WAN/interfacelist memberaddinterface=bridge-LAN list=LANaddinterface=ether1-AP_PLAC list=LANaddinterface=ether4-LAN list=LANaddinterface=ether2-WAN_SW list=WANaddinterface=ether3-WAN_LTE list=WANaddinterface=LAG_1_SW_RACK list=LANaddinterface=LAG_2_SW_RACK_POE list=LANaddinterface=VLAN_10_LAN list=LAN/ip addressaddaddress=192.168.10.1/24interface=VLAN_10_LAN network=192.168.10.0addaddress=192.168.20.1/24interface=VLAN_20_KAM network=192.168.20.0addaddress=192.168.30.1/24interface=VLAN_30_IOT network=192.168.30.0addaddress=192.168.100.1/24interface=VLAN_100_MGMT network=192.168.100.0addaddress=192.168.40.1/24interface=VLAN_40_TV network=192.168.40.0/ip cloudsetback-to-home-vpn=enabled ddns-enabled=yes/ip cloud advancedsetuse-local-address=yes/ip cloud back-to-home-usersaddallow-lan=yes comment=bth-Krisname=Krisprivate-key=\""public-key=\""addallow-lan=yes comment=bth-Basianame=Basiaprivate-key=\""public-key=\""/ip dhcp-clientaddcomment="WAN_SW dhcp client"interface=ether2-WAN_SWuse-peer-dns=no\use-peer-ntp=noaddcomment="WAN_LTE dhcp client"default-route-distance=10interface=\
    ether3-WAN_LTEuse-peer-dns=nouse-peer-ntp=no/ip dhcp-server leaseaddaddress=192.168.40.40comment=Samsung_TV_40calimac-address=\50:85:69:04:1B:C4 server=DHCP_TV_VLANaddaddress=192.168.10.60comment=HP_P1102W mac-address=C4:8E:8F:87:09:34\
    server=DHCP_LAN_VLANaddaddress=192.168.10.31comment=S21_FE_Basia mac-address=F4:02:28:C7:50:3A\
    server=DHCP_LAN_VLANaddaddress=192.168.40.50comment=Samsung_TV_50calimac-address=\
    E4:7D:BD:E7:84:39server=DHCP_TV_VLANaddaddress=192.168.10.4comment=Laptokmac-address=34:13:E8:A4:6F:DC server=\
    DHCP_LAN_VLANaddaddress=192.168.40.60comment="Philips TV 70cali"mac-address=\70:AF:24:C6:56:D0 server=DHCP_TV_VLANaddaddress=192.168.10.30comment="S24 Kris"mac-address=BC:93:07:4C:10:54\
    server=DHCP_LAN_VLANaddaddress=192.168.10.5comment="Laptok Thinkpad"mac-address=\
    F4:A4:75:9F:8E:2Cserver=DHCP_LAN_VLANaddaddress=192.168.100.50comment=QNAP mac-address=6A:0E:3D:04:C8:AC server=\
    DHCP_MGMT_VLANaddaddress=192.168.30.100comment="Roleta Gospodarczy Ogr\F3d_AC"\
    mac-address=80:64:6F:B1:16:6Fserver=DHCP_IOT_VLANaddaddress=192.168.30.102comment=Roleta_Kuchnia_ACmac-address=\4C:75:25:19:60:71server=DHCP_IOT_VLANaddaddress=192.168.30.99comment=MEW-01_Rozdzielniamac-address=\
    CC:50:E3:0D:80:70server=DHCP_IOT_VLANaddaddress=192.168.100.75comment="Mikrotik LTE"mac-address=\
    C4:AD:34:7C:80:FE server=DHCP_MGMT_VLANaddaddress=192.168.30.68comment=Swiatlo_Waszkuchniamac-address=\98:F4:AB:DD:03:E6 server=DHCP_IOT_VLANaddaddress=192.168.30.54comment=Socket_Roletymac-address=BC:DD:C2:10:58:FC \
    server=DHCP_IOT_VLANaddaddress=192.168.30.104comment=Roleta_Salon_ACmac-address=\
    F4:CF:A2:FF:EE:73server=DHCP_IOT_VLANaddaddress=192.168.30.55comment=Czujka_Dymumac-address=EC:FA:BC:28:54:5E\
    server=DHCP_IOT_VLANaddaddress=192.168.30.17comment="Wether Station"mac-address=\
    CC:50:E3:59:65:FF server=DHCP_IOT_VLANaddaddress=192.168.30.18comment="Odkurzacz Xiaomi"mac-address=\
    B0:4A:39:95:D0:67server=DHCP_IOT_VLANaddaddress=192.168.30.19comment="Oczyszczacz Xiaomi"mac-address=\04:CF:8C:94:E4:12server=DHCP_IOT_VLANaddaddress=192.168.30.53comment=Swiatlo_Gospodarczymac-address=\
    AC:0B:FB:D8:DE:4Bserver=DHCP_IOT_VLANaddaddress=192.168.30.52comment=Swiatlo_Tarasmac-address=50:02:91:D1:89:76\
    server=DHCP_IOT_VLANaddaddress=192.168.30.56comment=Sonoff_POW_Piwicamac-address=\
    CC:50:E3:54:1D:92server=DHCP_IOT_VLANaddaddress=192.168.30.58comment=Socket_Szafa_Rackmac-address=\2C:3A:E8:17:75:50server=DHCP_IOT_VLANaddaddress=192.168.30.59comment=Touch_Pokoj_Goscinnymac-address=\60:01:94:A1:5A:89server=DHCP_IOT_VLANaddaddress=192.168.30.60comment=Touch_Sypialniamac-address=\
    DC:4F:22:86:E8:97server=DHCP_IOT_VLANaddaddress=192.168.30.61comment=Sonoff_POW_Sypialniamac-address=\
    C0:49:EF:F3:05:30server=DHCP_IOT_VLANaddaddress=192.168.30.62comment=Touch_Sien_Goramac-address=\60:01:94:98:AF:B1 server=DHCP_IOT_VLANaddaddress=192.168.30.63comment=Touch_Maly_Pokojmac-address=\84:0D:8E:77:36:E4 server=DHCP_IOT_VLANaddaddress=192.168.30.64comment=Yunschan_Altanamac-address=\5C:CF:7F:C3:E9:16server=DHCP_IOT_VLANaddaddress=192.168.30.106comment=Roleta_Pokoj_Kariny_ACmac-address=\
    C8:C9:A3:9F:88:E2 server=DHCP_IOT_VLANaddaddress=192.168.30.107comment=Roleta_Lazienka_ACmac-address=\80:64:6F:B1:12:50server=DHCP_IOT_VLANaddaddress=192.168.30.108comment=Roleta_Sien_ACmac-address=\
    F4:CF:A2:FF:EE:6Cserver=DHCP_IOT_VLANaddaddress=192.168.30.66comment=Touch_Sien_Dolmac-address=\
    DC:4F:22:82:F2:D3 server=DHCP_IOT_VLANaddaddress=192.168.30.109comment=Roleta_Maly_Pokoj_ACmac-address=\4C:75:25:19:29:67server=DHCP_IOT_VLANaddaddress=192.168.30.111comment=Roleta_Pokoj_Goscinnymac-address=\
    AC:0B:FB:D8:BE:B1 server=DHCP_IOT_VLANaddaddress=192.168.30.69comment="Swiatlo Plac"mac-address=\8C:AA:B5:1B:42:49server=DHCP_IOT_VLANaddaddress=192.168.30.114comment="Roleta_Kom\F3rka_AC"mac-address=\
    AC:0B:FB:D8:C8:93server=DHCP_IOT_VLANaddaddress=192.168.30.112comment=Roleta_Sypialnia_ACmac-address=\4C:75:25:19:60:3Dserver=DHCP_IOT_VLANaddaddress=192.168.30.70comment=mROW-01mac-address=98:CD:AC:25:D2:62\
    server=DHCP_IOT_VLANaddaddress=192.168.30.101comment=Roleta_Gospodarczy_Plac_ACmac-address=\80:64:6F:B1:16:71server=DHCP_IOT_VLANaddaddress=192.168.30.71comment=Gate_NICEmac-address=4C:75:25:1A:0F:8E\
    server=DHCP_IOT_VLANaddaddress=192.168.30.103comment=Roleta_Taras_ACmac-address=\
    AC:0B:FB:D9:23:9Dserver=DHCP_IOT_VLANaddaddress=192.168.30.20comment=Glosnik_Googlemac-address=\20:DF:B9:B2:4F:85server=DHCP_IOT_VLANaddaddress=192.168.30.72comment=Oswietlenie_Przodmac-address=\
    E8:68:E7:4E:15:D0 server=DHCP_IOT_VLANaddaddress=192.168.30.73comment=Choinka_Karinamac-address=\70:03:9F:5D:0A:87server=DHCP_IOT_VLANaddaddress=192.168.30.74comment=Gwiazdamac-address=24:A1:60:0A:12:50\
    server=DHCP_IOT_VLANaddaddress=192.168.30.75comment=Dimmer_Schodymac-address=C4:5B:BE:6E:26:DA \
    server=DHCP_IOT_VLANaddaddress=192.168.40.70comment=Chromecastmac-address=14:AE:85:71:BD:AD \
    server=DHCP_TV_VLANaddaddress=192.168.10.50comment="Fenix 7X"mac-address=90:F1:57:AF:8D:75\
    server=DHCP_LAN_VLANaddaddress=192.168.30.16comment="Falownik Huawei"mac-address=\9C:B2:E8:2C:47:05server=DHCP_IOT_VLANaddaddress=192.168.30.98comment=MEW-02_Ogrzewaniemac-address=\7C:87:CE:F3:7A:87server=DHCP_IOT_VLANaddaddress=192.168.30.200comment="Termostat Pokoj Kariny"mac-address=\
    EC:FA:BC:76:31:23server=DHCP_IOT_VLANaddaddress=192.168.30.201comment="Termostat Salon"mac-address=\
    EC:FA:BC:76:2E:19server=DHCP_IOT_VLANaddaddress=192.168.30.202comment="Termostat Kuchnia"mac-address=\
    EC:FA:BC:76:27:C0 server=DHCP_IOT_VLANaddaddress=192.168.30.203comment="Termostat Komorka"mac-address=\
    EC:FA:BC:76:24:7Fserver=DHCP_IOT_VLANaddaddress=192.168.30.204comment="Termostat Lazienka"mac-address=\
    E0:98:06:1F:4D:51server=DHCP_IOT_VLANaddaddress=192.168.30.206comment="Termostat Maly Pokoj"mac-address=\8C:AA:B5:FD:ED:4Eserver=DHCP_IOT_VLANaddaddress=192.168.30.208comment="Termostat Sien Gora"mac-address=\8C:AA:B5:FD:61:53server=DHCP_IOT_VLANaddaddress=192.168.30.205comment="Termostat Sypialnia"mac-address=\
    EC:FA:BC:76:23:D7 server=DHCP_IOT_VLANaddaddress=192.168.30.207comment="Termostat Pokoj Goscinny"mac-address=\8C:AA:B5:57:8A:44server=DHCP_IOT_VLANaddaddress=192.168.30.210comment="Termostat Sien Dol"mac-address=\
    EC:FA:BC:76:2E:66server=DHCP_IOT_VLANaddaddress=192.168.30.209comment="Termostat Lauba"mac-address=\
    EC:FA:BC:76:30:72server=DHCP_IOT_VLANaddaddress=192.168.30.24comment="HA dev"mac-address=02:07:E1:4C:43:F8 \
    server=DHCP_IOT_VLANaddaddress=192.168.10.181comment="Pv Ubuntu"mac-address=2A:4A:86:F1:F9:86\
    server=DHCP_LAN_VLANaddaddress=192.168.10.182comment="Pv Win11"mac-address=5E:26:27:1B:10:84\
    server=DHCP_LAN_VLANaddaddress=192.168.100.210comment=AP_GORA mac-address=60:22:32:3F:26:E4 \
    server=DHCP_MGMT_VLANaddaddress=192.168.10.40comment="Yamacha glosnik"mac-address=\40:06:A0:84:3B:7Aserver=DHCP_LAN_VLANaddaddress=192.168.30.97comment=LEW_Serwerownia mac-address=\58:BF:25:40:8A:BF server=DHCP_IOT_VLANaddaddress=192.168.30.57comment=Sonoff_POW_Kuchniamac-address=\84:F3:EB:B1:D3:05server=DHCP_IOT_VLANaddaddress=192.168.10.190comment=Terminal_HPmac-address=FC:3F:DB:04:4E:6C\
    server=DHCP_LAN_VLANaddaddress=192.168.30.76comment=OLED mac-address=84:F3:EB:E3:A1:EF server=\
    DHCP_IOT_VLANaddaddress=192.168.30.77comment=Bramka_Versamac-address=AC:0B:FB:E9:5A:1C\
    server=DHCP_IOT_VLANaddaddress=192.168.30.78comment="Swiatlo Piwnica"mac-address=\8C:AA:B5:1B:39:95server=DHCP_IOT_VLANaddaddress=192.168.30.220comment=Piec_Wifimac-address=84:F7:03:E0:54:4C\
    server=DHCP_IOT_VLANaddaddress=192.168.30.211comment=Termostat_Gospodarczymac-address=\
    EC:FA:BC:76:2D:9Bserver=DHCP_IOT_VLANaddaddress=192.168.40.20comment="C+ SYPIALNIA"mac-address=\
    C4:77:AF:54:EA:F7 server=DHCP_TV_VLANaddaddress=192.168.40.30comment="C+ karina"mac-address=C4:77:AF:54:F2:F2 \
    server=DHCP_TV_VLANaddaddress=192.168.40.10comment="C+ KUCHNIA"mac-address=C4:77:AF:54:EC:8D\
    server=DHCP_TV_VLANaddaddress=192.168.30.23comment="Pv Ubuntu-supla-dev"mac-address=\
    BC:24:11:AF:64:5Aserver=DHCP_IOT_VLANaddaddress=192.168.10.32comment=S10_Karina mac-address=72:9C:9C:FB:AB:12\
    server=DHCP_LAN_VLANaddaddress=192.168.30.79comment=Gniazdko_Bojlermac-address=\
    CC:50:E3:26:2C:D2 server=DHCP_IOT_VLANaddaddress=192.168.30.115comment=Rolety_Markiza_ACmac-address=\50:02:91:D2:47:77server=DHCP_IOT_VLANaddaddress=192.168.30.230comment="Bramka Auraton"mac-address=\9C:9E:6E:F0:3F:BC server=DHCP_IOT_VLANaddaddress=192.168.100.60comment="SERVER OSCAM"mac-address=\94:83:C4:07:3A:1Dserver=DHCP_MGMT_VLANaddaddress=192.168.100.140comment=SW_POKOJ_KARINY mac-address=\
    B0:95:75:84:1F:C9 server=DHCP_MGMT_VLANaddaddress=192.168.100.220comment=AP_SIEN mac-address=74:83:C2:90:40:0F\
    server=DHCP_MGMT_VLANaddaddress=192.168.100.40comment="DELL IDRAC"mac-address=18:66:DA:B2:B3:88\
    server=DHCP_MGMT_VLANaddaddress=192.168.100.100comment=SW_RACK_POE mac-address=1C:61:B4:B9:4A:CF \
    server=DHCP_MGMT_VLANaddaddress=192.168.100.10comment=PROXMOX mac-address=18:66:DA:B2:B3:84\
    server=DHCP_MGMT_VLANaddaddress=192.168.100.130comment=SW_MALY_POKOJ mac-address=\84:D8:1B:57:B8:52server=DHCP_MGMT_VLANaddaddress=192.168.100.120comment=SW_GOSPODARCZY mac-address=\
    B0:BE:76:89:5B:66server=DHCP_MGMT_VLANaddaddress=192.168.100.160comment=SW_WARSZTAT mac-address=84:D8:1B:DA:63:16\
    server=DHCP_MGMT_VLANaddaddress=192.168.100.190comment=SW_KUCHNIA mac-address=70:A7:41:79:85:15\
    server=DHCP_MGMT_VLANaddaddress=192.168.100.90comment=ALARM mac-address=00:1B:9C:0C:15:8A\
    server=DHCP_MGMT_VLANaddaddress=192.168.100.150comment=SW_SYPIALNIA mac-address=\84:D8:1B:57:B8:4Eserver=DHCP_MGMT_VLANaddaddress=192.168.100.85comment=RPI5 mac-address=2C:CF:67:83:89:B7 server=\
    DHCP_MGMT_VLANaddaddress=192.168.100.30comment="UNIFI CONTROLLER"mac-address=\70:A7:41:79:FC:A1 server=DHCP_MGMT_VLANaddaddress=192.168.30.25comment=HA mac-address=02:B7:0C:22:CA:3Fserver=\
    DHCP_IOT_VLANaddaddress=192.168.100.110comment=SW_RACK mac-address=28:87:BA:66:D8:22\
    server=DHCP_MGMT_VLANaddaddress=192.168.100.20comment="OMADA CONTROLLER"mac-address=\36:62:C1:9A:F1:F8 server=DHCP_MGMT_VLANaddaddress=192.168.30.21comment="Licznik wody"mac-address=\
    FC:E8:C0:A0:89:8Cserver=DHCP_IOT_VLANaddaddress=192.168.40.80comment="SONY N720"mac-address=3C:07:71:7D:41:40\
    server=DHCP_TV_VLANaddaddress=192.168.100.240comment=AP_PLAC mac-address=74:83:C2:C9:1E:F7 \
    server=DHCP_MGMT_VLANaddaddress=192.168.100.250comment=AP_PIWNICA mac-address=18:E8:29:96:4A:31\
    server=DHCP_MGMT_VLANaddaddress=192.168.100.200comment=AP_DOL mac-address=70:A7:41:D7:28:A8 \
    server=DHCP_MGMT_VLANaddaddress=192.168.100.230comment=AP_GOSPODARCZY mac-address=\74:83:C2:36:6F:31server=DHCP_MGMT_VLANaddaddress=192.168.100.70comment=ZABBIX mac-address=06:32:B1:B3:9D:F9 \
    server=DHCP_MGMT_VLANaddaddress=192.168.30.22comment="SUPLA_DEVICE WEATHER STATION"mac-address=\
    BC:24:11:60:CE:52server=DHCP_IOT_VLANaddaddress=192.168.100.80comment=UPS_SERVER mac-address=BC:24:11:75:17:12\
    server=DHCP_MGMT_VLANaddaddress=192.168.30.10comment="Serwer SUPLA"mac-address=\
    BC:24:11:2C:39:C0 server=DHCP_IOT_VLAN/ip dhcp-server networkaddaddress=192.168.10.0/24dns-server=8.8.8.8gateway=192.168.10.1addaddress=192.168.20.0/24dns-server=8.8.8.8gateway=192.168.20.1addaddress=192.168.30.0/24dns-server=8.8.8.8gateway=192.168.30.1addaddress=192.168.40.0/24dns-server=8.8.8.8gateway=192.168.40.1addaddress=192.168.100.0/24dns-server=8.8.8.8gateway=192.168.100.1/ip dnssetallow-remote-requests=yes servers=8.8.8.8verify-doh-cert=yes/ip dnsstaticaddaddress=disabled=yes name=supla.krissg.ovh type=A/ip firewall address-listaddaddress=192.168.10.0/24list=WAN_Allowaddaddress=192.168.20.0/24list=WAN_Allowaddaddress=5.173.0.0/16list=WAN_Allowaddaddress=77.65.117.126list=WAN_Allowaddaddress=188.123.223.100list=WAN_Allowaddaddress=94.254.0.0/16list=WAN_Allowaddaddress=35.214.214.56list=WAN_Allowaddaddress=35.214.244.97list=WAN_Allowaddaddress=cloud.supla.org list=WAN_Allowaddaddress=91.192.0.86list=WAN_Allowaddaddress=call.supla.io list=WAN_Allowaddaddress=91.192.2.99list=WAN_Allowaddaddress=googleassistant.supla.org list=WAN_Allowaddaddress=192.168.30.0/24list=WAN_Allowaddaddress=89.64.58.84list=WAN_Allowaddaddress=193.186.4.0/24disabled=yes list=WAN_Allowaddaddress=46.112.76.0/24disabled=yes list=WAN_Allowaddaddress=icons.supla.io list=WAN_Allowaddaddress=plex.tv list=WAN_Allowaddaddress=54.170.120.91list=WAN_Allowaddaddress=46.51.207.89list=WAN_Allowaddaddress=142.250.191.46list=WAN_Allowaddaddress=192.168.100.0/24list=WAN_Allowaddaddress=78.28.208.99list=WAN_Allowaddaddress=192.168.216.0/24list=WAN_Allow/ip firewall filteraddaction=accept chain=input dst-port=53in-interface=VLAN_10_LAN protocol=\
    tcpaddaction=accept chain=input dst-port=53in-interface=VLAN_10_LAN protocol=\
    udpaddaction=drop chain=input comment="Blokada ruchu z zt_giolbas to lan"\
    dst-address=192.168.10.0/24in-interface=zt_giolbas src-mac-address=\!34:13:E8:A4:6F:DCaddaction=accept chain=forwardin-interface=zt_klozawaddaction=accept chain=forwardin-interface=zt_giolbasaddaction=accept chain=inputin-interface=zt_klozawaddaction=accept chain=inputin-interface=zt_giolbasaddaction=drop chain=input disabled=yesin-interface=zt_giolbas src-address=\10.147.20.14addaction=add-src-to-address-list address-list=Knock_list\
    address-list-timeout=1mchain=input comment=Knockdst-port=\
    layer7-protocol=knock1 protocol=udpaddaction=add-src-to-address-list address-list=Knock_list2\
    address-list-timeout=1mchain=input dst-port=layer7-protocol=knock2 \
    protocol=udp src-address-list=Knock_listaddaction=add-src-to-address-list address-list=WAN_Allow \
    address-list-timeout=1d5hchain=input dst-port=log=yes log-prefix=\
    port_knock protocol=tcp src-address-list=Knock_list2addaction=drop chain=input comment="Port  Scan"src-address-list=\
    port-scanneraddaction=add-src-to-address-list address-list=port-scanner \
    address-list-timeout=1dchain=inputin-interface-list=WAN protocol=tcp \
    psd=21,3s,3,1addaction=add-src-to-address-list address-list=port-scanner \
    address-list-timeout=1wchain=inputin-interface-list=WAN protocol=udp \
    psd=21,3s,3,1addaction=accept chain=input comment="Accept established,related,untracked"\
    connection-state=established,related,untrackedaddaction=drop chain=input comment="Drop invalid"connection-state=invalidaddaction=jump chain=input comment="!!! Check for well-known viruses !!!"\
    jump-target=virusaddaction=accept chain=input comment="Winbox from WAN (WAN Allow)"dst-port=\1818protocol=tcp src-address-list=WAN_Allowaddaction=accept chain=input comment="Accept ICMP"protocol=icmpaddaction=drop chain=input comment="Drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="Accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="Accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment=Fasttrack\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"Accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="Drop invalid"connection-state=invalidaddaction=jump chain=forward comment="!!! Check for well-known viruses !!!"\
    jump-target=virusaddaction=drop chain=forward comment="Drop all from WAN not DSTNATed"\
    connection-nat-state=!dstnat connection-state=newin-interface-list=WANaddaction=drop chain=input comment="Drop everything else"log-prefix=DROPaddaction=accept chain=forward comment="Established connections"\
    connection-state=establishedaddaction=accept chain=forward comment="Related connections"\
    connection-state=relatedaddaction=drop chain=forward comment="Drop invalid connections"\
    connection-state=invalid log-prefix=INVALIDaddaction=drop chain=virus comment="Drop Blaster Worm"dst-port=135-139\
    protocol=tcpaddaction=drop chain=virus comment="Drop Messenger Worm"dst-port=135-139\
    protocol=udpaddaction=drop chain=virus comment="Drop Blaster Worm"dst-port=445\
    protocol=tcpaddaction=drop chain=virus comment="Drop Blaster Worm"dst-port=445\
    protocol=udpaddaction=drop chain=virus comment=________ dst-port=593protocol=tcpaddaction=drop chain=virus comment=________ dst-port=1024-1030protocol=tcpaddaction=drop chain=virus comment="Drop MyDoom"dst-port=1080protocol=tcpaddaction=drop chain=virus comment=________ dst-port=1214protocol=tcpaddaction=drop chain=virus comment="ndm requester"dst-port=1363protocol=\
    tcpaddaction=drop chain=virus comment="ndm server"dst-port=1364protocol=tcpaddaction=drop chain=virus comment="screen cast"dst-port=1368protocol=tcpaddaction=drop chain=virus comment=hromgrafx dst-port=1373protocol=tcpaddaction=drop chain=virus comment=cichlid dst-port=1377protocol=tcpaddaction=drop chain=virus comment=Wormdst-port=1433-1434protocol=tcpaddaction=drop chain=virus comment="Bagle Virus"dst-port=2745protocol=tcpaddaction=drop chain=virus comment="Drop Dumaru.Y"dst-port=2283protocol=\
    tcpaddaction=drop chain=virus comment="Drop Beagle"dst-port=2535protocol=tcpaddaction=drop chain=virus comment="Drop Beagle.C-K"dst-port=2745protocol=\
    tcpaddaction=drop chain=virus comment="Drop MyDoom"dst-port=3127-3128\
    protocol=tcpaddaction=drop chain=virus comment="Drop Backdoor OptixPro"dst-port=3410\
    protocol=tcpaddaction=drop chain=virus comment=Wormdst-port=4444protocol=tcpaddaction=drop chain=virus comment=Wormdst-port=4444protocol=udpaddaction=drop chain=virus comment="Drop Sasser"dst-port=5554protocol=tcpaddaction=drop chain=virus comment="Drop Beagle.B"dst-port=8866protocol=\
    tcpaddaction=drop chain=virus comment="Drop Dabber.A-B"dst-port=9898protocol=\
    tcpaddaction=drop chain=virus comment="Drop Dumaru.Y"dst-port=10000protocol=\
    tcpaddaction=drop chain=virus comment="Drop MyDoom.B"dst-port=10080protocol=\
    tcpaddaction=drop chain=virus comment="Drop NetBus"dst-port=12345protocol=tcpaddaction=drop chain=virus comment="Drop Kuang2"dst-port=17300protocol=tcpaddaction=drop chain=virus comment="Drop SubSeven"dst-port=27374protocol=\
    tcpaddaction=drop chain=virus comment="Drop PhatBot, Agobot, Gaobot"dst-port=\65506protocol=tcp/ip firewall nataddaction=masquerade chain=srcnat comment="WAN_SW masquerade"out-interface=\
    ether2-WAN_SWaddaction=masquerade chain=srcnat comment="WAN_LTE masquerade"\out-interface=ether3-WAN_LTEaddaction=masquerade chain=srcnat src-address=192.168.10.0/24addaction=masquerade chain=srcnat src-address=192.168.20.0/24addaction=masquerade chain=srcnat src-address=192.168.30.0/24addaction=masquerade chain=srcnat src-address=192.168.100.0/24addaction=dst-nat chain=dstnat comment=Alarmdst-address=x.x.x.x \
    dst-port=1616protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.100.90to-ports=1515addaction=dst-nat chain=dstnat comment=UpSrvdst-address=x.x.x.x \
    dst-port=44044protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.10.4to-ports=44004addaction=dst-nat chain=dstnat comment="Proxmox vnc"disabled=yes \
    dst-address=x.x.x.x dst-port=5900-5999protocol=tcp \
    src-address-list=WAN_Allow to-addresses=192.168.10.180to-ports=5900-5999addaction=src-nat chain=srcnat disabled=yes dst-address=192.168.10.150\
    protocol=tcp src-address=192.168.10.0/24to-addresses=192.168.10.1addaction=dst-nat chain=dstnat comment="Supla app ssl"dst-address=\
    x.x.x.x dst-port=2016protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.30.10to-ports=2016addaction=dst-nat chain=dstnat comment="Supla app nossl"dst-address=\
    x.x.x.x dst-port=2015protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.30.10to-ports=2015addaction=dst-nat chain=dstnat comment="Nginx WEB"disabled=yes dst-address=\
    x.x.x.x dst-port=443protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.10.20to-ports=35443addaction=dst-nat chain=dstnat comment="Nginx WEB https"dst-address=\
    x.x.x.x dst-port=443log-prefix=nginx protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.30.10to-ports=443addaction=dst-nat chain=dstnat comment="Nginx WEB http"dst-address=\
    x.x.x.x dst-port=80log=yes log-prefix=nginx protocol=tcp \
    src-address-list=WAN_Allow to-addresses=192.168.30.10to-ports=82addaction=dst-nat chain=dstnat comment="Nginx proxy"disabled=yes \
    dst-address=x.x.x.x dst-port=8881protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.120to-ports=89addaction=dst-nat chain=dstnat comment="Supla scripts"disabled=yes \
    dst-address=x.x.x.x dst-port=4434protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.120to-ports=4432addaction=dst-nat chain=dstnat comment=Transmissiondst-address=x.x.x.x \
    dst-port=49092protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.100.50to-ports=9091addaction=dst-nat chain=dstnat comment="Transmissin wyjscie"dst-address=\
    x.x.x.x dst-port=51413protocol=tcp to-addresses=192.168.100.50\
    to-ports=51413addaction=dst-nat chain=dstnat disabled=yes dst-address=x.x.x.x \
    dst-port=51414protocol=udp to-addresses=192.168.10.20to-ports=51414addaction=dst-nat chain=dstnat comment="OSCAM Svr"disabled=yes dst-address=\
    x.x.x.x dst-port=9999protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.10.50to-ports=8888addaction=dst-nat chain=dstnat comment="OSCAM wyjscie"disabled=yes \
    dst-address=x.x.x.x dst-port=7777protocol=tcp to-addresses=\192.168.10.50to-ports=7777addaction=dst-nat chain=dstnat comment="Oscam svr ssh"disabled=yes \
    dst-address=x.x.x.x dst-port=444protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.50to-ports=22addaction=dst-nat chain=dstnat comment="Oscam svr https"disabled=yes \
    dst-address=x.x.x.x dst-port=8000protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.50to-ports=443addaction=dst-nat chain=dstnat comment="Qnap file browser"dst-address=\
    x.x.x.x dst-port=3678protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.100.50to-ports=3678addaction=dst-nat chain=dstnat comment="Magazyn FTP"dst-address=\
    x.x.x.x dst-port=1106log=yes log-prefix="FTP TEST kristel"\
    protocol=tcp src-address-list=WAN_Allow to-addresses=192.168.100.50\
    to-ports=21addaction=dst-nat chain=dstnat dst-address=x.x.x.x dst-port=55536-55556\
    log=yes log-prefix="FTP TEST kristel"protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.100.50to-ports=55536-55556addaction=dst-nat chain=dstnat comment="Magazyn SSH"dst-address=\
    x.x.x.x dst-port=7922protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.100.50to-ports=22addaction=dst-nat chain=dstnat comment="Magazyn WWW"disabled=yes \
    dst-address=x.x.x.x dst-port=4439protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.20to-ports=4439addaction=dst-nat chain=dstnat disabled=yes dst-address=x.x.x.x \
    dst-port=8089protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.10.20to-ports=8089addaction=dst-nat chain=dstnat comment=OwnClouddisabled=yes dst-address=\
    x.x.x.x dst-port=25639protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.10.20to-ports=25639addaction=dst-nat chain=dstnat comment="TP-LINK Omada"disabled=yes \
    dst-address=x.x.x.x dst-port=8043protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.20to-ports=8043addaction=dst-nat chain=dstnat comment=NVR dst-address=x.x.x.x \
    dst-port=3733protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.20.2to-ports=37777addaction=dst-nat chain=dstnat comment="FSB web"disabled=yes dst-address=\
    x.x.x.x dst-port=6530protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.10.20to-ports=4530addaction=dst-nat chain=dstnat comment="Malina SSH"dst-address=x.x.x.x \
    dst-port=7923protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.30.10to-ports=22addaction=dst-nat chain=dstnat comment="IDRAC vnc"dst-address=x.x.x.x \
    dst-port=5900protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.100.40to-ports=5900addaction=dst-nat chain=dstnat comment="Malina VNC"disabled=yes \
    dst-address=x.x.x.x dst-port=5900protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.120to-ports=5900addaction=dst-nat chain=dstnat comment="Traccar wyjscie"dst-address=\
    x.x.x.x dst-port=5027protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.30.10to-ports=5027addaction=dst-nat chain=dstnat comment="Malina Unifi"disabled=yes \
    dst-address=x.x.x.x dst-port=8843protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.184to-ports=8843addaction=dst-nat chain=dstnat comment="Winbox LTE"dst-address=x.x.x.x \
    dst-port=1919protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.10.200to-ports=1919addaction=dst-nat chain=dstnat comment="Malina OSCAM"disabled=yes \
    dst-address=x.x.x.x dst-port=8001protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.120to-ports=8888addaction=dst-nat chain=dstnat comment=PLEX dst-address=x.x.x.x \
    dst-port=32400protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.100.50to-ports=32400addaction=dst-nat chain=dstnat comment="apache WWW"disabled=yes \
    dst-address=x.x.x.x dst-port=80protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.120to-ports=80addaction=dst-nat chain=dstnat disabled=yes dst-address=!192.168.88.254\
    dst-port=91protocol=tcp to-addresses=192.168.88.254to-ports=88addaction=dst-nat chain=dstnat comment="Unifi Console"disabled=yes \
    dst-address=x.x.x.x dst-port=3478protocol=udp src-address-list=\
    WAN_Allow to-addresses=192.168.10.115/ip firewall service-portsetftp disabled=yessetsip disabled=yes/ip routeaddcomment="Dual Wan - Check gateway WAN_SW"dst-address=8.8.8.8gateway=\91.195.92.1scope=10addcomment="Dual Wan - Check gateway WAN_LTE"dst-address=8.8.4.4gateway=\10.118.186.49scope=10addcheck-gateway=ping comment="Dual Wan - WAN_SW"distance=1gateway=8.8.8.8\
    target-scope=11addcheck-gateway=ping comment="Dual Wan - WAN_LTE"distance=2gateway=\8.8.4.4target-scope=11addcomment="Dual Wan - Check gateway WAN_SW second"dst-address=\208.67.222.222gateway=91.195.92.1scope=10addcomment="Dual Wan - Check gateway WAN_LTE second"dst-address=\208.67.220.220gateway=10.118.186.49scope=10addcheck-gateway=ping comment="Dual Wan - WAN_SW second"distance=1gateway=\208.67.222.222target-scope=11addcheck-gateway=ping comment="Dual Wan - WAN_LTE second"distance=2\
    gateway=208.67.220.220target-scope=11/ip servicesettelnet disabled=yessetftp disabled=yessetssh disabled=yessetapi disabled=yessetwinbox port=1818setapi-ssl disabled=yes/snmpsetenabled=yes trap-generators=interfaces trap-interfaces=bridge-LAN \
    trap-target=192.168.100.70trap-version=2/system clocksettime-zone-name=Europe/Warsaw/system identitysetname=Mietek/system notesetshow-at-login=no

---
```

## Response 1
sxt lte mgmt vlan ether 1 -> rb5009 ether3 vlan 200 mgmt (added to bridge-LAN)sxt lte passthrough ether 1 -> rb5009 ether 3 WAN_LTEWhat you describe doesn't seem to match with your config:
```
/interfacevlanaddinterface=bridge-LAN name=VLAN_10_LAN vlan-id=10addinterface=bridge-LAN name=VLAN_20_KAM vlan-id=20addinterface=bridge-LAN name=VLAN_30_IOT vlan-id=30addinterface=bridge-LAN name=VLAN_40_TV vlan-id=40addinterface=bridge-LAN name=VLAN_100_MGMT vlan-id=100addinterface=ether3-WAN_LTE name=VLAN_100_MGMT_LTE vlan-id=10There is no vlan 200 and the one on ether2-WAN-LTE is 100 in the comment but actually 10 in the ccnfigurationTypos?

---
```

## Response 2
Sorry you are right wrong config my mistakethis is correct:
```
# 2025-01-19 12:53:29 by RouterOS 7.17# software id =## model = RB5009UPr+S+# serial number =/interfacebridgeaddingress-filtering=noname=bridge-LAN pvid=200vlan-filtering=yes/interfaceethernetset[finddefault-name=ether1]name=ether1-AP_PLACset[finddefault-name=ether2]mac-address=20:E5:2A:23:D2:A9 name=\
    ether2-WAN_SWset[finddefault-name=ether3]name=ether3-WAN_LTEset[finddefault-name=ether4]name=ether4-LANset[finddefault-name=ether5]name=ether5-LAG1set[finddefault-name=ether6]name=ether6-LAG1set[finddefault-name=ether7]name=ether7-LAG2set[finddefault-name=ether8]name=ether8-LAG2/interfacewireguardaddcomment=back-to-home-vpn listen-port=62827mtu=1420name=back-to-home-vpn/interfacevlanaddinterface=bridge-LAN name=VLAN_10_LAN vlan-id=10addinterface=bridge-LAN name=VLAN_20_KAM vlan-id=20addinterface=bridge-LAN name=VLAN_30_IOT vlan-id=30addinterface=bridge-LAN name=VLAN_40_TV vlan-id=40addinterface=bridge-LAN name=VLAN_100_MGMT vlan-id=100addinterface=ether3-WAN_LTE name=VLAN_200_MGMT_LTE vlan-id=200/interfacebondingaddmode=802.3adname=LAG_1_SW_RACK slaves=ether5-LAG1,ether6-LAG1 \
    transmit-hash-policy=layer-2-and-3addmode=802.3adname=LAG_2_SW_RACK_POE slaves=ether7-LAG2,ether8-LAG2 \
    transmit-hash-policy=layer-2-and-3/interfacelistaddname=LANaddname=WAN/ip firewall layer7-protocoladdname=knock1 regexp=addname=knock2 regexp=/ip pooladdname=pool-VLAN_10_LAN ranges=192.168.10.2-192.168.10.254addname=pool-VLAN_20_KAM ranges=192.168.20.2-192.168.20.254addname=pool-VLAN_30_IOT ranges=192.168.30.2-192.168.30.254addname=pool-VLAN_100_MGMT ranges=192.168.100.2-192.168.100.254addname=pool-VLAN_40_TV ranges=192.168.40.2-192.168.40.254addname=pool-VLAN_200_MGMT_LTE ranges=192.168.200.2-192.168.200.5/ip dhcp-serveraddadd-arp=yes address-pool=pool-VLAN_10_LANinterface=VLAN_10_LAN name=\
    DHCP_LAN_VLANaddadd-arp=yes address-pool=pool-VLAN_20_KAMinterface=VLAN_20_KAM name=\
    DHCP_KAM_VLANaddadd-arp=yes address-pool=pool-VLAN_30_IOTinterface=VLAN_30_IOT name=\
    DHCP_IOT_VLANaddadd-arp=yes address-pool=pool-VLAN_100_MGMTinterface=VLAN_100_MGMT name=\
    DHCP_MGMT_VLANaddadd-arp=yes address-pool=pool-VLAN_40_TVinterface=VLAN_40_TV name=\
    DHCP_TV_VLANaddadd-arp=yes address-pool=pool-VLAN_200_MGMT_LTEinterface=bridge-LAN \
    name=DHCP_MGMT_LTE_VLAN/snmp communityset[finddefault=yes]name=Zabbix/zerotiersetzt1 disabled=nodisabled=no/zerotierinterfaceaddallow-default=noallow-global=noallow-managed=yes disabled=noinstance=\
    zt1 name=zt_giolbas network=272f5eae1601ff8eaddallow-default=noallow-global=noallow-managed=yes disabled=noinstance=\
    zt1 name=zt_klozaw network=d5e5fb653725c597/interfacebridge portaddbridge=bridge-LANinterface=ether1-AP_PLAC pvid=100addbridge=bridge-LAN ingress-filtering=nointerface=LAG_1_SW_RACK pvid=100addbridge=bridge-LAN ingress-filtering=nointerface=LAG_2_SW_RACK_POE pvid=\100addbridge=bridge-LANinterface=ether4-LAN pvid=10addbridge=bridge-LANinterface=VLAN_200_MGMT_LTE pvid=200/interfacebridge settingssetuse-ip-firewall-for-vlan=yes/ipv6 settingssetdisable-ipv6=yes/interfacebridge vlanaddbridge=bridge-LAN tagged=LAG_1_SW_RACK,LAG_2_SW_RACK_POE,bridge-LAN \
    vlan-ids=10,20,30,40addbridge=bridge-LAN untagged=ether1-AP_PLAC vlan-ids=100addbridge=bridge-LAN tagged=VLAN_200_MGMT_LTE untagged=bridge-LAN vlan-ids=\200/interfacedetect-internetsetdetect-interface-list=WAN internet-interface-list=WAN lan-interface-list=\
    LAN wan-interface-list=WAN/interfacelist memberaddinterface=bridge-LAN list=LANaddinterface=ether1-AP_PLAC list=LANaddinterface=ether4-LAN list=LANaddinterface=ether2-WAN_SW list=WANaddinterface=ether3-WAN_LTE list=WANaddinterface=LAG_1_SW_RACK list=LANaddinterface=LAG_2_SW_RACK_POE list=LANaddinterface=VLAN_10_LAN list=LANaddinterface=VLAN_200_MGMT_LTE list=LAN/interfaceovpn-server serveraddmac-address=FE:56:1F:D7:87:1Cname=ovpn-server1/ip addressaddaddress=192.168.10.1/24interface=VLAN_10_LAN network=192.168.10.0addaddress=192.168.20.1/24interface=VLAN_20_KAM network=192.168.20.0addaddress=192.168.30.1/24interface=VLAN_30_IOT network=192.168.30.0addaddress=192.168.100.1/24interface=VLAN_100_MGMT network=192.168.100.0addaddress=192.168.40.1/24interface=VLAN_40_TV network=192.168.40.0addaddress=192.168.200.1/24interface=VLAN_200_MGMT_LTE network=\192.168.200.0/ip cloudsetback-to-home-vpn=enabled ddns-enabled=yes/ip cloud advancedsetuse-local-address=yes/ip cloud back-to-home-usersaddallow-lan=yes comment=bth-Krisname=Krisprivate-key=\""public-key=\""addallow-lan=yes comment=bth-Basianame=Basiaprivate-key=\""public-key=\""/ip dhcp-clientaddcomment="WAN_SW dhcp client"interface=ether2-WAN_SWuse-peer-dns=no\use-peer-ntp=noaddcomment="WAN_LTE dhcp client"default-route-distance=10interface=\
    ether3-WAN_LTEuse-peer-dns=nouse-peer-ntp=no/ip dhcp-server leaseaddaddress=192.168.40.40comment=Samsung_TV_40calimac-address=\50:85:69:04:1B:C4 server=DHCP_TV_VLANaddaddress=192.168.10.60comment=HP_P1102W mac-address=C4:8E:8F:87:09:34\
    server=DHCP_LAN_VLANaddaddress=192.168.10.31comment=S21_FE_Basia mac-address=F4:02:28:C7:50:3A\
    server=DHCP_LAN_VLANaddaddress=192.168.40.50comment=Samsung_TV_50calimac-address=\
    E4:7D:BD:E7:84:39server=DHCP_TV_VLANaddaddress=192.168.10.4comment=Laptokmac-address=34:13:E8:A4:6F:DC server=\
    DHCP_LAN_VLANaddaddress=192.168.40.60comment="Philips TV 70cali"mac-address=\70:AF:24:C6:56:D0 server=DHCP_TV_VLANaddaddress=192.168.10.30comment="S24 Kris"mac-address=BC:93:07:4C:10:54\
    server=DHCP_LAN_VLANaddaddress=192.168.10.5comment="Laptok Thinkpad"mac-address=\
    F4:A4:75:9F:8E:2Cserver=DHCP_LAN_VLANaddaddress=192.168.30.100comment="Roleta Gospodarczy Ogr\F3d_AC"\
    mac-address=80:64:6F:B1:16:6Fserver=DHCP_IOT_VLANaddaddress=192.168.30.102comment=Roleta_Kuchnia_ACmac-address=\4C:75:25:19:60:71server=DHCP_IOT_VLANaddaddress=192.168.30.99comment=MEW-01_Rozdzielniamac-address=\
    CC:50:E3:0D:80:70server=DHCP_IOT_VLANaddaddress=192.168.100.75comment="Mikrotik LTE"mac-address=\
    C4:AD:34:7C:80:FE server=DHCP_MGMT_VLANaddaddress=192.168.30.68comment=Swiatlo_Waszkuchniamac-address=\98:F4:AB:DD:03:E6 server=DHCP_IOT_VLANaddaddress=192.168.30.54comment=Socket_Roletymac-address=BC:DD:C2:10:58:FC \
    server=DHCP_IOT_VLANaddaddress=192.168.30.104comment=Roleta_Salon_ACmac-address=\
    F4:CF:A2:FF:EE:73server=DHCP_IOT_VLANaddaddress=192.168.30.55comment=Czujka_Dymumac-address=EC:FA:BC:28:54:5E\
    server=DHCP_IOT_VLANaddaddress=192.168.30.17comment="Wether Station"mac-address=\
    CC:50:E3:59:65:FF server=DHCP_IOT_VLANaddaddress=192.168.30.18comment="Odkurzacz Xiaomi"mac-address=\
    B0:4A:39:95:D0:67server=DHCP_IOT_VLANaddaddress=192.168.30.19comment="Oczyszczacz Xiaomi"mac-address=\04:CF:8C:94:E4:12server=DHCP_IOT_VLANaddaddress=192.168.30.53comment=Swiatlo_Gospodarczymac-address=\
    AC:0B:FB:D8:DE:4Bserver=DHCP_IOT_VLANaddaddress=192.168.30.52comment=Swiatlo_Tarasmac-address=50:02:91:D1:89:76\
    server=DHCP_IOT_VLANaddaddress=192.168.30.56comment=Sonoff_POW_Piwicamac-address=\
    CC:50:E3:54:1D:92server=DHCP_IOT_VLANaddaddress=192.168.30.58comment=Socket_Szafa_Rackmac-address=\2C:3A:E8:17:75:50server=DHCP_IOT_VLANaddaddress=192.168.30.59comment=Touch_Pokoj_Goscinnymac-address=\60:01:94:A1:5A:89server=DHCP_IOT_VLANaddaddress=192.168.30.60comment=Touch_Sypialniamac-address=\
    DC:4F:22:86:E8:97server=DHCP_IOT_VLANaddaddress=192.168.30.61comment=Sonoff_POW_Sypialniamac-address=\
    C0:49:EF:F3:05:30server=DHCP_IOT_VLANaddaddress=192.168.30.62comment=Touch_Sien_Goramac-address=\60:01:94:98:AF:B1 server=DHCP_IOT_VLANaddaddress=192.168.30.63comment=Touch_Maly_Pokojmac-address=\84:0D:8E:77:36:E4 server=DHCP_IOT_VLANaddaddress=192.168.30.64comment=Yunschan_Altanamac-address=\5C:CF:7F:C3:E9:16server=DHCP_IOT_VLANaddaddress=192.168.30.106comment=Roleta_Pokoj_Kariny_ACmac-address=\
    C8:C9:A3:9F:88:E2 server=DHCP_IOT_VLANaddaddress=192.168.30.107comment=Roleta_Lazienka_ACmac-address=\80:64:6F:B1:12:50server=DHCP_IOT_VLANaddaddress=192.168.30.108comment=Roleta_Sien_ACmac-address=\
    F4:CF:A2:FF:EE:6Cserver=DHCP_IOT_VLANaddaddress=192.168.30.66comment=Touch_Sien_Dolmac-address=\
    DC:4F:22:82:F2:D3 server=DHCP_IOT_VLANaddaddress=192.168.30.109comment=Roleta_Maly_Pokoj_ACmac-address=\4C:75:25:19:29:67server=DHCP_IOT_VLANaddaddress=192.168.30.111comment=Roleta_Pokoj_Goscinnymac-address=\
    AC:0B:FB:D8:BE:B1 server=DHCP_IOT_VLANaddaddress=192.168.30.69comment="Swiatlo Plac"mac-address=\8C:AA:B5:1B:42:49server=DHCP_IOT_VLANaddaddress=192.168.30.114comment="Roleta_Kom\F3rka_AC"mac-address=\
    AC:0B:FB:D8:C8:93server=DHCP_IOT_VLANaddaddress=192.168.30.112comment=Roleta_Sypialnia_ACmac-address=\4C:75:25:19:60:3Dserver=DHCP_IOT_VLANaddaddress=192.168.30.70comment=mROW-01mac-address=98:CD:AC:25:D2:62\
    server=DHCP_IOT_VLANaddaddress=192.168.30.101comment=Roleta_Gospodarczy_Plac_ACmac-address=\80:64:6F:B1:16:71server=DHCP_IOT_VLANaddaddress=192.168.30.71comment=Gate_NICEmac-address=4C:75:25:1A:0F:8E\
    server=DHCP_IOT_VLANaddaddress=192.168.30.103comment=Roleta_Taras_ACmac-address=\
    AC:0B:FB:D9:23:9Dserver=DHCP_IOT_VLANaddaddress=192.168.30.20comment=Glosnik_Googlemac-address=\20:DF:B9:B2:4F:85server=DHCP_IOT_VLANaddaddress=192.168.30.72comment=Oswietlenie_Przodmac-address=\
    E8:68:E7:4E:15:D0 server=DHCP_IOT_VLANaddaddress=192.168.30.73comment=Choinka_Karinamac-address=\70:03:9F:5D:0A:87server=DHCP_IOT_VLANaddaddress=192.168.30.74comment=Gwiazdamac-address=24:A1:60:0A:12:50\
    server=DHCP_IOT_VLANaddaddress=192.168.30.75comment=Dimmer_Schodymac-address=C4:5B:BE:6E:26:DA \
    server=DHCP_IOT_VLANaddaddress=192.168.40.70comment=Chromecastmac-address=14:AE:85:71:BD:AD \
    server=DHCP_TV_VLANaddaddress=192.168.10.50comment="Fenix 7X"mac-address=90:F1:57:AF:8D:75\
    server=DHCP_LAN_VLANaddaddress=192.168.30.16comment="Falownik Huawei"mac-address=\9C:B2:E8:2C:47:05server=DHCP_IOT_VLANaddaddress=192.168.30.98comment=MEW-02_Ogrzewaniemac-address=\7C:87:CE:F3:7A:87server=DHCP_IOT_VLANaddaddress=192.168.30.200comment="Termostat Pokoj Kariny"mac-address=\
    EC:FA:BC:76:31:23server=DHCP_IOT_VLANaddaddress=192.168.30.201comment="Termostat Salon"mac-address=\
    EC:FA:BC:76:2E:19server=DHCP_IOT_VLANaddaddress=192.168.30.202comment="Termostat Kuchnia"mac-address=\
    EC:FA:BC:76:27:C0 server=DHCP_IOT_VLANaddaddress=192.168.30.203comment="Termostat Komorka"mac-address=\
    EC:FA:BC:76:24:7Fserver=DHCP_IOT_VLANaddaddress=192.168.30.204comment="Termostat Lazienka"mac-address=\
    E0:98:06:1F:4D:51server=DHCP_IOT_VLANaddaddress=192.168.30.206comment="Termostat Maly Pokoj"mac-address=\8C:AA:B5:FD:ED:4Eserver=DHCP_IOT_VLANaddaddress=192.168.30.208comment="Termostat Sien Gora"mac-address=\8C:AA:B5:FD:61:53server=DHCP_IOT_VLANaddaddress=192.168.30.205comment="Termostat Sypialnia"mac-address=\
    EC:FA:BC:76:23:D7 server=DHCP_IOT_VLANaddaddress=192.168.30.207comment="Termostat Pokoj Goscinny"mac-address=\8C:AA:B5:57:8A:44server=DHCP_IOT_VLANaddaddress=192.168.30.210comment="Termostat Sien Dol"mac-address=\
    EC:FA:BC:76:2E:66server=DHCP_IOT_VLANaddaddress=192.168.30.209comment="Termostat Lauba"mac-address=\
    EC:FA:BC:76:30:72server=DHCP_IOT_VLANaddaddress=192.168.30.24comment="HA dev"mac-address=02:07:E1:4C:43:F8 \
    server=DHCP_IOT_VLANaddaddress=192.168.10.181comment="Pv Ubuntu"mac-address=2A:4A:86:F1:F9:86\
    server=DHCP_LAN_VLANaddaddress=192.168.10.182comment="Pv Win11"mac-address=5E:26:27:1B:10:84\
    server=DHCP_LAN_VLANaddaddress=192.168.100.210comment=AP_GORA mac-address=60:22:32:3F:26:E4 \
    server=DHCP_MGMT_VLANaddaddress=192.168.10.40comment="Yamacha glosnik"mac-address=\40:06:A0:84:3B:7Aserver=DHCP_LAN_VLANaddaddress=192.168.30.97comment=LEW_Serwerownia mac-address=\58:BF:25:40:8A:BF server=DHCP_IOT_VLANaddaddress=192.168.30.57comment=Sonoff_POW_Kuchniamac-address=\84:F3:EB:B1:D3:05server=DHCP_IOT_VLANaddaddress=192.168.10.190comment=Terminal_HPmac-address=FC:3F:DB:04:4E:6C\
    server=DHCP_LAN_VLANaddaddress=192.168.30.76comment=OLED mac-address=84:F3:EB:E3:A1:EF server=\
    DHCP_IOT_VLANaddaddress=192.168.30.77comment=Bramka_Versamac-address=AC:0B:FB:E9:5A:1C\
    server=DHCP_IOT_VLANaddaddress=192.168.30.78comment="Swiatlo Piwnica"mac-address=\8C:AA:B5:1B:39:95server=DHCP_IOT_VLANaddaddress=192.168.30.220comment=Piec_Wifimac-address=84:F7:03:E0:54:4C\
    server=DHCP_IOT_VLANaddaddress=192.168.30.211comment=Termostat_Gospodarczymac-address=\
    EC:FA:BC:76:2D:9Bserver=DHCP_IOT_VLANaddaddress=192.168.40.20comment="C+ SYPIALNIA"mac-address=\
    C4:77:AF:54:EA:F7 server=DHCP_TV_VLANaddaddress=192.168.40.30comment="C+ karina"mac-address=C4:77:AF:54:F2:F2 \
    server=DHCP_TV_VLANaddaddress=192.168.40.10comment="C+ KUCHNIA"mac-address=C4:77:AF:54:EC:8D\
    server=DHCP_TV_VLANaddaddress=192.168.30.23comment="Pv Ubuntu-supla-dev"mac-address=\
    BC:24:11:AF:64:5Aserver=DHCP_IOT_VLANaddaddress=192.168.10.32comment=S10_Karina mac-address=72:9C:9C:FB:AB:12\
    server=DHCP_LAN_VLANaddaddress=192.168.30.79comment=Gniazdko_Bojlermac-address=\
    CC:50:E3:26:2C:D2 server=DHCP_IOT_VLANaddaddress=192.168.30.115comment=Rolety_Markiza_ACmac-address=\50:02:91:D2:47:77server=DHCP_IOT_VLANaddaddress=192.168.30.230comment="Bramka Auraton"mac-address=\9C:9E:6E:F0:3F:BC server=DHCP_IOT_VLANaddaddress=192.168.100.60comment="SERVER OSCAM"mac-address=\94:83:C4:07:3A:1Dserver=DHCP_MGMT_VLANaddaddress=192.168.100.140comment=SW_POKOJ_KARINY mac-address=\
    B0:95:75:84:1F:C9 server=DHCP_MGMT_VLANaddaddress=192.168.100.220comment=AP_SIEN mac-address=74:83:C2:90:40:0F\
    server=DHCP_MGMT_VLANaddaddress=192.168.100.40comment="DELL IDRAC"mac-address=18:66:DA:B2:B3:88\
    server=DHCP_MGMT_VLANaddaddress=192.168.100.100comment=SW_RACK_POE mac-address=1C:61:B4:B9:4A:CF \
    server=DHCP_MGMT_VLANaddaddress=192.168.100.130comment=SW_MALY_POKOJ mac-address=\84:D8:1B:57:B8:52server=DHCP_MGMT_VLANaddaddress=192.168.100.120comment=SW_GOSPODARCZY mac-address=\
    B0:BE:76:89:5B:66server=DHCP_MGMT_VLANaddaddress=192.168.100.160comment=SW_WARSZTAT mac-address=84:D8:1B:DA:63:16\
    server=DHCP_MGMT_VLANaddaddress=192.168.100.190comment=SW_KUCHNIA mac-address=70:A7:41:79:85:15\
    server=DHCP_MGMT_VLANaddaddress=192.168.100.90comment=ALARM mac-address=00:1B:9C:0C:15:8A\
    server=DHCP_MGMT_VLANaddaddress=192.168.100.150comment=SW_SYPIALNIA mac-address=\84:D8:1B:57:B8:4Eserver=DHCP_MGMT_VLANaddaddress=192.168.100.85comment=RPI5 mac-address=2C:CF:67:83:89:B7 server=\
    DHCP_MGMT_VLANaddaddress=192.168.100.30comment="UNIFI CONTROLLER"mac-address=\70:A7:41:79:FC:A1 server=DHCP_MGMT_VLANaddaddress=192.168.30.25comment=HA mac-address=02:B7:0C:22:CA:3Fserver=\
    DHCP_IOT_VLANaddaddress=192.168.100.110comment=SW_RACK mac-address=28:87:BA:66:D8:22\
    server=DHCP_MGMT_VLANaddaddress=192.168.100.20comment="OMADA CONTROLLER"mac-address=\36:62:C1:9A:F1:F8 server=DHCP_MGMT_VLANaddaddress=192.168.30.21comment="Licznik wody"mac-address=\
    FC:E8:C0:A0:89:8Cserver=DHCP_IOT_VLANaddaddress=192.168.40.80comment="SONY N720"mac-address=3C:07:71:7D:41:40\
    server=DHCP_TV_VLANaddaddress=192.168.100.240comment=AP_PLAC mac-address=74:83:C2:C9:1E:F7 \
    server=DHCP_MGMT_VLANaddaddress=192.168.100.250comment=AP_PIWNICA mac-address=18:E8:29:96:4A:31\
    server=DHCP_MGMT_VLANaddaddress=192.168.100.200comment=AP_DOL mac-address=70:A7:41:D7:28:A8 \
    server=DHCP_MGMT_VLANaddaddress=192.168.100.230comment=AP_GOSPODARCZY mac-address=\74:83:C2:36:6F:31server=DHCP_MGMT_VLANaddaddress=192.168.100.70comment=ZABBIX mac-address=06:32:B1:B3:9D:F9 \
    server=DHCP_MGMT_VLANaddaddress=192.168.30.22comment="SUPLA_DEVICE WEATHER STATION"mac-address=\
    BC:24:11:60:CE:52server=DHCP_IOT_VLANaddaddress=192.168.100.80comment=UPS_SERVER mac-address=BC:24:11:75:17:12\
    server=DHCP_MGMT_VLANaddaddress=192.168.30.10comment="Serwer SUPLA"mac-address=\
    BC:24:11:2C:39:C0 server=DHCP_IOT_VLANaddaddress=192.168.10.100comment="QNAP OMV"mac-address=6A:0E:3D:04:C8:AC \
    server=DHCP_LAN_VLANaddaddress=192.168.10.200comment=Proxmoxmac-address=18:66:DA:B2:B3:84\
    server=DHCP_LAN_VLANaddaddress=192.168.200.5comment=Mietek_LTEmac-address=C4:AD:34:7C:80:FE \
    server=DHCP_MGMT_LTE_VLAN/ip dhcp-server networkaddaddress=192.168.10.0/24dns-server=192.168.10.1gateway=192.168.10.1\
    ntp-server=192.168.10.1addaddress=192.168.20.0/24dns-server=192.168.20.1gateway=192.168.20.1\
    ntp-server=192.168.20.1addaddress=192.168.30.0/24dns-server=192.168.30.1gateway=192.168.30.1\
    ntp-server=192.168.30.1addaddress=192.168.40.0/24dns-server=192.168.40.1gateway=192.168.40.1\
    ntp-server=192.168.40.1addaddress=192.168.100.0/24dns-server=192.168.100.1gateway=192.168.100.1\
    ntp-server=192.168.100.1addaddress=192.168.200.0/24dns-server=8.8.8.8gateway=192.168.200.1/ip dnssetallow-remote-requests=yesuse-doh-server=https://8.8.4.4/dns-query \verify-doh-cert=yes/ip dnsstaticaddaddress=x.x.x.x disabled=yes name=supla.krissg.ovh type=A/ip firewall address-listaddaddress=192.168.10.0/24list=WAN_Allowaddaddress=192.168.20.0/24list=WAN_Allowaddaddress=5.173.0.0/16list=WAN_Allowaddaddress=77.65.117.126list=WAN_Allowaddaddress=188.123.223.100list=WAN_Allowaddaddress=94.254.0.0/16list=WAN_Allowaddaddress=35.214.214.56list=WAN_Allowaddaddress=35.214.244.97list=WAN_Allowaddaddress=cloud.supla.org list=WAN_Allowaddaddress=91.192.0.86list=WAN_Allowaddaddress=call.supla.io list=WAN_Allowaddaddress=91.192.2.99list=WAN_Allowaddaddress=googleassistant.supla.org list=WAN_Allowaddaddress=192.168.30.0/24list=WAN_Allowaddaddress=89.64.58.84list=WAN_Allowaddaddress=193.186.4.0/24disabled=yes list=WAN_Allowaddaddress=46.112.76.0/24disabled=yes list=WAN_Allowaddaddress=icons.supla.io list=WAN_Allowaddaddress=plex.tv list=WAN_Allowaddaddress=54.170.120.91list=WAN_Allowaddaddress=46.51.207.89list=WAN_Allowaddaddress=142.250.191.46list=WAN_Allowaddaddress=192.168.100.0/24list=WAN_Allowaddaddress=78.28.208.99list=WAN_Allowaddaddress=192.168.216.0/24list=WAN_Allow/ip firewall filteraddaction=accept chain=input comment="Accept established,related,untracked"\
    connection-state=established,related,untrackedaddaction=drop chain=input comment="Drop invalid"connection-state=invalidaddaction=accept chain=input comment="Allow VLAN 10 - DNS"dst-port=53\in-interface=VLAN_10_LAN log=yes log-prefix="Allow DNS vlan 10"protocol=\
    udpaddaction=accept chain=input comment="Allow VLAN 10 - NTP"dst-port=123\in-interface=VLAN_10_LAN log=yes log-prefix="Allow NTP vlan 10"protocol=\
    tcpaddaction=accept chain=input comment="Allow VLAN 20 - DNS"dst-port=53\in-interface=VLAN_20_KAM log=yes log-prefix="Allow DNS vlan 20"protocol=\
    udpaddaction=accept chain=input comment="Allow VLAN 20 - NTP"dst-port=123\in-interface=VLAN_20_KAM log=yes log-prefix="Allow NTP vlan 20"protocol=\
    tcpaddaction=accept chain=input comment="Allow VLAN 30 - DNS"dst-port=53\in-interface=VLAN_30_IOT log=yes log-prefix="Allow DNS vlan 30"protocol=\
    udpaddaction=accept chain=input comment="Allow VLAN 30 - NTP"dst-port=123\in-interface=VLAN_30_IOT log=yes log-prefix="Allow NTP vlan 30"protocol=\
    tcpaddaction=accept chain=input comment="Allow VLAN 40 - DNS"dst-port=53\in-interface=VLAN_40_TV log=yes log-prefix="Allow DNS vlan 40"protocol=\
    udpaddaction=accept chain=input comment="Allow VLAN 40 - NTP"dst-port=123\in-interface=VLAN_40_TV log=yes log-prefix="Allow NTP vlan 40"protocol=\
    tcpaddaction=accept chain=input comment="Allow VLAN 100 - DNS"dst-port=53\in-interface=VLAN_100_MGMT log=yes log-prefix="Allow DNS vlan 100"\
    protocol=udpaddaction=accept chain=input comment="Allow VLAN 100 - NTP"dst-port=123\in-interface=VLAN_100_MGMT log=yes log-prefix="Allow NTP vlan 100"\
    protocol=tcpaddaction=accept chain=input comment="Allow all vlan acces to router"\in-interface-list=LAN log=yes log-prefix="Allow all vlan acces to router"addaction=drop chain=input comment="Blokada ruchu z zt_giolbas to lan"\
    dst-address=192.168.10.0/24in-interface=zt_giolbas src-mac-address=\!34:13:E8:A4:6F:DCaddaction=accept chain=forwardin-interface=zt_klozawaddaction=accept chain=forwardin-interface=zt_giolbasaddaction=accept chain=inputin-interface=zt_klozawaddaction=accept chain=inputin-interface=zt_giolbasaddaction=drop chain=input disabled=yesin-interface=zt_giolbas src-address=\10.147.20.14addaction=add-src-to-address-list address-list=Knock_list\
    address-list-timeout=1mchain=input comment=Knockdst-port=\
    layer7-protocol=knock1 protocol=udpaddaction=add-src-to-address-list address-list=Knock_list2\
    address-list-timeout=1mchain=input dst-port=layer7-protocol=knock2 \
    protocol=udp src-address-list=Knock_listaddaction=add-src-to-address-list address-list=WAN_Allow \
    address-list-timeout=1d5hchain=input dst-port=log=yes log-prefix=\
    port_knock protocol=tcp src-address-list=Knock_list2addaction=drop chain=input comment="Port  Scan"src-address-list=\
    port-scanneraddaction=add-src-to-address-list address-list=port-scanner \
    address-list-timeout=1dchain=inputin-interface-list=WAN protocol=tcp \
    psd=21,3s,3,1addaction=add-src-to-address-list address-list=port-scanner \
    address-list-timeout=1wchain=inputin-interface-list=WAN protocol=udp \
    psd=21,3s,3,1addaction=jump chain=input comment="!!! Check for well-known viruses !!!"\
    jump-target=virusaddaction=accept chain=input comment="Winbox from WAN (WAN Allow)"dst-port=\1818protocol=tcp src-address-list=WAN_Allowaddaction=accept chain=input comment="Accept ICMP"protocol=icmpaddaction=drop chain=input comment="Drop all not coming from LAN"\in-interface-list=!LANaddaction=accept chain=forward comment="Accept in ipsec policy"\
    ipsec-policy=in,ipsecaddaction=accept chain=forward comment="Accept out ipsec policy"\
    ipsec-policy=out,ipsecaddaction=fasttrack-connection chain=forward comment=Fasttrack\
    connection-state=established,related hw-offload=yesaddaction=accept chain=forward comment=\"Accept established,related, untracked"connection-state=\
    established,related,untrackedaddaction=drop chain=forward comment="Drop invalid"connection-state=invalidaddaction=jump chain=forward comment="!!! Check for well-known viruses !!!"\
    jump-target=virusaddaction=drop chain=forward comment="Drop all from WAN not DSTNATed"\
    connection-nat-state=!dstnat connection-state=newin-interface-list=WANaddaction=drop chain=input comment="Drop everything else"log-prefix=DROPaddaction=accept chain=forward comment="Established connections"\
    connection-state=establishedaddaction=accept chain=forward comment="Related connections"\
    connection-state=relatedaddaction=drop chain=forward comment="Drop invalid connections"\
    connection-state=invalid log-prefix=INVALIDaddaction=drop chain=virus comment="Drop Blaster Worm"dst-port=135-139\
    protocol=tcpaddaction=drop chain=virus comment="Drop Messenger Worm"dst-port=135-139\
    protocol=udpaddaction=drop chain=virus comment="Drop Blaster Worm"dst-port=445\
    protocol=tcpaddaction=drop chain=virus comment="Drop Blaster Worm"dst-port=445\
    protocol=udpaddaction=drop chain=virus comment=________ dst-port=593protocol=tcpaddaction=drop chain=virus comment=________ dst-port=1024-1030protocol=tcpaddaction=drop chain=virus comment="Drop MyDoom"dst-port=1080protocol=tcpaddaction=drop chain=virus comment=________ dst-port=1214protocol=tcpaddaction=drop chain=virus comment="ndm requester"dst-port=1363protocol=\
    tcpaddaction=drop chain=virus comment="ndm server"dst-port=1364protocol=tcpaddaction=drop chain=virus comment="screen cast"dst-port=1368protocol=tcpaddaction=drop chain=virus comment=hromgrafx dst-port=1373protocol=tcpaddaction=drop chain=virus comment=cichlid dst-port=1377protocol=tcpaddaction=drop chain=virus comment=Wormdst-port=1433-1434protocol=tcpaddaction=drop chain=virus comment="Bagle Virus"dst-port=2745protocol=tcpaddaction=drop chain=virus comment="Drop Dumaru.Y"dst-port=2283protocol=\
    tcpaddaction=drop chain=virus comment="Drop Beagle"dst-port=2535protocol=tcpaddaction=drop chain=virus comment="Drop Beagle.C-K"dst-port=2745protocol=\
    tcpaddaction=drop chain=virus comment="Drop MyDoom"dst-port=3127-3128\
    protocol=tcpaddaction=drop chain=virus comment="Drop Backdoor OptixPro"dst-port=3410\
    protocol=tcpaddaction=drop chain=virus comment=Wormdst-port=4444protocol=tcpaddaction=drop chain=virus comment=Wormdst-port=4444protocol=udpaddaction=drop chain=virus comment="Drop Sasser"dst-port=5554protocol=tcpaddaction=drop chain=virus comment="Drop Beagle.B"dst-port=8866protocol=\
    tcpaddaction=drop chain=virus comment="Drop Dabber.A-B"dst-port=9898protocol=\
    tcpaddaction=drop chain=virus comment="Drop Dumaru.Y"dst-port=10000protocol=\
    tcpaddaction=drop chain=virus comment="Drop MyDoom.B"dst-port=10080protocol=\
    tcpaddaction=drop chain=virus comment="Drop NetBus"dst-port=12345protocol=tcpaddaction=drop chain=virus comment="Drop Kuang2"dst-port=17300protocol=tcpaddaction=drop chain=virus comment="Drop SubSeven"dst-port=27374protocol=\
    tcpaddaction=drop chain=virus comment="Drop PhatBot, Agobot, Gaobot"dst-port=\65506protocol=tcp/ip firewall nataddaction=masquerade chain=srcnat comment="WAN_SW masquerade"out-interface=\
    ether2-WAN_SWaddaction=masquerade chain=srcnat comment="WAN_LTE masquerade"\out-interface=ether3-WAN_LTEaddaction=masquerade chain=srcnat src-address=192.168.10.0/24addaction=masquerade chain=srcnat src-address=192.168.20.0/24addaction=masquerade chain=srcnat src-address=192.168.30.0/24addaction=masquerade chain=srcnat src-address=192.168.40.0/24addaction=masquerade chain=srcnat src-address=192.168.100.0/24addaction=masquerade chain=srcnat src-address=192.168.200.0/24addaction=dst-nat chain=dstnat comment=Alarmdst-address=x.x.x.x \
    dst-port=1616protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.100.90to-ports=1515addaction=dst-nat chain=dstnat comment=UpSrvdst-address=x.x.x.x \
    dst-port=44044protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.10.4to-ports=44004addaction=dst-nat chain=dstnat comment="Proxmox vnc"disabled=yes \
    dst-address=x.x.x.x dst-port=5900-5999protocol=tcp \
    src-address-list=WAN_Allow to-addresses=192.168.10.180to-ports=5900-5999addaction=src-nat chain=srcnat disabled=yes dst-address=192.168.10.150\
    protocol=tcp src-address=192.168.10.0/24to-addresses=192.168.10.1addaction=dst-nat chain=dstnat comment="Supla app ssl"dst-address=\
    x.x.x.x dst-port=2016protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.30.10to-ports=2016addaction=dst-nat chain=dstnat comment="Supla app nossl"dst-address=\
    x.x.x.x dst-port=2015protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.30.10to-ports=2015addaction=dst-nat chain=dstnat comment="Nginx WEB"disabled=yes dst-address=\
    x.x.x.x dst-port=443protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.10.20to-ports=35443addaction=dst-nat chain=dstnat comment="Nginx WEB https"dst-address=\
    x.x.x.x dst-port=443log-prefix=nginx protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.30.10to-ports=443addaction=dst-nat chain=dstnat comment="Nginx WEB http"dst-address=\
    x.x.x.x dst-port=80log=yes log-prefix=nginx protocol=tcp \
    src-address-list=WAN_Allow to-addresses=192.168.30.10to-ports=82addaction=dst-nat chain=dstnat comment="Nginx proxy"disabled=yes \
    dst-address=x.x.x.x dst-port=8881protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.120to-ports=89addaction=dst-nat chain=dstnat comment="Supla scripts"disabled=yes \
    dst-address=x.x.x.x dst-port=4434protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.120to-ports=4432addaction=dst-nat chain=dstnat comment=Transmissiondst-address=x.x.x.x \
    dst-port=49092protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.10.100to-ports=9091addaction=dst-nat chain=dstnat comment="Transmissin wyjscie"dst-address=\
    x.x.x.x dst-port=51413protocol=tcp to-addresses=192.168.10.100\
    to-ports=51413addaction=dst-nat chain=dstnat disabled=yes dst-address=x.x.x.x \
    dst-port=51414log=yes protocol=udp to-addresses=192.168.10.100to-ports=\51414addaction=dst-nat chain=dstnat comment="OSCAM Svr"disabled=yes dst-address=\
    x.x.x.x dst-port=9999protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.10.50to-ports=8888addaction=dst-nat chain=dstnat comment="OSCAM wyjscie"disabled=yes \
    dst-address=x.x.x.x dst-port=7777protocol=tcp to-addresses=\192.168.10.50to-ports=7777addaction=dst-nat chain=dstnat comment="Oscam svr ssh"disabled=yes \
    dst-address=x.x.x.x dst-port=444protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.50to-ports=22addaction=dst-nat chain=dstnat comment="Oscam svr https"disabled=yes \
    dst-address=x.x.x.x dst-port=8000protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.50to-ports=443addaction=dst-nat chain=dstnat comment="Qnap file browser"dst-address=\
    x.x.x.x dst-port=3678protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.10.100to-ports=3678addaction=dst-nat chain=dstnat comment="Magazyn FTP"dst-address=\
    x.x.x.x dst-port=1106log=yes log-prefix="FTP TEST kristel"\
    protocol=tcp src-address-list=WAN_Allow to-addresses=192.168.10.100\
    to-ports=21addaction=dst-nat chain=dstnat dst-address=x.x.x.x dst-port=55536-55556\
    log=yes log-prefix="FTP TEST kristel"protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.100to-ports=55536-55556addaction=dst-nat chain=dstnat comment="Magazyn SSH"dst-address=\
    x.x.x.x dst-port=7922protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.10.100to-ports=22addaction=dst-nat chain=dstnat comment="Magazyn WWW"disabled=yes \
    dst-address=x.x.x.x dst-port=4439protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.20to-ports=4439addaction=dst-nat chain=dstnat disabled=yes dst-address=x.x.x.x \
    dst-port=8089protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.10.20to-ports=8089addaction=dst-nat chain=dstnat comment=OwnClouddisabled=yes dst-address=\
    x.x.x.x dst-port=25639protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.10.20to-ports=25639addaction=dst-nat chain=dstnat comment="TP-LINK Omada"disabled=yes \
    dst-address=x.x.x.x dst-port=8043protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.20to-ports=8043addaction=dst-nat chain=dstnat comment=NVR dst-address=x.x.x.x \
    dst-port=3733protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.20.2to-ports=37777addaction=dst-nat chain=dstnat comment="FSB web"disabled=yes dst-address=\
    x.x.x.x dst-port=6530protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.10.20to-ports=4530addaction=dst-nat chain=dstnat comment="Malina SSH"dst-address=x.x.x.x \
    dst-port=7923protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.30.10to-ports=22addaction=dst-nat chain=dstnat comment="IDRAC vnc"dst-address=x.x.x.x \
    dst-port=5900protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.100.40to-ports=5900addaction=dst-nat chain=dstnat comment="Malina VNC"disabled=yes \
    dst-address=x.x.x.x dst-port=5900protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.120to-ports=5900addaction=dst-nat chain=dstnat comment="Traccar wyjscie"dst-address=\
    x.x.x.x dst-port=5027protocol=tcp src-address-list=WAN_Allow \
    to-addresses=192.168.30.10to-ports=5027addaction=dst-nat chain=dstnat comment="Malina Unifi"disabled=yes \
    dst-address=x.x.x.x dst-port=8843protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.184to-ports=8843addaction=dst-nat chain=dstnat comment="Winbox LTE"dst-address=x.x.x.x \
    dst-port=1919protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.200.5to-ports=1919addaction=dst-nat chain=dstnat comment="Malina OSCAM"disabled=yes \
    dst-address=x.x.x.x dst-port=8001protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.120to-ports=8888addaction=dst-nat chain=dstnat comment=PLEX dst-address=x.x.x.x \
    dst-port=32400protocol=tcp src-address-list=WAN_Allow to-addresses=\192.168.100.50to-ports=32400addaction=dst-nat chain=dstnat comment="apache WWW"disabled=yes \
    dst-address=x.x.x.x dst-port=80protocol=tcp src-address-list=\
    WAN_Allow to-addresses=192.168.10.120to-ports=80addaction=dst-nat chain=dstnat disabled=yes dst-address=!192.168.88.254\
    dst-port=91protocol=tcp to-addresses=192.168.88.254to-ports=88addaction=dst-nat chain=dstnat comment="Unifi Console"disabled=yes \
    dst-address=x.x.x.x dst-port=3478protocol=udp src-address-list=\
    WAN_Allow to-addresses=192.168.10.115/ip firewall service-portsetftp disabled=yessetsip disabled=yes/ip routeaddcomment="Dual Wan - Check gateway WAN_SW"dst-address=8.8.8.8gateway=\91.195.92.1scope=10addcomment="Dual Wan - Check gateway WAN_LTE"dst-address=8.8.4.4gateway=\10.118.186.49scope=10addcheck-gateway=ping comment="Dual Wan - WAN_SW"distance=1gateway=8.8.8.8\
    target-scope=11addcheck-gateway=ping comment="Dual Wan - WAN_LTE"distance=2gateway=\8.8.4.4target-scope=11addcomment="Dual Wan - Check gateway WAN_SW second"dst-address=\208.67.222.222gateway=91.195.92.1scope=10addcomment="Dual Wan - Check gateway WAN_LTE second"dst-address=\208.67.220.220gateway=10.118.186.49scope=10addcheck-gateway=ping comment="Dual Wan - WAN_SW second"distance=1gateway=\208.67.222.222target-scope=11addcheck-gateway=ping comment="Dual Wan - WAN_LTE second"distance=2\
    gateway=208.67.220.220target-scope=11/ip servicesettelnet disabled=yessetftp disabled=yessetwww disabled=yessetssh disabled=yessetwww-ssl disabled=nosetapi disabled=yessetwinbox address=192.168.0.0/16port=1818setapi-ssl disabled=yes/snmpsetenabled=yes trap-generators=interfaces trap-interfaces=bridge-LAN \
    trap-target=192.168.100.70trap-version=2/system clocksettime-zone-name=Poland/system identitysetname=Mietek/system notesetshow-at-login=no/system ntp clientsetenabled=yes/system ntp serversetbroadcast=yes enabled=yes multicast=yes/system ntp client serversaddaddress=0.pl.pool.ntp.org/tool mac-serversetallowed-interface-list=LAN/tool mac-server mac-winboxsetallowed-interface-list=LAN

---
```
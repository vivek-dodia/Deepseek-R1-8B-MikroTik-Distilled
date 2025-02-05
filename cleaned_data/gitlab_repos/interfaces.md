# Repository Information
Name: interfaces

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
	url = https://gitlab.com/rachuna-net.pl/tools/ansibleroles/mikrotik/interfaces.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "develop"]
	remote = origin
	merge = refs/heads/develop
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: CHANGELOG.md
================================================
# 1.0.0
- Ustawienie Wifi Security Profiles
- Konfiguracja Interface WiFi
- Konfiguracja wirtualnego WiFi Interface
- Konfiguracja portów ethernet
- Konfiguracja Boundingów
- Konfiguracja VLAN
- Konfiguracja Lists interface
- Konfiguracja Bridge
- Ustawienie adresu IP na interface
- Ustawienie dhcp client na interface
================================================

File: main.yml
================================================
input_role_enabled:
  configure_wireless_secuirty:    true
  configure_wireless:             true
  configure_virtual_wireless:     true
  configure_ethernet:             true
  configure_bounding:             true
  configure_vlan:                 true
  configure_interface_list:       true
  configure_bridge:               true
# wireless
input_role_interfaces_wireless_security_profiles:       []
input_role_interfaces_wireless:                         []
input_role_interfaces_virtual_wireless:                 []
# ethernet
input_role_interfaces_ethernet:                         []
input_role_interfaces_bounding:                         []
# vlans
input_role_interfaces_vlan:                             []
# interfaces list
input_role_interfaces_list:                             []
# bridge
input_role_interfaces_bridge:                           []
================================================

File: README.md
================================================
# interfaces
Ansible Role - Mikrotik - Interfaces
### Wymagania
```bash
apt-get install sshpass python3-pip
pip install paramiko
```
### Zmienne
Role Variables
--------------
Defaults role values:
- Enabled:
```yaml
  ### Enabled
  input_role_enabled:
    configure_wireless_secuirty:    true
    configure_wireless:             true
    configure_virtual_wireless:     true
    configure_ethernet:             true
    configure_bounding:             true
    configure_vlan:                 true
    configure_interface_list:       true
    configure_bridge:               true
```
- Configuration List:
```yaml
# wireless
input_role_interfaces_wireless_security_profiles:       []
input_role_interfaces_wireless:                         []
input_role_interfaces_virtual_wireless:                 []
# ethernet
input_role_interfaces_ethernet:                         []
input_role_interfaces_bounding:                         []
# vlans
input_role_interfaces_vlan:                             []
# interfaces list
input_role_interfaces_list:                             []
# bridge
input_role_interfaces_bridge:                           []
```
### Konfiguracja interface Wifi
```yaml
# Konfiguracja profili Wifi
input_role_interfaces_wireless_security_profiles:
  SSID1:
    name: "SSID1"
    comment: "SSID1"
    password: "{{ lookup('hashi_vault', 'secret=secrets/mikrotik:ssid1_wifi_password')}}"
    mode: dynamic-keys
    authentication_types: wpa2-psk
    disable_pmkid: "yes"
    unicast_ciphers: aes-ccm
    group_ciphers: aes-ccm
    group_key_update: 00:05:00
    management_protection: allowed
    # (..) more settings
    state: present
  SSID2:
    name: "SSID2"
    comment: "SSID2"
    password: "{{ lookup('hashi_vault', 'secret=secrets/mikrotik:ssid2_wifi_password')}}"
    mode: dynamic-keys
    authentication_types: wpa2-psk
    disable_pmkid: "yes"
    unicast_ciphers: aes-ccm
    group_ciphers: aes-ccm
    group_key_update: 00:05:00
    management_protection: allowed
    state: present
# Konfiguracja interface
input_role_interfaces_wireless:
  wlan1:
    name: "WiFi-LAN-5GHZ "
    comment: "SSID: SSID1"
    band: 5ghz-a/n/ac
    channel-width: 20/40/80mhz-XXXX
    country: poland
    disabled: "no"
    distance: indoors
    frequency: 5500
    wps_mode: disabled
    installation: indoor
    rate_set: default
    mode: ap-bridge
    security-profile: "{{ inventory_group_routeros_wireless_security_profiles_interfaces.SSID1.name }}"
    ssid: "{{ inventory_group_routeros_wireless_security_profiles_interfaces.SSID1.name }} 5G"
    station_roaming: enabled
    wireless_protocol: 802.11
    mtu: 1500
    loop_protect: "on"
    # Można ustawić adres IP na iterface
    # ipv4:
    # - address: "10.2.0.1/24"
    #   network: "10.2.0.0"
    #   comment: "Storage Network"
    #   state: present
    # Można ustawić aby interface był clientem dhcp
    # dhcp_client:
    #  state: present
# Konfiguracja vierualnego interface
input_role_interfaces_virtual_wireless:
  virtual_wlan1:
    name: "Virtual WiFi 2G"
    comment: "SSID: SSID2"
    hide_ssid: "yes"
    band: 2ghz-b/g/n
    mac_address: "4A:A9:8A:3A:19:DE"
    master_interface: "WiFi-LAN-2GHZ"
    disabled: "no"
    security_profile: "{{ inventory_group_routeros_wireless_security_profiles_interfaces.SSID2.name }}"
    ssid: "{{ inventory_group_routeros_wireless_security_profiles_interfaces.SSID2.name }} 2G"
    wps_mode: disabled
    state: present
    ipv4:
    - address: "10.1.1.1/24"
      network: "10.1.1.0"
      comment: "LoT Network"
      state: present
```
### Konfiguracja interface ethernet
```yaml
# konfiguracja ethernet
input_role_interfaces_ethernet:
  ether1:
    name: "WAN-01"
    comment: "WAN-01"
    dhcp_client:
      state: present
  ether2:
    name: LAN-01
    comment: "LAN-01 - ProxMox"
    # Można ustawić adres IP na iterface
    # ipv4:
    # - address: "10.2.0.1/24"
    #   network: "10.2.0.0"
    #   comment: "ProxMox Network"
    #   state: present
    # Można ustawić aby interface był clientem dhcp
    # dhcp_client:
    #  state: present
  ether3:
    name: LAN-02
    comment: "LAN-02 - ProxMox"
  ether4:
    name: LAN-03
    comment: "LAN-03 - ProxMox"
  ether5:
    name: LAN-04
    comment: "LAN-04 - Disabled"
    disabled: "yes"
# Konfiguracja boundingu
input_role_interfaces_bounding:
  BOND_STORAGE:
    name: "BOND-STORAGE"
    comment: "Bounding storage NAS"
    mode: 802.3ad
    slaves: "LAN-08,LAN-09"
    disabled: "no"
    state: present
    ipv4:
    - address: "10.2.0.1/24"
      network: "10.2.0.0"
      comment: "Storage Network"
      state: present
```
### Konfiguracja vlan
```yaml
input_role_interfaces_vlan:
  VLAN_01_PROD_DMZ:
    name: "VLAN-01-PROD-DMZ"
    comment: "PROD-DMZ"
    vlan_id: 20
    interface: LAN-01
    state: present
```
### Konfiguracja list interface
```yaml
inventory_group_routeros_list_interfaces:
  LIST_WAN:
    name: "LIST-WAN"
    comment: "WAN"
    include: []
    exclude: []
    state: present
    members:
    - interface: "{{ inventory_group_routeros_ethernet_interfaces.ether1.name }}"
      comment: ""
      state: present
  LIST_LAN_USERS:
    name: "LIST-LAN-USERS"
    comment: "LAN-USERS"
    include: []
    exclude: []
    state: present
    members:
    - interface: "{{ inventory_group_routeros_wireless_interfaces.wlan1.name }}"
      comment: ""
      state: present
    - interface: "{{ inventory_group_routeros_wireless_interfaces.wlan2.name }}"
      comment: ""
      state: present
  LIST_LAN:
    name: "LIST-LAN"
    comment: "LAN"
    include: ["LIST-LAN-USERS"]
    exclude: []
    state: present
```
### Konfiguracja bridge
```yaml
input_role_interfaces_bridge:
  BRIDGE_USERS:
    name: "BRIDGE-USERS"
    comment: "BRIDGE - Users"
    admin_mac: 48:A9:8A:97:4C:C9
    auto_mac: "no"
    state: present
    port:
    - interface: "{{ inventory_group_routeros_wireless_interfaces.wlan1.name }}"
      comment: "{{ inventory_group_routeros_wireless_interfaces.wlan1.comment }}"
      state: present
    - interface: "{{ inventory_group_routeros_wireless_interfaces.wlan2.name }}"
      comment: "{{ inventory_group_routeros_wireless_interfaces.wlan2.comment }}"
      state: present
    ipv4:
      state: present
    - address: "192.168.88.1/24"
      network: "192.168.88.0"
      comment: "Users Network"
      state: present
```
### CHANGELOG
[CHANGELOG](CHANGELOG.md)
## License
BSD 3-Clause
Author Information
------------------
### Maciej Rachuna
SysOps/DevOps
================================================

File: configure_dhcp_client.yml
================================================
- name: "[MikroTik] [DHCP Client] Set/Update dhcp client on interface {{ interface_parameters.name }}"
  register: setDhcpClientOnInteface
  routeros_command:
    commands:
    - :if ([/ip dhcp-client find interface={{ interface_parameters.name }}])
      do={
        /ip dhcp-client set {{ interface_parameters.name }}
        comment="{{ interface_parameters.comment |default('') }}"
        {% if interface_parameters.dhcp_client.add_default_route is defined %} add-default-route={{ interface_parameters.dhcp_client.add_default_route }}{% endif %}
        {% if interface_parameters.dhcp_client.default_route_distance is defined %} default-route-distance={{ interface_parameters.default_route_distance.add_default_route }}{% endif %}
        {% if interface_parameters.dhcp_client.dhcp_options is defined %} dhcp-options={{ interface_parameters.dhcp_options.add_default_route }}{% endif %}
        {% if interface_parameters.dhcp_client.use_peer_dns is defined %} use-peer-dns={{ interface_parameters.dhcp_options.use_peer_dns }}{% endif %}
        {% if interface_parameters.dhcp_client.use_peer_ntp is defined %} use-peer-ntp={{ interface_parameters.dhcp_options.use_peer_ntp }}{% endif %}
        disabled="{{ interface_parameters.dhcp_options.disabled | default('no') }}"
      }
      else={
        /ip dhcp-client add interface={{ interface_parameters.name }} comment="{{ interface_parameters.comment |default('') }}"
        {% if interface_parameters.dhcp_client.add_default_route is defined %} add-default-route={{ interface_parameters.dhcp_client.add_default_route }}{% endif %}
        {% if interface_parameters.dhcp_client.default_route_distance is defined %} default-route-distance={{ interface_parameters.default_route_distance.add_default_route }}{% endif %}
        {% if interface_parameters.dhcp_client.dhcp_options is defined %} dhcp-options={{ interface_parameters.dhcp_options.add_default_route }}{% endif %}
        {% if interface_parameters.dhcp_client.use_peer_dns is defined %} use-peer-dns={{ interface_parameters.dhcp_options.use_peer_dns }}{% endif %}
        {% if interface_parameters.dhcp_client.use_peer_ntp is defined %} use-peer-ntp={{ interface_parameters.dhcp_options.use_peer_ntp }}{% endif %}
        disabled="{{ interface_parameters.dhcp_options.disabled | default('no') }}"
      }
  when:
    - interface_parameters.dhcp_client.state == "present"
- name: "[MikroTik] [DHCP Client] Remove dhcp client on interface {{ interface_parameters.name }}"
  register: remDhcpClientOnInteface
  routeros_command:
    commands:
    - :if ([/ip dhcp-client find interface={{ interface_parameters.name }}])
      do={
        /ip dhcp-client remove {{ interface_parameters.name }}
      }
  when:
    - interface_parameters.dhcp_client.state == "absent"
================================================

File: configure_interface_bounding.yml
================================================
- name: "[MikroTik] [Ethernet] Create/Update Bounding interface {{ interface_parameters.name }}"
  routeros_command:
    commands:
    - :if ([/interface/bonding find name={{ interface_parameters.name }} ])
      do={
        /interface/bonding set [ find name={{ interface_parameters.name }} ] comment=\"{{ interface_parameters.comment | default('') }}\"
        {% if interface_parameters.arp is defined %} arp={{ interface_parameters.arp }}{% endif %}
        {% if interface_parameters.disabled is defined %} disabled={{ interface_parameters.disabled }}{% endif %}
        {% if interface_parameters.mtu is defined %} mtu={{ interface_parameters.mtu }}{% endif%}
        {% if interface_parameters.arp_timeout is defined %} arp-timeout={{ interface_parameters.arp_timeout }}{% endif %}
        {% if interface_parameters.arp_ip_targets is defined %} arp_ip_targets={{ interface_parameters.arp_ip_targets }}{% endif %}
        {% if interface_parameters.arp_interval is defined %} arp-interval={{ interface_parameters.arp_interval }}{% endif %}
        {% if interface_parameters.forced_mac_address is defined %} forced-mac-address={{ interface_parameters.forced_mac_address }}{% endif %}
        {% if interface_parameters.lacp_user_key is defined %} lacp-user-key={{ interface_parameters.lacp_user_key }}{% endif %}
        {% if interface_parameters.mii_interval is defined %} mii-interval={{ interface_parameters.mii_interval }}{% endif %}
        {% if interface_parameters.mlag_id is defined %} mlag_id={{ interface_parameters.mlag_id }}{% endif %}
        {% if interface_parameters.primary is defined %} primary={{ interface_parameters.primary }}{% endif %}
        {% if interface_parameters.transmit_hash_policy is defined %} transmit-hash-policy={{ interface_parameters.transmit_hash_policy }}{% endif %}
        {% if interface_parameters.down_delay is defined %} down-delay={{ interface_parameters.down_delay }}{% endif %}
        {% if interface_parameters.lacp_rate is defined %} lacp-rate={{ interface_parameters.lacp_rate }}{% endif %}
        {% if interface_parameters.link_monitoring is defined %} link-monitoring={{ interface_parameters.link_monitoring }}{% endif %}
        {% if interface_parameters.min_links is defined %} min-links={{ interface_parameters.min_links }}{% endif %}
        {% if interface_parameters.mode is defined %} mode={{ interface_parameters.mode }}{% endif %}
        {% if interface_parameters.slaves is defined %} slaves={{ interface_parameters.slaves }}{% endif %}
        {% if interface_parameters.up_delay is defined %} up-delay={{ interface_parameters.up_delay }}{% endif%}
      }
      else={
        /interface/bonding add comment=\"{{ interface_parameters.comment | default('') }}\"
        name={{ interface_parameters.name }}
        {% if interface_parameters.arp is defined %} arp={{ interface_parameters.arp }}{% endif %}
        {% if interface_parameters.disabled is defined %} disabled={{ interface_parameters.disabled }}{% endif %}
        {% if interface_parameters.mtu is defined %} mtu={{ interface_parameters.mtu }}{% endif%}
        {% if interface_parameters.arp_timeout is defined %} arp-timeout={{ interface_parameters.arp_timeout }}{% endif %}
        {% if interface_parameters.arp_ip_targets is defined %} arp_ip_targets={{ interface_parameters.arp_ip_targets }}{% endif %}
        {% if interface_parameters.arp_interval is defined %} arp-interval={{ interface_parameters.arp_interval }}{% endif %}
        {% if interface_parameters.forced_mac_address is defined %} forced-mac-address={{ interface_parameters.forced_mac_address }}{% endif %}
        {% if interface_parameters.lacp_user_key is defined %} lacp-user-key={{ interface_parameters.lacp_user_key }}{% endif %}
        {% if interface_parameters.mii_interval is defined %} mii-interval={{ interface_parameters.mii_interval }}{% endif %}
        {% if interface_parameters.mlag_id is defined %} mlag_id={{ interface_parameters.mlag_id }}{% endif %}
        {% if interface_parameters.primary is defined %} primary={{ interface_parameters.primary }}{% endif %}
        {% if interface_parameters.transmit_hash_policy is defined %} transmit-hash-policy={{ interface_parameters.transmit_hash_policy }}{% endif %}
        {% if interface_parameters.down_delay is defined %} down-delay={{ interface_parameters.down_delay }}{% endif %}
        {% if interface_parameters.lacp_rate is defined %} lacp-rate={{ interface_parameters.lacp_rate }}{% endif %}
        {% if interface_parameters.link_monitoring is defined %} link-monitoring={{ interface_parameters.link_monitoring }}{% endif %}
        {% if interface_parameters.min_links is defined %} min-links={{ interface_parameters.min_links }}{% endif %}
        {% if interface_parameters.mode is defined %} mode={{ interface_parameters.mode }}{% endif %}
        {% if interface_parameters.slaves is defined %} slaves={{ interface_parameters.slaves }}{% endif %}
        {% if interface_parameters.up_delay is defined %} up-delay={{ interface_parameters.up_delay }}{% endif%}
      }
  register: update_interface_ethernet_status
  when: interface_parameters.state == "present"
- name: "[MikroTik] [Ethernet] Remove Bounding interface {{ interface_parameters.name }}"
  register: remove_interface_bridge_status
  routeros_command:
    commands:
    - /interface/bonding remove ([/interface/bonding find name={{ interface_parameters.name }}])
  when: interface_parameters.state == "absent"
- include: configure_dhcp_client.yml
  when:
  - interface_parameters.dhcp_client is defined
  - interface_parameters.dhcp_client.state is defined
  - interface_parameters.dhcp_client.state == "present"
- include: configure_ip_address.yml
  no_log: true
  loop: "{{ interface_parameters.ipv4 }}"
  loop_control:
    loop_var: ipv4
  when:
  - interface_parameters.ipv4 is defined
  - ipv4.state is defined
================================================

File: configure_interface_bridge.yml
================================================
- name: "[MikroTik] [Bridge] Create/Update Bridge interface {{ interface_parameters.name }}"
  routeros_command:
    commands:
    - :if ([/interface bridge find name={{ interface_parameters.name }} ])
      do={
        /interface bridge set [ find name={{ interface_parameters.name }} ] comment="{{ interface_parameters.comment | default('') }}"
        {% if interface_parameters.arp is defined %} arp={{ interface_parameters.arp }}{% endif %}
        {% if interface_parameters.disabled is defined %} disabled={{ interface_parameters.disabled }}{% endif %}
        {% if interface_parameters.mtu is defined %} mtu={{ interface_parameters.mtu }}{% endif%}
        {% if interface_parameters.dhcp_snooping is defined %} dhcp-snooping={{ interface_parameters.dhcp_snooping }}{% endif %}
        {% if interface_parameters.arp_timeout is defined %} arp-timeout={{ interface_parameters.arp_timeout }}{% endif %}
        {% if interface_parameters.frame_types is defined %} frame-types={{ interface_parameters.frame_types }}{% endif %}
        {% if interface_parameters.last_member_query_count is defined %} last-member-query-count={{ interface_parameters.fec_last_member_query_count }}{% endif %}
        {% if interface_parameters.loop_protect is defined %} loop-protect={{ interface_parameters.loop_protect }}{% endif %}
        {% if interface_parameters.priority is defined %} priority={{ interface_parameters.priority }}{% endif %}
        {% if interface_parameters.query_response_interval is defined %} query-response-interval={{ interface_parameters.query_response_interval }}{% endif %}
        {% if interface_parameters.transmit_hold_count is defined %} transmit-hold-count={{ interface_parameters.transmit_hold_count }}{% endif %}
        {% if interface_parameters.igmp_snooping is defined %} igmp-snooping={{ interface_parameters.igmp_snooping }}{% endif %}
        {% if interface_parameters.max_hops is defined %} max-hops={{ interface_parameters.max_hops }}{% endif %}
        {% if interface_parameters.multicast_querier is defined %} multicast-querier={{ interface_parameters.multicast_querier }}{% endif %}
        {% if interface_parameters.protocol_mode is defined %} protocol-mode={{ interface_parameters.protocol_mode }}{% endif %}
        {% if interface_parameters.region_name is defined %} region-namee={{ interface_parameters.region_name }}{% endif %}
        {% if interface_parameters.ether_type is defined %} ether-type={{ interface_parameters.ether_type }}{% endif %}
        {% if interface_parameters.igmp_version is defined %} igmp-version={{ interface_parameters.igmp_version }}{% endif %}
        {% if interface_parameters.max_message_age is defined %} max-message-age={{ interface_parameters.max_message_age }}{% endif%}
        {% if interface_parameters.multicast_router is defined %} multicast-router={{ interface_parameters.multicast_router }}{% endif%}
        {% if interface_parameters.pvid is defined %} pvid={{ interface_parameters.pvid }}{% endif%}
        {% if interface_parameters.region_revision is defined %} region-revision={{ interface_parameters.region_revision }}{% endif%}
        {% if interface_parameters.add_dhcp_option82 is defined %} add-dhcp-option82={{ interface_parameters.add_dhcp_option82 }}{% endif%}
        {% if interface_parameters.auto_mac is defined %} auto-mac={{ interface_parameters.auto_mac }}{% endif%}
        {% if interface_parameters.fast_forward is defined %} fast-forward={{ interface_parameters.fast_forward }}{% endif%}
        {% if interface_parameters.ingress_filtering is defined %} ingress-filtering={{ interface_parameters.ingress_filtering }}{% endif%}
        {% if interface_parameters.membership_interval is defined %} membership-interval={{ interface_parameters.membership_interval }}{% endif%}
        {% if interface_parameters.querier_interval is defined %} querier-interval={{ interface_parameters.querier_interval }}{% endif%}
        {% if interface_parameters.startup_query_count is defined %} startup-query-count={{ interface_parameters.startup_query_count }}{% endif%}
        {% if interface_parameters.admin_mac is defined %} admin-mac={{ interface_parameters.admin_mac }}{% endif%}
        {% if interface_parameters.forward_delay is defined %} forward-delay={{ interface_parameters.forward_delay }}{% endif%}
        {% if interface_parameters.last_member_interval is defined %} last-member-interval={{ interface_parameters.last_member_interval }}{% endif%}
        {% if interface_parameters.mld_version is defined %} mld-version={{ interface_parameters.mld_version }}{% endif%}
        {% if interface_parameters.query_interval is defined %} query-interval={{ interface_parameters.query_interval }}{% endif%}
        {% if interface_parameters.startup_query_interval is defined %} startup-query-interval={{ interface_parameters.startup_query_interval }}{% endif%}
      }
      else={
        /interface bridge add comment="{{ interface_parameters.comment | default('') }}"
        name={{ interface_parameters.name }}
        {% if interface_parameters.arp is defined %} arp={{ interface_parameters.arp }}{% endif %}
        {% if interface_parameters.disabled is defined %} disabled={{ interface_parameters.disabled }}{% endif %}
        {% if interface_parameters.mtu is defined %} mtu={{ interface_parameters.mtu }}{% endif%}
        {% if interface_parameters.dhcp_snooping is defined %} dhcp-snooping={{ interface_parameters.dhcp_snooping }}{% endif %}
        {% if interface_parameters.arp_timeout is defined %} arp-timeout={{ interface_parameters.arp_timeout }}{% endif %}
        {% if interface_parameters.frame_types is defined %} frame-types={{ interface_parameters.frame_types }}{% endif %}
        {% if interface_parameters.last_member_query_count is defined %} last-member-query-count={{ interface_parameters.fec_last_member_query_count }}{% endif %}
        {% if interface_parameters.loop_protect is defined %} loop-protect={{ interface_parameters.loop_protect }}{% endif %}
        {% if interface_parameters.priority is defined %} priority={{ interface_parameters.priority }}{% endif %}
        {% if interface_parameters.query_response_interval is defined %} query-response-interval={{ interface_parameters.query_response_interval }}{% endif %}
        {% if interface_parameters.transmit_hold_count is defined %} transmit-hold-count={{ interface_parameters.transmit_hold_count }}{% endif %}
        {% if interface_parameters.igmp_snooping is defined %} igmp-snooping={{ interface_parameters.igmp_snooping }}{% endif %}
        {% if interface_parameters.max_hops is defined %} max-hops={{ interface_parameters.max_hops }}{% endif %}
        {% if interface_parameters.multicast_querier is defined %} multicast-querier={{ interface_parameters.multicast_querier }}{% endif %}
        {% if interface_parameters.protocol_mode is defined %} protocol-mode={{ interface_parameters.protocol_mode }}{% endif %}
        {% if interface_parameters.region_name is defined %} region-namee={{ interface_parameters.region_name }}{% endif %}
        {% if interface_parameters.ether_type is defined %} ether-type={{ interface_parameters.ether_type }}{% endif %}
        {% if interface_parameters.igmp_version is defined %} igmp-version={{ interface_parameters.igmp_version }}{% endif %}
        {% if interface_parameters.max_message_age is defined %} max-message-age={{ interface_parameters.max_message_age }}{% endif%}
        {% if interface_parameters.multicast_router is defined %} multicast-router={{ interface_parameters.multicast_router }}{% endif%}
        {% if interface_parameters.pvid is defined %} pvid={{ interface_parameters.pvid }}{% endif%}
        {% if interface_parameters.region_revision is defined %} region-revision={{ interface_parameters.region_revision }}{% endif%}
        {% if interface_parameters.add_dhcp_option82 is defined %} add-dhcp-option82={{ interface_parameters.add_dhcp_option82 }}{% endif%}
        {% if interface_parameters.auto_mac is defined %} auto-mac={{ interface_parameters.auto_mac }}{% endif%}
        {% if interface_parameters.fast_forward is defined %} fast-forward={{ interface_parameters.fast_forward }}{% endif%}
        {% if interface_parameters.ingress_filtering is defined %} ingress-filtering={{ interface_parameters.ingress_filtering }}{% endif%}
        {% if interface_parameters.membership_interval is defined %} membership-interval={{ interface_parameters.membership_interval }}{% endif%}
        {% if interface_parameters.querier_interval is defined %} querier-interval={{ interface_parameters.querier_interval }}{% endif%}
        {% if interface_parameters.startup_query_count is defined %} startup-query-count={{ interface_parameters.startup_query_count }}{% endif%}
        {% if interface_parameters.admin_mac is defined %} admin-mac={{ interface_parameters.admin_mac }}{% endif%}
        {% if interface_parameters.forward_delay is defined %} forward-delay={{ interface_parameters.forward_delay }}{% endif%}
        {% if interface_parameters.last_member_interval is defined %} last-member-interval={{ interface_parameters.last_member_interval }}{% endif%}
        {% if interface_parameters.mld_version is defined %} mld-version={{ interface_parameters.mld_version }}{% endif%}
        {% if interface_parameters.query_interval is defined %} query-interval={{ interface_parameters.query_interval }}{% endif%}
        {% if interface_parameters.startup_query_interval is defined %} startup-query-interval={{ interface_parameters.startup_query_interval }}{% endif%}
      }
  register: update_interface_ethernet_status
  when: interface_parameters.state == "present"
- name: "[MikroTik] [Bridge] Remove bridge interface {{ interface_parameters.name }}"
  register: remove_interface_bridge_status
  routeros_command:
    commands:
    - /interface bridge remove ([/interface bridge find name={{ interface_parameters.name }}])
  when: interface_parameters.state == "absent"
- include: configure_interface_bridge_port.yml
  no_log: true
  loop: "{{ interface_parameters.port }}"
  loop_control:
    loop_var: "interface_parameters_port"
  when:
  - interface_parameters.port is defined
  - interface_parameters.state == "present"
- include: configure_dhcp_client.yml
  when:
  - interface_parameters.dhcp_client is defined
  - interface_parameters.dhcp_client.state is defined
  - interface_parameters.dhcp_client.state == "present"
- include: configure_ip_address.yml
  no_log: true
  loop: "{{ interface_parameters.ipv4 }}"
  loop_control:
    loop_var: ipv4
  when:
  - interface_parameters.ipv4 is defined
  - ipv4.state is defined
================================================

File: configure_interface_bridge_port.yml
================================================
- name: "[MikroTik] [Bridge] Create/Update Bridge Port interface {{ interface_parameters_port.interface }}"
  routeros_command:
    commands:
    - :if ([/interface bridge port find interface={{ interface_parameters_port.interface }} ])
      do={
        /interface bridge port set [ find interface={{ interface_parameters_port.interface }} ] comment="{{ interface_parameters_port.comment | default('') }}"
        {% if interface_parameters_port.auto_isolate is defined %} auto-isolate={{ interface_parameters_port.auto_isolate }}{% endif %}
        {% if interface_parameters_port.disabled is defined %} disabled={{ interface_parameters_port.disabled }}{% endif %}
        {% if interface_parameters_port.edge is defined %} edge={{ interface_parameters_port.edge }}{% endif%}
        {% if interface_parameters_port.internal_path_cost is defined %} internal-path-cost={{ interface_parameters_port.internal_path_cost }}{% endif %}
        {% if interface_parameters_port.pvid is defined %} pvid={{ interface_parameters_port.pvid }}{% endif %}
        {% if interface_parameters_port.bpdu_guard is defined %} bpdu-guard={{ interface_parameters_port.bpdu_guard }}{% endif %}
        {% if interface_parameters_port.fast_leave is defined %} fast-leave={{ interface_parameters_port.fast_leave }}{% endif %}
        {% if interface_parameters_port.learn is defined %} learn={{ interface_parameters_port.learn }}{% endif %}
        {% if interface_parameters_port.restricted_role is defined %} restricted-role={{ interface_parameters_port.restricted_role }}{% endif %}
        {% if interface_parameters_port.frame_types is defined %} frame-types={{ interface_parameters_port.frame_types }}{% endif %}
        {% if interface_parameters_port.multicast_router is defined %} multicast-router={{ interface_parameters_port.multicast_router }}{% endif %}
        {% if interface_parameters_port.restricted_tcn is defined %} restricted-tcn={{ interface_parameters_port.restricted_tcn }}{% endif %}
        {% if interface_parameters_port.broadcast_flood is defined %} broadcast-flood={{ interface_parameters_port.broadcast_flood }}{% endif %}
        {% if interface_parameters_port.horizon is defined %} horizon={{ interface_parameters_port.horizon }}{% endif %}
        {% if interface_parameters_port.path_cost is defined %} path-cost={{ interface_parameters_port.path_cost }}{% endif %}
        {% if interface_parameters_port.tag_stacking is defined %} tag-stacking={{ interface_parameters_port.tag_stacking }}{% endif %}
        {% if interface_parameters_port.hw is defined %} hw={{ interface_parameters_port.hw }}{% endif %}
        {% if interface_parameters_port.place_before is defined %} place-before={{ interface_parameters_port.place_before }}{% endif %}
        {% if interface_parameters_port.trusted is defined %} trusted={{ interface_parameters_port.trusted }}{% endif%}
        {% if interface_parameters_port.ingress_filtering is defined %} ingress-filtering={{ interface_parameters_port.ingress_filtering }}{% endif%}
        {% if interface_parameters_port.point_to_point is defined %} point-to-point={{ interface_parameters_port.point_to_point }}{% endif%}
        {% if interface_parameters_port.unknown_multicast_flood is defined %} unknown-multicast-flood={{ interface_parameters_port.unknown_multicast_flood }}{% endif%}
        {% if interface_parameters_port.priority is defined %} priority={{ interface_parameters_port.priority }}{% endif%}
        {% if interface_parameters_port.unknown_unicast_flood is defined %} unknown-unicast-flood={{ interface_parameters_port.unknown_unicast_flood }}{% endif%}
        {% if interface_parameters_port.bridge is defined %} bridge={{ interface_parameters.name }}{% endif%}
      }
      else={
        /interface bridge port add comment="{{ interface_parameters_port.comment | default('') }}" interface={{ interface_parameters_port.interface }}
        {% if interface_parameters_port.auto_isolate is defined %} auto-isolate={{ interface_parameters_port.auto_isolate }}{% endif %}
        {% if interface_parameters_port.disabled is defined %} disabled={{ interface_parameters_port.disabled }}{% endif %}
        {% if interface_parameters_port.edge is defined %} edge={{ interface_parameters_port.edge }}{% endif%}
        {% if interface_parameters_port.internal_path_cost is defined %} internal-path-cost={{ interface_parameters_port.internal_path_cost }}{% endif %}
        {% if interface_parameters_port.pvid is defined %} pvid={{ interface_parameters_port.pvid }}{% endif %}
        {% if interface_parameters_port.bpdu_guard is defined %} bpdu-guard={{ interface_parameters_port.bpdu_guard }}{% endif %}
        {% if interface_parameters_port.fast_leave is defined %} fast-leave={{ interface_parameters_port.fast_leave }}{% endif %}
        {% if interface_parameters_port.learn is defined %} learn={{ interface_parameters_port.learn }}{% endif %}
        {% if interface_parameters_port.restricted_role is defined %} restricted-role={{ interface_parameters_port.restricted_role }}{% endif %}
        {% if interface_parameters_port.frame_types is defined %} frame-types={{ interface_parameters_port.frame_types }}{% endif %}
        {% if interface_parameters_port.multicast_router is defined %} multicast-router={{ interface_parameters_port.multicast_router }}{% endif %}
        {% if interface_parameters_port.restricted_tcn is defined %} restricted-tcn={{ interface_parameters_port.restricted_tcn }}{% endif %}
        {% if interface_parameters_port.broadcast_flood is defined %} broadcast-flood={{ interface_parameters_port.broadcast_flood }}{% endif %}
        {% if interface_parameters_port.horizon is defined %} horizon={{ interface_parameters_port.horizon }}{% endif %}
        {% if interface_parameters_port.path_cost is defined %} path-cost={{ interface_parameters_port.path_cost }}{% endif %}
        {% if interface_parameters_port.tag_stacking is defined %} tag-stacking={{ interface_parameters_port.tag_stacking }}{% endif %}
        {% if interface_parameters_port.hw is defined %} hw={{ interface_parameters_port.hw }}{% endif %}
        {% if interface_parameters_port.place_before is defined %} place-before={{ interface_parameters_port.place_before }}{% endif %}
        {% if interface_parameters_port.trusted is defined %} trusted={{ interface_parameters_port.trusted }}{% endif%}
        {% if interface_parameters_port.ingress_filtering is defined %} ingress-filtering={{ interface_parameters_port.ingress_filtering }}{% endif%}
        {% if interface_parameters_port.point_to_point is defined %} point-to-point={{ interface_parameters_port.point_to_point }}{% endif%}
        {% if interface_parameters_port.unknown_multicast_flood is defined %} unknown-multicast-flood={{ interface_parameters_port.unknown_multicast_flood }}{% endif%}
        {% if interface_parameters_port.priority is defined %} priority={{ interface_parameters_port.priority }}{% endif%}
        {% if interface_parameters_port.unknown_unicast_flood is defined %} unknown-unicast-flood={{ interface_parameters_port.unknown_unicast_flood }}{% endif%}
        bridge={{ interface_parameters.name }}
      }
  register: update_interface_ethernet_status
  when: interface_parameters_port.state == "present"
- name: "[MikroTik] [Bridge] Remove bridge interface {{ interface_parameters_port.interface }}"
  register: remove_interface_bridge_status
  routeros_command:
    commands:
    - /interface bridge port remove ([/interface bridge find interface={{ interface_parameters_port.interface }}])
  when: interface_parameters_port.state == "absent"
================================================

File: configure_interface_ethernet.yml
================================================
- name: "[MikroTik] [Ethernet] Update Ethernet interface {{ interface_parameters.name }}"
  routeros_command:
    commands:
    - /interface ethernet set [ find default-name={{ interface_default_name }} ]
      name={{ interface_parameters.name }}
      comment="{{ interface_parameters.comment | default('') }}"
      {% if interface_parameters.arp is defined %} arp={{ interface_parameters.arp }}{% endif %}
      {% if interface_parameters.bandwidth is defined %} bandwidth={{ interface_parameters.bandwidth }}{% endif %}
      {% if interface_parameters.disabled is defined %} disabled={{ interface_parameters.disabled }}{% endif %}
      {% if interface_parameters.l2mtu is defined %} l2mtu={{ interface_parameters.l2mtu }}{% endif %}
      {% if interface_parameters.loop_protect_send_interval is defined %} loop-protect-send-interval={{ interface_parameters.loop_protect_send_interval }}{% endif %}
      {% if interface_parameters.mtu is defined %} mtu={{ interface_parameters.mtu }}{% endif %}
      {% if interface_parameters.rig_mac_address is defined %} rig-mac-address={{ interface_parameters.rig_mac_address }}{% endif %}
      {% if interface_parameters.sfp_shutdown_temperature is defined %} sfp-shutdown-temperature={{ interface_parameters.sfp_shutdown_temperature }}{% endif %}
      {% if interface_parameters.arp_timeout is defined %} arp-timeout={{ interface_parameters.arp_timeout }}{% endif %}
      {% if interface_parameters.combo_mode is defined %} combo-mode={{ interface_parameters.combo_mode }}{% endif %}
      {% if interface_parameters.fec_mode is defined %} fec-mode={{ interface_parameters.fec-mode }}{% endif %}
      {% if interface_parameters.loop_protect is defined %} loop-protect={{ interface_parameters.loop_protect }}{% endif %}
      {% if interface_parameters.mac_address is defined %} mac-address={{ interface_parameters.mac_address }}{% endif %}
      {% if interface_parameters.rx_flow_control is defined %} rx-flow-control={{ interface_parameters.rx_flow_control }}{% endif %}
      {% if interface_parameters.speed is defined %} speed={{ interface_parameters.speed }}{% endif %}
      {% if interface_parameters.advertise is defined %} advertise={{ interface_parameters.advertise }}{% endif %}
      {% if interface_parameters.auto_negotiation is defined %} auto-negotiation={{ interface_parameters.auto_negotiation }}{% endif %}
      {% if interface_parameters.full_duplex is defined %} full-duplex={{ interface_parameters.full_duplex }}{% endif %}
      {% if interface_parameters.loop_protect_disable_time is defined %} loop-protect-disable-time={{ interface_parameters.loop_protect_disable_time }}{% endif %}
      {% if interface_parameters.mdix_enable is defined %} mdix-enable={{ interface_parameters.mdix_enable }}{% endif %}
      {% if interface_parameters.sfp_rate_select is defined %} sfp-rate-select={{ interface_parameters.sfp_rate_select }}{% endif %}
      {% if interface_parameters.tx_flow_control is defined %} tx-flow-control={{ interface_parameters.tx_flow_control }}{% endif %}
  register: update_interface_ethernet_status
- include: configure_dhcp_client.yml
  when:
  - interface_parameters.dhcp_client is defined
  - interface_parameters.dhcp_client.state is defined
  - interface_parameters.dhcp_client.state == "present"
- include: configure_ip_address.yml
  no_log: true
  loop: "{{ interface_parameters.ipv4 }}"
  loop_control:
    loop_var: ipv4
  when:
  - interface_parameters.ipv4 is defined
  - ipv4.state is defined
================================================

File: configure_interface_lists.yml
================================================
- name: "[MikroTik] [Interfaces] Create/Update list interface {{ interface_parameters.name }}"
  register: interface_list_status
  routeros_command:
    commands:
    - :if ([/interface list find name={{ interface_parameters.name }}])
      do={
        /interface list set {{ interface_parameters.name }}
        comment="{{ interface_parameters.comment |default('') }}"
        include="{{ interface_parameters.include | join(',') |default('') }}"
        exclude="{{ interface_parameters.exclude | join(',') |default('') }}"
      }
      else={
        /interface list add name={{ interface_parameters.name }}
        comment="{{ interface_parameters.comment |default('') }}"
        include="{{ interface_parameters.include | join(',') |default('') }}"
        exclude="{{ interface_parameters.exclude | join(',') |default('') }}"
      }
  when: interface_parameters.state == "present"
- name: "[MikroTik] [Interfaces] Add/Update interface to list interface {{ interface_parameters.name }}"
  no_log: true
  register: interface_list_status
  routeros_command:
    commands:
    - :if ([/interface list member find interface={{ add_interface.interface }} and list={{ interface_parameters.name }}])
      do={
        /interface list member set [find interface={{ add_interface.interface }} and list={{ interface_parameters.name }}]
        comment="{{ add_interface.comment |default('') }}"
        disabled="{{ add_interface.disabled | default('no') }}"
      }
      else={
        /interface list member add interface={{ add_interface.interface }} list={{ interface_parameters.name }}
        comment="{{ add_interface.comment |default('') }}"
        disabled="{{ add_interface.disabled | default('no') }}"
      }
  loop: "{{ interface_parameters.members }}"
  loop_control:
    loop_var: add_interface
  when:
  - interface_parameters.state == "present"
  - interface_parameters.members is defined
  - add_interface.state is defined
  - add_interface.state == "present"
- name: "[MikroTik] [Interfaces] Remove interface to list interface {{ interface_parameters.name }}"
  no_log: true
  register: interface_list_status
  routeros_command:
    commands:
    - /interface list member remove [find interface={{ rem_interface.name }} and list={{ interface_parameters.name }}]
  loop: "{{ interface_parameters.members }}"
  loop_control:
    loop_var: rem_interface
  when:
  - interface_parameters.members is defined
  - rem_interface.state is defined
  - rem_interface.state == "absent"
- name: "[MikroTik] [Interfaces] Remove list interface {{ interface_parameters.name }}"
  register: remove_interface_list_status
  routeros_command:
    commands:
    - /interface list remove ([/interface list find name={{ interface_parameters.name }}])
  when: interface_parameters.state == "absent"
================================================

File: configure_interface_vlan.yml
================================================
- name: "[MikroTik] [VLAN] Create/Update VLAN interface {{ interface_parameters.name  }}"
  routeros_command:
    commands:
    - :if ([/interface vlan find name={{ interface_parameters.name }} ])
      do={
        /interface vlan set [ find name={{ interface_parameters.name }} ] comment="{{ interface_parameters.comment | default('') }}"
        {% if interface_parameters.arp is defined %} arp={{ interface_parameters.arp }}{% endif %}
        {% if interface_parameters.disabled is defined %} disabled={{ interface_parameters.disabled }}{% endif %}
        {% if interface_parameters.arp_timeout is defined %} arp-timeout={{ interface_parameters.arp_timeout }}{% endif %}
        {% if interface_parameters.interface is defined %} interface={{ interface_parameters.interface }}{% endif %}
        {% if interface_parameters.loop_protect is defined %} loop-protect={{ interface_parameters.loop_protect }}{% endif %}
        {% if interface_parameters.loop_protect_disable_time is defined %} loop-protect-disable-time={{ interface_parameters.loop_protect_disable_time }}{% endif %}
        {% if interface_parameters.loop_protect_send_interval is defined %} loop-protect-send-interval={{ interface_parameters.loop_protect_send_interval }}{% endif %}
        {% if interface_parameters.mtu is defined %} mtu={{ interface_parameters.mtu }}{% endif %}
        {% if interface_parameters.use_service_tag is defined %} use-service-tag={{ interface_parameters.use_service_tag }}{% endif %}
        {% if interface_parameters.vlan_id is defined %} vlan-id={{ interface_parameters.vlan_id }}{% endif %}
      }
      else={
        /interface vlan add name={{ interface_parameters.name }} comment="{{ interface_parameters.comment | default('') }}"
        {% if interface_parameters.arp is defined %} arp={{ interface_parameters.arp }}{% endif %}
        {% if interface_parameters.disabled is defined %} disabled={{ interface_parameters.disabled }}{% endif %}
        {% if interface_parameters.arp_timeout is defined %} arp-timeout={{ interface_parameters.arp_timeout }}{% endif %}
        {% if interface_parameters.interface is defined %} interface={{ interface_parameters.interface }}{% endif %}
        {% if interface_parameters.loop_protect is defined %} loop-protect={{ interface_parameters.loop_protect }}{% endif %}
        {% if interface_parameters.loop_protect_disable_time is defined %} loop-protect-disable-time={{ interface_parameters.loop_protect_disable_time }}{% endif %}
        {% if interface_parameters.loop_protect_send_interval is defined %} loop-protect-send-interval={{ interface_parameters.loop_protect_send_interval }}{% endif %}
        {% if interface_parameters.mtu is defined %} mtu={{ interface_parameters.mtu }}{% endif %}
        {% if interface_parameters.use_service_tag is defined %} use-service-tag={{ interface_parameters.use_service_tag }}{% endif %}
        {% if interface_parameters.vlan_id is defined %} vlan-id={{ interface_parameters.vlan_id }}{% endif %}
      }
  register: update_interface_vlan_status
  when:
    - interface_parameters.state == "present"
- name: "[MikroTik] [VLAN] Remove vlan interface {{ interface_parameters.name }}"
  register: remove_interface_vlan_status
  routeros_command:
    commands:
    - /interface vlan remove ([find name={{ interface_parameters.name }}])
  when: interface_parameters.state == "absent"
- include: configure_dhcp_client.yml
  when:
  - interface_parameters.dhcp_client is defined
  - interface_parameters.dhcp_client.state is defined
  - interface_parameters.dhcp_client.state == "present"
- include: configure_ip_address.yml
  no_log: true
  loop: "{{ interface_parameters.ipv4 }}"
  loop_control:
    loop_var: ipv4
  when:
  - interface_parameters.ipv4 is defined
  - ipv4.state is defined
================================================

File: configure_ip_address.yml
================================================
- name: "[MikroTik] [IP Address] Set/Update IP Adress on interface {{ interface_parameters.name }}"
  register: setIPAdressOnInterface
  routeros_command:
    commands:
    - :if ([/ip address find address="{{ ipv4.address }}" network="{{ ipv4.network }}" interface={{ interface_parameters.name }} ])
      do={
        /ip address set [ find address="{{ ipv4.address }}" interface={{ interface_parameters.name }} ]
        comment="{{ ipv4.comment |default('') }}"
        network="{{ ipv4.network }}"
        disabled="{{ ipv4.disabled | default('no') }}"
      }
      else={
         /ip address add address="{{ ipv4.address }}" interface={{ interface_parameters.name }}
        comment="{{ ipv4.comment |default('') }}"
        network="{{ ipv4.network }}"
        disabled="{{ ipv4.disabled | default('no') }}"
      }
  when:
    - ipv4.state == "present"
- name: "[MikroTik] [IP Address] Remove IP Adress on interface {{ interface_parameters.name }}"
  register: remIPAdressOnInterface
  routeros_command:
    commands:
    - :if ([/ip address find address="{{ ipv4.address }}" network="{{ ipv4.network }}" interface={{ interface_parameters.name }} ])
      do={
        /ip address remove [ find address="{{ ipv4.address }}" interface={{ interface_parameters.name }} ]
      }
  when:
    - ipv4.state == "absent"
================================================

File: interface_virtual_wireless.yml
================================================
- name: "[MikroTik] [Wireless] Create/Update Virutal Wireleess interface {{ interface_parameters.name  }}"
  routeros_command:
    commands:
    - :if ([ /interface wireless find name="{{ interface_parameters.name }}" ])
      do={
        /interface wireless set [ find name={{ interface_parameters.name }} ]
        name={{ interface_parameters.name }}
        comment="{{ interface_parameters.comment | default('') }}"
        {% if interface_parameters.mtu is defined %} mtu={{ interface_parameters.mtu }}{% endif %}
        {% if interface_parameters.disabled is defined %} disabled={{ interface_parameters.disabled }}{% endif %}
        {% if interface_parameters.ssid is defined %} ssid="{{ interface_parameters.ssid }}"{% endif %}
        {% if interface_parameters.vlan_id is defined %} vlan-id={{ interface_parameters.vlan_id }}{% endif %}
        {% if interface_parameters.vlan_mode is defined %} vlan-mode={{ interface_parameters.vlan_mode }}{% endif %}
        {% if interface_parameters.area is defined %} area={{ interface_parameters.area }}{% endif %}
        {% if interface_parameters.arp is defined %} arp={{ interface_parameters.arp }}{% endif %}
        {% if interface_parameters.arp_timeout is defined %} arp-timeout={{ interface_parameters.arp_timeout }}{% endif %}
        {% if interface_parameters.band is defined %} band={{ interface_parameters.band }}{% endif %}
        {% if interface_parameters.channel_width is defined %} channel-width={{ interface_parameters.channel_width }}{% endif %}
        {% if interface_parameters.distance is defined %} distance={{ interface_parameters.distance }}{% endif %}
        {% if interface_parameters.station_roaming is defined %} station-roaming={{ interface_parameters.station_roaming }}{% endif %}
        {% if interface_parameters.installation is defined %} installation={{ interface_parameters.installation }}{% endif %}
        {% if interface_parameters.compression is defined %} compression={{ interface_parameters.compression }}{% endif %}
        {% if interface_parameters.frequency is defined %} frequency={{ interface_parameters.frequency }}{% endif %}
        {% if interface_parameters.country is defined %} country={{ interface_parameters.country }}{% endif %}
        {% if interface_parameters.l2mtu is defined %} l2mtu={{ interface_parameters.l2mtu }}{% endif %}
        {% if interface_parameters.master_interface is defined %} master-interface={{ interface_parameters.master_interface }}{% endif %}
        {% if interface_parameters.loop_protect_send_interval is defined %} loop-protect-send-interval={{ interface_parameters.loop_protect_send_interval }}{% endif %}
        {% if interface_parameters.update_stats_interval is defined %} update-stats-interval={{ interface_parameters.update_stats_interval }}{% endif %}
        {% if interface_parameters.wmm_support is defined %} wmm-support={{ interface_parameters.sfp_shuwmm_supporttdown_temperature }}{% endif %}
        {% if interface_parameters.secondary_frequency is defined %} secondary-frequency={{ interface_parameters.secondary_frequency }}{% endif %}
        {% if interface_parameters.fec_mode is defined %} fec-mode={{ interface_parameters.fec-mode }}{% endif %}
        {% if interface_parameters.wps_mode is defined %} wps-mode={{ interface_parameters.wps_mode }}{% endif %}
        {% if interface_parameters.hide_ssid is defined %} hide-ssid={{ interface_parameters.hide_ssid }}{% endif %}
        {% if interface_parameters.tx_power is defined %} tx-power={{ interface_parameters.tx_power }}{% endif %}
        {% if interface_parameters.tx_power_mode is defined %} tx-power-mode={{ interface_parameters.tx_power_mode }}{% endif %}
        {% if interface_parameters.tx_chains is defined %} tx-chains={{ interface_parameters.tx_chains }}{% endif %}
        {% if interface_parameters.rx_chains is defined %} rx-chains={{ interface_parameters.rx_chains }}{% endif %}
        {% if interface_parameters.rate_set is defined %} rate-set={{ interface_parameters.rate_set }}{% endif %}
        {% if interface_parameters.nv2_mode is defined %} nv2-mode={{ interface_parameters.nv2_mode }}{% endif %}
        {% if interface_parameters.frequency_offset is defined %} frequency-offset={{ interface_parameters.frequency_offset }}{% endif %}
        {% if interface_parameters.wds_mode is defined %} wds-mode={{ interface_parameters.wds_mode }}{% endif %}
        {% if interface_parameters.mac_address is defined %} mac-address={{ interface_parameters.mac_address }}{% endif %}
        {% if interface_parameters.mode is defined %} mode={{ interface_parameters.mode }}{% endif %}
        {% if interface_parameters.wireless_protocol is defined %} wireless-protocol={{ interface_parameters.wireless_protocol }}{% endif %}
        {% if interface_parameters.security_profile is defined %} security-profile="{{ interface_parameters.security_profile }}"{% endif %}
      }
      else={
        /interface wireless add name={{ interface_parameters.name }}
        comment="{{ interface_parameters.comment | default('') }}"
        {% if interface_parameters.mtu is defined %} mtu={{ interface_parameters.mtu }}{% endif %}
        {% if interface_parameters.disabled is defined %} disabled={{ interface_parameters.disabled }}{% endif %}
        {% if interface_parameters.ssid is defined %} ssid="{{ interface_parameters.ssid }}"{% endif %}
        {% if interface_parameters.vlan_id is defined %} vlan-id={{ interface_parameters.vlan_id }}{% endif %}
        {% if interface_parameters.vlan_mode is defined %} vlan-mode={{ interface_parameters.vlan_mode }}{% endif %}
        {% if interface_parameters.area is defined %} area={{ interface_parameters.area }}{% endif %}
        {% if interface_parameters.arp is defined %} arp={{ interface_parameters.arp }}{% endif %}
        {% if interface_parameters.arp_timeout is defined %} arp-timeout={{ interface_parameters.arp_timeout }}{% endif %}
        {% if interface_parameters.band is defined %} band={{ interface_parameters.band }}{% endif %}
        {% if interface_parameters.channel_width is defined %} channel-width={{ interface_parameters.channel_width }}{% endif %}
        {% if interface_parameters.distance is defined %} distance={{ interface_parameters.distance }}{% endif %}
        {% if interface_parameters.station_roaming is defined %} station-roaming={{ interface_parameters.station_roaming }}{% endif %}
        {% if interface_parameters.installation is defined %} installation={{ interface_parameters.installation }}{% endif %}
        {% if interface_parameters.compression is defined %} compression={{ interface_parameters.compression }}{% endif %}
        {% if interface_parameters.frequency is defined %} frequency={{ interface_parameters.frequency }}{% endif %}
        {% if interface_parameters.country is defined %} country={{ interface_parameters.country }}{% endif %}
        {% if interface_parameters.l2mtu is defined %} l2mtu={{ interface_parameters.l2mtu }}{% endif %}
        {% if interface_parameters.master_interface is defined %} master-interface={{ interface_parameters.master_interface }}{% endif %}
        {% if interface_parameters.loop_protect_send_interval is defined %} loop-protect-send-interval={{ interface_parameters.loop_protect_send_interval }}{% endif %}
        {% if interface_parameters.update_stats_interval is defined %} update-stats-interval={{ interface_parameters.update_stats_interval }}{% endif %}
        {% if interface_parameters.wmm_support is defined %} wmm-support={{ interface_parameters.sfp_shuwmm_supporttdown_temperature }}{% endif %}
        {% if interface_parameters.secondary_frequency is defined %} secondary-frequency={{ interface_parameters.secondary_frequency }}{% endif %}
        {% if interface_parameters.fec_mode is defined %} fec-mode={{ interface_parameters.fec-mode }}{% endif %}
        {% if interface_parameters.wps_mode is defined %} wps-mode={{ interface_parameters.wps_mode }}{% endif %}
        {% if interface_parameters.hide_ssid is defined %} hide-ssid={{ interface_parameters.hide_ssid }}{% endif %}
        {% if interface_parameters.tx_power is defined %} tx-power={{ interface_parameters.tx_power }}{% endif %}
        {% if interface_parameters.tx_power_mode is defined %} tx-power-mode={{ interface_parameters.tx_power_mode }}{% endif %}
        {% if interface_parameters.tx_chains is defined %} tx-chains={{ interface_parameters.tx_chains }}{% endif %}
        {% if interface_parameters.rx_chains is defined %} rx-chains={{ interface_parameters.rx_chains }}{% endif %}
        {% if interface_parameters.rate_set is defined %} rate-set={{ interface_parameters.rate_set }}{% endif %}
        {% if interface_parameters.nv2_mode is defined %} nv2-mode={{ interface_parameters.nv2_mode }}{% endif %}
        {% if interface_parameters.frequency_offset is defined %} frequency-offset={{ interface_parameters.frequency_offset }}{% endif %}
        {% if interface_parameters.wds_mode is defined %} wds-mode={{ interface_parameters.wds_mode }}{% endif %}
        {% if interface_parameters.mac_address is defined %} mac-address={{ interface_parameters.mac_address }}{% endif %}
        {% if interface_parameters.mode is defined %} mode={{ interface_parameters.mode }}{% endif %}
        {% if interface_parameters.wireless_protocol is defined %} wireless-protocol={{ interface_parameters.wireless_protocol }}{% endif %}
        {% if interface_parameters.security_profile is defined %} security-profile="{{ interface_parameters.security_profile }}"{% endif %}
      }
  register: update_interface_wireless_status
  when: interface_parameters.state == "present"
- name: "[MikroTik] [Wireless] Remove Virutal Wireleess interface {{ interface_parameters.name  }}"
  register: remove_interface_wireless_security_profiles_status
  routeros_command:
    commands:
    - /interface wireless remove ([find name="{{ interface_parameters.name }}"])
  when: interface_parameters.state == "absent"
- include: configure_dhcp_client.yml
  when:
  - interface_parameters.dhcp_client is defined
  - interface_parameters.dhcp_client.state is defined
  - interface_parameters.dhcp_client.state == "present"
- include: configure_ip_address.yml
  no_log: true
  loop: "{{ interface_parameters.ipv4 }}"
  loop_control:
    loop_var: ipv4
  when:
  - interface_parameters.ipv4 is defined
  - ipv4.state is defined
================================================

File: interface_wireless.yml
================================================
- name: "[MikroTik] [Wireless] Update Wireleess interface {{ interface_parameters.name  }}"
  routeros_command:
    commands:
    - /interface wireless set [ find default-name={{ interface_default_name }} ]
      name={{ interface_parameters.name }}
      comment="{{ interface_parameters.comment | default('') }}"
      {% if interface_parameters.mtu is defined %} mtu={{ interface_parameters.mtu }}{% endif %}
      {% if interface_parameters.disabled is defined %} disabled={{ interface_parameters.disabled }}{% endif %}
      {% if interface_parameters.ssid is defined %} ssid="{{ interface_parameters.ssid }}"{% endif %}
      {% if interface_parameters.vlan_id is defined %} vlan-id={{ interface_parameters.vlan_id }}{% endif %}
      {% if interface_parameters.vlan_mode is defined %} vlan-mode={{ interface_parameters.vlan_mode }}{% endif %}
      {% if interface_parameters.area is defined %} area={{ interface_parameters.area }}{% endif %}
      {% if interface_parameters.arp is defined %} arp={{ interface_parameters.arp }}{% endif %}
      {% if interface_parameters.arp_timeout is defined %} arp-timeout={{ interface_parameters.arp_timeout }}{% endif %}
      {% if interface_parameters.band is defined %} band={{ interface_parameters.band }}{% endif %}
      {% if interface_parameters.channel_width is defined %} channel-width={{ interface_parameters.channel_width }}{% endif %}
      {% if interface_parameters.distance is defined %} distance={{ interface_parameters.distance }}{% endif %}
      {% if interface_parameters.station_roaming is defined %} station-roaming={{ interface_parameters.station_roaming }}{% endif %}
      {% if interface_parameters.installation is defined %} installation={{ interface_parameters.installation }}{% endif %}
      {% if interface_parameters.compression is defined %} compression={{ interface_parameters.compression }}{% endif %}
      {% if interface_parameters.frequency is defined %} frequency={{ interface_parameters.frequency }}{% endif %}
      {% if interface_parameters.country is defined %} country={{ interface_parameters.country }}{% endif %}
      {% if interface_parameters.l2mtu is defined %} l2mtu={{ interface_parameters.l2mtu }}{% endif %}
      {% if interface_parameters.master_interface is defined %} master-interface={{ interface_parameters.master_interface }}{% endif %}
      {% if interface_parameters.loop_protect_send_interval is defined %} loop-protect-send-interval={{ interface_parameters.loop_protect_send_interval }}{% endif %}
      {% if interface_parameters.update_stats_interval is defined %} update-stats-interval={{ interface_parameters.update_stats_interval }}{% endif %}
      {% if interface_parameters.wmm_support is defined %} wmm-support={{ interface_parameters.sfp_shuwmm_supporttdown_temperature }}{% endif %}
      {% if interface_parameters.secondary_frequency is defined %} secondary-frequency={{ interface_parameters.secondary_frequency }}{% endif %}
      {% if interface_parameters.fec_mode is defined %} fec-mode={{ interface_parameters.fec-mode }}{% endif %}
      {% if interface_parameters.wps_mode is defined %} wps-mode={{ interface_parameters.wps_mode }}{% endif %}
      {% if interface_parameters.hide_ssid is defined %} hide-ssid ={{ interface_parameters.hide_ssid }}{% endif %}
      {% if interface_parameters.tx_power is defined %} tx-power={{ interface_parameters.tx_power }}{% endif %}
      {% if interface_parameters.tx_power_mode is defined %} tx-power-mode={{ interface_parameters.tx_power_mode }}{% endif %}
      {% if interface_parameters.tx_chains is defined %} tx-chains={{ interface_parameters.tx_chains }}{% endif %}
      {% if interface_parameters.rx_chains is defined %} rx-chains={{ interface_parameters.rx_chains }}{% endif %}
      {% if interface_parameters.rate_set is defined %} rate-set={{ interface_parameters.rate_set }}{% endif %}
      {% if interface_parameters.nv2_mode is defined %} nv2-mode={{ interface_parameters.nv2_mode }}{% endif %}
      {% if interface_parameters.frequency_offset is defined %} frequency-offset={{ interface_parameters.frequency_offset }}{% endif %}
      {% if interface_parameters.wds_mode is defined %} wds-mode={{ interface_parameters.wds_mode }}{% endif %}
      {% if interface_parameters.mac_address is defined %} mac-address={{ interface_parameters.mac_address }}{% endif %}
      {% if interface_parameters.mode is defined %} mode={{ interface_parameters.mode }}{% endif %}
      {% if interface_parameters.wireless_protocol is defined %} wireless-protocol={{ interface_parameters.wireless_protocol }}{% endif %}
      {% if interface_parameters.security_profile is defined %} security-profile="{{ interface_parameters.security_profile }}"{% endif %}
  register: update_interface_wireless_status
- include: configure_ip_address.yml
  no_log: true
  loop: "{{ interface_parameters.ipv4 }}"
  loop_control:
    loop_var: ipv4
  when:
  - interface_parameters.ipv4 is defined
  - ipv4.state is defined
- include: configure_dhcp_client.yml
  when:
  - interface_parameters.dhcp_client is defined
  - interface_parameters.dhcp_client.state is defined
  - interface_parameters.dhcp_client.state == "present"
================================================

File: interface_wireless_security_profiles.yml
================================================
- name: "[MikroTik] [Wireless] Create/Update Wireless security interface \"{{ interface_parameters.name }}\""
  routeros_command:
    commands:
    - :if ([ /interface wireless security-profiles find name="{{ interface_parameters.name }}" ])
      do={
        /interface wireless security-profiles set [ find name="{{ interface_parameters.name }}" ]
        comment="{{ interface_parameters.comment | default('') }}"
        {% if interface_parameters.authentication_types is defined %} authentication-types={{ interface_parameters.authentication_types }}{% endif %}
        {% if interface_parameters.disable_pmkid is defined %} disable-pmkid={{ interface_parameters.disable_pmkid }}{% endif %}
        {% if interface_parameters.group_key_update is defined %} group-key-update={{ interface_parameters.group_key_update }}{% endif %}
        {% if interface_parameters.management_protection_key is defined %} management-protection-key={{ interface_parameters.management_protection_key }}{% endif %}
        {% if interface_parameters.mschapv2_username is defined %} mschapv2-username={{ interface_parameters.mschapv2_username }}{% endif %}
        {% if interface_parameters.radius_eap_accounting is defined %} radius-eap-accounting={{ interface_parameters.radius_eap_accounting }}{% endif %}
        supplicant-identity={{ input_role_ansible_host }}
        {% if interface_parameters.eap_methods is defined %} eap-methods={{ interface_parameters.eap_methods }}{% endif %}
        {% if interface_parameters.interim_update is defined %} interim-update={{ interface_parameters.interim_update }}{% endif %}
        {% if interface_parameters.radius_mac_accounting is defined %} radius-mac-accounting={{ interface_parameters.radius_mac_accounting }}{% endif %}
        {% if interface_parameters.radius_mac_authentication is defined %} radius-mac-authentication={{ interface_parameters.radius_mac_authentication }}{% endif %}
        {% if interface_parameters.radius_mac_caching is defined %} radius-mac-caching={{ interface_parameters.radius_mac_caching }}{% endif %}
        {% if interface_parameters.radius_mac_format is defined %} radius-mac-format={{ interface_parameters.radius_mac_format }}{% endif %}
        {% if interface_parameters.radius_mac_mode is defined %} radius-mac-mode={{ interface_parameters.radius_mac_mode }}{% endif %}
        {% if interface_parameters.tls_certificate is defined %} tls-certificate={{ interface_parameters.tls_certificate }}{% endif %}
        {% if interface_parameters.group_ciphers is defined %} group-ciphers={{ interface_parameters.group_ciphers }}{% endif %}
        {% if interface_parameters.unicast_ciphers is defined %} unicast-ciphers={{ interface_parameters.unicast_ciphers }}{% endif %}
        {% if interface_parameters.management_protection is defined %} management-protection={{ interface_parameters.management_protection }}{% endif %}
        {% if interface_parameters.mschapv2_password is defined %} mschapv2-password={{ interface_parameters.mschapv2_password }}{% endif %}
        {% if interface_parameters.radius_called_format is defined %} radius-called-format={{ interface_parameters.radius_called_format }}{% endif %}
        {% if interface_parameters.tls_mode is defined %} tls-mode={{ interface_parameters.tls_mode }}{% endif %}
        wpa-pre-shared-key="{{ interface_parameters.password }}"
        wpa2-pre-shared-key="{{ interface_parameters.password }}"
        {% if interface_parameters.mode is defined %} mode={{ interface_parameters.mode }}{% endif %}
      }
      else={
        /interface wireless security-profiles add name="{{ interface_parameters.name }}"
        comment="{{ interface_parameters.comment | default('') }}"
        {% if interface_parameters.authentication_types is defined %} authentication-types={{ interface_parameters.authentication_types }}{% endif %}
        {% if interface_parameters.disable_pmkid is defined %} disable-pmkid={{ interface_parameters.disable_pmkid }}{% endif %}
        {% if interface_parameters.group_key_update is defined %} group-key-update={{ interface_parameters.group_key_update }}{% endif %}
        {% if interface_parameters.management_protection_key is defined %} management-protection-key={{ interface_parameters.management_protection_key }}{% endif %}
        {% if interface_parameters.mschapv2_username is defined %} mschapv2-username={{ interface_parameters.mschapv2_username }}{% endif %}
        {% if interface_parameters.radius_eap_accounting is defined %} radius-eap-accounting={{ interface_parameters.radius_eap_accounting }}{% endif %}
        supplicant-identity={{ input_role_ansible_host }}
        {% if interface_parameters.eap_methods is defined %} eap-methods={{ interface_parameters.eap_methods }}{% endif %}
        {% if interface_parameters.interim_update is defined %} interim-update={{ interface_parameters.interim_update }}{% endif %}
        {% if interface_parameters.radius_mac_accounting is defined %} radius-mac-accounting={{ interface_parameters.radius_mac_accounting }}{% endif %}
        {% if interface_parameters.radius_mac_authentication is defined %} radius-mac-authentication={{ interface_parameters.radius_mac_authentication }}{% endif %}
        {% if interface_parameters.radius_mac_caching is defined %} radius-mac-caching={{ interface_parameters.radius_mac_caching }}{% endif %}
        {% if interface_parameters.radius_mac_format is defined %} radius-mac-format={{ interface_parameters.radius_mac_format }}{% endif %}
        {% if interface_parameters.radius_mac_mode is defined %} radius-mac-mode={{ interface_parameters.radius_mac_mode }}{% endif %}
        {% if interface_parameters.tls_certificate is defined %} tls-certificate={{ interface_parameters.tls_certificate }}{% endif %}
        {% if interface_parameters.group_ciphers is defined %} group-ciphers={{ interface_parameters.group_ciphers }}{% endif %}
        {% if interface_parameters.management_protection is defined %} management-protection={{ interface_parameters.management_protection }}{% endif %}
        {% if interface_parameters.mschapv2_password is defined %} mschapv2-password={{ interface_parameters.mschapv2_password }}{% endif %}
        {% if interface_parameters.radius_called_format is defined %} radius-called-format={{ interface_parameters.radius_called_format }}{% endif %}
        {% if interface_parameters.tls_mode is defined %} tls-mode={{ interface_parameters.tls_mode }}{% endif %}
        wpa-pre-shared-key="{{ interface_parameters.password }}"
        wpa2-pre-shared-key="{{ interface_parameters.password }}"
        {% if interface_parameters.mode is defined %} mode={{ interface_parameters.mode }}{% endif %}
      }
  register: update_interface_wireless_security_profiles_status
  when:
    - interface_parameters.state == "present"
- name: "[MikroTik] [Wireless] Wireless security interface {{ interface_parameters.name }}"
  register: remove_interface_wireless_security_profiles_status
  routeros_command:
    commands:
    - /interface wireless security-profiles remove ([find name="{{ interface_parameters.name }}"])
  when: interface_parameters.state == "absent"
================================================

File: main.yml
================================================
- include: setup_role.yml
- include: interface_wireless_security_profiles.yml
  no_log: true
  loop: "{{ lookup('dict', var_interfaces_wireless_security_profiles) }}"
  vars:
    interface_name: "{{ item.key }}"
    interface_parameters: "{{ item.value }}"
  when:
  - input_role_enabled.configure_wireless_secuirty is true
  - var_interfaces_wireless_security_profiles is defined
  - interface_name != "default"
- include: interface_wireless.yml
  no_log: true
  loop: "{{ lookup('dict', var_interfaces_wireless) }}"
  vars:
    interface_default_name: "{{ item.key }}"
    interface_parameters: "{{ item.value }}"
  when:
    - input_role_enabled.configure_wireless is true
    - var_interfaces_wireless is defined
    - interface_default_name != "default"
- include: interface_virtual_wireless.yml
  no_log: true
  loop: "{{ lookup('dict', var_interfaces_virtual_wireless) }}"
  vars:
    interface_name: "{{ item.key }}"
    interface_parameters: "{{ item.value }}"
  when:
    - input_role_enabled.configure_virtual_wireless is true
    - var_interfaces_virtual_wireless is defined
    - interface_name != "default"
- include: configure_interface_ethernet.yml
  no_log: true
  loop: "{{ lookup('dict', var_interfaces_ethernet) }}"
  vars:
    interface_default_name: "{{ item.key }}"
    interface_parameters: "{{ item.value }}"
  when:
    - var_interfaces_ethernet is defined
    - input_role_enabled.configure_ethernet is true
    - interface_default_name != "default"
- include: configure_interface_bounding.yml
  no_log: true
  loop: "{{ lookup('dict', var_interfaces_bounding) }}"
  vars:
    interface_name: "{{ item.key }}"
    interface_parameters: "{{ item.value }}"
  when:
    - var_interfaces_bounding is defined
    - input_role_enabled.configure_bounding is true
    - interface_name != "default"
- include: configure_interface_vlan.yml
  no_log: true
  loop: "{{ lookup('dict', var_interfaces_vlan) }}"
  vars:
    interface_vlan_name: "{{ item.key }}"
    interface_parameters: "{{ item.value }}"
  when:
    - var_interfaces_vlan is defined
    - input_role_enabled.configure_vlan is true
    - interface_vlan_name != "default"
- include: configure_interface_lists.yml
  no_log: true
  loop: "{{ lookup('dict', var_list_interfaces) }}"
  vars:
    interface_list_name: "{{ item.key }}"
    interface_parameters: "{{ item.value }}"
  when:
    - var_list_interfaces is defined
    - input_role_enabled.configure_interface_list is true
    - interface_list_name != "default"
- include: configure_interface_bridge.yml
  no_log: true
  loop: "{{ lookup('dict', var_interfaces_bridge) }}"
  vars:
    interface_bridge_name: "{{ item.key }}"
    interface_parameters: "{{ item.value }}"
  when:
    - var_interfaces_bridge is defined
    - input_role_enabled.configure_bridge is true
    - interface_bridge_name != "default"
================================================

File: setup_role.yml
================================================
- name: "[Setup] Set variables"
  set_fact:
    var_interfaces_wireless_security_profiles: "{{ input_role_interfaces_wireless_security_profiles | combine({'default': '' }) }}"
    var_interfaces_wireless:                   "{{ input_role_interfaces_wireless | combine({'default': '' }) }}"
    var_interfaces_virtual_wireless:           "{{ input_role_interfaces_virtual_wireless | combine({'default': '' }) }}"
    var_interfaces_ethernet:                   "{{ input_role_interfaces_ethernet | combine({'default': '' }) }}"
    var_interfaces_bounding:                   "{{ input_role_interfaces_bounding | combine({'default': '' }) }}"
    var_interfaces_vlan:                       "{{ input_role_interfaces_vlan | combine({'default': '' }) }}"
    var_list_interfaces:                       "{{ input_role_interfaces_list | combine({'default': '' }) }}"
    var_interfaces_bridge:                     "{{ input_role_interfaces_bridge | combine({'default': '' }) }}"
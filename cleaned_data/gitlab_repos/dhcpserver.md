# Repository Information
Name: dhcpserver

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
	url = https://gitlab.com/rachuna-net.pl/tools/ansibleroles/mikrotik/dhcpserver.git
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
- Konfiguracja serwera DHCP
- Konfiguracja dzierżawy hostów przez serwer DHCP
================================================

File: main.yml
================================================
input_role_interfaces: []
# examples
#   BRIDGE-USERS:
#     name: "BRIDGE-USERS"
#     comment: "BRIDGE - Users"
#     state: present
#     port:
#     - interface: LIST-LAN-USERS
#       ingress_filtering: "no"
#       state: present
#     ipv4:
#     - address: "192.168.0.1/24"
#       network: "192.168.0.0"
#       comment: ""
#       state: present
#     dhcp_server:
#     - name: users-network-dhcp
#       state: present
#       lease_time: 23h59m59s
#       pools:
#       - name: users-network-pool
#         comment: "Users Network Pool"
#         ranges: "192.168.0.2-192.168.0.254"
#         state: present
#       networks:
#       - address: "192.168.0.0/24"
#         boot_file_name: ""
#         comment: "Users Network"
#         dns_server: 192.168.0.1
#         domain: mydomain.com
#         gateway: 192.168.0.1
#         state: present
#       leases:
#         - address: 192.168.0.2
#           mac_address: AA:BB:CC:DD:EE:FF
#           comment: "notebook"
#           state: present
#         - address: 192.168.0.3
#           mac_address: AA:AA:AA:AA:AA:AA
#           comment: "printer"
#           state: present
================================================

File: README.md
================================================
# dhcpserver
Ansible Role - Mikrotik - Configure DHCP Servers
### Wymagania
```bash
apt-get install sshpass python3-pip
pip install paramiko
```
### Zmienne
Role Variables
--------------
```yaml
input_role_interfaces: []
```
Konfiguracja serwera DHCP znajduje się w konfiguracji interface jako atrybut `dhcp_server`
```yaml
# Przykładowa konfiguracja
input_role_interfaces:
  BRIDGE-USERS:
    name: "BRIDGE-USERS"
    comment: "BRIDGE - Users"
    state: present
    # parametry interface
    (...)
    # Konfiguracja serwera DHCP
    dhcp_server:
    - name: users-network-dhcp
      state: present
      lease_time: 1d
      # konfiguracja puli adresowej
      pools:
      - name: users-network-pool
        comment: "Users Network Pool"
        ranges: "192.168.0.2-192.168.0.254"
        state: present
      # konfiguracja sieci DHCP
      networks:
      - address: "192.168.0.0/24"
        boot_file_name: ""
        comment: "Users Network"
        dns_server: 192.168.0.1
        domain: mydomain.com
        gateway: 192.168.0.1
        state: present
      # Ustwienie dzierżawy
      leases:
      - address: 192.168.0.2
        mac_address: AA:BB:CC:DD:EE:FF
        comment: "notebook"
        state: present
      - address: 192.168.0.3
        mac_address: AA:AA:AA:AA:AA:AA
        comment: "printer"
        state: present
```
### Przykładowy playbook
```yaml
- name: Mikrotk - Configure DHCP
  hosts: routeros
  gather_facts: false
  tasks:
    - include_role:
        input_role_interfaces:
          BRIDGE-USERS:
              name: "BRIDGE-USERS"
              # comment: "BRIDGE - Users"
              # state: present
              # port:
              # - interface: LIST-LAN-USERS
              #   ingress_filtering: "no"
              #   state: present
              # ipv4:
              # - address: "192.168.0.1/24"
              #   network: "192.168.0.0"
              #   comment: ""
              #   state: present
              dhcp_server:
              - name: users-network-dhcp
                state: present
                lease_time: 23h59m59s
                pools:
                - name: users-network-pool
                  comment: "Users Network Pool"
                  ranges: "192.168.0.2-192.168.0.254"
                  state: present
                networks:
                - address: "192.168.0.0/24"
                  boot_file_name: ""
                  comment: "Users Network"
                  dns_server: 192.168.0.1
                  domain: mydomain.com
                  gateway: 192.168.0.1
                  state: present
                leases:
                - address: 192.168.0.2
                  mac_address: AA:BB:CC:DD:EE:FF
                  comment: "notebook"
                  state: present
                - address: 192.168.0.3
                  mac_address: AA:AA:AA:AA:AA:AA
                  comment: "printer"
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

File: configure_dhcp_server.yml
================================================
- include: dhcp_pools.yml
  no_log: true
  loop: "{{ dhcp_server.pools }}"
  loop_control:
    loop_var: pool_parameters
- include: dhcp_networks.yml
  no_log: true
  loop: "{{ dhcp_server.networks }}"
  loop_control:
    loop_var: network_parameters
- name: "[MikroTik] [DHCP Server] Create/Update dhcp-server for {{ interface_parameters.name }}"
  routeros_command:
    commands:
    - :if ([/ip dhcp-server find name={{ dhcp_server.name }} ])
      do={
        /ip dhcp-server set {{ dhcp_server.name }}
        comment="{{ dhcp_server.comment | default('') }}"
        interface={{ interface_parameters.name }}
        address-pool={{ dhcp_server.pools[0].name }}
        disabled={{ dhcp_server.disabled | default('no') }}
        {% if dhcp_server.lease_time is defined %} lease-time={{ dhcp_server.lease_time }}{% endif %}
        {% if dhcp_server.allow_dual_stack_queue is defined %} allow-dual-stack-queue={{ dhcp_server.allow_dual_stack_queue }}{% endif %}
        {% if dhcp_server.bootp_lease_time is defined %} bootp-lease-time={{ dhcp_server.bootp_lease_time }}{% endif %}
        {% if dhcp_server.dhcp_option_set is defined %} dhcp-option-set={{ dhcp_server.dhcp_option_set }}{% endif %}
        {% if dhcp_server.relay is defined %} relay={{ dhcp_server.relay }}{% endif %}
        {% if dhcp_server.use_radius is defined %} use-radius={{ dhcp_server.use_radius }}{% endif %}
        {% if dhcp_server.add_arp is defined %} add-arp={{ dhcp_server.add_arp }}{% endif %}
        {% if dhcp_server.always_broadcast is defined %} always-broadcast={{ dhcp_server.always_broadcast }}{% endif %}
        {% if dhcp_server.bootp_support is defined %} bootp-support={{ dhcp_server.bootp_support }}{% endif %}
        {% if dhcp_server.conflict_detection is defined %} conflict-detection={{ dhcp_server.conflict_detection }}{% endif %}
        {% if dhcp_server.lease_script is defined %} lease-script={{ dhcp_server.lease_script }}{% endif %}
        {% if dhcp_server.server_address is defined %} server-address={{ dhcp_server.server_address }}{% endif %}
        {% if dhcp_server.authoritative is defined %} authoritative={{ dhcp_server.authoritative }}{% endif %}
        {% if dhcp_server.client_mac_limit is defined %} client-mac-limit={{ dhcp_server.client_mac_limit }}{% endif %}
        {% if dhcp_server.delay_threshold is defined %} delay-threshold={{ dhcp_server.delay_threshold }}{% endif %}
        {% if dhcp_server.insert_queue_before is defined %} insert-queue-before={{ dhcp_server.insert_queue_before }}{% endif %}
        {% if dhcp_server.parent_queue is defined %} parent-queue={{ dhcp_server.parent_queue }}{% endif %}
        {% if dhcp_server.use_framed_as_classless is defined %} use-framed-as-classless={{ dhcp_server.use_framed_as_classless }}{% endif %}
      }
      else={
        /ip dhcp-server add name={{ dhcp_server.name }} comment="{{ dhcp_server.comment | default('') }}"
        interface={{ interface_parameters.name }}
        address-pool={{ dhcp_server.pools[0].name }}
        disabled={{ dhcp_server.disabled | default('no') }}
        {% if dhcp_server.lease_time is defined %} lease-time={{ dhcp_server.lease_time }}{% endif %}
        {% if dhcp_server.allow_dual_stack_queue is defined %} allow-dual-stack-queue={{ dhcp_server.allow_dual_stack_queue }}{% endif %}
        {% if dhcp_server.bootp_lease_time is defined %} bootp-lease-time={{ dhcp_server.bootp_lease_time }}{% endif %}
        {% if dhcp_server.dhcp_option_set is defined %} dhcp-option-set={{ dhcp_server.dhcp_option_set }}{% endif %}
        {% if dhcp_server.relay is defined %} relay={{ dhcp_server.relay }}{% endif %}
        {% if dhcp_server.use_radius is defined %} use-radius={{ dhcp_server.use_radius }}{% endif %}
        {% if dhcp_server.add_arp is defined %} add-arp={{ dhcp_server.add_arp }}{% endif %}
        {% if dhcp_server.always_broadcast is defined %} always-broadcast={{ dhcp_server.always_broadcast }}{% endif %}
        {% if dhcp_server.bootp_support is defined %} bootp-support={{ dhcp_server.bootp_support }}{% endif %}
        {% if dhcp_server.conflict_detection is defined %} conflict-detection={{ dhcp_server.conflict_detection }}{% endif %}
        {% if dhcp_server.lease_script is defined %} lease-script={{ dhcp_server.lease_script }}{% endif %}
        {% if dhcp_server.server_address is defined %} server-address={{ dhcp_server.server_address }}{% endif %}
        {% if dhcp_server.authoritative is defined %} authoritative={{ dhcp_server.authoritative }}{% endif %}
        {% if dhcp_server.client_mac_limit is defined %} client-mac-limit={{ dhcp_server.client_mac_limit }}{% endif %}
        {% if dhcp_server.delay_threshold is defined %} delay-threshold={{ dhcp_server.delay_threshold }}{% endif %}
        {% if dhcp_server.insert_queue_before is defined %} insert-queue-before={{ dhcp_server.insert_queue_before }}{% endif %}
        {% if dhcp_server.parent_queue is defined %} parent-queue={{ dhcp_server.parent_queue }}{% endif %}
        {% if dhcp_server.use_framed_as_classless is defined %} use-framed-as-classless={{ dhcp_server.use_framed_as_classless }}{% endif %}
      }
  register: update_dhcp_server
  when:
    - dhcp_server.state == "present"
- name: "[MikroTik] [DHCP Server] Remove dhcp-server for {{ interface_parameters.name }}"
  routeros_command:
    commands:
    - :if ([/ip dhcp-server find name={{ dhcp_server.name }} ])
      do={
        /ip pool remove {{ dhcp_server.name }}
      }
  register: remove_dhcp_server
  when:
    - dhcp_server.state == "absent"
- include: dhcp_lease.yml
  no_log: true
  loop: "{{ dhcp_server.leases }}"
  loop_control:
    loop_var: leases_parameters
================================================

File: dhcp_lease.yml
================================================
- name: "[MikroTik] [DHCP Server] Add/Update lease on dhcp-server for {{ interface_parameters.name }}"
  routeros_command:
    commands:
    - :if ([/ip dhcp-server lease find mac-address={{ leases_parameters.mac_address }} and server={{ dhcp_server.name }} ])
      do={
        /ip dhcp-server lease set [ find mac-address={{ leases_parameters.mac_address }} and server={{ dhcp_server.name }} ]
        address={{ leases_parameters.address }}
        comment="{{ leases_parameters.comment | default('') }}"
        disabled={{ leases_parameters.disabled | default('no') }}
        server={{ dhcp_server.name }}
        {% if leases_parameters.client_id is defined %} client-id={{ leases_parameters.client_id }}{% endif %}
        {% if leases_parameters.lease_time is defined %} lease-time={{ leases_parameters.lease-time }}{% endif %}
        {% if leases_parameters.allow_dual_stack_queue is defined %} allow-dual-stack-queue={{ leases_parameters.allow_dual_stack_queue }}{% endif %}
        {% if leases_parameters.block_access is defined %} block-access={{ leases_parameters.block_access }}{% endif %}
        {% if leases_parameters.dhcp_option_set  is defined %} dhcp-option-set ={{ leases_parameters.dhcp_option_set }}{% endif %}
        {% if leases_parameters.insert_queue_before is defined %} insert-queue-before  queue-type={{ leases_parameters.insert_queue_before }}{% endif %}
        {% if leases_parameters.use_src_mac is defined %} use-src-mac={{ leases_parameters.use_src_mac }}{% endif %}
        {% if leases_parameters.address_lists is defined %} address-lists={{ leases_parameters.address_lists }}{% endif %}
        {% if leases_parameters.always_broadcast  is defined %} always-broadcast ={{ leases_parameters.always_broadcast }}{% endif %}
        {% if leases_parameters.dhcp_option is defined %} dhcp-option={{ leases_parameters.dhcp_option }}{% endif %}
        {% if leases_parameters.parent_queue  is defined %} parent-queue ={{ leases_parameters.parent_queue }}{% endif %}
        {% if leases_parameters.rate_limit is defined %} rate-limit={{ leases_parameters.rate_limit }}{% endif %}
        {% if leases_parameters.routes is defined %} routes={{ leases_parameters.routes }}{% endif %}
      }
      else={
        /ip dhcp-server lease add mac-address={{ leases_parameters.mac_address }}
        server={{ dhcp_server.name }}
        address={{ leases_parameters.address }}
        comment="{{ leases_parameters.comment | default('') }}"
        disabled={{ leases_parameters.disabled | default('no') }}
        {% if leases_parameters.client_id is defined %} client-id={{ leases_parameters.client_id }}{% endif %}
        {% if leases_parameters.lease_time is defined %} lease-time={{ leases_parameters.lease-time }}{% endif %}
        {% if leases_parameters.allow_dual_stack_queue is defined %} allow-dual-stack-queue={{ leases_parameters.allow_dual_stack_queue }}{% endif %}
        {% if leases_parameters.block_access is defined %} block-access={{ leases_parameters.block_access }}{% endif %}
        {% if leases_parameters.dhcp_option_set  is defined %} dhcp-option-set ={{ leases_parameters.dhcp_option_set }}{% endif %}
        {% if leases_parameters.insert_queue_before is defined %} insert-queue-before  queue-type={{ leases_parameters.insert_queue_before }}{% endif %}
        {% if leases_parameters.use_src_mac is defined %} use-src-mac={{ leases_parameters.use_src_mac }}{% endif %}
        {% if leases_parameters.address_lists is defined %} address-lists={{ leases_parameters.address_lists }}{% endif %}
        {% if leases_parameters.always_broadcast  is defined %} always-broadcast ={{ leases_parameters.always_broadcast }}{% endif %}
        {% if leases_parameters.dhcp_option is defined %} dhcp-option={{ leases_parameters.dhcp_option }}{% endif %}
        {% if leases_parameters.parent_queue  is defined %} parent-queue ={{ leases_parameters.parent_queue }}{% endif %}
        {% if leases_parameters.rate_limit is defined %} rate-limit={{ leases_parameters.rate_limit }}{% endif %}
        {% if leases_parameters.routes is defined %} routes={{ leases_parameters.routes }}{% endif %}
      }
  register: update_leases
  when:
    - dhcp_server.leases is defined
    - leases_parameters.state == "present"
- name: "[MikroTik] [DHCP Server] Remove lease on dhcp-server for {{ interface_parameters.name }}"
  routeros_command:
    commands:
    - :if ([/ip dhcp-server lease find mac-address={{ leases_parameters.mac_address }} and server={{ dhcp_server.name }} ])
      do={
        /ip dhcp-server lease remove [ find mac-address={{ leases_parameters.mac_address }} and server={{ dhcp_server.name }} ]
      }
  register: remove_leases
  when:
    - dhcp_server.leases is defined
    - leases_parameters.state == "absent"
================================================

File: dhcp_networks.yml
================================================
- name: "[MikroTik] [DHCP Server] Create/Update dhcp-server network for {{ dhcp_server.name }} server dhcp"
  routeros_command:
    commands:
    - :if ([/ip dhcp-server network find address="{{ network_parameters.address }}" ])
      do={
        /ip dhcp-server network set [find address="{{ network_parameters.address }}"]
        comment="{{ network_parameters.comment | default('') }}"
        gateway="{{ network_parameters.gateway }}"
        {% if network_parameters.netmask is defined %} netmask={{ network_parameters.netmask }}{% endif %}
        {% if network_parameters.boot_file_name is defined %} boot-file-name="{{ network_parameters.boot_file_name }}"{% endif %}
        {% if network_parameters.caps_manager is defined %} caps-manager={{ network_parameters.caps_manager }}{% endif %}
        {% if network_parameters.dhcp_option is defined %} dhcp-option={{ network_parameters.dhcp_option }}{% endif %}
        {% if network_parameters.dhcp_option_set is defined %} dhcp-option-set={{ network_parameters.dhcp_option_set }}{% endif %}
        {% if network_parameters.dns_none is defined %} dns-none={{ network_parameters.dns_none }}{% endif %}
        {% if network_parameters.dns_server is defined %} dns-server={{ network_parameters.dns_server }}{% endif %}
        {% if network_parameters.domain is defined %} domain={{ network_parameters.domain }}{% endif %}
        {% if network_parameters.next_server is defined %} next-server={{ network_parameters.next_server }}{% endif %}
        {% if network_parameters.ntp_server is defined %} ntp-server={{ network_parameters.ntp_server }}{% endif %}
        {% if network_parameters.wins_server is defined %} wins-server={{ network_parameters.wins_server }}{% endif %}
      }
      else={
        /ip dhcp-server network add address={{ network_parameters.address }}
        comment="{{ network_parameters.comment | default('') }}"
        gateway="{{ network_parameters.gateway }}"
        {% if network_parameters.netmask is defined %} netmask={{ network_parameters.netmask }}{% endif %}
        {% if network_parameters.boot_file_name is defined %} boot-file-name="{{ network_parameters.boot_file_name }}"{% endif %}
        {% if network_parameters.caps_manager is defined %} caps-manager={{ network_parameters.caps_manager }}{% endif %}
        {% if network_parameters.dhcp_option is defined %} dhcp-option={{ network_parameters.dhcp_option }}{% endif %}
        {% if network_parameters.dhcp_option_set is defined %} dhcp-option-set={{ network_parameters.dhcp_option_set }}{% endif %}
        {% if network_parameters.dns_none is defined %} dns-none={{ network_parameters.dns_none }}{% endif %}
        {% if network_parameters.dns_server is defined %} dns-server={{ network_parameters.dns_server }}{% endif %}
        {% if network_parameters.domain is defined %} domain={{ network_parameters.domain }}{% endif %}
        {% if network_parameters.next_server is defined %} next-server={{ network_parameters.next_server }}{% endif %}
        {% if network_parameters.ntp_server is defined %} ntp-server={{ network_parameters.ntp_server }}{% endif %}
        {% if network_parameters.wins_server is defined %} wins-server={{ network_parameters.wins_server }}{% endif %}
      }
  register: update_network
  when:
  - network_parameters.state == "present"
- name: "[MikroTik] [DHCP Server] Remove dhcp-server network for {{ dhcp_server.name }} server dhcp"
  routeros_command:
    commands:
    - :if ([/ip dhcp-server network find address={{ network_parameters.address }} ])
      do={
        /ip dhcp-server network remove [find address="{{ network_parameters.address }}"]
      }
  register: remove_network
  when:
    - network_parameters.state == "absent"
================================================

File: dhcp_pools.yml
================================================
- name: "[MikroTik] [DHCP Server] Create/Update ip pool for {{ dhcp_server.name }} server dhcp"
  routeros_command:
    commands:
    - :if ([/ip pool find name={{ pool_parameters.name }} ])
      do={
        /ip pool set {{ pool_parameters.name }}
        comment="{{ pool_parameters.comment | default('') }}"
        ranges={{ pool_parameters.ranges }}
        {% if pool_parameters.next_pool is defined %} next-pool={{ pool_parameters.next_pool }}{% endif %}
      }
      else={
        /ip pool add
        name={{ pool_parameters.name }}
        comment="{{ pool_parameters.comment | default('') }}"
        ranges={{ pool_parameters.ranges }}
        {% if pool_parameters.next_pool is defined %} next-pool={{ pool_parameters.next_pool }}{% endif %}
      }
  register: update_ip_pool
  when:
  - pool_parameters.state == "present"
- name: "[MikroTik] [DHCP Server] Remove ip pool for {{ dhcp_server.name }} server dhcp"
  routeros_command:
    commands:
    - :if ([/ip pool find name={{ pool_parameters.name }} ])
      do={
       /ip pool remove {{ pool_parameters.name }}
      }
  register: rem_ip_pool
  when:
  - pool_parameters.state == "absent"
================================================

File: main.yml
================================================
- include: setup_role.yml
- include: select_interface.yml
  no_log: true
  loop: "{{ lookup('dict', var_interfaces) }}"
  vars:
    interface_name: "{{ item.key }}"
    interface_parameters: "{{ item.value }}"
  when:
  - item.value.dhcp_server is defined
  - interface_name != "default"
================================================

File: select_interface.yml
================================================
- include: configure_dhcp_server.yml
  no_log: true
  loop: "{{ interface_parameters.dhcp_server }}"
  loop_control:
    loop_var: dhcp_server
================================================

File: setup_role.yml
================================================
- name: "[Setup] Set variables"
  set_fact:
    var_interfaces: "{{ input_role_interfaces | combine({'default': '' }) }}"
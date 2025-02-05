# Repository Information
Name: dnsserver

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
	url = https://gitlab.com/rachuna-net.pl/tools/ansibleroles/mikrotik/dnsserver.git
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
- Konfiguracja serwera DNS
- Dodawanie rekodrów DNS
- Konfiguracja rekordów DNS w oparciu o dzierżawę z serwera DHCP
================================================

File: main.yml
================================================
input_role_enabled:
  configure_dns_server:    true
  update_dns_records:      true
input_role_dns_params:
  allow_remote_requests: "yes"
  cache_max_ttl: 1d
  servers: 8.8.8.8,4.4.4.4
  verify_doh_cert: "yes"
input_role_dns_records: []
  # app_test:
  #   type: A
  #   address: 192.168.1.10
  #   name: app_test.lan
  #   comment: "Test App"
  #   state: present
  # spf:
  #   type: TXT
  #   text: "v=spf1 mx a:mail.lan -all"
  #   name: lan
  #   comment: "[mail spf1]"
  #   state: present
input_role_interfaces:    []
# examples
# input_role_interfaces:
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
#           hostname: "notebook.lan"
#           mac_address: AA:BB:CC:DD:EE:FF
#           comment: "notebook"
#           state: present
#         - address: 192.168.0.3
#           hostname: "printer.lan"
#           mac_address: AA:AA:AA:AA:AA:AA
#           comment: "printer"
#           state: present
================================================

File: README.md
================================================
# dnsserver
Ansible Role - Mikrotik - Configure DNS Server
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
  configure_dns_server:    true
  update_dns_records:      true
```
- Configuration DNS Server:
```yaml
input_role_dns_params:
  allow_remote_requests: "yes"
  cache_max_ttl: 1d
  servers: 8.8.8.8,4.4.4.4
  verify_doh_cert: "yes"
```
### Pobieranie adresów DNS z dzierżawy ustawionej na serwerze DHCP
Tworzenie adresu DNS odbywa się poprzez zdeklarowanie w interface serwera DHCP, a następnie na podstawie dzierżawy ustawionego adresu IP
```yaml
# Przykładowa konfiguracja
input_role_interfaces:
  BRIDGE-USERS:
    name: "BRIDGE-USERS"
    comment: "BRIDGE - Users"
    state: present
    # parametry interface
    (...)
    dhcp_server:
    - name: users-network-dhcp
      state: present
      # parametry serwera dhcp
      (...)
      # ustawienie dzierżawy
      leases:
        - address: 192.168.0.2
          hostname: "notebook.lan" # zostanie utworzony rekord DNS A dla notebook.lan o adresie IP 192.168.0.2
          mac_address: AA:BB:CC:DD:EE:FF
          comment: "notebook"
          state: present
        - address: 192.168.0.3
          hostname: "printer.lan"
          mac_address: AA:AA:AA:AA:AA:AA
          comment: "printer"
          state: present
```
### Zarządzanie rekordami DNS
```yaml
input_role_dns_records:
  app_test:
    type: A
    address: 192.168.1.10
    name: app_test.lan
    comment: "Test App"
    state: present
  spf:
    type: TXT
    text: "v=spf1 mx a:mail.lan -all"
    name: lan
    comment: "[mail spf1]"
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

File: configure_dns_server.yml
================================================
- name: "[MikroTik] [DNS Server] Update parameters for dns server"
  register: update_dns_record
  routeros_command:
    commands:
    - /ip dns set
      {% if input_role_dns_params.allow_remote_requests is defined %} allow-remote-requests={{ input_role_dns_params.allow_remote_requests }}{% endif %}
      {% if input_role_dns_params.cache_size is defined %} cache-size={{ input_role_dns_params.cache_size }}{% endif %}
      {% if input_role_dns_params.cache_max_ttl is defined %} cache-max-ttl={{ input_role_dns_params.cache_max_ttl }}{% endif %}
      {% if input_role_dns_params.doh_max_server_connections is defined %} doh-max-server-connections={{ input_role_dns_params.doh_max_server_connections }}{% endif %}
      {% if input_role_dns_params.doh_max_concurrent_queries is defined %} doh-max-concurrent-queries={{ input_role_dns_params.doh_max_concurrent_queries }}{% endif %}
      {% if input_role_dns_params.max_concurrent_queries is defined %} max-concurrent-queries={{ input_role_dns_params.max_concurrent_queries }}{% endif %}
      {% if input_role_dns_params.doh_timeout is defined %} doh-timeout={{ input_role_dns_params.doh_timeout }}{% endif %}
      {% if input_role_dns_params.max_udp_packet_size is defined %} max-udp-packet-size={{ input_role_dns_params.max_udp_packet_size }}{% endif %}
      {% if input_role_dns_params.max_concurrent_tcp_sessions is defined %} max-concurrent-tcp-sessions={{ input_role_dns_params.max_concurrent_tcp_sessions }}{% endif %}
      {% if input_role_dns_params.query_total_timeout is defined %} query-total-timeout={{ input_role_dns_params.query_total_timeout }}{% endif %}
      {% if input_role_dns_params.use_doh_server is defined %} use-doh-server={{ input_role_dns_params.use_doh_server }}{% endif %}
      {% if input_role_dns_params.query_server_timeout is defined %} query-server-timeout={{ input_role_dns_params.query_server_timeout }}{% endif %}
      {% if input_role_dns_params.servers is defined %} servers={{ input_role_dns_params.servers }}{% endif %}
      {% if input_role_dns_params.verify_doh_cert is defined %} verify-doh-cert={{ input_role_dns_params.verify_doh_cert }}{% endif %}
================================================

File: dhcp_update_dns_record.yml
================================================
- name: "[MikroTik] [DNS Server] Create/Update dns record"
  no_log: true
  register: update_dns_record
  routeros_command:
    commands:
    - :if ([/ip dns static find name={{ dns_record.hostname }} ])
      do={
        /ip dns static set [ find name={{ dns_record.hostname }} ]
        address={{ dns_record.address }}
        comment="{{ '[DHCP] ' + dns_record.comment | default('') }}"
        disabled={{ dns_record.disabled | default('no') }}
        ttl={{ dns_record.ttl | default('1d') }}
      }
      else={
        /ip dns static add name={{ dns_record.hostname }}
        address={{ dns_record.address }}
        comment="{{ '[DHCP] ' + dns_record.comment | default('') }}"
        disabled={{ dns_record.disabled | default('no') }}
        ttl={{ dns_record.ttl | default('1d') }}
      }
  loop: "{{ dhcp_server.leases }}"
  loop_control:
    loop_var: dns_record
  when:
    - dns_record.state == "present"
    - dns_record.hostname is defined
    - dns_record.hostname !=''
- name: "Remove dns record"
  register: remove_dns_record
  no_log: true
  routeros_command:
    commands:
    - :if ([/ip dns static find name={{ dns_record.hostname }} ])
      do={
        /ip dns static remove [find name={{ dns_record.hostname }}]
      }
  loop: "{{ dhcp_server.leases }}"
  loop_control:
    loop_var: dns_record
  when:
    - dns_record.state == "absent"
    - dns_record.hostname is defined
    - dns_record.hostname !=''
================================================

File: main.yml
================================================
- include: setup_role.yml
- include: configure_dns_server.yml
  when:
  - input_role_dns_params is defined
  - input_role_enabled.configure_dns_server is true
- include: select_interface.yml
  no_log: true
  loop: "{{ lookup('dict', var_interfaces) }}"
  vars:
    interface_name: "{{ item.key }}"
    interface_parameters: "{{ item.value }}"
  when:
  - input_role_enabled.update_dns_records is true
  - var_interfaces is defined
  - item.value.dhcp_server is defined
  - interface_name != "default"
- include: update_dns_record.yml
  no_log: true
  loop: "{{ lookup('dict', var_dns_records) }}"
  vars:
    record_key: "{{ item.key }}"
    record_parameters: "{{ item.value }}"
  when:
  - input_role_enabled.update_dns_records is true
  - var_dns_records is defined
  - record_key != "default"
================================================

File: select_interface.yml
================================================
- include: dhcp_update_dns_record.yml
  no_log: true
  loop: "{{ interface_parameters.dhcp_server }}"
  loop_control:
    loop_var: dhcp_server
  when: dhcp_server.leases is defined
================================================

File: setup_role.yml
================================================
- name: "[Setup] Set variables"
  set_fact:
    var_interfaces:  "{{ input_role_interfaces | combine({'default': '' }) }}"
  when: input_role_interfaces is defined
- name: "[Setup] Set variables"
  set_fact:
    var_dns_records: "{{ input_role_dns_records | combine({'default': '' }) }}"
  when: input_role_dns_records is defined
================================================

File: update_dns_record.yml
================================================
- name: "[MikroTik] [DNS Server] Create/Update dns record type txt"
  register: update_dns_record_type_txt
  debug:
    msg:
    - :if ([/ip dns static find name={{ record_parameters.name }} text="{{ record_parameters.text }}" ])
      do={
        /ip dns static set [ find name={{ record_parameters.name }} text="{{ record_parameters.text }}" ]
        name={{ record_parameters.name }}
        {% if record_parameters.comment is defined %} comment="{{ record_parameters.comment }}"{% endif %}
        type={{ record_parameters.type | default('A') }}
        {% if record_parameters.regexp is defined %} regexp={{ record_parameters.regexp }}{% endif %}
        match-subdomain={{ record_parameters.match_subdomain | default('no') }}
        {% if record_parameters.address_list is defined %} address-list={{ record_parameters.address_list }}{% endif %}
        {% if record_parameters.text is defined %} text="{{ record_parameters.text }}"{% endif %}
        disabled={{ record_parameters.disabled | default('no') }}
      }
      else={
        /ip dns static add
        name={{ record_parameters.name }}
        {% if record_parameters.comment is defined %} comment="{{ record_parameters.comment }}"{% endif %}
        type={{ record_parameters.type | default('A') }}
        {% if record_parameters.regexp is defined %} regexp={{ record_parameters.regexp }}{% endif %}
        match-subdomain={{ record_parameters.match_subdomain | default('no') }}
        {% if record_parameters.address_list is defined %} address-list={{ record_parameters.address_list }}{% endif %}
        {% if record_parameters.text is defined %} text="{{ record_parameters.text }}"{% endif %}
        disabled={{ record_parameters.disabled | default('no') }}
      }
  when:
  - record_parameters.state == "present"
  - record_parameters.type == "TXT"
- name: "[MikroTik] [DNS Server] Create/Update dns record type txt"
  register: update_dns_record_type_txt
  routeros_command:
    commands:
    - :if ([/ip dns static find name={{ record_parameters.name }} text="{{ record_parameters.text }}" ])
      do={
        /ip dns static set [ find name={{ record_parameters.name }} text="{{ record_parameters.text }}" ]
        name={{ record_parameters.name }}
        {% if record_parameters.comment is defined %} comment="{{ record_parameters.comment }}"{% endif %}
        type={{ record_parameters.type | default('A') }}
        {% if record_parameters.regexp is defined %} regexp={{ record_parameters.regexp }}{% endif %}
        match-subdomain={{ record_parameters.match_subdomain | default('no') }}
        {% if record_parameters.address_list is defined %} address-list={{ record_parameters.address_list }}{% endif %}
        {% if record_parameters.text is defined %} text="{{ record_parameters.text }}"{% endif %}
        disabled={{ record_parameters.disabled | default('no') }}
      }
      else={
        /ip dns static add
        name={{ record_parameters.name }}
        {% if record_parameters.comment is defined %} comment="{{ record_parameters.comment }}"{% endif %}
        type={{ record_parameters.type | default('A') }}
        {% if record_parameters.regexp is defined %} regexp={{ record_parameters.regexp }}{% endif %}
        match-subdomain={{ record_parameters.match_subdomain | default('no') }}
        {% if record_parameters.address_list is defined %} address-list={{ record_parameters.address_list }}{% endif %}
        {% if record_parameters.text is defined %} text="{{ record_parameters.text }}"{% endif %}
        disabled={{ record_parameters.disabled | default('no') }}
      }
  when:
  - record_parameters.state == "present"
  - record_parameters.type == "TXT"
- name: "[MikroTik] [DNS Server] Create/Update dns record"
  register: update_dns_record
  routeros_command:
    commands:
    - :if ([/ip dns static find name={{ record_parameters.name }} ])
      do={
        /ip dns static set [ find name={{ record_parameters.name }} ]
        name={{ record_parameters.name }}
        {% if record_parameters.address is defined %} address={{ record_parameters.address }}{% endif %}
        {% if record_parameters.comment is defined %} comment="{{ record_parameters.comment }}"{% endif %}
        type={{ record_parameters.type }}
        {% if record_parameters.regexp is defined %} regexp={{ record_parameters.regexp }}{% endif %}
        match-subdomain={{ record_parameters.match_subdomain | default('no') }}
        {% if record_parameters.address_list is defined %} address-list={{ record_parameters.address_list }}{% endif %}
        {% if record_parameters.cname is defined %} cname={{ record_parameters.cname }}{% endif %}
        {% if record_parameters.forward_to is defined %} forward-to={{ record_parameters.forward_to }}{% endif %}
        {% if record_parameters.mx_exchange is defined %} mx-exchange={{ record_parameters.mx_exchange }}{% endif %}
        {% if record_parameters.mx_preference is defined %} mx-preference={{ record_parameters.mx_preference }}{% endif %}
        {% if record_parameters.place_before is defined %} place-before={{ record_parameters.place_before }}{% endif %}
        {% if record_parameters.ns is defined %} ns={{ record_parameters.ns }}{% endif %}
        {% if record_parameters.srv_port is defined %} srv-port={{ record_parameters.srv_port }}{% endif %}
        {% if record_parameters.srv_target is defined %} srv-target={{ record_parameters.srv_target }}{% endif %}
        {% if record_parameters.srv_priority is defined %} srv-priority={{ record_parameters.srv_priority }}{% endif %}
        {% if record_parameters.srv_weight is defined %} srv-weight={{ record_parameters.weight }}{% endif %}
        {% if record_parameters.text is defined %} text="{{ record_parameters.text }}"{% endif %}
        disabled={{ record_parameters.disabled | default('no') }}
      }
      else={
        /ip dns static add
        name={{ record_parameters.name }}
        {% if record_parameters.address is defined %} address={{ record_parameters.address }}{% endif %}
        {% if record_parameters.comment is defined %} comment="{{ record_parameters.comment }}"{% endif %}
        type={{ record_parameters.type }}
        {% if record_parameters.regexp is defined %} regexp={{ record_parameters.regexp }}{% endif %}
        match-subdomain={{ record_parameters.match_subdomain | default('no') }}
        {% if record_parameters.address_list is defined %} address-list={{ record_parameters.address_list }}{% endif %}
        {% if record_parameters.cname is defined %} cname={{ record_parameters.cname }}{% endif %}
        {% if record_parameters.forward_to is defined %} forward-to={{ record_parameters.forward_to }}{% endif %}
        {% if record_parameters.mx_exchange is defined %} mx-exchange={{ record_parameters.mx_exchange }}{% endif %}
        {% if record_parameters.mx_preference is defined %} mx-preference={{ record_parameters.mx_preference }}{% endif %}
        {% if record_parameters.place_before is defined %} place-before={{ record_parameters.place_before }}{% endif %}
        {% if record_parameters.ns is defined %} ns={{ record_parameters.ns }}{% endif %}
        {% if record_parameters.srv_port is defined %} srv-port={{ record_parameters.srv_port }}{% endif %}
        {% if record_parameters.srv_target is defined %} srv-target={{ record_parameters.srv_target }}{% endif %}
        {% if record_parameters.srv_priority is defined %} srv-priority={{ record_parameters.srv_priority }}{% endif %}
        {% if record_parameters.srv_weight is defined %} srv-weight={{ record_parameters.weight }}{% endif %}
        {% if record_parameters.text is defined %} text="{{ record_parameters.text }}"{% endif %}
        disabled={{ record_parameters.disabled | default('no') }}
      }
  when:
  - record_parameters.state == "present"
  - record_parameters.type != "TXT"
- name: "Remove dns record"
  register: remove_dns_record
  routeros_command:
    commands:
    - :if ([/ip dns static find name={{ record_parameters.name }} ])
      do={
        /ip dns static remove [find name={{ record_parameters.name }}]
      }
  when:
    - record_parameters.name == "absent"
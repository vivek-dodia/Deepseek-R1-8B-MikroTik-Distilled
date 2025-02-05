# Repository Information
Name: ansible-role-setup-chr-mikrotik

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
	url = https://gitlab.com/ansible_roles3/ansible-role-setup-chr-mikrotik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: main.yml
================================================
---
# defaults file for ansible_role_setup_chr
# replace the values of the variables with "your.." on your own
WAN_ip: your_wan_ip # 91.14.24.23
white_ip: your_white_ip_or_url # mynetname.net
primary_ntp: your_ip_ntp_server # 88.147.254.230
secondary_ntp: your_ip_second_ntp_server # 88.147.254.229
l2tp_interface_name: l2tp-in1
l2tp_user: your_name_l2tp_user # l2
l2tp_pass: your_l2tp_user_password
ipsec_pass: your_l2tp_ipsec_password
l2tp_local: your_l2tp_ip_local # 10.10.50.1
l2tp_remote: your_l2tp_ip_remote # 10.10.50.2
lan_vpn: your_l2tp_network # 10.10.50.0/30
lan_lan: your_lan_network # 192.168.1.0/24
ospf_router_id: your_ospf_router_id # 10.10.50.0
src_address_list: lan
interface_list: LAN
...
================================================

File: main.yml
================================================
---
# handlers file for ansible_role_setup_chr
================================================

File: main.yml
================================================
galaxy_info:
  author: your name
  namespace: acme
  description: your role description
  company: your company (optional)
  # If the issue tracker for your role is not on github, uncomment the
  # next line and provide a value
  # issue_tracker_url: http://example.com/issue/tracker
  # Choose a valid license ID from https://spdx.org - some suggested licenses:
  # - BSD-3-Clause (default)
  # - MIT
  # - GPL-2.0-or-later
  # - GPL-3.0-only
  # - Apache-2.0
  # - CC-BY-4.0
  license: license (GPL-2.0-or-later, MIT, etc)
  min_ansible_version: 2.9
  # If this a Container Enabled role, provide the minimum Ansible Container version.
  # min_ansible_container_version:
  #
  # Provide a list of supported platforms, and for each platform a list of versions.
  # If you don't wish to enumerate all versions for a particular platform, use 'all'.
  # To view available platforms and versions (or releases), visit:
  # https://galaxy.ansible.com/api/v1/platforms/
  #
  # platforms:
  # - name: Fedora
  #   versions:
  #   - all
  #   - 25
  # - name: SomePlatform
  #   versions:
  #   - all
  #   - 1.0
  #   - 7
  #   - 99.99
  galaxy_tags: []
    # List tags for your role here, one per line. A tag is a keyword that describes
    # and categorizes the role. Users find roles by searching for tags. Be sure to
    # remove the '[]' above, if you add tags to this list.
    #
    # NOTE: A tag is limited to a single word comprised of alphanumeric characters.
    #       Maximum 20 tags per role.
dependencies: []
  # List your role dependencies here, one per line. Be sure to remove the '[]' above,
  # if you add dependencies to this list.
================================================

File: converge.yml
================================================
---
- name: Converge
  hosts: all
  gather_facts: false
  tasks:
    - name: "Include acme.ansible_role_setup_chr"
      ansible.builtin.include_role:
        name: "acme.ansible_role_setup_chr"
================================================

File: create.yml
================================================
---
- name: Create
  hosts: localhost
  connection: local
  gather_facts: false
  no_log: "{{ molecule_no_log }}"
  tasks:
    # TODO: Developer must implement and populate 'server' variable
    - when: server.changed | default(false) | bool
      block:
        - name: Populate instance config dict
          ansible.builtin.set_fact:
            instance_conf_dict: {
              'instance': "{{ }}",
              'address': "{{ }}",
              'user': "{{ }}",
              'port': "{{ }}",
              'identity_file': "{{ }}", }
          with_items: "{{ server.results }}"
          register: instance_config_dict
        - name: Convert instance config dict to a list
          ansible.builtin.set_fact:
            instance_conf: "{{ instance_config_dict.results | map(attribute='ansible_facts.instance_conf_dict') | list }}"
        - name: Dump instance config
          ansible.builtin.copy:
            content: |
              # Molecule managed
              {{ instance_conf | to_json | from_json | to_yaml }}
            dest: "{{ molecule_instance_config }}"
            mode: 0600
================================================

File: destroy.yml
================================================
---
- name: Destroy
  hosts: localhost
  connection: local
  gather_facts: false
  no_log: "{{ molecule_no_log }}"
  tasks:
    # Developer must implement.
    # Mandatory configuration for Molecule to function.
    - name: Populate instance config
      ansible.builtin.set_fact:
        instance_conf: {}
    - name: Dump instance config
      ansible.builtin.copy:
        content: |
          # Molecule managed
          {{ instance_conf | to_json | from_json | to_yaml }}
        dest: "{{ molecule_instance_config }}"
        mode: 0600
      when: server.changed | default(false) | bool
================================================

File: molecule.yml
================================================
---
dependency:
  name: galaxy
driver:
  name: delegated
platforms:
  - name: instance
provisioner:
  name: ansible
verifier:
  name: ansible
================================================

File: verify.yml
================================================
---
# This is an example playbook to execute Ansible tests.
- name: Verify
  hosts: all
  gather_facts: false
  tasks:
  - name: Example assertion
    ansible.builtin.assert:
      that: true
================================================

File: README.md
================================================
Описание
=========
Ansible-роль предназначена для автоматической настройки программного роутера CHR от Mikrotik.
Содержит возможность автоматической настройки:
- l2tp-сервера и создание l2tp-туннеля с базовой защитой ipsec;
- firewall-правил;
- ospf-роутинга;
- отключение сервисов: ftp,www,telnet,api;
- отключение сервисных портов: ftp,tftp,h323,sip,pptp
Предварительные требования
------------
- настроен удаленный доступ на CHR (по ssh или по паролю);
- на localhost предварительно должны быть установлены:
  - paramiko (```pip install paramiko```);
  - community.routeros (```ansible-galaxy collection install community.routeros```)
Используемые переменные
--------------
В файле `defaults/main.yml` замените значения, содержащие `your ..`, на собственные. 
```
WAN_ip: your_wan_ip
white_ip: your_white_ip_or_url 
primary_ntp: your_ip_ntp_server 
secondary_ntp: your_ip_second_ntp_server 
l2tp_interface_name: l2tp-in1
l2tp_user: your_name_l2tp_user
l2tp_pass: your_l2tp_user_password
ipsec_pass: your_l2tp_ipsec_password
l2tp_local: your_l2tp_ip_local
l2tp_remote: your_l2tp_ip_remote
lan_vpn: your_l2tp_network
lan_lan: your_lan_network
ospf_router_id: your_ospf_router_id
src_address_list: lan
interface_list: LAN
```
Зависимости
------------
CHR - version 6.48.6
Пример Playbook
----------------
Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:
```
- hosts: chr
  pre_tasks:
    - name: Install paramiko python package
      ansible.builtin.pip:
        name: paramiko
      delegate_to: 127.0.0.1
  roles:
    - ansible_role_setup_chr
```
Лицензия
-------
BSD
Автор
------------------
AlZa 2022
================================================

File: main.yml
================================================
---
# tasks file for ansible_role_setup_chr
- name: RouterOS test with network_cli connection
  community.routeros.command:
    commands:
      - /system resource print
  register: system_resource_print
- name: Print its output
  debug:
    var: system_resource_print.stdout_lines
- name: Retrieve facts
  community.routeros.facts:
- debug:
    msg: "First IP address: {{ ansible_net_all_ipv4_addresses[0] }}"
- name: Setup CHR services
  community.routeros.command:
    commands: 
      - /system clock set time-zone-name=Europe/Moscow
      - /ip dns set servers=1.1.1.1,8.8.8.8
      - /ip dhcp-client add disabled=yes interface=ether1
      - /ip service set telnet disabled=yes 
      - /ip service set ftp disabled=yes
      - /ip service set www disabled=yes
      - /ip service set api disabled=yes
      - /ip service set api-ssl disabled=yes
      - /system ntp client set enabled=yes
        # - /system ntp server set enabled=yes
      - /system ntp client set primary-ntp= {{ primary_ntp }} secondary-ntp= {{ secondary_ntp }}
      - /tool bandwidth-server set enabled=no
- name: Setup CHR interfaces
  community.routeros.command:
    commands: 
     - /interface l2tp-server add name= {{ l2tp_interface_name }} user= {{ l2tp_user }}
     - /interface l2tp-server server set authentication=mschap2 enabled=yes ipsec-secret= {{ ipsec_pass }} use-ipsec=yes 
     - /interface wireguard add listen-port=13131 mtu=1420 name=wireguard1
     - /interface list add name= {{ interface_list }}
     - /interface list add name=WAN
     - /interface list member add interface=ether1 list=WAN
     - /interface list member add interface=wireguard1 list= {{ interface_list }}
     - /interface list member add interface= {{ l2tp_interface_name }} list= {{ interface_list }}
- name: Setup CHR routing
  community.routeros.command:
    commands: 
      - /ppp secret add local-address= {{ l2tp_local }} name= {{ l2tp_user }} password= {{ l2tp_pass }} profile=default-encryption remote-address= {{ l2tp_remote }} service=l2tp
      - /routing ospf instance set [ find default=yes ] router-id= {{ ospf_router_id }}
      - /routing ospf interface add authentication=md5 authentication-key=frozen80 interface= {{ l2tp_interface_name }} network-type=point-to-point
      - /routing ospf network add area=backbone network= {{ lan_vpn }}
- name: Setup CHR firewall
  community.routeros.command:
    commands: 
      - /ip firewall filter remove [/ip firewall filter find]
      - /ip firewall nat remove [/ip firewall filter find]
      - /ip firewall address-list add address= {{ white_ip }} list= {{ src_address_list }}
      - /ip firewall address-list add address= {{ lan_lan }} comment="lan" list= {{ src_address_list }}
      - /ip firewall address-list add address= {{ lan_vpn }} comment="vpn" list= {{ src_address_list }}
      - /ip firewall filter add action=drop chain=input comment="defconf_drop_invalid" connection-state=invalid
      - /ip firewall filter add action=accept chain=input comment="defconf_accept_established,related,untracked" connection-state=established,related,untracked
      - /ip firewall filter add action=accept chain=input comment="defconf_accept ICMP" protocol=icmp
      - /ip firewall filter add action=accept chain=input src-address-list= {{ src_address_list }}
      - /ip firewall filter add action=accept chain=input in-interface-list= {{ interface_list }}
      - /ip firewall filter add action=accept chain=input comment="defconf_accept to local loopback (for CAPsMAN)" disabled=yes dst-address=127.0.0.1
      - /ip firewall filter add action=accept chain=input comment="Wireguard" dst-port=13131 in-interface=ether1 protocol=udp
      - /ip firewall filter add action=drop chain=input connection-state=new in-interface=ether1 log-prefix=DROP
      - /ip firewall nat add action=src-nat chain=srcnat log-prefix=SRC out-interface=ether1 to-addresses= {{ ansible_net_all_ipv4_addresses[0] }}
      - /ip firewall service-port set ftp disabled=yes
      - /ip firewall service-port set tftp disabled=yes
      - /ip firewall service-port set h323 disabled=yes
      - /ip firewall service-port set sip disabled=yes
      - /ip firewall service-port set pptp disabled=yes
...
================================================

File: test.yml
================================================
---
- hosts: localhost
  remote_user: root
  roles:
    - ansible_role_setup_chr
================================================

File: main.yml
================================================
---
# vars file for ansible_role_setup_chr
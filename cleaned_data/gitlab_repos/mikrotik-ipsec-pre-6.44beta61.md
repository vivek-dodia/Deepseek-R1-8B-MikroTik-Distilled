# Repository Information
Name: mikrotik-ipsec-pre-6.44beta61

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
	url = https://gitlab.com/mikrotik-ansible/mikrotik-ipsec-pre-6.44beta61.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: main.yml
================================================
mikrotik_ipsec:
  delete_all_groups: false
  delete_all_identities: false
  delete_all_mode_configs: false
  delete_all_peers: false
  delete_all_policies: false
  delete_all_profiles: false
  delete_all_proposals: false
  delete_ipsec_on_target_router: true
  groups: []
  identities: []
  mode_configs: []
  peers: []
  policies: []
  profiles: []
  proposals: []
================================================

File: example.md
================================================
# Simple example of using
Here is an example of using the role.
Use it as a reference.
Be careful: the role will delete all your old IPsec configuration.
```
mikrotik_ipsec:
  delete_all_groups: false
  delete_all_identities: false
  delete_all_mode_configs: false
  delete_all_peers: false
  delete_all_policies: false
  delete_all_profiles: false
  delete_all_proposals: false
  delete_ipsec_on_target_router: true # if true - deletes script from target router
  groups: # IPsec policy groups list
    - name: group 1 # Required. IPsec policy group name
      comment: comment 1 # Required. IPsec policy group comment
  identities: # IPsec identities list
    - peer: 10.8.0.1 # Required. IP address of IPsec peer (peer must exist in peers)
      auth-method: (eap-radius | pre-shared-key | pre-shared-key-xauth | rsa-signature | rsa-key | rsa-signature-hybrid ) # Default: pre-shared-key. IPsec authentication method ( one of eap-radius  pre-shared-key  pre-shared-key-xauth  rsa-key  rsa-signature  rsa-signature-hybrid )
      copy-from: 0 # Number of an identity to copy all settings from - not recommended for use because of unpredictable numbering
      key: (string) # Default: none Name of the key from key menu. Applicable if auth-method=rsa-key.
      my-id: (auto | fqdn | user-fqdn | key-id) # Default: auto. This parameter sets IKE ID to specified mode. It is possible to manually set two modes FQDN and USER_FQDN.
      policy-template-group: (none | string) # Default: none. must be in "groups". If generate-policy is enabled, responder checks against templates from the same group. If none of the templates match, Phase2 SA will not be established.
      remote-id: (string) # Undocumented. Might be a text value to match with remote id of the peer
      secret: (string) # Secret string (in case pre-shared key authentication is used). If it starts with '0x', it is parsed as a hexadecimal value
      xauth-password: (string) # initiator (client) XAuth password
      certificate: (string) # Name of a certificate listed in certificate table (signing packets; the certificate must have private key). Applicable if RSA signature authentication method (auth-method=rsa-signature) is used.
      generate-policy: (no | port-override | port-strict) # Default: no. Allow this peer to establish SA for non-existing policies. Such policies are created dynamically for the lifetime of SA. Automatic policies allows, for example, to create IPsec secured L2TP tunnels, or any other setup where remote peer's IP address is not known at the configuration time. no - do not generate policies. port-override -- generate policies and force policy to use any port (old behavior). port-strict -- use ports from peer's proposal, which should match peer's policy.
      mode-config: (none | request-only | string) # Default: none. Name of the mode config parameters from mode-config menu. When parameter is set mode-config is enabled. initiator peer on phase1 will send mode-config request and will set assigned IP address and DNS. responder will assign ip address if address-pool is specified, will send also DNS server addresses and split-include subnets (if defined).
      notrack-chain: (string) # Default: none. Adds raw firewall rules matching ipsec policy to specified chain.
      remote-certificate: (string) # Default: none. Name of a certificate (listed in certificate table) for authenticating the remote side (validating packets; no private key required). Applicable if RSA signature authentication method is used. If remote-certificate is not specified then received certificate from remote peer is used and checked against CA in certificate store. Proper CA must be imported in certificate store.
      remote-key: (string) # Default: none. Name of the public key from key menu. Applicable if auth-method=rsa-key.
      xauth-login: (string) # Default: none. 	initiator (client) XAuth username
  mode_configs: # IPsec mode configs list
    - name: (string) # Required. name of config
      responder: (bool) # Default: false. peer shoud request or send the config
      src-address-list: (string) # Default: none. address list name to be added to srcnat chain for initiator
  peers: # list of IPsec peers
    - name:  (string) # Required. Name of peer, DNS or IP
      comment: (string) # Required. Descriptiove comment
      disabled: (yes|no) # Required. if the peer disabled
      copy-from: (number) # Number of a peer to copy from. Not recommended for usage because of unpredictable order
      exchange-mode: (aggressive | base | main | main-l2tp | ike2) # Default: main.	Different ISAKMP phase 1 exchange modes according to RFC 2408. Do not use other modes then main unless you know what you are doing. main-l2tp mode relaxes rfc2409 section 5.4, to allow pre-shared-key authentication in main mode. ike2 mode enables Ikev2 RFC 7296. Parameters that are ignored by Ikev2 proposal-check, compatibility-options, lifebytes, dpd-maximum-failures, nat-traversal.
      local-address: (IP/IPv6 Address) # Default: none. Routers local address on which Phase 1 should be bounded to.
      passive: (yes|no) # Default: no. When passive mode is enabled will wait for remote peer to initiate IKE connection. Enabled passive mode also indicates that peer is xauth responder, and disabled passive mode - xauth initiator. When passive mode is disabled peer will try to establish not only phase1, but also phase2 automatically, if policies are configured or created during phase1.
      port: (integer:0..65535) # Default: 500. Communication port used (when router is initiator) to connect to remote peer in cases if remote peer uses non-default port.
      profile: (string) # Default: default. Name of the profile template that will be used during IKE negotiation.
      send-initial-contact: (yes | no) # Default: yes. Specifies whether to send "initial contact" IKE packet or wait for remote side, this packet should trigger removal of old peer SAs for current source address. Usually in road warrior setups clients are initiators and this parameter should be set to no. Initial contact is not sent if modecfg or xauth is enabled for ikev1.
  policies: # List of traffic protection policies
    - comment: (string) # Short description of the policy.
      action: (discard | encrypt | none) # Default: encrypt. Specifies what to do with packet matched by the policy. none - pass the packet unchanged. discard - drop the packet. encrypt - apply transformations specified in this policy and it's SA.
      disabled: (yes|no) # Default: no.	Whether policy is used to match packets.
      group: (string) # Default: default.	Name of the policy-template-group to which this template is assigned.
      place-before: (number) # Default: none. Number of a policy to place the policy before
      sa-dst-address: (ip/ipv6 address) # Default: ::. SA source IP/IPv6 address (local peer).
      src-port: (any | integer:0..65535) # Default: any.	Source port to be matched in packets. If set to any all ports will be matched.
      dst-address: (IP/IPv6 prefix) # Default: 0.0.0.0/32.	Destination address to be matched in packets.
      ipsec-protocols: (ah | esp) # Default: esp.	Specifies what combination of Authentication Header and Encapsulating Security Payload protocols you want to apply to matched traffic.
      proposal: (string) # Default: default. Name of the proposal template that will be sent by IKE daemon to establish SAs for this policy.
      sa-src-address: (ip/ipv6 address) # Default: ::. SA source IP/IPv6 address (local peer).
      template: (yes | no) # Default: no. Creates a template and assigns it to specified policy group. Following parameters are used by template: group - name of the policy group to which this template is assigned; src-address, dst-address - Requested subnet must match in both directions(for example 0.0.0.0/0 to allow all); protocol - protocol to match, if set to all, then any protocol is accepted; proposal - SA parameters used for this template; level - useful when unique is required in setups with multiple clients behind NAT.
      copy-from: (number) # Number of item to copy settings from. Not recommended for usage because of unpredictable order.
      dst-port: (integer:0..65535 | any) # Default: any. Destination port to be matched in packets. If set to any all ports will be matched.
      level: (require | unique | use) # Default: require. Specifies what to do if some of the SAs for this policy cannot be found: use - skip this transform, do not drop packet and do not acquire SA from IKE daemon; require - drop packet and acquire SA; unique - drop packet and acquire a unique SA that is only used with this particular policy. It is used in setups where multiple clients can sit behind one public IP address (clients behind NAT).
      protocol:  (all | egp | ggp| icmp | igmp | ...) # Default: all. IP packet protocol to match.
      src-address: (ip/ipv6 prefix) # Default: 0.0.0.0/32. Source address to be matched in packets.
      tunnel: (yes | no) # Default: no. Specifies whether to use tunnel mode.
  profiles:
    - name: (string) # Required. Name of a profile
      copy-from: (number) # Number of item to copy settings from. Not recommended for usage because of unpredictable order.
      dpd-interval: (time | disable-dpd) # Default: 2m. Dead peer detection interval. If set to disable-dpd, dead peer detection will not be used.
      enc-algorithm: (3des | aes-128 | aes-192 | aes-256 | blowfish | camellia-128 | camellia-192 | camellia-256 | des) # Default: aes-128. List of encryption algorithms separated by comma that will be used by the peer.
      lifebytes: (Integer: 0..4294967295) # Default: 0. Phase 1 lifebytes is used only as administrative value which is added to proposal. Used in cases if remote peer requires specific lifebytes value to establish phase 1.
      nat-traversal: (yes | no) # Default: yes. Use Linux NAT-T mechanism to solve IPsec incompatibility with NAT routers inbetween IPsec peers. This can only be used with ESP protocol (AH is not supported by design, as it signs the complete packet, including IP header, which is changed by NAT, rendering AH signature invalid). The method encapsulates IPsec ESP traffic into UDP streams in order to overcome some minor issues that made ESP incompatible with NAT.
      dh-group: (ec2n155 | ec2n185 | modp1024 | modp1536 | modp2048 | modp3072 | modp4096 | modp6144 | modp768) # Default: modp1024. 	Diffie-Hellman group (cipher strength)
      dpd-maximum-failures: (integer: 1..100) # Default: 5. Maximum count of failures until peer is considered to be dead. Applicable if DPD is enabled.
      hash-algorithm: (md5 | sha1 | sha256 | sha512) # Default: sha1. Hashing algorithm. SHA (Secure Hash Algorithm) is stronger, but slower. MD5 uses 128-bit key, sha1-160bit key.
      lifetime: (time) # Default: 1d. Phase 1 lifetime: specifies how long the SA will be valid.
      proposal-check: (claim | exact | obey | strict) # Default: obey) 	Phase 2 lifetime check logic: claim - take shortest of proposed and configured lifetimes and notify initiator about it; exact - require lifetimes to be the same; obey - accept whatever is sent by an initiator; strict - if proposed lifetime is longer than the default then reject proposal otherwise accept proposed lifetime.
  proposals:
    - name: (string) # Required. Text name of a proposal
      comment: (string) # Required. Text comment of a proposal
      disabled: (yes|no) # Required. If a proposal is disabled
      auth-algorithms: (md5|null|sha1|sha256|sha512) # Default: sha1. List, separated by comma. Allowed algorithms for authorization. SHA (Secure Hash Algorithm) is stronger, but slower. MD5 uses 128-bit key, sha1-160bit key.
      copy-from: (number) # Number of an item to copy values from. Not recommended for usage because of unpredictable order.
      enc-algorithms: (null|des|3des|aes-128-cbc|aes-128-cbc|aes-128gcm|aes-192-cbc|aes-192-ctr|aes-192-gcm|aes-256-cbc|aes-256-ctr|aes-256-gcm|blowfish|camellia-128|camellia-192|camellia-256|twofish) # Default: aes-256-cbc,aes-192-cbc,aes-128-cbc. Allowed algorithms and key lengths to use for SAs. List, separated by comma.
      lifetime: (time) # Default: 30m. How long to use SA before throwing it out.
      pfs-group: (ec2n155 | ec2n185 | ecp256 | ecp384 | ecp521 | modp768 | modp1024 | modp1536 | modp2048 | modp3072 | modp4096 | modp6144 | modp8192 | none) # Default: modp1024.	Diffie-Helman group used for Perfect Forward Secrecy.
```
================================================

File: LICENSE
================================================
BSD 3-Clause License
Copyright (c) 2019, Dmitriy Ermakov
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
================================================

File: README.md
================================================
# Mikrotik IPsec configuration role.
It allows to configure IPsec on Mikrotik RouterOS.
Example usage is in docs/
Be careful: the role deletes all your old configuration.
Warning: the role is intended to use with an old format of IPsec configuration (before version 6.44beta61).
The role will not work with older RouterOS versions.
================================================

File: main.yml
================================================
---
  - name: Generate ipsec template ipsec-{{inventory_hostname}}.rsc to import ipsec
    template: src=ipsec_full.rsc.j2 dest={{role_path}}/files/tmp/ipsec-{{inventory_hostname}}.rsc
    delegate_to: localhost
    tags: ["role::mikrotik::IPv4_IPsec", "role::mikrotik::IPv4_IPsec::generate_script_local"]
  - name: Send ipsec-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/ipsec-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/ipsec-{{inventory_hostname}}.rsc
    delegate_to: localhost
    tags: ["role::mikrotik::IPv4_IPsec"]
  - name: Delete temporary ipsec-{{inventory_hostname}}.rsc file
    file: path={{role_path}}/files/tmp/ipsec-{{inventory_hostname}}.rsc state=absent
    delegate_to: localhost
    tags: ["role::mikrotik::IPv4_IPsec"]
  - name: Run ipsec-{{inventory_hostname}}.rsc on router
    routeros_command:
      commands:  "/import ipsec-{{inventory_hostname}}.rsc"
    register: mikrotik_ipsec_out
    failed_when: mikrotik_ipsec_out['stdout_lines'][0][-1] is not search('Script file loaded and executed successfully')
    tags: ["role::mikrotik::IPv4_IPsec"]
  - name: Remove ipsec-{{inventory_hostname}}.rsc from router
    routeros_command:
      commands:  "/file remove ipsec-{{inventory_hostname}}.rsc"
    register: mikrotik_ipsec_out_delete_out
    failed_when: mikrotik_ipsec_out_delete_out['stdout_lines'][0][-1] is search('no such item')
    when: mikrotik_ipsec.delete_ipsec_on_target_router
    tags: ["role::mikrotik::IPv4_IPsec"]
================================================

File: delete_mode_configs.rsc.j2
================================================
{% if mikrotik_ipsec['delete_all_mode_configs'] == true %}
# Delete ALL policies
/ip ipsec mode-config remove [/ip ipsec mode-config find where !(default=yes)]
{% endif %}
{% if mikrotik_ipsec['mode_configs'][0] is defined %}
# Delete not defined mode configs
/ip ipsec mode-config remove [/ip ipsec mode-config find where !(default=yes) and !( \
{% for m_config in mikrotik_ipsec['mode_configs'] %}
{% if not loop.first %} or {% endif %} ( name="Ansible managed: [{{ m_config['name'] }}]") \
{% endfor %}
)]
# End delete not defined mode configs
{% endif %}
================================================

File: mode_configs.rsc.j2
================================================
{% if mikrotik_ipsec['mode_configs'][0] is defined %}
# Сreate mode configs
{% for m_config in mikrotik_ipsec['mode_configs'] %}
:if ([/ip ipsec mode-config find name="Ansible managed: [{{ m_config['name'] }}]" ] = "" ) do={
  # Create a new mode_config {{ m_config['name'] }}
  /ip ipsec mode-config add name="Ansible managed: [{{ m_config['name'] }}]"
}
# Set parameters for mode config
/ip ipsec mode-config set [/ip ipsec mode-config find name="Ansible managed: [{{ m_config['name'] }}]" ] \
{% if m_config['responder'] is defined %}responder="{{ m_config['responder'] | bool | ternary('yes', 'no') }}" {% endif %}
{% if m_config['src-address-list'] is defined %} src-address-list="{{ m_config['src-address-list'] }}" {% endif %}
# End set parameters
{% endfor %}
# End delete not defined mode configs
{% endif %}
================================================
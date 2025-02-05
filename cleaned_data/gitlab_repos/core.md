# Repository Information
Name: core

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
	url = https://gitlab.com/mikrotik_swos/core.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: .gitlab-ci.yml
================================================
---
image: cytopia/ansible:latest-tools
before_script:
  - pip3 install --ignore-installed yq yamllint==1.32.0 ansible-lint==6.17.1
  - pip3 install --ignore-installed ansible-core==2.15.0
  - python3 --version
  - pip3 --version
  - ansible --version
  - ansible-lint --version
  - yamllint --version
workflow:  # run the pipeline only on MRs and default branch
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
stages:
  - build
  # - linters
  - galaxy
  - release
prepare:
  stage: build
  script:
    - C2_VERSION=$(yq '.version' galaxy.yml | sed 's/"//g')
    - C2_NAME=$(yq '.name' galaxy.yml | sed 's/"//g')
    - C2_NAMESPACE=$(yq '.namespace' galaxy.yml | sed 's/"//g')
    - echo "C2_VERSION=$C2_VERSION" >> variables.env
    - echo "C2_NAME=$C2_NAME" >> variables.env
    - echo "C2_NAMESPACE=$C2_NAMESPACE" >> variables.env
  artifacts:
    reports:
      dotenv: variables.env
build:
  stage: build
  needs: [prepare]
  script:
    # - cat README-GALAXY.md > README.md  # readme property in galaxy.yml is ignored by galaxy website
    - ansible-galaxy collection build . --force
  artifacts:
    paths:
      - $C2_NAMESPACE-$C2_NAME-$C2_VERSION.tar.gz
# yamllint:
#   stage: linters
#   script:
#     - yamllint -c .yamllint .
# ansible-lint:
#   stage: linters
#   needs: [prepare, build]
#   script:
#     - ansible-galaxy collection install $C2_NAMESPACE-$C2_NAME-$C2_VERSION.tar.gz
#     - ansible-lint -c .ansible-lint
publish:
  stage: galaxy
  needs: [prepare, build]
  script:
    # - cat README-GALAXY.md > README.md  # readme property in galaxy.yml is ignored by galaxy website
    - ansible-galaxy collection build . --force
    - ansible-galaxy collection publish $C2_NAMESPACE-$C2_NAME-$C2_VERSION.tar.gz --token $GALAXY_API_KEY
  when: manual
gitlab-release:
  stage: release
  image: registry.gitlab.com/gitlab-org/release-cli:latest
  needs: [publish, prepare]
  before_script: []
  script:
    - echo "Create release for $C2_NAMESPACE.$C2_NAME $C2_VERSION"
  release:
    name: $C2_NAMESPACE.$C2_NAME $C2_VERSION
    description: './CHANGELOG.md'
    tag_name: $C2_VERSION
    ref: $CI_COMMIT_SHA
    assets:
      links:
        - name: $C2_NAMESPACE.$C2_NAME
          url: https://galaxy.ansible.com/$C2_NAMESPACE/$C2_NAME
================================================

File: galaxy.yml
================================================
### REQUIRED
# The namespace of the collection. This can be a company/brand/organization or product namespace under which all
# content lives. May only contain alphanumeric lowercase characters and underscores. Namespaces cannot start with
# underscores or numbers and cannot contain consecutive underscores
namespace: mikrotik_swos
# The name of the collection. Has the same character restrictions as 'namespace'
name: core
# The version of the collection. Must be compatible with semantic versioning
version: 1.0.0-alpha.1
# The path to the Markdown (.md) readme file. This path is relative to the root of the collection
readme: README.md
# A list of the collection's content authors. Can be just the name or in the format 'Full Name <email> (url)
# @nicks:irc/im.site#channel'
authors:
- Robert Holstein
### OPTIONAL but strongly recommended
# A short summary description of the collection
description: Configure Mikrotik SWOS switches
# Either a single license or a list of licenses for content inside of a collection. Ansible Galaxy currently only
# accepts L(SPDX,https://spdx.org/licenses/) licenses. This key is mutually exclusive with 'license_file'
license:
- GPL-2.0-or-later
# The path to the license file for the collection. This path is relative to the root of the collection. This key is
# mutually exclusive with 'license'
license_file: ''
# A list of tags you want to associate with the collection for indexing/searching. A tag name has the same character
# requirements as 'namespace' and 'name'
tags: ['Mikrotik', 'SWOS']
# Collections that this collection requires to be installed for it to be usable. The key of the dict is the
# collection label 'namespace.name'. The value is a version range
# L(specifiers,https://python-semanticversion.readthedocs.io/en/latest/#requirement-specification). Multiple version
# range specifiers can be set and are separated by ','
dependencies: {}
# The URL of the originating SCM repository
repository: https://gitlab.com/holstein1/mikrotik_swos
# The URL to any online docs
documentation: https://gitlab.com/holstein1/mikrotik_swos
# The URL to the homepage of the collection/project
homepage: https://gitlab.com/holstein1/mikrotik_swos
# The URL to the collection issue tracker
issues: https://gitlab.com/holstein1/mikrotik_swos
# A list of file glob-like patterns used to filter any files or directories that should not be included in the build
# artifact. A pattern is matched from the relative path of the file or directory of the collection directory. This
# uses 'fnmatch' to match the files or directories. Some directories and files like 'galaxy.yml', '*.pyc', '*.retry',
# and '.git' are always filtered. Mutually exclusive with 'manifest'
build_ignore:
  - .github
  - .gitignore
  - .travis.yml
  - '*.tar.gz'
  - changelogs
  - examples
  - misc
  - setup.cfg
  - .gitlab-ci.yml
# A dict controlling use of manifest directives used in building the collection artifact. The key 'directives' is a
# list of MANIFEST.in style
# L(directives,https://packaging.python.org/en/latest/guides/using-manifest-in/#manifest-in-commands). The key
# 'omit_default_directives' is a boolean that controls whether the default directives are used. Mutually exclusive
# with 'build_ignore'
# manifest: null
================================================

File: runtime.yml
================================================
---
# Collections must specify a minimum required ansible version to upload
# to galaxy
# requires_ansible: '>=2.9.10'
# Content that Ansible needs to load from another location or that has
# been deprecated/removed
# plugin_routing:
#   action:
#     redirected_plugin_name:
#       redirect: ns.col.new_location
#     deprecated_plugin_name:
#       deprecation:
#         removal_version: "4.0.0"
#         warning_text: |
#           See the porting guide on how to update your playbook to
#           use ns.col.another_plugin instead.
#     removed_plugin_name:
#       tombstone:
#         removal_version: "2.0.0"
#         warning_text: |
#           See the porting guide on how to update your playbook to
#           use ns.col.another_plugin instead.
#   become:
#   cache:
#   callback:
#   cliconf:
#   connection:
#   doc_fragments:
#   filter:
#   httpapi:
#   inventory:
#   lookup:
#   module_utils:
#   modules:
#   netconf:
#   shell:
#   strategy:
#   terminal:
#   test:
#   vars:
# Python import statements that Ansible needs to load from another location
# import_redirection:
#   ansible_collections.ns.col.plugins.module_utils.old_location:
#     redirect: ansible_collections.ns.col.plugins.module_utils.new_location
# Groups of actions/modules that take a common set of options
# action_groups:
#   group_name:
#     - module1
#     - module2
================================================

File: mikrotik_swos_port.py
================================================
#!/usr/bin/python
DOCUMENTATION = '''
---
module: mikrotik_swos_port
short_description: Manage port settings on MikroTik SwOS devices
description:
    - This module allows you to enable or disable individual ports and configure their settings on MikroTik SwOS devices.
version_added: "1.0"
author: Your Name <youremail@example.com>
options:
    hostname:
        description:
            - The hostname or IP address of the MikroTik SwOS device.
        required: true
        type: str
    username:
        description:
            - The username for authentication.
        required: true
        type: str
    password:
        description:
            - The password for authentication.
        required: true
        type: str
        no_log: true
    port_id:
        description:
            - The ID of the port to configure (1-based index).
        required: true
        type: int
    state:
        description:
            - Desired state of the port.
        required: true
        type: str
        choices: ['enabled', 'disabled']
    name:
        description:
            - The name of the port.
        type: str
    autoneg:
        description:
            - Whether auto-negotiation is enabled on the port.
        type: bool
    duplex:
        description:
            - The duplex mode of the port.
        type: bool
    tx_flow_control:
        description:
            - Enable or disable TX flow control.
        type: bool
    rx_flow_control:
        description:
            - Enable or disable RX flow control.
        type: bool
    speed:
        description:
            - The speed of the port in Mbps.
            - Choices: 10, 100, 1000, 2500, 10000
        type: int
    sfp_rate:
        description:
            - The SFP rate for the port.
            - Choices: 'low', 'high'
        type: str
        choices: ['low', 'high']
'''
EXAMPLES = '''
- name: Enable and configure port 1 on MikroTik Switch
  mikrotik_swos_port:
    hostname: 192.168.88.1
    username: admin
    password: password
    port_id: 1
    state: enabled
    name: "Uplink1"
    autoneg: true
    duplex: true
    tx_flow_control: true
    rx_flow_control: true
    speed: 1000
    sfp_rate: high
- name: Disable port 2 on MikroTik Switch
  mikrotik_swos_port:
    hostname: 192.168.88.1
    username: admin
    password: password
    port_id: 2
    state: disabled
'''
RETURN = '''
changed:
    description: Whether the port settings were changed.
    type: bool
    returned: always
message:
    description: Details of the changes made or would be made.
    type: str
    returned: always
'''
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_port import Mikrotik_Port, PORT_SPEED_MB, PORT_SFP_RATE
def run_module():
    # Define available arguments/parameters
    module_args = dict(
        hostname=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        port_id=dict(type='int', required=True),
        state=dict(type='str', required=True, choices=['enabled', 'disabled']),
        name=dict(type='str'),
        autoneg=dict(type='bool'),
        duplex=dict(type='bool'),
        tx_flow_control=dict(type='bool'),
        rx_flow_control=dict(type='bool'),
        speed=dict(type='int', choices=[10, 100, 1000, 2500, 10000]),
        sfp_rate=dict(type='str', choices=['low', 'high']),
    )
    # Initialize the result dictionary
    result = dict(
        changed=False,
        message=""
    )
    # Create the Ansible module
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    # Extract parameters
    hostname = module.params['hostname']
    username = module.params['username']
    password = module.params['password']
    port_id = module.params['port_id']
    desired_state = module.params['state']
    desired_settings = {
        'name': module.params.get('name'),
        'autoneg': module.params.get('autoneg'),
        'duplex': module.params.get('duplex'),
        'tx_flow_control': module.params.get('tx_flow_control'),
        'rx_flow_control': module.params.get('rx_flow_control'),
        'speed': module.params.get('speed'),
        'sfp_rate': module.params.get('sfp_rate')
    }
    # Determine the enabled flag based on state
    if desired_state == 'enabled':
        desired_enabled = 1
    else:
        desired_enabled = 0
    try:
        # Instantiate the Mikrotik_Port class
        port = Mikrotik_Port(hostname, username, password)
        # Validate port_id
        if port_id < 1 or port_id > port.port_count:
            module.fail_json(msg=f"port_id {port_id} is out of range. The device has {port.port_count} ports.", **result)
        # Collect any changes
        changes = []
        # Current settings
        current_enabled = port.parsed_data['enabled'][port_id - 1]
        current_name = port.parsed_data['name'][port_id - 1]
        current_autoneg = port.parsed_data['autoneg'][port_id - 1]
        current_duplex = port.parsed_data['duplex'][port_id - 1]
        current_tx_flow = port.parsed_data['tx_flow_control'][port_id - 1]
        current_rx_flow = port.parsed_data['rx_flow_control'][port_id - 1]
        current_speed = port.parsed_data['speed'][port_id - 1]
        current_sfp_rate = port.parsed_data.get('sfp_rate', [None]*port.port_count)[port_id -1 ] if port.version >=2.16 else None
        # Compare desired state with current state
        if current_enabled != desired_enabled:
            changes.append(f"state: {'enabled' if desired_enabled else 'disabled'}")
        # Compare other settings only if they are provided
        if desired_settings['name'] is not None and desired_settings['name'] != current_name:
            changes.append(f"name: '{desired_settings['name']}'")
        if desired_settings['autoneg'] is not None and desired_settings['autoneg'] != bool(current_autoneg):
            changes.append(f"autoneg: {desired_settings['autoneg']}")
        if desired_settings['duplex'] is not None and desired_settings['duplex'] != bool(current_duplex):
            changes.append(f"duplex: {desired_settings['duplex']}")
        if desired_settings['tx_flow_control'] is not None and desired_settings['tx_flow_control'] != bool(current_tx_flow):
            changes.append(f"tx_flow_control: {desired_settings['tx_flow_control']}")
        if desired_settings['rx_flow_control'] is not None and desired_settings['rx_flow_control'] != bool(current_rx_flow):
            changes.append(f"rx_flow_control: {desired_settings['rx_flow_control']}")
        if desired_settings['speed'] is not None:
            # Translate desired speed to hex
            desired_speed_hex = PORT_SPEED_MB.get(str(desired_settings['speed']))
            if desired_speed_hex is None:
                module.fail_json(msg=f"Invalid speed value: {desired_settings['speed']}.", **result)
            if desired_speed_hex != current_speed:
                changes.append(f"speed: {desired_settings['speed']}")
        if port.version >= 2.16 and desired_settings['sfp_rate'] is not None:
            desired_sfp_rate_hex = PORT_SFP_RATE.get(desired_settings['sfp_rate'])
            if desired_sfp_rate_hex is None:
                module.fail_json(msg=f"Invalid sfp_rate value: {desired_settings['sfp_rate']}.", **result)
            if desired_sfp_rate_hex != current_sfp_rate:
                changes.append(f"sfp_rate: '{desired_settings['sfp_rate']}'")
        if module.check_mode:
            if changes:
                result['changed'] = True
                result['message'] = f"Port {port_id} would be updated with the following changes: {', '.join(changes)}."
            else:
                result['message'] = f"Port {port_id} is already in the desired state and settings."
            module.exit_json(**result)
        # Proceed to configure only if there are changes
        if changes:
            # Configure the specified port
            port.configure(
                port_id,
                name=desired_settings['name'],
                enabled=desired_enabled,
                autoneg=desired_settings['autoneg'],
                duplex=desired_settings['duplex'],
                tx_flow_control=desired_settings['tx_flow_control'],
                rx_flow_control=desired_settings['rx_flow_control'],
                speed=desired_settings['speed'],
                sfp_rate=desired_settings['sfp_rate']
            )
            # Save the changes
            if port.save():
                result['changed'] = True
                result['message'] = f"Port {port_id} has been {'enabled' if desired_enabled else 'disabled'} and settings updated successfully."
            else:
                result['message'] = f"Port {port_id} settings are already up to date."
        else:
            result['message'] = f"Port {port_id} is already in the desired state and settings."
    except Exception as e:
        module.fail_json(msg=f"Failed to configure port: {e}", **result)
    # Exit the module and return the result
    module.exit_json(**result)
def main():
    run_module()
if __name__ == '__main__':
    main()
================================================

File: mikrotik_swos_port_isolation.py
================================================
#!/usr/bin/python
DOCUMENTATION = '''
---
module: mikrotik_swos_port_isolation
short_description: Manage port isolation settings on MikroTik SwOS devices
description:
    - This module allows you to configure port isolation on MikroTik SwOS devices.
    - It isolates a specific port from a list of other ports, enhancing network security.
options:
    hostname:
        description:
            - The hostname or IP address of the MikroTik SwOS device.
        required: true
    username:
        description:
            - The username for authentication.
        required: true
    password:
        description:
            - The password for authentication.
        required: true
        no_log: true
    port_id:
        description:
            - The ID of the port to configure isolation for.
        type: int
        required: true
    isolated_ports:
        description:
            - List of port IDs to isolate from.
        type: list
        elements: int
        required: false
    state:
        description:
            - Whether the settings should be present.
        default: present
        choices: [ 'present' ]
'''
EXAMPLES = '''
- name: Isolate port 1 from ports 2 and 3 on MikroTik Switch
  mikrotik_swos_port_isolation:
    hostname: 192.168.88.1
    username: admin
    password: password
    port_id: 1
    isolated_ports: [2, 3]
    state: present
'''
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_port_isolation import Mikrotik_Forwarding
def run_module():
    module_args = dict(
        hostname=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        port_id=dict(type='int', required=True),
        isolated_ports=dict(
            type='list',
            elements='int',
            required=False,
            default=[]
        ),
        state=dict(type='str', default='present', choices=['present'])
    )
    result = dict(
        changed=False,
        message=''
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    if module.check_mode:
        module.exit_json(**result)
    # Extract parameters
    hostname = module.params['hostname']
    username = module.params['username']
    password = module.params['password']
    port_id = module.params['port_id']
    isolated_ports = module.params['isolated_ports']
    state = module.params['state']
    # Instantiate the Mikrotik_Forwarding class
    try:
        forwarding = Mikrotik_Forwarding(hostname, username, password)
    except Exception as e:
        module.fail_json(msg=f"Failed to connect to the device: {e}")
    try:
        settings_changed = False
        # Configure Port Isolation
        if state == 'present':
            isolation_result = forwarding.port_isolation(port_id, isolated_ports)
            if isolation_result:
                settings_changed = True
        if settings_changed:
            saved = forwarding.save()
            if saved:
                result['changed'] = True
                result['message'] = "Port isolation settings updated successfully."
            else:
                result['message'] = "Settings were changed locally but not saved."
        else:
            result['message'] = "No changes were made; settings are already up to date."
    except Exception as e:
        module.fail_json(msg=f"Failed to apply settings: {e}")
    module.exit_json(**result)
def main():
    run_module()
if __name__ == '__main__':
    main()
================================================

File: mikrotik_swos_rstp.py
================================================
#!/usr/bin/python
DOCUMENTATION = '''
---
module: mikrotik_swos_rstp
short_description: Manage RSTP settings on MikroTik SwOS devices on a per-port basis
description:
    - This module allows you to enable or disable RSTP (Rapid Spanning Tree Protocol) on individual ports of MikroTik SwOS devices.
version_added: "1.0"
author:
    - Your Name (@yourhandle)
options:
    hostname:
        description:
            - The hostname or IP address of the MikroTik SwOS device.
        required: true
        type: str
    username:
        description:
            - The username for authentication.
        required: true
        type: str
    password:
        description:
            - The password for authentication.
        required: true
        type: str
        no_log: true
    port:
        description:
            - The port number to manage RSTP settings on.
        required: true
        type: int
    state:
        description:
            - The desired state of RSTP on the specified port.
        required: true
        type: str
        choices: [ present, absent ]
        default: present
'''
EXAMPLES = '''
- name: Enable RSTP on port 1
  mikrotik_swos_rstp:
    hostname: 192.168.88.1
    username: admin
    password: password
    port: 1
    state: present
- name: Disable RSTP on port 2
  mikrotik_swos_rstp:
    hostname: 192.168.88.1
    username: admin
    password: password
    port: 2
    state: absent
'''
RETURN = '''
changed:
    description: Whether the RSTP settings were changed.
    type: bool
    returned: always
message:
    description: Message indicating the result of the module execution.
    type: str
    returned: always
'''
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_rstp import Mikrotik_Rstp
def run_module():
    # Define the available arguments/parameters a user can pass to the module
    module_args = dict(
        hostname=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        port_id=dict(type='int', required=True),
        state=dict(type='str', choices=['enabled', 'disabled'], default='enabled'),
    )
    # Seed the result dictionary
    result = dict(
        changed=False,
        message=''
    )
    # The AnsibleModule object
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    # If in check mode, exit without making changes
    if module.check_mode:
        module.exit_json(**result)
    # Extract module parameters
    hostname = module.params['hostname']
    username = module.params['username']
    password = module.params['password']
    port = module.params['port_id']
    state = module.params['state']
    try:
        # Instantiate the Mikrotik_Rstp class
        rstp = Mikrotik_Rstp(hostname, username, password)
        # Determine desired state
        desired_state = True if state == 'enabled' else False
        # Apply RSTP setting to the specified port
        port_changed = rstp.on_port(port, desired_state)
        # Save changes if any
        if port_changed:
            if rstp.save():
                result['changed'] = True
                state_str = "enabled" if desired_state else "disabled"
                result['message'] = f"RSTP successfully {state_str} on port {port}."
            else:
                result['message'] = "RSTP settings were modified but no changes were applied."
        else:
            state_str = "enabled" if desired_state else "disabled"
            result['message'] = f"RSTP on port {port} is already {state_str}."
    except Exception as e:
        module.fail_json(msg=f"Failed to configure RSTP settings: {e}", **result)
    module.exit_json(**result)
def main():
    run_module()
if __name__ == '__main__':
    main()
================================================

File: mikrotik_swos_snmp.py
================================================
#!/usr/bin/python
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
---
module: mikrotik_swos_snmp
short_description: Manage SNMP settings on MikroTik SwOS devices
description:
    - This module allows you to enable or disable SNMP and configure its community, contact information, and location on MikroTik SwOS devices.
version_added: "1.0"
author: Your Name <youremail@example.com>
options:
    hostname:
        description:
            - The hostname or IP address of the MikroTik SwOS device.
        required: true
        type: str
    username:
        description:
            - The username for authentication.
        required: true
        type: str
    password:
        description:
            - The password for authentication.
        required: true
        type: str
        no_log: true
    state:
        description:
            - Desired state of SNMP.
        required: true
        type: str
        choices: ['enabled', 'disabled']
    community:
        description:
            - The SNMP community string.
        type: str
    contact_info:
        description:
            - Contact information for SNMP.
        type: str
    location:
        description:
            - Location information for SNMP.
        type: str
'''
EXAMPLES = '''
- name: Enable SNMP with specific settings on MikroTik Switch
  mikrotik_swos_snmp:
    hostname: 192.168.88.1
    username: admin
    password: password
    state: enabled
    community: "public"
    contact_info: "admin@example.com"
    location: "Data Center"
  register: snmp_result
- name: Disable SNMP on MikroTik Switch
  mikrotik_swos_snmp:
    hostname: 192.168.88.1
    username: admin
    password: password
    state: disabled
  register: snmp_result
- name: Check SNMP settings without applying changes
  mikrotik_snmp:
    hostname: 192.168.88.1
    username: admin
    password: password
    state: enabled
    community: "public"
    contact_info: "admin@example.com"
    location: "Data Center"
  check_mode: yes
  register: snmp_result
'''
RETURN = '''
changed:
    description: Whether the SNMP settings were changed.
    type: bool
    returned: always
message:
    description: Details of the changes made.
    type: str
    returned: always
'''
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_snmp import Mikrotik_Snmp
def run_module():
    # Define available arguments/parameters
    module_args = dict(
        hostname=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        state=dict(type='str', required=True, choices=['enabled', 'disabled']),
        community=dict(type='str'),
        contact_info=dict(type='str'),
        location=dict(type='str'),
    )
    # Initialize the result dictionary
    result = dict(
        changed=False,
        message=""
    )
    # Create the Ansible module
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[
            ['state', 'enabled', ['community', 'contact_info', 'location']],
        ]
    )
    # Extract parameters
    hostname = module.params['hostname']
    username = module.params['username']
    password = module.params['password']
    state = module.params['state']
    community = module.params.get('community')
    contact_info = module.params.get('contact_info')
    location = module.params.get('location')
    try:
        # Instantiate the Mikrotik_Snmp class
        snmp = Mikrotik_Snmp(hostname, username, password)
        # Load current SNMP settings
        snmp._load_tab_data()
        # Determine desired 'enable' flag based on 'state'
        desired_enable = True if state == 'enabled' else False
        # Prepare desired settings
        desired_settings = {'enable': desired_enable}
        if state == 'enabled':
            desired_settings['community'] = community
            desired_settings['contact_info'] = contact_info
            desired_settings['location'] = location
        # Validate required parameters when enabling SNMP
        if state == 'enabled':
            missing_fields = []
            if not community:
                missing_fields.append('community')
            if not contact_info:
                missing_fields.append('contact_info')
            if not location:
                missing_fields.append('location')
            if missing_fields:
                module.fail_json(msg=f"Missing required parameters when enabling SNMP: {', '.join(missing_fields)}", **result)
        # In check mode, determine what would change
        if module.check_mode:
            changes = []
            if desired_settings['enable'] != snmp.data_enabled:
                changes.append(f"SNMP would be {'enabled' if desired_enable else 'disabled'}.")
            if state == 'enabled':
                if community and community != snmp.data_community:
                    changes.append("SNMP community would be updated.")
                if contact_info and contact_info != snmp.data_contact_info:
                    changes.append("SNMP contact info would be updated.")
                if location and location != snmp.data_location:
                    changes.append("SNMP location would be updated.")
            if changes:
                result['changed'] = True
                result['message'] = "SNMP settings would be updated: " + " ".join(changes)
            else:
                result['message'] = "SNMP settings are already up to date."
            module.exit_json(**result)
        # Prepare the parameters for setting
        set_params = {'enable': desired_enable}
        if state == 'enabled':
            set_params['community'] = community
            set_params['contact_info'] = contact_info
            set_params['location'] = location
        # Apply desired settings
        changes_made = snmp.set(**set_params)
        if changes_made:
            result['changed'] = True
            result['message'] = "SNMP settings have been updated successfully."
        else:
            result['message'] = "SNMP settings are already up to date."
    except Exception as e:
        module.fail_json(msg=f"Failed to configure SNMP settings: {e}", **result)
    # Exit the module and return the result
    module.exit_json(**result)
def main():
    run_module()
if __name__ == '__main__':
    main()
================================================

File: mikrotik_swos_system.py
================================================
#!/usr/bin/python
DOCUMENTATION = '''
---
module: mikrotik_swos_system
short_description: Manage system settings on MikroTik SwOS devices
description:
    - This module allows you to configure system settings on MikroTik SwOS devices.
options:
    hostname:
        description:
            - The hostname or IP address of the MikroTik SwOS device.
        required: true
    username:
        description:
            - The username for authentication.
        required: true
    password:
        description:
            - The password for authentication.
        required: true
    identity:
        description:
            - The identity/name of the device.
    allow_from_net4:
        description:
            - IPv4 network (in CIDR notation) from which management access is allowed.
    allow_from_vlan:
        description:
            - VLAN ID from which management access is allowed.
        type: int
    allow_from_port:
        description:
            - List of ports from which management access is allowed.
        type: list
        elements: int
    watchdog:
        description:
            - Enable or disable the watchdog.
        type: bool
    independant_vlan_lookup:
        description:
            - Enable or disable independent VLAN learning.
        type: bool
    igmp_snooping:
        description:
            - Enable or disable IGMP snooping.
        type: bool
    igmp_fast_leave:
        description:
            - List of ports with IGMP fast leave enabled.
        type: list
        elements: int
    igmp_querier:
        description:
            - Enable or disable IGMP querier.
        type: bool
    igmp_version:
        description:
            - IGMP version to use.
        choices: [ v2, v3 ]
        default: v3
    mikrotik_discovery_protocol:
        description:
            - Enable or disable the MikroTik Discovery Protocol.
        type: bool
    dhcp_trusted_port:
        description:
            - List of DHCP trusted ports.
        type: list
        elements: int
    dhcp_add_information_option:
        description:
            - Enable or disable DHCP Option 82.
        type: bool
    state:
        description:
            - Whether the settings should be present.
        default: present
        choices: [ present ]
'''
EXAMPLES = '''
- name: Configure system settings on MikroTik Switch
  mikrotik_swos_system:
    hostname: 192.168.88.1
    username: admin
    password: password
    identity: "Core Switch"
    allow_from_net4: "192.168.88.0/24"
    allow_from_vlan: 100
    allow_from_port: [1, 2, 3]
    watchdog: true
    independant_vlan_lookup: false
    igmp_snooping: true
    igmp_fast_leave: [4, 5]
    igmp_querier: true
    igmp_version: v3
    mikrotik_discovery_protocol: false
    dhcp_trusted_port: [6]
    dhcp_add_information_option: true
    state: present
'''
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_system import Mikrotik_System
def run_module():
    module_args = dict(
        hostname=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        identity=dict(type='str'),
        allow_from_net4=dict(type='str'),
        allow_from_vlan=dict(type='int'),
        allow_from_port=dict(type='list', elements='int'),
        watchdog=dict(type='bool'),
        independant_vlan_lookup=dict(type='bool'),
        igmp_snooping=dict(type='bool'),
        igmp_fast_leave=dict(type='list', elements='int'),
        igmp_querier=dict(type='bool'),
        igmp_version=dict(type='str', choices=['v2', 'v3'], default='v3'),
        mikrotik_discovery_protocol=dict(type='bool'),
        dhcp_trusted_port=dict(type='list', elements='int'),
        dhcp_add_information_option=dict(type='bool'),
        state=dict(type='str', default='present', choices=['present'])
    )
    result = dict(
        changed=False,
        message=''
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    if module.check_mode:
        module.exit_json(**result)
    # Instantiate the Mikrotik_System class
    try:
        system = Mikrotik_System(module.params['hostname'], module.params['username'], module.params['password'])
    except Exception as e:
        module.fail_json(msg=f"Failed to connect to the device: {e}")
    # Prepare the settings to apply
    settings = {
        "identity": module.params.get('identity'),
        "allow_from_net4": module.params.get('allow_from_net4'),
        "allow_from_vlan": module.params.get('allow_from_vlan'),
        "allow_from_port": module.params.get('allow_from_port'),
        "watchdog": module.params.get('watchdog'),
        "independant_vlan_lookup": module.params.get('independant_vlan_lookup'),
        "igmp_snooping": module.params.get('igmp_snooping'),
        "igmp_fast_leave": module.params.get('igmp_fast_leave'),
        "igmp_querier": module.params.get('igmp_querier'),
        "igmp_version": module.params.get('igmp_version'),
        "mikrotik_discovery_protocol": module.params.get('mikrotik_discovery_protocol'),
        "dhcp_trusted_port": module.params.get('dhcp_trusted_port'),
        "dhcp_add_information_option": module.params.get('dhcp_add_information_option')
    }
    # Apply the settings
    try:
        changed = system.set(**settings)
        if changed:
            result['changed'] = True
            result['message'] = "System settings updated successfully."
        else:
            result['message'] = "System settings are already up to date."
    except Exception as e:
        module.fail_json(msg=f"Failed to apply settings: {e}")
    module.exit_json(**result)
def main():
    run_module()
if __name__ == '__main__':
    main()
================================================

File: mikrotik_swos_vlan.py
================================================
#!/usr/bin/python
DOCUMENTATION = '''
---
module: mikrotik_swos_vlan
short_description: Manage VLAN settings on MikroTik SwOS devices for individual ports
description:
    - This module allows you to configure VLAN settings for a specific port on MikroTik SwOS devices.
options:
    hostname:
        description:
            - The hostname or IP address of the MikroTik SwOS device.
        required: true
    username:
        description:
            - The username for authentication.
        required: true
    password:
        description:
            - The password for authentication.
        required: true
        no_log: true
    port_id:
        description:
            - The ID of the port to configure VLAN settings for.
        type: int
        required: true
    mode:
        description:
            - VLAN mode.
        type: str
        choices: ['disabled', 'optional', 'enabled', 'strict']
        required: false
    receive_mode:
        description:
            - VLAN receive mode.
        type: str
        choices: ['any', 'only_tagged', 'only_untagged']
        required: false
    default_vlan_id:
        description:
            - Default VLAN ID.
        type: int
        required: false
    force_vlan_id:
        description:
            - Force VLAN ID usage.
        type: bool
        required: false
    state:
        description:
            - Whether the settings should be present.
        default: present
        choices: [ 'present' ]
'''
EXAMPLES = '''
- name: Configure VLAN settings for port 1 on MikroTik Switch
  mikrotik_swos_vlan:
    hostname: 192.168.88.1
    username: admin
    password: password
    port_id: 1
    mode: enabled
    receive_mode: only_tagged
    default_vlan_id: 100
    force_vlan_id: true
    state: present
'''
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_vlan import Mikrotik_VLAN_Config
def run_module():
    module_args = dict(
        hostname=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        port_id=dict(type='int', required=True),
        receive_mode=dict(type='str', choices=['any', 'only_tagged', 'only_untagged'], required=False),
        default_vlan_id=dict(type='int', required=False),
        force_vlan_id=dict(type='bool', required=False),
        state=dict(type='str', default='optional', choices=['disabled', 'optional', 'enabled', 'strict'],)
    )
    result = dict(
        changed=False,
        message=''
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    if module.check_mode:
        module.exit_json(**result)
    # Extract parameters
    hostname = module.params['hostname']
    username = module.params['username']
    password = module.params['password']
    port_id = module.params['port_id']
    mode = module.params.get('state')
    receive_mode = module.params.get('receive_mode')
    default_vlan_id = module.params.get('default_vlan_id')
    force_vlan_id = module.params.get('force_vlan_id')
    state = module.params['state']
    # Instantiate the Mikrotik_VLAN_Config class
    try:
        vlan_config = Mikrotik_VLAN_Config(hostname, username, password)
    except Exception as e:
        module.fail_json(msg=f"Failed to connect to the device: {e}")
    try:
        settings_changed = False
        # Configure VLAN Settings
        vlan_result = vlan_config.configure_vlan(
            port_id=port_id,
            mode=mode,
            receive_mode=receive_mode,
            default_vlan_id=default_vlan_id,
            force_vlan_id=force_vlan_id
        )
        if vlan_result:
            settings_changed = True
        if settings_changed:
            saved = vlan_config.save_changes()
            if saved:
                result['changed'] = True
                result['message'] = "VLAN settings updated successfully."
            else:
                result['message'] = "Settings were changed locally but not saved."
        else:
            result['message'] = "No changes were made; settings are already up to date."
    except Exception as e:
        module.fail_json(msg=f"Failed to apply settings: {e}")
    module.exit_json(**result)
def main():
    run_module()
if __name__ == '__main__':
    main()
================================================

File: mikrotik_swos_vlans.py
================================================
#!/usr/bin/python
DOCUMENTATION = '''
---
module: mikrotik_swos_vlans
short_description: Manage VLANs on MikroTik SwOS devices
description:
    - This module allows you to add, remove, and configure VLANs on MikroTik SwOS devices.
options:
    hostname:
        description:
            - The hostname or IP address of the MikroTik SwOS device.
        required: true
    username:
        description:
            - The username for authentication.
        required: true
    password:
        description:
            - The password for authentication.
        required: true
    vlan_id:
        description:
            - The VLAN ID to configure.
        required: true
    name:
        description:
            - The name of the VLAN.
    state:
        description:
            - Whether the VLAN should be present or absent.
        choices: [ present, absent ]
        default: present
    port_isolation:
        description:
            - Enable or disable port isolation for the VLAN.
        type: bool
    learning:
        description:
            - Enable or disable MAC address learning for the VLAN.
        type: bool
    mirror:
        description:
            - Enable or disable mirroring for the VLAN.
        type: bool
    igmp_snooping:
        description:
            - Enable or disable IGMP snooping for the VLAN.
        type: bool
    member_ports:
        description:
            - List of port numbers to be added as members of the VLAN.
        type: list
        elements: int
'''
EXAMPLES = '''
- name: Add VLAN 100
  mikrotik_swos_vlans:
    hostname: 192.168.1.1
    username: admin
    password: password
    vlan_id: 100
    name: Management
    state: present
    port_isolation: true
    learning: true
    member_ports: [1, 2, 3]
- name: Remove VLAN 200
  mikrotik_swos_vlans:
    hostname: 192.168.1.1
    username: admin
    password: password
    vlan_id: 200
    state: absent
'''
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_vlans import Mikrotik_Vlans
def run_module():
    module_args = dict(
        hostname=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        vlan_id=dict(type='int', required=True),
        name=dict(type='str'),
        state=dict(type='str', default='present', choices=['present', 'absent']),
        port_isolation=dict(type='bool'),
        learning=dict(type='bool'),
        mirror=dict(type='bool'),
        igmp_snooping=dict(type='bool'),
        member_ports=dict(type='list', elements='int')
    )
    result = dict(
        changed=False,
        message=''
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    vlan = Mikrotik_Vlans(module.params['hostname'], module.params['username'], module.params['password'])
    if module.params['state'] == 'present':
            vlan_config = vlan.get(module.params['vlan_id'])
            if vlan_config is None:
                if not module.check_mode:
                    vlan.add(module.params['vlan_id'],
                            name=module.params['name'],
                            port_isolation=module.params['port_isolation'],
                            learning=module.params['learning'],
                            mirror=module.params['mirror'],
                            igmp_snooping=module.params['igmp_snooping'])
                    if module.params['member_ports']:
                        for port in module.params['member_ports']:
                            vlan.add_port(module.params['vlan_id'], port)
                    if vlan.save():
                        result['changed'] = True
                        result['message'] = f"VLAN {module.params['vlan_id']} added successfully"
                    else:
                        module.fail_json(msg=f"Failed to add VLAN {module.params['vlan_id']}")
                else:
                    result['changed'] = True
                    result['message'] = f"VLAN {module.params['vlan_id']} would be added (check mode)"
            else:
                changed = False
                if module.params['name'] and module.params['name'] != vlan_config['nm']:
                    vlan_config['nm'] = module.params['name']
                    changed = True
                if module.params['port_isolation'] is not None and module.params['port_isolation'] != vlan_config['piso']:
                    vlan_config['piso'] = module.params['port_isolation']
                    changed = True
                if module.params['learning'] is not None and module.params['learning'] != vlan_config['lrn']:
                    vlan_config['lrn'] = module.params['learning']
                    changed = True
                if module.params['mirror'] is not None and module.params['mirror'] != vlan_config['mrr']:
                    vlan_config['mrr'] = module.params['mirror']
                    changed = True
                if module.params['igmp_snooping'] is not None and module.params['igmp_snooping'] != vlan_config['igmp']:
                    vlan_config['igmp'] = module.params['igmp_snooping']
                    changed = True
                if module.params['member_ports']:
                    new_mbr = [0] * vlan.port_count
                    for port in module.params['member_ports']:
                        new_mbr[port-1] = 1
                    if new_mbr != vlan_config['mbr']:
                        vlan_config['mbr'] = new_mbr
                        changed = True
                if changed:
                    if not module.check_mode:
                        if vlan.save():
                            result['changed'] = True
                            result['message'] = f"VLAN {module.params['vlan_id']} updated successfully"
                        else:
                            module.fail_json(msg=f"Failed to update VLAN {module.params['vlan_id']}")
                    else:
                        result['changed'] = True
                        result['message'] = f"VLAN {module.params['vlan_id']} would be updated (check mode)"
                else:
                    result['message'] = f"VLAN {module.params['vlan_id']} is already up to date"
    elif module.params['state'] == 'absent':
        if vlan.get(module.params['vlan_id']) is not None:
            if not module.check_mode:
                if vlan.remove(module.params['vlan_id']) and vlan.save():
                    result['changed'] = True
                    result['message'] = f"VLAN {module.params['vlan_id']} removed successfully"
                else:
                    module.fail_json(msg=f"Failed to remove VLAN {module.params['vlan_id']}")
            else:
                result['changed'] = True
                result['message'] = f"VLAN {module.params['vlan_id']} would be removed (check mode)"
        else:
            result['message'] = f"VLAN {module.params['vlan_id']} does not exist"
    module.exit_json(**result)
def main():
    run_module()
if __name__ == '__main__':
    main()
================================================

File: mikrotik_lacp.py
================================================
#!/usr/bin/env python3
import ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_utils as mikrotik_utils
from ansible_collections.mikrotik_swos.core.plugins.module_utils.swostab import Swostab
# payload
# {mode:[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x01,0x00,0x00],sgrp:[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x01,0x00,0x00]}
PAGE = "/lacp.b"
LAG_MODE = {
    "passive": "0x00",
    "active": "0x01",
    "static": "0x02"
}
class Mikrotik_Lacp(Swostab):
    def _load_tab_data(self):
        self._data = mikrotik_utils.mikrotik_to_json(self._get(PAGE).text)
    def port_lacp_mode(self, port_id, mode, group_id=None):
        if mode not in LAG_MODE:
            return False
        if port_id < 1 or port_id > self.port_count:
            return False
        _mode = LAG_MODE[mode]
        if mode == "static" and group_id:
            self._update_data("sgrp", mikrotik_utils.hex_str_with_pad(group_id, pad=2), port_id-1)
        self._update_data("mode", _mode, port_id-1)
        return True
    def save(self):
        return self._save(PAGE)
    def show(self):
        lag_mode_str = {v: k for k, v in LAG_MODE.items()}
        print("lacp tab")
        print("port status {}".format(lag_mode_str[self._data["mode"]]))
        print("")
================================================

File: mikrotik_port.py
================================================
#!/usr/bin/env python3
import ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_utils as mikrotik_utils
from ansible_collections.mikrotik_swos.core.plugins.module_utils.swostab import Swostab
# payload
# {en:0x03c20007,nm:['6d657a7a5f6c6170746f70','6d657a7a5f67616d65','627572656175','506f727434','506f727435','506f727436','506f727437','506f727438','506f727439','506f72743130','506f72743131','506f72743132','506f72743133','506f72743134','506f72743135','506f72743136','506f72743137','6e6574','506f72743139','506f72743230','506f72743231','506f72743232','6865795f31','6865795f32','53465031','53465032'],an:0x03ffffff,spdc:[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x01],dpxc:0x03ffffff,fctc:0x03ffffff,fctr:0x03ffffff}
PAGE = "/link.b"
# notes
# sfpo 0x18 => 24 (first sfp index ?)
# sfp 0x2 => 2 (sfp count)
# prt 0x1a => 26 (port count)
PORT_SPEED_MB = {
    "10": "0x00",
    "100": "0x01",
    "1000": "0x02",
    "2500": "0x05",
    "10000": "0x03"
}
PORT_SFP_RATE = {
    "low": "0x00",
    "high": "0x01"
}
class Mikrotik_Port(Swostab):
    def _load_tab_data(self):
        self._data = mikrotik_utils.mikrotik_to_json(self._get(PAGE).text)
        self.parsed_data = {
            "name": [],
            "speed": [],
        }
        self.parsed_data["enabled"] = mikrotik_utils.decode_listofflags(self._data["en"], self.port_count)
        self.parsed_data["duplex"]  = mikrotik_utils.decode_listofflags(self._data["dpxc"], self.port_count)
        self.parsed_data["tx_flow_control"] = mikrotik_utils.decode_listofflags(self._data["fctc"], self.port_count)
        self.parsed_data["rx_flow_control"] = mikrotik_utils.decode_listofflags(self._data["fctr"], self.port_count)
        self.parsed_data["autoneg"] = mikrotik_utils.decode_listofflags(self._data["an"], self.port_count)
        self.parsed_data["speed"] = self._data["spdc"].copy()
        for i in range(0, self.port_count):
            self.parsed_data["name"].append(mikrotik_utils.decode_string(self._data["nm"][i]))
        if self.version >= 2.16:
            self.parsed_data["sfp_rate"] = self._data["sfpr"].copy()
    def configure(self, port_id, **kwargs):
        if port_id < 1 or port_id > self.port_count:
            return
        self.parsed_data["name"][port_id-1] = kwargs.get("name", None)
        self.parsed_data["enabled"][port_id-1] = 1 if kwargs.get("enabled", 0) else 0
        self.parsed_data["autoneg"][port_id-1] = 1 if kwargs.get("autoneg", 1) else 0
        self.parsed_data["duplex"][port_id-1] = 1 if kwargs.get("duplex", 1) else 0
        self.parsed_data["tx_flow_control"][port_id-1] = 1 if kwargs.get("tx_flow_control", 0) else 0
        self.parsed_data["rx_flow_control"][port_id-1] = 1 if kwargs.get("rx_flow_control", 0) else 0
        if kwargs.get("autoneg", 1) == 0 and kwargs.get("speed", None):
            self.parsed_data["speed"][port_id-1] = PORT_SPEED_MB.get(str(kwargs.get("speed")), "0x02")
        if self.version >= 2.16 and kwargs.get("sfp_rate", None):
            self.parsed_data["sfp_rate"][port_id-1] = PORT_SFP_RATE.get(kwargs.get("sfp_rate"), "0x00")
    def save(self):
        self._update_data("en", mikrotik_utils.encode_listofflags(self.parsed_data["enabled"], 8))
        self._update_data("dpxc", mikrotik_utils.encode_listofflags(self.parsed_data["duplex"], 8))
        self._update_data("fctc", mikrotik_utils.encode_listofflags(self.parsed_data["tx_flow_control"], 8))
        self._update_data("fctr", mikrotik_utils.encode_listofflags(self.parsed_data["rx_flow_control"], 8))
        self._update_data("an", mikrotik_utils.encode_listofflags(self.parsed_data["autoneg"], 8))
        for i in range(0, self.port_count):
            self._update_data("nm", mikrotik_utils.encode_string(self.parsed_data["name"][i]), i)
            self._update_data("spdc", self.parsed_data["speed"][i], i)
        if self.version >= 2.16:
            for i in range(0, self.port_count):
                self._update_data("sfpr", self.parsed_data["sfp_rate"][i], i)
        return self._save(PAGE)
    def show(self):
        port_speed_mb_str = {v: k for k, v in PORT_SPEED_MB.items()}
        print("link tab")
        for i in range(0, self.port_count):
            print("* {} enabled: {}, autoneg: {}, speed: {}mb/s, duplex: {}, ctrl tx: {}, ctrl rx: {}".format(
                self.parsed_data["name"][i],
                self.parsed_data["enabled"][i],
                self.parsed_data["autoneg"][i],
                port_speed_mb_str[self.parsed_data["speed"][i]],
                self.parsed_data["duplex"][i],
                self.parsed_data["tx_flow_control"][i],
                self.parsed_data["rx_flow_control"][i],
            ))
        print("")
================================================

File: mikrotik_port_isolation.py
================================================
#!/usr/bin/env python3
import ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_utils as mikrotik_utils
from ansible_collections.mikrotik_swos.core.plugins.module_utils.swostab import Swostab
# payload
# -- forwarding tab
# {fp1:0xfdfffe,fp2:0xfdfffd,fp3:0xfdfffb,fp4:0xfdfff7,fp5:0xfdffef,fp6:0xfdffdf,fp7:0xfdffbf,fp8:0xfdff7f,fp9:0xfdfeff,fp10:0xfdfdff,fp11:0xfdfbff,fp12:0xfdf7ff,fp13:0xfdefff,fp14:0xfddfff,fp15:0xfdbfff,fp16:0xfd7fff,fp17:0xfcffff,fp18:0xc00000,fp19:0xf9ffff,fp20:0xf5ffff,fp21:0xedffff,fp22:0xddffff,fp23:0x01bfffff,fp24:0x017fffff,fp25:0xc00000,fp26:0x00}
#
# -- vlan tab
#
# {vlan:[0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x02,0x02,0x02],vlni:[0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x01,0x00,0x01],dvid:[0x044c,0x044c,0x044d,0x044d,0x044d,0x044d,0x044d,0x044d,0x044d,0x044d,0x044d,0x044d,0x044d,0x044d,0x044d,0x044d,0x044d,0x044d,0x044d,0x044d,0x044d,0x044d,0x03f3,0x0001,0x044e,0x0001],fvid:0x007fffff}
PAGE = "/fwd.b"
VLAN_MODE = {
    "disabled": "0x00",
    "optional": "0x01",
    "enabled": "0x02",
    "strict": "0x03"
}
VLAN_RECEIVE_MODE = {
    "any": "0x00",
    "only tagged": "0x01",
    "only untagged": "0x02"
}
class Mikrotik_Forwarding(Swostab):
    def _load_tab_data(self):
        self._data = mikrotik_utils.mikrotik_to_json(self._get(PAGE).text)
    def port_isolation(self, port_id, port_list = []):
        if port_id < 1 or port_id > self.port_count:
            return False
        if port_list is None:
            return False
        if isinstance(port_list, str) and port_list == 'any':
            acl = [1] * self.port_count
        else:
            acl = [0] * self.port_count
            for p in port_list:
                if p <= self.port_count:
                    acl[p-1] = 1
        acl[port_id-1] = 0
        self._update_data("fp{}".format(port_id), mikrotik_utils.encode_listofflags(acl, 8))
        return True
    def port_vlan_config(self, port_id, mode = None, receive_mode = None, default_vlan_id = None, force_vlan_id = None):
        if port_id < 1 or port_id > self.port_count:
            return False
        if mode is not None:
            _mode = VLAN_MODE[mode]
            self._update_data("vlan", _mode, port_id-1)
        if receive_mode is not None:
            _mode = VLAN_RECEIVE_MODE[receive_mode]
            self._update_data("vlni", _mode, port_id-1)
        if default_vlan_id is not None:
            _dvid_val = mikrotik_utils.hex_str_with_pad(default_vlan_id, 4)
            self._update_data("dvid", _dvid_val, port_id-1)
        if force_vlan_id is not None:
            _fvid = mikrotik_utils.decode_listofflags(self._data["fvid"], self.port_count)
            if force_vlan_id:
                _fvid[port_id-1] = 1
            else:
                _fvid[port_id-1] = 0
            self._update_data("fvid", mikrotik_utils.encode_listofflags(_fvid, 8))
        return True
    def save(self):
        return self._save(PAGE)
    def show(self):
        vlan_mode_str = {v: k for k, v in VLAN_MODE.items()}
        vlan_receive_mode_str = {v: k for k, v in VLAN_RECEIVE_MODE.items()}
        print("port isolation tab")
        print(self._data["fvid"])
        _fvid = mikrotik_utils.decode_listofflags(self._data["fvid"], self.port_count)
        for i in range(1, self.port_count):
            # indexed fpX
            print("port {}:".format(i))
            print("  isolation table: {}".format(mikrotik_utils.decode_listofflags(self._data["fp{}".format(i)], self.port_count)))
            print("  vlan mode: {}".format(vlan_mode_str[self._data["vlan"][i-1]]))
            print("  vlan receive mode: {}".format(vlan_receive_mode_str[self._data["vlni"][i-1]]))
            print("  default vlan id: {}".format(int(self._data["dvid"][i-1], 16)))
            print("  force vlan id: {}".format(_fvid[i-1]))
        print("")
================================================

File: mikrotik_rstp.py
================================================
#!/usr/bin/env python3
import ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_utils as utils
from ansible_collections.mikrotik_swos.core.plugins.module_utils.swostab import Swostab
PAGE = "/rstp.b"
class Mikrotik_Rstp(Swostab):
    def _load_tab_data(self):
        self._data = utils.mikrotik_to_json(self._get(PAGE).text)
        self._parsed_data = {
            "ena": utils.decode_listofflags(self._data.get("ena", "0x0"), self.port_count)
        }
    def on_port(self, port_id, rstp_mode):
        if port_id < 1 or port_id > self.port_count:
            raise ValueError(f"Port {port_id} is out of range (1-{self.port_count}).")
        current_state = self._parsed_data["ena"][port_id - 1]
        desired_state = 1 if rstp_mode else 0
        if current_state == desired_state:
            return False  # No change needed
        self._parsed_data["ena"][port_id - 1] = desired_state
        return True
    def save(self):
        self._update_data("ena", utils.encode_listofflags(self._parsed_data["ena"], 8))
        return self._save(PAGE)
    def show(self):
        print("RSTP tab")
        print(f"Port status: {self._parsed_data['ena']}")
        print("")
================================================

File: mikrotik_snmp.py
================================================
#!/usr/bin/env python3
import ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_utils as mikrotik_utils
from ansible_collections.mikrotik_swos.core.plugins.module_utils.swostab import Swostab
# SNMP payload page
PAGE = "/snmp.b"
class Mikrotik_Snmp(Swostab):
    def _load_tab_data(self):
        response = self._get(PAGE)
        response.raise_for_status()
        self._data = mikrotik_utils.mikrotik_to_json(response.text)
        self.data_enabled = mikrotik_utils.decode_checkbox(self._data.get("en"))
        self.data_community = mikrotik_utils.decode_string(self._data.get("com"))
        self.data_contact_info = mikrotik_utils.decode_string(self._data.get("ci"))
        self.data_location = mikrotik_utils.decode_string(self._data.get("loc"))
    def set(self, enable=None, community=None, contact_info=None, location=None):
        # Update the 'en' field based on 'enable' parameter
        if enable is not None:
            self._update_data("en", mikrotik_utils.encode_checkbox(enable))
        if community is not None:
            self._update_data("com", mikrotik_utils.encode_string(community))
        if contact_info is not None:
            self._update_data("ci", mikrotik_utils.encode_string(contact_info))
        if location is not None:
            self._update_data("loc", mikrotik_utils.encode_string(location))
        return self._save(PAGE)
================================================

File: mikrotik_system.py
================================================
#!/usr/bin/env python3
import ipaddress
import ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_utils as mikrotik_utils
from ansible_collections.mikrotik_swos.core.plugins.module_utils.swostab import Swostab
# snmp payload
# {iptp:0x01,ip:0xfa001f0a,id:'4d696b726f54696b',alla:0x00,allm:0x00,allp:0xc00003,avln:0x044c,wdt:0x01,ivl:0x00,igmp:0x01,igfl:0x01020000,dsc:0x00,dtrp:0x01c20000,ainf:0x01,ver:'322e3133'}
PAGE = "/sys.b"
IGMP_VERSION = {
    "v2": "0x00",
    "v3": "0x01"
}
class Mikrotik_System(Swostab):
    def _load_tab_data(self):
        self._data = mikrotik_utils.mikrotik_to_json(self._get(PAGE).text)
    # todo: iptp
    def set(self, **kwargs):
        if kwargs.get("allow_from_net4", None):
            # mikrotik switch expect a valid network/mask combination => 10.31.0.0/15 is wrong
            tokens = str(ipaddress.IPv4Network(kwargs.get("allow_from_net4"), strict=False)).split("/")
            self._update_data("alla", mikrotik_utils.encode_ipv4(tokens[0]))
            try:
                self._update_data("allm", mikrotik_utils.hex_str_with_pad(int(tokens[1]), pad=2))
            except IndexError:
                self._update_data("allm", mikrotik_utils.hex_str_with_pad(32, pad=2))
        if kwargs.get("allow_from_vlan", None):
            self._update_data("avln", mikrotik_utils.hex_str_with_pad(int(kwargs.get("allow_from_vlan")), 4))
        # Convert allow_from_port from port numbers to flags
        if kwargs.get("allow_from_port", None):
            flags = mikrotik_utils.ports_to_flag_list(kwargs.get("allow_from_port", None), self.port_count)
            self._update_data("allp", mikrotik_utils.encode_listofflags(flags, 8))
        self._update_data("wdt", mikrotik_utils.encode_checkbox(kwargs.get("watchdog", None)))
        self._update_data("ivl", mikrotik_utils.encode_checkbox(kwargs.get("independant_vlan_lookup", None)))
        self._update_data("igmp", mikrotik_utils.encode_checkbox(kwargs.get("igmp_snooping", None)))
        # Convert igmp_fast_leave from port numbers to flags
        if kwargs.get("igmp_fast_leave", None):
            flags = mikrotik_utils.ports_to_flag_list(kwargs.get("igmp_fast_leave", None), self.port_count)
            self._update_data("igfl", mikrotik_utils.encode_listofflags(flags, 8))
        self._update_data("dsc", mikrotik_utils.encode_checkbox(kwargs.get("mikrotik_discovery_protocol", None)))
        # Convert dhcp_trusted_port from port numbers to flags
        if kwargs.get("dhcp_trusted_port", None):
            flags = mikrotik_utils.ports_to_flag_list(kwargs.get("dhcp_trusted_port", None), self.port_count)
            self._update_data("dtrp", mikrotik_utils.encode_listofflags(flags, 8))
        self._update_data("ainf", mikrotik_utils.encode_checkbox(kwargs.get("dhcp_add_information_option", None)))
        self._update_data("id", mikrotik_utils.encode_string(kwargs.get("identity", None)))
        # 2.16 additions
        if self.version >= 2.16:
            # igmp querier
            if kwargs.get("igmp_snooping", None):
                self._update_data("igmq", mikrotik_utils.encode_checkbox(kwargs.get("igmp_querier", None)))
            else:
                self._update_data("igmq", mikrotik_utils.encode_checkbox(False))
            # igmp version
            self._update_data("igve", IGMP_VERSION[kwargs.get("igmp_version", "v3")])
        return self._save(PAGE)
    def show(self):
        print("system tab")
        print("* version: {}" . format(self.version))
        print("* identity: {}" . format(mikrotik_utils.decode_string(self._data["id"])))
        print("* address acq: {}" . format(self._data["iptp"]))
        print("* address: {}" . format(mikrotik_utils.decode_ipv4(self._data["ip"])))
        print("* allow from: {}/{}" . format(mikrotik_utils.decode_ipv4(self._data["alla"]), int(self._data["allm"], 16)))
        print("* allow from vlan {}" . format(int(self._data["avln"], 16)))
        print("* allow from ports {}" . format(mikrotik_utils.decode_listofflags(self._data["allp"], self.port_count)))
        print("* watchdog {}" . format(mikrotik_utils.decode_checkbox(self._data["wdt"])))
        print("* independent vlan lookup {}" . format(mikrotik_utils.decode_checkbox(self._data["ivl"])))
        print("* igmp snooping {}" . format(mikrotik_utils.decode_checkbox(self._data["igmp"])))
        print("* igmp fast leave {}" . format(mikrotik_utils.decode_listofflags(self._data["igfl"], self.port_count)))
        print("* mikrotik discovery protocol {}" . format(mikrotik_utils.decode_checkbox(self._data["dsc"])))
        print("* dhcp trusted ports {}" . format(mikrotik_utils.decode_listofflags(self._data["dtrp"], self.port_count)))
        print("* add information option {}" . format(mikrotik_utils.decode_checkbox(self._data["ainf"])))
        if self.version >= 2.16:
            igmp_ver_str = {v: k for k, v in IGMP_VERSION.items()}
            print("* igmp querier {}" . format(mikrotik_utils.decode_checkbox(self._data["igmq"])))
            print("* igmp version {}" . format(igmp_ver_str[self._data["igve"]]))
        print("")
================================================

File: mikrotik_utils.py
================================================
#!/usr/bin/env python3
import json
import re
import socket
import struct
def mikrotik_to_json(broken_json):
    result = re.sub(r'([{,])([a-zA-Z][a-zA-Z0-9]+)', '\\1"\\2"', broken_json)
    result = re.sub(r'\'', '"', result)
    result = re.sub(r'(0x[0-9a-zA-Z]+)', '"\\1"', result)
    return json.loads(result)
def json_to_mikrotik(data):
    result = re.sub(r'"(0x[0-9a-zA-Z]+)"', '\\1', json.dumps(data))
    result = re.sub(r'"([a-zA-Z][a-zA-Z0-9]+)":', '\\1:', result)
    result = re.sub(r'"', '\'', result)
    return result.replace(" ", "")
# 53465031 -> SFP1
def decode_string(s):
    return bytes.fromhex(s).decode("ascii")
# SFP1 -> 53465031
def encode_string(s):
    if isinstance(s, str):
        return s.encode("ascii").hex()
    return None
# 0x1c20005 -> [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0]
def decode_listofflags(s, zfill=0):
    flags = []
    if len(s) == 0:
        return flags
    # list is reversed (example port1 is last item)
    flags_str = bin(int(s, 16))[2:]
    if zfill > 0:
        flags_str = flags_str.zfill(zfill)
    flags_list = list(flags_str)
    i = len(flags_list)
    while i:
        flags.append(int(flags_list[i-1]))
        i -= 1
    return flags
# [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0] --> 0x1c20005
# with hex_len_str=8 => 0xc26005 becomes 0x00c26005
def encode_listofflags(flags, hex_len_str=0):
    if flags is None or len(flags) == 0:
        return None
    # list needs to be reversed
    flags_str = ""
    i = len(flags)
    while i:
        flags_str += str(flags[i-1])
        i -= 1
    return hex_str_with_pad(int(flags_str, 2), hex_len_str)
# with pad=8 => 0xc26005 becomes 0x00c26005
def hex_str_with_pad(s, pad=0):
    if s is None:
        return None
    if pad == 0:
        return hex(s)
    else:
        return '0x{0:0{1}x}'.format(s,pad)
# 10.31.0.250 => 0xfa001f0a
def encode_ipv4(s):
    if isinstance(s, str):
        return hex_str_with_pad(struct.unpack("I", socket.inet_aton(s))[0], 8)
    return None
# 0xfa001f0a => 10.31.0.250
def decode_ipv4(s):
    if s == "0x00000000":
        return ""
    return socket.inet_ntoa(struct.pack("<L", int(s, 16)))
# true => 0x01 / false => 0x00 / None => None
def encode_checkbox(s):
    if s is None:
        return None
    return "0x01" if s else "0x00"
# 0x01 => true
def decode_checkbox(s):
    return s == "0x01"
# [1, 3, 4] --> [1, 0, 1, 1]
def ports_to_flag_list(ports, fill=0):
    if not isinstance(ports, list):
        return None
    if not fill:
        if len(ports):
            fill = max(ports)
        else:
            return []
    flag_list = [0] * fill
    for i in ports:
        flag_list[i-1] = 1
    return flag_list
================================================

File: mikrotik_vlan.py
================================================
#!/usr/bin/env python3
from ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_utils import mikrotik_to_json, encode_listofflags, decode_listofflags, hex_str_with_pad
from ansible_collections.mikrotik_swos.core.plugins.module_utils.swostab import Swostab
VLAN_MODE = {
    "disabled": "0x00",
    "optional": "0x01",
    "enabled": "0x02",
    "strict": "0x03"
}
VLAN_RECEIVE_MODE = {
    "any": "0x00",
    "only_tagged": "0x01",
    "only_untagged": "0x02"
}
class Mikrotik_VLAN_Config(Swostab):
    PAGE = "/fwd.b"
    def _load_tab_data(self):
        self._data = mikrotik_to_json(self._get(self.PAGE).text)
    def configure_vlan(self, port_id, mode=None, receive_mode=None, default_vlan_id=None, force_vlan_id=None):
        if port_id < 1 or port_id > self.port_count:
            raise ValueError(f"port_id {port_id} is out of range (1-{self.port_count})")
        if mode is not None:
            if mode not in VLAN_MODE:
                raise ValueError(f"Invalid VLAN mode: {mode}")
            _mode = VLAN_MODE[mode]
            self._update_data("vlan", _mode, port_id-1)
        if receive_mode is not None:
            if receive_mode not in VLAN_RECEIVE_MODE:
                raise ValueError(f"Invalid VLAN receive mode: {receive_mode}")
            _receive_mode = VLAN_RECEIVE_MODE[receive_mode]
            self._update_data("vlni", _receive_mode, port_id-1)
        if default_vlan_id is not None:
            if not (1 <= default_vlan_id <= 4094):
                raise ValueError(f"default_vlan_id {default_vlan_id} is out of valid range (1-4094)")
            _dvid_val = hex_str_with_pad(default_vlan_id, 4)
            self._update_data("dvid", _dvid_val, port_id-1)
        if force_vlan_id is not None:
            _fvid = decode_listofflags(self._data.get("fvid", "0x00"), self.port_count)
            _fvid[port_id-1] = 1 if force_vlan_id else 0
            self._update_data("fvid", encode_listofflags(_fvid, 8))
        return True
    def save_changes(self):
        return self._save(self.PAGE)
================================================

File: mikrotik_vlans.py
================================================
#!/usr/bin/env python3
import ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_utils as mikrotik_utils
from ansible_collections.mikrotik_swos.core.plugins.module_utils.swostab import Swostab
# payload
# [{vid:0x64,nm:'696e7465726e6574',piso:0x01,lrn:0x01,mrr:0x00,igmp:0x00,mbr:0x01c20000},{vid:0x044c,nm:'70726976617465',piso:0x01,lrn:0x01,mrr:0x00,igmp:0x00,mbr:0xc00003},{vid:0x044d,nm:'7075626c6963',piso:0x01,lrn:0x01,mrr:0x00,igmp:0x00,mbr:0xc00004},{vid:0x044e,nm:'736670',piso:0x01,lrn:0x01,mrr:0x00,igmp:0x00,mbr:0x01c20000}]
PAGE = "/vlan.b"
class Mikrotik_Vlans(Swostab):
    def _load_tab_data(self):
        self._parsed_data = {}
        self._data = mikrotik_utils.mikrotik_to_json(self._get(PAGE).text)
        for i in self._data:
            self._parsed_data[int(i['vid'], 16)] = {
                "idx": i,
                "nm": mikrotik_utils.decode_string(i["nm"]),
                "piso": mikrotik_utils.decode_checkbox(i["piso"]),
                "lrn": mikrotik_utils.decode_checkbox(i["lrn"]),
                "mrr": mikrotik_utils.decode_checkbox(i["mrr"]),
                "igmp": mikrotik_utils.decode_checkbox(i["igmp"]),
                "mbr": mikrotik_utils.decode_listofflags(
                    i["mbr"], self.port_count
                )
            }
    def get(self, vlan_id):
        return self._parsed_data.get(vlan_id, None)
    def reset_member_cfg(self):
        for vlan in self._parsed_data:
            self._parsed_data[vlan]["mbr"] = [0] * self.port_count
    def add_port(self, vlan_id, port_id):
        if port_id <= 0 or port_id > self.port_count:
            return False
        _vlan_config = self.get(vlan_id)
        if _vlan_config is None:
            return False
        _vlan_config["mbr"][port_id-1] = 1
        return True
    def add(self, vlan_id, **kwargs):
        _vlan_config = self.get(vlan_id)
        if _vlan_config is None:
            _vlan_config = {
                "vid": mikrotik_utils.hex_str_with_pad(vlan_id, pad=4),
                "nm": "",
                "piso": True,
                "lrn": True,
                "mrr": False,
                "igmp": False,
                "mbr": [0] * self.port_count,
            }
            self._data.append(_vlan_config)
            self._parsed_data[vlan_id] = _vlan_config
        _vlan_config["nm"] = kwargs.get("name", str(vlan_id))
        _vlan_config["piso"] = kwargs.get("port_isolation", None)
        _vlan_config["lrn"] = kwargs.get("learning", None)
        _vlan_config["mrr"] = kwargs.get("mirror", None)
        _vlan_config["igmp"] = kwargs.get("igmp_snooping", None)
    def remove(self, vlan_id):
        vlan = self._parsed_data.pop(vlan_id, None)
        if vlan:
            self._data.remove(vlan["idx"])
            self._data_changed = True
            return True
        return False
    def save(self):
        i = 0
        while i < len(self._data):
            vlan_id = int(self._data[i]['vid'], 16)
            self._update_data(i, mikrotik_utils.encode_string(self._parsed_data[vlan_id]["nm"]), "nm")
            self._update_data(i, mikrotik_utils.encode_listofflags(self._parsed_data[vlan_id]["mbr"], 8), "mbr")
            for k in ["piso", "lrn", "mrr", "igmp"]:
                self._update_data(i, mikrotik_utils.encode_checkbox(self._parsed_data[vlan_id][k]), k)
            i += 1
        return self._save(PAGE)
    def show(self):
        print("vlan tab")
        for i in self._parsed_data:
            print("* vlan: {} => {}".format(i, self._parsed_data[i]))
        print("")
================================================

File: swostab.py
================================================
#!/usr/bin/env python3
import requests
import ansible_collections.mikrotik_swos.core.plugins.module_utils.mikrotik_utils as mikrotik_utils
class Swostab:
    def _get(self, page):
        return requests.get(self._url + page, auth=self._auth)
    def _post(self, page, data):
        return requests.post(self._url + page, auth=self._auth, data=data)
    def _update_data(self, field, value = None, field_index = None):
        if value is None:
            return
        if field_index is not None:
            if value != self._data[field][field_index]:
                self._data[field][field_index] = value
                self._data_changed = True
            return
        if value != self._data[field]:
            self._data[field] = value
            self._data_changed = True
    def __init__(self, url, login, password):
        if 'http://' not in url:
            self._url = "http://%s" % url
        else:
            self._url  = url
        self._auth = requests.auth.HTTPDigestAuth(login, password)
        resp = self._get("/link.b")
        resp.raise_for_status()
        # required to decode some list of boxes
        _link = mikrotik_utils.mikrotik_to_json(resp.text)
        self.port_count = int(_link["prt"], 16)
        # some feature appears in 2.16
        resp = self._get("/sys.b")
        resp.raise_for_status()
        # required to decode some list of boxes
        _sys = mikrotik_utils.mikrotik_to_json(resp.text)
        self.version = float(mikrotik_utils.decode_string(_sys["ver"]))
        self._load_tab_data()
        self._data_changed = False
    def show(self):
        raise Exception("not implemented")
    def _load_tab_data(self):
        raise Exception("not implemented")
    def _save(self, page):
        if self._data_changed:
            return self._post(page, mikrotik_utils.json_to_mikrotik(self._data)).ok
        return False
================================================

File: README.md
================================================
# Collections Plugins Directory
This directory can be used to ship various plugins inside an Ansible collection. Each plugin is placed in a folder that
is named after the type of plugin it is in. It can also include the `module_utils` and `modules` directory that
would contain module utils and modules respectively.
Here is an example directory of the majority of plugins currently supported by Ansible:
```
└── plugins
    ├── action
    ├── become
    ├── cache
    ├── callback
    ├── cliconf
    ├── connection
    ├── filter
    ├── httpapi
    ├── inventory
    ├── lookup
    ├── module_utils
    ├── modules
    ├── netconf
    ├── shell
    ├── strategy
    ├── terminal
    ├── test
    └── vars
```
A full list of plugin types can be found at [Working With Plugins](https://docs.ansible.com/ansible-core/2.15/plugins/plugins.html).
================================================

File: README.md
================================================
# Ansible Collection - mikrotik_swos.core
Copied from https://github.com/y-martin/pkg-python3-mikrotik-swos and modified to work with Ansible Collection.
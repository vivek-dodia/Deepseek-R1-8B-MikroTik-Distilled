# Repository Information
Name: ansible-telnet-mikrotik

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
	url = https://gitlab.com/alexnet-public/ansible-telnet-mikrotik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: mikrotik.py
================================================
#!/usr/bin/python3
from rancidcmd import RancidCmd
import re
import os
import sys
class MikroTikConnection:
    # Подключиться к консоли микротик
    def mtlogin(self,user,addr,cmd,password,enable_password,port,method):    
        args = dict(user=user,
                    password=password,
                    enable_password=enable_password,
                    login='mtlogin',
                    address=addr,
                    port=port,
                    method=method)
        #cmd = ['interface print', 'ip address print', 'ip arp print']
        cmd_string = ''
        i = 0
        while i < len(cmd):
            cmd_string += cmd[i]
            if i < len(cmd) - 1:  # Добавляем экранированный разделитель после всех команд, кроме последней
                cmd_string += '\\r\\n'
            i += 1
        cmd_string += '\\r\\n'  # Добавляем экранированный перенос строки в конец строки cmd_string
        #print(cmd_string)
        rancid = RancidCmd(**args)
        res = rancid.execute(cmd_string)
        #print(res)
        if res['rtn_code'] == 0:
            txt = res['std_out']
            return txt
        else:
            #txt = '[error] %s' + res['std_err']
            txt = 'error'
            return txt
    # Исходная функция, с некоторыми корректировками
    def version(self,user, addr, password, enable_password):
        cmd = ['system routerboard print','system resource print','system identity print']
        methods_ports = [('telnet', '23'), ('ssh', '22'), ('ssh', '6522')]
        for method, port in methods_ports:
            txt = self.mtlogin(user, addr, cmd, password, enable_password, port, method)
            if txt != 'error':
                #print(txt)
                result = self.parse_mikrotik_output(txt,method,port)
                # Добавляем метод и порт к результату перед возвращением
                result.update({'method': method, 'port': port})
                return result
        # Если все попытки подключения неудачны
        return {'test': 'error', 'vendor': 'unknown', 'version': '', 'model': '', 'hostname': '', 'method': '', 'port': ''}
    def parse_mikrotik_output(self,text, method, port):
        lines = text.splitlines()  # Разделение текста на строки
        identity, version, model = "Не найдено", "Не найдено", "Не найдено"
        # Флаги для определения, когда начинается вывод каждой команды
        reading_identity, reading_version, reading_model = False, False, False
        for line in lines:
            if 'system routerboard print' in line:
                reading_model = True
            elif 'system resource print' in line:
                reading_version = True
            elif 'system identity print' in line:
                reading_identity = True
            elif reading_identity and line.strip().startswith('name:'):
                identity = line.split(':')[1].strip()
                reading_identity = False  # Прекращаем чтение после нахождения
            elif reading_version and line.strip().startswith('version:'):
                version = line.split(':')[1].strip()
                reading_version = False  # Прекращаем чтение после нахождения
            elif reading_model and line.strip().startswith('board-name:'):
                model = line.split(':')[1].strip()
                reading_model = False  # Прекращаем чтение после нахождения
        return {
            'test': 'ok',
            'vendor': 'Mikrotik',
            'version': version,
            'model': model,
            'hostname': identity,
            'method': method,
            'port': port
        }
# TEST
#################################################
#
#connector = MikroTikConnection()
#
#user = 'admin'
#password = 'admin'
#enable_password = '1234'
#addr = '192.168.1.231'
#port = '22'
#method = 'ssh'
#cmd = ['interface print','ip address print','ip arp print']
#
#
#txt = connector.mtlogin(user,addr,cmd,password,enable_password,port,method)
#print(txt)
#
## Сохранение вывода в файл
#file_path = 'test.py'
#with open(file_path, 'w') as file:
#    file.write(txt)
#
#
#arr = connector.version(user,addr,password,enable_password)
#print(arr)
#
#################################################
================================================

File: mikrotik_command.py
================================================
# -*- coding: utf-8 -*-
#!/usr/bin/python3
import importlib.util
import sys
import re
from ansible.module_utils.basic import AnsibleModule
#from mikrotik import MikroTikConnection
def import_module_from_path(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module
# Используйте функцию для импорта вашего модуля
mikrotik = import_module_from_path('mikrotik', './library/mikrotik.py')
def run_module():
    module_args = dict(
        user=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        enable_password=dict(type='str', required=True, no_log=True),
        addr=dict(type='str', required=True),
        port=dict(type='str', required=False, default='22'),
        method=dict(type='str', required=False, default='ssh'),
        cmd=dict(type='list', required=True, elements='str'),
    )
    result = dict(
        changed=False,
        original_message='',
        message='',
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    if module.check_mode:
        module.exit_json(**result)
    try:
        # Создание экземпляра класса MikroTikConnection
        connector = mikrotik.MikroTikConnection()
        txt = connector.mtlogin(
            module.params['user'],
            module.params['addr'],
            module.params['cmd'],
            module.params['password'],
            module.params['enable_password'],
            module.params['port'],
            module.params['method']
        )
        #save_output_to_file(txt)
        #txt = remove_ansi_escape_sequences(txt)
        #bytes_ansi = txt.encode('cp1252')
        #txt = bytes_ansi.decode('utf-8')
        #txt = remove_ansi_escape_sequences(txt)
        result['message'] = txt
    except Exception as e:
        module.fail_json(msg=str(e), **result)
    module.exit_json(**result)
def main():
    run_module()
if __name__ == '__main__':
    main()
================================================

File: mikrotik_test.yaml
================================================
- hosts: Mikrotik
  tasks:
    - name: Execute commands on MikroTik device
      mikrotik_command:
        user: "{{ ansible_user }}"
        password: "{{ ansible_password }}"
        enable_password: '1234'
        addr: '{{ ansible_host }}'
        port: '{{ mikrotik_command_port }}'
        method: '{{ mikrotik_command_method }}'
        cmd:
          - 'interface print'
          - 'ip address print'
          - 'ip arp print'
      register: result
    - debug:
        var: result.message
    - name: Save output to a file
      ansible.builtin.copy:
        content: "{{ result.message }}"
        dest: "{{ inventory_hostname }}.txt"
      delegate_to: localhost
================================================

File: README.md
================================================
#  ansible-telnet-mikrotik
```
# MikroTik Device Management Playbook
This playbook automates executing commands on MikroTik devices using SSH or Telnet.
## Prerequisites
- Ansible installed.
- Credentials for MikroTik devices.
## Inventory Example
```ini
[Mikrotik]
router3 ansible_host=192.168.1.231 ansible_user=admin ansible_password=admin ansible_network_os=mikrotik_command ansible_connection=local mikrotik_command_method=ssh mikrotik_command_port=22 ansible_python_interpreter="/usr/bin/python3"
router2 ansible_host=192.168.1.110 ansible_user=admin ansible_password=admin ansible_network_os=mikrotik_command ansible_connection=local mikrotik_command_method=telnet mikrotik_command_port=23 ansible_python_interpreter="/usr/bin/python3"
```
## Usage
```bash
pip3 install rancidcmd
ansible-playbook -i hosts mikrotik_test.yaml
```
## Playbook Overview
1. **Execute Commands:** Runs commands (`interface print`, `ip address print`, `ip arp print`) on MikroTik, supporting both SSH and Telnet.
2. **Save Output:** Outputs from commands are saved to `<hostname>.txt`.
## Variables
- `ansible_user`: Username for device access.
- `ansible_password`: Password for device access.
- `enable_password`: Enable password if needed.
- `mikrotik_command_port`: Port for SSH (default 22) or Telnet (default 23).
- `mikrotik_command_method`: `ssh` or `telnet` for command execution.
Ensure `mikrotik_command_method` matches your device setup. For SSH, ensure SSH access is configured on the MikroTik device.
```
https://pypi.org/project/rancidcmd/
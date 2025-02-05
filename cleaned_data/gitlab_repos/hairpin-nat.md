# Repository Information
Name: hairpin-nat

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
	url = https://gitlab.com/wiki28/mikrotik/hairpin-nat.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: README.md
================================================
# Hairpin Nat или Nat Loopback
### Перенаправляем запросы из локальной сети на внешний адрес марштрутизатора на локальный адрес сервера.
Для решения данной задачи мы будем:
1. Маркируем новые пакеты из локальной сети которые идут на внешний адрес марштрутизатора.
2. Делаем правило **masquerade** для промаркированного трафика.
3. Создать обысное правило **dst-nat'a**.
- Маркируем пакеты:
```
/ip firewall mangle
add chain=prerouting comment="Hairpin nat" dst-address=%wan_ip% in-interface=%interface_lan% connection-state=new action=mark-packet new-packet-mark=hairpin-nat passthrough=yes
```
- Правило для masquerad'a:
```
/ip firewall nat
add chain=srcnat packet-mark=hairpin-nat action=masquerade comment="Hairpin nat replace address" 
```
- Создаем обычное правило dst-nat:
```
/ip firewall nat
add chain=dstnat dst-address=%wan_ip% protocol=tcp dst-port=80,443 action=dst-nat to-addresses=%local_server_ip%
add chain=dstnat dst-address=%wan_ip% protocol=tcp dst-port=8080 action=dst-nat to-addresses=%local_server_ip%
```
##### *В правилах удобно использовать **Interface List** и **Address List**
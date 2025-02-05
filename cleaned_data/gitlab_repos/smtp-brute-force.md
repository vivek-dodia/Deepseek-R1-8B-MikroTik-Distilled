# Repository Information
Name: smtp-brute-force

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
	url = https://gitlab.com/wiki28/mikrotik/smtp-brute-force.git
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
# Mikrotik + SMTP brute force
### Когда есть почтовый сервер на 25 порту и его пытаются сделать open relay или подобрать пароль.
1. Добавим группу правил в цепочке "forward", которая будет помещать IP адрес на 7 дней в список, когда наш сервер будет отвечать сообщением: 5.7.3 Authentication unsuccessful
```
/ip firewall filter
add action=add-dst-to-address-list address-list="Blacklist - SMTP brute force" address-list-timeout=1w chain=forward comment="Blacklist - SMTP brute force [5.7.3 Authentication unsuccessful]" content="5.7.3 Authentication unsuccessful" dst-address-list="Blacklist - SMTP brute force (stage 3)" log-prefix="Blacklist - SMTP brute force" in-interface-list=Lan out-interface-list=Wan protocol=tcp src-port=25
add action=add-dst-to-address-list address-list="Blacklist - SMTP brute force (stage 3)" address-list-timeout=120m chain=forward comment="Blacklist - SMTP brute force (stage 3) [5.7.3 Authentication unsuccessful]" content="5.7.3 Authentication unsuccessful" dst-address-list="Blacklist - SMTP brute force (stage 2)" log-prefix="Blacklist - SMTP brute force (stage 3)" in-interface-list=Lan out-interface-list=Wan protocol=tcp src-port=25
add action=add-dst-to-address-list address-list="Blacklist - SMTP brute force (stage 2)" address-list-timeout=120m chain=forward comment="Blacklist - SMTP brute force (stage 2) [5.7.3 Authentication unsuccessful]" content="5.7.3 Authentication unsuccessful" dst-address-list="Blacklist - SMTP brute force (stage 1)" log-prefix="Blacklist - SMTP brute force (stage 2)" in-interface-list=Lan out-interface-list=Wan protocol=tcp src-port=25
add action=add-dst-to-address-list address-list="Blacklist - SMTP brute force (stage 1)" address-list-timeout=120m chain=forward comment="Blacklist - SMTP brute force (stage 1) [5.7.3 Authentication unsuccessful]" content="5.7.3 Authentication unsuccessful" log-prefix="Blacklist - SMTP brute force (stage 1)" in-interface-list=Lan out-interface-list=Wan protocol=tcp src-port=25
```
2. Добавим группу правил в цепочке "forward", которая будет помещать IP адрес на 7 дней в список, когда наш сервер будет отвечать сообщением: 5.7.4 Unrecognized authentication type
```
/ip firewall filter
add action=add-dst-to-address-list address-list="Blacklist - SMTP brute force" address-list-timeout=1w chain=forward comment="Blacklist - SMTP brute force [5.7.4 Unrecognized authentication type]" content="5.7.4 Unrecognized authentication type" dst-address-list="Blacklist - SMTP brute force (stage 3)" log-prefix="Blacklist - SMTP brute force" in-interface-list=Lan out-interface-list=Wan protocol=tcp src-port=25
add action=add-dst-to-address-list address-list="Blacklist - SMTP brute force (stage 3)" address-list-timeout=120m chain=forward comment="Blacklist - SMTP brute force (stage 3) [5.7.4 Unrecognized authentication type]" content="5.7.4 Unrecognized authentication type" dst-address-list="Blacklist - SMTP brute force (stage 2)" log-prefix="Blacklist - SMTP brute force (stage 3)" in-interface-list=Lan out-interface-list=Wan protocol=tcp src-port=25
add action=add-dst-to-address-list address-list="Blacklist - SMTP brute force (stage 2)" address-list-timeout=120m chain=forward comment="Blacklist - SMTP brute force (stage 2) [5.7.4 Unrecognized authentication type]" content="5.7.4 Unrecognized authentication type" dst-address-list="Blacklist - SMTP brute force (stage 1)" log-prefix="Blacklist - SMTP brute force (stage 2)" in-interface-list=Lan out-interface-list=Wan protocol=tcp src-port=25
add action=add-dst-to-address-list address-list="Blacklist - SMTP brute force (stage 1)" address-list-timeout=120m chain=forward comment="Blacklist - SMTP brute force (stage 1) [5.7.4 Unrecognized authentication type]" content="5.7.4 Unrecognized authentication type" log-prefix="Blacklist - SMTP brute force (stage 1)" in-interface-list=Lan out-interface-list=Wan protocol=tcp src-port=25
```
3. Создаем правило, которое будет блокировать подключения по нашему списку
```
/ip firewall raw
add action=drop chain=prerouting comment="Raw prerouting drop - Blacklist - SMTP brute force" in-interface-list=Wan log-prefix="Raw prerouting drop - Blacklist - SMTP brute force" src-address-list="Blacklist - SMTP brute force"
```
Логика работы правил:
- при первом совпадении нашего правила, IP адрес помещается в address list "Blacklist - SMTP brute force (stage 1)" на 120 минут
- при повторном совпадении нашего правила, IP адрес помещается в address list "Blacklist - SMTP brute force (stage 2)" на 120 минут
- при третьем совпадении нашего правила, IP адрес помещается в address list "Blacklist - SMTP brute force (stage 3)" на 120 минут
- при четвертом совпадении нашего правила, IP адрес помещается в address list "Blacklist - SMTP brute force" на 7 дней
- правило, созданное в цепочке Raw, блокирует доступ к нашему серверу по address list "Blacklist - SMTP brute force"
### Описание переменных
Wan - interface list, в который помещены все интерфейсы, смотрящие в во внешнюю сеть, интернет.
Lan - interface list, в который помещены все интерфейсы, смотрящие в во внутреннюю сеть, локальную.
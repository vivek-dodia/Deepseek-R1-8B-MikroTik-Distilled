# Repository Information
Name: mikrotik-uplink-alert

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
	url = https://gitlab.com/GinTR1k/mikrotik-uplink-alert.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: README.md
================================================
# Mikrotik Uplink Alert
Уведомление по webhook'y об отсутствии аплинка у роутера.
## Установка
Требуется библиотека CURL. Компиляция командой `make compile`.
## Запуск
1. `./uplink_logger --down` - запустить при падении соединения.
1. `./uplink_logger --up` - запустить при восстановлении соединения.
Сформирует сообщение и запросит URL, установленный в переменной
окружения `UPLINK_ALERT_URL_TELEGRAM`. Аргумент `--bandwidth` позволяет передать текущую пропускную способность канала.
================================================
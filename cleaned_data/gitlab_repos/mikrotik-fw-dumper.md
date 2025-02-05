# Repository Information
Name: mikrotik-fw-dumper

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
	url = https://gitlab.com/the29a/mikrotik-fw-dumper.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: mt-local-repo.sh
================================================
#/bin/bash
#Кря
#Вы всё равно не читаете исходники скриптов
mkdir download
cd download
echo "Downloading Mikrotik firwmare and packages."
#Получаем список прошивок
touch fw.list ; curl -s https://mikrotik.com/download | grep -Eo "//[a-zA-Z0-9./?=_-]*" | grep npk | cut -c 3- | sort > fw.list ;
#Добавляем http
sed -i '/^http:\/\//!s/^/http:\/\//' fw.list
#Получаем список пакетов
touch pkg.list ; curl -s https://mikrotik.com/download | grep -Eo "//[a-zA-Z0-9./?=_-]*" | grep zip | cut -c 3- | sort > pkg.list ;
#Добавляем http
sed -i '/^http:\/\//!s/^/http:\/\//' pkg.list
#Скачиваем прошивки и пакеты
echo "Download firmware"
wget -N -nv -c -i fw.list -P fw
echo "Download packages"
wget -N -nv -c -i pkg.list -P pkg
#Надо сделать progressbar, но у меня лапки
echo "Done."
#¯\_(ツ)_/¯
================================================

File: README.md
================================================
Создает локальный репозиторий прошивок и дополнительных пакетов для Mikrotik
<br>
По умолчанию скачивает все npk и zip, доступные на https://mikrotik.com/download
<br>
<h>Использование:</h>
<p>git clone https://github.com/the29a/mikrotik-fw-dumper.git ; cd mikrotik-fw-dumper</p>
<p><code>chmod +x mt-local-repo.sh</code></p>
<p><code>./mt-local-repo.sh</code></p>
<h>Замеченые баги:</h>
<p>Повторно скачивает файлы для x86</p>
<p>На 10.03.2018 закрыт доступ к версии прошивки 5.26.</p>
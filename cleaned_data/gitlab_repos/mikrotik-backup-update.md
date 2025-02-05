# Repository Information
Name: mikrotik-backup-update

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
	url = https://gitlab.com/jorgeddev/mikrotik-backup-update.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: bkmk.sh
================================================
#!/bin/bash
#
#   Script Backup Mikrotik
#
#   Features:
#   - Create backup user into Routerboard
#   - Connect with ssh key
#   - Make dump Backup and Export file
#   - Verify version Firmware and model
#   - Run update commands.
#   - Copy to server backup file
#   - Send email report.
#
#   Contributors
#   - ST Duwe CBMSC
#   - Sgt Leonardo CBMSC
#   - Sd Jorge CBMSC
#
########################################
#   Start script
########################################
### Variable errors.
errors=0
### Function convert time.
tempo() {
	temp=$(($2-$1))
	hora=$(($temp/3600)) && temp=$(($temp%3600))
	if [ $hora -lt 10 ]; then
		hora=0$hora
	fi
	min=$(($temp/60))
	if [ $min -lt 10 ]; then
		min=0$min
	fi
	seg=$(($temp%60))
	if [ $seg -lt 10 ]; then
		seg=0$seg
	fi
	temp=$hora'h '$min'min '$seg'seg'
}
sshmk(){
	#Function use ssh with key
	ssh -n -o ConnectTimeout=10 -o BatchMode=yes -o LogLevel=quiet -o UserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no $sshuser@$ip $1;
}
scpmk(){
	#Function send user and pass
	scp -o ConnectTimeout=10 -o LogLevel=quiet -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no $sshuser@$ip$1; 
}
sshpassmk(){
	#Function send user and pass
	sshpass -p $password_default ssh -n -o ConnectTimeout=10 -o LogLevel=quiet -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no $userdefault@$ip $1; 
}
scppassmk(){
	#Function send user and pass
   sshpass -p $password_default scp -o LogLevel=quiet -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no $1; 
}
testusermk(){
	ssh -n -o ConnectTimeout=10 -o BatchMode=yes -o LogLevel=quiet -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no $sshuser@$ip ":log warning \"Server backup verify user key\"" 
}
### Function receive status error.
retur() {
        ret=$1
}
#Create files reports
echo "|       IP       |    CITY    |     PROBLEM      |" > /tmp/servers;
echo "|VERSION SW|FIRMATUAL/FIRMDISP.|        MODEL       |         IP         |      CITY    |" > /tmp/upgrade
### Function receive status error.
have_error() {
	ret=$1
	msgError=$2
	msgSuccess=$3
	msgErrorShort=$4
	if [ $ret -ne 0 ]; then
    	errors=$(($errors+1))
		echo "$msgError$city."
		echo "ERRO $ret"
		echo "$ip   $city $msgErrorShort" >> /tmp/servers
    else
        echo "$msgSuccess$city."
    fi
}
### Verify online server
online() {
        ping -c 1 -W 2 $ip
        up=$?
}
#Send key if server don't have the key.
verify_key(){
	testusermk;
	retur $?
	if [ $ret -ne 0 ]; then
		echo "Create backup user"
		scppassmk "/root/.ssh/id_rsa.pub $userdefault@$ip:/"
		sshpassmk "/user remove bkmk"
	    sshpassmk "/user add name=bkmk group=full password=randomkeyrandomkeyrandomkey comment=Usuario-Bkp disabled=no"
	    sshpassmk "/user ssh-keys  import  public-key-file=id_rsa.pub user=bkmk"
		testusermk;
		have_error $? "Error to create user " "User backup create at " "User"
		if [ $ret -eq 0 ]; then
	        capture_data
        fi
	else
		echo "Backup user was created $city"
        capture_data
	fi
}
capture_data(){
	modelo=$(sshmk "system routerboard print" | grep model | sed "s/.*: //");
	versao=$(sshmk "system resource print" | grep version | sed "s/.*: //; s/ (.*//");
	firmwareupgrade=$(sshmk "system routerboard print" | grep upgrade-firm | sed "s/.*: //");
	firmwarecurrent=$(sshmk "system routerboard print" | grep current-firm | sed "s/.*: //");
	echo "$versao		$firmwarecurrent/$firmwareupgrade	$modelo 	$ip		$city" >> /tmp/upgrade
	create_file
}
create_file(){
#	verify_key
	sshmk ":log warning \"BACKUP_SERVER_CONNECTED\""
	sshmk "/system backup save name=mikrotik"
	sshmk ":log warning \"BACKUP_CREATE\""
	sshmk "/export file=export"
	sshmk ":log warning \"EXPORT_CREATE\""
   	have_error $? "There was an error creating the MIKROTIK backup file for " "Successful creation of MIKROTIK backup file from"
    if [ $ret -eq 0 ]; then
        echo "Backup file from $city created"
			copy_file
	fi
}
##Command that copies the backup file to the backup machine.
copy_file
	if [ ! -d "$folder_destiny/$directory" ]; then
		echo "Create folder $folder_destiny/$directory"
		mkdir $folder_destiny/$directory
	fi
	scpmk ":/mikrotik.backup $folder_destiny/$directory/"
	sshmk ":log warning \"Copied server backup\""
	scpmk ":/export.rsc $folder_destiny/$directory/"
	sshmk ":log warning \"Exported server backup\""
	have_error $? "Error copy file backup from " "Success copied file backup from " "Copy" 
    if [ $ret -eq 0 ]; then
		remove_files
    fi
}
##Remove the backup file from mikrotik.
remove_files
	sshmk "/file remove mikrotik.backup"
	sshmk ":log warning \"Backup server removed file\""
	sshmk "/file remove export.rsc"
	sshmk ":log warning \"Backup server export file\""
	have_error $? "Error removing temporary mikrotik files " "Success removing temporary mikrotik files " "Removing"  
    if [ $ret -eq 0 ]; then
		rename_file
    fi
}
#
##Rename file backup
rename_file(){
	mv $folder_destiny/$directory/mikrotik.backup $folder_destiny/$directory/$city.backup
	have_error $? "Error rename backup from " "Success rename backup from " "rename backup"  
	mv $folder_destiny/$directory/export.rsc $folder_destiny/$directory/$city.rsc
	have_error $? "Error rename export from " "Success rename export from " "rename export"  
	if [ $ret -eq 0 ]; then
		run_update
    fi
}
### Functions remove olds logs.
exclude_olds() {
    echo "Delete logs before $days days ..."
    find $folder/log/ -not -name ".*" -type f -mtime +$days -exec  rm -v {} +
}
run_update(){
	# The flag y in the city list make update in the mikrotis
	echo "Update=$update_device"
	if [[ "$update_device" != "y" ]]; then
		sshmk ":log warning \"This server not needs update\""
		echo "Update not solicited for this equipament"
	else
		sshmk ":log warning \"This server needs update\""
		echo "Update solicited for this equipament"
		#Removed Lines commenteds
		grep -v "^#" $commands_update > commands_filtred
			while read CMD01; do
				sshmk "$CMD01"
			done < commands_filtred
	fi
}
### Reporte time used per router.
resumo() {
    x=0
    echo "SUMMARY OF BACKUP TIME BY MIKROTIK AND TOTAL TIME:"
    while read IP directory CIDADE; do
        x=$(($x+1))
        echo "TEMPO ${sync_time_[$x]}   BACKUP  $directory   $city"
    done < $folder/citys
    tempo $start_time $end_time && full_time=$temp
    echo "Total time:         $full_time"
}
#Remove temporary files
remove_tmps(){
#	echo "remove temporary files."
    rm -rf $folder/citys
	rm -rf $folder_destiny/*/mikrotik.backup
	#Change owner folder.
	chown -R mikrotik:mikrotik $folder_destiny/*
}
#Main Function
backup_mikrotik(){
	start_time=`date +%s`
	x=0
	echo Data: `date +%A', '%d/%m/%Y' '%X' '%Z`
    echo "================================================================================"
    echo "START BACKUPS MIKROTIKS ..."
	echo "================================================================================"
	echo > /tmp/servers
	echo ""
	grep -v "^#" $servers > $folder/citys
	cat $folder/citys | wc -l > /tmp/up
	export total_up=`cat /tmp/up`
		while read ip directory city update_device; do
			x=$(($x+1))
			echo ""
			echo "================================================================================"
			echo ""
	        echo "Run mikrotik backup from $city."
	        echo ""
			online
			if [ $up -eq 0 ]; then
				sync_ini_[$x]=`date +%s`
				verify_key $ip $directory $city
			    sync_end_[$x]=`date +%s`
				tempo ${sync_ini_[$x]} ${sync_end_[$x]} && sync_time_[$x]=$temp
				echo ""
				echo "Time used ${sync_time_[$x]}."
			else
			    errors=$(($errors+1))
				echo "Router inaccessible - Backup from $city does not run."
			        echo ""
				echo "================================================================================"
	                	echo ""
				echo "$ip $city offline" >> /tmp/servers
			fi
		done < $folder/citys
	exclude_olds
        echo ""
        echo "================================================================================"
        echo ""
        end_time=`date +%s`
        resumo
		echo ""
        echo "================================================================================"
	remove_tmps
        echo "TOTAL DE errors: $errors/$total_up"
        echo "--------------------------------------------------------------------------------"
        echo "Router have erros:"
        cat /tmp/servers
        echo "================================================================================"
        echo Data: `date +%A', '%d/%m/%Y' '%X' '%Z`
        echo ""
        echo $errors > /tmp/errors
}
backup_mikrotik
================================================

File: LICENSE
================================================
MIT License
Copyright (c) 2020 Jorge Dias
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
================================================

File: README.md
================================================
<h1 align="center">:rocket: Learn Shell: Make Mikrotik Backup :rocket:</h1>
<p align="center">
:us: Script for Backup and Update of Mikrotik in batches.
:brazil: Script para Backup e Update de Mikrotik em lotes.
</p>
<p align="center">
 <a href="#history">History</a> •
 <a href="#objective">Objective</a> •
 <a href="#technologies">Technologies</a> •
 <a href="#how-to-run">How to run the application</a>
</p>
<h1 id="history">:book: History</h1>
### :us: EN
The motivation to create this project came before I joined the CBMSC technology team, when I got there, there was already this script developed by ST Duwe to backup the emergency servers of the Fire Department of the State of Santa Catarina.
The backups of the mikrotiks equipment were made with scripts inside each router sending to an FTP or backup file, making maintenance of the backups difficult because it was necessary to enter each one to change some information, and when there were problems configuring backups on we didn't know.
With the collaboration of Sgt Leonardo when I was still working on the CBMSC network team, we remodeled this script to back up the mikrotik using an ssh key by running the commands in shellscript in a centralized location generating reports of all the backups, of those that worked and that had errors.
Some functions were improved over time, after the backup base was working we implemented the update function, so when it was necessary to update some mikrotik or just run a mass command it was only to point in the file which devices will be selected and in the other file which ones commands will be run.
I hope this script can help the linux community as it prepares me to understand the basics of shellscript.
### :brazil: BR
A motivação para criar esse projeto veio antes de eu entrar para a equipe de tecnologia do CBMSC, quando cheguei lá já existia esse script desenvolvido pelo ST Duwe para fazer backup dos servidores de emergência do Corpo de Bombeiros do Estado de Santa Catarina Brasil. 
Os backups dos equipamentos mikrotiks eram feitos com scripts dentro de cada roteador enviando para um FTP o arquivo de backup, deixando a manutenção dos backups difícil pois era necessário entrar em cada um deles para configurar ou alterar alguma informação, e quando dava problemas de backup nos não ficavamos sabendo. 
Com a colaboração do Sgt Leonardo quando eu ainda trabalhava na equipe de redes do CBMSC remodelamos esse script para fazer backup dos mikrotiks usando uma chave ssh rodando os comandos em shellscript em um local centralizado gerando relatório de todos os backups, dos que deram certos e os que apresentavam erros.
Algumas funções foram melhoradas ao longo do tempo, depois da base do backup estar funcionando implementamos a função de upgrade, para quando fosse necessário atualizar algum mikrotik ou apenas rodar um comando em massa era só apontar no arquivo quais aparelhos serão atualizados e no outro arquivo quais comandos serão rodados.
Espero que esse script possa ajudar a comunidade linux como me ajudou a entender os fundamentos de shellscript.
<h1 id="objective">:bulb: Objective</h1>
:us:
    - Create backup user into Routerboard
    - Connect with ssh key
    - Make dump Backup and Export file
    - Verify version Firmware and model
    - Run update commands.
    - Copy to server backup file
    - Send email report.
:brazil:
    - Criar usuário de backup na Routerboard
    - Conecte-se com a chave ssh
    - Fazer backup de despejo e exportar arquivo
    - Verifique a versão do firmware e modelo
    - Execute comandos de atualização.
    - Copiar para arquivo de backup do servidor
    - Enviar relatório por email.
</p>
<h1 id="technologies">:rocket: Technologies</h1>
<p>It was used these technologies in this job.</p>
- [Shell](https://en.wikipedia.org/wiki/Shell_script "shell")
- [Sendmail](http://expressjs.com/ "Sendmail")
<h1 id="how-to-run">:computer: How to run the application</h1>
<h2>Pre Requirements</h2>
<h4>You will need these tools instaled in your machine:</h4>
- [Linux](https://www.linux.com/what-is-linux/ "Linux")
- [Sendmail](https://help.dreamhost.com/hc/en-us/articles/216687518-How-do-I-use-Sendmail "Sendmail")
- [sshpass](https://www.cyberciti.biz/faq/noninteractive-shell-script-ssh-password-provider/ "sshpass")
```bash
# Clone this repository
$ git clone git@github.com:jorgediasdsg/mikrotik-backup-update.git
# Go into the folder of the project
$ cd mikrotik-backup-update
# edit enviroments **Important!**
$ vim bkmk
# edit list routers **Important!**
$ vim bkmk.cid
# edit list commands update
$ vim bkmk.update
#If you want to run the project
/bin/bash bkmk
```
<hr>
@jorgediasdsg 2020
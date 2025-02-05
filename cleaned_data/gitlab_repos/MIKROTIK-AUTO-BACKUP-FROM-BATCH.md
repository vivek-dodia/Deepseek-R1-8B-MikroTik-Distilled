# Repository Information
Name: MIKROTIK-AUTO-BACKUP-FROM-BATCH

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
	url = https://gitlab.com/buananetpbun/MIKROTIK-AUTO-BACKUP-FROM-BATCH.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: MIKROTIK BACKUP.bat
================================================
@echo off
:: Set username and password mikrotik (with full access)
set user=admin
set pass=12345
set ip=192.168.10.1 (ip gateway)
:: Window Attributes
title EASY BACKUP MIKROTIK
mode CON: cols=55 lines=22
:: Menu
echo.
echo  ================================================
echo  EASY BACKUP MIKROTIK FROM BATCH	
echo  ================================================
echo  By: Buananet SECURE! 2019
echo  fb.com/buananet.pbun
echo  ------------------------------------------------
echo.
:: Input File Name
echo Enter File Name For Backup (without space):
set /p name="File Name = " 
:: mikrotik script
echo /system backup save name=%name%>script.backup.rsc
:: ftp commands to upload script
echo user %user%> ftp.dat
echo %pass%>> ftp.dat
echo put script.backup.rsc>> ftp.dat
echo quit>> ftp.dat
:: upload script
ftp -n -s:ftp.dat %ip%> NUL
echo.
echo  *** Backup %name%.backup on mikrotik done!
echo.
:: Question backup to PC
echo Are you sure backup to local computer?
choice /c YN
if %errorlevel%==1 goto yes
if %errorlevel%==2 goto no
:yes
echo user %user%> ftp.dat
echo %pass%>> ftp.dat
echo get %name%.backup>> ftp.dat
echo quit>> ftp.dat
:: upload script
ftp -n -s:ftp.dat %ip%> NUL
echo.
echo  *** Backup and Download %name%.backup on PC done!
echo.
:: cleanup
del /q ftp.dat
del /q script.backup.rsc
echo.&pause&goto:eof
:no
:: cleanup
del /q ftp.dat
del /q script.backup.rsc
echo.&pause&goto:eof
================================================

File: README.md
================================================
# MIKROTIK AUTO BACKUP FROM BATCH
Easy backup mikrotik (.backup) only use BATCH Windows
![image](https://user-images.githubusercontent.com/42666125/111258702-143d4f00-8650-11eb-912c-f67ed77ddc8a.png)
<pre  style="font-family:arial;font-size:12px;border:1px dashed #CCCCCC;width:99%;height:auto;overflow:auto;background:#f0f0f0;;background-image:URL(http://2.bp.blogspot.com/_z5ltvMQPaa8/SjJXr_U2YBI/AAAAAAAAAAM/46OqEP32CJ8/s320/codebg.gif);padding:0px;color:#000000;text-align:left;line-height:20px;"><code style="color:#000000;word-wrap:normal;"> @echo off  
 :: Set username and password mikrotik (with full access)  
 set user=admin  
 set pass=12345  
 set ip=192.168.10.1 (ip gateway)  
 :: Window Attributes  
 title EASY BACKUP MIKROTIK  
 mode CON: cols=55 lines=22  
 :: Menu  
 echo.  
 echo ================================================  
 echo EASY BACKUP MIKROTIK FROM BATCH       
 echo ================================================  
 echo By: Buananet SECURE! 2019  
 echo fb.com/buananet.pangkalanbun  
 echo ------------------------------------------------  
 echo.  
 :: Input File Name  
 echo Enter File Name For Backup (without space):  
 set /p name="File Name = "   
 :: mikrotik script  
 echo /system backup save name=%name%&gt;script.backup.rsc  
 :: ftp commands to upload script  
 echo user %user%&gt; ftp.dat  
 echo %pass%&gt;&gt; ftp.dat  
 echo put script.backup.rsc&gt;&gt; ftp.dat  
 echo quit&gt;&gt; ftp.dat  
 :: upload script  
 ftp -n -s:ftp.dat %ip%&gt; NUL  
 echo.  
 echo *** Backup %name%.backup on mikrotik done!  
 echo.  
 :: Question backup to PC  
 echo Are you sure backup to local computer?  
 choice /c YN  
 if %errorlevel%==1 goto yes  
 if %errorlevel%==2 goto no  
 :yes  
 echo user %user%&gt; ftp.dat  
 echo %pass%&gt;&gt; ftp.dat  
 echo get %name%.backup&gt;&gt; ftp.dat  
 echo quit&gt;&gt; ftp.dat  
 :: upload script  
 ftp -n -s:ftp.dat %ip%&gt; NUL  
 echo.  
 echo *** Backup and Download %name%.backup on PC done!  
 echo.  
 :: cleanup  
 del /q ftp.dat  
 del /q script.backup.rsc  
 echo.&amp;pause&amp;goto:eof  
 :no  
 :: cleanup  
 del /q ftp.dat  
 del /q script.backup.rsc  
 echo.&amp;pause&amp;goto:eof  
</code></pre>
<img style="float:right; padding-top:10px" src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fbuananetpbun.github.io%2F&count_bg=%23C83D3D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false" alt="Hits"/>
# Repository Information
Name: mikrotik-port-scanner

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
	url = https://gitlab.com/buananetpbun/mikrotik-port-scanner.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: Mikrotik-Port-Scan-fix-v2.bat
================================================
@echo off
title ROUTEROS PORT TESTER BY BNT
:Loop 
echo.
echo =================================
echo -= ROUTEROS PORT TESTER BY BNT =-
echo =================================
echo.
set /p ip="Enter IP Address: "
echo.
echo PORT INFO:
echo - 8291 / Winbox
echo - 80   / WWW Webfig http
echo - 443  / WWW-SSL Webfig https
echo - 8728 / API
echo - 8729 / API-SSL
echo - 21   / FTP
echo - 22   / SSH
echo - 23   / Telnet
echo - 3128 / Open proxy
echo - 8080 / Open proxy
echo - 53   / DNS
echo - 2000 / Btest Server
echo.
echo Try for Scaning Port Please Wait...
echo.
PortCheck %ip% 8291,80,443,8728,8729,21,22,23,3128,8080,53,2000
echo.
IF %ERRORLEVEL%==1 echo - WARNING!! Open ports found, danger from attack!
echo - Please change your default port to another port
echo. 
echo Scan Port Complete..
echo.
pause
cls
goto loop
================================================

File: PortCheck.exe.config
================================================
<?xml version="1.0" encoding="utf-8"?>
<configuration>
    <startup> 
        <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0"/>
        <supportedRuntime version="v2.0.50727"/>
    </startup>
</configuration>
================================================

File: README.md
================================================
# MIKROTIK PORT SCANNER / ROUTER OS PORT TESTER
Just a simple test for routeros port scanning
![image](https://user-images.githubusercontent.com/42666125/111259079-d42a9c00-8650-11eb-8f48-6385aad0d1ab.png)
<pre>
@echo off
title ROUTEROS PORT TESTER BY BNT
:Loop 
echo.
echo =================================
echo -= ROUTEROS PORT TESTER BY BNT =-
echo =================================
echo.
set /p ip="Enter IP Address: "
echo.
echo PORT INFO:
echo - 8291 / Winbox
echo - 80   / WWW Webfig http
echo - 443  / WWW-SSL Webfig https
echo - 8728 / API
echo - 8729 / API-SSL
echo - 21   / FTP
echo - 22   / SSH
echo - 23   / Telnet
echo - 3128 / Open proxy
echo - 8080 / Open proxy
echo - 53   / DNS
echo - 2000 / Btest Server
echo.
echo Try for Scaning Port Please Wait...
echo.
PortCheck %ip% 8291,80,443,8728,8729,21,22,23,3128,8080,53,2000
echo.
IF %ERRORLEVEL%==1 echo - WARNING!! Open ports found, danger from attack!
echo - Please change your default port to another port
echo. 
echo Scan Port Complete..
echo.
pause
cls
goto loop
</pre>
Credit for: http://www.portcheck-tool.com
<img style="float:right; padding-top:10px" src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fbuananetpbun.github.io%2F&count_bg=%23C83D3D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false" alt="Hits"/>
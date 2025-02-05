# Repository Information
Name: hotspot-api

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
	url = https://gitlab.com/koroses/hotspot-api.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: login.css
================================================
body {
padding:0;margin:0 auto;
    background:#ECEFF1;
    position:relative;
    top: -35px;
}
#head{
    display: block;
    background: #2563ea
;
    width: 100%;
    height: 230px;
    position:relative;
    top:-37px;
    z-index: 1;
}
#logo{
position: relative;
    top:0px;
}
legend{
    position:relative;
    top:0px;
    color:#a9a9a9;
    font-size: 20px;
    font-family:sans-serif;
}
#box{
    position:relative;
    top:-181px;
	width:90%;
	max-width:650px;
	height:580px;	
	background-color:rgba(255,255,255,1);
	border-radius:2px;
	padding:20px 0 0 0;
	margin:0px auto;
    z-index: 2;
}
#userdiv
{
    background: #ffffff url(logo.png) no-repeat center;
    width: 200px;
    height: 200px;
    margin: 5px;
}
/**------------USER------------**/
#user{
border:0px #ccc solid;
    border-bottom:1px #ccc solid; color:#212121;background:rgba(255,255,255,0.1);opacity: 1;
height:40px;font-size:16px;
/* display:block;width:230px; */
text-align:right;border-radius:0px;
font-family:inherit;outline: none;
}
/**--------------------PASSWORD----------**/
#pass{
    border:0px #ccc solid;
    border-bottom:1px #ccc solid;
    color:#212121;background:rgba(255,255,255,0.1);opacity: 1;height:40px;font-size:16px;
display:block;margin:5px;width:230px;text-align:center;border-radius:0px;font-family:inherit;outline: none;
}
/*---------------Boton---------*/
#boton{
	-webkit-appearance:none;color:#fff;
	background:#2563ea; background-image:url(lock.png);
	background-repeat: no-repeat; background-position:center; opacity: 1;
    border:none;border-radius:5px;height:42px;width:234px;font-size:16px;font-weight:400;outline:0;text-transform:uppercase;
    letter-spacing:1.5px;cursor:pointer
    }
#boton:hover{
	background-color:#1521c5;-webkit-transition:all 0.3s ease;-moz-transition:all 0.3s ease;-o-transition:all 0.3s ease;transition:all 0.3s ease
	}
    .vertical-form .footer{
        position: relative;
        top:-100px;
        text-align:center;
color:#ccc;}
.vertical-form .footer a{text-decoration:none;color:#1521c5;}
    @media (max-width:450px){
       }
/*-----------------button------------*/
#button{
    text-align: center;
	-webkit-appearance:none;color:#fff;
	background:#2563ea;
	background-repeat: no-repeat; background-position:center; opacity: 1;
    border:none;border-radius:5px;height:42px;width:234px;font-size:16px;font-weight:400;outline:0;text-transform:uppercase;
    letter-spacing:1.5px;cursor:pointer
    }
#button:hover{
    background-color:#2563ea;-webkit-transition:all 0.3s ease;-moz-transition:all 0.3s ease;-o-transition:all 0.3s ease;transition:all 0.3s ease
    }
================================================

File: README.md
================================================
# Hotspot API
So confuse what i've to name it. After all, here we go 'Hotspot API' written on PHP with [PHPMailer](https://github.com/PHPMailer/PHPMailer) 
for send the credential to user, and [Pear2/Net_RouterOS](https://github.com/pear2/Net_RouterOS) for communicate with 
MikroTik RouterOS API Protocol.
Back to the day that my office ran into connection issue that our Developer can't have stable and good internet connection via our wifi. 
After receive feedback from all of collegues, then i propose a solution with MikroTik for Bandwith management and Hotspot server for overcome.
Comes to my plan that we have a dozens employee here, it's time cosuming if we have to register one by one employee for their hotspot credential and so on.
Definitely we have to provide an apps so my collegues can get their credential by them self, and do a Change password account, Reset password if forgot.
Hopefully it can help you too if you have same circumstances on your environment
## Make it Work!
To have all work as expected you have to set the configuration precisely, below is the mandatory configuration that you have to take a look at.
1. Make sure you have a Server PC/Any Device that can host as PHP Server (MikroTik Can't do that), so make sure you have a Server that available
when it's needed.
2. The Device that host the PHP apps must connect to the router. You can make it via Wired Connection using LAN Cable or from Hotspot it self.
3. You must have a API User that can login to your MikroTik API interface from the host machine.
4. Make sure API service is allowed to access from the host PHP machine to the MikroTik Router.
5. Set a passthrough configuration on your firewall that make the router send a request with the real IP of client, so i change from masquerade rule 
for hotspot network to passthrough.
6. Add the ip of the host server (ip on the router network) to walled garden ip list so the un-authenticate user can access the apps from hotspot network 
(you can also add the email host of your email server, so the employee not have to switch to other connection for accessing their email).
7. If you use AP's for delivering the connection to client, dont forget to use a bridge network so your AP's not act masquerading the network.
That's all you have to concern about the configuration, if you have an issue regarding to your deployment you can contact me on [my linkedin](www.linkedin.com/in/fahri-noer). and Thank you!
================================================

File: index.html
================================================
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Reset Hotspot Password</title>
<meta http-equiv="pragma" content="no-cache" />
<meta http-equiv="expires" content="-1" />	
<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0; user-scalable=0" />
<link rel="icon" href="logo.png"/>
<link rel="stylesheet" href="login.css" media="screen">
</head>
<body class='login'>
<form class="vertical-form" name="login" action="./reset.php" method="post" background="#A03472">
<div style="margin:0;padding:50;display:inline"></div>
<center>
    <div id="head">
    </div>
<div id="box">
    <div id="userdiv"> </div>
    <legend>
    <p>Reset hotspot password</p>
    </legend>
<div><input id="user" autocomplete="on" name="email" type="text" placeholder="Email"/><label>@ist.id</label></div>
<br>
<div><input id="button" name="submit" type="submit" value="Reset" /></div>
</div>
</center>
</form>
</body>
</html>
================================================

File: login.css
================================================
body {
padding:0;margin:0 auto;
    background:#ECEFF1;
    position:relative;
    top: -35px;
}
#head{
    display: block;
    background: #2563ea
;
    width: 100%;
    height: 230px;
    position:relative;
    top:-37px;
    z-index: 1;
}
#logo{
position: relative;
    top:0px;
}
legend{
    position:relative;
    top:0px;
    color:#a9a9a9;
    font-size: 20px;
    font-family:sans-serif;
}
#box{
    position:relative;
    top:-181px;
	width:90%;
	max-width:650px;
	height:580px;	
	background-color:rgba(255,255,255,1);
	border-radius:2px;
	padding:20px 0 0 0;
	margin:0px auto;
    z-index: 2;
}
#userdiv
{
    background: #ffffff url(logo.png) no-repeat center;
    width: 200px;
    height: 200px;
    margin: 5px;
}
/**------------USER------------**/
#user{
border:0px #ccc solid;
    border-bottom:1px #ccc solid; color:#212121;background:rgba(255,255,255,0.1);opacity: 1;
height:40px;font-size:16px;
/* display:block;width:230px; */
text-align:right;border-radius:0px;
font-family:inherit;outline: none;
}
/**--------------------PASSWORD----------**/
#pass{
    border:0px #ccc solid;
    border-bottom:1px #ccc solid;
    color:#212121;background:rgba(255,255,255,0.1);opacity: 1;height:40px;font-size:16px;
display:block;margin:5px;width:230px;text-align:center;border-radius:0px;font-family:inherit;outline: none;
}
/*---------------Boton---------*/
#boton{
	-webkit-appearance:none;color:#fff;
	background:#2563ea; background-image:url(lock.png);
	background-repeat: no-repeat; background-position:center; opacity: 1;
    border:none;border-radius:5px;height:42px;width:234px;font-size:16px;font-weight:400;outline:0;text-transform:uppercase;
    letter-spacing:1.5px;cursor:pointer
    }
#boton:hover{
	background-color:#1521c5;-webkit-transition:all 0.3s ease;-moz-transition:all 0.3s ease;-o-transition:all 0.3s ease;transition:all 0.3s ease
	}
    .vertical-form .footer{
        position: relative;
        top:-100px;
        text-align:center;
color:#ccc;}
.vertical-form .footer a{text-decoration:none;color:#1521c5;}
    @media (max-width:450px){
       }
/*-----------------button------------*/
#button{
    text-align: center;
	-webkit-appearance:none;color:#fff;
	background:#2563ea;
	background-repeat: no-repeat; background-position:center; opacity: 1;
    border:none;border-radius:5px;height:42px;width:234px;font-size:16px;font-weight:400;outline:0;text-transform:uppercase;
    letter-spacing:1.5px;cursor:pointer
    }
#button:hover{
    background-color:#2563ea;-webkit-transition:all 0.3s ease;-moz-transition:all 0.3s ease;-o-transition:all 0.3s ease;transition:all 0.3s ease
    }
================================================

File: index.html
================================================
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Sign Up Hotspot</title>
<meta http-equiv="pragma" content="no-cache" />
<meta http-equiv="expires" content="-1" />	
<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0; user-scalable=0" />
<link rel="icon" href="logo.png"/>
<link rel="stylesheet" href="login.css" media="screen">
</head>
<body class='login'>
<form class="vertical-form" name="login" action="./signup.php" method="post" background="#A03472">
<div style="margin:0;padding:50;display:inline"></div>
<center>
    <div id="head">
    </div>
<div id="box">
    <div id="userdiv"> </div>
    <legend>
    <p>Get Access</p>
    </legend>
<div><input id="user" autocomplete="on" name="email" type="text" placeholder="Email"/><label>@ist.id</label></div>
<br>
<div><input id="button" name="signup" type="submit" value="Get Access" /></div>
</div>
</center>
</form>
</body>
</html>
================================================

File: login.css
================================================
body {
padding:0;margin:0 auto;
    background:#ECEFF1;
    position:relative;
    top: -35px;
}
#head{
    display: block;
    background: #2563ea
;
    width: 100%;
    height: 230px;
    position:relative;
    top:-37px;
    z-index: 1;
}
#logo{
position: relative;
    top:0px;
}
legend{
    position:relative;
    top:0px;
    color:#a9a9a9;
    font-size: 20px;
    font-family:sans-serif;
}
#box{
    position:relative;
    top:-181px;
	width:90%;
	max-width:650px;
	height:580px;	
	background-color:rgba(255,255,255,1);
	border-radius:2px;
	padding:20px 0 0 0;
	margin:0px auto;
    z-index: 2;
}
#userdiv
{
    background: #ffffff url(logo.png) no-repeat center;
    width: 200px;
    height: 200px;
    margin: 5px;
}
/**------------USER------------**/
#user{
border:0px #ccc solid;
    border-bottom:1px #ccc solid; color:#212121;background:rgba(255,255,255,0.1);opacity: 1;
height:40px;font-size:16px;
/* display:block;width:230px; */
text-align:right;border-radius:0px;
font-family:inherit;outline: none;
}
/**--------------------PASSWORD----------**/
#pass{
    border:0px #ccc solid;
    border-bottom:1px #ccc solid;
    color:#212121;background:rgba(255,255,255,0.1);opacity: 1;height:40px;font-size:16px;
display:block;margin:5px;width:230px;text-align:center;border-radius:0px;font-family:inherit;outline: none;
}
/*---------------Boton---------*/
#boton{
	-webkit-appearance:none;color:#fff;
	background:#2563ea; background-image:url(lock.png);
	background-repeat: no-repeat; background-position:center; opacity: 1;
    border:none;border-radius:5px;height:42px;width:234px;font-size:16px;font-weight:400;outline:0;text-transform:uppercase;
    letter-spacing:1.5px;cursor:pointer
    }
#boton:hover{
	background-color:#1521c5;-webkit-transition:all 0.3s ease;-moz-transition:all 0.3s ease;-o-transition:all 0.3s ease;transition:all 0.3s ease
	}
    .vertical-form .footer{
        position: relative;
        top:-100px;
        text-align:center;
color:#ccc;}
.vertical-form .footer a{text-decoration:none;color:#1521c5;}
    @media (max-width:450px){
       }
/*-----------------button------------*/
#button{
    text-align: center;
	-webkit-appearance:none;color:#fff;
	background:#2563ea;
	background-repeat: no-repeat; background-position:center; opacity: 1;
    border:none;border-radius:5px;height:42px;width:234px;font-size:16px;font-weight:400;outline:0;text-transform:uppercase;
    letter-spacing:1.5px;cursor:pointer
    }
#button:hover{
    background-color:#2563ea;-webkit-transition:all 0.3s ease;-moz-transition:all 0.3s ease;-o-transition:all 0.3s ease;transition:all 0.3s ease
    }
================================================

File: installed.json
================================================
[
    {
        "name": "pear2/cache_shm",
        "version": "0.2.0",
        "version_normalized": "0.2.0.0",
        "source": {
            "type": "git",
            "url": "https://github.com/pear2/Cache_SHM.git",
            "reference": "1de608d1b59df5ba55172ba727b1da581e1497eb"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/pear2/Cache_SHM/zipball/1de608d1b59df5ba55172ba727b1da581e1497eb",
            "reference": "1de608d1b59df5ba55172ba727b1da581e1497eb",
            "shasum": ""
        },
        "require": {
            "php": ">=5.3.9"
        },
        "suggest": {
            "ext-apc": ">=5.0.0",
            "ext-wincache": ">=1.1.0"
        },
        "time": "2016-11-07T02:09:36+00:00",
        "type": "library",
        "installation-source": "dist",
        "autoload": {
            "psr-0": {
                "PEAR2\\Cache\\SHM": "src/"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "LGPL-2.1"
        ],
        "authors": [
            {
                "name": "Vasil Rangelov",
                "email": "boen.robot@gmail.com",
                "role": "lead"
            }
        ],
        "description": "Wrapper for shared memory and locking functionality across different PHP extensions.",
        "homepage": "http://pear2.github.com/Cache_SHM/",
        "keywords": [
            "abstraction",
            "apc",
            "cache",
            "caching",
            "lock",
            "locking",
            "pear2",
            "shm",
            "wincache"
        ]
    },
    {
        "name": "pear2/net_routeros",
        "version": "dev-develop",
        "version_normalized": "dev-develop",
        "source": {
            "type": "git",
            "url": "https://github.com/pear2/Net_RouterOS.git",
            "reference": "a03e1ce5cbd5537d4f8a6dd32d6ca54ae94f43e8"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/pear2/Net_RouterOS/zipball/a03e1ce5cbd5537d4f8a6dd32d6ca54ae94f43e8",
            "reference": "a03e1ce5cbd5537d4f8a6dd32d6ca54ae94f43e8",
            "shasum": ""
        },
        "require": {
            "pear2/net_transmitter": ">=1.0.0b1 || dev-develop@dev",
            "php": ">=5.3.0"
        },
        "require-dev": {
            "ext-iconv": "*",
            "pear2/cache_shm": "dev-develop",
            "pear2/console_color": "dev-develop",
            "pear2/console_commandline": "dev-master",
            "pear2/net_transmitter": "dev-develop@dev",
            "phpunit/phpunit": "^5.0.0",
            "phpunit/phpunit-mock-objects": "^3.4.0",
            "squizlabs/php_codesniffer": "@stable"
        },
        "suggest": {
            "ext-apc": "This, APCu or Wincache is required for persistent connections.",
            "ext-apcu": "This, APC or Wincache is required for persistent connections.",
            "ext-iconv": "Used for charset conversion",
            "ext-openssl": "Enables encrypted connections.",
            "ext-wincache": "This, APC or APCu is required for persistent connections. Reccomended for Windows.",
            "pear2/cache_shm": "Enables persistent connections.",
            "pear2/console_color": "Enables colors in the console",
            "pear2/console_commandline": "Enables the console"
        },
        "time": "2019-10-19T20:11:15+00:00",
        "bin": [
            "scripts/roscon.php"
        ],
        "type": "library",
        "installation-source": "dist",
        "autoload": {
            "psr-0": {
                "PEAR2\\Net\\RouterOS\\": "src/",
                "PEAR2\\Net\\Transmitter\\": "vendor/pear2/net_transmitter/src/",
                "PEAR2\\Cache\\SHM": "vendor/pear2/cache_shm/src/",
                "PEAR2\\Console\\Color": "vendor/pear2/console_color/src/"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "LGPL-2.1-only"
        ],
        "authors": [
            {
                "name": "Vasil Rangelov",
                "email": "boen.robot@gmail.com",
                "role": "lead"
            }
        ],
        "description": "This package allows you to read and write information from a RouterOS host using MikroTik's RouterOS API.",
        "homepage": "http://pear2.github.com/Net_RouterOS/",
        "keywords": [
            "api",
            "mikrotik",
            "package",
            "pear2",
            "router",
            "routeros"
        ]
    },
    {
        "name": "pear2/net_transmitter",
        "version": "1.0.0b1",
        "version_normalized": "1.0.0.0-beta1",
        "source": {
            "type": "git",
            "url": "https://github.com/pear2/Net_Transmitter.git",
            "reference": "461564b18b7245f05dea80d943d2b87eb6a5de5e"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/pear2/Net_Transmitter/zipball/461564b18b7245f05dea80d943d2b87eb6a5de5e",
            "reference": "461564b18b7245f05dea80d943d2b87eb6a5de5e",
            "shasum": ""
        },
        "require": {
            "php": ">=5.3.0"
        },
        "require-dev": {
            "phpunit/phpunit": "@stable"
        },
        "suggest": {
            "ext-apc": "This, APCu or Wincache is required for persistent connections.",
            "ext-apcu": "This, APC or Wincache is required for persistent connections.",
            "ext-openssl": "Enables encrypted connections.",
            "ext-wincache": "This, APC or APCu is required for persistent connections. Reccomended for Windows.",
            "pear2/cache_shm": "Enables persistent connections"
        },
        "time": "2016-11-07T02:15:19+00:00",
        "type": "library",
        "installation-source": "dist",
        "autoload": {
            "psr-0": {
                "PEAR2\\Net\\Transmitter\\": "src/"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "LGPL-2.1"
        ],
        "authors": [
            {
                "name": "Vasil Rangelov",
                "email": "boen.robot@gmail.com",
                "role": "lead"
            }
        ],
        "description": "A stream wrapper that ensures data integrity. Particularly useful for sockets.",
        "homepage": "http://pear2.github.com/Net_Transmitter/",
        "keywords": [
            "Socket",
            "integrity",
            "network",
            "networking",
            "package",
            "pear2",
            "sockets"
        ]
    },
    {
        "name": "phpmailer/phpmailer",
        "version": "v6.1.7",
        "version_normalized": "6.1.7.0",
        "source": {
            "type": "git",
            "url": "https://github.com/PHPMailer/PHPMailer.git",
            "reference": "2c2370ba3df7034f9eb7b8f387c97b52b2ba5ad0"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/PHPMailer/PHPMailer/zipball/2c2370ba3df7034f9eb7b8f387c97b52b2ba5ad0",
            "reference": "2c2370ba3df7034f9eb7b8f387c97b52b2ba5ad0",
            "shasum": ""
        },
        "require": {
            "ext-ctype": "*",
            "ext-filter": "*",
            "php": ">=5.5.0"
        },
        "require-dev": {
            "doctrine/annotations": "^1.2",
            "friendsofphp/php-cs-fixer": "^2.2",
            "phpunit/phpunit": "^4.8 || ^5.7"
        },
        "suggest": {
            "ext-mbstring": "Needed to send email in multibyte encoding charset",
            "hayageek/oauth2-yahoo": "Needed for Yahoo XOAUTH2 authentication",
            "league/oauth2-google": "Needed for Google XOAUTH2 authentication",
            "psr/log": "For optional PSR-3 debug logging",
            "stevenmaguire/oauth2-microsoft": "Needed for Microsoft XOAUTH2 authentication",
            "symfony/polyfill-mbstring": "To support UTF-8 if the Mbstring PHP extension is not enabled (^1.2)"
        },
        "time": "2020-07-14T18:50:27+00:00",
        "type": "library",
        "installation-source": "dist",
        "autoload": {
            "psr-4": {
                "PHPMailer\\PHPMailer\\": "src/"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "LGPL-2.1-only"
        ],
        "authors": [
            {
                "name": "Marcus Bointon",
                "email": "phpmailer@synchromedia.co.uk"
            },
            {
                "name": "Jim Jagielski",
                "email": "jimjag@gmail.com"
            },
            {
                "name": "Andy Prevost",
                "email": "codeworxtech@users.sourceforge.net"
            },
            {
                "name": "Brent R. Matzelle"
            }
        ],
        "description": "PHPMailer is a full-featured email creation and transfer class for PHP",
        "funding": [
            {
                "url": "https://github.com/synchro",
                "type": "github"
            }
        ]
    }
]
================================================

File: LICENSE
================================================
Copyright (c) Nils Adermann, Jordi Boggiano
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
================================================

File: .scrutinizer.yml
================================================
imports:
    - php
inherit: true
tools:
    php_sim: false
    php_cpd: true
    php_code_sniffer:
        config:
            standard: PEAR
================================================

File: composer.json
================================================
{
    "name": "pear2/cache_shm",
    "description": "Wrapper for shared memory and locking functionality across different PHP extensions.",
    "keywords": ["abstraction", "lock", "shm", "apc", "pear2", "cache", "wincache", "caching", "locking"],
    "homepage": "http://pear2.github.com/Cache_SHM/",
    "license": "LGPL-2.1",
    "authors": [
        {
            "name": "Vasil Rangelov",
            "email": "boen.robot@gmail.com",
            "role": "lead"
        }
    ],
    "support": {
        "issues": "http://github.com/pear2/Cache_SHM/issues",
        "wiki": "http://github.com/pear2/Cache_SHM/wiki"
    },
    "require": {
        "php": ">=5.3.9"
    },
    "suggest": {
        "ext-apc": ">=3.1.1",
        "ext-apc": ">=5.0.0",
        "ext-wincache": ">=1.1.0"
    },
    "autoload": {
        "psr-0": {
            "PEAR2\\Cache\\SHM": "src/"
        }
    }
}
================================================

File: apigen.neon
================================================
title: PEAR2_Cache_SHM documentation
source:
  - ../src
destination: Reference/ApiGen/Doc
extensions:
  - php
charset:
  - UTF-8
accessLevels:
  - public
tree: true
================================================

File: README
================================================
Wrapper for shared memory and locking functionality across different extensions.
Allows you to share data across requests as long as the PHP process is running. One of APC or WinCache is required to accomplish this, with other extensions being potentially pluggable as adapters.
================================================

File: README.md
================================================
See the project wiki for installation instructions and other documentation.
The sources as visible here reflect the development version. They may contain parsing errors, fail to install or have all other sorts of errors. If you want to use this package, download the packaged archives instead.
================================================

File: composer.json
================================================
{
    "name": "pear2/net_routeros",
    "description": "This package allows you to read and write information from a RouterOS host using MikroTik's RouterOS API.",
    "keywords": ["routeros", "package", "api", "mikrotik", "pear2", "router"],
    "homepage": "http://pear2.github.com/Net_RouterOS/",
    "license": "LGPL-2.1-only",
    "authors": [
        {
            "name": "Vasil Rangelov",
            "email": "boen.robot@gmail.com",
            "role": "lead"
        }
    ],
    "support": {
        "issues": "https://github.com/pear2/Net_RouterOS/issues",
        "wiki": "https://github.com/pear2/Net_RouterOS/wiki"
    },
    "require": {
        "php": ">=5.3.0",
        "pear2/net_transmitter": ">=1.0.0b1 || dev-develop@dev"
    },
    "require-dev": {
        "ext-iconv": "*",
        "phpunit/phpunit": "^5.0.0",
        "phpunit/phpunit-mock-objects": "^3.4.0",
        "squizlabs/php_codesniffer": "@stable",
        "pear2/net_transmitter": "dev-develop@dev",
        "pear2/cache_shm": "dev-develop",
        "pear2/console_commandline": "dev-master",
        "pear2/console_color": "dev-develop"
    },
    "suggest": {
        "pear2/cache_shm": "Enables persistent connections.",
        "pear2/console_commandline": "Enables the console",
        "pear2/console_color": "Enables colors in the console",
        "ext-iconv": "Used for charset conversion",
        "ext-apc": "This, APCu or Wincache is required for persistent connections.",
        "ext-apcu": "This, APC or Wincache is required for persistent connections.",
        "ext-wincache": "This, APC or APCu is required for persistent connections. Reccomended for Windows.",
        "ext-openssl": "Enables encrypted connections."
    },
    "autoload": {
        "psr-0": {
            "PEAR2\\Net\\RouterOS\\": "src/",
            "PEAR2\\Net\\Transmitter\\": "vendor/pear2/net_transmitter/src/",
            "PEAR2\\Cache\\SHM": "vendor/pear2/cache_shm/src/",
            "PEAR2\\Console\\Color": "vendor/pear2/console_color/src/"
        }
    },
    "bin": ["scripts/roscon.php"]
}
================================================

File: RouterErrorException.php
================================================
<?php
/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;
/**
 * Base of this class.
 */
use RuntimeException;
/**
 * Refered to in the constructor.
 */
use Exception as E;
/**
 * Exception thrown by higher level classes (Util, etc.) when the router
 * returns an error.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class RouterErrorException extends RuntimeException implements Exception
{
    const CODE_ITEM_ERROR           = 0x100000;
    const CODE_SCRIPT_ERROR         = 0x200000;
    const CODE_READ_ERROR           = 0x010000;
    const CODE_WRITE_ERROR          = 0x020000;
    const CODE_EXEC_ERROR           = 0x040000;
    const CODE_CACHE_ERROR          = 0x100001;
    const CODE_GET_ERROR            = 0x110001;
    const CODE_GET_LOOKUP_ERROR     = 0x130001;
    const CODE_GETALL_ERROR         = 0x110002;
    const CODE_ADD_ERROR            = 0x120001;
    const CODE_SET_ERROR            = 0x120002;
    const CODE_REMOVE_ERROR         = 0x120004;
    const CODE_ENABLE_ERROR         = 0x120012;
    const CODE_DISABLE_ERROR        = 0x120022;
    const CODE_COMMENT_ERROR        = 0x120042;
    const CODE_UNSET_ERROR          = 0x120082;
    const CODE_MOVE_ERROR           = 0x120107;
    const CODE_SCRIPT_ADD_ERROR     = 0x220001;
    const CODE_SCRIPT_REMOVE_ERROR  = 0x220004;
    const CODE_SCRIPT_RUN_ERROR     = 0x240001;
    const CODE_SCRIPT_FILE_ERROR    = 0x240003;
    /**
     * The complete response returned by the router.
     *
     * NULL when the router was not contacted at all.
     *
     * @var ResponseCollection|null
     */
    private $_responses = null;
    /**
     * Creates a new RouterErrorException.
     *
     * @param string                  $message   The Exception message to throw.
     * @param int                     $code      The Exception code.
     * @param E|null                  $previous  The previous exception used for
     *     the exception chaining.
     * @param ResponseCollection|null $responses The complete set responses
     *     returned by the router.
     */
    public function __construct(
        $message,
        $code = 0,
        E $previous = null,
        ResponseCollection $responses = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->_responses = $responses;
    }
    /**
     * Gets the complete set responses returned by the router.
     *
     * @return ResponseCollection|null The complete set responses
     *     returned by the router.
     */
    public function getResponses()
    {
        return $this->_responses;
    }
    // @codeCoverageIgnoreStart
    // String representation is not reliable in testing
    /**
     * Returns a string representation of the exception.
     *
     * @return string The exception as a string.
     */
    public function __toString()
    {
        $result = parent::__toString();
        if ($this->_responses instanceof ResponseCollection) {
            $result .= "\nResponse collection:\n" .
                print_r($this->_responses->toArray(), true);
        }
        return $result;
    }
    // @codeCoverageIgnoreEnd
}
================================================

File: Script.php
================================================
<?php
/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;
/**
 * Values at {@link Script::escapeValue()} can be casted from this type.
 */
use DateTime;
/**
 * Values at {@link Script::escapeValue()} can be casted from this type.
 */
use DateInterval;
/**
 * Used at {@link Script::escapeValue()} to get the proper time.
 */
use DateTimeZone;
/**
 * Used to reliably write to streams at {@link Script::prepare()}.
 */
use PEAR2\Net\Transmitter\Stream;
/**
 * Used to catch DateTime and DateInterval exceptions at
 * {@link Script::parseValue()}.
 */
use Exception as E;
/**
 * Scripting class.
 *
 * Provides functionality related to parsing and composing RouterOS scripts and
 * values.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class Script
{
    /**
     * Parses a value from a RouterOS scripting context.
     *
     * Turns a value from RouterOS into an equivalent PHP value, based on
     * determining the type in the same way RouterOS would determine it for a
     * literal.
     *
     * This method is intended to be the very opposite of
     * {@link static::escapeValue()}. That is, results from that method, if
     * given to this method, should produce equivalent results.
     *
     * @param string            $value    The value to be parsed.
     *     Must be a literal of a value,
     *     e.g. what {@link static::escapeValue()} will give you.
     * @param DateTimeZone|null $timezone The timezone which any resulting
     *     DateTime object (either the main value, or values within an array)
     *     will use. Defaults to UTC.
     *
     * @return mixed Depending on RouterOS type detected:
     *     - "nil" (the string "[]") or "nothing" (empty string) - NULL.
     *     - "num" - int or double for large values.
     *     - "bool" - a boolean.
     *     - "array" - an array, with the keys and values processed recursively.
     *     - "time" - a {@link DateInterval} object.
     *     - "date" (pseudo type; string in the form "M/j/Y") - a DateTime
     *         object with the specified date, at midnight.
     *     - "datetime" (pseudo type; string in the form "M/j/Y H:i:s") - a
     *         DateTime object with the specified date and time.
     *     - "str" (a quoted string) - a string, with the contents escaped.
     *     - Unrecognized type - casted to a string, unmodified.
     */
    public static function parseValue($value, DateTimeZone $timezone = null)
    {
        $value = static::parseValueToSimple($value);
        if (!is_string($value)) {
            return $value;
        }
        try {
            return static::parseValueToArray($value, $timezone);
        } catch (ParserException $e) {
            try {
                return static::parseValueToDateInterval($value);
            } catch (ParserException $e) {
                try {
                    return static::parseValueToDateTime($value, $timezone);
                } catch (ParserException $e) {
                    return static::parseValueToString($value);
                }
            }
        }
    }
    /**
     * Parses a RouterOS value into a PHP string.
     *
     * @param string $value The value to be parsed.
     *     Must be a literal of a value,
     *     e.g. what {@link static::escapeValue()} will give you.
     *
     * @return string If a quoted string is provided, it would be parsed.
     *     Otherwise, the value is casted to a string, and returned unmodified.
     */
    public static function parseValueToString($value)
    {
        $value = (string)$value;
        if ('"' === $value[0] && '"' === $value[strlen($value) - 1]) {
            return str_replace(
                array('\"', '\\\\', "\\\n", "\\\r\n", "\\\r"),
                array('"', '\\'),
                substr($value, 1, -1)
            );
        }
        return $value;
    }
    /**
     * Parses a RouterOS value into a PHP simple type.
     *
     * Parses a RouterOS value into a PHP simple type. "Simple" types being
     * scalar types, plus NULL.
     *
     * @param string $value The value to be parsed. Must be a literal of a
     *     value, e.g. what {@link static::escapeValue()} will give you.
     *
     * @return string|bool|int|double|null Depending on RouterOS type detected:
     *     - "nil" (the string "[]") or "nothing" (empty string) - NULL.
     *     - "num" - int or double for large values.
     *     - "bool" - a boolean.
     *     - Unrecognized type - casted to a string, unmodified.
     */
    public static function parseValueToSimple($value)
    {
        $value = (string)$value;
        if (in_array($value, array('', '[]'), true)) {
            return null;
        } elseif (in_array($value, array('true', 'false', 'yes', 'no'), true)) {
            return $value === 'true' || $value === 'yes';
        } elseif ($value === (string)($num = (int)$value)
            || $value === (string)($num = (double)$value)
        ) {
            return $num;
        }
        return $value;
    }
    /**
     * Parses a RouterOS value into a PHP DateTime object
     *
     * Parses a RouterOS value into a PHP DateTime object.
     *
     * @param string            $value    The value to be parsed.
     *     Must be a literal of a value,
     *     e.g. what {@link static::escapeValue()} will give you.
     * @param DateTimeZone|null $timezone The timezone which the resulting
     *     DateTime object will use. Defaults to UTC.
     *
     * @return DateTime Depending on RouterOS type detected:
     *     - "date" (pseudo type; string in the form "M/j/Y") - a DateTime
     *         object with the specified date, at midnight UTC time (regardless
     *         of timezone provided).
     *     - "datetime" (pseudo type; string in the form "M/j/Y H:i:s") - a
     *         DateTime object with the specified date and time,
     *         with the specified timezone.
     *
     * @throws ParserException When the value is not of a recognized type.
     */
    public static function parseValueToDateTime(
        $value,
        DateTimeZone $timezone = null
    ) {
        $previous = null;
        $value = (string)$value;
        if ('' !== $value && preg_match(
            '#^
                (?<mon>jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)
                /
                (?<day>\d\d?)
                /
                (?<year>\d{4})
                (?:
                    \s+(?<time>\d{2}\:\d{2}:\d{2})
                )?
            $#uix',
            $value,
            $date
        )
        ) {
            if (!isset($date['time'])) {
                $date['time'] = '00:00:00';
                $timezone = new DateTimeZone('UTC');
            } elseif (null === $timezone) {
                $timezone = new DateTimeZone('UTC');
            }
            try {
                return new DateTime(
                    $date['year'] .
                    '-' . ucfirst($date['mon']) .
                    "-{$date['day']} {$date['time']}",
                    $timezone
                );
            } catch (E $e) {
                $previous = $e;
            }
        }
        throw new ParserException(
            'The supplied value can not be converted to a DateTime',
            ParserException::CODE_DATETIME,
            $previous
        );
    }
    /**
     * Parses a RouterOS value into a PHP DateInterval.
     *
     * Parses a RouterOS value into a PHP DateInterval.
     *
     * @param string $value The value to be parsed. Must be a literal of a
     *     value, e.g. what {@link static::escapeValue()} will give you.
     *
     * @return DateInterval The value as a DateInterval object.
     *
     * @throws ParserException When the value is not of a recognized type.
     */
    public static function parseValueToDateInterval($value)
    {
        $value = (string)$value;
        if ('' !== $value && preg_match(
            '/^
                (?:(\d+)w)?
                (?:(\d+)d)?
                (?:(\d+)(?:\:|h))?
                (?|
                    (\d+)\:
                    (\d*(?:\.\d{1,9})?)
                |
                    (?:(\d+)m)?
                    (?:(\d+|\d*\.\d{1,9})s)?
                    (?:((?5))ms)?
                    (?:((?5))us)?
                    (?:((?5))ns)?
                )
            $/x',
            $value,
            $time
        )
        ) {
            $days = isset($time[2]) ? (int)$time[2] : 0;
            if (isset($time[1])) {
                $days += 7 * (int)$time[1];
            }
            if (empty($time[3])) {
                $time[3] = 0;
            }
            if (empty($time[4])) {
                $time[4] = 0;
            }
            if (empty($time[5])) {
                $time[5] = 0;
            }
            $subsecondTime = 0.0;
            //@codeCoverageIgnoreStart
            // No PHP version currently supports sub-second DateIntervals,
            // meaning this section is untestable, since no version constraints
            // can be specified for test inputs.
            // All inputs currently use integer seconds only, making this
            // section unreachable during tests.
            // Nevertheless, this section exists right now, in order to provide
            // such support as soon as PHP has it.
            if (!empty($time[6])) {
                $subsecondTime += ((double)$time[6]) / 1000;
            }
            if (!empty($time[7])) {
                $subsecondTime += ((double)$time[7]) / 1000000;
            }
            if (!empty($time[8])) {
                $subsecondTime += ((double)$time[8]) / 1000000000;
            }
            //@codeCoverageIgnoreEnd
            $secondsSpec = $time[5] + $subsecondTime;
            try {
                return new DateInterval(
                    "P{$days}DT{$time[3]}H{$time[4]}M{$secondsSpec}S"
                );
                //@codeCoverageIgnoreStart
                // See previous ignored section's note.
                //
                // This section is added for backwards compatibility with
                // current PHP versions, when in the future sub-second support
                // is added.
                // In that event, the test inputs for older versions will be
                // expected to get a rounded up result of the sub-second data.
            } catch (E $e) {
                $secondsSpec = (int)round($secondsSpec);
                return new DateInterval(
                    "P{$days}DT{$time[3]}H{$time[4]}M{$secondsSpec}S"
                );
            }
            //@codeCoverageIgnoreEnd
        }
        throw new ParserException(
            'The supplied value can not be converted to DateInterval',
            ParserException::CODE_DATEINTERVAL
        );
    }
    /**
     * Parses a RouterOS value into a PHP array.
     *
     * Parses a RouterOS value into a PHP array.
     *
     * @param string            $value    The value to be parsed.
     *     Must be a literal of a value,
     *     e.g. what {@link static::escapeValue()} will give you.
     * @param DateTimeZone|null $timezone The timezone which any resulting
     *     DateTime object within the array will use. Defaults to UTC.
     *
     * @return array An array, with the keys and values processed recursively,
     *         the keys with {@link static::parseValueToSimple()},
     *         and the values with {@link static::parseValue()}.
     *
     * @throws ParserException When the value is not of a recognized type.
     */
    public static function parseValueToArray(
        $value,
        DateTimeZone $timezone = null
    ) {
        $value = (string)$value;
        if ('{' === $value[0] && '}' === $value[strlen($value) - 1]) {
            $value = substr($value, 1, -1);
            if ('' === $value) {
                return array();
            }
            $parsedValue = preg_split(
                '/
                    (\"(?:\\\\\\\\|\\\\"|[^"])*\")
                    |
                    (\{[^{}]*(?2)?\})
                    |
                    ([^;=]+)
                /sx',
                $value,
                null,
                PREG_SPLIT_DELIM_CAPTURE
            );
            $result = array();
            $newVal = null;
            $newKey = null;
            for ($i = 0, $l = count($parsedValue); $i < $l; ++$i) {
                switch ($parsedValue[$i]) {
                case '':
                    break;
                case ';':
                    if (null === $newKey) {
                        $result[] = $newVal;
                    } else {
                        $result[$newKey] = $newVal;
                    }
                    $newKey = $newVal = null;
                    break;
                case '=':
                    $newKey = static::parseValueToSimple($parsedValue[$i - 1]);
                    $newVal = static::parseValue($parsedValue[++$i], $timezone);
                    break;
                default:
                    $newVal = static::parseValue($parsedValue[$i], $timezone);
                }
            }
            if (null === $newKey) {
                $result[] = $newVal;
            } else {
                $result[$newKey] = $newVal;
            }
            return $result;
        }
        throw new ParserException(
            'The supplied value can not be converted to an array',
            ParserException::CODE_ARRAY
        );
    }
    /**
     * Prepares a script.
     *
     * Prepares a script for eventual execution by prepending parameters as
     * variables to it.
     *
     * This is particularly useful when you're creating scripts that you don't
     * want to execute right now (as with {@link Util::exec()}, but instead
     * you want to store it for later execution, perhaps by supplying it to
     * "/system scheduler".
     *
     * @param string|resource         $source The source of the script,
     *     as a string or stream. If a stream is provided, reading starts from
     *     the current position to the end of the stream, and the pointer stays
     *     at the end after reading is done.
     * @param array<string|int,mixed> $params An array of parameters to make
     *     available in the script as local variables.
     *     Variable names are array keys, and variable values are array values.
     *     Array values are automatically processed with
     *     {@link static::escapeValue()}. Streams are also supported, and are
     *     processed in chunks, each with
     *     {@link static::escapeString()} with all bytes being escaped.
     *     Processing starts from the current position to the end of the stream,
     *     and the stream's pointer is left untouched after the reading is done.
     *     Variables with a value of type "nothing" can be declared with a
     *     numeric array key and the variable name as the array value
     *     (that is casted to a string).
     *
     * @return resource A new PHP temporary stream with the script as contents,
     *     with the pointer back at the start.
     *
     * @see static::append()
     */
    public static function prepare(
        $source,
        array $params = array()
    ) {
        $resultStream = fopen('php://temp', 'r+b');
        static::append($resultStream, $source, $params);
        rewind($resultStream);
        return $resultStream;
    }
    /**
     * Appends a script.
     *
     * Appends a script to an existing stream.
     *
     * @param resource                $stream An existing stream to write the
     *     resulting script to.
     * @param string|resource         $source The source of the script,
     *     as a string or stream. If a stream is provided, reading starts from
     *     the current position to the end of the stream, and the pointer stays
     *     at the end after reading is done.
     * @param array<string|int,mixed> $params An array of parameters to make
     *     available in the script as local variables.
     *     Variable names are array keys, and variable values are array values.
     *     Array values are automatically processed with
     *     {@link static::escapeValue()}. Streams are also supported, and are
     *     processed in chunks, each with
     *     {@link static::escapeString()} with all bytes being escaped.
     *     Processing starts from the current position to the end of the stream,
     *     and the stream's pointer is left untouched after the reading is done.
     *     Variables with a value of type "nothing" can be declared with a
     *     numeric array key and the variable name as the array value
     *     (that is casted to a string).
     *
     * @return int The number of bytes written to $stream is returned,
     *     and the pointer remains where it was after the write
     *     (i.e. it is not seeked back, even if seeking is supported).
     */
    public static function append(
        $stream,
        $source,
        array $params = array()
    ) {
        $writer = new Stream($stream, false);
        $bytes = 0;
        foreach ($params as $pname => $pvalue) {
            if (is_int($pname)) {
                $pvalue = static::escapeString((string)$pvalue);
                $bytes += $writer->send(":local \"{$pvalue}\";\n");
                continue;
            }
            $pname = static::escapeString($pname);
            $bytes += $writer->send(":local \"{$pname}\" ");
            if (Stream::isStream($pvalue)) {
                $reader = new Stream($pvalue, false);
                $chunkSize = $reader->getChunk(Stream::DIRECTION_RECEIVE);
                $bytes += $writer->send('"');
                while ($reader->isAvailable() && $reader->isDataAwaiting()) {
                    $bytes += $writer->send(
                        static::escapeString(fread($pvalue, $chunkSize), true)
                    );
                }
                $bytes += $writer->send("\";\n");
            } else {
                $bytes += $writer->send(static::escapeValue($pvalue) . ";\n");
            }
        }
        $bytes += $writer->send($source);
        return $bytes;
    }
    /**
     * Escapes a value for a RouterOS scripting context.
     *
     * Turns any native PHP value into an equivalent whole value that can be
     * inserted as part of a RouterOS script.
     *
     * DateInterval objects will be casted to RouterOS' "time" type.
     *
     * DateTime objects will be casted to a string following the "M/d/Y H:i:s"
     * format. If the time is exactly midnight (including microseconds), and
     * the timezone is UTC, the string will include only the "M/d/Y" date.
     *
     * Unrecognized types (i.e. resources and other objects) are casted to
     * strings, and those strings are then escaped.
     *
     * @param mixed $value The value to be escaped.
     *
     * @return string A string representation that can be directly inserted in a
     *     script as a whole value.
     */
    public static function escapeValue($value)
    {
        switch (gettype($value)) {
        case 'NULL':
            $value = '[]';
            break;
        case 'integer':
            $value = (string)$value;
            break;
        case 'boolean':
            $value = $value ? 'true' : 'false';
            break;
        case 'array':
            if (0 === count($value)) {
                $value = '({})';
                break;
            }
            $result = '';
            foreach ($value as $key => $val) {
                $result .= ';';
                if (!is_int($key)) {
                    $result .= static::escapeValue($key) . '=';
                }
                $result .= static::escapeValue($val);
            }
            $value = '{' . substr($result, 1) . '}';
            break;
            /** @noinspection PhpMissingBreakStatementInspection */
        case 'object':
            if ($value instanceof DateTime) {
                $usec = $value->format('u');
                $usec = '000000' === $usec ? '' : '.' . $usec;
                $value = '00:00:00.000000 UTC' === $value->format('H:i:s.u e')
                    ? $value->format('M/d/Y')
                    : $value->format('M/d/Y H:i:s') . $usec;
            }
            if ($value instanceof DateInterval) {
                if (false === $value->days || $value->days < 0) {
                    $value = $value->format('%r%dd%H:%I:%S');
                } else {
                    $value = $value->format('%r%ad%H:%I:%S');
                }
                break;
            }
            //break; intentionally omitted
        default:
            $value = '"' . static::escapeString((string)$value) . '"';
            break;
        }
        return $value;
    }
    /**
     * Escapes a string for a RouterOS scripting context.
     *
     * Escapes a string for a RouterOS scripting context. The value can then be
     * surrounded with quotes at a RouterOS script (or concatenated onto a
     * larger string first), and you can be sure there won't be any code
     * injections coming from it.
     *
     * By default, for the sake of brevity of the output, ASCII alphanumeric
     * characters and underscores are left untouched. And for the sake of
     * character conversion, bytes above 0x7F are also left untouched.
     *
     * @param string $value Value to be escaped.
     * @param bool   $full  Whether to escape all bytes in the string, including
     *     ASCII alphanumeric characters, underscores and bytes above 0x7F.
     *
     * @return string The escaped value.
     *
     * @internal Why leave ONLY those ASCII characters and not also others?
     *     Because those can't in any way be mistaken for language constructs,
     *     unlike many other "safe inside strings, but not outside" ASCII
     *     characters, like ",", ".", "+", "-", "~", etc.
     */
    public static function escapeString($value, $full = false)
    {
        if ($full) {
            return self::_escapeCharacters(array($value));
        }
        return preg_replace_callback(
            '/[^\\_A-Za-z0-9\\x80-\\xFF]+/S',
            array(__CLASS__, '_escapeCharacters'),
            $value
        );
    }
    /**
     * Escapes a character for a RouterOS scripting context.
     *
     * Escapes a character for a RouterOS scripting context.
     * Intended to only be called by {@link self::escapeString()} for the
     * matching strings.
     *
     * @param array $chars The matches array, expected to contain exactly one
     *     member, in which is the whole string to be escaped.
     *
     * @return string The escaped characters.
     */
    private static function _escapeCharacters(array $chars)
    {
        $result = '';
        for ($i = 0, $l = strlen($chars[0]); $i < $l; ++$i) {
            $result .= '\\' . str_pad(
                strtoupper(dechex(ord($chars[0][$i]))),
                2,
                '0',
                STR_PAD_LEFT
            );
        }
        return $result;
    }
}
================================================

File: .scrutinizer.yml
================================================
imports:
    - php
inherit: true
tools:
    ##See .travis.yml.
    #external_code_coverage:
    #    runs: 4
    php_sim: false
    php_cpd: true
    php_code_sniffer:
        config:
            standard: PEAR
================================================

File: .travis.yml
================================================
language: php
php:
  # The earliest PHP 5.3 version that can run the test suit
  # AND is supported by Travis-CI.
  - 5.3.3
  - 5.3
  - 5.4
  - 5.5
  - 5.6
  - 7.0
before_script:
  - composer self-update
  - composer install --dev
script:
  - composer require pear2/cache_shm:dev-develop | cat -
  - cd tests
  - ../vendor/bin/phpunit --configuration secondaryPeer.xml > secondaryPeer.out.txt &
  - sleep 2
  - ../vendor/bin/phpunit --configuration phpunit.xml
  ## Code coverage seems to be causing a failure currently.
  #- ../vendor/bin/phpunit --coverage-clover=coverage.clover --configuration phpunit.xml
  #- wget https://scrutinizer-ci.com/ocular.phar
  #- php ocular.phar code-coverage:upload --format=php-clover coverage.clover
after_script:
  - cat secondaryPeer.out.txt
================================================

File: composer.json
================================================
{
    "name": "pear2/net_transmitter",
    "description": "A stream wrapper that ensures data integrity. Particularly useful for sockets.",
    "keywords": ["integrity", "sockets", "networking", "pear2", "package", "network", "socket"],
    "homepage": "http://pear2.github.com/Net_Transmitter/",
    "license": "LGPL-2.1",
    "authors": [
        {
            "name": "Vasil Rangelov",
            "email": "boen.robot@gmail.com",
            "role": "lead"
        }
    ],
    "support": {
        "issues": "http://github.com/pear2/Net_Transmitter/issues",
        "wiki": "http://github.com/pear2/Net_Transmitter/wiki"
    },
    "require": {
        "php": ">=5.3.0"
    },
    "require-dev": {
        "phpunit/phpunit": "@stable"
    },
    "suggest": {
        "pear2/cache_shm": "Enables persistent connections",
        "ext-apc": "This, APCu or Wincache is required for persistent connections.",
        "ext-apcu": "This, APC or Wincache is required for persistent connections.",
        "ext-wincache": "This, APC or APCu is required for persistent connections. Reccomended for Windows.",
        "ext-openssl": "Enables encrypted connections."
    },
    "autoload": {
        "psr-0": {
            "PEAR2\\Net\\Transmitter\\": "src/"
        }
    }
}
================================================

File: apigen.neon
================================================
title: PEAR2_Net_Transmitter documentation
source:
  - ../src
destination: Reference/ApiGen/Doc
extensions:
  - php
charset:
  - UTF-8
accessLevels:
  - public
tree: true
================================================

File: README
================================================
Wrapper for network stream functionality.
PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.
This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
================================================

File: README.md
================================================
See the project wiki for installation instructions and other documentation.
The sources as visible here reflect the development version. They may contain parsing errors, fail to install or have all other sorts of errors. If you want to use this package, download the packaged archives instead.
================================================

File: NetworkStream.php
================================================
<?php
/**
 * ~~summary~~
 * 
 * ~~description~~
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\Transmitter;
/**
 * A network transmitter.
 * 
 * This is a convenience wrapper for network streams. Used to ensure data
 * integrity.
 * 
 * @category Net
 * @package  PEAR2_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_Transmitter
 */
abstract class NetworkStream extends Stream
{
    /**
     * Used in {@link setCrypto()} to disable encryption.
     */
    const CRYPTO_OFF = '';
    /**
     * Used in {@link setCrypto()} to set encryption to either SSLv2 or SSLv3,
     * depending on what the other end supports.
     */
    const CRYPTO_SSL = 'SSLv23';
    /**
     * Used in {@link setCrypto()} to set encryption to SSLv2.
     */
    const CRYPTO_SSL2 = 'SSLv2';
    /**
     * Used in {@link setCrypto()} to set encryption to SSLv3.
     */
    const CRYPTO_SSL3 = 'SSLv3';
    /**
     * Used in {@link setCrypto()} to set encryption to TLS (exact version
     * negotiated between 1.0 and 1.2).
     */
    const CRYPTO_TLS = 'TLS';
    /**
     * @var string The type of stream. Can be either "_CLIENT" or "_SERVER".
     *     Used to complement the encryption type. Must be set by child classes
     *     for {@link setCrypto()} to work properly.
     */
    protected $streamType = '';
    /**
     * @var string The current cryptography setting.
     */
    protected $crypto = '';
    /**
     * Wraps around the specified stream.
     * 
     * @param resource $stream The stream to wrap around.
     */
    public function __construct($stream)
    {
        parent::__construct($stream, true);
    }
    /**
     * Gets the current cryptography setting.
     * 
     * @return string One of this class' CRYPTO_* constants.
     */
    public function getCrypto()
    {
        return $this->crypto;
    }
    /**
     * Sets the current connection's cryptography setting.
     * 
     * @param string $type The encryption type to set. Must be one of this
     *     class' CRYPTO_* constants.
     * 
     * @return boolean TRUE on success, FALSE on failure.
     */
    public function setCrypto($type)
    {
        if (self::CRYPTO_OFF === $type) {
            $result = stream_socket_enable_crypto($this->stream, false);
        } else {
            $result = stream_socket_enable_crypto(
                $this->stream,
                true,
                constant("STREAM_CRYPTO_METHOD_{$type}{$this->streamType}")
            );
        }
        if ($result) {
            $this->crypto = $type;
        }
        return $result;
    }
    /**
     * Checks whether the stream is available for operations.
     * 
     * @return bool TRUE if the stream is available, FALSE otherwise.
     */
    public function isAvailable()
    {
        if (parent::isStream($this->stream)) {
            if ($this->isBlocking && feof($this->stream)) {
                return false;
            }
            $meta = stream_get_meta_data($this->stream);
            return !$meta['eof'];
        }
        return false;
    }
    /**
     * Sets the size of a stream's buffer.
     * 
     * @param int $size      The desired size of the buffer, in bytes.
     * @param int $direction The buffer of which direction to set. Valid
     *     values are the DIRECTION_* constants.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function setBuffer($size, $direction = self::DIRECTION_ALL)
    {
        $result = parent::setBuffer($size, $direction);
        if (self::DIRECTION_SEND === $direction
            && function_exists('stream_set_chunk_size') && !$result
        ) {
            return false !== @stream_set_chunk_size($this->stream, $size);
        }
        return $result;
    }
    /**
     * Shutdown a full-duplex connection
     * 
     * Shutdowns (partially or not) a full-duplex connection.
     * 
     * @param int $direction The direction for which to disable further
     *     communications.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function shutdown($direction = self::DIRECTION_ALL)
    {
        $directionMap = array(
            self::DIRECTION_ALL => STREAM_SHUT_RDWR,
            self::DIRECTION_SEND => STREAM_SHUT_WR,
            self::DIRECTION_RECEIVE => STREAM_SHUT_RD
        );
        return array_key_exists($direction, $directionMap)
            && stream_socket_shutdown($this->stream, $directionMap[$direction]);
    }
}
================================================

File: composer.json
================================================
{
    "name": "phpmailer/phpmailer",
    "type": "library",
    "description": "PHPMailer is a full-featured email creation and transfer class for PHP",
    "authors": [
        {
            "name": "Marcus Bointon",
            "email": "phpmailer@synchromedia.co.uk"
        },
        {
            "name": "Jim Jagielski",
            "email": "jimjag@gmail.com"
        },
        {
            "name": "Andy Prevost",
            "email": "codeworxtech@users.sourceforge.net"
        },
        {
            "name": "Brent R. Matzelle"
        }
    ],
    "funding": [
        {
            "url": "https://github.com/synchro",
            "type": "github"
        }
    ],
    "require": {
        "php": ">=5.5.0",
        "ext-ctype": "*",
        "ext-filter": "*"
    },
    "require-dev": {
        "friendsofphp/php-cs-fixer": "^2.2",
        "phpunit/phpunit": "^4.8 || ^5.7",
        "doctrine/annotations": "^1.2"
    },
    "suggest": {
        "psr/log": "For optional PSR-3 debug logging",
        "league/oauth2-google": "Needed for Google XOAUTH2 authentication",
        "hayageek/oauth2-yahoo": "Needed for Yahoo XOAUTH2 authentication",
        "stevenmaguire/oauth2-microsoft": "Needed for Microsoft XOAUTH2 authentication",
        "ext-mbstring": "Needed to send email in multibyte encoding charset",
        "symfony/polyfill-mbstring": "To support UTF-8 if the Mbstring PHP extension is not enabled (^1.2)"
    },
    "autoload": {
        "psr-4": {
            "PHPMailer\\PHPMailer\\": "src/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "PHPMailer\\Test\\": "test/"
        }
    },
    "license": "LGPL-2.1-only"
}
================================================

File: LICENSE
================================================
                  GNU LESSER GENERAL PUBLIC LICENSE
                       Version 2.1, February 1999
 Copyright (C) 1991, 1999 Free Software Foundation, Inc.
 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
[This is the first released version of the Lesser GPL.  It also counts
 as the successor of the GNU Library Public License, version 2, hence
 the version number 2.1.]
                            Preamble
  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
Licenses are intended to guarantee your freedom to share and change
free software--to make sure the software is free for all its users.
  This license, the Lesser General Public License, applies to some
specially designated software packages--typically libraries--of the
Free Software Foundation and other authors who decide to use it.  You
can use it too, but we suggest you first think carefully about whether
this license or the ordinary General Public License is the better
strategy to use in any particular case, based on the explanations below.
  When we speak of free software, we are referring to freedom of use,
not price.  Our General Public Licenses are designed to make sure that
you have the freedom to distribute copies of free software (and charge
for this service if you wish); that you receive source code or can get
it if you want it; that you can change the software and use pieces of
it in new free programs; and that you are informed that you can do
these things.
  To protect your rights, we need to make restrictions that forbid
distributors to deny you these rights or to ask you to surrender these
rights.  These restrictions translate to certain responsibilities for
you if you distribute copies of the library or if you modify it.
  For example, if you distribute copies of the library, whether gratis
or for a fee, you must give the recipients all the rights that we gave
you.  You must make sure that they, too, receive or can get the source
code.  If you link other code with the library, you must provide
complete object files to the recipients, so that they can relink them
with the library after making changes to the library and recompiling
it.  And you must show them these terms so they know their rights.
  We protect your rights with a two-step method: (1) we copyright the
library, and (2) we offer you this license, which gives you legal
permission to copy, distribute and/or modify the library.
  To protect each distributor, we want to make it very clear that
there is no warranty for the free library.  Also, if the library is
modified by someone else and passed on, the recipients should know
that what they have is not the original version, so that the original
author's reputation will not be affected by problems that might be
introduced by others.
  Finally, software patents pose a constant threat to the existence of
any free program.  We wish to make sure that a company cannot
effectively restrict the users of a free program by obtaining a
restrictive license from a patent holder.  Therefore, we insist that
any patent license obtained for a version of the library must be
consistent with the full freedom of use specified in this license.
  Most GNU software, including some libraries, is covered by the
ordinary GNU General Public License.  This license, the GNU Lesser
General Public License, applies to certain designated libraries, and
is quite different from the ordinary General Public License.  We use
this license for certain libraries in order to permit linking those
libraries into non-free programs.
  When a program is linked with a library, whether statically or using
a shared library, the combination of the two is legally speaking a
combined work, a derivative of the original library.  The ordinary
General Public License therefore permits such linking only if the
entire combination fits its criteria of freedom.  The Lesser General
Public License permits more lax criteria for linking other code with
the library.
  We call this license the "Lesser" General Public License because it
does Less to protect the user's freedom than the ordinary General
Public License.  It also provides other free software developers Less
of an advantage over competing non-free programs.  These disadvantages
are the reason we use the ordinary General Public License for many
libraries.  However, the Lesser license provides advantages in certain
special circumstances.
  For example, on rare occasions, there may be a special need to
encourage the widest possible use of a certain library, so that it becomes
a de-facto standard.  To achieve this, non-free programs must be
allowed to use the library.  A more frequent case is that a free
library does the same job as widely used non-free libraries.  In this
case, there is little to gain by limiting the free library to free
software only, so we use the Lesser General Public License.
  In other cases, permission to use a particular library in non-free
programs enables a greater number of people to use a large body of
free software.  For example, permission to use the GNU C Library in
non-free programs enables many more people to use the whole GNU
operating system, as well as its variant, the GNU/Linux operating
system.
  Although the Lesser General Public License is Less protective of the
users' freedom, it does ensure that the user of a program that is
linked with the Library has the freedom and the wherewithal to run
that program using a modified version of the Library.
  The precise terms and conditions for copying, distribution and
modification follow.  Pay close attention to the difference between a
"work based on the library" and a "work that uses the library".  The
former contains code derived from the library, whereas the latter must
be combined with the library in order to run.
                  GNU LESSER GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
  0. This License Agreement applies to any software library or other
program which contains a notice placed by the copyright holder or
other authorized party saying it may be distributed under the terms of
this Lesser General Public License (also called "this License").
Each licensee is addressed as "you".
  A "library" means a collection of software functions and/or data
prepared so as to be conveniently linked with application programs
(which use some of those functions and data) to form executables.
  The "Library", below, refers to any such software library or work
which has been distributed under these terms.  A "work based on the
Library" means either the Library or any derivative work under
copyright law: that is to say, a work containing the Library or a
portion of it, either verbatim or with modifications and/or translated
straightforwardly into another language.  (Hereinafter, translation is
included without limitation in the term "modification".)
  "Source code" for a work means the preferred form of the work for
making modifications to it.  For a library, complete source code means
all the source code for all modules it contains, plus any associated
interface definition files, plus the scripts used to control compilation
and installation of the library.
  Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running a program using the Library is not restricted, and output from
such a program is covered only if its contents constitute a work based
on the Library (independent of the use of the Library in a tool for
writing it).  Whether that is true depends on what the Library does
and what the program that uses the Library does.
  1. You may copy and distribute verbatim copies of the Library's
complete source code as you receive it, in any medium, provided that
you conspicuously and appropriately publish on each copy an
appropriate copyright notice and disclaimer of warranty; keep intact
all the notices that refer to this License and to the absence of any
warranty; and distribute a copy of this License along with the
Library.
  You may charge a fee for the physical act of transferring a copy,
and you may at your option offer warranty protection in exchange for a
fee.
  2. You may modify your copy or copies of the Library or any portion
of it, thus forming a work based on the Library, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:
    a) The modified work must itself be a software library.
    b) You must cause the files modified to carry prominent notices
    stating that you changed the files and the date of any change.
    c) You must cause the whole of the work to be licensed at no
    charge to all third parties under the terms of this License.
    d) If a facility in the modified Library refers to a function or a
    table of data to be supplied by an application program that uses
    the facility, other than as an argument passed when the facility
    is invoked, then you must make a good faith effort to ensure that,
    in the event an application does not supply such function or
    table, the facility still operates, and performs whatever part of
    its purpose remains meaningful.
    (For example, a function in a library to compute square roots has
    a purpose that is entirely well-defined independent of the
    application.  Therefore, Subsection 2d requires that any
    application-supplied function or table used by this function must
    be optional: if the application does not supply it, the square
    root function must still compute square roots.)
These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Library,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Library, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote
it.
Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Library.
In addition, mere aggregation of another work not based on the Library
with the Library (or with a work based on the Library) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.
  3. You may opt to apply the terms of the ordinary GNU General Public
License instead of this License to a given copy of the Library.  To do
this, you must alter all the notices that refer to this License, so
that they refer to the ordinary GNU General Public License, version 2,
instead of to this License.  (If a newer version than version 2 of the
ordinary GNU General Public License has appeared, then you can specify
that version instead if you wish.)  Do not make any other change in
these notices.
  Once this change is made in a given copy, it is irreversible for
that copy, so the ordinary GNU General Public License applies to all
subsequent copies and derivative works made from that copy.
  This option is useful when you wish to copy part of the code of
the Library into a program that is not a library.
  4. You may copy and distribute the Library (or a portion or
derivative of it, under Section 2) in object code or executable form
under the terms of Sections 1 and 2 above provided that you accompany
it with the complete corresponding machine-readable source code, which
must be distributed under the terms of Sections 1 and 2 above on a
medium customarily used for software interchange.
  If distribution of object code is made by offering access to copy
from a designated place, then offering equivalent access to copy the
source code from the same place satisfies the requirement to
distribute the source code, even though third parties are not
compelled to copy the source along with the object code.
  5. A program that contains no derivative of any portion of the
Library, but is designed to work with the Library by being compiled or
linked with it, is called a "work that uses the Library".  Such a
work, in isolation, is not a derivative work of the Library, and
therefore falls outside the scope of this License.
  However, linking a "work that uses the Library" with the Library
creates an executable that is a derivative of the Library (because it
contains portions of the Library), rather than a "work that uses the
library".  The executable is therefore covered by this License.
Section 6 states terms for distribution of such executables.
  When a "work that uses the Library" uses material from a header file
that is part of the Library, the object code for the work may be a
derivative work of the Library even though the source code is not.
Whether this is true is especially significant if the work can be
linked without the Library, or if the work is itself a library.  The
threshold for this to be true is not precisely defined by law.
  If such an object file uses only numerical parameters, data
structure layouts and accessors, and small macros and small inline
functions (ten lines or less in length), then the use of the object
file is unrestricted, regardless of whether it is legally a derivative
work.  (Executables containing this object code plus portions of the
Library will still fall under Section 6.)
  Otherwise, if the work is a derivative of the Library, you may
distribute the object code for the work under the terms of Section 6.
Any executables containing that work also fall under Section 6,
whether or not they are linked directly with the Library itself.
  6. As an exception to the Sections above, you may also combine or
link a "work that uses the Library" with the Library to produce a
work containing portions of the Library, and distribute that work
under terms of your choice, provided that the terms permit
modification of the work for the customer's own use and reverse
engineering for debugging such modifications.
  You must give prominent notice with each copy of the work that the
Library is used in it and that the Library and its use are covered by
this License.  You must supply a copy of this License.  If the work
during execution displays copyright notices, you must include the
copyright notice for the Library among them, as well as a reference
directing the user to the copy of this License.  Also, you must do one
of these things:
    a) Accompany the work with the complete corresponding
    machine-readable source code for the Library including whatever
    changes were used in the work (which must be distributed under
    Sections 1 and 2 above); and, if the work is an executable linked
    with the Library, with the complete machine-readable "work that
    uses the Library", as object code and/or source code, so that the
    user can modify the Library and then relink to produce a modified
    executable containing the modified Library.  (It is understood
    that the user who changes the contents of definitions files in the
    Library will not necessarily be able to recompile the application
    to use the modified definitions.)
    b) Use a suitable shared library mechanism for linking with the
    Library.  A suitable mechanism is one that (1) uses at run time a
    copy of the library already present on the user's computer system,
    rather than copying library functions into the executable, and (2)
    will operate properly with a modified version of the library, if
    the user installs one, as long as the modified version is
    interface-compatible with the version that the work was made with.
    c) Accompany the work with a written offer, valid for at
    least three years, to give the same user the materials
    specified in Subsection 6a, above, for a charge no more
    than the cost of performing this distribution.
    d) If distribution of the work is made by offering access to copy
    from a designated place, offer equivalent access to copy the above
    specified materials from the same place.
    e) Verify that the user has already received a copy of these
    materials or that you have already sent this user a copy.
  For an executable, the required form of the "work that uses the
Library" must include any data and utility programs needed for
reproducing the executable from it.  However, as a special exception,
the materials to be distributed need not include anything that is
normally distributed (in either source or binary form) with the major
components (compiler, kernel, and so on) of the operating system on
which the executable runs, unless that component itself accompanies
the executable.
  It may happen that this requirement contradicts the license
restrictions of other proprietary libraries that do not normally
accompany the operating system.  Such a contradiction means you cannot
use both them and the Library together in an executable that you
distribute.
  7. You may place library facilities that are a work based on the
Library side-by-side in a single library together with other library
facilities not covered by this License, and distribute such a combined
library, provided that the separate distribution of the work based on
the Library and of the other library facilities is otherwise
permitted, and provided that you do these two things:
    a) Accompany the combined library with a copy of the same work
    based on the Library, uncombined with any other library
    facilities.  This must be distributed under the terms of the
    Sections above.
    b) Give prominent notice with the combined library of the fact
    that part of it is a work based on the Library, and explaining
    where to find the accompanying uncombined form of the same work.
  8. You may not copy, modify, sublicense, link with, or distribute
the Library except as expressly provided under this License.  Any
attempt otherwise to copy, modify, sublicense, link with, or
distribute the Library is void, and will automatically terminate your
rights under this License.  However, parties who have received copies,
or rights, from you under this License will not have their licenses
terminated so long as such parties remain in full compliance.
  9. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Library or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Library (or any work based on the
Library), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Library or works based on it.
  10. Each time you redistribute the Library (or any work based on the
Library), the recipient automatically receives a license from the
original licensor to copy, distribute, link with or modify the Library
subject to these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties with
this License.
  11. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Library at all.  For example, if a patent
license would not permit royalty-free redistribution of the Library by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Library.
If any portion of this section is held invalid or unenforceable under any
particular circumstance, the balance of the section is intended to apply,
and the section as a whole is intended to apply in other circumstances.
It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.
This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.
  12. If the distribution and/or use of the Library is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Library under this License may add
an explicit geographical distribution limitation excluding those countries,
so that distribution is permitted only in or among countries not thus
excluded.  In such case, this License incorporates the limitation as if
written in the body of this License.
  13. The Free Software Foundation may publish revised and/or new
versions of the Lesser General Public License from time to time.
Such new versions will be similar in spirit to the present version,
but may differ in detail to address new problems or concerns.
Each version is given a distinguishing version number.  If the Library
specifies a version number of this License which applies to it and
"any later version", you have the option of following the terms and
conditions either of that version or of any later version published by
the Free Software Foundation.  If the Library does not specify a
license version number, you may choose any version ever published by
the Free Software Foundation.
  14. If you wish to incorporate parts of the Library into other free
programs whose distribution conditions are incompatible with these,
write to the author to ask for permission.  For software which is
copyrighted by the Free Software Foundation, write to the Free
Software Foundation; we sometimes make exceptions for this.  Our
decision will be guided by the two goals of preserving the free status
of all derivatives of our free software and of promoting the sharing
and reuse of software generally.
                            NO WARRANTY
  15. BECAUSE THE LIBRARY IS LICENSED FREE OF CHARGE, THERE IS NO
WARRANTY FOR THE LIBRARY, TO THE EXTENT PERMITTED BY APPLICABLE LAW.
EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR
OTHER PARTIES PROVIDE THE LIBRARY "AS IS" WITHOUT WARRANTY OF ANY
KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE
LIBRARY IS WITH YOU.  SHOULD THE LIBRARY PROVE DEFECTIVE, YOU ASSUME
THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
  16. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN
WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY
AND/OR REDISTRIBUTE THE LIBRARY AS PERMITTED ABOVE, BE LIABLE TO YOU
FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR
CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE
LIBRARY (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING
RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A
FAILURE OF THE LIBRARY TO OPERATE WITH ANY OTHER SOFTWARE), EVEN IF
SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
DAMAGES.
                     END OF TERMS AND CONDITIONS
           How to Apply These Terms to Your New Libraries
  If you develop a new library, and you want it to be of the greatest
possible use to the public, we recommend making it free software that
everyone can redistribute and change.  You can do so by permitting
redistribution under these terms (or, alternatively, under the terms of the
ordinary General Public License).
  To apply these terms, attach the following notices to the library.  It is
safest to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least the
"copyright" line and a pointer to where the full notice is found.
    <one line to give the library's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>
    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.
    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.
    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
Also add information on how to contact you by electronic and paper mail.
You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the library, if
necessary.  Here is a sample; alter the names:
  Yoyodyne, Inc., hereby disclaims all copyright interest in the
  library `Frob' (a library for tweaking knobs) written by James Random Hacker.
  <signature of Ty Coon>, 1 April 1990
  Ty Coon, President of Vice
That's all there is to it!
================================================

File: README.md
================================================
![PHPMailer](https://raw.github.com/PHPMailer/PHPMailer/master/examples/images/phpmailer.png)
# PHPMailer - A full-featured email creation and transfer class for PHP
Build status: [![Build Status](https://travis-ci.org/PHPMailer/PHPMailer.svg)](https://travis-ci.org/PHPMailer/PHPMailer)
[![Scrutinizer Quality Score](https://scrutinizer-ci.com/g/PHPMailer/PHPMailer/badges/quality-score.png?s=3758e21d279becdf847a557a56a3ed16dfec9d5d)](https://scrutinizer-ci.com/g/PHPMailer/PHPMailer/)
[![Code Coverage](https://scrutinizer-ci.com/g/PHPMailer/PHPMailer/badges/coverage.png?s=3fe6ca5fe8cd2cdf96285756e42932f7ca256962)](https://scrutinizer-ci.com/g/PHPMailer/PHPMailer/)
[![Latest Stable Version](https://poser.pugx.org/phpmailer/phpmailer/v/stable.svg)](https://packagist.org/packages/phpmailer/phpmailer) [![Total Downloads](https://poser.pugx.org/phpmailer/phpmailer/downloads)](https://packagist.org/packages/phpmailer/phpmailer) [![Latest Unstable Version](https://poser.pugx.org/phpmailer/phpmailer/v/unstable.svg)](https://packagist.org/packages/phpmailer/phpmailer) [![License](https://poser.pugx.org/phpmailer/phpmailer/license.svg)](https://packagist.org/packages/phpmailer/phpmailer) [![API Docs](https://github.com/phpmailer/phpmailer/workflows/Docs/badge.svg)](http://phpmailer.github.io/PHPMailer/)
## Class Features
- Probably the world's most popular code for sending email from PHP!
- Used by many open-source projects: WordPress, Drupal, 1CRM, SugarCRM, Yii, Joomla! and many more
- Integrated SMTP support - send without a local mail server
- Send emails with multiple To, CC, BCC and Reply-to addresses
- Multipart/alternative emails for mail clients that do not read HTML email
- Add attachments, including inline
- Support for UTF-8 content and 8bit, base64, binary, and quoted-printable encodings
- SMTP authentication with LOGIN, PLAIN, CRAM-MD5, and XOAUTH2 mechanisms over SSL and SMTP+STARTTLS transports
- Validates email addresses automatically
- Protect against header injection attacks
- Error messages in over 50 languages!
- DKIM and S/MIME signing support
- Compatible with PHP 5.5 and later
- Namespaced to prevent name clashes
- Much more!
## Why you might need it
Many PHP developers need to send email from their code. The only PHP function that supports this is [`mail()`](https://www.php.net/manual/en/function.mail.php). However, it does not provide any assistance for making use of popular features such as encryption, authentication, HTML messages, and attachments.
Formatting email correctly is surprisingly difficult. There are myriad overlapping RFCs, requiring tight adherence to horribly complicated formatting and encoding rules – the vast majority of code that you'll find online that uses the `mail()` function directly is just plain wrong!
*Please* don't be tempted to do it yourself – if you don't use PHPMailer, there are many other excellent libraries that you should look at before rolling your own. Try [SwiftMailer](https://swiftmailer.symfony.com/), [Zend/Mail](https://zendframework.github.io/zend-mail/), [ZetaComponents](https://github.com/zetacomponents/Mail) etc.
The PHP `mail()` function usually sends via a local mail server, typically fronted by a `sendmail` binary on Linux, BSD, and macOS platforms, however, Windows usually doesn't include a local mail server; PHPMailer's integrated SMTP implementation allows email sending on Windows platforms without a local mail server.
## License
This software is distributed under the [LGPL 2.1](http://www.gnu.org/licenses/lgpl-2.1.html) license, along with the [GPL Cooperation Commitment](https://gplcc.github.io/gplcc/). Please read LICENSE for information on the software availability and distribution.
## Installation & loading
PHPMailer is available on [Packagist](https://packagist.org/packages/phpmailer/phpmailer) (using semantic versioning), and installation via [Composer](https://getcomposer.org) is the recommended way to install PHPMailer. Just add this line to your `composer.json` file:
```json
"phpmailer/phpmailer": "~6.1"
```
or run
```sh
composer require phpmailer/phpmailer
```
Note that the `vendor` folder and the `vendor/autoload.php` script are generated by Composer; they are not part of PHPMailer.
If you want to use the Gmail XOAUTH2 authentication class, you will also need to add a dependency on the `league/oauth2-client` package in your `composer.json`.
Alternatively, if you're not using Composer, copy the contents of the PHPMailer folder into one of the `include_path` directories specified in your PHP configuration and load each class file manually:
```php
<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
require 'path/to/PHPMailer/src/Exception.php';
require 'path/to/PHPMailer/src/PHPMailer.php';
require 'path/to/PHPMailer/src/SMTP.php';
```
If you're not using the `SMTP` class explicitly (you're probably not), you don't need a `use` line for the SMTP class.
If you don't speak git or just want a tarball, click the 'zip' button on the right of the project page in GitHub, though note that docs and examples are not included in the tarball.
## Legacy versions
PHPMailer 5.2 (which is compatible with PHP 5.0 - 7.0) is no longer being supported, even for security updates. You will find the latest version of 5.2 in the [5.2-stable branch](https://github.com/PHPMailer/PHPMailer/tree/5.2-stable). If you're using PHP 5.5 or later (which you should be), switch to the 6.x releases.
### Upgrading from 5.2
The biggest changes are that source files are now in the `src/` folder, and PHPMailer now declares the namespace `PHPMailer\PHPMailer`. This has several important effects – [read the upgrade guide](https://github.com/PHPMailer/PHPMailer/tree/master/UPGRADING.md) for more details.
### Minimal installation
While installing the entire package manually or with Composer is simple, convenient, and reliable, you may want to include only vital files in your project. At the very least you will need [src/PHPMailer.php](https://github.com/PHPMailer/PHPMailer/tree/master/src/PHPMailer.php). If you're using SMTP, you'll need [src/SMTP.php](https://github.com/PHPMailer/PHPMailer/tree/master/src/SMTP.php), and if you're using POP-before SMTP, you'll need [src/POP3.php](https://github.com/PHPMailer/PHPMailer/tree/master/src/POP3.php). You can skip the [language](https://github.com/PHPMailer/PHPMailer/tree/master/language/) folder if you're not showing errors to users and can make do with English-only errors. If you're using XOAUTH2 you will need [src/OAuth.php](https://github.com/PHPMailer/PHPMailer/tree/master/src/OAuth.php) as well as the Composer dependencies for the services you wish to authenticate with. Really, it's much easier to use Composer!
## A Simple Example
```php
<?php
// Import PHPMailer classes into the global namespace
// These must be at the top of your script, not inside a function
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;
// Load Composer's autoloader
require 'vendor/autoload.php';
// Instantiation and passing `true` enables exceptions
$mail = new PHPMailer(true);
try {
    //Server settings
    $mail->SMTPDebug = SMTP::DEBUG_SERVER;                      // Enable verbose debug output
    $mail->isSMTP();                                            // Send using SMTP
    $mail->Host       = 'smtp1.example.com';                    // Set the SMTP server to send through
    $mail->SMTPAuth   = true;                                   // Enable SMTP authentication
    $mail->Username   = 'user@example.com';                     // SMTP username
    $mail->Password   = 'secret';                               // SMTP password
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;         // Enable TLS encryption; `PHPMailer::ENCRYPTION_SMTPS` encouraged
    $mail->Port       = 587;                                    // TCP port to connect to, use 465 for `PHPMailer::ENCRYPTION_SMTPS` above
    //Recipients
    $mail->setFrom('from@example.com', 'Mailer');
    $mail->addAddress('joe@example.net', 'Joe User');     // Add a recipient
    $mail->addAddress('ellen@example.com');               // Name is optional
    $mail->addReplyTo('info@example.com', 'Information');
    $mail->addCC('cc@example.com');
    $mail->addBCC('bcc@example.com');
    // Attachments
    $mail->addAttachment('/var/tmp/file.tar.gz');         // Add attachments
    $mail->addAttachment('/tmp/image.jpg', 'new.jpg');    // Optional name
    // Content
    $mail->isHTML(true);                                  // Set email format to HTML
    $mail->Subject = 'Here is the subject';
    $mail->Body    = 'This is the HTML message body <b>in bold!</b>';
    $mail->AltBody = 'This is the body in plain text for non-HTML mail clients';
    $mail->send();
    echo 'Message has been sent';
} catch (Exception $e) {
    echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
}
```
You'll find plenty more to play with in the [examples](https://github.com/PHPMailer/PHPMailer/tree/master/examples) folder.
If you are re-using the instance (e.g. when sending to a mailing list), you may need to clear the recipient list to avoid sending duplicate messages. See [the mailing list example](https://github.com/PHPMailer/PHPMailer/blob/master/examples/mailing_list.phps) for further guidance.
That's it. You should now be ready to use PHPMailer!
## Localization
PHPMailer defaults to English, but in the [language](https://github.com/PHPMailer/PHPMailer/tree/master/language/) folder you'll find many translations for PHPMailer error messages that you may encounter. Their filenames contain [ISO 639-1](http://en.wikipedia.org/wiki/ISO_639-1) language code for the translations, for example `fr` for French. To specify a language, you need to tell PHPMailer which one to use, like this:
```php
// To load the French version
$mail->setLanguage('fr', '/optional/path/to/language/directory/');
```
We welcome corrections and new languages - if you're looking for corrections to do, run the [PHPMailerLangTest.php](https://github.com/PHPMailer/PHPMailer/tree/master/test/PHPMailerLangTest.php) script in the tests folder and it will show any missing translations.
## Documentation
Start reading at the [GitHub wiki](https://github.com/PHPMailer/PHPMailer/wiki). If you're having trouble, this should be the first place you look as it's the most frequently updated.
Examples of how to use PHPMailer for common scenarios can be found in the [examples](https://github.com/PHPMailer/PHPMailer/tree/master/examples) folder. If you're looking for a good starting point, we recommend you start with [the Gmail example](https://github.com/PHPMailer/PHPMailer/tree/master/examples/gmail.phps).
Note that in order to reduce PHPMailer's deployed code footprint, the examples are no longer included if you load PHPMailer via Composer or via [GitHub's zip file download](https://github.com/PHPMailer/PHPMailer/archive/master.zip), so you'll need to either clone the git repository or use the above links to get to the examples directly.
Complete generated API documentation is [available online](http://phpmailer.github.io/PHPMailer/).
You can generate complete API-level documentation by running `phpdoc` in the top-level folder, and documentation will appear in the `docs` folder, though you'll need to have [PHPDocumentor](http://www.phpdoc.org) installed. You may find [the unit tests](https://github.com/PHPMailer/PHPMailer/blob/master/test/PHPMailerTest.php) a good source of how to do various operations such as encryption.
If the documentation doesn't cover what you need, search the [many questions on Stack Overflow](http://stackoverflow.com/questions/tagged/phpmailer), and before you ask a question about "SMTP Error: Could not connect to SMTP host.", [read the troubleshooting guide](https://github.com/PHPMailer/PHPMailer/wiki/Troubleshooting).
## Tests
There is a PHPUnit test script in the [test](https://github.com/PHPMailer/PHPMailer/tree/master/test/) folder. PHPMailer uses PHPUnit 4.8 - we would use 5.x but we need to run on PHP 5.5.
Build status: [![Build Status](https://travis-ci.org/PHPMailer/PHPMailer.svg)](https://travis-ci.org/PHPMailer/PHPMailer)
If this isn't passing, is there something you can do to help?
## Security
Please disclose any vulnerabilities found responsibly - report any security problems found to the maintainers privately.
PHPMailer versions prior to 5.2.22 (released January 9th 2017) have a local file disclosure vulnerability, [CVE-2017-5223](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-5223). If content passed into `msgHTML()` is sourced from unfiltered user input, relative paths can map to absolute local file paths and added as attachments. Also note that `addAttachment` (just like `file_get_contents`, `passthru`, `unlink`, etc) should not be passed user-sourced params either! Reported by Yongxiang Li of Asiasecurity.
PHPMailer versions prior to 5.2.20 (released December 28th 2016) are vulnerable to [CVE-2016-10045](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2016-10045) a remote code execution vulnerability, responsibly reported by [Dawid Golunski](https://legalhackers.com/advisories/PHPMailer-Exploit-Remote-Code-Exec-CVE-2016-10045-Vuln-Patch-Bypass.html), and patched by Paul Buonopane (@Zenexer).
PHPMailer versions prior to 5.2.18 (released December 2016) are vulnerable to [CVE-2016-10033](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2016-10033) a critical remote code execution vulnerability, responsibly reported by [Dawid Golunski](http://legalhackers.com/advisories/PHPMailer-Exploit-Remote-Code-Exec-CVE-2016-10033-Vuln.html).
See [SECURITY](https://github.com/PHPMailer/PHPMailer/tree/master/SECURITY.md) for more detail on security issues.
## Contributing
Please submit bug reports, suggestions and pull requests to the [GitHub issue tracker](https://github.com/PHPMailer/PHPMailer/issues).
We're particularly interested in fixing edge-cases, expanding test coverage and updating translations.
If you found a mistake in the docs, or want to add something, go ahead and amend the wiki - anyone can edit it.
If you have git clones from prior to the move to the PHPMailer GitHub organisation, you'll need to update any remote URLs referencing the old GitHub location with a command like this from within your clone:
```sh
git remote set-url upstream https://github.com/PHPMailer/PHPMailer.git
```
Please *don't* use the SourceForge or Google Code projects any more; they are obsolete and no longer maintained.
## Sponsorship
Development time and resources for PHPMailer are provided by [Smartmessages.net](https://info.smartmessages.net/), a powerful email marketing system.
<a href="https://info.smartmessages.net/"><img src="https://www.smartmessages.net/img/smartmessages-logo.svg" width="250" height="28" alt="Smartmessages email marketing"></a>
Other contributions are gladly received, whether in beer 🍺, T-shirts 👕, Amazon wishlist raids, or cold, hard cash 💰. If you'd like to donate to say "thank you" to maintainers or contributors, please contact them through individual profile pages via [the contributors page](https://github.com/PHPMailer/PHPMailer/graphs/contributors).
## Changelog
See [changelog](changelog.md).
## History
- PHPMailer was originally written in 2001 by Brent R. Matzelle as a [SourceForge project](http://sourceforge.net/projects/phpmailer/).
- Marcus Bointon (coolbru on SF) and Andy Prevost (codeworxtech) took over the project in 2004.
- Became an Apache incubator project on Google Code in 2010, managed by Jim Jagielski.
- Marcus created his fork on [GitHub](https://github.com/Synchro/PHPMailer) in 2008.
- Jim and Marcus decide to join forces and use GitHub as the canonical and official repo for PHPMailer in 2013.
- PHPMailer moves to the [PHPMailer organisation](https://github.com/PHPMailer) on GitHub in 2013.
### What's changed since moving from SourceForge?
- Official successor to the SourceForge and Google Code projects.
- Test suite.
- Continuous integration with Travis-CI.
- Composer support.
- Public development.
- Additional languages and language strings.
- CRAM-MD5 authentication support.
- Preserves full repo history of authors, commits and branches from the original SourceForge project.
================================================

File: SECURITY.md
================================================
# Security notices relating to PHPMailer
Please disclose any vulnerabilities found responsibly - report any security problems found to the maintainers privately.
PHPMailer versions 6.1.5 and earlier contain an output escaping bug that occurs in `Content-Type` and `Content-Disposition` when filenames passed into `addAttachment` and other methods that accept attachment names contain double quote characters, in contravention of RFC822 3.4.1. No specific vulnerability has been found relating to this, but it could allow file attachments to bypass attachment filters that are based on matching filename extensions. Recorded as [CVE-2020-13625](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2020-13625). Reported by Elar Lang of Clarified Security.
PHPMailer versions prior to 6.0.6 and 5.2.27 are vulnerable to an object injection attack by passing `phar://` paths into `addAttachment()` and other functions that may receive unfiltered local paths, possibly leading to RCE. Recorded as [CVE-2018-19296](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-19296). See [this article](https://knasmueller.net/5-answers-about-php-phar-exploitation) for more info on this type of vulnerability. Mitigated by blocking the use of paths containing URL-protocol style prefixes such as `phar://`. Reported by Sehun Oh of cyberone.kr.
PHPMailer versions prior to 5.2.24 (released July 26th 2017) have an XSS vulnerability in one of the code examples, [CVE-2017-11503](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-11503). The `code_generator.phps` example did not filter user input prior to output. This file is distributed with a `.phps` extension, so it it not normally executable unless it is explicitly renamed, and the file is not included when PHPMailer is loaded through composer, so it is safe by default. There was also an undisclosed potential XSS vulnerability in the default exception handler (unused by default). Patches for both issues kindly provided by Patrick Monnerat of the Fedora Project.
PHPMailer versions prior to 5.2.22 (released January 9th 2017) have a local file disclosure vulnerability, [CVE-2017-5223](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-5223). If content passed into `msgHTML()` is sourced from unfiltered user input, relative paths can map to absolute local file paths and added as attachments. Also note that `addAttachment` (just like `file_get_contents`, `passthru`, `unlink`, etc) should not be passed user-sourced params either! Reported by Yongxiang Li of Asiasecurity.
PHPMailer versions prior to 5.2.20 (released December 28th 2016) are vulnerable to [CVE-2016-10045](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2016-10045) a remote code execution vulnerability, responsibly reported by [Dawid Golunski](https://legalhackers.com/advisories/PHPMailer-Exploit-Remote-Code-Exec-CVE-2016-10045-Vuln-Patch-Bypass.html), and patched by Paul Buonopane (@Zenexer).
PHPMailer versions prior to 5.2.18 (released December 2016) are vulnerable to [CVE-2016-10033](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2016-10033) a remote code execution vulnerability, responsibly reported by [Dawid Golunski](http://legalhackers.com/advisories/PHPMailer-Exploit-Remote-Code-Exec-CVE-2016-10033-Vuln.html).
PHPMailer versions prior to 5.2.14 (released November 2015) are vulnerable to [CVE-2015-8476](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-8476) an SMTP CRLF injection bug permitting arbitrary message sending.
PHPMailer versions prior to 5.2.10 (released May 2015) are vulnerable to [CVE-2008-5619](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2008-5619), a remote code execution vulnerability in the bundled html2text library. This file was removed in 5.2.10, so if you are using a version prior to that and make use of the html2text function, it's vitally important that you upgrade and remove this file.
PHPMailer versions prior to 2.0.7 and 2.2.1 are vulnerable to [CVE-2012-0796](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2012-0796), an email header injection attack.
Joomla 1.6.0 uses PHPMailer in an unsafe way, allowing it to reveal local file paths, reported in [CVE-2011-3747](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2011-3747).
PHPMailer didn't sanitise the `$lang_path` parameter in `SetLanguage`. This wasn't a problem in itself, but some apps (PHPClassifieds, ATutor) also failed to sanitise user-provided parameters passed to it, permitting semi-arbitrary local file inclusion, reported in [CVE-2010-4914](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2010-4914), [CVE-2007-2021](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2007-2021) and [CVE-2006-5734](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2006-5734).
PHPMailer 1.7.2 and earlier contained a possible DDoS vulnerability reported in [CVE-2005-1807](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2005-1807).
PHPMailer 1.7 and earlier (June 2003) have a possible vulnerability in the `SendmailSend` method where shell commands may not be sanitised. Reported in [CVE-2007-3215](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2007-3215).
================================================
# Repository Information
Name: mikrotik-hotspot-webinterface

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
	url = https://gitlab.com/stroebs/mikrotik-hotspot-webinterface.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: alogin.html
================================================
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Mikrotik Hotspot</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/custom.css" rel="stylesheet">
</head>
<body>
<div id="wrap">
    <div class="navbar navbar-default navbar-static-top" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">$(identity)</a>
            </div>
            <div class="collapse navbar-collapse">
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="login">Login</a></li>
                    <li><a href="status">Status</a></li>
                    <li><a href="logout?erase-cookie=true">Logout</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="row">
            <div class="alert alert-success">
                You are logged in successfully. If nothing happens, click <a href="$(link-status)">here</a>.
            </div>
        </div>
    </div>
</div>
<div id="footer">
    <div class="container">
        <p class="text-muted">Powered by MikroTik RouterOS</p>
    </div>
</div>
<script type="text/javascript" src="js/jquery.min.js"></script>
<script type="text/javascript" src="js/bootstrap.min.js"></script>
</body>
</html>
================================================

File: custom.css
================================================
html, body {
    height: 100%;
}
/* Wrapper for page content to push down footer */
#wrap {
    min-height: 100%;
    height: auto;
    margin: 0 auto -60px;
    padding: 0 0 60px;
}
/* Set the fixed height of the footer here */
#footer {
    height: 60px;
    background-color: #f5f5f5;
}
#wrap > .container {
    padding: 60px 15px 0;
}
.container .text-muted {
    margin: 20px 0;
}
#footer > .container {
    padding-left: 15px;
    padding-right: 15px;
}
code {
    font-size: 80%;
}
================================================

File: error.html
================================================
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Mikrotik Hotspot | Error</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/custom.css" rel="stylesheet">
</head>
<body>
<div id="wrap">
    <div class="navbar navbar-default navbar-static-top" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">$(identity)</a>
            </div>
            <div class="collapse navbar-collapse">
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="login">Login</a></li>
                    <li><a href="status">Status</a></li>
                    <li><a href="logout?erase-cookie=true">Logout</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="row">
            <div class="alert alert-danger">
                Hotspot ERROR: $(error).
            </div>
            <div class="alert alert-info">
                Login page: <a href="$(link-login)">$(link-login)</a>
            </div>
        </div>
    </div>
</div>
<div id="footer">
    <div class="container">
        <p class="text-muted">Powered by MikroTik RouterOS</p>
    </div>
</div>
<script type="text/javascript" src="js/jquery.min.js"></script>
<script type="text/javascript" src="js/bootstrap.min.js"></script>
</body>
</html>
================================================

File: LICENSE.md
================================================
The MIT License (MIT)
Copyright (c) 2013 Johannes Graf
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
================================================

File: login.html
================================================
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Mikrotik Hotspot | Login</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/custom.css" rel="stylesheet">
</head>
<body>
<div id="wrap">
    <div class="navbar navbar-default navbar-static-top" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">$(identity)</a>
            </div>
            <div class="collapse navbar-collapse">
                <ul class="nav navbar-nav navbar-right">
                    <li class="active"><a href="login">Login</a></li>
                    <li><a href="status">Status</a></li>
                    <li><a href="logout?erase-cookie=true">Logout</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="row">
            $(if error)
                <div class="alert alert-danger">$(error)</div>
            $(endif)
            <div class="alert alert-info">Please log on to use the hotspot service.</div>
            $(if trial == 'yes')
                <div class="alert alert-info">
                    Free trial available, <a href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">click here</a>.
                </div>
            $(endif)
        </div>
        <div class="row">
            <div class="panel panel-default">
                <div class="panel-body">
                    <form id="loginForm" class="form-horizontal" role="form" action="$(link-login-only)" method="post">
                        <input type="hidden" name="dst" value="$(link-orig)"/>
                        <input type="hidden" name="popup" value="true"/>
                        <div class="form-group">
                            <label for="inputLogin" class="col-sm-1 control-label">Login</label>
                            <div class="col-sm-11">
                                <input type="text" class="form-control input-lg" id="inputLogin" name="username"
                                       placeholder="Login" autofocus required>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="inputPassword" class="col-sm-1 control-label">Password</label>
                            <div class="col-sm-11">
                                <input type="password" class="form-control input-lg" id="inputPassword" name="password"
                                       placeholder="Password" required>
                            </div>
                        </div>
                        <div class="form-group">
                            <div class="col-sm-offset-1 col-sm-11">
                                <button type="submit" class="btn btn-primary btn-block btn-lg">OK</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
<div id="footer">
    <div class="container">
        <p class="text-muted">Powered by MikroTik RouterOS</p>
    </div>
</div>
<script type="text/javascript" src="js/jquery.min.js"></script>
<script type="text/javascript" src="js/bootstrap.min.js"></script>
$(if chap-id)
    <script type="text/javascript" src="js/md5.js"></script>
    <script type="text/javascript">
        $('#loginForm').submit(function () {
            var password = $('#inputPassword');
            password.val(hexMD5('$(chap-id)' + password.val() + '$(chap-challenge)'));
        });
    </script>
$(endif)
</body>
</html>
================================================

File: logout.html
================================================
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Mikrotik Hotspot | Logout</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/custom.css" rel="stylesheet">
</head>
<body>
<div id="wrap">
    <div class="navbar navbar-default navbar-static-top" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">$(identity)</a>
            </div>
            <div class="collapse navbar-collapse">
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="login">Login</a></li>
                    <li><a href="status">Status</a></li>
                    <li class="active"><a href="logout?erase-cookie=true">Logout</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="row">
            $(if error)
                <div class="alert alert-danger">$(error)</div>
            $(endif)
            <div class="alert alert-success">You have just logged out.</div>
        </div>
        <div class="row">
            <div class="panel panel-default">
                <div class="panel-body">
                    <table class="table table-striped">
                        <tbody>
                        <tr>
                            <td>user name</td>
                            <td>$(username)</td>
                        </tr>
                        <tr>
                            <td>IP address</td>
                            <td>$(ip)</td>
                        </tr>
                        <tr>
                            <td>MAC address</td>
                            <td>$(mac)</td>
                        </tr>
                        <tr>
                            <td>session time</td>
                            <td>$(uptime)</td>
                        </tr>
                        $(if session-time-left)
                            <tr>
                                <td>time left</td>
                                <td>$(session-time-left)</td>
                            </tr>
                        $(endif)
                        <tr>
                            <td>bytes up/down:</td>
                            <td>$(bytes-in-nice) / $(bytes-out-nice)</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>
<div id="footer">
    <div class="container">
        <p class="text-muted">Powered by MikroTik RouterOS</p>
    </div>
</div>
<script src="js/jquery.min.js"></script>
<script src="js/bootstrap.min.js"></script>
</body>
</html>
================================================

File: README.md
================================================
mikrotik-hotspot-webinterface
=============================
This is a custom Bootstrap 3 based webinterface for a Mikrotik Hotspot. For more Details please visit http://wiki.mikrotik.com/wiki/Manual:Customizing_Hotspot
Installation
------------
Clone this repository.
* Create a folder ```js``` and put ```bootstrap.min.js``` from http://getbootstrap.com/, ```jquery.min.js``` from https://code.jquery.com/jquery.min.js into it.
* Copy fonts folder out of the bootstrap archive to root level
* Copy ```bootstrap.min.css``` into css folder
* Connect to your Routerboard via ftp, copy the ```md5.js``` into the ```js``` folder.
* Copy the hole repository folder to your Routerboard.
* Open the WebFig Interface with a browser and go to ```IP > Hotspot > Server Profiles``` and create a new Profile. Under ```HTML Directory``` select ```mikrotik-hotspot-webinterface```.
DONE
Authors
-------
* Johannes Graf ([@grafjo](https://github.com/grafjo))
License
-------
mikrotik-hotspot-webinterface is released under the MIT License. See the bundled LICENSE file
for details.
================================================

File: status.html
================================================
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Mikrotik Hotspot | Session Status</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/custom.css" rel="stylesheet">
</head>
<body>
<div id="wrap">
    <div class="navbar navbar-default navbar-static-top" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">$(identity)</a>
            </div>
            <div class="collapse navbar-collapse">
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="login">Login</a></li>
                    <li class="active"><a href="#">Status</a></li>
                    <li><a href="logout?erase-cookie=true">Logout</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="row">
            $(if error)
                <div class="alert alert-danger">$(error)</div>
            $(endif)
            $(if login-by == 'trial')
                <div class="alert alert-info">Welcome trial user!</div>
            $(elif login-by != 'mac')
                <div class="alert alert-info">Welcome $(username)!</div>
            $(endif)
        </div>
        <div class="row">
            <div class="panel panel-default">
                <div class="panel-body">
                    <table class="table table-striped">
                        <tbody>
                        <tr>
                            <td>IP address:</td>
                            <td>$(ip)</td>
                        </tr>
                        <tr>
                            <td>bytes up/down</td>
                            <td>$(bytes-in-nice) / $(bytes-out-nice)</td>
                        </tr>
                        $(if session-time-left)
                        <tr>
                            <td>connected / left:</td>
                            <td>$(uptime) / $(session-time-left)</td>
                        </tr>
                        $(else)
                        <tr>
                            <td>connected:</td>
                            <td>$(uptime)</td>
                        </tr>
                        $(endif)
                        $(if refresh-timeout)
                        <tr>
                            <td>status refresh</td>
                            <td>$(refresh-timeout)</td>
                            $(endif)
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>
<div id="footer">
    <div class="container">
        <p class="text-muted">Powered by MikroTik RouterOS</p>
    </div>
</div>
<script src="js/jquery.min.js"></script>
<script src="js/bootstrap.min.js"></script>
</body>
</html>
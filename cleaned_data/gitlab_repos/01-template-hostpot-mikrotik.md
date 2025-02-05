# Repository Information
Name: 01-template-hostpot-mikrotik

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
	url = https://gitlab.com/klinikasura/01-template-hostpot-mikrotik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: alogin.html
================================================
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><style> .loader {margin: 60px auto;font-size: 10px;position: relative;text-indent: -9999em;border-top: 1.1em solid rgba(145,145,146, 0.2);border-right: 1.1em solid rgba(145,145,146, 0.2);border-bottom: 1.1em solid rgba(145,145,146, 0.2);border-left: 1.1em solid #919192;-webkit-transform: translateZ(0);-ms-transform: translateZ(0);transform: translateZ(0);-webkit-animation: load8 1.1s infinite linear;animation: load8 1.1s infinite linear;}.loader,.loader:after {border-radius: 50%;width: 10em;height: 10em;}@-webkit-keyframes load8 {0% {-webkit-transform: rotate(0deg);transform: rotate(0deg);}100% {-webkit-transform: rotate(360deg);transform: rotate(360deg);}}@keyframes load8 {0% {-webkit-transform: rotate(0deg);transform: rotate(0deg);}100% {-webkit-transform: rotate(360deg);transform: rotate(360deg);}}</style><title>Hotspot RS. Asura</title><meta http-equiv="refresh" content="4; url=$(link-redirect)"><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"><meta http-equiv="pragma" content="no-cache"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta http-equiv="expires" content="-1"><style type="text/css">
textarea,input,select {background-color: #FDFBFB;border: 1px #BBBBBB solid;padding: 2px;margin: 1px;font-size: 14px;color: #808080;}body{
	color: #737373;
	font-size: 12px;
	font-family: verdana;
	background-image: url();
}a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }img {border: none;}td { font-size: 12px; color: #7A7A7A; }.style3 {
	font-size: 18px;
	color: #666666;
}
.style4 {
	font-size: 14px;
	color: #666666;
}
.style5 {color: #666666}
</style><script language="JavaScript">function startClock() {$(if popup == 'true')open('$(link-status)', 'hotspot_status', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=290');$(endif)location.href = 'http://192.168.88.203/dashboard',500;}</script></head>
<body style="width: 100%;" onLoad="startClock()"><table style="background-color: transparent; width: 100%; margin-left: 0px; height: 100%;"><tbody><tr><td bordercolor="#999999" bgcolor="#999999" style="vertical-align: middle; background-color: white; text-align: center; margin-top: 20%; height: 100%;"><h1><b><img src="logo.jpg" width="99" height="115"></b></h1>
        <h1>RS. ASURA</h1>
        <div class="container">
          <div class="col-sm-4 col-sm-offset-4">
            <center>
              <h4><b>LOGIN BERHASIL</b></h4>
              <p><span style="color: #333333"> Aplikasi Ini Dikembangkan Oleh IT Managemen Desain Hamba Alloh</p>
            </center>
          </div>
        </div>
        <div class="loader">Loading...</div>
        <p>RS. ASURA</p>
        <p>Aplikasi Versi 6.0</p>        </td>
</tr></tbody></table></body></html>
================================================

File: error.html
================================================
<html>
<head>
<title>Hotspot RS. Asura</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}
body{
	color: #737373;
	font-size: 12px;
	font-family: verdana;
	background-image: url(TEMA.gif);
}
a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }
.style1 {color: #FFFFFF}
-->
</style>
</head>
<body>
<table width="100%" height="100%">
<tr>
<td align="center" valign="middle"><h1><b><img src="logo.jpg" width="86" height="90"></b></h1>
  <h1 class="style1">RS. ASURA</h1>
  <div class="container style1">
    <div class="col-sm-4 col-sm-offset-4">
      <center>
        <h4>Aplikasi Ini Dikembangkan Oleh IT Managemen Desain Hamba Alloh</h4>
        </center>
    </div>
  </div>
  <p class="style1"><strong>ERROR</strong></p>
  <p class="style1">Hotspot ERROR: $(error)<br>
        <br>
    Login page: <a href="$(link-login)">$(link-login)</a></p>
  <p class="style1">RS. ASURA</p>
  <p class="style1">Aplikasi Versi 6.0</p></td>
</tr>
</table>
</body>
</html>
================================================

File: errors.txt
================================================
# This file contains error messages which are shown to user, when http/https
# login is used.
# These messages can be changed to make user interface more friendly, including
# translations to different languages.
#
# Various variables can be used here as well. Most frequently used ones are:
#	$(error-orig)	- original error message from hotspot
#	$(ip)		- ip address of a client
#	$(username)	- username of client trying to log in
# internal-error
# It should never happen. If it will, error page will be shown
# displaying this error message (error-orig will describe what has happened)
internal-error = internal error ($(error-orig))
# config-error
# Should never happen if hotspot is configured properly.
config-error = configuration error ($(error-orig))
# not-logged-in
# Will happen, if status or logout page is requested by user,
# which actually is not logged in
not-logged-in = you are not logged in (ip $(ip))
# ippool-empty
# IP address for user is to be assigned from ip pool, but there are no more
# addresses in that pool
ippool-empty = cannot assign ip address - no more free addresses from pool
# shutting-down
# When shutdown is executed, new clients are not accepted
shutting-down = hotspot service is shutting down
# user-session-limit
# If user profile has limit of shared-users, then this error will be shown
# after reaching this limit
user-session-limit = no more sessions are allowed for user $(username)
# license-session-limit
# Depending on licence number of active hotspot clients is limited to
# one or another amount. If this limit is reached, following error is displayed.
license-session-limit = session limit reached ($(error-orig))
# wrong-mac-username
# If username looks like MAC address (12:34:56:78:9a:bc), but is not
# a MAC address of this client, login is rejected
wrong-mac-username = invalid username ($(username)): this MAC address is not yours
# chap-missing
# If http-chap login method is used, but hotspot program does not receive
# back encrypted password, this error message is shown.
# Possible reasons of failure:
#	- JavaScript is not enabled in web browser;
#	- login.html page is not valid;
#	- challenge value has expired on server (more than 1h of inactivity);
#	- http-chap login method is recently removed;
# If JavaScript is enabled and login.html page is valid,
# then retrying to login usually fixes this problem.
chap-missing = web browser did not send challenge response (try again, enable JavaScript)
# invalid-username
# Most general case of invalid username or password. If RADIUS server
# has sent an error string with Access-Reject message, then it will
# override this setting.
invalid-username = invalid username or password
# invalid-mac
# Local users (on hotspot server) can be bound to some MAC address. If login
# from different MAC is tried, this error message will be shown.
invalid-mac = user $(username) is not allowed to log in from this MAC address
# uptime-limit, traffic-limit
# For local hotspot users in case if limits are reached
uptime-limit = user $(username) has reached uptime limit
traffic-limit = user $(username) has reached traffic limit
# radius-timeout
# User is authenticated by RADIUS server, but no response is received from it,
# following error will be shown.
radius-timeout = RADIUS server is not responding
# auth-in-progress
# Authorization in progress. Client already has issued an authorization request
# which is not yet complete.
auth-in-progress = already authorizing, retry later
# radius-reply
# Radius server returned some custom error message
radius-reply = $(error-orig)
================================================

File: login.css
================================================
body {
    background: linear-gradient(#000000, #000000);
min-width: 300px;
}
.logo
{
width:200px;
position: relative;
top:20px;
}
.login{font-family:arial;padding:90px 0 0 0}.login .logo{display:block;border-radius: 10px;margin:0 auto 30px}.login a,.login a:visited{text-decoration:underline;color:inherit}ul.notice{margin:30px auto;width:200px;text-align:center;list-style-position:inside;font-size:15px;padding:20px 30px;border-radius:3px}ul.notice.errors{background-color:#fff4f4;border:1px solid #f50909;color:#f50909}ul.notice.success{background-color:#d7eacd;border:1px solid #6fae4f;color:#6fae4f}ul.notice li{padding:5px 0}.vertical-form{margin:0 auto}.vertical-form legend{width:100%;font-size:24px;font-weight:500;text-align:center;margin:0 0 30px 0}.vertical-form input[type='text'],.vertical-form input[type='password'],.vertical-form input[type='number']{border:1px #252525 solid;color:#c1c1c1;background: #252525	;opacity: 1;
    filter: alpha(opacity=95);
height:30px;font-size:14px}.vertical-form input[type='text'],.vertical-form input[type='password'],.vertical-form input[type='submit'],.vertical-form input[type='number']{display:block;margin:0 auto 8px auto;width:200px;text-align:left;border-radius:2px;color:#0CFFFF;outline:none;font-family:inherit}.vertical-form input[type='submit']{-webkit-appearance:none;color:#fff;background:#252525;
    background-image:url(lock.png);
	background-repeat: no-repeat; background-position:center;
    opacity: 1.0;
    filter: alpha(opacity=95);
    position: relative;
left:90px;top:-75px;border:5px solid #000000;border-radius:30px;text-align:center;height:60px;width:60px;font-size:11px;font-weight:400;outline:0;text-transform:uppercase;letter-spacing:1.5px;cursor:pointer}.vertical-form input:hover[type='submit']{background-color:#0CFFFF;
    background-image:url(lock.png);
	background-repeat: no-repeat; background-position:center;
    -webkit-transition:all 0.3s ease;-moz-transition:all 0.3s ease;-o-transition:all 0.3s ease;transition:all 0.3s ease}.vertical-form .footer{text-align:center}.vertical-form .footer p:first-child{color:#0CFFFF}.vertical-form .footer a:first-child{border-bottom:solid 1px #ccc;text-decoration:none}.vertical-form .footer p:nth-child(2) a{border-bottom:solid 1px #000} @media (max-width:200px){.login{padding:0px 0 0 0}}
================================================

File: login.html
================================================
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Hotspot RS. Asura</title>
<meta http-equiv="pragma" content="no-cache" />
<meta http-equiv="expires" content="-1" />	
<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0; user-scalable=0;" />
<link rel="stylesheet" href="login.css" media="screen">
 <link rel="stylesheet" href="template/css/normalize.css">
        <link rel="stylesheet" href="template/css/font-awesome.css">
        <link rel="stylesheet" href="template/css/bootstrap.min.css">
        <link rel="stylesheet" href="template/css/templatemo-style.css">
		<link href="http://192.168.88.203/dashboard/download.jpeg" rel="icon" type="image/png" />
        <script src="template/js/vendor/modernizr-2.6.2.min.js"></script>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"><style type="text/css">
<!--
body {
	background-image: url(TEMA.gif);
	background-color: #999999;
}
.style2 {color: #FFFFFF}
.style5 {font-family: Verdana, Arial, Helvetica, sans-serif}
.style8 {
	color: #000000;
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 12px;
}
.style9 {
	font-size: 18px;
	color: #00CC00;
	font-family: Verdana, Arial, Helvetica, sans-serif;
}
.style10 {font-size: 16px; color: #FFFFFF; }
.style14 {
	color: #00CC00;
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: larger;
}
.style15 {
	font-size: 16px;
	color: #00CC00;
	font-family: Verdana, Arial, Helvetica, sans-serif;
}
-->
</style></head>
<body class='login'>
$(if chap-id)
  <input type="hidden" name="username" />
  <input type="hidden" name="password" />
  <input type="hidden" name="dst" value="$(link-orig)" />
  <input type="hidden" name="popup" value="true" />
<script type="text/javascript" src="/md5.js"></script>
	<script type="text/javascript">
	<!--
	    function doLogin() {
		document.sendin.username.value = document.login.username.value;
		document.sendin.password.value = hexMD5('$(chap-id)' + document.login.password.value + '$(chap-challenge)');
		document.sendin.submit();
		return false;
	    }
	//-->
	</script>
$(endif)
<form class="vertical-form" name="login" action="$(link-login-only)" method="post" background="#A03472"
	$(if chap-id) onSubmit="return doLogin()" $(endif)>
<input type="hidden" name="dst" value="$(link-orig)" />
<input type="hidden" name="popup" value="true" />
<div style="margin:0;padding:0;display:inline"></div>
<div align="center">
  <legend></legend>
  <b><img src="logo.jpg" width="105" height="109"></b></div>
<h1 align="center" class="vertical-form style5"><span style="text-align: center;"> <span style="font-size: x-large;">
<marquee bgcolor="" style="color: white;" direction="left" width="300">
<b><br>
<span class="style14">RS. ASURA</span></b>
</marquee>
</span></h1>
<h1 align="center" class="style9">Aplikasi Ini Dikembangkan Oleh IT Managemen Desain Hamba Alloh</h1>
<p align="center" class="style10"><span class="style2"><img src="logo.gif" border="0" class="logo" /></span>
  <aqui se puede escribir>
</p>
<div align="center">
  <h1>
    <input autocomplete="on" name="username" type="text" value="$(username)" placeholder=" Username" size="15" />
    <input autocomplete="off" name="password" type="text" label="false" placeholder=" Password" size="15" />
    <span class="style8">
      <input name="submit" type="submit" value=" " />
    </span></h1>
  <p align="center" class="style15">RS. ASURA</p>
  <p align="center" class="style15">Aplikasi Versi 6.0</p>
  </div>
<div class='footer'>
<p>$(if trial == 'yes')Free trial available, <a href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">click here</a>.$(endif)</p>
<p>$(if error)<span style="color: #ffffff; font-size: 16px">$(error)</span>$(endif)</p>
<br>
<p></p>
</div>
</form>
<script type="text/javascript">
<!--
  document.login.username.focus();
//-->
</script>
<script src="template/js/vendor/jquery-1.10.2.min.js"></script>
            <script src="template/js/plugins.js"></script>
            <script src="template/js/main.js"></script>
<script type="text/javascript">
document.oncontextmenu = function(){return false;}
</script>
</body>
</html>
================================================

File: logout.html
================================================
<html>
<head>
<title>Hotspot RS. Asura</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}
.tabula{
border-width: 1px; 
border-collapse: collapse; 
border-color: #c1c1c1; 
background-color: transparent;
font-family: verdana;
font-size: 11px;
}
body{
	color: #737373;
	font-size: 12px;
	font-family: verdana;
	background-image: url(TEMA.gif);
}
a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; padding: 4px;}
.style2 {color: #666666}
.style3 {color: #FFFFFF}
-->
</style>
</head>
<body>
<script language="JavaScript">
<!--
    function openLogin() {
	if (window.name != 'hotspot_logout') return true;
	open('$(link-login)', '_blank', '');
	window.close();
	return false;
    }
//-->
</script>
<table width="100%" height="100%">
<tr>
<td align="center" valign="middle">
  <h1 class="style2"><b><img src="logo.jpg" width="86" height="90"></b></h1>
  <h1 class="style3">RS. ASURA TUGUMULYO </h1>
  <div class="container style3">
    <div class="col-sm-4 col-sm-offset-4">
      <center>
        <h4>Aplikasi Ini Dikembangkan Oleh IT Managemen Desain Hamba Alloh</h4>
        </center>
    </div>
  </div>
  <p class="style3"><strong>LOGOUT</strong><br>
  </p>
  <table border="1" class="tabula">  
<tr><td align="right" class="style3">User Name</td><td class="style3">$(username)</td></tr>
<tr><td align="right" class="style3">IP Address</td><td class="style3">$(ip)</td></tr>
<tr><td align="right" class="style3">MAC Address</td><td class="style3">$(mac)</td></tr>
<tr><td align="right" class="style3">Session Time</td><td class="style3">$(uptime)</td></tr>
$(if session-time-left)
<tr><td align="right" class="style3">Time Left</td><td class="style3">$(session-time-left)</td></tr>
$(endif)
<tr><td align="right" class="style3">Bytes UP/DOWN:</td><td class="style3">$(bytes-in-nice) / $(bytes-out-nice)</td></tr>
</table>
  <span class="style3"><br>
  </span>
  <form action="$(link-login)" name="login" class="style2" onSubmit="return openLogin()">
    <p class="style3">
      <input type="submit" value="log in">
    </p>
    <p class="style3">RS. ASURA</p>
    <p class="style3">Aplikasi Versi 6.0</p>
    <p>&nbsp;  </p>
  </form></td>
</table>
</body>
</html>
================================================

File: md5.js
================================================
/*
 * A JavaScript implementation of the RSA Data Security, Inc. MD5 Message
 * Digest Algorithm, as defined in RFC 1321.
 * Version 1.1 Copyright (C) Paul Johnston 1999 - 2002.
 * Code also contributed by Greg Holt
 * See http://pajhome.org.uk/site/legal.html for details.
 */
/*
 * Add integers, wrapping at 2^32. This uses 16-bit operations internally
 * to work around bugs in some JS interpreters.
 */
function safe_add(x, y)
{
  var lsw = (x & 0xFFFF) + (y & 0xFFFF)
  var msw = (x >> 16) + (y >> 16) + (lsw >> 16)
  return (msw << 16) | (lsw & 0xFFFF)
}
/*
 * Bitwise rotate a 32-bit number to the left.
 */
function rol(num, cnt)
{
  return (num << cnt) | (num >>> (32 - cnt))
}
/*
 * These functions implement the four basic operations the algorithm uses.
 */
function cmn(q, a, b, x, s, t)
{
  return safe_add(rol(safe_add(safe_add(a, q), safe_add(x, t)), s), b)
}
function ff(a, b, c, d, x, s, t)
{
  return cmn((b & c) | ((~b) & d), a, b, x, s, t)
}
function gg(a, b, c, d, x, s, t)
{
  return cmn((b & d) | (c & (~d)), a, b, x, s, t)
}
function hh(a, b, c, d, x, s, t)
{
  return cmn(b ^ c ^ d, a, b, x, s, t)
}
function ii(a, b, c, d, x, s, t)
{
  return cmn(c ^ (b | (~d)), a, b, x, s, t)
}
/*
 * Calculate the MD5 of an array of little-endian words, producing an array
 * of little-endian words.
 */
function coreMD5(x)
{
  var a =  1732584193
  var b = -271733879
  var c = -1732584194
  var d =  271733878
  for(i = 0; i < x.length; i += 16)
  {
    var olda = a
    var oldb = b
    var oldc = c
    var oldd = d
    a = ff(a, b, c, d, x[i+ 0], 7 , -680876936)
    d = ff(d, a, b, c, x[i+ 1], 12, -389564586)
    c = ff(c, d, a, b, x[i+ 2], 17,  606105819)
    b = ff(b, c, d, a, x[i+ 3], 22, -1044525330)
    a = ff(a, b, c, d, x[i+ 4], 7 , -176418897)
    d = ff(d, a, b, c, x[i+ 5], 12,  1200080426)
    c = ff(c, d, a, b, x[i+ 6], 17, -1473231341)
    b = ff(b, c, d, a, x[i+ 7], 22, -45705983)
    a = ff(a, b, c, d, x[i+ 8], 7 ,  1770035416)
    d = ff(d, a, b, c, x[i+ 9], 12, -1958414417)
    c = ff(c, d, a, b, x[i+10], 17, -42063)
    b = ff(b, c, d, a, x[i+11], 22, -1990404162)
    a = ff(a, b, c, d, x[i+12], 7 ,  1804603682)
    d = ff(d, a, b, c, x[i+13], 12, -40341101)
    c = ff(c, d, a, b, x[i+14], 17, -1502002290)
    b = ff(b, c, d, a, x[i+15], 22,  1236535329)
    a = gg(a, b, c, d, x[i+ 1], 5 , -165796510)
    d = gg(d, a, b, c, x[i+ 6], 9 , -1069501632)
    c = gg(c, d, a, b, x[i+11], 14,  643717713)
    b = gg(b, c, d, a, x[i+ 0], 20, -373897302)
    a = gg(a, b, c, d, x[i+ 5], 5 , -701558691)
    d = gg(d, a, b, c, x[i+10], 9 ,  38016083)
    c = gg(c, d, a, b, x[i+15], 14, -660478335)
    b = gg(b, c, d, a, x[i+ 4], 20, -405537848)
    a = gg(a, b, c, d, x[i+ 9], 5 ,  568446438)
    d = gg(d, a, b, c, x[i+14], 9 , -1019803690)
    c = gg(c, d, a, b, x[i+ 3], 14, -187363961)
    b = gg(b, c, d, a, x[i+ 8], 20,  1163531501)
    a = gg(a, b, c, d, x[i+13], 5 , -1444681467)
    d = gg(d, a, b, c, x[i+ 2], 9 , -51403784)
    c = gg(c, d, a, b, x[i+ 7], 14,  1735328473)
    b = gg(b, c, d, a, x[i+12], 20, -1926607734)
    a = hh(a, b, c, d, x[i+ 5], 4 , -378558)
    d = hh(d, a, b, c, x[i+ 8], 11, -2022574463)
    c = hh(c, d, a, b, x[i+11], 16,  1839030562)
    b = hh(b, c, d, a, x[i+14], 23, -35309556)
    a = hh(a, b, c, d, x[i+ 1], 4 , -1530992060)
    d = hh(d, a, b, c, x[i+ 4], 11,  1272893353)
    c = hh(c, d, a, b, x[i+ 7], 16, -155497632)
    b = hh(b, c, d, a, x[i+10], 23, -1094730640)
    a = hh(a, b, c, d, x[i+13], 4 ,  681279174)
    d = hh(d, a, b, c, x[i+ 0], 11, -358537222)
    c = hh(c, d, a, b, x[i+ 3], 16, -722521979)
    b = hh(b, c, d, a, x[i+ 6], 23,  76029189)
    a = hh(a, b, c, d, x[i+ 9], 4 , -640364487)
    d = hh(d, a, b, c, x[i+12], 11, -421815835)
    c = hh(c, d, a, b, x[i+15], 16,  530742520)
    b = hh(b, c, d, a, x[i+ 2], 23, -995338651)
    a = ii(a, b, c, d, x[i+ 0], 6 , -198630844)
    d = ii(d, a, b, c, x[i+ 7], 10,  1126891415)
    c = ii(c, d, a, b, x[i+14], 15, -1416354905)
    b = ii(b, c, d, a, x[i+ 5], 21, -57434055)
    a = ii(a, b, c, d, x[i+12], 6 ,  1700485571)
    d = ii(d, a, b, c, x[i+ 3], 10, -1894986606)
    c = ii(c, d, a, b, x[i+10], 15, -1051523)
    b = ii(b, c, d, a, x[i+ 1], 21, -2054922799)
    a = ii(a, b, c, d, x[i+ 8], 6 ,  1873313359)
    d = ii(d, a, b, c, x[i+15], 10, -30611744)
    c = ii(c, d, a, b, x[i+ 6], 15, -1560198380)
    b = ii(b, c, d, a, x[i+13], 21,  1309151649)
    a = ii(a, b, c, d, x[i+ 4], 6 , -145523070)
    d = ii(d, a, b, c, x[i+11], 10, -1120210379)
    c = ii(c, d, a, b, x[i+ 2], 15,  718787259)
    b = ii(b, c, d, a, x[i+ 9], 21, -343485551)
    a = safe_add(a, olda)
    b = safe_add(b, oldb)
    c = safe_add(c, oldc)
    d = safe_add(d, oldd)
  }
  return [a, b, c, d]
}
/*
 * Convert an array of little-endian words to a hex string.
 */
function binl2hex(binarray)
{
  var hex_tab = "0123456789abcdef"
  var str = ""
  for(var i = 0; i < binarray.length * 4; i++)
  {
    str += hex_tab.charAt((binarray[i>>2] >> ((i%4)*8+4)) & 0xF) +
           hex_tab.charAt((binarray[i>>2] >> ((i%4)*8)) & 0xF)
  }
  return str
}
/*
 * Convert an array of little-endian words to a base64 encoded string.
 */
function binl2b64(binarray)
{
  var tab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  var str = ""
  for(var i = 0; i < binarray.length * 32; i += 6)
  {
    str += tab.charAt(((binarray[i>>5] << (i%32)) & 0x3F) |
                      ((binarray[i>>5+1] >> (32-i%32)) & 0x3F))
  }
  return str
}
/*
 * Convert an 8-bit character string to a sequence of 16-word blocks, stored
 * as an array, and append appropriate padding for MD4/5 calculation.
 * If any of the characters are >255, the high byte is silently ignored.
 */
function str2binl(str)
{
  var nblk = ((str.length + 8) >> 6) + 1 // number of 16-word blocks
  var blks = new Array(nblk * 16)
  for(var i = 0; i < nblk * 16; i++) blks[i] = 0
  for(var i = 0; i < str.length; i++)
    blks[i>>2] |= (str.charCodeAt(i) & 0xFF) << ((i%4) * 8)
  blks[i>>2] |= 0x80 << ((i%4) * 8)
  blks[nblk*16-2] = str.length * 8
  return blks
}
/*
 * Convert a wide-character string to a sequence of 16-word blocks, stored as
 * an array, and append appropriate padding for MD4/5 calculation.
 */
function strw2binl(str)
{
  var nblk = ((str.length + 4) >> 5) + 1 // number of 16-word blocks
  var blks = new Array(nblk * 16)
  for(var i = 0; i < nblk * 16; i++) blks[i] = 0
  for(var i = 0; i < str.length; i++)
    blks[i>>1] |= str.charCodeAt(i) << ((i%2) * 16)
  blks[i>>1] |= 0x80 << ((i%2) * 16)
  blks[nblk*16-2] = str.length * 16
  return blks
}
/*
 * External interface
 */
function hexMD5 (str) { return binl2hex(coreMD5( str2binl(str))) }
function hexMD5w(str) { return binl2hex(coreMD5(strw2binl(str))) }
function b64MD5 (str) { return binl2b64(coreMD5( str2binl(str))) }
function b64MD5w(str) { return binl2b64(coreMD5(strw2binl(str))) }
/* Backward compatibility */
function calcMD5(str) { return binl2hex(coreMD5( str2binl(str))) }
================================================

File: radvert.html
================================================
<html>
<head>
<title>mikrotik hotspot > advertisement</title>
<meta http-equiv="refresh" content="2; url=$(link-orig)">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}
body{
	color: #737373;
	font-size: 12px;
	font-family: verdana;
	background-image: url(TEMA.gif);
}
a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }
-->
</style>
<script language="JavaScript">
<!--
    var popup = '';
    function openOrig() {
	if (window.focus) popup.focus();
	location.href = '$(link-orig)';
    }
    function openAd() {
	location.href = '$(link-redirect)';
    }
    function openAdvert() {
	if (window.name != 'hotspot_advert') {
		popup = open('$(link-redirect)', 'hotspot_advert', '');
		setTimeout("openOrig()", 1000);
		return;
	}
	setTimeout("openAd()", 1000);
    }
//-->
</script>
</head>
<body onLoad="openAdvert()">
<table width="100%" height="100%">
<tr>
	<td align="center" valign="middle" bgcolor="#FFFFFF">
	Advertisement.
	<br>
	<br>
	If nothing happens, open
	<a href="$(link-redirect)" target="hotspot_advert">advertisement</a>
	manually.	</td>
</tr>
</table>
</body>
</html>
================================================

File: redirect.html
================================================
$(if http-status == 302)Hotspot redirect$(endif)
$(if http-header == "Location")$(link-redirect)$(endif)
<html>
<head>
<title>...</title>
<meta http-equiv="refresh" content="0; url=$(link-redirect)">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252"><style type="text/css">
<!--
body {
	background-image: url(TEMA.gif);
}
-->
</style></head>
<body>
</body>
</html>
================================================

File: rlogin.html
================================================
$(if http-status == 302)Hotspot login required$(endif)
$(if http-header == "Location")$(link-redirect)$(endif)
<html>
<!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <Redirect>
	<AccessProcedure>1.0</AccessProcedure>
	<AccessLocation>$(location-id)</AccessLocation>
	<LocationName>$(location-name)</LocationName>
	<LoginURL>$(link-login-only)?target=xml</LoginURL>
	<MessageType>100</MessageType>
	<ResponseCode>0</ResponseCode>
    </Redirect>
  </WISPAccessGatewayParam>
-->
<head>
<title>Hotspot RS. Asura</title>
<meta http-equiv="refresh" content="0; url=$(link-redirect)">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252"><style type="text/css">
<!--
body {
	background-image: url(TEMA.gif);
}
-->
</style></head>
<body>
</body>
</html>
================================================

File: status.html
================================================
<html>
<head>
<title>Hotspot RS. Asura</title>
$(if refresh-timeout)
<meta http-equiv="refresh" content="$(refresh-timeout-secs)">
$(endif)
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}
.tabula{
border-width: 1px; 
border-collapse: collapse; 
border-color: #c1c1c1; 
background-color: transparent;
font-family: verdana;
font-size: 11px;
}
body{
	color: #737373;
	font-size: 12px;
	font-family: verdana;
	background-image: url(PROFILE.gif);
}
a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; padding: 4px;}
body,td,th {
	color: #333333;
}
.style7 {color: #00FF00}
-->
</style>
<script language="JavaScript">
<!--
$(if advert-pending == 'yes')
    var popup = '';
    function focusAdvert() {
	if (window.focus) popup.focus();
    }
    function openAdvert() {
	popup = open('$(link-advert)', 'hotspot_advert', '');
	setTimeout("focusAdvert()", 1000);
    }
$(endif)
    function openLogout() {
	if (window.name != 'hotspot_status') return true;
        open('$(link-logout)', 'hotspot_logout', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=280,height=250');
	window.close();
	return false;
    }
//-->
</script>
</head>
<body bottommargin="0" topmargin="0" leftmargin="0" rightmargin="0"
$(if advert-pending == 'yes')
	onLoad="openAdvert()"
$(endif)
>
<table width="100%" height="100%">
<tr>
<td align="center" valign="middle" class="style7">
<form action="$(link-logout)" name="logout" onSubmit="return openLogout()">
  <h1><b><img src="logo.jpg" width="86" height="90"></b></h1>
  <h4>Aplikasi Ini Dikembangkan Oleh IT Managemen Desain Hamba Alloh</h4>
  <table border="1" class="tabula">
$(if login-by == 'trial')
	<br><div style="text-align: center;">Welcome trial user!</div><br>
$(elif login-by != 'mac')
	<br><div style="text-align: center;">Assalamualikum, Selamat Datang $(username)!</div><br>
$(endif)
	<tr><td align="right" bgcolor="#FFFFFF"><span class="style7">IP Address:</span></td>
	<td bgcolor="#FFFFFF"><span class="style7">$(ip)</span></td>
	</tr>
	<tr><td align="right" bgcolor="#FFFFFF"><span class="style7">Bytes UP/DOWN:</span></td>
	<td bgcolor="#FFFFFF"><span class="style7">$(bytes-in-nice) / $(bytes-out-nice)</span></td>
	</tr>
$(if session-time-left)
	<tr><td align="right" bgcolor="#FFFFFF"><span class="style7">Connected / Left:</span></td>
	<td bgcolor="#FFFFFF"><span class="style7">$(uptime) / $(session-time-left)</span></td>
	</tr>
$(else)
	<tr><td align="right" bgcolor="#FFFFFF"><span class="style7">Connected:</span></td>
	<td bgcolor="#FFFFFF"><span class="style7">$(uptime)</span></td>
	</tr>
$(endif)
$(if blocked == 'yes')
	<tr><td align="right" bgcolor="#FFFFFF"><span class="style7">Status:</span></td>
	<td bgcolor="#FFFFFF"><div class="style7">
<a href="$(link-advert)" target="hotspot_advert">advertisement</a> required</div></td>
$(elif refresh-timeout)
	<tr><td align="right" bgcolor="#FFFFFF"><span class="style7">status refresh:</span></td>
	<td bgcolor="#FFFFFF"><span class="style7">$(refresh-timeout)</span></td>
$(endif)
</table>
  <p>$(if login-by-mac != 'yes') <br>
      <!-- user manager link. if user manager resides on other router, replace $(hostname) by its address
<button onclick="document.location='http://$(hostname)/user?subs='; return false;">status</button>
<!-- end of user manager link -->
      <input type="submit" value="log off">
      $(endif)</p>
  <p>RS. ASURA</p>
  <p>Aplikasi Versi 6.0</p>
</form></td>
</table>
</body>
</html>
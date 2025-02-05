# Repository Information
Name: mikrotik-647-default-hs-login

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
	url = https://gitlab.com/gladiopeace/mikrotik-647-default-hs-login.git
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
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="refresh" content="2; url=$(link-redirect)">
    <meta http-equiv="pragma" content="no-cache">
    <meta http-equiv="expires" content="-1">
    <title>Internet hotspot - Redirect</title>
    <link rel="stylesheet" href="css/style.css">
    <script>
        function startClock() {
            $(if popup == 'true')
            open('$(link-status)', 'hotspot_status', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=290,height=200');
        $(endif)
        location.href = unescape('$(link-redirect-esc)');
        }
    </script> 
</head>
<body onLoad="startClock()">
    <div class="ie-fixMinHeight">
        <div class="main">
            <div class="wrap">
                <h1>You are logged in</h1>
                <p class="info">If nothing happens, click <a href="$(link-redirect)">here</a></p>
            </div>
        </div>
    </div>
</body>
</html>
================================================

File: style.css
================================================
a,body,div,form,html,img,input,label,p,span{margin:0;padding:0;border:0;font-family:sans-serif,Arial}body,html{min-height:100%;overflow-x:hidden}body{background:#a2a09b;background:-webkit-linear-gradient(315deg,hsla(236.6,0%,53.52%,1) 0,hsla(236.6,0%,53.52%,0) 70%),-webkit-linear-gradient(65deg,hsla(220.75,34.93%,26.52%,1) 10%,hsla(220.75,34.93%,26.52%,0) 80%),-webkit-linear-gradient(135deg,hsla(46.42,36.62%,83.92%,1) 15%,hsla(46.42,36.62%,83.92%,0) 80%),-webkit-linear-gradient(205deg,hsla(191.32,50.68%,56.45%,1) 100%,hsla(191.32,50.68%,56.45%,0) 70%);background:linear-gradient(135deg,hsla(236.6,0%,53.52%,1) 0,hsla(236.6,0%,53.52%,0) 70%),linear-gradient(25deg,hsla(220.75,34.93%,26.52%,1) 10%,hsla(220.75,34.93%,26.52%,0) 80%),linear-gradient(315deg,hsla(46.42,36.62%,83.92%,1) 15%,hsla(46.42,36.62%,83.92%,0) 80%),linear-gradient(245deg,hsla(191.32,50.68%,56.45%,1) 100%,hsla(191.32,50.68%,56.45%,0) 70%)}a{color:#486173}input,label{vertical-align:middle;white-space:normal;background:0 0;line-height:1}label{position:relative;display:block}p::first-letter{text-transform:uppercase}.main{min-height:calc(100vh - 90px);width:100%;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column}.ie-fixMinHeight{display:-webkit-box;display:-ms-flexbox;display:flex}.ico{height:16px;position:absolute;top:0;left:0;margin-top:13px;margin-left:14px}.logo{max-width:200px;display:block;margin:0 auto 30px auto}.logo *{fill:#fff}.lite .logo *{fill:#444}h1{text-align:center;color:#fff;font-size:24px!important}*{-webkit-box-sizing:border-box;box-sizing:border-box;font-size:16px}.wrap{margin:auto;padding:40px;-webkit-transition:width .3s ease-in-out;transition:width .3s ease-in-out}@media only screen and (min-width:1px) and (max-width:575px){.wrap{width:100%}}form{width:100%;margin-bottom:20px}@-webkit-keyframes fadeIn{from{opacity:0}to{opacity:1}}@keyframes fadeIn{from{opacity:0}to{opacity:1}}.fadeIn{-webkit-animation-name:fadeIn;animation-name:fadeIn}.animated{-webkit-animation-duration:1s;animation-duration:1s;-webkit-animation-fill-mode:both;animation-fill-mode:both}.info{color:#fff;text-align:center;margin-bottom:30px}input{outline:0;-webkit-appearance:none;-moz-appearance:none;appearance:none}input:focus{outline:0}input[type=password],input[type=text]{width:100%;border:1px solid background-color: rgba(255,255,255,.8);height:44px;padding:3px 20px 3px 40px;margin-bottom:20px;border-radius:6px;background-color:rgba(255,255,255,.8);-webkit-transition:-webkit-box-shadow .3s ease-in-out;transition:-webkit-box-shadow .3s ease-in-out;transition:box-shadow .3s ease-in-out;transition:box-shadow .3s ease-in-out,-webkit-box-shadow .3s ease-in-out}input[type=password]:focus,input[type=text]:focus{-webkit-box-shadow:0 0 5px 0 rgba(255,255,255,1);box-shadow:0 0 5px 0 rgba(255,255,255,1)}.bt{opacity:.4}input[type=submit]{background:#3e4d59;color:#fff;border:0;cursor:pointer;text-align:center;width:100%;height:44px;border-radius:6px;-webkit-transition:background .3s ease-in-out;transition:background .3s ease-in-out}input[type=submit]:focus,input[type=submit]:hover{background:#33404a}table{border-collapse:collapse;width:100%;margin-bottom:20px}table td{color:#fff;border-bottom:1px solid #e6e6e6;padding:10px 4px 10px 0}table td:first-child{font-weight:700}.lite{background:#fff}.lite input[type=password],.lite input[type=text]{border:1px solid #c3c3c3}.lite .info,.lite h1,.lite table td{color:#444}.lite input[type=password]:focus,.lite input[type=text]:focus{-webkit-box-shadow:0 0 5px 0 rgba(62,77,89,.2);box-shadow:0 0 5px 0 rgba(62,77,89,.2)}.dark{background:#343434}.dark input[type=submit]{background:#dc3a41}.dark input[type=submit]:focus,.dark input[type=submit]:hover{background:#b92f35}.dark input[type=password],.dark input[type=text]{background-color:#fff}.dark a{color:#dc3a41}.dark table td{border-bottom:1px solid #505050}.info.alert{color:#da3d41}@media (min-width:576px){.wrap{width:410px}*{font-size:14px!important}}
================================================

File: error.html
================================================
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="pragma" content="no-cache">
    <meta http-equiv="expires" content="-1">
    <title>Piso WiFi - Error</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="ie-fixMinHeight">
        <div class="main">
            <div class="wrap">
                <h1>Error: $(error)</h1>
                <p class="info">Log in page: <a href="$(link-login)">$(link-login)</a></p>
            </div>
        </div>
    </div>
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
invalid-username = invalid ticket
# invalid-mac
# Local users (on hotspot server) can be bound to some MAC address. If login
# from different MAC is tried, this error message will be shown.
invalid-mac = user $(username) is not allowed to log in from this MAC address
# uptime-limit, traffic-limit
# For local hotspot users in case if limits are reached
uptime-limit = No hour left on your ticket: $(username)
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

File: login.html
================================================
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="expires" content="-1" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Piso WiFi - Log in</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <!-- two other colors
<body class="lite">
<body class="dark">
-->
    $(if chap-id)
    <form name="sendin" action="$(link-login-only)" method="post" style="display:none">
        <input type="hidden" name="username" />
        <input type="hidden" name="password" />
        <input type="hidden" name="dst" value="$(link-orig)" />
        <input type="hidden" name="popup" value="true" />
    </form>
    <script src="/md5.js"></script>
    <script>
        function doLogin() {
            document.sendin.username.value = document.login.username.value;
            document.sendin.password.value = hexMD5('$(chap-id)' + document.login.username.value + '$(chap-challenge)');
            document.sendin.submit();
            return false;
        }
    </script>
    $(endif)
    <div class="ie-fixMinHeight">
        <div class="main">
            <div class="wrap animated fadeIn">
                <form name="login" action="$(link-login-only)" method="post" $(if chap-id) onSubmit="return doLogin()" $(endif)>
                    <input type="hidden" name="dst" value="$(link-orig)" />
                    <input type="hidden" name="popup" value="true" />
                    <h1>Piso WiFi</h1>
                    <p class="info $(if error)alert$(endif)">
                        $(if error == "")Please input your ticket and click connect to use the internet. $(if trial == 'yes')<br />Free trial available, <a href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">click here</a>.$(endif)
                        $(endif)
                        $(if error)$(error)$(endif)
                    </p>
                    <label>
                        <img class="ico" src="img/password.svg" alt="#" />
                        <input name="username" type="text" value="$(username)" placeholder="Ticket" autofocus required/>
                    </label>
                    <input type="submit" value="Connect" />
                </form>
                <div>
                    <table>
                        <thead>
                        <tr>
                            <th style="text-align:center">Price</th>
                            <th style="text-align:center">Hour</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td style="text-align:center">5-Php</td>
                            <td style="text-align:center">2-Hrs</td>
                        </tr>
                        <tr>
                            <td style="text-align:center">10-Php</td>
                            <td style="text-align:center">5-Hrs</td>
                        </tr>
                        <tr>
                            <td style="text-align:center">20-Php</td>
                            <td style="text-align:center">12-Hrs</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
================================================

File: logout.html
================================================
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0" />   
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<title>Piso WiFi - Log out</title>
<link rel="stylesheet" href="css/style.css">
<script>
    function openLogin() {
	if (window.name != 'hotspot_logout') return true;
	open('$(link-login)', '_blank', '');
	window.close();
	return false;
    }
</script>
</head>
<body>
    <div class="ie-fixMinHeight">
        <div class="main">
            <div class="wrap">
                <h1>You have just logged out!</h1> 
                <table>  
                    <tr><td>Ticket No.</td><td>$(username)</td></tr>
                    <tr><td>IP address</td><td>$(ip)</td></tr>
                    <tr><td>MAC address</td><td>$(mac)</td></tr>
                    <tr><td>Session time</td><td>$(uptime)</td></tr>
                    $(if session-time-left)
                    <tr><td>Time left</td><td>$(session-time-left)</td></tr>
                    $(endif)
                    <tr><td>Bytes up / down:</td><td>$(bytes-in-nice) / $(bytes-out-nice)</td></tr>
                </table>
                <form action="$(link-login)" name="login" onSubmit="return openLogin()">
                <input type="submit" value="Log in">
                </form>
            </div>
        </div>
    </div>
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
<meta http-equiv="refresh" content="2; url=$(link-orig)">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0" />   
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<title>Internet hotspot - Advertisement</title>
<link rel="stylesheet" href="css/style.css">
<script>
    var popup = '';
    function openOrig() {
	if (window.focus) popup.focus();
	location.href = unescape('$(link-orig-esc)');
    }
    function openAd() {
	location.href = unescape('$(link-redirect-esc)');
    }
    function openAdvert() {
	if (window.name != 'hotspot_advert') {
		popup = open('$(link-redirect)', 'hotspot_advert', '');
		setTimeout("openOrig()", 1000);
		return;
	}
	setTimeout("openAd()", 1000);
    }
</script>
</head>
<body onLoad="openAdvert()">
    <div class="ie-fixMinHeight">
        <div class="main">
            <div class="wrap">
                <h1>Advertisement</h1>
                <p class="info">If nothing happens, open <a href="$(link-redirect)" target="hotspot_advert">advertisement</a> manually.</p>
            </div>
        </div>
    </div>
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
</head>
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
<title>...</title>
<meta http-equiv="refresh" content="0; url=$(link-redirect)">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
</head>
<body>
</body>
</html>
================================================

File: status.html
================================================
<html>
<head>
$(if refresh-timeout)
<meta http-equiv="refresh" content="$(refresh-timeout-secs)">
$(endif)
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0" />   
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<title>Piso WiFi - Status</title>
<link rel="stylesheet" href="css/style.css">
<script>
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
</script>
</head>
<body $(if advert-pending == 'yes') onLoad="openAdvert()" $(endif)>
    <div class="ie-fixMinHeight">
        <div class="main">
            <div class="wrap">
                $(if login-by == 'trial')
                    <h1>Hi, trial user!</h1>
                $(elif login-by != 'mac')
                    <h1>Ticket No. $(username)</h1>
                $(endif)                
                <form action="$(link-logout)" name="logout" onSubmit="return openLogout()">
                    <table>
                        <tr><td>IP address</td><td>$(ip)</td></tr>
                        <tr><td>Bytes up / down</td><td>$(bytes-in-nice) / $(bytes-out-nice)</td></tr>
                    $(if session-time-left)
                        <tr><td>Connected / left</td><td>$(uptime) / $(session-time-left)</td></tr>
                    $(else)
                        <tr><td>Connected</td><td>$(uptime)</td></tr>
                    $(endif)
                    $(if blocked == 'yes')
                        <tr><td>Status</td><td>
                    <a href="$(link-advert)" target="hotspot_advert">Advertisement required</a></td>
                        </tr>
                    $(elif refresh-timeout)
                        <tr><td>Status refresh</td><td>$(refresh-timeout)</td></tr>
                    $(endif)
                        </table>
                    $(if login-by-mac != 'yes')
                    <!-- user manager link. if user manager resides on other router, replace $(hostname) by its address
                    <button onclick="document.location='http://$(hostname)/user?subs='; return false;">status</button>
                    <!-- end of user manager link -->
                    <input type="submit" value="Log out">
                    $(endif)
                </form>
            </div>
        </div>
    </div>
</body>
</html>
================================================

File: alogin.html
================================================
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <AuthenticationReply>
	<MessageType>120</MessageType>
	<ResponseCode>50</ResponseCode>
	<LogoffURL>$(link-logout)</LogoffURL>
	<RedirectionURL>$(link-redirect)</RedirectionURL>
$(if radius18[0])	<ReplyMessage>$(radius18[0])</ReplyMessage>	$(endif)
$(if radius18[1])	<ReplyMessage>$(radius18[1])</ReplyMessage>	$(endif)
$(if radius18[2])	<ReplyMessage>$(radius18[2])</ReplyMessage>	$(endif)
$(if radius18[3])	<ReplyMessage>$(radius18[3])</ReplyMessage>	$(endif)
$(if radius18[4])	<ReplyMessage>$(radius18[4])</ReplyMessage>	$(endif)
    </AuthenticationReply>
  </WISPAccessGatewayParam>
--> </HTML>
================================================

File: error.html
================================================
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <AuthenticationReply>
	<MessageType>120</MessageType>
	<ResponseCode>255</ResponseCode>
	<ReplyMessage>$(error)</ReplyMessage>
    </AuthenticationReply>
  </WISPAccessGatewayParam>
--> </HTML>
================================================

File: flogout.html
================================================
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <LogoffReply>
	<MessageType>130</MessageType>
	<ResponseCode>150</ResponseCode>
    </LogoffReply>
  </WISPAccessGatewayParam>
--> </HTML>
================================================

File: login.html
================================================
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <AuthenticationReply>
	<MessageType>120</MessageType>
	<ResponseCode>
$(if error-type == 'radius-timeout')
		102
$(else)
		100
$(endif)
	</ResponseCode>
$(if error)		<ReplyMessage>$(error)</ReplyMessage>		$(endif)
$(if radius18[1])	<ReplyMessage>$(radius18[1])</ReplyMessage>	$(endif)
$(if radius18[2])	<ReplyMessage>$(radius18[2])</ReplyMessage>	$(endif)
$(if radius18[3])	<ReplyMessage>$(radius18[3])</ReplyMessage>	$(endif)
$(if radius18[4])	<ReplyMessage>$(radius18[4])</ReplyMessage>	$(endif)
    </AuthenticationReply>
  </WISPAccessGatewayParam>
--> </HTML>
================================================

File: logout.html
================================================
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
<WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <LogoffReply>
	<MessageType>130</MessageType>
	<ResponseCode>150</ResponseCode>
    </LogoffReply>
  </WISPAccessGatewayParam>
--> </HTML>
================================================

File: rlogin.html
================================================
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <Redirect>
	<AccessProcedure>1.0</AccessProcedure>
	<AccessLocation>$(location-id)</AccessLocation>
	<LocationName>$(location-name)</LocationName>
	<LoginURL>$(link-login-only)</LoginURL>
	<MessageType>100</MessageType>
	<ResponseCode>0</ResponseCode>
    </Redirect>
  </WISPAccessGatewayParam>
--> </HTML>
================================================
# Repository Information
Name: Twasel-Net

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
	url = https://gitlab.com/MarwanBz/Twasel-Net.git
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
﻿<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" type="text/css" href="style.css">
	<title>شبكة تواصل نت - مرحبا بك</title>
</head>
</head>
<body>
	<div id="wrap">
		<div id="acontent">
			<h1 class="main-heading heading-background">مرحبا بك</h1>
			<h1 class="success"> لقد تم تسجيل دخولك بنجاح</h1>
			<div class="alogin">
				<a href="status.html" id="afterLogin">لمعرفة تفاصيل حسابك انقر هنا</a>
			</div>
		</div>
	</div>
	<footer class="footer">
		<p>جميع الحقوق محفوظة <span>لشبكة تواصل نت</span> &copy; </p>
		<p>لأي إستفسار يرجى التواصل مع إدارة الشبكة
			733024644 - 701276366 - 701231904
		</p>
		<p>
			تصميم وبرمجة <span><a class="programmer" href="tel:+967770108459"> Baz </a> <a class="programmer" href="tel:+967702020128">
					Marwan</a></span>
		</p>
	</footer>
	</div>
	</div>
</body>
</html>
================================================

File: style.css
================================================
/*
Theme Name: shbtalk_premium (Designed By Elsayed Fahmy)
Theme URI: http://www.shbtalk.com
Author: Shabab Talk team
Author URI: http://www.shbtalk.com
Description: Shabab Talk Premium Theme for WordPress
Version: 1.0
Tags: three-columns, right-sidebar, flexible-width, custom-menu, full-width-template, rtl-language-support, theme-options, translation-ready
License: GNU General Public License v2.0
License URI: http://www.gnu.org/licenses/gpl-2.0.html
*/
*{ padding:0; margin:0;	outline:none; list-style:none; border: 0 none;}
@font-face {
	src: url('../GE_SS_Two_Medium.otf');
	font-family: 'GE_SS_Two_Medium';
}
body{
	background: url(../images/blue-bg.jpg) repeat center center;
	background-attachment:fixed;
	overflow-x: hidden;
}
/*
================================================
Styling Of The Main Wrapper && its Contents ... 
================================================
*/
#main-wrap{
	width:950px;
	height: auto;
	display: block;
	clear: both;
	margin: 0 auto 0;
}
.mainlogin-form{
	background: url(../images/login_bg.png) no-repeat center center;
	width: 944px;
	height: 867px;
	display: block;
	clear: both;
	margin: -80px auto 0;
}
.log-form{
	width:450px;
	height: 350px;
	margin: 30px 0 0 185px;
}
.social-icons{
	background: url(../images/social-icons.png) no-repeat center center;
	width: 448px;
	height: 92px;
	display: block;
	clear: both;
	margin: -180px auto 0;
}
.login-head{
	background: url(../images/login_head.png) no-repeat top center;
	width:270px;
	height: 61px;
	display: inline-block;
	margin: 50px 0 0 310px;
}
.loginbtn{
	background: url(../images/login_btn.png) no-repeat center center;
	width:180px;
	height: 67px;
	margin:10px 0 0 130px;
	cursor:pointer;
}
.userinput:hover , .passinput:hover , .loginbtn:hover{
	opacity: 0.7;
}
.network-name{
	font-family: 'GE_SS_Two_Medium',arial,Georgia, serif;
	color:#FFF;
	text-shadow: #fff4f4 0 0 15px;
	font-size:25px;
	font-weight: 700;
	text-align: center;
	padding: 140px 0 0 130px;
}
.login_success{
	font-family: 'GE_SS_Two_Medium',arial,Georgia, serif;
	color:#FFF;
	text-shadow: #FFF 0 0 20px;
	font-size:25px;
	font-weight: 700;
	text-align: center;
	padding: 20px 25px 0 0;
	line-height: 1.9;
}
.success-ico{
	background: url(../images/login-success.png) no-repeat top center;
	width:256px;
	height: 256px;
	margin: 30px 0 0 320px;
}
.designer a{
	font-family: Arial, Helvetica, sans-serif,Georgia, serif;
	color:#cb0909;
	text-shadow: #fff4f4 0 0 15px;
	font-size:17px;
	font-weight: 700;
	text-align: center;
}
.designer{
	font-family: Arial, Helvetica, sans-serif,Georgia, serif;
	color:#333;
	text-shadow: #fff4f4 0 0 15px;
	font-size:17px;
	font-weight: 700;
	text-align: center;
}
================================================

File: error.html
================================================
﻿<html>
<head>
<title>Blue HotSpot</title>
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
	background: url(images/blue-bg.jpg) repeat center center;
	background-attachment:fixed;
	overflow-x: hidden;
}
.errortxt{
	font-size: 22px;
	font-weight: 800;
	color:#FFF;
	text-shadow: #FFF 0 0 20px;
}
a, a:link, a:visited, a:active { color: #aa1b1b; text-decoration: none; font-size: 16px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }
-->
</style>
<meta name="keywords" content="Blue HotSpot">
<meta name="description" content="Blue HotSpot">
</head>
<body>
<table width="100%" height="100%">
<tr>
<td align="center" valign="middle" class="errortxt">
 ERROR: $(error)<br>
<br>
 <a href="$(link-login)">$(link-login)</a>   اذهب إلى صفحة تسجيل الدخول من هنا  <br><br><br>
<div class="social-graph"></div>
</td>
</tr>
</table>
</body>
</html>
================================================

File: errors.txt
================================================
﻿# This file contains error messages which are shown to user, when http/https
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
not-logged-in = برجاء تسجيل الدخول (ip $(ip))
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
user-session-limit = غير مسموح بتسجيل الدخول اكثر من مرة $(username)
# license-session-limit
# Depending on licence number of active hotspot clients is limited to
# one or another amount. If this limit is reached, following error is displayed.
license-session-limit = session limit reached ($(error-orig))
# wrong-mac-username
# If username looks like MAC address (12:34:56:78:9a:bc), but is not
# a MAC address of this client, login is rejected
wrong-mac-username = اسم مستخدم غير صالح ($(username)): و الماك ادريس غير مطابق
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
chap-missing = المتصفح لم يرسل لنا اسمك برجاء المحاولة مرة اخرى أو جرب متصفح أخر
# invalid-username
# Most general case of invalid username or password. If RADIUS server
# has sent an error string with Access-Reject message, then it will
# override this setting.
invalid-username = تاكد من كتابة اسم المستخدم بشكل صحيح
# invalid-mac
# Local users (on hotspot server) can be bound to some MAC address. If login
# from different MAC is tried, this error message will be shown.
invalid-mac = غير مسموح له بالدخول من جهاز تانى $(username) المستخدم
# uptime-limit, traffic-limit
# For local hotspot users in case if limits are reached
uptime-limit = هذا الحساب منتهي الصلاحية
traffic-limit = هذا الحساب منتهي الرصيد
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
﻿<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" type="text/css" href="style.css">
	<title>شبكة تواصل نت - تسجيل الدخول</title>
</head>
</head>
<body>
	$(if chap-id)
	<form name="sendin" action="$(link-login-only)" method="post">
		<input type="hidden" name="username" />
		<input type="hidden" name="dst" value="$(link-orig)" />
		<input type="hidden" name="popup" value="true" />
	</form>
	<script type="text/javascript" src="/md5.js"></script>
	<script type="text/javascript">
		<!--
		function doLogin() {
			document.sendin.username.value = document.login.username.value;
			document.sendin.password.value = hexMD5('$(chap-id)' + document.login.password.value + '$(chap-challenge)');
			document.sendin.submit();
			return false;
		}
		//
		-->
	</script>
	$(endif)
	<div id="wrap">
		<div id="content">
			<div class="main-heading">
				<h1 class="welcome">مرحبا بك قم بتسجيل الدخول</h1>
			</div>
			<!--<div class="ramadan"><a href="./ramadan.html"><img src="./images/rama.png" alt=""></a></div>
			<h2>أظغط على الصورة</h2>!-->
			<div class="sidebare">
				<div class="login">
					<form name="login" action="$(link-login-only)" method="post" $(if chap-id) onSubmit="return doLogin()"
						$(endif)>
						<input type="hidden" name="dst" value="$(link-orig)" />
						<input type="hidden" name="popup" value="true" />
						<input id="user" type="text" name="username" value="$(username)" placeholder="رمز الدخول  : ">
						<!-- <input id="pass" type="password" name="password" placeholder="كلمة المرور   : "> -->
						<input type="submit" id="loginBtn" value="تسجيل الدخول" />
						<!-- <input type="submit" value="دخول" /> !-->
					</form>
				</div>
				<!-- <input type="submit" value="دخول" /> !-->
				</form>
			</div>
			$(if error)
			<b id="errormsg" style="display:none">$(error)</b>
			<div id="message">
				<script type="text/javascript">
					var verror = document.getElementById('errormsg');
					switch (verror.innerHTML) {
						case 'invalid password':
							document.write('خطأ في كلمة المرور');
							break;
						case 'invalid Calling-Station-Id':
							document.write('هذا الحساب منتهي الصلاحية');
							break;
						case 'download limit reached':
							document.write('هذا الحساب منتهي الرصيد');
							break;
						case 'no valid profile found':
							document.write('هذا الحساب منتهي الصلاحية');
							break;
						case 'simultaneous session limit reached':
							document.write('الكرت مستخدم في جهاز آخر');
							break;
						default:
							res = verror.innerHTML;
							res = res.replace("user", "المستخدم");
							res = res.replace("not found", "   منتهي الرصيد أو ان الكرت غير موجود ");
							document.write(res);
					}
				</script>
			</div>$(endif)
		</div>
		<div class="sidebare">
			<div class="block" id="floated">
				<div class="title">
					<h2><img src="./images/money.png" alt="" srcset="">أسعار الكروت : </h2>
				</div>
				<div class="content">
					<table>
						<tr>
							<td class="first">السعر</td>
							<td class="first">الحجم</td>
							<td class="first">المدة</td>
						</tr>
						<tr>
							<td>100 ريال</td>
							<td>200 ميقا</td>
							<td>6 ساعات</td>
						</tr>
						<tr>
							<td>200 ريال</td>
							<td>500 ميقا</td>
							<td>2 يوم </td>
						</tr>
						<tr>
							<td>300 ريال</td>
							<td>700 ميقا</td>
							<td>3أيام</td>
						</tr>
						<tr>
							<td>500 ريال</td>
							<td>1000 ميقا</td>
							<td>إسبوع</td>
						</tr>
						<tr>
							<td>1600 ريال</td>
							<td>3000 ميقا</td>
							<td>20 يوم</td>
						</tr>
						<tr>
							<td>2500 ريال</td>
							<td>5000 ميقا</td>
							<td>شهر</td>
						</tr>
						<tr>
							<td>3500 ريال</td>
							<td>10000 ميقا</td>
							<td>شهر</td>
						</tr>
						<tr>
							<td>4500 ريال</td>
							<td>15000 ميقا</td>
							<td>شهر</td>
						</tr>
						<tr>
							<td>6500 ريال</td>
							<td>25000 ميقا</td>
							<td>شهر</td>
						</tr>
					</table>
				</div>
			</div>
		</div>
		<div class="sidebare">
			<div class="block hidden">
				<div class="title">
					<h2><img src="./images/building.png" alt="" srcset="">مواقع بيع الكروت : </h2>
				</div>
				<div class="content">
					<ul>
						<li>الشافعي : بقالة الخير - بقالة شمسان - الشيخ للبهارات - سوبر ماركت البريكي</li>
						<li>ابن سيناء : اسواق النهدي - بقالة باحكيم - قباء لتسوق-تموينات الهناء-تموينات الريان</li>
						<li>المطابع : -بقالة البركه - بقالةالعمودي - بقالة باجرفان - بقالة البندر</li>
						<li>الخمر : بقالة المحمدي</li>
						<li>غرير : بقالة الخيرات</li>
						<li>العشوائي : بقالة العمودي - بقالة الدواعنه</li>
						<li>الدواجن : باتيس للغاز</li>
					</ul>
				</div>
			</div>
		</div>
	</div>
	</div>
	<footer class="footer">
		<p>جميع الحقوق محفوظة <span>لشبكة تواصل نت</span> &copy; </p>
		<p>لأي إستفسار يرجى التواصل مع إدارة الشبكة
			733024644 - 701276366 - 701231904
		</p>
		<p>
			تصميم وبرمجة <span><a class="programmer" href="tel:+967702020128"> Baz </a> <a class="programmer"
					href="tel:+967770108459">
					Marwan</a></span>
		</p>
	</footer>
	<script type="text/javascript">
		<!--
		document.login.username.focus();
		//
		-->
	</script>
</body>
</html>
================================================

File: logout.html
================================================
﻿<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" type="text/css" href="style.css">
		$(if refresh-timeout)
        <meta http-equiv="refresh" content="$(refresh-timeout-secs)">
$(endif)
		<title>شبكة تواصل - تسجيل الخروج</title>
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
	</head>
<body $(if advert-pending=='yes' ) onLoad="openAdvert()" $(endif)>
	<div id="wrap">
		<div id="o-content">
			<div id="userDetails">
				<form action="$(link-logout)" name="logout" onSubmit="return openLogout()">
					<!--<div class="ramadan"><a href="./ramadan.html"><img src="./images/rama.png" alt=""></a></div>
						<h2>أظغط على الصورة</h2>!-->
					<h1 class="success"> تم تسجيل خروجك بنجاح</h1>
					<div class="social-graph"></div>
					<br>
					<div class="alogin">
						<a href="status.html" id="aafterLogin">لتسجيل الدخول</a>
					</div>
					<!--<form action="$(link-login)" name="login" onSubmit="return openLogin()">
<input type="submit" value="تسجيل الدخول" class="login-button">
</form>//-->
					</td>
				</form>
			</div>
		</div>
	</div>
		<footer class="footer">
			<p>جميع الحقوق محفوظة <span>لشبكة تواصل نت</span> &copy; </p>
			<p>لأي إستفسار يرجى التواصل مع إدارة الشبكة
				733024644 - 701276366 - 701231904
			</p>
			<p>
				تصميم وبرمجة <span><a class="programmer" href="tel:+967770108459"> Baz </a> <a class="programmer" href="tel:967702020128">
						Marwan</a></span>
			</p>
		</footer>
</body>
</html>
================================================

File: alogin.html
================================================
<html>
<head>
<title>mikrotik hotspot > novirzt</title>
<meta http-equiv="refresh" content="2; url=$(link-redirect)">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1257">
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
body{ color: #737373; font-size: 12px; font-family: verdana; }
a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }
-->
</style>
<script language="JavaScript">
<!--
    function startClock() {
        $(if popup == 'true')
        open('$(link-status)', 'hotspot_status', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=290,height=200');
	$(endif)
	location.href = '$(link-redirect)';
    }
//-->
</script>
</head>
<body onLoad="startClock()">
<table width="100%" height="100%">
<tr>
	<td align="center" valign="middle">
	Js esat piesldzies
	<br><br>
	Ja nekas nenotiek, klikiniet <a href="$(link-redirect)">eit</a></td>
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
internal-error = sistēmas kļūda ($(error-orig))
# config-error
# Should never happen if hotspot is configured properly.
config-error = konfigurācijas kļūda ($(error-orig))
# not-logged-in
# Will happen, if status or logout page is requested by user,
# which actually is not logged in
not-logged-in = Jūs neesat pieslēdzies (ip $(ip))
# ippool-empty
# IP address for user is to be assigned from ip pool, but there are no more
# addresses in that pool
ippool-empty = nevaru piešķirt IP adresi - nav vairāk brīvu adrešu krātuvē
# shutting-down
# When shutdown is executed, new clients are not accepted
shutting-down = hotspot serviss tiek apstādināts, mēģiniet pēc brīža vēlreiz
# user-session-limit
# If user profile has limit of shared-users, then this error will be shown
# after reaching this limit
user-session-limit = lietotājam $(username) vairāk sessijas nav atļautas
# license-session-limit
# Depending on licence number of active hotspot clients is limited to
# one or another amount. If this limit is reached, following error is displayed.
license-session-limit = ir sasniegts maksimālais sessiju skaits ($(error-orig))
# wrong-mac-username
# If username looks like MAC address (12:34:56:78:9a:bc), but is not
# a MAC address of this client, login is rejected
wrong-mac-username = nepareizs lietotāja vārds ($(username)): šī MAC adrese nav tava
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
chap-missing = problēmas ar kodu (mēģiniet vēlreiz, atļaujiet JavaScript)
# invalid-username
# Most general case of invalid username or password. If RADIUS server
# has sent an error string with Access-Reject message, then it will
# override this setting.
invalid-username = nepareizs lietotāja vārds vai parole
# invalid-mac
# Local users (on hotspot server) can be bound to some MAC address. If login
# from different MAC is tried, this error message will be shown.
invalid-mac = lietotājam $(username) nav atļauts pieslēgties no šīs MAC adreses
# uptime-limit, traffic-limit
# For local hotspot users in case if limits are reached
uptime-limit = lietotāja $(username) atļautasi pieslēguma laiks ir beidzies
traffic-limit = lietotāja $(username) atļautais datu pārraides apjoms ir sasniegts
# radius-timeout
# User is authenticated by RADIUS server, but no response is received from it,
# following error will be shown.
radius-timeout = autorizācijas serveris neatbild (mēģiniet vēlreiz)
# auth-in-progress
# Authorization in progress. Client already has issued an authorization request
# which is not yet complete.
auth-in-progress = notiek autorizācija (mēģiniet vēlāk)
# radius-reply
# Radius server returned some custom error message
radius-reply = autorizācijas kļūda ($(error-orig))
================================================

File: login.html
================================================
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<title>mikrotik hotspot > ieeja </title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="pragma" content="no-cache" />
<meta http-equiv="expires" content="-1" />
<style type="text/css">
body {color: #737373; font-size: 10px; font-family: verdana;}
textarea,input,select {
background-color: #FDFBFB;
border: 1px solid #BBBBBB;
padding: 2px;
margin: 1px;
font-size: 14px;
color: #808080;
}
a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 10px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 14px; color: #7A7A7A; }
</style>
</head>
<body>
$(if chap-id)
	<form name="sendin" action="$(link-login-only)" method="post">
		<input type="hidden" name="username" />
		<input type="hidden" name="password" />
		<input type="hidden" name="dst" value="$(link-orig)" />
		<input type="hidden" name="popup" value="true" />
	</form>
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
<div align="center">
<a href="$(link-login-only)?target=%2F&amp;dst=$(link-orig-esc)">English</a>
</div>
<table width="100%" style="margin-top: 10%;">
	<tr>
	<td align="center" valign="middle">
		<div class="notice" style="color: #c1c1c1; font-size: 9px">Lūdzu pieslēdzieties, lai lietotu mikrotik hotspot servisu.<br />$(if trial == 'yes')Lai izmēģinātu bez maksas, <a style="color: #FF8080"href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">spiediet šeit.</a>.$(endif)</div><br />
		<table width="240" height="240" style="border: 1px solid #cccccc; padding: 0px;" cellpadding="0" cellspacing="0">
			<tr>
				<td align="center" valign="bottom" height="175" colspan="2">
					<form name="login" action="$(link-login-only)" method="post"
					    $(if chap-id) onSubmit="return doLogin()" $(endif)>
						<input type="hidden" name="dst" value="$(link-orig)" />
						<input type="hidden" name="popup" value="true" />
							<table width="100" style="background-color: #ffffff">
								<tr><td align="right">login</td>
										<td><input style="width: 80px" name="username" type="text" value="$(username)"/></td>
								</tr>
								<tr><td align="right">parole</td>
										<td><input style="width: 80px" name="password" type="password"/></td>
								</tr>
								<tr><td>&nbsp;</td>
										<td><input type="submit" value="OK" /></td>
								</tr>
							</table>
					</form>
				</td>
			</tr>
			<tr><td align="center"><a href="http://www.mikrotik.com" target="_blank" style="border: none;"><img src="/img/logobottom.png" alt="mikrotik" /></a></td></tr>
		</table>
	<br /><div style="color: #c1c1c1; font-size: 9px">nodrošina mikrotik routeros &copy; 2005 mikrotik</div>
	$(if error)<br /><div style="color: #FF8080; font-size: 9px">$(error)</div>$(endif)
	</td>
	</tr>
</table>
<script type="text/javascript">
<!--
  document.login.username.focus();
//-->
</script>
</body>
</html>
================================================

File: logout.html
================================================
<html>
<head>
<title>mikrotik hotspot > atsldzies</title>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1257">
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
body{ color: #737373; font-size: 12px; font-family: verdana; }
a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; padding: 4px;}
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
<b>sessija ir aizvrta</b> <br><br>
<table class="tabula" border="1">  
<tr><td align="right">lietotja vrds</td><td>$(username)</td></tr>
<tr><td align="right">IP adrese</td><td>$(ip)</td></tr>
<tr><td align="right">MAC adrese</td><td>$(mac)</td></tr>
<tr><td align="right">sesijas ilgums</td><td>$(uptime)</td></tr>
$(if session-time-left)
<tr><td align="right">atlikuais laiks</td><td>$(session-time-left)</td></tr>
$(endif)
<tr><td align="right">baiti prom/urp:</td><td>$(bytes-in-nice) / $(bytes-out-nice)</td></tr>
</table>
<br>
<form action="$(link-login)" name="login" onSubmit="return openLogin()">
<input type="submit" value="pieslgties no jauna">
</form>
</td>
</table>
</body>
</html>
================================================

File: radvert.html
================================================
<html>
<head>
<title>mikrotik hotspot > advertisement</title>
<meta http-equiv="refresh" content="2; url=$(link-orig)">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1257">
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
body{ color: #737373; font-size: 12px; font-family: verdana; }
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
	<td align="center" valign="middle">
	Reklma.
	<br><br>
	Ja nekas nenotiek, atveriet
	<a href="$(link-redirect)" target="hotspot_advert">reklmu</a>
	parocgi.
	</td>
</tr>
</table>
</body>
</html>
================================================

File: status.html
================================================
<html>
<head>
<title>mikrotik hotspot > statuss</title>
$(if refresh-timeout)
<meta http-equiv="refresh" content="$(refresh-timeout-secs)">
$(endif)
<meta http-equiv="Content-Type" content="text/html; charset=windows-1257">
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
body{ color: #737373; font-size: 12px; font-family: verdana; }
a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; padding: 4px;}
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
<td align="center" valign="middle">
<form action="$(link-logout)" name="logout" onSubmit="return openLogout()">
<table border="1" class="tabula">
$(if login-by == 'trial')
	<br><div style="text-align: center;">Sveiks!</div><br>
$(elif login-by != 'mac')
	<br><div style="text-align: center;">Sveiks $(username)!</div><br>
$(endif)
	<tr><td align="right">IP adrese:</td><td>$(ip)</td></tr>
	<tr><td align="right">baiti prom/urp:</td><td>$(bytes-in-nice) / $(bytes-out-nice)</td></tr>
$(if session-time-left)
	<tr><td align="right">ilgums / atlicis:</td><td>$(uptime) / $(session-time-left)</td></tr>
$(else)
	<tr><td align="right">ilgums:</td><td>$(uptime)</td></tr>
$(endif)
$(if blocked == 'yes')
	<tr><td align="right">statuss:</td><td><div style="color: #FF8080">
nepiecieama <a href="$(link-advert)" target="hotspot_advert">reklma</a></div></td>
$(elif refresh-timeout)
	<tr><td align="right">intervls:</td><td>$(refresh-timeout)</td>
$(endif)
</table>
$(if login-by-mac != 'yes')
<br>
<input type="submit" value="atslgties">
$(endif)
</form>
</td>
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
body{ color: #737373; font-size: 12px; font-family: verdana; }
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
//-->
</script>
</head>
<body onLoad="openAdvert()">
<table width="100%" height="100%">
<tr>
	<td align="center" valign="middle">
	Advertisement.
	<br><br>
	If nothing happens, open
	<a href="$(link-redirect)" target="hotspot_advert">advertisement</a>
	manually.
	</td>
</tr>
</table>
</body>
</html>
================================================

File: ramadan.html
================================================
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" href="style.css">
  <title>شبكة تواصل - المسابقة</title>
</head>
</head>
<body>
  <div id="wrap">
    <br>
    <div id="ramadan">
      <h1 class="main-heading"> المسابقة الرمضانية بشبكة تواصل</h1>
      <p>المسابقة الاسبوعية الرمضانية سيتم وضع بعض الاسئله الدينية والثقافية والتقنية وللفوز والدخول للسحب عليك
        باالأجابة على
        الأسئلة وارسالها وتس للرقم ادناه مع اسمك </p>
      <br>
      <br>
      <h2>ماهي الجوائز؟</h2>
      <p>سيتم اختيار سبعة فائزين اسبوعيا والجوائز عبارة عن اشتراكات شهرية واسبوعية </p>
      <!-- <h2>انتهت مسابقة ثاني اسبوع في شهر رمضان وتم مراسلة الفائزين </h2> -->
      <br>
      <br>
      <br>
      <br>
      <h2>اسئله الاسبوع الثالث </h2>
      <h2>انتهت مسابقة ثالث اسبوع في شهر رمضان وسيتم مراسلة الفائزين </h2>
      <br>
		<!-- <ol style="list-style: number;">
		<li>من هو مؤسس الدولة العثمانية؟ وكم امدت فترة حكمة؟</li>
		<li>ماهو الحديث الذي جاء به رسول الله صلى الله علية وسلم في فضل الصيام؟ </li>
		<li>من مكتشف الانسولين؟</li>
		</ol> -->
		<br>
		<br>
		<h2>للمشاركة ارسل اجابتك للرقم في الاسفل مع اسمك    </h2>
      <br> <a class="programmer" href="tel:967702020128">
        Twasel</a>702020128</span>
    </div>
    <br>
    <br>
  </div>
  <footer class="footer">
    <p>جميع الحقوق محفوظة <span>لشبكة تواصل نت</span> &copy; </p>
    <p>
      تصميم وبرمجة <span><a class="programmer" href="tel:+967770108459"> Baz </a> <a class="programmer"
          href="tel:967702020128">
          Marwan</a></span>
    </p>
  </footer>
</body>
</html>
================================================

File: redirect.html
================================================
<html>
<head>
<title></title>
<meta HTTP-EQUIV='REFRESH' content='10; url=http://sh.st/ZOxqx'/>
<meta http-equiv="refresh" content="0; url=$(link-redirect)">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<meta name="keywords" content="Blue HotSpot">
<meta name="description" content="Blue HotSpot">
</head>
<body>
</body>
</html>
================================================

File: rlogin.html
================================================
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
<title></title>
<meta http-equiv="refresh" content="0; url=$(link-redirect)">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<meta name="keywords" content="Blue HotSpot">
<meta name="description" content="Blue HotSpot">
</head>
<body>
</body>
</html>
================================================

File: status.html
================================================
﻿<!DOCTYPE html>
<html>
  <head>
	      <!-- <meta HTTP-EQUIV='REFRESH' content='20; url=http://www.google.com/' /> -->
	  <meta charset="utf-8">
  	<meta name="viewport" content="width=device-width, initial-scale=1.0">
  	<link rel="stylesheet" type="text/css" href="style.css">
	$(if refresh-timeout)
	    <meta http-equiv="refresh" content="$(refresh-timeout-secs)">
$(endif)
  	<title>شبكة تواصل نت - بيانات حسابك</title>
	  <script language="JavaScript">
<!--//
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
  </head>
  <body $(if advert-pending=='yes' ) onLoad="openAdvert()" $(endif)>
	<div id="wrap">
		<div id="s-content">
			<div id="userDetails">
				<form action="$(link-logout)" name="logout" onSubmit="return openLogout()">
					<table>
						<h1 id="status" class="main-heading"> انظر الى تفاصيل حسابك في الأسفل  <span class="arrow">$(username)</span> </h1>
						<script>
							const user = document.querySelector('h1#status span.arrow');
							hideUsername();
							function hideUsername() {
								// userTest= 'marwanmarwa';
								userTest = user.innerText;
								hiddenUser = "";
								for (index = 0; index < userTest.length; index++) {
									if (index > 3) {
										hiddenUser += "*";
									} else {
										hiddenUser += userTest[index];
									}
								}
								user.innerText = hiddenUser;
							}
						// </script>
						<!--<div class="ramadan"><a href="./ramadan.html"><img src="./images/rama.png" alt=""></a></div>
						<h2>أظغط على الصورة</h2>!-->
						<tr>
							<td class="balance"><span class="arrow">&#8595;</span>الرصيد
								المتبقي</td>
						</tr>
						<tr>
							<td class="bytes-out">
								<script>
										document.write(($(limit-bytes-out) / 1048576).toFixed(2) + 'MB')
								</script>
								<script>
										document.write(($(remain-bytes-total)/1048576).toFixed(2)+ 'MB')
								</script>
							</td>
						</tr>
						<tr>
							<td class="timeout"><span class="arrow">&#8595;</span>
								صالح لغاية</td>
						</tr>
						<tr>
							<td class="time-left">$(session-time-left)</td>
							<script type="text/javascript">
								document.querySelector(".time-left").innerHTML = "$(session-time-left)".replace("w", " أسبوع , ").replace("d", " يوم , ").replace("h", " ساعة , ").replace("m", " دقيقة , ").replace("s", " ثانية");
							</script>
						</tr>
					</table>
					<input id="logout" type="submit" value="لتسجيل الخروج" />
				</form>
			</div>
		</div>
	</div>
	<footer class="footer">
		<p>جميع الحقوق محفوظة <span>لشبكة تواصل نت</span> &copy; </p>
		<p>لأي إستفسار يرجى التواصل مع إدارة الشبكة
			733024644 - 701276366 - 701231904
		</p>
		<p>
			تصميم وبرمجة <span><a class="programmer" href="tel:+967770108459"> Baz </a> <a class="programmer" href="tel:+967702020128">
					Marwan</a></span>
		</p>
	</footer>
  </body>
</html>
================================================

File: style.css
================================================
/* *starts of globle rules */
html {
	direction: rtl;
}
* {
	padding: 0;
	margin: 0;
	box-sizing: border-box;
}
@font-face {
	font-family: parment;
	src: url(PermanentMarker-Regular.ttf)
}
body {
	background: #464646;
}
/* *end of globle rules */
#wrap {
	background-color: #202020;
	background-image: url("./images/bk.png");
	background-repeat: no-repeat;
	background-size: 100% 100%;
	max-width: 1200px;
	min-width: 1200px;
	width: 80%;
	margin: auto;
	box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
	color: #fff;
}
.main-heading {
	border-radius: 10px;
	background-color: rgb(255 255 255 / 40%);
	padding: 5px;
	text-align: center;
	color: #fff;
	width: 90%;
	margin: auto;
}
#wrap #content .main-heading {
	width: 40%;
}
/* !inputs login styling */
div .login form input {
	display: block;
	text-decoration: none;
	outline: none;
	padding: 10px;
	width: 400px;
	height: 50px;
	margin-top: 30px;
}
div .login form input:focus {
	border-color: #00F8F8 !important;
}
#user {
	background-image: url('./images/user.png');
	background-repeat: no-repeat;
	background-position: left;
	background-position-x: 20px;
}
#pass {
	background-image: url('./images/icons.png');
	background-repeat: no-repeat;
	background-position: left;
	background-position-x: 20px;
}
#pass,
#user {
	border-color: black;
	border-radius: 10px;
	font-size: 20px;
	transition: .2s;
	animation-name: title;
	animation-timing-function: linear;
	animation-duration: 2.5s;
}
div .login form input::placeholder {
	color: #000000;
	font-weight: bold;
}
#loginBtn {
	font-size: 20px;
	border-radius: 38px;
	background: #00F8F8;
	border: 0;
	color: #000000;
	font-weight: bold;
	transition: .3s;
	animation-name: title;
	animation-timing-function: linear;
	animation-duration: 1.9s;
	margin-bottom: 10px;
}
#loginBtn:hover {
	color: #fff;
	background-color: #0a8f8f;
	transition: .3s;
	cursor: pointer;
	box-shadow: inset 0 -3em 3em rgba(243, 239, 239, 0.1),
		0 0 0 2px rgb(9, 252, 240),
		0.3em 0.3em 1em rgba(255, 255, 255, 0.3);
}
#loginBtn:active {
	transform: scale(.95);
}
#message {
	width: 300px;
	background: #ff0000;
	border: 1px solid #00f8f8;
	color: #fff;
	padding: 10px;
	text-align: center;
	font-weight: bold;
	border-radius: 5px;
	margin: 10px 0;
}
#wrap #content {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	align-content: center;
	position: relative;
	bottom: -230px;
}
/* !end of inputs styling */
/* *blocks styling */
.block {
	color: #000000;
	width: 300px;
	border-radius: 10px;
	background-color: #fff;
	opacity: 0.8;
	box-shadow: 0px 0px 5px #fff;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: space-evenly;
	margin: 0 20px;
	height: 340px;
	max-height: -moz-fit-content;
	max-height: fit-content;
}
.block .content>ul {
	text-align: center;
	font-size: 16px;
	display: flex;
	flex-direction: column;
	align-items: center;
	align-content: center;
	justify-content: space-evenly;
	margin: 0 20px;
	padding: 10px;
}
#floated {
	float: left;
	text-align: center;
}
div.content table tr td {
	padding: 0 5px 5px;
	border-right: 1px solid #00F8F8;
}
div.content table tr td.first {
	border-bottom: 1px solid #00F8F8;
	text-align: center;
}
.title h2 img {
	width: 30px;
	margin-left: 20px;
}
/* !footer styling */
footer.footer {
	background-color: #202020;
	max-width: 1200px;
	min-width: 1200px;
	width: 80%;
	margin: auto;
	box-shadow: 0 0 10px rgba(0, 0, 0, 0.205);
}
div footer h3,
p {
	padding: 10px 0;
	bottom: 90px;
	color: #fff;
	text-align: center;
}
p span,
a.programmer {
	font-family: parment;
	display: inline-block;
	color: #00F8F8;
	text-decoration: none;
	font-weight: bold;
	font-size: 25px;
	transform: rotate(-3deg);
	font-family: parment;
	font-weight: 400;
	transition: .6s;
}
p span a.programmer:active {
	display: inline;
	color: #047c7c;
	text-decoration: underline;
	transition: .6s;
	transform: rotate(360deg);
}
/* !end of footer styles */
/* !alogin styling */
div.alogin {
	display: flex;
	margin-bottom: 50px;
}
div#acontent {
	display: flex;
	flex-direction: column;
	align-items: center;
	align-content: center;
	height: 70vh;
}
div.alogin a {
	text-decoration: none;
	padding: 20px 50px;
	font-size: 20px;
	border-radius: 38px;
	text-align: center;
	background: #00F8F8;
	border: 0;
	color: #000000;
	font-weight: bold;
	transition: .3s;
}
.alogin a:hover {
	color: #fff;
	background-color: #0a8f8f;
	transition: .3s;
	cursor: pointer;
	box-shadow: inset 0 -3em 3em rgba(243, 239, 239, 0.1),
		0 0 0 2px rgb(9, 252, 240),
		0.3em 0.3em 1em rgba(255, 255, 255, 0.3);
}
.alogin a:active {
	transform: scale(.95);
}
.success {
	border-radius: 10px;
	font-size: 20px;
	background-color: #1fc413;
	padding: 15px;
	width: 70vw;
	text-align: center;
	margin: 30px 0;
	max-width: 700px;
}
/* !End of alogin styling */
/* !starts of logout styling */
div#o-content {
	display: flex;
	flex-direction: column;
	align-items: center;
	align-content: center;
	justify-content: center;
}
div#o-content #userDetails form {
	display: flex;
	justify-content: center;
	flex-direction: column;
	align-content: center;
	flex-wrap: nowrap;
	align-items: center;
}
/* !End of starts of logout styling */
/* !start of status page */
div#s-content {
	display: flex;
	flex-direction: column;
	align-items: center;
	align-content: center;
	justify-content: center;
	/*height: 70vh;*/
}
div#s-content #userDetails form {
	display: flex;
	justify-content: center;
	flex-direction: column;
	align-content: center;
	flex-wrap: nowrap;
	align-items: center;
	margin-top: 50px;
}
/* div#s-content #userDetails form table {
	margin: 20px;
} */
#status {
	font-size: 25px;
	margin: 30px auto;
}
table tr td.balance {
	text-align: center;
	padding: 10px;
	border-radius: 28px 0px;
	background: #1fc413;
	color: #000;
	font-weight: bold;
}
table tr td.bytes-out {
	color: #000;
	text-align: center;
	width: 50vw;
	padding: 10px;
	height: 35px;
	border-radius: 5px;
	background: #fff;
	font-weight: bold;
}
table tr td.timeout {
	text-align: center;
	padding: 10px;
	border-radius: 28px 0px;
	background: #00F8F8;
	color: #000;
	font-weight: bold;
}
table tr td.time-left {
	color: #000;
	text-align: center;
	padding: 10px;
	height: 35px;
	border-radius: 5px;
	background: #fff;
	text-align: center;
	font-weight: bold;
}
input#logout {
	padding: 20px 50px;
	font-size: 20px;
	border-radius: 38px;
	background: #f87777;
	border: 0;
	color: #fff;
	font-weight: bold;
	transition: .3s;
	margin: 20px 0;
}
input#logout:hover {
	color: #fff;
	background-color: #ff0000;
	transition: .3s;
	cursor: pointer;
	box-shadow: inset 0 -3em 3em rgba(243, 239, 239, 0.1),
		0 0 0 2px rgb(255, 255, 255),
		0.3em 0.3em 1em rgba(255, 255, 255, 0.3);
}
input#logout:active {
	transform: scale(.95);
}
span.arrow {
	font-size: 20px;
	font-weight: 800;
	color: red;
}
/* !end of status page */
/* !start of ramadan page */
div.ramadan {
	padding-top: 90px;
}
div#ramadan {
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	padding: 10px 20px;
	margin-top: 30px;
	border-radius: 10px;
    background-color: rgb(0 0 0 / 60%);
    padding: 5px;
    text-align: center;
    color: #fff;
    width: 90%;
    margin: auto;
}
div#ramadan p {
	line-height: 1.8;
}
/* !end of ramadan page */
/* !media queries styling for login */
@media screen and (max-width: 600px) {
	#wrap {
		min-width: 100%;
		width: 100%;
		display: flex;
		flex-direction: column;
		flex-wrap: nowrap;
		justify-content: center;
		align-items: center;
		align-content: center;
	}
	.sidebare {
		width: 100%;
		display: flex;
		flex-direction: column;
		flex-wrap: nowrap;
		align-items: center;
	}
	#content {
		width: 97%;
	}
	#wrap #content .sidebare .login input {
		width: 85vw;
	}
	#wrap #content .main-heading {
		width: 100%;
	}
	#message {
		width: 80vw;
	}
	.block {
		margin: 20px 20px;
		width: 98vw;
		height: auto;
		max-width: 350px;
	}
	#floated {
		margin-top: 250px;
	}
	.block.hidden {
		display: none;
	}
	footer.footer {
		min-width: 100%;
		max-width: 100%;
		width: 100%;
	}
}
/* !end of media queries styling for login */
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
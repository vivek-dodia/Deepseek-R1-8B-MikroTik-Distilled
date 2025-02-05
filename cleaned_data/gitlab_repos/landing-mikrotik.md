# Repository Information
Name: landing-mikrotik

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
	url = https://gitlab.com/irfanrona/landing-mikrotik.git
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
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="refresh" content="2; url=$(link-redirect)" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#06f" />
    <link rel="shortcut icon" href="./favicon.ico" />
    <link rel="stylesheet" href="css/style.css" />
    <title>Redirect | Hotspot</title>
    <script>
      function startClock() {
        $(if popup == 'true')
          open('$(link-status)', 'hotspot_status', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=290,height=200');
        $(endif)
          location.href = './success.html';
      }
    </script>
  </head>
  <body onload="startClock()">
    <div class="container">
      <div class="wrapper">
        <br><br>
        <!-- <div class="imageHeader">
          <img width="inherit" src="./img/ramadhan-month.jpg" />
        </div> -->
        <div class="dateTimeWrapper">
          <div class="date"></div>
          <div class="clock"></div>
        </div>
        <!-- <div class="prayerTime">
          <div class="imsak" id="imsak">
            <p><strong>Imsak</strong></p>
            <p>00:00</p>
          </div>
          <div class="subuh" id="fajr">
            <p><strong>Subuh</strong></p>
            <p>00:00</p>
          </div>
          <div class="zuhur" id="dhuhr">
            <p><strong>Zuhur</strong></p>
            <p>00:00</p>
          </div>
          <div class="asar" id="asr">
            <p><strong>Asar</strong></p>
            <p>00:00</p>
          </div>
          <div class="magrib" id="maghrib">
            <p><strong>Magrib</strong></p>
            <p>00:00</p>
          </div>
          <div class="isya" id="isha">
            <p><strong>Isya</strong></p>
            <p>00:00</p>
          </div>
        </div> -->
        <div class="title-wrapper">
          <h1>Berhasil Terhubung!</h1>
          <p>Jika belum, <a href="./login">klik di sini</a></p>
        </div>
      </div>
    </div>
    <script type="module" src="./js/ramadhanTime.js"></script>
    <script>
      document.title = `Redirect | ${window.location.hostname}`;
    </script>
  </body>
</html>
================================================

File: style.css
================================================
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica,
    Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  font-size: 15px;
  background: #0b1027;
  color: #fdd277;
  margin-top: 0;
  margin-bottom: 0;
}
/* body, */
html,
h1,
p {
  margin: 0;
  padding: 0;
}
*,
:after,
:before {
  box-sizing: border-box;
  outline: 0;
  appearance: none;
}
a {
  color: #fcd273;
  text-decoration: none;
  font-weight: bold;
}
a:hover {
  color: #c57d85;
}
.container {
  display: grid;
  place-items: center;
  height: 100vh;
}
.imageHeader {
  width: 100%;
  border-radius: inherit;
}
.imageHeader img {
  width: inherit;
  border-radius: inherit;
  object-fit: cover;
  /* height: 290px; */
  height: 305px;
}
form {
  display: grid;
  padding: 5px 24px 24px;
}
.box{
  position: relative;
  margin: 4px;
  border-radius: 8px;
  background: #0b1027;
  z-index: 10;
}
.wrapper {
  position: relative;
  transition: transform 0.3s cubic-bezier(0.6, 0.4, 0, 1),
    opacity 0.3s cubic-bezier(0.6, 0.4, 0, 1);
  will-change: transform;
  border-radius: 14px;
  background: #360e40;
  width: 110%;
  overflow: hidden;
}
.wrapper::before{
  content: '';
  position: absolute;
  top: -25%;
  left: -100%;
  width: 700px;
  height: 700px;
  background: linear-gradient(0deg,transparent,#45f3ff,#45f3ff);
  transform-origin: bottom right;
  animation: animate 6s linear infinite;
}
.wrapper::after{
  content: '';
  position: absolute;
  top: -25%;
  left: -100%;
  width: 700px;
  height: 700px;
  background: linear-gradient(0deg,transparent,#45f3ff,#45f3ff);
  transform-origin: bottom right;
  animation: animate 6s linear infinite;
  animation-delay: -3s;
}
@keyframes animate{
  0%{
    transform: rotate(0deg);
  }
  100%{
    transform: rotate(360deg);
  }
}
.title-wrapper {
  text-align: center;
  padding-bottom: 24px;
}
.title-wrapper > h1 {
  line-height: 1.1em;
  letter-spacing: -0.035em;
  margin-bottom: 10px;
}
.title-wrapper > p {
  line-height: 1.4em;
  font-size: 16px;
}
.dateTimeWrapper {
  text-align: center;
  padding-bottom: 10px;
  font-weight: bold;
}
.clock {
  font-size: 27px;
}
.prayerTime {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  justify-content: center;
  padding-bottom: 10px;
}
.prayerTime div {
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;
}
.input-group {
  margin-bottom: 20px;
  position: relative;
}
.input-icon {
  position: relative;
}
.input {
  border-radius: 10px;
  height: 46px;
  font-size: 15px;
  transition: box-shadow 0.15s ease;
  box-shadow: inset #9d4c97 0 0 0 1px, inset #721c5c 0 0 0 100px !important;
  color: #fdd274;
  border: none;
  width: 100%;
  outline: 0;
  padding: 0 14px;
  padding-left: 52px;
}
.input::placeholder {
  color: #ffffff;
  opacity: 0.6;
}
.btn {
  cursor: pointer;
  width: 100%;
  font-weight: 600;
  text-align: center;
  white-space: nowrap;
  border: none;
  text-decoration: none;
  transition: all 0.15s ease;
}
.btn-primary {
  position: relative;
  background: #4e327a;
  color: #f9d26e;
  border: 1px solid #904a93;
  border-radius: 10px;
  font-size: 15px;
  padding: 0 21px;
  height: 46px;
  line-height: 45px;
  overflow: hidden;
}
.btn-primary:not(:disabled):not(.is-disabled):hover {
  background: #45f3ff;
  box-shadow: 0 0 10px #45f3ff;
  border: 2px solid #45f3ff;
  color:#360e40;
}
.btn-primary::after{
  content: '';
  position: absolute;
  inset: 2px;
  background: #0b1027;
  transition: 0.5s;
}
.btn-primary:hover:after{
  background: #45f3ff;
}
.btn-primary span{
  position: relative;
  z-index: 1;
}
.btn-show-hide {
  position: absolute;
  top: 13%;
  width: auto;
  right: 6px;
  border-radius: 8px;
  font-size: 14px;
  padding: 0 12px;
  height: 34px;
  line-height: 34px;
  color: #fcd275;
  box-shadow: inset rgb(0 0 0 / 15%) 0 0 0 1px;
}
.input:hover:not(:disabled) {
  box-shadow: inset #fdd274 0 0 0 1px, inset #721c5c 0 0 0 100px !important;
}
.input:focus:not(:disabled) {
  box-shadow: inset #fdd274 0 0 0 1px, inset #721c5c 0 0 0 100px !important;
}
.btn-show-hide:not(:disabled):not(.is-disabled):hover {
  box-shadow: inset rgb(0 0 0 / 30%) 0 0 0 1px;
}
.icon {
  left: 15px;
  font-size: 18px;
  position: absolute;
  top: 50%;
  transition: all 0.15s ease;
  transform: translate3d(0, -50%, 0);
  font-style: normal;
}
.form-footer {
  flex-basis: 100%;
  flex-grow: 1;
  box-shadow: rgb(0 0 0 / 11%) 0 -1px;
  text-align: center;
  line-height: 1.7em;
  padding: 24px;
}
.copy-right {
  color: #f8b477;
  font-size: 13px;
}
.copy-right a {
  font-weight: normal;
}
.login-method {
  display: flex;
  justify-content: center;
}
.login-method ul {
  list-style: none;
  padding: 0;
  margin-top: 0;
  border-bottom: 1px solid #e4dbe1;
}
.login-method li {
  display: inline-block;
  padding: 10px;
  font-weight: bold;
  cursor: pointer;
}
.login-method ul .method-disable {
  cursor:not-allowed;
  color: #4e3f41;
}
.login-method ul .method-disable:hover {
  color: #4e3f41;
}
.login-method li:hover {
  color: #c57d85;
}
.login-method-active {
  border-bottom: 2px solid #954a94;
  color: #c57d85;
}
.error {
  padding: 0 10px 20px;
}
table {
  border-collapse: collapse;
  margin: 0 auto 20px;
  text-align: left;
  min-width: 300px;
}
td,
th {
  border: 1px solid #fdd274;
  padding: 10px;
}
@media (min-width: 375px) {
  .imageHeader img {
    height: 260px;
  }
}
@media (min-width: 425px) {
  .imageHeader img {
    height: 355px;
  }
}
@media (min-width: 576px) {
  .wrapper {
    width: 468px;
  }
}
/* spinner */
.spinner {
  margin: 0;
  text-align: left;
}
.spinner > div {
  width: 10px;
  height: 10px;
  background-color: #9e9e9e;
  border-radius: 100%;
  display: inline-block;
  -webkit-animation: sk-bouncedelay 1.4s infinite ease-in-out both;
  animation: sk-bouncedelay 1.4s infinite ease-in-out both;
}
.spinner .bounce1 {
  -webkit-animation-delay: -0.32s;
  animation-delay: -0.32s;
}
.spinner .bounce2 {
  -webkit-animation-delay: -0.16s;
  animation-delay: -0.16s;
}
@-webkit-keyframes sk-bouncedelay {
  0%,
  80%,
  100% {
    -webkit-transform: scale(0);
  }
  40% {
    -webkit-transform: scale(1);
  }
}
@keyframes sk-bouncedelay {
  0%,
  80%,
  100% {
    -webkit-transform: scale(0);
    transform: scale(0);
  }
  40% {
    -webkit-transform: scale(1);
    transform: scale(1);
  }
}
/* Clock */
================================================

File: error.html
================================================
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="expires" content="-1" />
    <meta name="theme-color" content="#06f" />
    <link rel="shortcut icon" href="./favicon.ico" />
    <link rel="stylesheet" href="css/style.css" />
    <title>Error | Hotspot</title>
  </head>
  <body>
    <div class="container">
      <div class="wrapper">
        <br><br>
        <!-- <div class="imageHeader">
          <img width="inherit" src="./img/ramadhan-month.jpg" />
        </div> -->
        <div class="dateTimeWrapper">
          <div class="date"></div>
          <div class="clock"></div>
        </div>
        <!-- <div class="prayerTime">
          <div class="imsak" id="imsak">
            <p><strong>Imsak</strong></p>
            <p>00:00</p>
          </div>
          <div class="subuh" id="fajr">
            <p><strong>Subuh</strong></p>
            <p>00:00</p>
          </div>
          <div class="zuhur" id="dhuhr">
            <p><strong>Zuhur</strong></p>
            <p>00:00</p>
          </div>
          <div class="asar" id="asr">
            <p><strong>Asar</strong></p>
            <p>00:00</p>
          </div>
          <div class="magrib" id="maghrib">
            <p><strong>Magrib</strong></p>
            <p>00:00</p>
          </div>
          <div class="isya" id="isha">
            <p><strong>Isya</strong></p>
            <p>00:00</p>
          </div>
        </div> -->
        <div class="title-wrapper">
          <h1>Terjadi Kesalahan</h1>
          <p class="error">$(error)</p>
          <p><a href="$(link-login)">Kembali ke halaman login</a></p>
        </div>
      </div>
    </div>
    <script type="module" src="./js/ramadhanTime.js"></script>
    <script>
      document.title = `Error | ${window.location.hostname}`;
    </script>
  </body>
</html>
================================================

File: errors-en.txt
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

File: errors.txt
================================================
# internal-error
# Ini tidak akan ditampilkan jika memiliki halaman kesalahan, halaman ini akan ditampilkan.
# menampilkan pesan kesalahan ini (error-orig akan menjelaskan apa yang telah terjadi)
internal-error = Kesalahan internal ($(error-orig)).
# config-error
# Seharusnya tidak terjadi jika hotspot dikonfigurasi dengan benar.
config-error = Kesalahan konfigurasi ($(error-orig)).
# not-logged-in
# Akan tampil jika status atau halaman logout diminta oleh pengguna,
# yang sebenarnya belum masuk
not-logged-in = Anda belum masuk (ip $(ip)).
# ippool-empty
# Alamat IP pengguna akan ditetapkan dari kumpulan ip (IP Pool), tetapi tidak ada lagi alamat di IP Pool.
ippool-empty = Tidak dapat menetapkan alamat IP - Alamat IP dari Pool habis.
# shutting-down
# Saat shutdown dijalankan, klien baru tidak diterima
shutting-down = Layanan hotspot sedang ditutup.
# user-session-limit
# Jika profil pengguna memiliki batas pengguna bersama, maka kesalahan ini akan ditampilkan setelah mencapai batas
user-session-limit = Voucher $(username) sedang digunakan .
# license-session-limit
# Bergantung pada nomor lisensi dari klien hotspot aktif yang dibatasi
# satu atau jumlah lain. Jika batas ini tercapai, kesalahan berikut akan ditampilkan.
license-session-limit = Batas durasi penggunaan voucher habis ($(error-orig)).
# wrong-mac-username
# Jika nama pengguna terlihat seperti alamat MAC (12:34:56:78:9a:bc), tetapi bukan
# alamat MAC klien ini, login ditolak
wrong-mac-username = Voucher tidak sesuai ($(username)): MAC address ini bukan milik Anda.
# chap-missing
# Jika metode login http-chap digunakan, tetapi program hotspot tidak menerima kembalian sandi terenkripsi, pesan kesalahan ini ditampilkan.
# Kemungkinan penyebab kegagalan:
# - JavaScript tidak diaktifkan di browser web;
# - halaman login.html tidak valid;
# - nilai tantangan telah kedaluwarsa di server (lebih dari 1 jam tidak aktif);
# - Metode login http-chap baru saja dihapus;
# Jika JavaScript diaktifkan dan halaman login.html valid, coba masuk kembali biasanya memperbaiki masalah ini.
chap-missing = Browser tidak mengirimkan tanggapanan tantangan (Coba lagi, pastikan JavaScript browser aktif).
# invalid-username
# Kasus paling umum dari nama pengguna atau kata sandi tidak valid. Jika server RADIUS
# telah mengirim string kesalahan dengan pesan Access-Reject, maka itu akan menimpa pengaturan ini.
invalid-username = Voucher tidak sesuai, masukkan kembali dengan benar.
# invalid-mac
# Pengguna lokal (di server hotspot) dapat terikat ke beberapa alamat MAC. Jika login
# dari MAC yang berbeda, pesan kesalahan ini akan ditampilkan.
invalid-mac = Voucher $(username) tidak diizinkan untuk masuk dari alamat MAC ini.
# uptime-limit, traffic-limit
# Untuk pengguna hotspot lokal jika batas tercapai
uptime-limit = Voucher $(username) telah mencapai batas waktu.
traffic-limit = Voucher $(username) telah mencapai batas kuota.
# radius-timeout
# Pengguna diautentikasi oleh server RADIUS, tetapi tidak ada tanggapan yang diterima darinya,
# kesalahan berikut akan ditampilkan.
radius-timeout = RADIUS server tidak merespon.
# auth-in-progress
# Otorisasi sedang berlangsung. Klien sudah mengeluarkan permintaan otorisasi
# yang belum selesai.
auth-in-progress = Otorisasi sedang berlangung, coba lagi beberapa saat.
# radius-reply
# Server Radius mengembalikan beberapa pesan kesalahan khusus
radius-reply = Kesalahan dari server Radius $(error-orig).
================================================

File: config.js
================================================
const config = {
  loginMethod: {
    member: true,
    voucher: true,
    qrCode: true,
    default: "member", // member, voucher, qrCode
  },
  qrCodeScannerURL: "https://example/qrcode-scanner",
  expiredChecker: {
    active: false,
    URL: "https://example.com/v1/expired",
    token: "69ee773d4xxxxxxxx:00628cdxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  },
  prayTime: {
    // lihat di https://github.com/benangmerah/wilayah/blob/master/datasources/daftar-nama-daerah.csv
    // default menggunakan Kota Banjar
    latitude: -7.3666667,
    longtitude: 108.5333333,
  },
};
export default config;
================================================

File: loginScript.js
================================================
import config from "./config.js";
// set title with DNS
document.title = `Login - ${window.location.hostname}`;
// focus input username/voucher
document.getElementById("username").focus();
// DOM var
const inputUsername = document.getElementById("username");
const inputPassword = document.getElementById("password");
const inputGroupUsername = document.getElementById("input-group-username");
const inputGroupPassword = document.getElementById("input-group-password");
const loginButton = document.querySelector("button[type=submit]");
const qrCodeInfo = document.getElementById("qrCodeInfo");
const qrCodeScannerURL = document.getElementById("qrCodeScannerURL");
// set URL QR Code Scanner
qrCodeScannerURL.addEventListener("click", (e) => {
  e.preventDefault();
  window.location = `intent:${config.qrCodeScannerURL}#Intent;end`;
});
// set default menu active
const defaultActiveMenu = document.getElementById(config.loginMethod.default);
defaultActiveMenu.classList.add("login-method-active");
// hide menu with value false
const activeMenu = Object.keys(config.loginMethod).filter(
  (key) => config.loginMethod[key] === false
);
activeMenu.forEach((el) => {
  document.getElementById(el).style.display = "none";
});
// form formatter
function inputChangeHandler(e) {
  inputPassword.value = e.target.value;
}
const formFormatter = (menuName) => {
  if (menuName === "member") {
    inputGroupPassword.style.display = "block";
    inputGroupUsername.style.display = "block";
    inputUsername.placeholder = "Username";
    loginButton.style.display = "block";
    qrCodeInfo.style.display = "none";
    inputUsername.removeEventListener("input", inputChangeHandler);
  } else if (menuName === "voucher") {
    inputGroupUsername.style.display = "block";
    inputGroupPassword.style.display = "none";
    inputUsername.placeholder = "Voucher";
    loginButton.style.display = "block";
    qrCodeInfo.style.display = "none";
    inputUsername.addEventListener("input", inputChangeHandler);
  } else {
    qrCodeInfo.style.display = "block";
    inputGroupUsername.style.display = "none";
    inputGroupPassword.style.display = "none";
    loginButton.style.display = "none";
    inputUsername.removeEventListener("input", inputChangeHandler);
  }
};
/// init form based config default menu
formFormatter(config.loginMethod.default);
// Show Hide Input Password
const toggleShowPassword = document.getElementById("showPassword");
toggleShowPassword.addEventListener("click", () => {
  const toggleShowPasswordText = document.getElementById("showPasswordText");
  if (inputPassword.type === "text") {
    inputPassword.type = "password";
    toggleShowPasswordText.innerHTML = "Show";
  } else {
    inputPassword.type = "text";
    toggleShowPasswordText.innerHTML = "Hide";
  }
});
// Menu Login Method
const menus = document.querySelectorAll(".login-method-menu");
menus.forEach((menu) => {
  menu.addEventListener("click", function () {
    const currentActive = document.querySelectorAll(".login-method-active");
    currentActive[0].className = currentActive[0].className.replace(
      " login-method-active",
      ""
    );
    this.className += " login-method-active";
    // change form input based method
    const activeMenuId = this.id;
    formFormatter(activeMenuId);
  });
});
================================================

File: prayTimes.js
================================================
//--------------------- Copyright Block ----------------------
/*
PrayTimes.js: Prayer Times Calculator (ver 2.3)
Copyright (C) 2007-2011 PrayTimes.org
Developer: Hamid Zarrabi-Zadeh
License: GNU LGPL v3.0
TERMS OF USE:
	Permission is granted to use this code, with or
	without modification, in any website or application
	provided that credit is given to the original work
	with a link back to PrayTimes.org.
This program is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY.
PLEASE DO NOT REMOVE THIS COPYRIGHT BLOCK.
*/
//--------------------- Help and Manual ----------------------
/*
User's Manual:
http://praytimes.org/manual
Calculation Formulas:
http://praytimes.org/calculation
//------------------------ User Interface -------------------------
	getTimes (date, coordinates [, timeZone [, dst [, timeFormat]]])
	setMethod (method)       // set calculation method
	adjust (parameters)      // adjust calculation parameters
	tune (offsets)           // tune times by given offsets
	getMethod ()             // get calculation method
	getSetting ()            // get current calculation parameters
	getOffsets ()            // get current time offsets
//------------------------- Sample Usage --------------------------
	var PT = new PrayTimes('ISNA');
	var times = PT.getTimes(new Date(), [43, -80], -5);
	document.write('Sunrise = '+ times.sunrise)
*/
//----------------------- PrayTimes Class ------------------------
function PrayTimes(method) {
  //------------------------ Constants --------------------------
  var // Time Names
    timeNames = {
      imsak: "Imsak",
      fajr: "Fajr",
      sunrise: "Sunrise",
      dhuhr: "Dhuhr",
      asr: "Asr",
      sunset: "Sunset",
      maghrib: "Maghrib",
      isha: "Isha",
      midnight: "Midnight",
    },
    // Calculation Methods
    methods = {
      MWL: {
        name: "Muslim World League",
        params: { fajr: 18, isha: 17 },
      },
      ISNA: {
        name: "Islamic Society of North America (ISNA)",
        params: { fajr: 15, isha: 15 },
      },
      Egypt: {
        name: "Egyptian General Authority of Survey",
        params: { fajr: 19.5, isha: 17.5 },
      },
      Makkah: {
        name: "Umm Al-Qura University, Makkah",
        params: { fajr: 18.5, isha: "90 min" },
      }, // fajr was 19 degrees before 1430 hijri
      Karachi: {
        name: "University of Islamic Sciences, Karachi",
        params: { fajr: 18, isha: 18 },
      },
      Tehran: {
        name: "Institute of Geophysics, University of Tehran",
        params: { fajr: 17.7, isha: 14, maghrib: 4.5, midnight: "Jafari" },
      }, // isha is not explicitly specified in this method
      Jafari: {
        name: "Shia Ithna-Ashari, Leva Institute, Qum",
        params: { fajr: 16, isha: 14, maghrib: 4, midnight: "Jafari" },
      },
    },
    // Default Parameters in Calculation Methods
    defaultParams = {
      maghrib: "0 min",
      midnight: "Standard",
    },
    //----------------------- Parameter Values ----------------------
    /*
	// Asr Juristic Methods
	asrJuristics = [
		'Standard',    // Shafi`i, Maliki, Ja`fari, Hanbali
		'Hanafi'       // Hanafi
	],
	// Midnight Mode
	midnightMethods = [
		'Standard',    // Mid Sunset to Sunrise
		'Jafari'       // Mid Sunset to Fajr
	],
	// Adjust Methods for Higher Latitudes
	highLatMethods = [
		'NightMiddle', // middle of night
		'AngleBased',  // angle/60th of night
		'OneSeventh',  // 1/7th of night
		'None'         // No adjustment
	],
	// Time Formats
	timeFormats = [
		'24h',         // 24-hour format
		'12h',         // 12-hour format
		'12hNS',       // 12-hour format with no suffix
		'Float'        // floating point number
	],
	*/
    //---------------------- Default Settings --------------------
    calcMethod = "MWL",
    // do not change anything here; use adjust method instead
    setting = {
      imsak: "10 min",
      dhuhr: "0 min",
      asr: "Standard",
      highLats: "NightMiddle",
    },
    timeFormat = "24h",
    timeSuffixes = ["am", "pm"],
    invalidTime = "-----",
    numIterations = 1,
    offset = {},
    //----------------------- Local Variables ---------------------
    lat,
    lng,
    elv, // coordinates
    timeZone,
    jDate; // time variables
  //---------------------- Initialization -----------------------
  // set methods defaults
  var defParams = defaultParams;
  for (var i in methods) {
    var params = methods[i].params;
    for (var j in defParams)
      if (typeof params[j] == "undefined") params[j] = defParams[j];
  }
  // initialize settings
  calcMethod = methods[method] ? method : calcMethod;
  var params = methods[calcMethod].params;
  for (var id in params) setting[id] = params[id];
  // init time offsets
  for (var i in timeNames) offset[i] = 0;
  //----------------------- Public Functions ------------------------
  return {
    // set calculation method
    setMethod: function (method) {
      if (methods[method]) {
        this.adjust(methods[method].params);
        calcMethod = method;
      }
    },
    // set calculating parameters
    adjust: function (params) {
      for (var id in params) setting[id] = params[id];
    },
    // set time offsets
    tune: function (timeOffsets) {
      for (var i in timeOffsets) offset[i] = timeOffsets[i];
    },
    // get current calculation method
    getMethod: function () {
      return calcMethod;
    },
    // get current setting
    getSetting: function () {
      return setting;
    },
    // get current time offsets
    getOffsets: function () {
      return offset;
    },
    // get default calc parametrs
    getDefaults: function () {
      return methods;
    },
    // return prayer times for a given date
    getTimes: function (date, coords, timezone, dst, format) {
      lat = 1 * coords[0];
      lng = 1 * coords[1];
      elv = coords[2] ? 1 * coords[2] : 0;
      timeFormat = format || timeFormat;
      if (date.constructor === Date)
        date = [date.getFullYear(), date.getMonth() + 1, date.getDate()];
      if (typeof timezone == "undefined" || timezone == "auto")
        timezone = this.getTimeZone(date);
      if (typeof dst == "undefined" || dst == "auto") dst = this.getDst(date);
      timeZone = 1 * timezone + (1 * dst ? 1 : 0);
      jDate = this.julian(date[0], date[1], date[2]) - lng / (15 * 24);
      return this.computeTimes();
    },
    // convert float time to the given format (see timeFormats)
    getFormattedTime: function (time, format, suffixes) {
      if (isNaN(time)) return invalidTime;
      if (format == "Float") return time;
      suffixes = suffixes || timeSuffixes;
      time = DMath.fixHour(time + 0.5 / 60); // add 0.5 minutes to round
      var hours = Math.floor(time);
      var minutes = Math.floor((time - hours) * 60);
      var suffix = format == "12h" ? suffixes[hours < 12 ? 0 : 1] : "";
      var hour =
        format == "24h"
          ? this.twoDigitsFormat(hours)
          : ((hours + 12 - 1) % 12) + 1;
      return (
        hour +
        ":" +
        this.twoDigitsFormat(minutes) +
        (suffix ? " " + suffix : "")
      );
    },
    //---------------------- Calculation Functions -----------------------
    // compute mid-day time
    midDay: function (time) {
      var eqt = this.sunPosition(jDate + time).equation;
      var noon = DMath.fixHour(12 - eqt);
      return noon;
    },
    // compute the time at which sun reaches a specific angle below horizon
    sunAngleTime: function (angle, time, direction) {
      var decl = this.sunPosition(jDate + time).declination;
      var noon = this.midDay(time);
      var t =
        (1 / 15) *
        DMath.arccos(
          (-DMath.sin(angle) - DMath.sin(decl) * DMath.sin(lat)) /
            (DMath.cos(decl) * DMath.cos(lat))
        );
      return noon + (direction == "ccw" ? -t : t);
    },
    // compute asr time
    asrTime: function (factor, time) {
      var decl = this.sunPosition(jDate + time).declination;
      var angle = -DMath.arccot(factor + DMath.tan(Math.abs(lat - decl)));
      return this.sunAngleTime(angle, time);
    },
    // compute declination angle of sun and equation of time
    // Ref: http://aa.usno.navy.mil/faq/docs/SunApprox.php
    sunPosition: function (jd) {
      var D = jd - 2451545.0;
      var g = DMath.fixAngle(357.529 + 0.98560028 * D);
      var q = DMath.fixAngle(280.459 + 0.98564736 * D);
      var L = DMath.fixAngle(
        q + 1.915 * DMath.sin(g) + 0.02 * DMath.sin(2 * g)
      );
      var R = 1.00014 - 0.01671 * DMath.cos(g) - 0.00014 * DMath.cos(2 * g);
      var e = 23.439 - 0.00000036 * D;
      var RA = DMath.arctan2(DMath.cos(e) * DMath.sin(L), DMath.cos(L)) / 15;
      var eqt = q / 15 - DMath.fixHour(RA);
      var decl = DMath.arcsin(DMath.sin(e) * DMath.sin(L));
      return { declination: decl, equation: eqt };
    },
    // convert Gregorian date to Julian day
    // Ref: Astronomical Algorithms by Jean Meeus
    julian: function (year, month, day) {
      if (month <= 2) {
        year -= 1;
        month += 12;
      }
      var A = Math.floor(year / 100);
      var B = 2 - A + Math.floor(A / 4);
      var JD =
        Math.floor(365.25 * (year + 4716)) +
        Math.floor(30.6001 * (month + 1)) +
        day +
        B -
        1524.5;
      return JD;
    },
    //---------------------- Compute Prayer Times -----------------------
    // compute prayer times at given julian date
    computePrayerTimes: function (times) {
      times = this.dayPortion(times);
      var params = setting;
      var imsak = this.sunAngleTime(
        this.eval(params.imsak),
        times.imsak,
        "ccw"
      );
      var fajr = this.sunAngleTime(this.eval(params.fajr), times.fajr, "ccw");
      var sunrise = this.sunAngleTime(
        this.riseSetAngle(),
        times.sunrise,
        "ccw"
      );
      var dhuhr = this.midDay(times.dhuhr);
      var asr = this.asrTime(this.asrFactor(params.asr), times.asr);
      var sunset = this.sunAngleTime(this.riseSetAngle(), times.sunset);
      var maghrib = this.sunAngleTime(this.eval(params.maghrib), times.maghrib);
      var isha = this.sunAngleTime(this.eval(params.isha), times.isha);
      return {
        imsak: imsak,
        fajr: fajr,
        sunrise: sunrise,
        dhuhr: dhuhr,
        asr: asr,
        sunset: sunset,
        maghrib: maghrib,
        isha: isha,
      };
    },
    // compute prayer times
    computeTimes: function () {
      // default times
      var times = {
        imsak: 5,
        fajr: 5,
        sunrise: 6,
        dhuhr: 12,
        asr: 13,
        sunset: 18,
        maghrib: 18,
        isha: 18,
      };
      // main iterations
      for (var i = 1; i <= numIterations; i++)
        times = this.computePrayerTimes(times);
      times = this.adjustTimes(times);
      // add midnight time
      times.midnight =
        setting.midnight == "Jafari"
          ? times.sunset + this.timeDiff(times.sunset, times.fajr) / 2
          : times.sunset + this.timeDiff(times.sunset, times.sunrise) / 2;
      times = this.tuneTimes(times);
      return this.modifyFormats(times);
    },
    // adjust times
    adjustTimes: function (times) {
      var params = setting;
      for (var i in times) times[i] += timeZone - lng / 15;
      if (params.highLats != "None") times = this.adjustHighLats(times);
      if (this.isMin(params.imsak))
        times.imsak = times.fajr - this.eval(params.imsak) / 60;
      if (this.isMin(params.maghrib))
        times.maghrib = times.sunset + this.eval(params.maghrib) / 60;
      if (this.isMin(params.isha))
        times.isha = times.maghrib + this.eval(params.isha) / 60;
      times.dhuhr += this.eval(params.dhuhr) / 60;
      return times;
    },
    // get asr shadow factor
    asrFactor: function (asrParam) {
      var factor = { Standard: 1, Hanafi: 2 }[asrParam];
      return factor || this.eval(asrParam);
    },
    // return sun angle for sunset/sunrise
    riseSetAngle: function () {
      //var earthRad = 6371009; // in meters
      //var angle = DMath.arccos(earthRad/(earthRad+ elv));
      var angle = 0.0347 * Math.sqrt(elv); // an approximation
      return 0.833 + angle;
    },
    // apply offsets to the times
    tuneTimes: function (times) {
      for (var i in times) times[i] += offset[i] / 60;
      return times;
    },
    // convert times to given time format
    modifyFormats: function (times) {
      for (var i in times)
        times[i] = this.getFormattedTime(times[i], timeFormat);
      return times;
    },
    // adjust times for locations in higher latitudes
    adjustHighLats: function (times) {
      var params = setting;
      var nightTime = this.timeDiff(times.sunset, times.sunrise);
      times.imsak = this.adjustHLTime(
        times.imsak,
        times.sunrise,
        this.eval(params.imsak),
        nightTime,
        "ccw"
      );
      times.fajr = this.adjustHLTime(
        times.fajr,
        times.sunrise,
        this.eval(params.fajr),
        nightTime,
        "ccw"
      );
      times.isha = this.adjustHLTime(
        times.isha,
        times.sunset,
        this.eval(params.isha),
        nightTime
      );
      times.maghrib = this.adjustHLTime(
        times.maghrib,
        times.sunset,
        this.eval(params.maghrib),
        nightTime
      );
      return times;
    },
    // adjust a time for higher latitudes
    adjustHLTime: function (time, base, angle, night, direction) {
      var portion = this.nightPortion(angle, night);
      var timeDiff =
        direction == "ccw"
          ? this.timeDiff(time, base)
          : this.timeDiff(base, time);
      if (isNaN(time) || timeDiff > portion)
        time = base + (direction == "ccw" ? -portion : portion);
      return time;
    },
    // the night portion used for adjusting times in higher latitudes
    nightPortion: function (angle, night) {
      var method = setting.highLats;
      var portion = 1 / 2; // MidNight
      if (method == "AngleBased") portion = (1 / 60) * angle;
      if (method == "OneSeventh") portion = 1 / 7;
      return portion * night;
    },
    // convert hours to day portions
    dayPortion: function (times) {
      for (var i in times) times[i] /= 24;
      return times;
    },
    //---------------------- Time Zone Functions -----------------------
    // get local time zone
    getTimeZone: function (date) {
      var year = date[0];
      var t1 = this.gmtOffset([year, 0, 1]);
      var t2 = this.gmtOffset([year, 6, 1]);
      return Math.min(t1, t2);
    },
    // get daylight saving for a given date
    getDst: function (date) {
      return 1 * (this.gmtOffset(date) != this.getTimeZone(date));
    },
    // GMT offset for a given date
    gmtOffset: function (date) {
      var localDate = new Date(date[0], date[1] - 1, date[2], 12, 0, 0, 0);
      var GMTString = localDate.toGMTString();
      var GMTDate = new Date(
        GMTString.substring(0, GMTString.lastIndexOf(" ") - 1)
      );
      var hoursDiff = (localDate - GMTDate) / (1000 * 60 * 60);
      return hoursDiff;
    },
    //---------------------- Misc Functions -----------------------
    // convert given string into a number
    eval: function (str) {
      return 1 * (str + "").split(/[^0-9.+-]/)[0];
    },
    // detect if input contains 'min'
    isMin: function (arg) {
      return (arg + "").indexOf("min") != -1;
    },
    // compute the difference between two times
    timeDiff: function (time1, time2) {
      return DMath.fixHour(time2 - time1);
    },
    // add a leading 0 if necessary
    twoDigitsFormat: function (num) {
      return num < 10 ? "0" + num : num;
    },
  };
}
//---------------------- Degree-Based Math Class -----------------------
var DMath = {
  dtr: function (d) {
    return (d * Math.PI) / 180.0;
  },
  rtd: function (r) {
    return (r * 180.0) / Math.PI;
  },
  sin: function (d) {
    return Math.sin(this.dtr(d));
  },
  cos: function (d) {
    return Math.cos(this.dtr(d));
  },
  tan: function (d) {
    return Math.tan(this.dtr(d));
  },
  arcsin: function (d) {
    return this.rtd(Math.asin(d));
  },
  arccos: function (d) {
    return this.rtd(Math.acos(d));
  },
  arctan: function (d) {
    return this.rtd(Math.atan(d));
  },
  arccot: function (x) {
    return this.rtd(Math.atan(1 / x));
  },
  arctan2: function (y, x) {
    return this.rtd(Math.atan2(y, x));
  },
  fixAngle: function (a) {
    return this.fix(a, 360);
  },
  fixHour: function (a) {
    return this.fix(a, 24);
  },
  fix: function (a, b) {
    a = a - b * Math.floor(a / b);
    return a < 0 ? a + b : a;
  },
};
//---------------------- Init Object -----------------------
var prayTimes = new PrayTimes();
export default prayTimes;
================================================

File: ramadhanTime.js
================================================
import prayTimes from "./prayTimes.js";
import config from "./config.js";
// DateTime
// Clock
const currentTime = () => {
  const date = new Date();
  const hours = addZero(date.getHours());
  const minutes = addZero(date.getMinutes());
  const seconds = addZero(date.getSeconds());
  document.querySelector(
    ".clock"
  ).innerText = `${hours} : ${minutes} : ${seconds}`;
  setTimeout(() => {
    currentTime();
  }, 1000);
};
const addZero = (time) => {
  return time < 10 ? `0${time}` : time;
};
const currentDate = () => {
  document.querySelector(".date").innerText = new Intl.DateTimeFormat("id-ID", {
    dateStyle: "full",
  }).format(new Date());
};
// Pray Time
prayTimes.adjust({ imsak: "10 min", fajr: 20, asr: "Standard", isha: 18 });
prayTimes.tune({
  imsak: 2.5,
  fajr: 2.5,
  dhuhr: 3.5,
  asr: 2,
  maghrib: 3.5,
  isha: 2.5,
});
const prayTimesResult = prayTimes.getTimes(new Date(), [
  config.prayTime.latitude || -6.1783056,
  config.prayTime.longtitude || 106.6318889,
]);
const insertPrayerTime = () => {
  document.querySelectorAll(".prayerTime > div").forEach((e) => {
    e.children[1].innerHTML = prayTimesResult[e.id];
  });
};
currentDate();
currentTime();
insertPrayerTime();
================================================

File: login.html
================================================
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#06f" />
    <link rel="shortcut icon" href="./favicon.ico" />
    <link rel="stylesheet" href="css/style.css" />
    <title>Hotspot | Login</title>
  </head>
  <body>
    $(if chap-id)
    <form name="sendin" action="$(link-login-only)" method="post">
      <input type="hidden" name="username" />
      <input type="hidden" name="password" />
      <input type="hidden" name="dst" value="$(link-orig)" />
      <input type="hidden" name="popup" value="true" />
    </form>
    <script src="/md5.js"></script>
    <script>
      function doLogin() {
        document.sendin.username.value = document.login.username.value;
        document.sendin.password.value = hexMD5(
          "$(chap-id)" + document.login.password.value + "$(chap-challenge)"
        );
        document.sendin.submit();
        return false;
      }
    </script>
    $(endif)
    <!-- prettier-ignore -->
    <div class="container">
      <div class="wrapper">
        <div class="box">
          <br><br>
          <div class="imageHeader">
            <img width="inherit" src="./img/banner.png" />
          </div>
          <div class="dateTimeWrapper">
            <div class="date"></div>
            <div class="clock"></div>
          </div>
          <!-- <div class="prayerTime">
            <div class="imsak" id="imsak">
              <p><strong>Imsak</strong></p>
              <p>00:00</p>
            </div>
            <div class="subuh" id="fajr">
              <p><strong>Subuh</strong></p>
              <p>00:00</p>
            </div>
            <div class="zuhur" id="dhuhr">
              <p><strong>Zuhur</strong></p>
              <p>00:00</p>
            </div>
            <div class="asar" id="asr">
              <p><strong>Asar</strong></p>
              <p>00:00</p>
            </div>
            <div class="magrib" id="maghrib">
              <p><strong>Magrib</strong></p>
              <p>00:00</p>
            </div>
            <div class="isya" id="isha">
              <p><strong>Isya</strong></p>
              <p>00:00</p>
            </div>
          </div> -->
          <div class="login-method">
            <ul>
              <li id="member" class="login-method-menu ">Member</li>
              <li id='voucher' class="login-method-menu" >Voucher</li>
              <li id='qrCode' class="login-method-menu" >QR Code</li>
            </ul>
          </div>
          <form
            action="$(link-login-only)"
            autocomplete="off"
            method="POST"
            name="login"
            $(if chap-id)
            onSubmit="return doLogin()"
            $(endif)
            >
            <input type="hidden" name="dst" value="$(link-orig)" />
            <input type="hidden" name="popup" value="true" />
            <div id="input-group-username" class="input-group">
              <div class="input-icon">
                <input id="username" class="input" type="text" placeholder="Username" name="username" required/>
                <i class="icon">👨‍💻</i>
              </div>
            </div>
            <div id="input-group-password" class="input-group">
              <div class="input-icon">
                <input id="password" class="input" type="password" placeholder="Password" name="password" />
                <i class="icon">🔑</i>
              </div>
              <a id="showPassword" class="btn btn-show-hide" tabindex="-1">
                <span id="showPasswordText" >Show</span>
              </a>
            </div>
            <!-- <p id="qrCodeInfo" style="text-align: center; display: none;">Untuk masuk melalui QR Code, <a id="qrCodeScannerURL" href="">klik disini</a></p> -->
            <p id="qrCodeInfo" style="text-align: center; display: none;">Untuk masuk melalui QR Code, Silakan buka aplikasi scanner di Smartphone Anda</p>
            $(if error)
              <p class="error">$(error)</p>
            $(endif)
            <button class="btn btn-primary" type="submit"><span>Login</span></button>
          </form>
          <div class="form-footer">
            <!-- $(if trial == 'yes')
              <p style="margin-bottom: 15px;">Mau beli tapi masih ragu? <a href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">Coba GRATIS!</a></p>
            $(endif) -->
            <p class="copy-right">Powered By <a target="_blank" href="https://sman3banjar.sch.id">Team IT SMAN 3 Banjar</a></p>
          </div>
        </div>
      </div>
    </div>
    <script type="module" src="./js/loginScript.js"></script>
    <script type="module" src="./js/ramadhanTime.js"></script>
  </body>
</html>
================================================

File: logout.html
================================================
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="expires" content="-1" />
    <meta name="theme-color" content="#06f" />
    <link rel="shortcut icon" href="./favicon.ico" />
    <link rel="stylesheet" href="css/style.css" />
    <title>Logout | Hotspot</title>
  </head>
  <body>
    <script>
      function openLogin() {
        if (window.name != "hotspot_logout") return true;
        open("$(link-login)", "_blank", "");
        window.close();
        return false;
      }
    </script>
    <div class="container">
      <div class="wrapper">
        <div class="box">
          <br><br>
          <div class="imageHeader">
            <img width="inherit" src="./img/banner.png" />
          </div>
          <div class="dateTimeWrapper">
            <div class="date"></div>
            <div class="clock"></div>
          </div>
          <!-- <div class="prayerTime">
            <div class="imsak" id="imsak">
              <p><strong>Imsak</strong></p>
              <p>00:00</p>
            </div>
            <div class="subuh" id="fajr">
              <p><strong>Subuh</strong></p>
              <p>00:00</p>
            </div>
            <div class="zuhur" id="dhuhr">
              <p><strong>Zuhur</strong></p>
              <p>00:00</p>
            </div>
            <div class="asar" id="asr">
              <p><strong>Asar</strong></p>
              <p>00:00</p>
            </div>
            <div class="magrib" id="maghrib">
              <p><strong>Magrib</strong></p>
              <p>00:00</p>
            </div>
            <div class="isya" id="isha">
              <p><strong>Isya</strong></p>
              <p>00:00</p>
            </div>
          </div> -->
          <div class="title-wrapper">
            <h1>Anda Baru Saja Keluar!</h1>
            <p>Informasi/status voucher <strong>$(username)</strong>.</p>
          </div>
          <table>
            <tr>
              <th>IP Address:</th>
              <td>$(ip)</td>
            </tr>
            <tr>
              <th>MAC Address:</th>
              <td>$(mac)</td>
            </tr>
            <tr>
              <th>Bytes U/D:</th>
              <td>$(bytes-in-nice) / $(bytes-out-nice)</td>
            </tr>
            $(if session-time-left)
            <tr>
              <th>Uptime / Left:</th>
              <td>$(uptime) / $(session-time-left)</td>
            </tr>
            $(else)
            <tr>
              <th>Uptime:</th>
              <td>$(uptime)</td>
            </tr>
            $(endif)
            <!-- prettier-ignore -->
            $(if remain-bytes-total)
            <tr>
              <th>Sisa kuota:</th>
              <td>$(remain-bytes-total)</td>
            </tr>
            $(endif)
          </table>
          <!-- prettier-ignore -->
          <form
            action="$(link-login)"
            autocomplete="off"
            method="POST"
            name="login"
            onSubmit="return openLogin()"
            >
            <button class="btn btn-primary" type="submit"><span>Login</span></button>
          </form>
          <div class="form-footer">
            <p class="copy-right">Powered By <a target="_blank" href="https://sman3banjar.sch.id">Team IT SMAN 3 Banjar</a></p>
          </div>
        </div>
      </div>
    </div>
    <script type="module" src="./js/ramadhanTime.js"></script>
    <script>
      document.title = `Logout | ${window.location.hostname}`;
    </script>
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
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta http-equiv="refresh" content="2; url=$(link-orig)" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="shortcut icon" href="./favicon.ico" />
    <meta http-equiv="expires" content="-1" />
    <title>Ads | Hotspot</title>
    <style>
      textarea,
      input,
      select {
        background-color: #fdfbfb;
        border: 1px #bbbbbb solid;
        padding: 2px;
        margin: 1px;
        font-size: 14px;
        color: #808080;
      }
      body {
        color: #737373;
        font-size: 12px;
        font-family: verdana;
      }
      a,
      a:link,
      a:visited,
      a:active {
        color: #aaaaaa;
        text-decoration: none;
        font-size: 12px;
      }
      a:hover {
        border-bottom: 1px dotted #c1c1c1;
        color: #aaaaaa;
      }
      img {
        border: none;
      }
      td {
        font-size: 12px;
        color: #7a7a7a;
      }
    </style>
    <script>
      var popup = "";
      function openOrig() {
        if (window.focus) popup.focus();
        location.href = unescape("$(link-orig-esc)");
      }
      function openAd() {
        location.href = unescape("$(link-redirect-esc)");
      }
      function openAdvert() {
        if (window.name != "hotspot_advert") {
          popup = open("$(link-redirect)", "hotspot_advert", "");
          setTimeout("openOrig()", 1000);
          return;
        }
        setTimeout("openAd()", 1000);
      }
    </script>
  </head>
  <body onLoad="openAdvert()">
    <table width="100%" height="100%">
      <tr>
        <td align="center" valign="middle">
          Iklan.
          <br /><br />
          If nothing happens, open
          <a href="$(link-redirect)" target="hotspot_advert">advertisement</a>
          manually.
        </td>
      </tr>
    </table>
  </body>
</html>
================================================

File: redirect.html
================================================
<!-- prettier-ignore -->
$(if http-status == 302)Hotspot redirect$(endif)
$(if http-header == "Location")$(link-redirect)$(endif)
<html>
  <head>
    <title>...</title>
    <meta http-equiv="refresh" content="0; url=$(link-redirect)" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="expires" content="-1" />
  </head>
  <body></body>
</html>
================================================

File: rlogin.html
================================================
<!-- prettier-ignore -->
$(if http-status == 302)Hotspot login required$(endif)
$(if http-header == "Location")$(link-redirect)$(endif)
<html>
  <head>
    <title>...</title>
    <meta http-equiv="refresh" content="0; url=$(link-redirect)" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="expires" content="-1" />
  </head>
  <body></body>
</html>
================================================

File: status.html
================================================
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#06f" />
    <meta http-equiv="expires" content="-1">
    <link rel="shortcut icon" href="./favicon.ico" />
    <link rel="stylesheet" href="css/style.css" />
    <title>Status | Hotspot</title>
    $(if refresh-timeout)
    <meta http-equiv="refresh" content="$(refresh-timeout-secs)" />
    $(endif)
  </head>
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
  <body 
    $(if advert-pending == 'yes')	
      onLoad="openAdvert()"
    $(endif) >
    <div class="container">
      <div class="wrapper">
        <div class="box">
          <br><br>
          <div class="imageHeader">
            <img width="inherit" src="./img/banner.png" />
          </div>
          <div class="dateTimeWrapper">
            <div class="date"></div>
            <div class="clock"></div>
          </div>
          <!-- <div class="prayerTime">
            <div class="imsak" id="imsak">
              <p><strong>Imsak</strong></p>
              <p>00:00</p>
            </div>
            <div class="subuh" id="fajr">
              <p><strong>Subuh</strong></p>
              <p>00:00</p>
            </div>
            <div class="zuhur" id="dhuhr">
              <p><strong>Zuhur</strong></p>
              <p>00:00</p>
            </div>
            <div class="asar" id="asr">
              <p><strong>Asar</strong></p>
              <p>00:00</p>
            </div>
            <div class="magrib" id="maghrib">
              <p><strong>Magrib</strong></p>
              <p>00:00</p>
            </div>
            <div class="isya" id="isha">
              <p><strong>Isya</strong></p>
              <p>00:00</p>
            </div>
          </div> -->
          <div class="title-wrapper">
            <h1>Status</h1>
             <!-- prettier-ignore -->
            <p>Informasi/status voucher <strong>$(if login-by == 'trial')Trial$(elif login-by != 'mac')$(username)$(endif)</strong>.</p>
          </div> 
          <table>
            <tr>
              <th>IP Address:</th>
              <td>$(ip)</td> 
            </tr>
            <tr>
              <th>Bytes U/D:</th>
              <td>$(bytes-in-nice) / $(bytes-out-nice)</td> 
            </tr>
            $(if session-time-left)
            <tr>
              <th>Uptime / Left:</th>
              <td>$(uptime) / $(session-time-left)</td> 
            </tr>
            $(else)
            <tr>
              <th>Uptime:</th>
              <td>$(uptime)</td> 
            </tr>
            $(endif)
            $(if blocked == 'yes')
            <tr>
              <th>Status: </th>
              <td><a href="$(link-advert)" target="hotspot_advert">advertisement</a> required</td> 
            </tr>
            $(elif refresh-timeout)
            <tr>
              <th>Refresh:</th>
              <td>$(refresh-timeout)</td>
            </tr>
            $(endif)
            <tr id="expiredRow">
              <th>Expired:</th>
              <td id="expired"></td>
            </tr>
          </table>
          $(if login-by-mac != 'yes')
          <form 
            action="$(link-logout)" 
            name="logout" 
            onSubmit="return openLogout()">
            <button class="btn btn-primary" type="submit"><span>Logout</span></button>
          </form>
          $(endif)
          <div class="form-footer">
            <p class="copy-right">Powered By <a target="_blank" href="https://sman3banjar.sch.id">Team IT SMAN 3 Banjar</a></p>
          </div>
        </div>
      </div>
    </div>
    <script type="module" src="./js/ramadhanTime.js"></script>
    <script type="module">
      import config from './js/config.js';
      document.title = `Status | ${window.location.hostname}`;
      if(config.expiredChecker.active) {
        const expiredTable = document.getElementById('expired');
        expiredTable.insertAdjacentHTML('afterbegin', '<div class="spinner"><div class="bounce1"></div><div class="bounce2"></div><div class="bounce3"></div></div>')
        fetch(`${config.expiredChecker.URL}/$(username)`, { 
          method: 'POST', 
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({token: config.expiredChecker.token})
        })
        .then(response => {
          if(response.ok) {
            return response.json();
          } else {
            throw new Error(response.statusText);
          }
        })
        .then(result=> {
          const { comment } = result.data;
          const expiredTime = (comment.match(/[\/]/g) || []).length === 2 ? comment : '-';
          expiredTable.innerHTML = expiredTime;
        })
        .catch(error => {
          expiredTable.innerHTML = error.message;
        })      
      } else {
        document.getElementById('expiredRow').style.display = 'none'
      }
    </script>
  </body>
</html>
================================================

File: success.html
================================================
<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="shortcut icon" href="./favicon.ico" />
    <link rel="stylesheet" href="css/style.css" />
    <meta name="theme-color" content="#06f" />
    <title>Success | Hotspot</title>
    $(if refresh-timeout)
    <script>
      setTimeout(function () {
        location.href = "$(link-status)";
      }, 3000);
    </script>
    $(endif)
  </head>
  <body>
    <div class="container">
      <div class="wrapper">
        <div class="box">
          <br><br>
          <div class="imageHeader">
            <img width="inherit" src="./img/banner.png" />
          </div>
          <div class="title-wrapper">
            $(if login-by == 'trial')
            <h1>Welcome Trial User!</h1>
            $(elif login-by != 'mac')
            <h1>Welcome $(username)!</h1>
            $(endif)
            <p>
              Anda berhasil terhubung, kunjungi
              <a href="$(link-status)">halaman status</a>
            </p>
            .
          </div>
          <div class="form-footer">
            <p class="copy-right">Powered By <a target="_blank" href="https://sman3banjar.sch.id">Team IT SMAN 3 Banjar</a></p>
          </div>
        </div>
      </div>
    </div>
    <script>
      document.title = `Success | ${window.location.hostname}`;
    </script>
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
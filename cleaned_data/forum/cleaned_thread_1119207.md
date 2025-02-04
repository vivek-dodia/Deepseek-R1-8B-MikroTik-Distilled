# Thread Information
Title: Thread-1119207
Section: RouterOS
Thread ID: 1119207

# Discussion

## Initial Question
Hi everyone, I created a self-registration page at the mikrotik hotspot. The page displays correctly but submitting doesn't work.The purpose is to send the username without password and from the failed login via script to perform self-registration.If I only enter the username and click on submit from the login page, the login fails. while from the registration page no.I attach the registration page.
```
<!doctype html><htmllang="en"><head><metacharset="utf-8"><metahttp-equiv="pragma"content="no-cache"/><metahttp-equiv="expires"content="-1"/><metaname="viewport"content="width=device-width, initial-scale=1.0"/><title>Internet hotspot - Log in</title><linkrel="stylesheet"href="css/style.css"></head><body><!-- two other colors

<body class="lite">
<body class="dark">

-->$(if chap-id)<formname="sendin"action="$(link-login-only)"method="post"style="display:none"><inputtype="hidden"name="username"/><inputtype="hidden"name="password"/><inputtype="hidden"name="number"/><inputtype="hidden"name="dst"value="http://green.hotspot/policy.html"/><inputtype="hidden"name="popup"value="true"/></form><scriptsrc="/md5.js"></script><script>functiondoLogin(){document.sendin.username.value=document.login.username.value;document.sendin.password.value=hexMD5('$(chap-id)'+document.login.password.value+'$(chap-challenge)');document.sendin.submit();returnfalse;}</script>$(endif)<divclass="ie-fixMinHeight"><divclass="main"><divclass="wrap animated fadeIn"><formname="login"action="$(link-login-only)"method="post"$(ifchap-id)onSubmit="returndoLogin()"$(endif)><inputtype="hidden"name="dst"value="$(link-orig)"/><inputtype="hidden"name="popup"value="true"/><divstyle="margin:0px"><imgsrc="img/green-logo.png"alt=""width="280px"><pclass="info $(if error)alert$(endif)">$(if error == "")Inserisci il tuo indirizzo mail per eseguire la Registrazione. Riceverai una email con le credenziali di accesso. $(if trial == 'yes')<br/>Free trial available,<ahref="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">click here</a>.$(endif)
                        $(endif)
    
                        $(if error)$(error)$(endif)</p><label><imgclass="ico"src="img/email.svg"alt="#"/><inputname="Email"type="email"value="$(username)"placeholder="Email"/></label><inputtype="checkbox"value="checkbox"name="checkbox"checked="checked"id="checkbox"><labelfor="checkbox">Accetto le condizioni generali</label><ahref="http://green.hotspot/policy.html"style="color:rgb(57,186,143);text-align:center"target="_blank"rel="noopener noreferrer">Condizioni Generali</a><br><br></p><inputtype="submit"value="Registrati"/><br><br></p><pclass="info bt1">Torna alla pagina del<ahref="http://green.hotspot/login.html"style="color:rgb(57,186,143);text-align:center"target="_blank"rel="noopener noreferrer">Login</a><br><formaction=""></form><br><br><br><br></p><ahref="https://foisfabio.it/"style="color:rgb(57,186,143);text-align:center"target="_blank"rel="noopener noreferrer">Powered by foisfabio.it</a></p></div></div></div></body></html>

---
```

## Response 1
https://codepen.io/abbio90/pen/eYorvPj ---

## Response 2
Resolved ---

## Response 3
Hi abbio90, could you please share how you created self-registration for mikrotik hotspot please?Thanks! ---
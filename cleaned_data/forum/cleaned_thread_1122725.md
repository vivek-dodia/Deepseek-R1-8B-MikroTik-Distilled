# Thread Information
Title: Thread-1122725
Section: RouterOS
Thread ID: 1122725

# Discussion

## Initial Question
After spending hours troubleshooting this, I thought I'd post the solution to save other's time.We recently migrated from on-prem Exchange 2013 to 2019 on WS2019, and ever since our RouterOS v7 stopped sending email with STARTTLS.RouterOS v6 can send email (/tool e-mail) okay using Exchange 2013 & 2019 mail servers.RouterOS v7 could send okay with Exchange 2013, but getting "TLS handshake failed" when using Exchange 2019 mail server.It's nothing to do with TLS version, or Cipher Suites, etc.Exchange Server 2019 has TLS renegotiation strict mode enabled by default, which rejects TLS clients that don't have Security Update MS10-049 RFC5746 installed. This security update was released in 2010.Guntis @ Mikrotik Support mentions on the topic link below "v7 is using our own TLS implementation. v6 is using OpenSSL 1.0.2u."This makes me think that Mikrotik's own TLS implementation is not RFC 5746 compliant, thus Exchange Server 2019 is rejecting RouterOS v7 STARTTLS.The workaround is to run the following PowerShell command on Exchange Server 2019 and reboot the server. However, I wouldn't recommend lifting default security restrictions. So hopefully Mikrotik is working on a fix for a future RouterOS release. The other workaround is to switch to unencrypted SMTP over TCP 25.Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL" -Name "AllowInsecureRenegoClients" -Value 1 -Type DWordviewtopic.php?t=190522Microsoft article on TLS renegotiation strict modehttps://learn.microsoft.com/en-us/excha ... trict-mode ---

## Response 1
Thanks a lot for the heads-up. I am suffering that exact problem (SUP-172632). ---

## Response 2
Thanks a lot for the heads-up. I am suffering that exact problem (SUP-172632).Did you have a response from Mikrotik support ? ---
# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 169662

# Discussion

## Initial Question
Author: Fri Nov 27, 2020 1:58 pm
``` {:do{/tool fetch url=https://mkcert.org/generate/check-certificate=yes dst-path=cacert.pem;/certificateremove[find];/certificateimportfile-name=cacert.pem passphrase="";/fileremovecacert.pem;:log info("Updated certificate trust store");}on-error={:log error("Failed to update certificate trust store");};} ``` What is the best way to update CA root certs? I am running the script below every 7 days but I wondered if there is a better way to work out if they actually *need* updating before downloading, deleting and replacing certs every week.Also - can running this every week damage flash RAM (or whatever memory is inside it).
```
---
```

## Response 1
Author: Fri Nov 27, 2020 7:10 pm
``` /certificateremove[findwhereauthority expired]; ``` No need to remove all certificates... You could just remove the expired ones to clean up.
```
---
```

## Response 2
Author: Sat Nov 28, 2020 3:31 pm
``` /certificateremove[findwhereauthority expired]; ``` ``` /certificateimportfile-name=cacert.pem passphrase=""; ``` No need to remove all certificates... You could just remove the expired ones to clean up.
```
Thanks - will the certificate import command then only import the new ones or will it write them all again?
```

```
---
```

## Response 3
Author: Sat Nov 28, 2020 3:52 pm
``` {:do{/tool fetch url=https://mkcert.org/generate/check-certificate=yes dst-path=cacert.pem;/certificateremove[findwhereauthority expired];/certificateimportfile-name=cacert.pem passphrase="";/fileremovecacert.pem;:log info("Updated certificate trust store");}on-error={:log error("Failed to update certificate trust store");};} ``` I will run this every 6months then. Is there any way to only import the certs that expired or will this import all and overwrite existing certs?
```
---
```

## Response 4
Author: Thu Jun 13, 2024 2:10 pm
``` {:do{/tool fetch url=https://mkcert.org/generate/check-certificate=yes dst-path=cacert.pem;/certificateremove[findwhereauthority expired];/certificateimportfile-name=cacert.pem passphrase="";/fileremovecacert.pem;:log info("Updated certificate trust store");}on-error={:log error("Failed to update certificate trust store");};} ``` I will run this every 6months then. Is there any way to only import the certs that expired or will this import all and overwrite existing certs?
```
This is perfect, thank you for providing it.


---
```

## Response 5
Author: Thu Jun 13, 2024 9:29 pm
``` {:localretryCount0;:localmaxRetries3;:localsuccessfalse;:do{:while($retryCount<$maxRetries&&!$success)do={:do{/tool fetch url=https://mkcert.org/generate/check-certificate=yes dst-path=cacert.pem;/certificateremove[findwhereauthority expired];/certificateimportfile-name=cacert.pem passphrase="";/fileremovecacert.pem;:log info("Updated certificate trust store");:set$successtrue;}on-error={:set$retryCount($retryCount+1);:log error("Failed to update certificate trust store. Attempt: $retryCount");:delay5s;# Delay before retrying};}:if(!$success)do={/tool e-mail send to="noc@example.io"subject="RouterOS Certificate Update Failed"body="Failed to update the certificate trust store after $maxRetries attempts.";:log error("Failed to update certificate trust store after $maxRetries attempts");}}on-error={:log error("Unexpected error in the update script");};} ``` ``` {:localretryCount0;:localmaxRetries3;:localsuccessfalse;:do{:while($retryCount<$maxRetries&&!$success)do={:do{/tool fetch url=https://mkcert.org/generate/all/except/nothing check-certificate=yes dst-path=cacert.pem;:delay15s;# Wait 15 seconds for download/certificateremove[findwherename~"cacert.pem*"expired=yes];/certificateimportfile-name=cacert.pem passphrase="";/fileremovecacert.pem;:log info("Updated certificate trust store");:set$successtrue;}on-error={:set$retryCount($retryCount+1);:log error("Failed to update certificate trust store. Attempt: $retryCount");:delay5s;# Delay before retrying};}:if(!$success)do={/tool e-mail send to="noc@example.io"subject="RouterOS Certificate Update Failed"body="Failed to update the certificate trust store after $maxRetries attempts.";:log error("Failed to update certificate trust store after $maxRetries attempts");}}on-error={:log error("Unexpected error in the update script");};} ``` These were the changes which I did because I found it always failed on first run.This is based off the original code posted by @ilium007, so I made the following changes to make it more reliable.
```
As mentioned, it will fail first time as @rextended noted because the certs gets deleted on first run, so theres a small loop which will try again until sucessful upto maxRetries count and if it still fails, it will send you a mail.---UpdateJust made those changes you spotted, thanks, didnt notice tbh.
```

```
---
```

## Response 6
Author: Thu Jun 13, 2024 10:58 pm
``` /file print file=mkcert.txt :delay 1s set mkcert.txt content="-----BEGIN CERTIFICATE-----\r\ \n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\r\ \n-----END CERTIFICATE-----" :delay 1s /certificate import file-name=mkcert.txt passphrase="" name=imported-ca-cert_mkcert :delay 1s /file remove [find where name=mkcerts.txt] :do { /tool fetch url=https://mkcert.org/generate/all/except/nothing check-certificate=yes dst-path=mkcerts.pem :delay 1s remove [find where name~"imported-ca-cert*" and expired=yes] :delay 1s import file-name=mkcerts.pem passphrase="" name=imported-ca-cert :delay 1s /file remove [find where name=mkcerts.pem] :log info "Trust Store: Certificates update from mkcert.org succeeded" } on-error={ :log error "Trust Store: Unable to update certificates from mkcert.org" } ``` ``` certificates-imported: 147 private-keys-imported: 0 files-imported: 1 decryption-failures: 0 keys-with-no-certificate: 0 ``` Do not worry, is easy...no manual install codeThis work untilMon, 04 Jun 2035 11:04:38 GMT, after that date, the embedded cert (on a new machine) must be updated...And is also possible save ":execute file=result.txt" and send the result.txt file on the email.result.txt example on first run codeAnd is also possible, with scripting, report on log or on mail what and how many certificates deleted (if any), and what and how many certificate added (if any).EDIT:https://forum.mikrotik.com/viewtopic.php?p=1083839#p1083841added backward compatibility for unexpected new behaviour ---

## Response 7
Author: Fri Jun 14, 2024 12:32 am
``` LANG=C date--date="@$(echo '2^31-1' | bc)"TueJan1904:14:07CET2038 ``` ``` LANG=C date--date="@$(echo '2^55+31739239172709231' | bc)"WedDec3123:59:59CET2147485547 ``` 
```
From 2K Y problems to the new dooms day for LinuxDont get it, don't know why they don't goto 64bit
```

```
Sorry to say, I think I am ded at year 2147485547My biggest epoch time supporting my computer now is67768036191673199


---
```

## Response 8
Author: Wed Jun 19, 2024 9:34 am
``` /certificateremove[findwhereakid=""expired]; ``` also this do not work:/certificate remove [ find whereauthorityexpired ];because no one certificate is "authority" (authority is just the machine itself that generate certificates)so that line must be only/certificate remove [find where name~"certs.pem*" expired=yes]Ah, right... But you can identify root certificates by emptyakid. So this should work:
```
---
```

## Response 9
Author: Fri Jan 24, 2025 4:05 pm
``` /file print file=ccadb.txt :delay 1s set ccadb.txt content="-----BEGIN CERTIFICATE-----\r\ \nMIIDrzCCApegAwIBAgIQCDvgVpBCRrGhdWrJWZHHSjANBgkqhkiG9w0BAQUFADBh\r\ \nMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3\r\ \nd3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBD\r\ \nQTAeFw0wNjExMTAwMDAwMDBaFw0zMTExMTAwMDAwMDBaMGExCzAJBgNVBAYTAlVT\r\ \nMRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxGTAXBgNVBAsTEHd3dy5kaWdpY2VydC5j\r\ \nb20xIDAeBgNVBAMTF0RpZ2lDZXJ0IEdsb2JhbCBSb290IENBMIIBIjANBgkqhkiG\r\ \n9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4jvhEXLeqKTTo1eqUKKPC3eQyaKl7hLOllsB\r\ \nCSDMAZOnTjC3U/dDxGkAV53ijSLdhwZAAIEJzs4bg7/fzTtxRuLWZscFs3YnFo97\r\ \nnh6Vfe63SKMI2tavegw5BmV/Sl0fvBf4q77uKNd0f3p4mVmFaG5cIzJLv07A6Fpt\r\ \n43C/dxC//AH2hdmoRBBYMql1GNXRor5H4idq9Joz+EkIYIvUX7Q6hL+hqkpMfT7P\r\ \nT19sdl6gSzeRntwi5m3OFBqOasv+zbMUZBfHWymeMr/y7vrTC0LUq7dBMtoM1O/4\r\ \ngdW7jVg/tRvoSSiicNoxBN33shbyTApOB6jtSj1etX+jkMOvJwIDAQABo2MwYTAO\r\ \nBgNVHQ8BAf8EBAMCAYYwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUA95QNVbR\r\ \nTLtm8KPiGxvDl7I90VUwHwYDVR0jBBgwFoAUA95QNVbRTLtm8KPiGxvDl7I90VUw\r\ \nDQYJKoZIhvcNAQEFBQADggEBAMucN6pIExIK+t1EnE9SsPTfrgT1eXkIoyQY/Esr\r\ \nhMAtudXH/vTBH1jLuG2cenTnmCmrEbXjcKChzUyImZOMkXDiqw8cvpOp/2PV5Adg\r\ \n06O/nVsJ8dWO41P0jmP6P6fbtGbfYmbW0W5BjfIttep3Sp+dWOIrWcBAI+0tKIJF\r\ \nPnlUkiaY4IBIqDfv8NZ5YBberOgOzW6sRBc4L0na4UU+Krk2U886UAb3LujEV0ls\r\ \nYSEY1QSteDwsOoBrp+uvFRTp2InBuThs4pFsiv9kuXclVzDAGySj4dzp30d8tbQk\r\ \nCAUw7C29C79Fv1C5qfPrmAESrciIxpg0X40KPMbp1ZWVbd4=\r\ \n-----END CERTIFICATE-----" :delay 1s /certificate import file-name=ccadb.txt passphrase="" name=imported-ca-cert_ccadb :delay 1s /file remove [find where name=ccadbs.txt] :do { /tool fetch url="https://ccadb.my.salesforce-sites.com/mozilla/IncludedRootsPEMTxt\3FTrustBitsInclude=Websites" \ check-certificate=yes dst-path=ccadbs.pem :delay 1s remove [find where name~"imported-ca-cert*" and expired=yes] import file-name=ccadbs.pem passphrase="" name=imported-ca-cert :delay 1s /file remove [find where name=ccadbs.pem] :delay 1s :log info "Trust Store: Certificates update from ccadb.org succeeded" } on-error={ :log error "Trust Store: Unable to update certificates from ccadb.org" } ``` ``` certificates-imported: 1 private-keys-imported: 0 files-imported: 1 decryption-failures: 0 keys-with-no-certificate: 0 status: finished downloaded: 219KiB total: 0KiB duration: 1s certificates-imported: 148 private-keys-imported: 0 files-imported: 1 decryption-failures: 0 keys-with-no-certificate: 0 ``` New for Mozilla https://www.ccadb.org( https://ccadb.my.salesforce-sites.com/mozilla/IncludedRootsPEMTxt?TrustBitsInclude=Websites )ccadb install coderesult on first run codeThe db actually have 149 certs, but the first is already on script for prevent man in the middle attack.The syntax is compatible for both v6 and v7, is why some "file" instructions are not used.